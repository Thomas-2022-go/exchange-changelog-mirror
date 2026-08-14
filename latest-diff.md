<!-- has_changes=true date=2026-08-14 -->
# Exchange API Changelog Diff

Generated: 2026-08-14 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 11 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (213755 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [OK] Bybit V5 (`bybit`): no change (91216 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (36766 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145596 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index 032d2a3..2d8391d 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -566,5 +566,5 @@ WebSocket API
 #### SBE
 
-* SBE: schema 3:1 ([spot_3_1.xml](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot_3_1.xml)) has been updated to support [listenToken Subscription Methods](https://developers.binance.com/docs/margin_trading/trade-data-stream/Listen-Token-Websocket-API) for Margin Trading.
+* SBE: schema 3:1 ([spot_3_1.xml](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot_3_1.xml)) has been updated to support [listenToken Subscription Methods](https://developers.binance.com/en/docs/products/margin-trading/listen-token-data-stream) for Margin Trading.
 
 #### REST and WebSocket API

```
