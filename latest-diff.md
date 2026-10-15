<!-- has_changes=true date=2026-10-15 -->
# Exchange API Changelog Diff

Generated: 2026-10-15 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 4861 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (217852 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 11 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42424 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [CHANGED] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): 129 diff lines



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index d2dc26c..8b3dfe2 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -7,11 +7,16 @@
 REST and WebSocket API:
 
-* Reminder that SBE 3:2 schema will be retired on 2026-09-25, [6 months after being deprecated](./faqs/sbe_faq.md#regarding-legacy-support).
-* The [SBE lifecycle for Production](./sbe/schemas/sbe_schema_lifecycle_prod.json) has been updated to reflect this change.
+- Reminder that SBE 3:2 schema will be retired on 2026-09-25,
+  [6 months after being deprecated](faqs/sbe_faq.md#sbe-schema).
+- The [SBE lifecycle for Production](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/sbe_schema_lifecycle_prod.json) has
+  been updated to reflect this change.
 
 FIX API:
 
-* Reminder that FIX SBE 1:0 schema will be retired on 2026-09-25, [6 months after being deprecated](./faqs/sbe_faq.md#regarding-legacy-support).
-* The [FIX SBE lifecycle for Production](./sbe/schemas/sbe_fix_schema_lifecycle_prod.json) has been updated to reflect this change.
+- Reminder that FIX SBE 1:0 schema will be retired on 2026-09-25,
+  [6 months after being deprecated](faqs/sbe_faq.md#sbe-schema).
+- The
+  [FIX SBE lifecycle for Production](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/sbe_fix_schema_lifecycle_prod.json)
+  has been updated to reflect this change.
 
 ---
@@ -21,5 +26,7 @@ FIX API:
 #### FIX API
 
-* Removed the top-level `Symbol (55)` field from `ListStatus <N>` in the [QuickFIX Order Entry schema](./fix/schemas/spot-fix-oe.xml) and API documentation since, as [previously announced](#2025-11-28) the API no longer emits this field.
+- Removed the top-level `Symbol (55)` field from `ListStatus <N>` in the
+  [QuickFIX Order Entry schema](https://github.com/binance/binance-spot-api-docs/blob/master/fix/schemas/spot-fix-oe.xml) and API documentation
+  since, as [previously announced](#2025-12-02) the API no longer emits this field.
 
 ---
@@ -27,5 +34,7 @@ FIX API:
 ### 2026-07-27
 
-* Updated [Price Range Execution Rule](./faqs/price_range_execution_rules.md#externalCalculationId4) with additional External Reference Price Calculation Methods.
+- Updated
+  [Price Range Execution Rule](faqs/price_range_execution_rules.md#external-reference-price-calculation-method-4)
+  with additional External Reference Price Calculation Methods.
 
 ---
@@ -35,7 +44,8 @@ FIX API:
 The following will occur on **2026-08-04 at approximately 07:00 UTC**.
 
-* The update speed of the below SBE Market Data Streams will be changed **from 25ms to 20ms**:
-  * SBE Market Data Streams: [Diff Depth Streams](sbe-market-data-streams.md#diff-depth-streams)
-  * FIX SBE: [MarketDataIncrementalDepth](fix-api.md#marketdataincrementaldepth)
+- The update speed of the below SBE Market Data Streams will be changed **from 25ms to 20ms**:
+  - SBE Market Data Streams:
+    [Diff Depth Streams](sbe-market-data-streams.md#diff-depth-streams)
+  - FIX SBE: [MarketDataIncrementalDepth](fix-api.md#marketdataincrementaldepth)
 
 ---
@@ -47,17 +57,21 @@ The following will occur on **2026-08-04 at approximately 07:00 UTC**.
 #### New Features
 
-* The new `symbolStatus` value `CANCEL_ONLY` can appear in Exchange Information responses.
-    * REST API: `GET /api/v3/exchangeInfo`
-    * WebSocket API: `exchangeInfo`
-* REST and WebSocket API SBE schema [spot_3_5.xml](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot_3_5.xml)
-  * The current schema 3:4 [spot_3_4.xml](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot_3_4.xml) is deprecated and will be retired in 6 months as per our schema deprecation policy.
-  * Changes in schema 3:5:
-    * Updated `symbolStatus` enum: new variant `CANCEL_ONLY`
+- The new `symbolStatus` value `CANCEL_ONLY` can appear in Exchange Information responses.
+  - REST API: `GET /api/v3/exchangeInfo`
+  - WebSocket API: `exchangeInfo`
+- REST and WebSocket API SBE schema [spot_3_5.xml](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot_3_5.xml)
+  - The current schema 3:4 [spot_3_4.xml](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot_3_4.xml) is deprecated and
+    will be retired in 6 months as per our schema deprecation policy.
+  - Changes in schema 3:5:
+    - Updated `symbolStatus` enum: new variant `CANCEL_ONLY`
+
 ---
 
 ### 2026-06-24
 
-* Beginning at **2026-07-09 07:00 UTC**, [WebSocket Streams](web-socket-streams.md) will undergo an infrastructure upgrade and will approximately take up to an hour.
-* During the upgrade, your WebSocket connection may be disconnected; please reconnect to restore your connection.
+- Beginning at **2026-07-09 07:00 UTC**, [WebSocket Streams](web-socket-streams.md) will
+  undergo an infrastructure upgrade and will approximately take up to an hour.
+- During the upgrade, your WebSocket connection may be disconnected; please reconnect to restore
+  your connection.
 
 ---
@@ -67,6 +81,8 @@ The following will occur on **2026-08-04 at approximately 07:00 UTC**.
 REST and WebSocket API:
 
-* Reminder that SBE 3:1 schema will be retired on 2026-06-29, [6 months after being deprecated](faqs/sbe_faq.md#sbe-schema).
-* The [SBE lifecycle for Production](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/sbe_schema_lifecycle_prod.json) has been updated to reflect this change.
+- Reminder that SBE 3:1 schema will be retired on 2026-06-29,
+  [6 months after being deprecated](faqs/sbe_faq.md#sbe-schema).
+- The [SBE lifecycle for Production](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/sbe_schema_lifecycle_prod.json) has
+  been updated to reflect this change.
 
 ---
@@ -76,8 +92,12 @@ REST and WebSocket API:
 #### FIX API
 
-* Documentation update: removed `LastFragment (893)` from [FIX API](./fix-api.md#marketdataincrementalrefresh).
-  * As [previously announced](#2025-12-02), `MarketDataIncrementalRefresh <X>` messages stopped being fragmented on 2025-12-18, and the server no longer sends `LastFragment (893)`.
-  * The field has been removed from the [FIX API](fix-api.md) field list and from the corresponding [QuickFIX MD schema](https://github.com/binance/binance-spot-api-docs/blob/master/fix/schemas/spot-fix-md.xml).
-* Documentation update: updated the [News `<B>`](./fix-api.md#news-b) message description to be consistent with the announcement from [2026-06-09](#2026-06-09).
+- Documentation update: removed `LastFragment (893)` from
+  [FIX API](fix-api.md#marketdataincrementalrefresh).
+  - As [previously announced](#2025-12-02), `MarketDataIncrementalRefresh <X>` messages stopped
+    being fragmented on 2025-12-18, and the server no longer sends `LastFragment (893)`.
+  - The field has been removed from the [FIX API](fix-api.md) field list and from the
+    corresponding [QuickFIX MD schema](https://github.com/binance/binance-spot-api-docs/blob/master/fix/schemas/spot-fix-md.xml).
+- Documentation update: updated the [News `<B>`](fix-api.md#news-b) message description
+  to be consistent with the announcement from [2026-06-09](#2026-06-09).
 
 ---
@@ -87,14 +107,18 @@ REST and WebSocket API:
 **Update:**
 
-* Updated the [Price Range Execution Rule FAQ](./faqs/price_range_execution_rules.md#externalCalculationId1) with new External Reference Price Calculation Methods.
+- Updated the
+  [Price Range Execution Rule FAQ](faqs/price_range_execution_rules.md#external-reference-price-calculation-method-1)
+  with new External Reference Price Calculation Methods.
 
-The `serverShutdown` event will be sent when the **server is about to be shut down**; when you receive this event, please disconnect and open a new connection.
+The `serverShutdown` event will be sent when the **server is about to be shut down**; when you
+receive this event, please disconnect and open a new connection.
 
 All mention of a fixed time before the server shuts down has been removed from the documentation.
 
-* Documented the `serverShutdown` event in [SBE Market Data Streams](./sbe-market-data-streams.md#serverShutdown).
-  * ~~`serverShutdown` event will be sent 10 minutes before disconnection.~~
-  * Please establish a new connection as soon as possible to prevent connection interruption.
-  * Note that you will receive `serverShutdown` events in JSON in WebSocket text frames.
+- Documented the `serverShutdown` event in
+  [SBE Market Data Streams](sbe-market-data-streams.md#server-shutdown).
+  - ~~`serverShutdown` event will be sent 10 minutes before disconnection.~~
+  - Please establish a new connection as soon as possible to prevent connection interruption.
+  - Note that you will receive `serverShutdown` events in JSON in WebSocket text frames.
 
 ---
@@ -104,7 +128,8 @@ All mention of a fixed time before the server shuts down has been removed from t
 The following rollout will occur at **approximately 07:00 UTC on 2026-05-12**.
 
-* Added WebSocket Stream support for [Block Trades](https://www.binance.info/en/support/faq/detail/557f95eaf8fb4460aed0a891d42a1425).
-  * New stream:
-    * `<symbol>@blockTrade`
+- Added WebSocket Stream support for
+  [Block Trades](https://www.binance.info/en/support/faq/detail/557f95eaf8fb4460aed0a891d42a1425).
+  - New stream:
+    - `<symbol>@blockTrade`
 
 ---
@@ -112,39 +137,50 @@ The following rollout will occur at **approximately 07:00 UTC on 2026-05-12**.
 ### 2026-05-06
 
-**Notice: The following changes will be deployed on 2026-05-08, starting at 06:00 UTC and may take several hours to complete.**
-
-* Added `serverShutdown` event to [WebSocket API](./web-socket-api.md#serverShutdown) and [WebSocket Streams](./web-socket-streams.md#serverShutdown).
-  * `serverShutdown` event will be sent 10 minutes before disconnection.
-
-* [`PERCENT_PRICE`](./filters.md#percent_price), [`PERCENT_PRICE_BY_SIDE`](./filters.md#percent_price_by_side), [`MIN_NOTIONAL`](./filters.md#min_notional), and [`NOTIONAL`](./filters.md#notional) filters now use [reference price](./faqs/price_range_execution_rules.md) when it exists and is non-null. The filters fall back to their previous behavior when the reference price does not exist or is null.
-
-* Market data for [Block Trades](https://www.binance.info/en/support/faq/detail/557f95eaf8fb4460aed0a891d42a1425).
-  * New Endpoints/Methods
-    * REST API:
-      * `GET /api/v3/historicalBlockTrades`
-    * WebSocket API:
-      * `blockTrades.historical`
-
-* Order query responses may include an [`expiryReason`](./enums.md#expiryreasons) field.
-  * This field is returned **only for expired orders** and helps users understand why an order expired, including cases where the order is expired due to the **execution price range rule**.
-  * This field is included in both JSON and SBE 3:4 responses.
-  * This applies to the following endpoint/method:
-    * REST API:
-      * `GET /api/v3/order`
-      * `GET /api/v3/allOrders`
-      * `GET /api/v3/orderList`
-      * `GET /api/v3/allOrderList`
-    * WebSocket API:
-      * `order.status`
-      * `allOrders`
-      * `orderList.status`
-      * `allOrderLists`
-
-* REST and WebSocket API SBE schema 3:4
-  * The current schema 3:3 [spot_3_3.xml](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot_3_3.xml) is deprecated and will be retired in 6 months as per our schema deprecation policy.
-  * Changes in schema 3:4:
-    * New message `BlockTradesResponse`
-    * New type `blockTradeId`
-    * New field `expiryReason` in `OrderResponse` and `OrdersResponse`
+**Notice: The following changes will be deployed on 2026-05-08, starting at 06:00 UTC and may take
+several hours to complete.**
+
+- Added `serverShutdown` event to [WebSocket API](web-socket-api.md#server-shutdown) and
+  [WebSocket Streams](web-socket-streams.md#server-shutdown).
+  - `serverShutdown` event will be sent 10 minutes before disconnection.
+
+- [`PERCENT_PRICE`](filters.md#percent_price),
+  [`PERCENT_PRICE_BY_SIDE`](filters.md#percent_price_by_side),
+  [`MIN_NOTIONAL`](filters.md#min_notional), and
+  [`NOTIONAL`](filters.md#notional) filters now use
... (diff truncated, total 4861 lines) ...
```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index b82c22c..198c079 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,6 @@
+2026-10-14​
+REST API​
+- Get Instrument Summary [NEW]
+  - Add GET /v5/market/instrument-summary to query summary information and trading increments for linear and option instruments.
 2026-10-13​
 REST API​

```

### Gate.io Futures WebSocket v4 (`gate-futures-ws`)
- Source: https://www.gate.io/docs/developers/futures/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/futures/ws/zh_CN/

```diff
diff --git a/changelogs/gate-futures-ws.txt b/changelogs/gate-futures-ws.txt
index 163b62c..a142e5e 100644
--- a/changelogs/gate-futures-ws.txt
+++ b/changelogs/gate-futures-ws.txt
@@ -479,59 +479,4 @@ futures.order_book
 - event
 unsubscribe
-# RPI 深度全量更新频道
-futures.rpi_order_book
-推送 RPI 订单簿的全量快照。本频道是公开频道。
-订阅参数和推送字段与 futures.order_book 相同。价格合并精度只支持 "0"。推送 event 为 all。
-SBE 复用 orderBook 模板（templateId=4），帧里的 channel 为 futures.rpi_order_book。
-# RPI 深度全量订阅
-代码示例
-from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.rpi_order_book","event": "subscribe", "payload" : ["BTC_USDT", "20", "0"]}') print(ws.recv())
-代码示例
-package main import ( "fmt" "log" "net/http" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.rpi_order_book","event":"subscribe","payload":["BTC_USDT","20","0"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
-上面的命令返回 JSON 结构如下:
-{ "time": 1545405058, "time_ms": 1545405058123, "channel": "futures.rpi_order_book", "event": "subscribe", "result": { "status": "success" } }
-订阅 RPI 深度.
-# 请求参数
-- channel
-futures.rpi_order_book
-- event
-subscribe
-- params
-| 名称 | 类型 | 必选 | 描述
-| contract | String | 是 | 合约名称
-| limit | String | 是 | 深度层级: 100, 50, 20, 10, 5
-| interval | String | 是 | 价格合并精度，只支持 "0"
-# RPI 全量深度推送
-{ "channel": "futures.rpi_order_book", "event": "all", "time": 1541500161, "time_ms": 1541500161123, "result": { "t": 1541500161123, "contract": "BTC_USDT", "id": 93973511, "asks": [ { "p": "97.1", "s": "2245.5" } ], "bids": [ { "p": "96.9", "s": "3100.2" } ], "l": "20" } }
-RPI 全量深度更新推送
-# 推送参数
-- channel
-futures.rpi_order_book
-- event
-all
-- params
-| 名称 | 类型 | 描述
-| result | object | 深度信息
-| »t | Integer | 深度生成时间戳（以毫秒为单位）
-| »contract | String | 合约名称
-| »id | Integer | 深度 ID
-| »asks | Array | 深度卖方的档位列表
-| »»p | String | 档位价格
-| »»s | String | 档位的数量
-| »bids | Array | 深度买方的档位列表
-| »»p | String | 档位价格
-| »»s | String | 档位的数量
-| »l | String | 深度层级（例如 20 即代表 20 层的深度更新）
-# RPI 全量深度取消订阅
-代码示例
-from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.rpi_order_book","event": "unsubscribe", "payload" : ["BTC_USDT", "20", "0"]}') print(ws.recv())
-代码示例
-package main import ( "fmt" "log" "net/http" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.rpi_order_book","event":"unsubscribe","payload":["BTC_USDT","20","0"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
-取消订阅指定市场的 RPI 深度
-# 请求参数
-- channel
-futures.rpi_order_book
-- event
-unsubscribe
 # 最佳买卖价订阅
 代码示例
@@ -639,4 +584,59 @@ futures.order_book_update
 - event
 unsubscribe
+# RPI 深度全量更新频道
+futures.rpi_order_book
+推送 RPI 订单簿的全量快照。本频道是公开频道。
+订阅参数和推送字段与 futures.order_book 相同。价格合并精度只支持 "0"。推送 event 为 all。
+SBE 复用 orderBook 模板（templateId=4），帧里的 channel 为 futures.rpi_order_book。
+# RPI 深度全量订阅
+代码示例
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.rpi_order_book","event": "subscribe", "payload" : ["BTC_USDT", "20", "0"]}') print(ws.recv())
+代码示例
+package main import ( "fmt" "log" "net/http" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.rpi_order_book","event":"subscribe","payload":["BTC_USDT","20","0"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+上面的命令返回 JSON 结构如下:
+{ "time": 1545405058, "time_ms": 1545405058123, "channel": "futures.rpi_order_book", "event": "subscribe", "result": { "status": "success" } }
+订阅 RPI 深度.
+# 请求参数
+- channel
+futures.rpi_order_book
+- event
+subscribe
+- params
+| 名称 | 类型 | 必选 | 描述
+| contract | String | 是 | 合约名称
+| limit | String | 是 | 深度层级: 100, 50, 20, 10, 5
+| interval | String | 是 | 价格合并精度，只支持 "0"
+# RPI 全量深度推送
+{ "channel": "futures.rpi_order_book", "event": "all", "time": 1541500161, "time_ms": 1541500161123, "result": { "t": 1541500161123, "contract": "BTC_USDT", "id": 93973511, "asks": [ { "p": "97.1", "s": "2245.5" } ], "bids": [ { "p": "96.9", "s": "3100.2" } ], "l": "20" } }
+RPI 全量深度更新推送
+# 推送参数
+- channel
+futures.rpi_order_book
+- event
+all
+- params
+| 名称 | 类型 | 描述
+| result | object | 深度信息
+| »t | Integer | 深度生成时间戳（以毫秒为单位）
+| »contract | String | 合约名称
+| »id | Integer | 深度 ID
+| »asks | Array | 深度卖方的档位列表
+| »»p | String | 档位价格
+| »»s | String | 档位的数量
+| »bids | Array | 深度买方的档位列表
+| »»p | String | 档位价格
+| »»s | String | 档位的数量
+| »l | String | 深度层级（例如 20 即代表 20 层的深度更新）
+# RPI 全量深度取消订阅
+代码示例
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.rpi_order_book","event": "unsubscribe", "payload" : ["BTC_USDT", "20", "0"]}') print(ws.recv())
+代码示例
+package main import ( "fmt" "log" "net/http" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.rpi_order_book","event":"unsubscribe","payload":["BTC_USDT","20","0"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+取消订阅指定市场的 RPI 深度
+# 请求参数
+- channel
+futures.rpi_order_book
+- event
+unsubscribe
 # 深度频道V2
 提供一种更快更新的获取深度信息的方法.
@@ -2242,3 +2242,3 @@ req_param` API 订单模型的 JSON 字节数据:
 | »»label | String | 错误类型
 | »»message | String | 详细错误信息
-Last Updated: 10/14/2026, 3:12:02 AM
+Last Updated: 10/14/2026, 7:46:30 AM

```
