#!/usr/bin/env python3
"""遍历 sources.json，抓取每个交易所的 changelog 并生成 latest-diff.md。

设计目标：
- 单文件、零外部依赖（只用标准库），方便在 GitHub Actions 中运行。
- 抓取后把 HTML 简单清洗（剔除 <script>/<style>/标签）再保存到 changelogs/<key>.txt，
  这样 git diff 就能反映"语义"变更，而不会被压缩 JS/CSS 的换行抖动污染。
- 通过 git diff 判断是否有变化，并把每个有变化的来源汇总到 latest-diff.md。
- latest-diff.md 始终被覆盖写入；如果当天没有变更，写入 "No changes on YYYY-MM-DD"。
  Dify workflow 只要读这一份文件即可决定是否推送。

退出码恒为 0；抓取失败的来源会被记录到 fetch-errors.log，但不会让 Action 失败，
避免一家挂掉就阻塞所有人。
"""
from __future__ import annotations

import json
import re
import ssl
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES_FILE = ROOT / "sources.json"
CHANGELOG_DIR = ROOT / "changelogs"
DIFF_FILE = ROOT / "latest-diff.md"
ERROR_LOG = ROOT / "fetch-errors.log"

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36 "
    "blofin-changelog-mirror/1.0"
)
TIMEOUT = 60
MAX_DIFF_LINES_PER_SOURCE = 200  # latest-diff.md 单条目最多保留多少行 diff，防止刷屏

COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
# Docusaurus / readme.io 等文档站的固定噪声块：导航条、侧边栏目录、SDK 推广、页脚 footer。
# 这些每次发版都会变（菜单顺序、SDK 列表），但与 API 文档实质内容无关，必须先剔除再 diff。
TOC_BLOCK_RE = re.compile(
    r"<(?:ul|div|nav)\b[^>]*class\s*=\s*[\"'][^\"']*"
    r"(?:table-of-contents|tocSection|theme-doc-toc|on-this-page|right-side|sidebar)"
    r"[^\"']*[\"'][^>]*>.*?</(?:ul|div|nav)>",
    re.DOTALL | re.IGNORECASE,
)
# 默认主体抽取顺序：<article> → Docusaurus markdown 容器 → <main>。
# sources.json 可通过 `content_class_re` 字段为 OKX/Gate 等无 main/article 的站点指定精确抽取。
DEFAULT_MAIN_PATTERNS = [
    re.compile(r"<article\b[^>]*>(.*?)</article>", re.DOTALL | re.IGNORECASE),
    re.compile(
        r"<div\b[^>]*class\s*=\s*[\"'][^\"']*"
        r"(?:theme-doc-markdown|docMainContainer)"
        r"[^\"']*[\"'][^>]*>(.*?)</div>\s*</main>",
        re.DOTALL | re.IGNORECASE,
    ),
    re.compile(r"<main\b[^>]*>(.*?)</main>", re.DOTALL | re.IGNORECASE),
]
INTRA_LINE_WS_RE = re.compile(r"[ \t]+")
BLANK_RE = re.compile(r"\n{3,}")
INTRA_DATA_WS_RE = re.compile(r"[ \t\r\n]+")

# 在 HtmlToText 中区分标签语义：
# - SKIP_TAGS：标签 + 内容整体丢弃（脚本/样式/噪声块）
# - BLOCK_TAGS：开/闭合时换行（段落、标题、表格行）
# - 其他默认 inline，文本直接拼接（保证 inline <code>/<a>/<span> 不会打断一行）
SKIP_TAGS = {
    "script", "style", "noscript", "svg", "template", "iframe",
    "nav", "aside", "header", "footer", "form",
}
BLOCK_TAGS = {
    "p", "div", "section", "article", "main",
    "h1", "h2", "h3", "h4", "h5", "h6",
    "pre", "blockquote", "hr",
    "tr", "thead", "tbody", "tfoot", "table", "figure", "figcaption",
    "details", "summary",
}


def log_error(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)
    with ERROR_LOG.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")


def fetch(url: str) -> str:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8",
        "Accept-Encoding": "identity",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
    })
    with urllib.request.urlopen(req, context=ctx, timeout=TIMEOUT) as resp:
        raw = resp.read()
        encoding = resp.headers.get_content_charset() or "utf-8"
        return raw.decode(encoding, errors="replace")


def _extract_balanced_div(html_text: str, class_re: re.Pattern) -> str | None:
    """从 html_text 中找到 class 匹配 class_re 的第一个 <div>，返回其完整内层 HTML。

    用栈做配对，正确处理嵌套 <div>，避免被首个 </div> 提前截断。找不到返回 None。
    """
    open_re = re.compile(r"<div\b([^>]*)>", re.IGNORECASE)
    close_re = re.compile(r"</div\s*>", re.IGNORECASE)
    pos = 0
    while True:
        m = open_re.search(html_text, pos)
        if not m:
            return None
        attrs = m.group(1)
        cls_m = re.search(r"class\s*=\s*[\"']([^\"']+)[\"']", attrs)
        pos = m.end()
        if not cls_m or not class_re.search(cls_m.group(1)):
            continue
        depth = 1
        cur = pos
        while depth > 0:
            nxt_open = open_re.search(html_text, cur)
            nxt_close = close_re.search(html_text, cur)
            if not nxt_close:
                return html_text[pos:]
            if nxt_open and nxt_open.start() < nxt_close.start():
                depth += 1
                cur = nxt_open.end()
            else:
                depth -= 1
                if depth == 0:
                    return html_text[pos:nxt_close.start()]
                cur = nxt_close.end()


