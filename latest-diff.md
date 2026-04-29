<!-- has_changes=true date=2026-04-29 -->
# Exchange API Changelog Diff

Generated: 2026-04-29 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 23 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (85776 bytes)

- [OK] OKX V5 (`okx`): no change (186803 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (76863 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (28151 bytes)

- [CHANGED] **Gate.io Spot WebSocket v4** (`gate-spot-ws`): 9 diff lines

- [CHANGED] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): 9 diff lines



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index 140eb18..c745ad1 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -1,5 +1,11 @@
 # CHANGELOG for Binance's API
 
-**Last Updated: 2026-04-17**
+**Last Updated: 2026-04-28**
+
+### 2026-04-28
+
+* Corrected the JSON in the `Price Range Execution Rule FAQ` for the question [`How does the Price Range Execution Rule work?`](./faqs/price_range_execution_rules.md#how-does-the-price-range-execution-rule-work).
+
+---
 
 ### 2026-04-17
@@ -11,5 +17,4 @@ The following will occur on **2026-05-05 at approximately 10:00 UTC**.
   * FIX SBE: [MarketDataIncrementalDepth](fix-api.md#marketdataincrementaldepth)
 
-
 ---
 

```

### Gate.io Spot WebSocket v4 (`gate-spot-ws`)
- Source: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/

```diff
diff --git a/changelogs/gate-spot-ws.txt b/changelogs/gate-spot-ws.txt
index 2567e1d..dff8154 100644
--- a/changelogs/gate-spot-ws.txt
+++ b/changelogs/gate-spot-ws.txt
@@ -1477,3 +1477,3 @@ account: 指定查询账户。不指定默认现货，保证金和逐仓杠杆
 | »»label | String | 以字符串格式表示错误类型
 | »»message | String | 错误信息详情
-Last Updated: 4/26/2026, 6:24:01 AM
+Last Updated: 4/27/2026, 10:15:14 AM

```

### Gate.io Futures WebSocket v4 (`gate-futures-ws`)
- Source: https://www.gate.io/docs/developers/futures/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/futures/ws/zh_CN/

```diff
diff --git a/changelogs/gate-futures-ws.txt b/changelogs/gate-futures-ws.txt
index 9f3884f..83275bb 100644
--- a/changelogs/gate-futures-ws.txt
+++ b/changelogs/gate-futures-ws.txt
@@ -1947,3 +1947,3 @@ req_param` API 订单模型的 JSON 字节数据:
 | »»label | String | 错误类型
 | »»message | String | 详细错误信息
-Last Updated: 4/27/2026, 1:01:38 AM
+Last Updated: 4/27/2026, 10:15:14 AM

```
