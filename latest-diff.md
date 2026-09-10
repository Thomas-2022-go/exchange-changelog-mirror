<!-- has_changes=true date=2026-09-10 -->
# Exchange API Changelog Diff

Generated: 2026-09-10 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (131990 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (216777 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3256 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 13 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42000 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (124213 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 8ec94be..4e2eda9 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,8 @@
+2026-09-10​
+REST API​
+- Get Instruments Info [UPDATE]
+  - baseCoin now supports passing All to return all option symbols. Only valid when category=option
+- Create Order [UPDATE]
+  - rpiTakerAccess=true now supports orderType=Limit with timeInForce=IOC or FOK
 2026-09-07​
 REST API​

```
