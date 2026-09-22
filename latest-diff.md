<!-- has_changes=true date=2026-09-22 -->
# Exchange API Changelog Diff

Generated: 2026-09-22 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132590 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (217257 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 14 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42424 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (124213 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 4e2eda9..472f79d 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,9 @@
+2026-09-17​
+REST API​
+- Strategy [UPDATE]
+  - pov now supports Spot (category=UTA_SPOT), covering all three execution modes and One-Time execution
+  - pov adds new request parameter positionValue: total order quantity by value, denominated in the quote currency. Mutually exclusive with size
+  - pov adds new request parameter leverageType: 0: normal, 1: borrow to trade (UTA_SPOT only)
+  - iceberg maximum number of sub-orders raised from 100 to 200
 2026-09-10​
 REST API​

```
