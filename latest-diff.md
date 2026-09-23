<!-- has_changes=true date=2026-09-23 -->
# Exchange API Changelog Diff

Generated: 2026-09-23 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132590 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (217257 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 22 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42424 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (124213 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 472f79d..a31131c 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,3 +1,3 @@
-2026-09-17​
+2026-09-23​
 REST API​
 - Strategy [UPDATE]
@@ -6,4 +6,12 @@ REST API​
   - pov adds new request parameter leverageType: 0: normal, 1: borrow to trade (UTA_SPOT only)
   - iceberg maximum number of sub-orders raised from 100 to 200
+2026-09-22​
+REST API​
+- Get Option Base Coins [NEW]
+  - Add GET /v5/market/option-base-coins to query option base coins, including display names, launch times, and tradable symbol availability. Supports filtering by multiple underlying asset types.
+- Get Delay Liquidation Status [NEW]
+  - Add GET /v5/ins-loan/delay-liq-status to query the current LTV, liquidation status, and delay liquidation timing information for an institutional loan account.
+- Integration Guidance [UPDATE]
+  - Remove Netherlands domain.
 2026-09-10​
 REST API​

```
