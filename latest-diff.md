<!-- has_changes=true date=2026-08-28 -->
# Exchange API Changelog Diff

Generated: 2026-08-28 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132451 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (214695 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 13 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (41867 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 82d3b2a..3800fab 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -10,4 +10,8 @@ REST API​
 - Integration Guidance
   - Add Rest API integration method for Argentina users
+- Get Fee Group Structure [UPDATE]
+  - Add new response field rpiMakerRebate
+- Get Fee Rate [UPDATE]
+  - Add new response field rpiMakerFeeRate
 Websocket API​
 - Connect

```
