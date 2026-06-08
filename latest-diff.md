<!-- has_changes=true date=2026-06-08 -->
# Exchange API Changelog Diff

Generated: 2026-06-08 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128989 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (87006 bytes)

- [OK] OKX V5 (`okx`): no change (199202 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (81117 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 14 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (138977 bytes)



## Changes

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index ec007a6..27c84f3 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,4 +1,9 @@
 WARNING
 The Pro API is currently in beta testing and should not be used in production trading environments.
+2026.06.05#
+[Add] UTA REST Get API Rate Limit
+[Add] UTA REST Get All API Rate Limit
+[Add] UTA REST Get API Rate Limit Cap
+[Add] UTA REST Set Sub Accounts API Rate Limit
 2026.06.03#
 1. UTA API Upgrade#

```
