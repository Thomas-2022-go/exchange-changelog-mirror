<!-- has_changes=true date=2026-05-26 -->
# Exchange API Changelog Diff

Generated: 2026-05-26 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128989 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [OK] OKX V5 (`okx`): no change (194741 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 16 diff lines

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 11 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [CHANGED] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): 474 diff lines



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 2863f5f..9d17fe0 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,11 @@
+2026-05-28​
+REST API​
+- Get Crypto Loan Position [UPDATE]
+  - Add new response field colRes (platform level collateral restriction status)
+- Get Wallet Balance [UPDATE]
+  - Add new response field colRes (platform level collateral restriction status)
+Websocket API​
+- Wallet [UPDATE]
+  - Add new response field colRes (platform level collateral restriction status)
 2026-05-26​
 Websocket API​

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index 4aeda20..852f962 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -12,5 +12,5 @@ Added new enum value:MARGIN
 [Modify] Classic REST Get Trade History
 For liquidation orders, the tradeType will return the value: liquid
-[修改]Pro Websocket Execution Lite
+[Modify]Pro Websocket Execution Lite
 Push to add clientOid field
 [Add] Pro REST Get API Key Info

```

### Gate.io Futures WebSocket v4 (`gate-futures-ws`)
- Source: https://www.gate.io/docs/developers/futures/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/futures/ws/zh_CN/

```diff
diff --git a/changelogs/gate-futures-ws.txt b/changelogs/gate-futures-ws.txt
index f49d4be..bbef65e 100644
--- a/changelogs/gate-futures-ws.txt
+++ b/changelogs/gate-futures-ws.txt
@@ -194,7 +194,7 @@ WebSocket 认证使用与 HTTP API 相同的签名计算方法，但具有 以
 - 身份验证信息在请求正文中的auth字段中发送。
 代码示例
-# example WebSocket signature calculation implementation in Python import hmac, hashlib, json, time def gen_sign(channel, event, timestamp): # GateAPIv4 key pair api_key = 'YOUR_API_KEY' api_secret = 'YOUR_API_SECRET' s = 'channel=%s&event=%s&time=%d' % (channel, event, timestamp) sign = hmac.new(api_secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest() return {'method': 'api_key', 'KEY': api_key, 'SIGN': sign} request = { 'id': int(time.time() * 1e6), 'time': int(time.time()), 'channel': 'futures.orders', 'event': 'subscribe', 'payload': ["20011", "BTC_USD"] } request['auth'] = gen_sign(request['channel'], request['event'], request['time']) print(json.dumps(request))
+# example WebSocket signature calculation implementation in Python import hmac, hashlib, json, time def gen_sign(channel, event, timestamp): # GateAPIv4 key pair api_key = 'YOUR_API_KEY' api_secret = 'YOUR_API_SECRET' s = 'channel=%s&event=%s&time=%d' % (channel, event, timestamp) sign = hmac.new(api_secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest() return {'method': 'api_key', 'KEY': api_key, 'SIGN': sign} request = { 'id': int(time.time() * 1e6), 'time': int(time.time()), 'channel': 'futures.orders', 'event': 'subscribe', 'payload': ["20011", "BTC_USDT"] } request['auth'] = gen_sign(request['channel'], request['event'], request['time']) print(json.dumps(request))
 代码示例
-package main import ( "crypto/hmac" "crypto/sha512" "encoding/hex" "encoding/json" "fmt" "time" ) func genSign(channel, event string, timestamp int64) map[string]string { apiKey := "YOUR_API_KEY" apiSecret := "YOUR_API_SECRET" s := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, timestamp) h := hmac.New(sha512.New, []byte(apiSecret)) h.Write([]byte(s)) sign := hex.EncodeToString(h.Sum(nil)) return map[string]string{ "method": "api_key", "KEY": apiKey, "SIGN": sign, } } func main() { timestamp := time.Now().Unix() request := map[string]interface{}{ "id": time.Now().UnixNano() / 1e3, "time": timestamp, "channel": "futures.orders", "event": "subscribe", "payload": []string{"20011", "BTC_USD"}, } request["auth"] = genSign(request["channel"].(string), request["event"].(string), timestamp) jsonBytes, _ := json.Marshal(request) fmt.Println(string(jsonBytes)) }
+package main import ( "crypto/hmac" "crypto/sha512" "encoding/hex" "encoding/json" "fmt" "time" ) func genSign(channel, event string, timestamp int64) map[string]string { apiKey := "YOUR_API_KEY" apiSecret := "YOUR_API_SECRET" s := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, timestamp) h := hmac.New(sha512.New, []byte(apiSecret)) h.Write([]byte(s)) sign := hex.EncodeToString(h.Sum(nil)) return map[string]string{ "method": "api_key", "KEY": apiKey, "SIGN": sign, } } func main() { timestamp := time.Now().Unix() request := map[string]interface{}{ "id": time.Now().UnixNano() / 1e3, "time": timestamp, "channel": "futures.orders", "event": "subscribe", "payload": []string{"20011", "BTC_USDT"}, } request["auth"] = genSign(request["channel"].(string), request["event"].(string), timestamp) jsonBytes, _ := json.Marshal(request) fmt.Println(string(jsonBytes)) }
 您可以登录账户获取永续合约账户的 api_key 和 secret。
 | 名称 | 类型 | 描述
