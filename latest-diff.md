<!-- has_changes=true date=2026-09-01 -->
# Exchange API Changelog Diff

Generated: 2026-09-01 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 79 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (214695 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 20 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (41867 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index 2d8391d..f32930e 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -334,5 +334,5 @@ Please consult the [FIX API documentation](./fix-api.md#general-api-information)
 ### 2026-02-24
 
-* [ICEBERG_PARTS](https://developers.binance.com/docs/binance-spot-api-docs/filters#iceberg_parts) will be increased to 100 for all symbols at **2026-03-12 07:00 UTC**.
+* [ICEBERG_PARTS](filters.md#iceberg_parts) will be increased to 100 for all symbols at **2026-03-12 07:00 UTC**.
 * Following the announcement on [2025-12-02](#2025-12-02), `!ticker@arr` will be retired on **2026-03-26**.
 
@@ -371,5 +371,5 @@ REST and WebSocket API:
 **Notice: The following changes will occur at 2026-02-11 7:00 UTC**:
 
-* [ICEBERG_PARTS](https://developers.binance.com/docs/binance-spot-api-docs/filters#iceberg_parts) will be increased to 50 for all symbols.
+* [ICEBERG_PARTS](filters.md#iceberg_parts) will be increased to 50 for all symbols.
 
 ---
@@ -402,5 +402,5 @@ WebSocket API
 * Updated [FIX SBE documentation](fix-api.md#fix-sbe)
 * Clarified User Data Stream documentation regarding [`eventStreamTerminated`](user-data-stream.md#event-stream-terminated).
-* Assets `这是测试币` and `456` and symbol `这是测试币456` have been added to [SPOT Testnet](http://testnet.binance.vision) for testing endpoints/methods with a Unicode symbol. See the [Testnet CHANGELOG](https://developers.binance.com/docs/binance-spot-api-docs/testnet) for more information.
+* Assets `这是测试币` and `456` and symbol `这是测试币456` have been added to [SPOT Testnet](http://testnet.binance.vision) for testing endpoints/methods with a Unicode symbol. See the [Testnet CHANGELOG](testnet/CHANGELOG.md) for more information.
 
 ---
@@ -414,9 +414,9 @@ WebSocket API
 #### REST API
 
-* Updated documentation for REST API regarding [Signed Endpoints examples for placing an order](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/request-security#signed-endpoint-examples-for-post-apiv3order).
+* Updated documentation for REST API regarding [Signed Endpoints examples for placing an order](rest-api.md#signed-endpoint-examples-for-post-apiv3order).
 
 #### WebSocket API
 
-* Updated documentation for WebSocket API regarding [SIGNED request security](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/request-security#signed-request-security).
+* Updated documentation for WebSocket API regarding [SIGNED request security](web-socket-api.md#signed-request-security).
 
 ---
@@ -426,5 +426,5 @@ WebSocket API
 **Clarification Regarding UTF-8 Encoding:**
 
-* In [FIX](fix-api.md), [REST](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-api-information), and [WebSocket APIs](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/general-api-information), if your request contains a symbol name containing non-ASCII characters, then the response may contain non-ASCII characters encoded in UTF-8.
+* In [FIX](fix-api.md), [REST](rest-api.md#general-api-information), and [WebSocket APIs](web-socket-api.md#general-api-information), if your request contains a symbol name containing non-ASCII characters, then the response may contain non-ASCII characters encoded in UTF-8.
 * In REST and WebSocket APIs, some endpoints/methods may return asset and/or symbol names containing non-ASCII characters encoded in UTF-8 even if the request did not contain non-ASCII characters.
 * In [WebSocket Streams](web-socket-streams.md), if your request contains a symbol name containing non-ASCII characters, then the stream events may contain non-ASCII characters encoded in UTF-8.
@@ -474,5 +474,5 @@ WebSocket API
 
 **Notice: The following changes will occur at approximately 2025-12-18 7:00 UTC**:
-* [ICEBERG_PARTS](https://developers.binance.com/docs/binance-spot-api-docs/filters#iceberg_parts) will be increased to 25 for all symbols.
+* [ICEBERG_PARTS](filters.md#iceberg_parts) will be increased to 25 for all symbols.
 * [FIX SBE support](fix-api.md) becomes available.
 * [One Pays the Other (OPO)](https://github.com/binance/binance-spot-api-docs/blob/master/faqs/opo.md) becomes available on all symbols.
@@ -507,5 +507,5 @@ WebSocket API
 
 * All Market Tickers Stream (`!ticker@arr`) has been deprecated; This means this will be removed both from the documentation and from our systems at a later date. More details to follow.
-* Please use [`<symbol>@ticker`](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-ticker-streams) or [`!miniTicker@arr`](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-mini-tickers-stream) instead.
+* Please use [`<symbol>@ticker`](web-socket-streams.md#individual-symbol-ticker-streams) or [`!miniTicker@arr`](web-socket-streams.md#all-market-mini-tickers-stream) instead.
 
 ---
@@ -513,5 +513,5 @@ WebSocket API
 ### 2025-11-12
 
-* The steps on [how to manage a local order book correctly](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#how-to-manage-a-local-order-book-correctly) has been corrected.
+* The steps on [how to manage a local order book correctly](web-socket-streams.md#how-to-manage-a-local-order-book-correctly) has been corrected.
 
 ---
@@ -572,5 +572,5 @@ WebSocket API
 Following the announcement from [2025-04-07](#2025-04-07), all documentation related with `listenKey` for use on `wss://stream.binance.com` has been removed.
 
-**We remind you that you should instead get user data updates by subscribing to the [User Data Stream on the WebSocket API](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests). This will offer better performance (lower latency).**
+**We remind you that you should instead get user data updates by subscribing to the [User Data Stream on the WebSocket API](web-socket-api.md#user-data-stream-requests). This will offer better performance (lower latency).**
 
 Please refer to the list of requests and methods below for more information.
@@ -931,5 +931,5 @@ REST and WebSocket API:
 * **Receiving user data streams on wss://stream.binance.com:9443 using a `listenKey` is now deprecated.**
     * This feature will be removed from our systems at a later date.
-* **Instead, you should get user data updates by subscribing to the [User Data Stream on the WebSocket API](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests)**.
+* **Instead, you should get user data updates by subscribing to the [User Data Stream on the WebSocket API](web-socket-api.md#user-data-stream-requests)**.
     * This should offer slightly better performance **(lower latency)**.
     * This requires the use of an Ed25519 API Key.

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 3800fab..2659965 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,15 @@
+2026-09-02​
+REST API​
+- Event Trading [NEW]
+  - Launch Event Contract OpenAPI. Includes Market, Trade endpoints and WebSocket streams.
+2026-09-01​
+- Get API Key Information [UPDATE]
+  - Add new response field isFixApi
+- Get Fee Group Structure [UPDATE]
+  - G2 (High Growth), G3 (Mid-Tier Liquidity), G4 (Mid-Tier Activation), G5 (Long Tail), USDC are merged to Altcoin
+- Get Instruments Info [UPDATE]
+  - Add a new "status" for Futures, PendingOpen. You cannot place orders until it becomes Trading
+- Get Account Instruments Info [UPDATE]
+  - Add a new "status" for Futures, PendingOpen. You cannot place orders until it becomes Trading
 2026-08-31​
 REST API​

```
