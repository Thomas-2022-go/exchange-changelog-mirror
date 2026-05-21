<!-- has_changes=true date=2026-05-21 -->
# Exchange API Changelog Diff

Generated: 2026-05-21 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128997 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [CHANGED] **OKX V5** (`okx`): 36 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (78327 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (29217 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139416 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 89eef13..8614c9d 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,11 +1,3 @@
 待发布内容
-ELP Maker 费率
-最近更新：2026年5月14日
-随着 ELP Maker 费率调整，在费率查询接口的返回参数 feeGroup 中新增 elpMaker 字段，用于展示 ELP Maker 有效费率。本次变更预计于 2026年5月20日 上线。详情请参阅公告。
-- 在 feeGroup 中新增返回参数 elpMaker：
-  - GET / 获取当前账户交易手续费费率
-返回参数
-| 参数名 | 类型 | 描述
-| > elpMaker | String | ELP Maker 有效费率。若 ELP 不适用于该交易产品，则返回 ""。不适用于 EVENTS instType。
 信号复制新增 API 接口
 最后更新：2026 年 5 月 14 日
@@ -44,4 +36,19 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
  1. books5 和 bbo-tbt 频道本身不包含 checksum 字段，不在本次变更范围内。
  2. WebSocket 连接已全面启用 TLS（wss://），具备防窃听、防篡改以及完整性校验的能力；结合 seqId/prevSeqId 的严格校验，可有效防止数据乱序、部分丢失或被恶意注入，实现与原 checksum 等效甚至更强的完整性保护。
+2026-05-20
+新增专用 REST API 域名 openapi.okx.com
+OKX 全球站用户现可使用新的专用 REST API 域名 openapi.okx.com。该域名在 API 访问方面与 www.okx.com 完全等价，建议所有 REST API 请求优先使用此域名。
+- 文档中的 REST API 基础 URL 已从 https://www.okx.com 更新为 https://openapi.okx.com
+- www.okx.com 将继续可用，不会下线
+- WebSocket URL（ws.okx.com、wspap.okx.com）保持不变
+- 区域域名（us.okx.com、eea.okx.com、tr.okx.com）保持不变
+建议您将 API 客户端配置中的 REST API 基础 URL 更新为 https://openapi.okx.com。
+ELP Maker 费率
+随着 ELP Maker 费率调整，在费率查询接口的返回参数 feeGroup 中新增 elpMaker 字段，用于展示 ELP Maker 有效费率。详情请参阅公告。
+- 在 feeGroup 中新增返回参数 elpMaker：
+  - GET / 获取当前账户交易手续费费率
+返回参数
+| 参数名 | 类型 | 描述
+| > elpMaker | String | ELP Maker 有效费率。若 ELP 不适用于该交易产品，则返回 ""。
 2026-05-19
 - 平台持仓限额优化 — 新增币量维度限额字段及错误码 54031。

```
