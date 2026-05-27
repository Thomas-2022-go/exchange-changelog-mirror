<!-- has_changes=true date=2026-05-27 -->
# Exchange API Changelog Diff

Generated: 2026-05-27 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128989 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [OK] OKX V5 (`okx`): no change (194741 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 12 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (29221 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (138977 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 9d17fe0..8d05e30 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -9,4 +9,7 @@ Websocket API​
   - Add new response field colRes (platform level collateral restriction status)
 2026-05-26​
+REST API​
+- Strategy [UPDATE]
+  - Supports a new strategy type pov
 Websocket API​
 - Order [UPDATE]

```
