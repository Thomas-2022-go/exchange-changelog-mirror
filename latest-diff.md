<!-- has_changes=true date=2026-11-17 -->
# Exchange API Changelog Diff

Generated: 2026-11-17 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (146418 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (220476 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3488 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 11 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (44528 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (164576 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 12dfc66..83e0919 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,6 @@
+2026-11-17​
+REST API​
+- Get Institution Connection Limit [NEW]
+  - Add GET /v5/ins/connection-limit to retrieve the JSON and SBE connection limits and current usage for each dedicated endpoint.
 2026-11-09​
 REST API​

```
