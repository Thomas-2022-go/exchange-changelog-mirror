<!-- has_changes=true date=2026-10-13 -->
# Exchange API Changelog Diff

Generated: 2026-10-13 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132590 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 16 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 15 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42424 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (124213 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 972d0a4..3774e83 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -82,4 +82,11 @@ tradeQuoteCcy 的默认值为 instId 中的计价币种。因此，如果仅将
 - 新增 POST / 开通功能。仅当下单返回错误码 54109 时才需调用该接口；否则无需调用。
 - 新增错误码 54109，详情请参阅 REST API 错误码。
+2026-09-29
+全球流动性计划 API v2
+在 /api/v5/users/glp/v2/ 下新增三个 REST 接口，支持全球流动性计划（GLP）。经过身份验证的用户可查询 GLP 注册状态、实时绩效指标和每周考核历史。子账户 API key 获取的是主账户的 GLP 数据。
+新增接口
+- GET / 获取 GLP v2 概览
+- GET / 获取 GLP v2 考核详情
+- GET / 获取 GLP v2 历史绩效
 2026-09-15
 RPI 挂单最小名义金额门槛

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 0339fb6..b82c22c 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,10 @@
+2026-10-13​
+REST API​
+- Enum [UPDATE]
+  - execType: add ForwardSplitOpen and ReverseSplitOpen.
+  - For forward or reverse stock splits, ForwardSplitSettle and ReverseSplitSettle settle and close the entire existing position, followed by opening a new position.
+- Enum [UPDATE]
+  - type(uta-translog): add FORWARD_SPLIT_OPEN and REVERSE_SPLIT_OPEN.
+  - Update the descriptions of FORWARD_SPLIT_SETTLE and REVERSE_SPLIT_SETTLE.
 2026-09-30​
 REST API​

```
