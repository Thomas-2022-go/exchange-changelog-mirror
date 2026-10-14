<!-- has_changes=true date=2026-10-14 -->
# Exchange API Changelog Diff

Generated: 2026-10-14 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132590 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (217852 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [OK] Bybit V5 (`bybit`): no change (97765 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42424 bytes)

- [CHANGED] **Gate.io Spot WebSocket v4** (`gate-spot-ws`): 151 diff lines

- [CHANGED] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): 163 diff lines



## Changes

### Gate.io Spot WebSocket v4 (`gate-spot-ws`)
- Source: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/

```diff
diff --git a/changelogs/gate-spot-ws.txt b/changelogs/gate-spot-ws.txt
index aff8da4..363b616 100644
--- a/changelogs/gate-spot-ws.txt
+++ b/changelogs/gate-spot-ws.txt
@@ -19,4 +19,6 @@ TIP
 SDK 的源代码 在 gatews (opens new window) GitHub 仓库。
 # 变更历史
+2026-10-14
+- 新增公开频道 spot.rpi_order_book，spot.rpi_obu 推送 RPI 深度全量快照
 2026-08-31
 - spot.order_place 单笔和批量下单新增 trade_quote；RESULT 和 FULL 结果在下游返回实际计价资产时输出该字段。
@@ -179,7 +181,9 @@ WebSocket 认证使用与 Gate APIv4 API 相同的签名计算方法，即: HexE
 | spot.candlesticks | 6 | candlestick | K 线
 | spot.order_book | 4 | orderBook | 订单簿（全量深度）
+| spot.rpi_order_book | 4 | orderBook | RPI 订单簿（全量深度）
 | spot.order_book_update | 5 | orderBookUpdate | 订单簿增量更新
 | spot.book_ticker | 1 | bbo | 最优买卖价（BBO）
 | spot.obu | 3 | obu | 订单簿增量（OBU）
+| spot.rpi_obu | 3 | obu | RPI 订单簿增量（OBU）
 | spot.usertrades | 8 | userTrade | 用户成交
 | spot.orders | 9 | orders | 订单
@@ -399,5 +403,5 @@ TIP
 | »w | Boolean | true 表示窗口已关闭。注：可能会缺失 true 的消息，但不影响数据的完整性
 # 订单簿/深度频道
-深度有 3 个订阅频道，分别满足不同的需求。它们是:
+深度有以下订阅频道，分别满足不同的需求。它们是:
 - spot.book_ticker
 及时推送订阅货币对的最优卖/买（ask/bid）单。
@@ -406,4 +410,6 @@ TIP
 - spot.order_book
 基于订阅的 level，定时推送深度全量更新
+- spot.rpi_order_book
+基于订阅的 level，定时推送 RPI 深度全量更新
 每个货币对的深度更新都有一个内部更新 ID，该 ID 在每个订单成交后递增 1。深度更新 ID 对应于 REST API 的 GET /api/v4/spot/order_book 响应中的ID 字段。
 如何维护本地订单簿/深度：
@@ -521,6 +527,51 @@ TIP
 | » asks | Array[OrderBookArray] | 在当前快照的 顶层 asks（卖单） 数据，按价格从低到高排序
 | »» OrderBookArray | Array[String] | [Price, Amount] 数组对
+# RPI 深度全量更新频道
+spot.rpi_order_book
+推送 RPI 订单簿的全量快照。本频道是公开频道。
+订阅参数和推送字段与 spot.order_book 相同。同一时刻两条频道的买卖盘可以不同，本频道对齐 RPI 盘口。
+更新速度: 100ms、500ms 或 1000ms
+SBE 复用 orderBook 模板（templateId=4），帧里的 channel 为 spot.rpi_order_book。
+# 客户端订阅
+代码示例：
+import time import json # pip install websocket_client from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/") ws.send(json.dumps({ "time": int(time.time()), "channel": "spot.rpi_order_book", "event": "subscribe", # "unsubscribe" for unsubscription "payload": ["BTC_USDT", "20", "100ms"] })) print(ws.recv())
+代码示例：
+package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" ) func main() { url := "wss://api.gateio.ws/ws/v4/" conn, _, err := websocket.DefaultDialer.Dial(url, nil) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() subscribe := map[string]interface{}{ "time": time.Now().Unix(), "channel": "spot.rpi_order_book", "event": "subscribe", "payload": []string{"BTC_USDT", "20", "100ms"}, } msg, err := json.Marshal(subscribe) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+订阅参数格式:
+| 字段 | 类型 | 必选 | 描述
+| payload | Array[String] | 是 | 订阅参数，从左到右分别是 cp, level, interval
+| » cp | String | 是 | 货币对
+| » level | String | 是 | 深度层级
+| » interval | String | 是 | 通知更新速度
+# 字段枚举值
+| Property | Value
+| level | 5
+| level | 10
+| level | 20
+| level | 30
+| level | 50
+| level | 100
+| interval | 100ms
+| interval | 500ms
+| interval | 1000ms
+取消订阅使用相同的 payload，event 改为 unsubscribe。
+# 服务端推送
+通知示例：
+{ "time": 1606295412, "time_ms": 1606295412213, "channel": "spot.rpi_order_book", "event": "update", "result": { "t": 1606295412123, "lastUpdateId": 48791820, "s": "BTC_USDT", "l": "20", "bids": [ ["19079.55", "0.0195"], ["19079.07", "0.7341"] ], "asks": [ ["19080.24", "0.1638"], ["19080.91", "0.1366"] ] } }
+通知结果格式：
+| 字段 | 类型 | 描述
+| result | Object | 深度信息
+| » t | Integer | 深度更新毫秒时间戳
+| » lastUpdateId | Integer | 深度副本当前的深度 ID
+| » s | String | 货币对
+| » l | String | 深度层级（例如 20 即代表 20 层的深度更新）
+| » bids | Array[OrderBookArray] | 在当前快照的顶层 bids（买单）数据，按价格从高到低排序
+| »» OrderBookArray | Array[String] | [Price, Amount] 数组对
+| » asks | Array[OrderBookArray] | 在当前快照的顶层 asks（卖单）数据，按价格从低到高排序
+| »» OrderBookArray | Array[String] | [Price, Amount] 数组对
+买卖档数不超过订阅的 level。
 # 深度频道V2
 提供一种更快更新的获取深度信息的方法.
+spot.obu 与 spot.rpi_obu 都使用这一套本地深度维护方式。spot.rpi_obu 见下方 RPI 深度频道V2。
 # 维护本地深度
 说明:
@@ -585,4 +636,58 @@ spot.obu
 - event
 unsubscribe
+# RPI 深度频道V2
+spot.rpi_obu
+推送 RPI 订单簿的全量和增量。本频道是公开频道。
+消息结构、本地深度维护方式与 深度频道V2 相同。流名称前缀为 rpi_ob.。
+SBE 复用 obu 模板（templateId=3），帧里的 channel 为 spot.rpi_obu。
+# RPI 深度频道V2订阅
+代码示例
+from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/") ws.send('{"time" : 123456, "channel" : "spot.rpi_obu", "event": "subscribe", "payload" : ["rpi_ob.BTC_USDT.50"]}') print(ws.recv())
+代码示例
+package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://api.gateio.ws/ws/v4/" conn, _, err := websocket.DefaultDialer.Dial(url, nil) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time" : 123456, "channel" : "spot.rpi_obu", "event": "subscribe", "payload" : ["rpi_ob.BTC_USDT.50"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+上面的命令返回 JSON 结构如下：
+{ "time": 1747054611, "time_ms": 1747054611614, "conn_id": "d7de96c024f2a5b2", "trace_id": "e6fd9bdd617fcdb80d0762ffa33e71f6", "channel": "spot.rpi_obu", "event": "subscribe", "payload": [ "rpi_ob.BTC_USDT.50" ], "result": { "status": "success" } }
+# 请求参数
+- channel
+spot.rpi_obu
+- event
+subscribe
+- params
+payload 是一个包含流名称的列表. 格式为: rpi_ob.{symbol}.{level}；例如 rpi_ob.BTC_USDT.400、rpi_ob.BTC_USDT.50
+其中 level 枚举为：400、50；更新频率: 400 档为 100ms；50 档为 20ms。
+订阅成功后，首条推送为全量（full=true），之后为增量。同一现货的同一深度流，一个链接只允许订阅一次。
+# RPI 深度v2订阅推送
+全量推送示例:
+{ "channel": "spot.rpi_obu", "result": { "t": 1747054612673, "full": true, "s": "rpi_ob.BTC_USDT.50", "u": 73777715168, "b": [ ["104027.1", "509392"], ["104027", "477932"] ], "a": [ ["104027.2", "44617"], ["104027.4", "39322"] ] }, "time_ms": 1747054612848 }
+增量推送示例:
+{ "channel": "spot.rpi_obu", "result": { "t": 1747054612695, "s": "rpi_ob.BTC_USDT.50", "U": 73777715169, "u": 73777715212, "b": [ ["104024.5", "10343"] ], "a": [ ["104027.2", "0"] ] }, "time_ms": 1747054612925 }
+RPI 深度频道V2的消息推送
+# 推送参数
+- channel
+spot.rpi_obu
+- event
+update
+- params
+| 名称 | 类型 | 描述
+| result | Object | 自上次更新以来发生变更的卖单和买单
+| »t | Integer | 订单簿生成时间戳（以毫秒为单位）
+| »full | Boolean | true 代表全量的深度；false 代表增量的深度，为 false 时，不传输该字段
+| »s | String | 深度流的名称，例如 rpi_ob.BTC_USDT.50
+| »U | Integer | 本次更新开始的订单簿更新 ID
+| »u | Integer | 本次更新结束的订单簿更新 ID
+| »b | Array[OrderBookArray] | 自上次更新以来的 bids 更新
+| »» OrderBookArray | Array[String] | [Price, Amount] 数组对, Amount=0 应当从本地深度中移除
+| »a | Array[OrderBookArray] | 自上次更新以来的 asks 更新
+| »» OrderBookArray | Array[String] | [Price, Amount] 数组对, Amount=0 应当从本地深度中移除
+# RPI 深度频道V2取消订阅
+代码示例
+from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/") ws.send( '{"time" : 123456, "channel" : "spot.rpi_obu", "event": "unsubscribe", "payload" : ["rpi_ob.BTC_USDT.50"]}') print(ws.recv())
+代码示例
+package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://api.gateio.ws/ws/v4/" conn, _, err := websocket.DefaultDialer.Dial(url, nil) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time" : 123456, "channel" : "spot.rpi_obu", "event": "unsubscribe", "payload" : ["rpi_ob.BTC_USDT.50"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+# 请求参数
+- channel
+spot.rpi_obu
+- event
+unsubscribe
 # 订单频道
 spot.orders
@@ -1587,3 +1692,3 @@ account: 指定查询账户。不指定默认现货，保证金和逐仓杠杆
 | »»label | String | 以字符串格式表示错误类型
 | »»message | String | 错误信息详情
-Last Updated: 9/1/2026, 9:17:42 AM
+Last Updated: 10/14/2026, 3:12:02 AM

```

