<!-- has_changes=true date=2026-05-19 -->
# Exchange API Changelog Diff

Generated: 2026-05-19 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128997 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [OK] OKX V5 (`okx`): no change (193443 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (78327 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 18 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139416 bytes)



## Changes

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index 5eb0126..4aeda20 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -2,6 +2,4 @@ WARNING
 The Pro API is currently in beta testing and should not be used in production trading environments.
 2026.05.15#
-[Modify] Pro Websocket Private Channel Order
-Added new enum value MATCH for the response field eT, supporting pushing MATCH events for UTA FUTURES trading
 [Modify] Pro REST Get Position List (UTA)
 Added response field:
@@ -14,4 +12,6 @@ Added new enum value:MARGIN
 [Modify] Classic REST Get Trade History
 For liquidation orders, the tradeType will return the value: liquid
+[修改]Pro Websocket Execution Lite
+Push to add clientOid field
 [Add] Pro REST Get API Key Info
 [Add] Pro REST Add Sub-Account

```
