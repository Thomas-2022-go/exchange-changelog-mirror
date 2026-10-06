<!-- has_changes=true date=2026-10-06 -->
# Exchange API Changelog Diff

Generated: 2026-10-06 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132590 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (217607 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 20 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42424 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (124213 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 89d3fc1..0339fb6 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,6 @@
+2026-09-30​
+REST API​
+- Get/Set Auto Savings Settings [NEW]
+  - Add GET and POST /v5/earn/flexible-saving/auto-savings to query and update Flexible Saving auto savings settings.
 2026-09-29​
 REST API​
@@ -8,4 +12,8 @@ REST API​
 - Get Batch Export Report Status [NEW]
   - Add GET /v5/fht/compliance/tax/private/batch_query to query each task's status and download URL by batchId.
+2026-09-24​
+REST API​
+- Get Token Splash User Activity Params [UPDATE]
+  - Add response field tradeToken, which identifies the token counted by the trade task.
 2026-09-23​
 REST API​

```
