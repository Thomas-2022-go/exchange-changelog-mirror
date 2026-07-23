<!-- has_changes=true date=2026-07-23 -->
# Exchange API Changelog Diff

Generated: 2026-07-23 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132274 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (206336 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3590 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 11 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (35340 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120249 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 07d09a7..fd0095f 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,6 @@
+2026-07-23​
+REST API​
+- Enum [UPDATE]
+  - Add new execType value: CorporateAction (stock split or reverse stock split)
 2026-07-21​
 Websocket API​

```