def extract_main(html_text: str, content_class_re: str | None) -> str:
    """尝试只保留 HTML 主体内容区，剔除导航/侧边栏/footer 等装饰元素。

    优先用 source 配置的 content_class_re（针对 OKX/Gate 这种无 main/article 的站点），
    其次走默认链：<article> → Docusaurus markdown 容器 → <main>。
    都没命中则原样返回（少数小站点没有语义标签）。
    """
    if content_class_re:
        body = _extract_balanced_div(html_text, re.compile(content_class_re, re.IGNORECASE))
        if body:
            return body
    for pat in DEFAULT_MAIN_PATTERNS:
        m = pat.search(html_text)
        if m:
            return m.group(1) if m.groups() else m.group(0)
    return html_text


class HtmlToText(HTMLParser):
    """把 HTML 转成保留语义层次（标题、段落、嵌套列表）的纯文本。

    设计要点：
    - SKIP_TAGS：标签 + 内容整体丢弃。
    - <ul>/<ol>：进入时 list_depth+=1，退出时 -=1。
    - <li>：根据 list_depth 输出 `(depth-1)*"  " + "- "` 的缩进项，模仿 markdown
      bullet（保留 Binance Derivatives 这种 "Portfolio Margin Pro → User Data Stream
      → Add new event ..." 的两级嵌套结构）。
    - BLOCK_TAGS：开/闭合时换行；其他标签当作 inline，文本流过即可。
    - 文本中的连续空白先压缩成单空格，最后再做整体的多空行合并。
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip_depth = 0
        self.list_depth = 0
        self._last_was_newline = True  # 控制不必要的空行/前导换行
        # 刚开了一个 <li> 但还没写过内容时为 True：此时若紧接着出现块元素（<p>/<div>/...）
        # 就吞掉它的换行，避免出现孤立的 "-" + 内容另起一行的情况。
        self._li_pending = False

    def _emit(self, s: str) -> None:
        if not s:
            return
        if s == "\n":
            if self._last_was_newline:
                return
            self.parts.append("\n")
            self._last_was_newline = True
        else:
            self.parts.append(s)
            self._last_was_newline = s.endswith("\n")

    def handle_starttag(self, tag: str, attrs):
        if tag in SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth > 0:
            return
        if tag in ("ul", "ol"):
            self._emit("\n")
            self.list_depth += 1
        elif tag == "li":
            self._emit("\n")
            indent = "  " * max(self.list_depth - 1, 0)
            self.parts.append(indent + "- ")
            self._last_was_newline = False
            self._li_pending = True
        elif tag == "br":
            self._emit("\n")
        elif tag in ("td", "th"):
            # 表格单元格用 " | " 分隔，渲染成 markdown 风格的表格行（KuCoin 文档大量用 <table>）
            if not self._last_was_newline:
                if self.parts and not self.parts[-1].endswith(" "):
                    self.parts.append(" ")
                self.parts.append("| ")
            else:
                self.parts.append("| ")
                self._last_was_newline = False
        elif tag in BLOCK_TAGS:
            if self._li_pending:
                # 吞掉紧跟在 <li> 后的块级换行，让 bullet 与首段文字保持同一行
                return
            self._emit("\n")

    def handle_endtag(self, tag: str):
        if tag in SKIP_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth > 0:
            return
        if tag in ("ul", "ol"):
            self.list_depth = max(0, self.list_depth - 1)
            self._emit("\n")
            self._li_pending = False
        elif tag == "li":
            self._emit("\n")
            self._li_pending = False
        elif tag in BLOCK_TAGS:
            self._emit("\n")

    def handle_startendtag(self, tag: str, attrs):
        if tag == "br":
            self._emit("\n")

    def handle_data(self, data: str):
        if self.skip_depth > 0:
            return
        cleaned = INTRA_DATA_WS_RE.sub(" ", data)
        if cleaned and cleaned != " ":
            self.parts.append(cleaned)
            self._last_was_newline = False
            if cleaned.strip():
                self._li_pending = False
        elif cleaned == " " and not self._last_was_newline and self.parts and not self.parts[-1].endswith(" "):
            self.parts.append(" ")

    def get_text(self) -> str:
        return "".join(self.parts)


def html_to_text(html_text: str) -> str:
    parser = HtmlToText()
    parser.feed(html_text)
    parser.close()
    return parser.get_text()


def normalize(content: str, url: str, content_class_re: str | None = None) -> str:
    """把 HTML 抓取结果清洗成可对比的纯文本。Markdown / yaml 直接保留。

    清洗顺序：
    1. 先 strip 注释（HTMLParser 内部也能处理但提前删掉省事）
    2. 抽主体内容区（避免把侧边栏/导航/footer 带进来）
    3. 剔除主体内的 ToC / on-this-page 侧边目录
    4. 用 HtmlToText 解析剩余 HTML，保留段落 + 嵌套列表层次
    5. 合并多余空白
    """
    lower = url.lower()
    if lower.endswith((".md", ".markdown", ".txt", ".yml", ".yaml", ".json")):
        return content.rstrip() + "\n"

    text = COMMENT_RE.sub("", content)
    text = extract_main(text, content_class_re)
    text = TOC_BLOCK_RE.sub("", text)
    text = html_to_text(text)
    text = BLANK_RE.sub("\n\n", text)

    out: list[str] = []
    for line in text.splitlines():
        # 保留行首缩进（list bullet "  - foo"），仅压缩行内多余空白
        stripped = line.lstrip(" \t")
        if not stripped.strip():
            continue
        indent = line[: len(line) - len(stripped)]
        out.append(indent + INTRA_LINE_WS_RE.sub(" ", stripped).rstrip())
    return "\n".join(out) + "\n"


def git_diff(file_path: Path) -> str:
    """返回该文件相对 HEAD 的 unified diff。新文件返回完整内容（带 + 前缀）。"""
    rel = file_path.relative_to(ROOT)
    try:
        out = subprocess.check_output(
            ["git", "diff", "--no-color", "--unified=2", "HEAD", "--", str(rel)],
            cwd=ROOT,
            stderr=subprocess.STDOUT,
        ).decode("utf-8", errors="replace")
    except subprocess.CalledProcessError as e:
        return e.output.decode("utf-8", errors="replace")
    if out.strip():
        return out
    try:
        subprocess.check_output(
            ["git", "ls-files", "--error-unmatch", str(rel)],
            cwd=ROOT,
            stderr=subprocess.DEVNULL,
        )
        return ""
    except subprocess.CalledProcessError:
        return f"(new file)\n+++ {rel}\n" + "".join(
            f"+{line}\n" for line in file_path.read_text(encoding="utf-8").splitlines()
        )


def truncate_diff(diff: str, limit: int) -> str:
    lines = diff.splitlines()
    if len(lines) <= limit:
        return diff
    keep = lines[:limit]
    return "\n".join(keep) + f"\n... (diff truncated, total {len(lines)} lines) ..."


def main() -> int:
    sources = json.loads(SOURCES_FILE.read_text(encoding="utf-8"))["sources"]
    CHANGELOG_DIR.mkdir(exist_ok=True)
    if ERROR_LOG.exists():
        ERROR_LOG.unlink()

    today = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
    changed_blocks: list[str] = []
    summary: list[str] = []

    for src in sources:
        key = src["key"]
        name = src["name"]
        url = src["raw_url"]
        out_file = CHANGELOG_DIR / f"{key}.txt"
        try:
            raw = fetch(url)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as e:
            log_error(f"{key}: fetch failed: {type(e).__name__}: {e}")
            summary.append(f"- [FAIL] **{name}** (`{key}`): {type(e).__name__}")
            continue
        normalized = normalize(raw, url, src.get("content_class_re"))
        prev = out_file.read_text(encoding="utf-8") if out_file.exists() else ""
        if normalized == prev:
            summary.append(f"- [OK] {name} (`{key}`): no change ({len(normalized)} bytes)")
            continue
        out_file.write_text(normalized, encoding="utf-8")
        diff = git_diff(out_file)
        if not diff.strip():
            summary.append(f"- [NEW] {name} (`{key}`): first snapshot, {len(normalized)} bytes")
            changed_blocks.append(
                f"### {name} (`{key}`) — first snapshot\n"
                f"- Source: {src['doc_url']}\n"
                f"- Raw: {url}\n"
                f"- Bytes: {len(normalized)}\n"
            )
            continue
        truncated = truncate_diff(diff, MAX_DIFF_LINES_PER_SOURCE)
        summary.append(f"- [CHANGED] **{name}** (`{key}`): {len(diff.splitlines())} diff lines")
        changed_blocks.append(
            f"### {name} (`{key}`)\n"
            f"- Source: {src['doc_url']}\n"
            f"- Raw: {url}\n\n"
            f"```diff\n{truncated}\n```\n"
        )

    parts = [
        "# Exchange API Changelog Diff\n",
        f"Generated: {today} (Asia/Shanghai)\n",
        "## Summary\n",
        *summary,
        "\n",
    ]
    if changed_blocks:
        parts.append("## Changes\n")
        parts.extend(changed_blocks)
        header_status = "true"
    else:
        parts.append(f"## Changes\n\nNo changes on {today}.\n")
        header_status = "false"

    final = (
        f"<!-- has_changes={header_status} date={today} -->\n"
        + "\n".join(p if p.endswith("\n") else p + "\n" for p in parts)
    )
    DIFF_FILE.write_text(final, encoding="utf-8")
    print(f"has_changes={header_status} sources={len(sources)} changed={len(changed_blocks)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
