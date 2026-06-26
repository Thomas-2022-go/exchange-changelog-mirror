<!-- has_changes=true date=2026-06-26 -->
# Exchange API Changelog Diff

Generated: 2026-06-26 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 18 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (87509 bytes)

- [OK] OKX V5 (`okx`): no change (202930 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (82998 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 24 diff lines

- [FAIL] **Gate.io Spot WebSocket v4** (`gate-spot-ws`): HTTPError

- [FAIL] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): HTTPError



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index c596963..fabafba 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -34,5 +34,5 @@ REST and WebSocket API:
 **Update:**
 
-* Updated the [Price Range Execution Rule FAQ](../faqs/price_range_execution_rules.md#external-reference-price-calculation-method-1) with new External Reference Price Calculation Methods.
+* Updated the [Price Range Execution Rule FAQ](../faqs/price_range_execution_rules.md#externalCalculationId1) with new External Reference Price Calculation Methods.
 
 The `serverShutdown` event will be sent when the **server is about to be shut down**; when you receive this event, please disconnect and open a new connection.
@@ -186,5 +186,5 @@ The following will occur on **2026-04-02 at approximately 07:00 UTC**.
 ### 2026-03-13
 
-* Updated [Price Range Execution Rule](./faqs/price_range_execution_rules.md#external-reference-price-calculation-method-0) with a new External Reference Price Calculation Method.
+* Updated [Price Range Execution Rule](./faqs/price_range_execution_rules.md#externalCalculationId0) with a new External Reference Price Calculation Method.
 
 ---

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index 27c84f3..1e88672 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,4 +1,19 @@
 WARNING
 The Pro API is currently in beta testing and should not be used in production trading environments.
+2026.06.17#
+[Modify] UTA API Orderbook Websocket
+A new incremental depth streaming mode depth=increment@10ms is introduced (supported for both Spot and Futures).
+Compared with the existing depth=increment streaming mode, the new depth streams provide the following improvements:
+Streaming mode
+Changed from incremental updates to a “snapshot + incremental updates” model.
+Depth levels
+Depth coverage is adjusted from full order book to 500 levels.
+Update frequency
+Updates are aggregated and pushed every 10ms instead of real-time pushing.
+Depth update logic
+For price levels outside the top 500 depth, changes in size will not be pushed.
+For price levels within the top 500 depth:
+If a price level size becomes 0 due to trades, a message with size = 0 will be pushed for that price.
+If a price level is pushed out of the top 500 depth due to order book changes, a message with size = 0 will be pushed for that price.
 2026.06.05#
 [Add] UTA REST Get API Rate Limit

```
