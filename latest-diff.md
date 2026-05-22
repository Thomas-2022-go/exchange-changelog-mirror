<!-- has_changes=true date=2026-05-22 -->
# Exchange API Changelog Diff

Generated: 2026-05-22 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 25 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [OK] OKX V5 (`okx`): no change (194198 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (78327 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (29217 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139416 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index e68f261..f36102e 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -364,5 +364,5 @@ WebSocket API
 
 * [Schema for FIX SBE](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot-fixsbe-1_0.xml) has been updated to use `smallGroupSize16Encoding` in `MarketDataSnapshot` and use `presence="optional"` for incremental book ticker/depth `MDEntrySize` fields.
-* Updated documentation re: [FIX vs FIX SBE](fix-api.md#fix-vs-fix-sbe-schema)
+* Updated documentation re: [FIX vs FIX SBE](fix-api.md#fix-vs-fix-sbe)
 * Added documentation in REST, and WebSocket APIs stating: <br>**Please avoid SQL keywords in requests** as they may trigger a security block by a WAF (Web Application Firewall) rule. <br> See https://www.binance.com/en/support/faq/detail/360004492232 for more details.
 
@@ -645,5 +645,5 @@ REST and WebSocket API:
   * When called with `subscriptionId`, this will attempt to close the subscription matching that Id, if it exists.
   * The authorization for this request has been changed to `NONE`.
-* Field `subscriptionId` has been added to the User Data Stream events payload when listening through the [WebSocket API](web-socket-api.md#user_data_stream_subscribe). This will identify which subscription the event is coming from.
+* Field `subscriptionId` has been added to the User Data Stream events payload when listening through the [WebSocket API](web-socket-api.md#user-data-stream-subscribe). This will identify which subscription the event is coming from.
 
 #### FIX API
@@ -2352,5 +2352,5 @@ USER DATA STREAM
 
 ### 2020-05-01
-* From 2020-05-01 UTC 00:00, all symbols will have a limit of 200 open orders using the [MAX_NUM_ORDERS](./rest-api.md#max_num_orders) filter.
+* From 2020-05-01 UTC 00:00, all symbols will have a limit of 200 open orders using the [MAX_NUM_ORDERS](./filters.md#max_num_orders) filter.
     * No existing orders will be removed or canceled.
     * Accounts that have 200 or more open orders on a symbol will not be able to place new orders on that symbol until the open order count is below 200.

```
