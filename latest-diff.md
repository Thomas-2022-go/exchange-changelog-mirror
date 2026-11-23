<!-- has_changes=true date=2026-11-23 -->
# Exchange API Changelog Diff

Generated: 2026-11-23 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (146418 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (220592 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3488 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 13 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (45900 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (166885 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 10194b6..0d9eece 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,8 @@
+2026-11-23​
+REST API​
+- Move Position [UPDATE]
+  - Add an optional request parameter reduceOnly
+- Get Move Position History [UPDATE]
+  - Add a response parameter reduceOnly
 2026-11-20​
 REST API​

```