@@ -251,7 +251,7 @@ websocket rfc 协议 (opens new window)
 如果想主动检测连接状态，可以发送应用层 ping 消息，并接收 pong 消息。
 代码示例
-from websocket import create_connection ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/btc") ws.send('{"time" : 123456, "channel" : "futures.ping"}') print(ws.recv())
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.ping"}') print(ws.recv())
 代码示例
-package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws-testnet.gateio.ws/v4/ws/btc" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() ping := map[string]interface{}{ "time": time.Now().Unix(), "channel": "futures.ping", } msg, err := json.Marshal(ping) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() ping := map[string]interface{}{ "time": time.Now().Unix(), "channel": "futures.ping", } msg, err := json.Marshal(ping) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 futures.ping操作返回 JSON 结构如下：
 { "time": 1545404023, "time_ms": 1545404023123, "channel": "futures.pong", "event": "", "result": null }
@@ -272,7 +272,7 @@ ticker是合约状态的高级概述。它向你展示了最高的， 最低的
 # 订阅操作
 代码示例
-from websocket import create_connection ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/btc") ws.send('{"time" : 123456, "channel" : "futures.tickers","event": "subscribe", "payload" : ["BTC_USD"]}') print(ws.recv())
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.tickers","event": "subscribe", "payload" : ["BTC_USDT"]}') print(ws.recv())
 代码示例