### Gate.io Futures WebSocket v4 (`gate-futures-ws`)
- Source: https://www.gate.io/docs/developers/futures/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/futures/ws/zh_CN/

```diff
diff --git a/changelogs/gate-futures-ws.txt b/changelogs/gate-futures-ws.txt
index 776d5cd..163b62c 100644
--- a/changelogs/gate-futures-ws.txt
+++ b/changelogs/gate-futures-ws.txt
@@ -26,4 +26,6 @@ WebSocket 应用示例
 WebSocket 应用示例
 package main import ( "crypto/hmac" "crypto/sha512" "crypto/tls" "encoding/hex" "encoding/json" "fmt" "io" "net/http" "net/url" "time" "github.com/gorilla/websocket" ) type Msg struct { Time int64 `json:"time"` Channel string `json:"channel"` Event string `json:"event"` Payload []string `json:"payload"` Auth *Auth `json:"auth"` } type Auth struct { Method string `json:"method"` KEY string `json:"KEY"` SIGN string `json:"SIGN"` } const ( Key = "YOUR_API_KEY" Secret = "YOUR_API_SECRETY" ) func sign(channel, event string, t int64) string { message := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, t) h2 := hmac.New(sha512.New, []byte(Secret)) io.WriteString(h2, message) return hex.EncodeToString(h2.Sum(nil)) } func (msg *Msg) sign() { signStr := sign(msg.Channel, msg.Event, msg.Time) msg.Auth = &Auth{ Method: "api_key", KEY: Key, SIGN: signStr, } } func (msg *Msg) send(c *websocket.Conn) error { msgByte, err := json.Marshal(msg) if err != nil { return err } return c.WriteMessage(websocket.TextMessage, msgByte) } func NewMsg(channel, event string, t int64, payload []string) *Msg { return &Msg{ Time: t, Channel: channel, Event: event, Payload: payload, } } func main() { u := url.URL{Scheme: "wss", Host: "fx-ws.gateio.ws", Path: "/v4/ws/usdt"} websocket.DefaultDialer.TLSClientConfig = &tls.Config{RootCAs: nil, InsecureSkipVerify: true} c, _, err := websocket.DefaultDialer.Dial(u.String(), http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { panic(err) } c.SetPingHandler(nil) // read msg go func() { for { _, message, err := c.ReadMessage() if err != nil { c.Close() panic(err) } fmt.Printf("recv: %s\n", message) } }() t := time.Now().Unix() pingMsg := NewMsg("futures.ping", "", t, []string{}) err = pingMsg.send(c) if err != nil { panic(err) } // subscribe order book orderBookMsg := NewMsg("futures.order_book", "subscribe", t, []string{"BTC_USDT"}) err = orderBookMsg.send(c) if err != nil { panic(err) } // subscribe positions positionsMsg := NewMsg("futures.positions", "subscribe", t, []string{"USERID", "BTC_USDT"}) positionsMsg.sign() err = positionsMsg.send(c) if err != nil { panic(err) } select {} }
+2026-10-14
+- 新增公开频道 futures.rpi_order_book，futures.rpi_obu 推送 RPI 深度全量快照
 2026-08-25
 - 新增市场级 ADL 风险预警公共频道 futures.adl_warning
@@ -244,7 +246,9 @@ package main import ( "crypto/hmac" "crypto/sha512" "encoding/hex" "encoding/jso
 | futures.trades | 公共成交
 | futures.order_book | 订单簿（深度）
+| futures.rpi_order_book | RPI 订单簿（深度）
 | futures.order_book_update | 订单簿增量更新
 | futures.book_ticker | 最优买卖（BBO）
 | futures.obu | 订单簿增量（OBU）
+| futures.rpi_obu | RPI 订单簿增量（OBU）
 | futures.candlesticks | K 线
 | futures.tickers | 行情
@@ -402,7 +406,9 @@ unsubscribe
 # 深度频道
 order_book 频道允许您跟踪 Gate 订单簿深度的状态。它以价格聚合的方式提供，可自定义精度。
-共有三种不同的订单簿渠道可供订阅:
+共有以下订单簿渠道可供订阅:
 - futures.order_book
 全量频道，定期使用all推送完整的有限级别订单簿.
+- futures.rpi_order_book
+RPI 全量频道，定期使用all推送有限级别订单簿。价格合并精度只支持 0.
 - futures.book_ticker
 实时推送最佳买价和卖价.
@@ -473,4 +479,59 @@ futures.order_book
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
 # 最佳买卖价订阅
 代码示例
@@ -580,4 +641,5 @@ unsubscribe
 # 深度频道V2
 提供一种更快更新的获取深度信息的方法.
+futures.obu 与 futures.rpi_obu 都使用这一套本地深度维护方式。futures.rpi_obu 见下方 RPI 深度频道V2。
 # 维护本地深度
 说明:
@@ -642,4 +704,59 @@ futures.obu
 - event
 unsubscribe
+# RPI 深度频道V2
+futures.rpi_obu
+推送 RPI 订单簿的全量和增量。本频道是公开频道。
+消息结构、本地深度维护方式与 深度频道V2 相同。流名称前缀为 rpi_ob.。
+SBE 复用 obu 模板（templateId=3），帧里的 channel 为 futures.rpi_obu。
+# RPI 深度频道V2订阅
+代码示例
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.rpi_obu", "event": "subscribe", "payload" : ["rpi_ob.BTC_USDT.400"]}') print(ws.recv())
+代码示例
+package main import ( "fmt" "log" "net/http" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time" : 123456, "channel" : "futures.rpi_obu", "event": "subscribe", "payload" : ["rpi_ob.BTC_USDT.400"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+上面的命令返回 JSON 结构如下：
+{ "time": 1747391482, "time_ms": 1747391482384, "id": 1, "conn_id": "d9db9373dc5e081e", "trace_id": "ee001938590e183db957bd5ba71651c0", "channel": "futures.rpi_obu", "event": "subscribe", "payload": [ "rpi_ob.BTC_USDT.400" ], "result": { "status": "success" } }
+# 请求参数
+- channel
+futures.rpi_obu
+- event
+subscribe
+- params
+payload 是一个包含流名称的列表. 格式为: rpi_ob.{symbol}.{level}；例如 rpi_ob.BTC_USDT.400、rpi_ob.BTC_USDT.50
+其中 level 枚举为：400、50；更新频率: 400 档为 100ms；50 档为 20ms。
+订阅成功后，首条推送为全量（full=true），之后为增量。同一合约的同一深度流，一个链接只允许订阅一次。
+# RPI 深度v2订阅推送
+全量推送示例:
+{ "channel": "futures.rpi_obu", "result": { "t": 1743673026995, "full": true, "s": "rpi_ob.BTC_USDT.400", "u": 79072179673, "b": [ ["83705.9", "30166"] ], "a": [ ["83706", "4208"] ] }, "time_ms": 1743673026999 }
+增量推送示例:
+{ "channel": "futures.rpi_obu", "result": { "t": 1743673027017, "s": "rpi_ob.BTC_USDT.400", "U": 79072179674, "u": 79072179694, "b": [ ["83702.2", "62"], ["83702.1", "0"] ] }, "time_ms": 1743673027020 }
+RPI 深度频道V2的消息推送
+# 推送参数
+- channel
+futures.rpi_obu
+- event
+update
+- params
+| 名称 | 类型 | 描述
+| result | Object | 自上次更新以来发生变更的卖单和买单
+| »t | Integer | 订单簿生成时间戳（以毫秒为单位）
+| »full | Boolean | true 代表全量的深度；false 代表增量的深度，为 false 时，不传输该字段
+| »s | String | 深度流的名称，例如 rpi_ob.BTC_USDT.400
+| »U | Integer | 本次更新开始的订单簿更新 ID
+| »u | Integer | 本次更新结束的订单簿更新 ID
+| »b | Array[OrderBookArray] | 自上次更新以来的 bids 更新
+| »» OrderBookArray | Array[String] | [Price, Amount] 数组对, Amount=0 应当从本地深度中移除
+| »a | Array[OrderBookArray] | 自上次更新以来的 asks 更新
+| »» OrderBookArray | Array[String] | [Price, Amount] 数组对, Amount=0 应当从本地深度中移除
+# RPI 深度频道V2取消订阅
+代码示例
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send( '{"time" : 123456, "channel" : "futures.rpi_obu", "event": "unsubscribe", "payload" : ["rpi_ob.BTC_USDT.400"]}') print(ws.recv())
+代码示例
+package main import ( "fmt" "log" "net/http" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time" : 123456, "channel" : "futures.rpi_obu", "event": "unsubscribe", "payload" : ["rpi_ob.BTC_USDT.400"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+取消指定合约的 RPI 深度频道V2订阅
+# 请求参数
+- channel
+futures.rpi_obu
+- event
+unsubscribe
 # K 线频道
 提供一种访问 K 线信息的方法.
@@ -2125,3 +2242,3 @@ req_param` API 订单模型的 JSON 字节数据:
 | »»label | String | 错误类型
 | »»message | String | 详细错误信息
-Last Updated: 8/25/2026, 6:35:20 AM
+Last Updated: 10/14/2026, 3:12:02 AM

```
