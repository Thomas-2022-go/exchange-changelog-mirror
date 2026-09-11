<!-- has_changes=true date=2026-09-11 -->
# Exchange API Changelog Diff

Generated: 2026-09-11 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (131990 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (216777 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3256 bytes)

- [OK] Bybit V5 (`bybit`): no change (95421 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 12 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (124213 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index 1e88015..2b8f562 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -41,7 +41,4 @@ Update response field types: callauctionFirstStageStartTime, callauctionSecondSt
 | [Modify] | UTA REST Get Futures Interest Rate Index | Add standard XBTUSDTM to the input parameter
 | [Modify] | UTA REST Get Klines | Add klineType to replace symbol suffix encoding; strip suffix from symbol (backward compatible); Symbol Naming Standard set to govern future interfaces
-2026.08.27#
-[Modify] For all UTA public WebSocket connections (FUTURES and SPOT), the welcome response sent after a successful connection now returns "data":"welcome" rather than "message":"welcome". A new pingTimeout field is also included, which indicates the estimated interval (in ms) within which the client should receive a pong message from the server.
-[Modify] For all UTA public Websocket connections and private connections, extra spaces between parameters inside JSON body of push data will be removed.
 2026.08.20#
 [Modify] UTA REST Get Trade History When fillType is ADL/LIQUID/SETTLEMENT, size must be returned as positive values.

```
