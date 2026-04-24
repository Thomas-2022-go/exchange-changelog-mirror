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

import html
import json
import re
import ssl
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone, timedelta
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

TAG_RE = re.compile(r"<[^>]+>")
SCRIPT_RE = re.compile(
    r"<(script|style|noscript|svg)\b[^>]*>.*?</\1>", re.DOTALL | re.IGNORECASE
)
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
# Docusaurus / readme.io 等文档站的固定噪声块：导航条、侧边栏目录、SDK 推广、页脚 footer。
# 这些每次发版都会变（菜单顺序、SDK 列表），但与 API 文档实质内容无关，必须先剔除再 diff。
NOISE_BLOCK_RE = re.compile(
    r"<(nav|aside|header|footer|form)\b[^>]*>.*?</\1>",
    re.DOTALL | re.IGNORECASE,
)
TOC_BLOCK_RE = re.compile(
    r"<(?:ul|div|nav)\b[^>]*class\s*=\s*[\"'][^\"']*"
    r"(?:table-of-contents|tocSection|theme-doc-toc|on-this-page|right-side|sidebar)"
    r"[^\"']*[\"'][^>]*>.*?</(?:ul|div|nav)>",
    re.DOTALL | re.IGNORECASE,
)
# 页面主体抽取：优先 <article>，其次 Docusaurus 的 markdown 容器，最后 <main>。
MAIN_PATTERNS = [
    re.compile(r"<article\b[^>]*>(.*?)</article>", re.DOTALL | re.IGNORECASE),
    re.compile(
        r"<div\b[^>]*class\s*=\s*[\"'][^\"']*"
        r"(?:theme-doc-markdown|markdown|docMainContainer|content)"
        r"[^\"']*[\"'][^>]*>(.*?)</div>\s*</main>",
        re.DOTALL | re.IGNORECASE,
    ),
    re.compile(r"<main\b[^>]*>(.*?)</main>", re.DOTALL | re.IGNORECASE),
]
WS_RE = re.compile(r"[ \t]+")
BLANK_RE = re.compile(r"\n{3,}")


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


def extract_main(html_text: str) -> str:
    """尝试只保留 HTML 主体内容区，剔除导航/侧边栏/footer 等装饰元素。

    匹配优先级：<article> > Docusaurus markdown 容器 > <main>。任一命中即返回。
    都没命中则原样返回（少数小站点没有语义标签）。
    """
    for pat in MAIN_PATTERNS:
        m = pat.search(html_text)
        if m:
            return m.group(1) if m.groups() else m.group(0)
    return html_text


def normalize(content: str, url: str) -> str:
    """把 HTML 抓取结果清洗成可对比的纯文本。Markdown / yaml 直接保留。

    清洗顺序很关键：
    1. 先 strip 注释 / script / style / svg 等不可见内容
    2. 再抽主体内容区（避免后续把侧边栏/导航也带进来）
    3. 再剔除主体内仍可能存在的导航条 / 侧边栏目录 / footer
    4. 最后剥剩余标签、合并空白
    """
    lower = url.lower()
    if lower.endswith((".md", ".markdown", ".txt", ".yml", ".yaml", ".json")):
        return content.rstrip() + "\n"

    text = COMMENT_RE.sub("", content)
    text = SCRIPT_RE.sub("", text)
    text = extract_main(text)
    text = NOISE_BLOCK_RE.sub("", text)
    text = TOC_BLOCK_RE.sub("", text)
    text = TAG_RE.sub("\n", text)
    text = html.unescape(text)
    text = WS_RE.sub(" ", text)
    text = BLANK_RE.sub("\n\n", text)
    lines = [line.strip() for line in text.splitlines()]
    return "\n".join(line for line in lines if line) + "\n"


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
        normalized = normalize(raw, url)
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
