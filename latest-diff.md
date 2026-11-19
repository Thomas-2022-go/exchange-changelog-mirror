<!-- has_changes=true date=2026-11-19 -->
# Exchange API Changelog Diff

Generated: 2026-11-19 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (146418 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (220476 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3488 bytes)

- [OK] Bybit V5 (`bybit`): no change (101059 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 22 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [CHANGED] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): 70 diff lines



## Changes

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index 22cfeef..4b5fdc1 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,2 +1,17 @@
+2026.11.20#
+[Modify] UTA REST Get Symbol
+The response field st of the API now supports a new type:
+st (symbol type) previously supported spot only. Futures is now supported as well.
+[Add] UTA REST Get Small Balance Currencies
+Queries currencies eligible for small-balance conversion in FUNDING or SPOT accounts. The response includes the source amount, estimated KCS amount, and estimated fee in KCS.
+[Add] UTA REST Convert Small Balance
+Converts between 1 and 20 source currencies into KCS in a single request. The response includes the order status, net KCS total, and per-currency conversion amounts, fees, and statuses.
+[Add] UTA REST Get Small Balance Convert Order Detail
+Queries a small-balance conversion order by orderId or clientOrderId. The response includes the order status, net KCS total, order time, and per-currency conversion results.
+[Add] UTA REST Get Small Balance Convert Order History
+Returns paginated small-balance conversion order history for FUNDING or SPOT accounts. Supports optional start and end timestamps and returns page metadata with complete order details.
+[Modify] UTA REST Cancel Withdrawal
+api-rate-limit-pool change into Management
+[Add] UTA API V2 Error Code 111235, "Service busy, please reduce request frequency and retry later". Error code 111235 will replace 111202 and 111209, error codes 111202 and 111209 will be deprecated.
 2026.11.06#
 [Add] UTA WebSocket Private Channel FundingFeeSettle

```

### Gate.io Futures WebSocket v4 (`gate-futures-ws`)
- Source: https://www.gate.io/docs/developers/futures/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/futures/ws/zh_CN/

```diff
diff --git a/changelogs/gate-futures-ws.txt b/changelogs/gate-futures-ws.txt
index dcf2a0a..5d22328 100644
--- a/changelogs/gate-futures-ws.txt
+++ b/changelogs/gate-futures-ws.txt
@@ -26,4 +26,6 @@ WebSocket 应用示例
 WebSocket 应用示例
 package main import ( "crypto/hmac" "crypto/sha512" "crypto/tls" "encoding/hex" "encoding/json" "fmt" "io" "net/http" "net/url" "time" "github.com/gorilla/websocket" ) type Msg struct { Time int64 `json:"time"` Channel string `json:"channel"` Event string `json:"event"` Payload []string `json:"payload"` Auth *Auth `json:"auth"` } type Auth struct { Method string `json:"method"` KEY string `json:"KEY"` SIGN string `json:"SIGN"` } const ( Key = "YOUR_API_KEY" Secret = "YOUR_API_SECRETY" ) func sign(channel, event string, t int64) string { message := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, t) h2 := hmac.New(sha512.New, []byte(Secret)) io.WriteString(h2, message) return hex.EncodeToString(h2.Sum(nil)) } func (msg *Msg) sign() { signStr := sign(msg.Channel, msg.Event, msg.Time) msg.Auth = &Auth{ Method: "api_key", KEY: Key, SIGN: signStr, } } func (msg *Msg) send(c *websocket.Conn) error { msgByte, err := json.Marshal(msg) if err != nil { return err } return c.WriteMessage(websocket.TextMessage, msgByte) } func NewMsg(channel, event string, t int64, payload []string) *Msg { return &Msg{ Time: t, Channel: channel, Event: event, Payload: payload, } } func main() { u := url.URL{Scheme: "wss", Host: "fx-ws.gateio.ws", Path: "/v4/ws/usdt"} websocket.DefaultDialer.TLSClientConfig = &tls.Config{RootCAs: nil, InsecureSkipVerify: true} c, _, err := websocket.DefaultDialer.Dial(u.String(), http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { panic(err) } c.SetPingHandler(nil) // read msg go func() { for { _, message, err := c.ReadMessage() if err != nil { c.Close() panic(err) } fmt.Printf("recv: %s\n", message) } }() t := time.Now().Unix() pingMsg := NewMsg("futures.ping", "", t, []string{}) err = pingMsg.send(c) if err != nil { panic(err) } // subscribe order book orderBookMsg := NewMsg("futures.order_book", "subscribe", t, []string{"BTC_USDT"}) err = orderBookMsg.send(c) if err != nil { panic(err) } // subscribe positions positionsMsg := NewMsg("futures.positions", "subscribe", t, []string{"USERID", "BTC_USDT"}) positionsMsg.sign() err = positionsMsg.send(c) if err != nil { panic(err) } select {} }
+2026-11-19
+- 3.0 用户可在 futures.order_place、futures.order_cancel、futures.order_amend、futures.order_cancel_cp 的 payload.req_header 中传入 X-Gate-Client-Send-Us 和 X-Gate-Timeout-Window-Us。这两个参数在撮合引擎生效，撮合引擎按微秒发送时间和超时窗口拒绝过期请求。futures.order_batch_place、futures.order_cancel_ids、futures.order_list、futures.order_status 不转发这两个字段。详见 3.0 用户请求超时。
 2026-10-22
 - 补充 futures.adl_warning 的功能说明、三种市场级风险状态的含义，以及其与单个用户仓位和实际 ADL 事件的关系。
@@ -1864,4 +1866,25 @@ Error 推送示例（限速）
 | 311 | 合约限流
 | 312 | 合约成交比率限流
+# 3.0 用户请求超时
+3.0 用户可以在部分交易请求里声明客户端发送时间和允许的超时窗口，用来拒绝发出后已经过期的请求。
+这两个字段只写在 payload.req_header。不要写到 WebSocket 握手请求头，也不要写到 req_param。键名区分大小写，必须与下表一致。值必须是十进制整数字符串，单位是微秒。服务端不生成发送时间，只把非空值原样转发。
+| 字段 | 类型 | 必选 | 描述
+| X-Gate-Client-Send-Us | string | 否 | 客户端发出该请求的 Unix 时间戳，单位微秒。例如 1700000000123456
+| X-Gate-Timeout-Window-Us | string | 否 | 超时窗口，单位微秒。例如 500000 表示 500 毫秒
+这两个参数在撮合引擎生效。两个字段都传入有效值时，撮合引擎按下面的条件判断请求是否仍然有效：
+当前时间（微秒） - X-Gate-Client-Send-Us <= X-Gate-Timeout-Window-Us
+超出窗口的请求会被拒绝。
+适用频道：
+- futures.order_place
+- futures.order_cancel
+- futures.order_amend
+- futures.order_cancel_cp
+futures.order_batch_place、futures.order_cancel_ids、futures.order_list、futures.order_status 不转发这两个字段。
+- 仅 3.0 用户生效。其他用户传入这两个字段时，服务端不会转发。
+- 窗口判断需要两个字段同时有效。只传入其中一个时，服务端仍会转发这个非空值。
+- 空字符串，以及去掉首尾空格后为空的值，视为未传。首尾空格会被去掉后再转发。
+- 这与 x-gate-exptime 不是同一个字段。x-gate-exptime 仍是毫秒绝对时间，由 WebSocket 服务在收到请求时判断是否过期，单位不要和上面的微秒字段混用。
+下单时携带超时字段。撤单、改单、取消匹配的未结束订单使用同一组 req_header，替换 channel 和 req_param 即可。登录方式不变。
+{ "time": 1681195484, "channel": "futures.order_place", "event": "api", "payload": { "req_id": "request-id-1", "req_header": { "X-Gate-Client-Send-Us": "1700000000123456", "X-Gate-Timeout-Window-Us": "500000" }, "req_param": { "contract": "BTC_USDT", "size": "1", "price": "50000", "tif": "gtc" } } }
 # 登录
 WARNING
@@ -1944,4 +1967,6 @@ req_header 自定义 header 数据:
 | 字段 | 类型 | 必选 | 描述
 | x-gate-exptime | string | 否 | 指定过期的时间戳（毫秒）。如果 ws 收到请求的时间大于过期时间，请求将被拒绝
+| X-Gate-Client-Send-Us | string | 否 | 3.0 用户的客户端发送时间，单位微秒。须与 X-Gate-Timeout-Window-Us 同时传入，见 3.0 用户请求超时
+| X-Gate-Timeout-Window-Us | string | 否 | 3.0 用户的超时窗口，单位微秒。见 3.0 用户请求超时
 # 详细描述
 tif: 有效时间
@@ -2070,4 +2095,6 @@ req_header 自定义 header 数据:
 | 字段 | 类型 | 必选 | 描述
 | x-gate-exptime | string | 否 | 指定过期的时间戳（毫秒）。如果 ws 收到请求的时间大于过期时间，请求将被拒绝
+| X-Gate-Client-Send-Us | string | 否 | 3.0 用户的客户端发送时间，单位微秒。须与 X-Gate-Timeout-Window-Us 同时传入，见 3.0 用户请求超时
+| X-Gate-Timeout-Window-Us | string | 否 | 3.0 用户的超时窗口，单位微秒。见 3.0 用户请求超时
 # 订单取消通知
 订单取消返回示例
@@ -2160,4 +2187,6 @@ req_header 自定义 header 数据:
 | 字段 | 类型 | 必选 | 描述
 | x-gate-exptime | string | 否 | 指定过期的时间戳（毫秒）。如果 ws 收到请求的时间大于过期时间，请求将被拒绝
+| X-Gate-Client-Send-Us | string | 否 | 3.0 用户的客户端发送时间，单位微秒。须与 X-Gate-Timeout-Window-Us 同时传入，见 3.0 用户请求超时
+| X-Gate-Timeout-Window-Us | string | 否 | 3.0 用户的超时窗口，单位微秒。见 3.0 用户请求超时
 # 响应结果
 订单取消返回示例
@@ -2211,4 +2240,6 @@ req_header 自定义 header 数据:
 | 字段 | 类型 | 必选 | 描述
 | x-gate-exptime | string | 否 | 指定过期的时间戳（毫秒）。如果 ws 收到请求的时间大于过期时间，请求将被拒绝
+| X-Gate-Client-Send-Us | string | 否 | 3.0 用户的客户端发送时间，单位微秒。须与 X-Gate-Timeout-Window-Us 同时传入，见 3.0 用户请求超时
+| X-Gate-Timeout-Window-Us | string | 否 | 3.0 用户的超时窗口，单位微秒。见 3.0 用户请求超时
 # 详细描述
 => size: 新订单尺寸，包括已填充部分。
@@ -2328,3 +2359,3 @@ req_param` API 订单模型的 JSON 字节数据:
 | »»label | String | 错误类型
 | »»message | String | 详细错误信息
-Last Updated: 10/22/2026, 7:54:06 AM
+Last Updated: 11/19/2026, 2:06:06 AM

```