-package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws-testnet.gateio.ws/v4/ws/btc" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.tickers","event":"subscribe","payload":["BTC_USD"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.tickers","event":"subscribe","payload":["BTC_USDT"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的订阅请求返回 JSON 结构如下：
 { "time": 1545404023, "time_ms": 1545404023123, "channel": "futures.tickers", "event": "subscribe", "result": { "status": "success" } }
@@ -287,5 +287,5 @@ subscribe
 | payload | Array | 是 | 合约列表
 # ticker 推送
-{ "time": 1541659086, "time_ms": 1541659086123, "channel": "futures.tickers", "event": "update", "result": [ { "contract": "BTC_USD", "last": "118.4", "change_percentage": "0.77", "funding_rate": "-0.000114", "funding_rate_indicative": "0.01875", "mark_price": "118.35", "index_price": "118.36", "total_size": "73648", "volume_24h": "745487577", "volume_24h_btc": "117", "volume_24h_usd": "419950", "quanto_base_rate": "", "volume_24h_quote": "1665006", "volume_24h_settle": "178", "volume_24h_base": "5526", "low_24h": "99.2", "high_24h": "132.5" } ] }
+{ "time": 1541659086, "time_ms": 1541659086123, "channel": "futures.tickers", "event": "update", "result": [ { "contract": "BTC_USDT", "last": "118.4", "change_percentage": "0.77", "funding_rate": "-0.000114", "funding_rate_indicative": "0.01875", "mark_price": "118.35", "index_price": "118.36", "total_size": "73648", "volume_24h": "745487577", "volume_24h_btc": "117", "volume_24h_usd": "419950", "quanto_base_rate": "", "volume_24h_quote": "1665006", "volume_24h_settle": "178", "volume_24h_base": "5526", "low_24h": "99.2", "high_24h": "132.5" } ] }
 永续合约 24hr 价格变动情况推送
 # 推送参数
@@ -317,7 +317,7 @@ update
 # 取消订阅
 代码示例
-import json from websocket import create_connection ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/btc") req = { "time": 123456, "channel": "futures.tickers", "event": "unsubscribe", "payload": ["BTC_USD"] } ws.send(json.dumps(req)) print(ws.recv())
+import json from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") req = { "time": 123456, "channel": "futures.tickers", "event": "unsubscribe", "payload": ["BTC_USDT"] } ws.send(json.dumps(req)) print(ws.recv())
 代码示例
-package main import ( "encoding/json" "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws-testnet.gateio.ws/v4/ws/btc" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() req := map[string]interface{}{ "time": 123456, "channel": "futures.tickers", "event": "unsubscribe", "payload": []string{"BTC_USD"}, } msg, err := json.Marshal(req) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+package main import ( "encoding/json" "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() req := map[string]interface{}{ "time": 123456, "channel": "futures.tickers", "event": "unsubscribe", "payload": []string{"BTC_USDT"}, } msg, err := json.Marshal(req) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的命令返回 JSON 结构如下：
 { "time": 1545404900, "time_ms": 1545404900123, "channel": "futures.tickers", "event": "unsubscribe", "result": { "status": "success" } }
@@ -332,7 +332,7 @@ unsubscribe
 # 公有成交订阅
 代码示例
-from websocket import create_connection ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/btc") ws.send('{"time" : 123456, "channel" : "futures.trades","event": "subscribe", "payload" : ["BTC_USD"]}') print(ws.recv())
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.trades","event": "subscribe", "payload" : ["BTC_USDT"]}') print(ws.recv())
 代码示例
-package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws-testnet.gateio.ws/v4/ws/btc" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.trades","event":"subscribe","payload":["BTC_USD"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.trades","event":"subscribe","payload":["BTC_USDT"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的命令返回 JSON 结构如下：
 { "time": 1545405058, "time_ms": 1545405058123, "channel": "futures.trades", "event": "subscribe", "result": { "status": "success" } }
@@ -348,5 +348,5 @@ subscribe
 # 公有成交推送
 size 正数表示买家，负数表示卖家
-{ "channel": "futures.trades", "event": "update", "time": 1541503698, "time_ms": 1541503698123, "result": [ { "size": "-108", "id": 27753479, "create_time": 1545136464, "create_time_ms": 1545136464123, "price": "96.4", "contract": "BTC_USD", "is_internal": true } ] }
+{ "channel": "futures.trades", "event": "update", "time": 1541503698, "time_ms": 1541503698123, "result": [ { "size": "-108", "id": 27753479, "create_time": 1545136464, "create_time_ms": 1545136464123, "price": "96.4", "contract": "BTC_USDT", "is_internal": true } ] }
 通知最新交易更新
 # 推送参数
@@ -368,7 +368,7 @@ update
 # 取消订阅
 代码示例
-from websocket import create_connection ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/btc") ws.send( '{"time" : 123456, "channel" : "futures.trades", "event": "subscribe", "payload" : ["BTC_USD"]}') print(ws.recv())
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send( '{"time" : 123456, "channel" : "futures.trades", "event": "subscribe", "payload" : ["BTC_USDT"]}') print(ws.recv())
 代码示例
-package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws-testnet.gateio.ws/v4/ws/btc" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.trades","event":"subscribe","payload":["BTC_USD"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.trades","event":"subscribe","payload":["BTC_USDT"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的命令返回 JSON 结构如下：
 { "time": 1545404900, "time_ms": 1545404900123, "channel": "futures.trades", "event": "unsubscribe", "result": { "status": "success" } }
@@ -402,7 +402,7 @@ WARNING
 # 深度全量更新频道
 代码示例
-from websocket import create_connection ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/btc") ws.send('{"time" : 123456, "channel" : "futures.order_book","event": "subscribe", "payload" : ["BTC_USD", "20", "0"]}') print(ws.recv())
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.order_book","event": "subscribe", "payload" : ["BTC_USDT", "20", "0"]}') print(ws.recv())
 代码示例
-package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws-testnet.gateio.ws/v4/ws/btc" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.order_book","event":"subscribe","payload":["BTC_USD","20","0"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.order_book","event":"subscribe","payload":["BTC_USDT","20","0"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的命令返回 JSON 结构如下:
 { "time": 1545405058, "time_ms": 1545405058123, "channel": "futures.order_book", "event": "subscribe", "result": { "status": "success" } }
@@ -419,5 +419,5 @@ subscribe
 | interval | String | 是 | 价格合并精度: "0"
 # 全量深度推送
-{ "channel": "futures.order_book", "event": "all", "time": 1541500161, "time_ms": 1541500161123, "result": { "t": 1541500161123, "contract": "BTC_USD", "id": 93973511, "asks": [ { "p": "97.1", "s": "2245" }, { "p": "97.1", "s": "2245" } ], "bids": [ { "p": "97.1", "s": "2245" }, { "p": "97.1", "s": "2245" } ], "l": "20" } }
+{ "channel": "futures.order_book", "event": "all", "time": 1541500161, "time_ms": 1541500161123, "result": { "t": 1541500161123, "contract": "BTC_USDT", "id": 93973511, "asks": [ { "p": "97.1", "s": "2245" }, { "p": "97.1", "s": "2245" } ], "bids": [ { "p": "97.1", "s": "2245" }, { "p": "97.1", "s": "2245" } ], "l": "20" } }
 全量深度更新推送
 # 推送参数
@@ -441,7 +441,7 @@ all
 # 全量深度取消订阅
 代码示例
-from websocket import create_connection ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/btc") ws.send('{"time" : 123456, "channel" : "futures.order_book","event": "unsubscribe", "payload" : ["BTC_USD", "20", "0"]}') print(ws.recv())
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.order_book","event": "unsubscribe", "payload" : ["BTC_USDT", "20", "0"]}') print(ws.recv())
 代码示例
-package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws-testnet.gateio.ws/v4/ws/btc" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.order_book","event":"unsubscribe","payload":["BTC_USD","20","0"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.order_book","event":"unsubscribe","payload":["BTC_USDT","20","0"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的命令返回 JSON 结构如下：
 { "time": 1545445847, "time_ms": 1545445847123, "channel": "futures.order_book", "event": "unsubscribe", "result": { "status": "success" } }
@@ -469,5 +469,5 @@ payload是一个包含合约市场的列表.
 # 最佳买卖价的推送
 如果 a 为空字符串，则表示空买价；如果 b 为空字符串，则表示空卖价。
-{ "time": 1615366379, "time_ms": 1615366379123, "channel": "futures.book_ticker", "event": "update", "result": { "t": 1615366379123, "u": 2517661076, "s": "BTC_USD", "b": "54696.6", "B": "37000", "a": "54696.7", "A": "47061" } }
+{ "time": 1615366379, "time_ms": 1615366379123, "channel": "futures.book_ticker", "event": "update", "result": { "t": 1615366379123, "u": 2517661076, "s": "BTC_USDT", "b": "54696.6", "B": "37000", "a": "54696.7", "A": "47061" } }
 最新买卖价的推送
 # 推送参数
@@ -518,5 +518,5 @@ subscribe
 | level | String | 否 | 可选的深度层级。允许以下层级：100、50、20；20ms频率 只支持 20层
 # 深度更新推送
-{ "time": 1615366381, "time_ms": 1615366381123, "channel": "futures.order_book_update", "event": "update", "result": { "t": 1615366381417, "s": "BTC_USD", "U": 2517661101, "u": 2517661113, "b": [ { "p": "54672.1", "s": "0" }, { "p": "54664.5", "s": "58794" } ], "a": [ { "p": "54743.6", "s": "0" }, { "p": "54742", "s": "95" } ], "l": "100" } }
+{ "time": 1615366381, "time_ms": 1615366381123, "channel": "futures.order_book_update", "event": "update", "result": { "t": 1615366381417, "s": "BTC_USDT", "U": 2517661101, "u": 2517661113, "b": [ { "p": "54672.1", "s": "0" }, { "p": "54664.5", "s": "58794" } ], "a": [ { "p": "54743.6", "s": "0" }, { "p": "54742", "s": "95" } ], "l": "100" } }
 深度更新推送
 # 推送参数
@@ -568,7 +568,7 @@ unsubscribe
 # 深度频道V2订阅
 代码示例
-from websocket import create_connection ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.obu", "event": "subscribe", "payload" : ["ob.BTC_USDT.400"]}') print(ws.recv())
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.obu", "event": "subscribe", "payload" : ["ob.BTC_USDT.400"]}') print(ws.recv())
 代码示例
-package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws-testnet.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time" : 123456, "channel" : "futures.obu", "event": "subscribe", "payload" : ["ob.BTC_USDT.400"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time" : 123456, "channel" : "futures.obu", "event": "subscribe", "payload" : ["ob.BTC_USDT.400"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的命令返回 JSON 结构如下：
 { "time": 1747391482, "time_ms": 1747391482384, "id": 1, "conn_id": "d9db9373dc5e081e", "trace_id": "ee001938590e183db957bd5ba71651c0", "channel": "futures.obu", "event": "subscribe", "payload": [ "ob.BTC_USDT.400" ], "result": { "status": "success" } }
@@ -606,7 +606,7 @@ update
 # 深度频道V2取消订阅
 代码示例
-from websocket import create_connection ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/btc") ws.send( '{"time" : 123456, "channel" : "futures.obu", "event": "unsubscribe", "payload" : ["ob.BTC_USDT.400"]}') print(ws.recv())
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send( '{"time" : 123456, "channel" : "futures.obu", "event": "unsubscribe", "payload" : ["ob.BTC_USDT.400"]}') print(ws.recv())
 代码示例
-package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws-testnet.gateio.ws/v4/ws/btc" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time" : 123456, "channel" : "futures.obu", "event": "unsubscribe", "payload" : ["ob.BTC_USDT.400"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time" : 123456, "channel" : "futures.obu", "event": "unsubscribe", "payload" : ["ob.BTC_USDT.400"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的命令返回 JSON 结构如下：
 { "time": 1743673617, "time_ms": 1743673617242, "id": 1, "conn_id": "7b06ff199a98ab0e", "trace_id": "8f86e4021a84440e502f73fde5b94918", "channel": "futures.obu", "event": "unsubscribe", "payload": ["ob.BTC_USDT.400"], "result": { "status": "success" } }
@@ -622,7 +622,7 @@ unsubscribe
 如果在contract前面加上mark_，则将订阅合约的标记价格 K 线；如果 前缀为“index_”，将订阅指数价格 K 线.
 代码示例
-from websocket import create_connection ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/btc") ws.send('{"time" : 123456, "channel" : "futures.candlesticks","event": "subscribe", "payload" : ["1m", "BTC_USD"]}') print(ws.recv())
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.candlesticks","event": "subscribe", "payload" : ["1m", "BTC_USDT"]}') print(ws.recv())
 代码示例
-package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws-testnet.gateio.ws/v4/ws/btc" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.candlesticks","event":"subscribe","payload":["1m", "BTC_USD"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.candlesticks","event":"subscribe","payload":["1m", "BTC_USDT"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的命令返回 JSON 结构如下：
 { "time": 1545445847, "time_ms": 1545445847123, "channel": "futures.candlesticks", "event": "subscribe", "result": { "status": "success" } }
@@ -637,5 +637,5 @@ subscribe
 | contract | String | 合约名称
 # k 线消息推送
-{ "time": 1542162490, "time_ms": 1542162490123, "channel": "futures.candlesticks", "event": "update", "result": [ { "t": 1545129300, "v": "27525555", "c": "95.4", "h": "96.9", "l": "89.5", "o": "94.3", "n": "1m_BTC_USD", "a": "314732.87412", "w": false }, { "t": 1545129300, "v": "27525555", "c": "95.4", "h": "96.9", "l": "89.5", "o": "94.3", "n": "1m_BTC_USD", "a": "314732.87412", "w": true } ] }
+{ "time": 1542162490, "time_ms": 1542162490123, "channel": "futures.candlesticks", "event": "update", "result": [ { "t": 1545129300, "v": "27525555", "c": "95.4", "h": "96.9", "l": "89.5", "o": "94.3", "n": "1m_BTC_USDT", "a": "314732.87412", "w": false }, { "t": 1545129300, "v": "27525555", "c": "95.4", "h": "96.9", "l": "89.5", "o": "94.3", "n": "1m_BTC_USDT", "a": "314732.87412", "w": true } ] }
 k 线的消息推送
 # 推送参数
@@ -659,7 +659,7 @@ update
 # 取消订阅
 代码示例
-from websocket import create_connection ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/btc") ws.send( '{"time" : 123456, "channel" : "futures.candlesticks", "event": "unsubscribe", "payload" : ["1m", "BTC_USD"]}') print(ws.recv())
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send( '{"time" : 123456, "channel" : "futures.candlesticks", "event": "unsubscribe", "payload" : ["1m", "BTC_USDT"]}') print(ws.recv())
 代码示例
-package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws-testnet.gateio.ws/v4/ws/btc" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.candlesticks","event":"unsubscribe","payload":["1m", "BTC_USD"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.candlesticks","event":"unsubscribe","payload":["1m", "BTC_USDT"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的命令返回 JSON 结构如下：
 { "time": 1545445847, "time_ms": 1545445847123, "channel": "futures.candlesticks", "event": "unsubscribe", "result": { "status": "success" } }
@@ -675,7 +675,7 @@ unsubscribe
 如果您想订阅所有合约中的强平订单推送，请在订阅请求列表中使用 !all
 代码示例
-import json from websocket import create_connection ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/btc") req = { "time": 123456, "channel": "futures.public_liquidates", "event": "subscribe", "payload": ["BTC_USD","ETH_USD"], } ws.send(json.dumps(req)) print(ws.recv())
+import json from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") req = { "time": 123456, "channel": "futures.public_liquidates", "event": "subscribe", "payload": ["BTC_USDT","BTC_USDT"], } ws.send(json.dumps(req)) print(ws.recv())
 代码示例
-package main import ( "fmt" "log" "encoding/json" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws-testnet.gateio.ws/v4/ws/btc" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() req := map[string]interface{}{ "time": 123456, "channel": "futures.public_liquidates", "event": "subscribe", "payload": []string{"BTC_USD", "ETH_USD"}, } msg, err := json.Marshal(req) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+package main import ( "fmt" "log" "encoding/json" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() req := map[string]interface{}{ "time": 123456, "channel": "futures.public_liquidates", "event": "subscribe", "payload": []string{"BTC_USDT", "BTC_USDT"}, } msg, err := json.Marshal(req) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的命令返回 JSON 结构如下：
 { "time": 1545459681, "time_ms": 1545459681123, "channel": "futures.public_liquidates", "event": "subscribe", "result": { "status": "success" } }
@@ -690,5 +690,5 @@ subscribe
 | contract | String | 是 | 合约名称列表
 # 公共强平订单推送
-{ "channel": "futures.public_liquidates", "event": "update", "time": 1541505434, "time_ms": 1541505434123, "result": [ { "price": 215.1, "size": "-124", "time_ms": 1541486601123, "contract": "BTC_USD", } ] }
+{ "channel": "futures.public_liquidates", "event": "update", "time": 1541505434, "time_ms": 1541505434123, "result": [ { "price": 215.1, "size": "-124", "time_ms": 1541486601123, "contract": "BTC_USDT", } ] }
 推送公共强制平仓更新
 # 推送参数
@@ -707,7 +707,7 @@ update
 # 取消订阅
 代码示例
-import json from websocket import create_connection ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/btc") req = { "time": 123456, "channel": "futures.public_liquidates", "event": "unsubscribe", "payload": ["BTC_USD"], } ws.send(json.dumps(req)) print(ws.recv())
+import json from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") req = { "time": 123456, "channel": "futures.public_liquidates", "event": "unsubscribe", "payload": ["BTC_USDT"], } ws.send(json.dumps(req)) print(ws.recv())
 代码示例
-package main import ( "fmt" "log" "encoding/json" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws-testnet.gateio.ws/v4/ws/btc" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() req := map[string]interface{}{ "time": 123456, "channel": "futures.public_liquidates", "event": "unsubscribe", "payload": []string{"BTC_USD"}, } msg, err := json.Marshal(req) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+package main import ( "fmt" "log" "encoding/json" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() req := map[string]interface{}{ "time": 123456, "channel": "futures.public_liquidates", "event": "unsubscribe", "payload": []string{"BTC_USDT"}, } msg, err := json.Marshal(req) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的命令返回 JSON 结构如下：
 { "time": 1545459681, "time_ms": 1545459681123, "channel": "futures.public_liquidates", "event": "unsubscribe", "result": { "status": "success" } }
@@ -722,7 +722,7 @@ contract_stats 通道允许您获取合约统计信息
 # 订阅操作
 代码示例
-from websocket import create_connection ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/btc") ws.send('{"time" : 123456, "channel" : "futures.contract_stats","event": "subscribe", "payload" : ["BTC_USD","1m"]}') print(ws.recv())
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.contract_stats","event": "subscribe", "payload" : ["BTC_USDT","1m"]}') print(ws.recv())
 代码示例
-package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws-testnet.gateio.ws/v4/ws/btc" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() message := `{ "time": 123456, "channel": "futures.contract_stats", "event": "subscribe", "payload": ["BTC_USD", "1m"] }` err = conn.WriteMessage(websocket.TextMessage, []byte(message)) if err != nil { log.Fatal("write error:", err) } _, msg, err := conn.ReadMessage() if err != nil { log.Fatal("read error:", err) } fmt.Println(string(msg)) }
... (diff truncated, total 474 lines) ...
```
