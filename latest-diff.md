<!-- has_changes=true date=2026-11-06 -->
# Exchange API Changelog Diff

Generated: 2026-11-06 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (137687 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (219577 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 20 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (44528 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (164576 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 721bc4a..9960cf1 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,8 @@
+2026-11-05​
+REST API​
+- Get Strategy List [UPDATE]
+  - Restrict the query time range between beginTimeE0 and endTimeE0 to one year.
+- Get Strategy Order List [UPDATE]
+  - Restrict the query time range between beginTimeE0 and endTimeE0 to one year.
 2026-11-04​
 REST API​
@@ -15,4 +21,6 @@ REST API​
 - Cancel All Quotes [NEW]
   - Add POST /v5/event/cancel-all to cancel all active Event Contract quotes for a specified symbol.
+- JSON Market Data [UPDATE]
+  - Tokyo Dedicated Host has the extra connection limit.
 2026-10-29​
 REST API​

```
