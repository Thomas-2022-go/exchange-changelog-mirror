<!-- has_changes=true date=2026-08-25 -->
# Exchange API Changelog Diff

Generated: 2026-08-25 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132451 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (214540 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [OK] Bybit V5 (`bybit`): no change (92575 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 10 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (149534 bytes)



## Changes

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index cd3077b..8974b36 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,2 +1,5 @@
+2026.08.27#
+[Modify] For all UTA public WebSocket connections (FUTURES and SPOT), the welcome response sent after a successful connection now returns "data":"welcome" rather than "message":"welcome". A new pingTimeout field is also included, which indicates the estimated interval (in ms) within which the client should receive a pong message from the server.
+[Modify] For all UTA public Websocket connections and private connections, extra spaces between parameters inside JSON body of push data will be removed.
 2026.08.20#
 [Modify] UTA REST Get Trade History When fillType is ADL/LIQUID/SETTLEMENT, size must be returned as positive values.

```
