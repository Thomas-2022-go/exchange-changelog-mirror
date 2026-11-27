<!-- has_changes=true date=2026-11-27 -->
# Exchange API Changelog Diff

Generated: 2026-11-27 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (146725 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 58 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3488 bytes)

- [OK] Bybit V5 (`bybit`): no change (101511 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (45900 bytes)

- [CHANGED] **Gate.io Spot WebSocket v4** (`gate-spot-ws`): 1198 diff lines

- [CHANGED] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): 1565 diff lines



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 10f05d2..48f09ac 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -23,11 +23,18 @@ REST API 不受影响。
 | 64010 | WebSocket 8443 端口即将下线，请迁移至 443 端口。
 SBE 交易及私有数据
-最近更新：2026 年 11 月 13 日
-欧易已于 2026 年 11 月 13 日在模拟交易环境上线简单二进制编码（Simple Binary Encoding，SBE）交易服务，以及私有订单与成交数据服务。相关服务预计于 2026 年 12 月上旬上线生产环境。
+最近更新：2026 年 11 月 26 日
+欧易已于 2026 年 11 月 13 日在模拟交易环境上线简单二进制编码（Simple Binary Encoding，SBE）交易服务，以及私有订单与成交数据服务。下方新版 XML 模板将于 2026 年 12 月 3 日上线模拟交易环境，相关服务将于 2026 年 12 月 16 日上线生产环境。
 现有 REST API 和 JSON WebSocket API 不受影响。
 新增 SBE 服务
-| 服务 | 生产环境地址 | 模拟交易环境地址 | XML 模板
-| 交易 | wss://ws.okx.com/ws/v5/trade-sbe | wss://wspap.okx.com/ws/v5/trade-sbe | okx_sbe_trade_2_0.xml
-| 私有数据 | wss://ws.okx.com/ws/v5/private-sbe | wss://wspap.okx.com/ws/v5/private-sbe | okx_sbe_private_1_1.xml
+新版 XML 模板：2026 年 12 月 3 日模拟交易环境生效，2026 年 12 月 16 日生产环境生效。
+| 服务 | WebSocket 地址 | 新版 XML 模板
+| 交易 | 生产环境: wss://ws.okx.com/ws/v5/trade-sbe
+模拟交易环境: wss://wspap.okx.com/ws/v5/trade-sbe | okx_sbe_trade_order_entry_standard_3_0.xml
+| 私有数据 | 生产环境: wss://ws.okx.com/ws/v5/private-sbe
+模拟交易环境: wss://wspap.okx.com/ws/v5/private-sbe | okx_sbe_trade_private_orders_2_0.xml
+okx_sbe_trade_private_fills_1_1.xml
+当前模拟交易环境使用的 XML 模板（2026 年 12 月 3 日更新前）
+- 交易: okx_sbe_trade_2_0.xml
+- 私有数据（orders 和 fills）: okx_sbe_private_1_1.xml
 /ws/v5/trade-sbe 和 /ws/v5/private-sbe 两个 WebSocket 服务共享连接频率限制：每个 IP 每 5 分钟最多发起 500 次连接请求。
 登录方式与现有的 SBE 行情数据服务一致。客户端需在 WebSocket HTTP Upgrade 请求头中提供 API key 和签名以完成鉴权。
@@ -35,16 +42,17 @@ JSON 控制消息使用 opcode 为 1 的文本帧，SBE 消息使用 opcode 为
 相比 JSON 服务，SBE 消息的字段有所精简。完整的消息结构及字段定义请参考 XML 模板。
 XML 模板更新
-XML 模板已在服务上线前更新。请使用上方最新版本的模板生成编码器和解码器。
-交易：okx_sbe_trade_2_0.xml
-- Schema id 从 1 调整为 2，version 仍为 0，semanticVersion 调整为 2.0.0。消息结构发生变化，请使用此模板重新生成编码器和解码器。
-- 单笔及批量下单请求新增可选字段 rpiPxRound（RPI 价格取整）和 reduceOnly（只减仓）；单笔及批量改单请求新增可选字段 rpiPxRound。
-- 单笔及批量下单、改单请求中的 expTime 更名为 expTimeUs；所有下单、改单、撤单响应中的 ts 更名为 tsUs。这些字段的时间单位仍为微秒。
-- 单笔及批量下单响应移除 instIdCode，后续定长字段前移，字段 ID 随之调整。
-- 单笔下单、改单、撤单响应新增变长 UTF-8 错误信息 msg。
-- 批量下单、改单、撤单响应中的 data 分组更名为 results，结果按请求顺序排列，最多 20 条；新增 sMsgDetails 分组，通过从 0 开始的 resultIndex 将逐笔错误信息 sMsg 关联至 results，并新增批次级错误信息 msg。msg 和 sMsg 均使用 varString16，即以 uint16 为长度前缀的变长 UTF-8 字符串。
-私有数据：okx_sbe_private_1_1.xml
-- Schema id 仍为 1，version 从 0 调整为 1，semanticVersion 调整为 1.1.0。
-- orders 消息新增可选字段 reduceOnly（只减仓标识，booleanEnum：FALSE=0、TRUE=1）和 avgPxMantissa（成交均价尾数，共用 pxExponent）。两个字段均标记为 sinceVersion="1"。
-- orders 中的 fillTime、uTime、cTime 分别更名为 fillTimeUs、uTimeUs、cTimeUs；fills 中的 ts 更名为 tsUs。时间单位仍为微秒，更名字段的 ID 和类型保持不变。
+以下更新将于 2026 年 12 月 3 日上线模拟交易环境，并于 2026 年 12 月 16 日上线生产环境。模拟交易环境将于 12 月 3 日直接切换至新版协议，替换旧版协议。请按环境及生效日期选择 XML 模板，提前完成新版编码器和解码器适配，并在对应环境更新生效时切换至新版。
+交易：okx_sbe_trade_order_entry_standard_3_0.xml
+- Schema id 从 2 调整为 3，version 仍为 0，semanticVersion 调整为 3.0.0。
+- 价格和数量沿用现有的尾数/指数编码格式。
+- 批量下单、改单、撤单响应中的 inTime 和 outTime 从逐笔结果 results 分组移至响应根块，每个响应仅编码一次。时间单位仍为微秒。
+- 单笔及批量下单请求和响应中的 tag 从 int64 调整为 char16，即以 NUL 字节补齐的定长 16 字节 ASCII 字符数组。未设置或为空时编码为 16 个 NUL 字节（0x00）。
+订单频道：okx_sbe_trade_private_orders_2_0.xml
+- orders 频道使用独立的 XML 模板，Schema id="2"、version="0"、semanticVersion="2.0.0"。
+- 新增五个指数字段：fillPxExponent、fillSzExponent、fillFeeExponent、accFillSzExponent 和 avgPxExponent。每个尾数均有独立的指数，请使用对应的尾数/指数对解码各字段。
+- 委托和成交的价格、数量保持精确。avgPx、fillFee 和 fee 截取至最多 18 位有效数字。预计不会对交易产生实质影响，但对账时可能出现截取导致的轻微差异。
+- tag 从 int64 调整为与交易服务相同的定长 16 字节 char16 格式。
+成交频道：okx_sbe_trade_private_fills_1_1.xml
+- fills 频道通过独立 XML 文件提供，消息结构和编码保持不变；Schema 仍为 id="1"、version="1"、semanticVersion="1.1.0"。
 SBE 交易
 SBE 交易服务将支持以下操作：

```

### Gate.io Spot WebSocket v4 (`gate-spot-ws`)
- Source: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/

```diff
diff --git a/changelogs/gate-spot-ws.txt b/changelogs/gate-spot-ws.txt
index 363b616..b2e4693 100644
--- a/changelogs/gate-spot-ws.txt
+++ b/changelogs/gate-spot-ws.txt
@@ -1,7 +1,15 @@
+- Python
+- Golang
+- python µs
+- golang µs
 # Spot WebSocket v4.0.0
 WebSocket 应用示例
 # !/usr/bin/env python # coding: utf-8 import hashlib import hmac import json import logging import time import threading # pip install -U websocket_client from websocket import WebSocketApp logging.basicConfig(level=logging.INFO) logger = logging.getLogger(__name__) event = threading.Event() class GateWebSocketApp(WebSocketApp): def __init__(self, url, api_key, api_secret, **kwargs): super(GateWebSocketApp, self).__init__(url, **kwargs) self._api_key = api_key self._api_secret = api_secret def _send_ping(self): while not event.wait(10): self.last_ping_tm = time.time() if self.sock: try: self.sock.ping() except Exception as ex: logger.warning("send_ping routine terminated: {}".format(ex)) break try: self._request("spot.ping", auth_required=False) except Exception as e: raise e def _request(self, channel, event=None, payload=None, auth_required=True): current_time = int(time.time()) data = { "time": current_time, "channel": channel, "event": event, "payload": payload, } if auth_required: message = 'channel=%s&event=%s&time=%d' % (channel, event, current_time) data['auth'] = { "method": "api_key", "KEY": self._api_key, "SIGN": self.get_sign(message), } data = json.dumps(data) logger.info('request: %s', data) self.send(data) def get_sign(self, message): h = hmac.new(self._api_secret.encode("utf8"), message.encode("utf8"), hashlib.sha512) return h.hexdigest() def subscribe(self, channel, payload=None, auth_required=True): self._request(channel, "subscribe", payload, auth_required) def unsubscribe(self, channel, payload=None, auth_required=True): self._request(channel, "unsubscribe", payload, auth_required) def on_message(ws, message): # type: (GateWebSocketApp, str) -> None # handle whatever message you received logger.info("message received from server: {}".format(message)) def on_open(ws): # type: (GateWebSocketApp) -> None # subscribe to channels interested logger.info('websocket connected') ws.subscribe("spot.trades", ['BTC_USDT'], False) if __name__ == "__main__": logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG) app = GateWebSocketApp("wss://api.gateio.ws/ws/v4/", "YOUR_API_KEY", "YOUR_API_SECRET", on_open=on_open, on_message=on_message) app.run_forever(ping_interval=5)
 WebSocket 应用示例
+# !/usr/bin/env python # coding: utf-8 import hashlib import hmac import json import logging import time import threading # pip install -U websocket_client from websocket import WebSocketApp logging.basicConfig(level=logging.INFO) logger = logging.getLogger(__name__) event = threading.Event() class GateWebSocketApp(WebSocketApp): def __init__(self, url, api_key, api_secret, **kwargs): super(GateWebSocketApp, self).__init__(url, **kwargs) self._api_key = api_key self._api_secret = api_secret def _send_ping(self): while not event.wait(10): self.last_ping_tm = time.time() if self.sock: try: self.sock.ping() except Exception as ex: logger.warning("send_ping routine terminated: {}".format(ex)) break try: self._request("spot.ping", auth_required=False) except Exception as e: raise e def _request(self, channel, event=None, payload=None, auth_required=True): current_time = int(time.time()) data = { "time": current_time, "channel": channel, "event": event, "payload": payload, } if auth_required: message = 'channel=%s&event=%s&time=%d' % (channel, event, current_time) data['auth'] = { "method": "api_key", "KEY": self._api_key, "SIGN": self.get_sign(message), } data = json.dumps(data) logger.info('request: %s', data) self.send(data) def get_sign(self, message): h = hmac.new(self._api_secret.encode("utf8"), message.encode("utf8"), hashlib.sha512) return h.hexdigest() def subscribe(self, channel, payload=None, auth_required=True): self._request(channel, "subscribe", payload, auth_required) def unsubscribe(self, channel, payload=None, auth_required=True): self._request(channel, "unsubscribe", payload, auth_required) def on_message(ws, message): # type: (GateWebSocketApp, str) -> None # handle whatever message you received logger.info("message received from server: {}".format(message)) def on_open(ws): # type: (GateWebSocketApp) -> None # subscribe to channels interested logger.info('websocket connected') ws.subscribe("spot.trades", ['BTC_USDT'], False) if __name__ == "__main__": logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG) app = GateWebSocketApp("wss://api.gateio.ws/ws/v4/", "YOUR_API_KEY", "YOUR_API_SECRET", on_open=on_open, on_message=on_message, header={"timeUnit": "microsecond"}) app.run_forever(ping_interval=5)
+WebSocket 应用示例
 package main import ( "crypto/hmac" "crypto/sha512" "crypto/tls" "encoding/hex" "encoding/json" "fmt" "io" "net/url" "time" "github.com/gorilla/websocket" ) type Msg struct { Time int64 `json:"time"` Channel string `json:"channel"` Event string `json:"event"` Payload []string `json:"payload"` Auth *Auth `json:"auth"` } type Auth struct { Method string `json:"method"` KEY string `json:"KEY"` SIGN string `json:"SIGN"` } const ( Key = "YOUR_API_KEY" Secret = "YOUR_API_SECRETY" ) func sign(channel, event string, t int64) string { message := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, t) h2 := hmac.New(sha512.New, []byte(Secret)) io.WriteString(h2, message) return hex.EncodeToString(h2.Sum(nil)) } func (msg *Msg) sign() { signStr := sign(msg.Channel, msg.Event, msg.Time) msg.Auth = &Auth{ Method: "api_key", KEY: Key, SIGN: signStr, } } func (msg *Msg) send(c *websocket.Conn) error { msgByte, err := json.Marshal(msg) if err != nil { return err } return c.WriteMessage(websocket.TextMessage, msgByte) } func NewMsg(channel, event string, t int64, payload []string) *Msg { return &Msg{ Time: t, Channel: channel, Event: event, Payload: payload, } } func main() { u := url.URL{Scheme: "wss", Host: "api.gateio.ws", Path: "/ws/v4/"} websocket.DefaultDialer.TLSClientConfig = &tls.Config{RootCAs: nil, InsecureSkipVerify: true} c, _, err := websocket.DefaultDialer.Dial(u.String(), nil) if err != nil { panic(err) } c.SetPingHandler(nil) // read msg go func() { for { _, message, err := c.ReadMessage() if err != nil { c.Close() panic(err) } fmt.Printf("recv: %s\n", message) } }() t := time.Now().Unix() pingMsg := NewMsg("spot.ping", "", t, []string{}) err = pingMsg.send(c) if err != nil { panic(err) } // subscribe order book orderBookMsg := NewMsg("spot.order_book", "subscribe", t, []string{"BTC_USDT", "5", "100ms"}) err = orderBookMsg.send(c) if err != nil { panic(err) } // subscribe positions ordersMsg := NewMsg("spot.orders", "subscribe", t, []string{"BTC_USDT"}) ordersMsg.sign() err = ordersMsg.send(c) if err != nil { panic(err) } select {} }
+WebSocket 应用示例
+package main import ( "crypto/hmac" "crypto/sha512" "crypto/tls" "encoding/hex" "encoding/json" "fmt" "io" "net/url" "time" "github.com/gorilla/websocket" "net/http" ) type Msg struct { Time int64 `json:"time"` Channel string `json:"channel"` Event string `json:"event"` Payload []string `json:"payload"` Auth *Auth `json:"auth"` } type Auth struct { Method string `json:"method"` KEY string `json:"KEY"` SIGN string `json:"SIGN"` } const ( Key = "YOUR_API_KEY" Secret = "YOUR_API_SECRETY" ) func sign(channel, event string, t int64) string { message := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, t) h2 := hmac.New(sha512.New, []byte(Secret)) io.WriteString(h2, message) return hex.EncodeToString(h2.Sum(nil)) } func (msg *Msg) sign() { signStr := sign(msg.Channel, msg.Event, msg.Time) msg.Auth = &Auth{ Method: "api_key", KEY: Key, SIGN: signStr, } } func (msg *Msg) send(c *websocket.Conn) error { msgByte, err := json.Marshal(msg) if err != nil { return err } return c.WriteMessage(websocket.TextMessage, msgByte) } func NewMsg(channel, event string, t int64, payload []string) *Msg { return &Msg{ Time: t, Channel: channel, Event: event, Payload: payload, } } func main() { u := url.URL{Scheme: "wss", Host: "api.gateio.ws", Path: "/ws/v4/"} websocket.DefaultDialer.TLSClientConfig = &tls.Config{RootCAs: nil, InsecureSkipVerify: true} c, _, err := websocket.DefaultDialer.Dial(u.String(), http.Header{"timeUnit": []string{"microsecond"}}) if err != nil { panic(err) } c.SetPingHandler(nil) // read msg go func() { for { _, message, err := c.ReadMessage() if err != nil { c.Close() panic(err) } fmt.Printf("recv: %s\n", message) } }() t := time.Now().Unix() pingMsg := NewMsg("spot.ping", "", t, []string{}) err = pingMsg.send(c) if err != nil { panic(err) } // subscribe order book orderBookMsg := NewMsg("spot.order_book", "subscribe", t, []string{"BTC_USDT", "5", "100ms"}) err = orderBookMsg.send(c) if err != nil { panic(err) } // subscribe positions ordersMsg := NewMsg("spot.orders", "subscribe", t, []string{"BTC_USDT"}) ordersMsg.sign() err = ordersMsg.send(c) if err != nil { panic(err) } select {} }
 Gate 提供了一个简单而健壮的 Websocket API 来集成现货交易状态信息为您的业务或应用提供支持。
 我们当前使用 Python 和 Golang 作为代码示例，将来会有更多语言示例支持！
@@ -19,4 +27,9 @@ TIP
 SDK 的源代码 在 gatews (opens new window) GitHub 仓库。
 # 变更历史
+2026-11-26
+- OMS 3.0 用户可在 spot.order_place 单笔、spot.order_cancel、spot.order_amend、spot.order_cancel_cp 的 payload.req_header 传入 X-Gate-Client-Send-Us 和 X-Gate-Timeout-Window-Us。详见 3.0 用户请求超时。
+- 请求 Header timeUnit: microsecond 可追加微秒字段，URL Query timeUnit=microsecond 同样生效。公有通道对所有连接生效，私有通道仅 OMS 3.0 生效。详见 微秒时间戳。
+2026-11-20
+- 向 API 用户开放 RPI（Retail Price Improvement）流动性接入功能。普通单笔下单可传 rpi_taker_access。详见 RPI 流动性接入（Speed Bump）。
 2026-10-14
 - 新增公开频道 spot.rpi_order_book，spot.rpi_obu 推送 RPI 深度全量快照
@@ -113,4 +126,5 @@ WebSocket 操作分为不同的频道。频道可以是公共的或私有的。
 | time | Integer | 精确到秒的响应时间
 | time_ms | Integer | 精确到毫秒的响应时间
+| time_us | Integer | 同 time 字段，微秒精度
 | id | Integer | 从客户端请求 payload 中提取的请求 ID （如果请求参数中有的话）
 | channel | String | WebSocket 频道名称
@@ -120,4 +134,28 @@ WebSocket 操作分为不同的频道。频道可以是公共的或私有的。
 注意：如果它是服务端发起的数据更新通知 那么 result 的类型是基于 channel 的，不同 channel 的 result 类型有所不同。
 但如果是对客户端订阅请求的响应，那么 result 为固定的 {"status": "success"}。 验证订阅请求是否成功，您只需要检查 error 字段是否为空即可，不需要再解析 result 字段。
+# 微秒时间戳
+握手时用下面任一方式开启，连接建立后不能修改：
+- Header：timeUnit: microsecond
+- URL Query：timeUnit=microsecond
+值必须是全小写 microsecond。Microsecond、空字符串、带空格都等于未开启。Header 的键名不区分大小写，Query 的键名区分大小写，必须是 timeUnit。两者任一命中即开启。不带该参数的连接与升级前一致。
+原有的秒、毫秒字段保留，只追加微秒字段。新增字段是整数。SBE 不追加这些字段。现货没有 PB 推送。
+订阅确认、错误和 spot.pong 只在外层追加 time_us，result 里不补业务微秒。time_us 是服务端发出该条消息时的 Unix 微秒。仅 timeUnit: microsecond 开启后推送。
+URL 示例：wss://api.gateio.ws/ws/v4/?timeUnit=microsecond
+# 公有通道
+已开启的连接都会追加，不区分是不是 OMS 3.0 用户。
+| 通道 | 保留 | 新增
+| spot.trades、spot.trades_v2 | create_time、create_time_ms | create_time_us。create_time_ms 带小数时按小数换算，原字符串不变
+| spot.order_book、spot.rpi_order_book、spot.order_book_update、spot.obu、spot.rpi_obu、spot.book_ticker、spot.tickers | t（毫秒） | t_us
+| spot.candlesticks | t（秒，字符串） | t_us。t 仍是字符串
+各通道的微秒示例写在对应频道的推送说明中。
+# OMS 3.0 的私有通道
+已开启，并且该条消息处理时判定为 OMS 3.0，才追加。非 3.0 用户的私有推送与未开启时一致，没有外层 time_us，也没有业务微秒字段。
+| 通道 | 保留 | 新增
+| spot.orders、spot.orders_v2 | create_time、create_time_ms、update_time、update_time_ms | create_time_us、update_time_us
+| spot.usertrades、spot.usertrades_v2 | create_time、create_time_ms | create_time_us
+| spot.balances、spot.margin_balances、spot.funding_balances、spot.cross_balances | timestamp（秒，字符串）、timestamp_ms | timestamp_us。timestamp 原字符串不变
+| spot.cross_loan | timestamp（毫秒） | timestamp_us。不补 timestamp_ms
+各通道的微秒示例写在对应频道的推送说明中。
+已开启且为 OMS 3.0 时，下单、撤单、改单、查单的响应也会追加对应微秒字段。header 追加 time_us、response_time_us。订单对象追加 create_time_us、update_time_us。spot.login 不追加。示例写在各接口的响应说明中。
 为了简单起见，下面的频道（channel）描述只给出对应频道的 payload 格式。
 # Error
@@ -138,4 +176,8 @@ WARNING
 # example WebSocket signature calculation implementation in Python import hmac, hashlib, json, time def gen_sign(channel, event, timestamp): # GateAPIv4 key pair api_key = 'YOUR_API_KEY' api_secret = 'YOUR_API_SECRET' s = 'channel=%s&event=%s&time=%d' % (channel, event, timestamp) sign = hmac.new(api_secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest() return {'method': 'api_key', 'KEY': api_key, 'SIGN': sign} request = { 'id': int(time.time() * 1e6), 'time': int(time.time()), 'channel': 'spot.orders', 'event': 'subscribe', 'payload': ["BTC_USDT", "GT_USDT"] } request['auth'] = gen_sign(request['channel'], request['event'], request['time']) print(json.dumps(request))
 代码示例
+# example WebSocket signature calculation implementation in Python import hmac, hashlib, json, time def gen_sign(channel, event, timestamp): # GateAPIv4 key pair api_key = 'YOUR_API_KEY' api_secret = 'YOUR_API_SECRET' s = 'channel=%s&event=%s&time=%d' % (channel, event, timestamp) sign = hmac.new(api_secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest() return {'method': 'api_key', 'KEY': api_key, 'SIGN': sign} request = { 'id': int(time.time() * 1e6), 'time': int(time.time()), 'channel': 'spot.orders', 'event': 'subscribe', 'payload': ["BTC_USDT", "GT_USDT"] } request['auth'] = gen_sign(request['channel'], request['event'], request['time']) print(json.dumps(request))
+代码示例
+package main import ( "crypto/hmac" "crypto/sha512" "encoding/hex" "encoding/json" "fmt" "time" ) func genSign(channel, event string, timestamp int64) map[string]string { apiKey := "YOUR_API_KEY" apiSecret := "YOUR_API_SECRET" s := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, timestamp) h := hmac.New(sha512.New, []byte(apiSecret)) h.Write([]byte(s)) sign := hex.EncodeToString(h.Sum(nil)) return map[string]string{ "method": "api_key", "KEY": apiKey, "SIGN": sign, } } func main() { timestamp := time.Now().Unix() request := map[string]interface{}{ "id": time.Now().UnixNano() / 1e3, "time": timestamp, "channel": "spot.orders", "event": "subscribe", "payload": []string{"BTC_USDT", "GT_USDT"}, } request["auth"] = genSign(request["channel"].(string), request["event"].(string), timestamp) jsonBytes, _ := json.Marshal(request) fmt.Println(string(jsonBytes)) }
+代码示例
 package main import ( "crypto/hmac" "crypto/sha512" "encoding/hex" "encoding/json" "fmt" "time" ) func genSign(channel, event string, timestamp int64) map[string]string { apiKey := "YOUR_API_KEY" apiSecret := "YOUR_API_SECRET" s := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, timestamp) h := hmac.New(sha512.New, []byte(apiSecret)) h.Write([]byte(s)) sign := hex.EncodeToString(h.Sum(nil)) return map[string]string{ "method": "api_key", "KEY": apiKey, "SIGN": sign, } } func main() { timestamp := time.Now().Unix() request := map[string]interface{}{ "id": time.Now().UnixNano() / 1e3, "time": timestamp, "channel": "spot.orders", "event": "subscribe", "payload": []string{"BTC_USDT", "GT_USDT"}, } request["auth"] = genSign(request["channel"].(string), request["event"].(string), timestamp) jsonBytes, _ := json.Marshal(request) fmt.Println(string(jsonBytes)) }
 如果频道是私有的，例如 spot.orders 频道用于获取用户订单更新，那么客户端请求需要携带身份验证信息。
@@ -221,7 +263,19 @@ spot.ping
 import time # pip install websocket_client from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/") ws.send('{"time": %d, "channel" : "spot.ping"}' % int(time.time())) print(ws.recv())
 代码示例
+import time # pip install websocket_client from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/", header={"timeUnit": "microsecond"}) ws.send('{"time": %d, "channel" : "spot.ping"}' % int(time.time())) print(ws.recv())
+代码示例
 package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" ) func main() { url := "wss://api.gateio.ws/ws/v4/" conn, _, err := websocket.DefaultDialer.Dial(url, nil) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() ping := map[string]interface{}{ "time": time.Now().Unix(), "channel": "spot.ping", } msg, err := json.Marshal(ping) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+代码示例
+package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" "net/http" ) func main() { url := "wss://api.gateio.ws/ws/v4/" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"timeUnit": []string{"microsecond"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() ping := map[string]interface{}{ "time": time.Now().Unix(), "channel": "spot.ping", } msg, err := json.Marshal(ping) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 响应示例
 { "time": 1545404023, "channel": "spot.pong", "event": "", "error": null, "result": null }
+请求 Header timeUnit: microsecond 开启后，pong 只追加外层 time_us。
+spot.pong
+from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/", header={"timeUnit": "microsecond"})
+{ "time": 1545404023, "time_us": 1545404023123456, "channel": "spot.pong", "event": "", "error": null, "result": null }
+请求 Header timeUnit: microsecond 开启后，pong 只追加外层 time_us。
+spot.pong
+conn, _, err := websocket.DefaultDialer.Dial( "wss://api.gateio.ws/ws/v4/", http.Header{"timeUnit": []string{"microsecond"}}, )
+{ "time": 1545404023, "time_us": 1545404023123456, "channel": "spot.pong", "event": "", "error": null, "result": null }
 检查与服务器的连接是否仍然存活。
 这是一种额外的连接可达性检查。服务器使用协议层的 ping/pong (opens new window) 消息来检查客户端是否仍然连接。它不强制要求使用这种方法。如果您使用一些知名的 WebSocket 客户端库，通常不需要关心这个 API。
@@ -249,5 +303,9 @@ Ticker 是对现货交易状态的高级概览。它显示了最高、最低和
 import time import json # pip install websocket_client from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/") ws.send(json.dumps({ "time": int(time.time()), "channel": "spot.tickers", "event": "subscribe", # "unsubscribe" for unsubscription "payload": ["BTC_USDT"] })) print(ws.recv())
 代码示例：
+import time import json # pip install websocket_client from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/", header={"timeUnit": "microsecond"}) ws.send(json.dumps({ "time": int(time.time()), "channel": "spot.tickers", "event": "subscribe", # "unsubscribe" for unsubscription "payload": ["BTC_USDT"] })) print(ws.recv())
+代码示例：
 package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" ) func main() { url := "wss://api.gateio.ws/ws/v4/" conn, _, err := websocket.DefaultDialer.Dial(url, nil) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() subscribe := map[string]interface{}{ "time": time.Now().Unix(), "channel": "spot.tickers", "event": "subscribe", "payload": []string{"BTC_USDT"}, } msg, err := json.Marshal(subscribe) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+代码示例：
+package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" "net/http" ) func main() { url := "wss://api.gateio.ws/ws/v4/" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"timeUnit": []string{"microsecond"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() subscribe := map[string]interface{}{ "time": time.Now().Unix(), "channel": "spot.tickers", "event": "subscribe", "payload": []string{"BTC_USDT"}, } msg, err := json.Marshal(subscribe) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 订阅参数格式:
 | 字段 | 类型 | 必选 | 描述
@@ -258,5 +316,13 @@ TIP
 # 服务端推送
 通知示例：
-{ "time": 1606291803, "channel": "spot.tickers", "event": "update", "result": { "currency_pair": "BTC_USDT", "last": "19106.55", "lowest_ask": "19108.71", "highest_bid": "19106.55", "change_percentage": "3.66", "base_volume": "2811.3042155865", "quote_volume": "53441606.52411221454674732293", "high_24h": "19417.74", "low_24h": "18434.21" } }
+{ "time": 1606291803, "time_ms": 1606291803123, "channel": "spot.tickers", "event": "update", "result": { "currency_pair": "BTC_USDT", "last": "19106.55", "lowest_ask": "19108.71", "highest_bid": "19106.55", "change_percentage": "3.66", "base_volume": "2811.3042155865", "quote_volume": "53441606.52411221454674732293", "high_24h": "19417.74", "low_24h": "18434.21" } }
+请求 Header timeUnit: microsecond 开启后，在原有字段之外追加微秒字段。
+spot.tickers
+from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/", header={"timeUnit": "microsecond"})
+{ "time": 1606291803, "time_ms": 1606291803123, "time_us": 1606291803123456, "channel": "spot.tickers", "event": "update", "result": { "currency_pair": "BTC_USDT", "last": "19106.55", "lowest_ask": "19108.71", "highest_bid": "19106.55", "change_percentage": "3.66", "base_volume": "2811.3042155865", "quote_volume": "53441606.52411221454674732293", "high_24h": "19417.74", "low_24h": "18434.21" } }
+请求 Header timeUnit: microsecond 开启后，在原有字段之外追加微秒字段。
+spot.tickers
+conn, _, err := websocket.DefaultDialer.Dial( "wss://api.gateio.ws/ws/v4/", http.Header{"timeUnit": []string{"microsecond"}}, )
+{ "time": 1606291803, "time_ms": 1606291803123, "time_us": 1606291803123456, "channel": "spot.tickers", "event": "update", "result": { "currency_pair": "BTC_USDT", "last": "19106.55", "lowest_ask": "19108.71", "highest_bid": "19106.55", "change_percentage": "3.66", "base_volume": "2811.3042155865", "quote_volume": "53441606.52411221454674732293", "high_24h": "19417.74", "low_24h": "18434.21" } }
 通知结果格式：
 | 字段 | 类型 | 描述
@@ -281,5 +347,9 @@ spot.trades
 import time import json # pip install websocket_client from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/") ws.send(json.dumps({ "time": int(time.time()), "channel": "spot.trades", "event": "subscribe", # "unsubscribe" for unsubscription "payload": ["BTC_USDT"] })) print(ws.recv())
 代码示例：
+import time import json # pip install websocket_client from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/", header={"timeUnit": "microsecond"}) ws.send(json.dumps({ "time": int(time.time()), "channel": "spot.trades", "event": "subscribe", # "unsubscribe" for unsubscription "payload": ["BTC_USDT"] })) print(ws.recv())
+代码示例：
 package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" ) func main() { url := "wss://api.gateio.ws/ws/v4/" conn, _, err := websocket.DefaultDialer.Dial(url, nil) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() subscribe := map[string]interface{}{ "time": time.Now().Unix(), "channel": "spot.trades", "event": "subscribe", "payload": []string{"BTC_USDT"}, } msg, err := json.Marshal(subscribe) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+代码示例：
+package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" "net/http" ) func main() { url := "wss://api.gateio.ws/ws/v4/" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"timeUnit": []string{"microsecond"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() subscribe := map[string]interface{}{ "time": time.Now().Unix(), "channel": "spot.trades", "event": "subscribe", "payload": []string{"BTC_USDT"}, } msg, err := json.Marshal(subscribe) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 订阅参数格式:
 | 字段 | 类型 | 必选 | 描述
@@ -290,5 +360,13 @@ TIP
 # 服务端推送
 通知示例：
-{ "time": 1606292218, "channel": "spot.trades", "event": "update", "result": { "id": 309143071, "create_time": 1606292218, "create_time_ms": "1606292218213.4578", "side": "sell", "currency_pair": "BTC_USD", "amount": "16.4700000000", "price": "0.4705000000", "range": "2390902-2390902", "id_market": 917144, "stock": "BTC", "money": "USDC", "trade_mode": 1 } }
+{ "time": 1606292218, "time_ms": 1606292218123, "channel": "spot.trades", "event": "update", "result": { "id": 309143071, "create_time": 1606292218, "create_time_ms": "1606292218213.4578", "side": "sell", "currency_pair": "BTC_USD", "amount": "16.4700000000", "price": "0.4705000000", "range": "2390902-2390902", "id_market": 917144, "stock": "BTC", "money": "USDC", "trade_mode": 1 } }
+请求 Header timeUnit: microsecond 开启后，在原有字段之外追加微秒字段。
+spot.trades
+from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/", header={"timeUnit": "microsecond"})
+{ "time": 1606292218, "time_ms": 1606292218123, "time_us": 1606292218123456, "channel": "spot.trades", "event": "update", "result": { "id": 309143071, "create_time": 1606292218, "create_time_ms": "1606292218213.4578", "create_time_us": 1606292218213457, "side": "sell", "currency_pair": "BTC_USD", "amount": "16.4700000000", "price": "0.4705000000", "range": "2390902-2390902", "id_market": 917144, "stock": "BTC", "money": "USDC", "trade_mode": 1 } }
+请求 Header timeUnit: microsecond 开启后，在原有字段之外追加微秒字段。
+spot.trades
+conn, _, err := websocket.DefaultDialer.Dial( "wss://api.gateio.ws/ws/v4/", http.Header{"timeUnit": []string{"microsecond"}}, )
+{ "time": 1606292218, "time_ms": 1606292218123, "time_us": 1606292218123456, "channel": "spot.trades", "event": "update", "result": { "id": 309143071, "create_time": 1606292218, "create_time_ms": "1606292218213.4578", "create_time_us": 1606292218213457, "side": "sell", "currency_pair": "BTC_USD", "amount": "16.4700000000", "price": "0.4705000000", "range": "2390902-2390902", "id_market": 917144, "stock": "BTC", "money": "USDC", "trade_mode": 1 } }
 请注意，公共交易频道只通知交易中的吃单方。下面的私有用户交易频道将通知所有与用户相关的交易。
 通知结果格式：
@@ -298,4 +376,5 @@ TIP
 | » create_time | Integer | 成交时间，精确到秒
 | » create_time_ms | String | 成交时间，毫秒精度
+| » create_time_us | Integer | 同 create_time 字段，微秒精度
 | » side | String | 买单或者卖单
 | » currency_pair | String | 交易货币对
@@ -321,5 +400,9 @@ spot.trades_v2
 import time import json # pip install websocket_client from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/") ws.send(json.dumps({ "time": int(time.time()), "channel": "spot.trades_v2", "event": "subscribe", # "unsubscribe" for unsubscription "payload": ["BTC_USDT"] })) print(ws.recv())
 代码示例：
+import time import json # pip install websocket_client from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/", header={"timeUnit": "microsecond"}) ws.send(json.dumps({ "time": int(time.time()), "channel": "spot.trades_v2", "event": "subscribe", # "unsubscribe" for unsubscription "payload": ["BTC_USDT"] })) print(ws.recv())
+代码示例：
 package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" ) func main() { url := "wss://api.gateio.ws/ws/v4/" conn, _, err := websocket.DefaultDialer.Dial(url, nil) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() subscribe := map[string]interface{}{ "time": time.Now().Unix(), "channel": "spot.trades_v2", "event": "subscribe", "payload": []string{"BTC_USDT"}, } msg, err := json.Marshal(subscribe) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+代码示例：
+package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" "net/http" ) func main() { url := "wss://api.gateio.ws/ws/v4/" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"timeUnit": []string{"microsecond"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() subscribe := map[string]interface{}{ "time": time.Now().Unix(), "channel": "spot.trades_v2", "event": "subscribe", "payload": []string{"BTC_USDT"}, } msg, err := json.Marshal(subscribe) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 订阅参数格式:
 | 字段 | 类型 | 必选 | 描述
@@ -330,5 +413,13 @@ TIP
 # 服务端推送
 通知示例：
-{ "time": 1606292218, "channel": "spot.trades_v2", "event": "update", "result": { "id": 309143071, "create_time": 1606292218, "create_time_ms": "1606292218213.4578", "side": "sell", "currency_pair": "BTC_USD", "amount": "16.4700000000", "price": "0.4705000000", "range": "2390902-2390902", "id_market": 917144, "stock": "BTC", "money": "USDC", "trade_mode": 1 } }
+{ "time": 1606292218, "time_ms": 1606292218123, "channel": "spot.trades_v2", "event": "update", "result": { "id": 309143071, "create_time": 1606292218, "create_time_ms": "1606292218213.4578", "side": "sell", "currency_pair": "BTC_USD", "amount": "16.4700000000", "price": "0.4705000000", "range": "2390902-2390902", "id_market": 917144, "stock": "BTC", "money": "USDC", "trade_mode": 1 } }
+请求 Header timeUnit: microsecond 开启后，在原有字段之外追加微秒字段。
+spot.trades_v2
+from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/", header={"timeUnit": "microsecond"})
+{ "time": 1606292218, "time_ms": 1606292218123, "time_us": 1606292218123456, "channel": "spot.trades_v2", "event": "update", "result": { "id": 309143071, "create_time": 1606292218, "create_time_ms": "1606292218213.4578", "create_time_us": 1606292218213457, "side": "sell", "currency_pair": "BTC_USD", "amount": "16.4700000000", "price": "0.4705000000", "range": "2390902-2390902", "id_market": 917144, "stock": "BTC", "money": "USDC", "trade_mode": 1 } }
+请求 Header timeUnit: microsecond 开启后，在原有字段之外追加微秒字段。
+spot.trades_v2
+conn, _, err := websocket.DefaultDialer.Dial( "wss://api.gateio.ws/ws/v4/", http.Header{"timeUnit": []string{"microsecond"}}, )
+{ "time": 1606292218, "time_ms": 1606292218123, "time_us": 1606292218123456, "channel": "spot.trades_v2", "event": "update", "result": { "id": 309143071, "create_time": 1606292218, "create_time_ms": "1606292218213.4578", "create_time_us": 1606292218213457, "side": "sell", "currency_pair": "BTC_USD", "amount": "16.4700000000", "price": "0.4705000000", "range": "2390902-2390902", "id_market": 917144, "stock": "BTC", "money": "USDC", "trade_mode": 1 } }
 请注意，公共交易频道只通知交易中的吃单方。下面的私有用户交易频道将通知所有与用户相关的交易。
 通知结果格式：
@@ -338,4 +429,5 @@ TIP
 | » create_time | Integer | 成交时间，精确到秒
 | » create_time_ms | String | 成交时间，毫秒精度
+| » create_time_us | Integer | 同 create_time 字段，微秒精度
 | » side | String | 买单或者卖单
 | » currency_pair | String | 交易货币对
@@ -360,5 +452,9 @@ spot.candlesticks
 import time import json # pip install websocket_client from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/") ws.send(json.dumps({ "time": int(time.time()), "channel": "spot.candlesticks", "event": "subscribe", # "unsubscribe" for unsubscription "payload": ["1m", "BTC_USDT"] })) print(ws.recv())
 代码示例：
+import time import json # pip install websocket_client from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/", header={"timeUnit": "microsecond"}) ws.send(json.dumps({ "time": int(time.time()), "channel": "spot.candlesticks", "event": "subscribe", # "unsubscribe" for unsubscription "payload": ["1m", "BTC_USDT"] })) print(ws.recv())
+代码示例：
 package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" ) func main() { url := "wss://api.gateio.ws/ws/v4/" conn, _, err := websocket.DefaultDialer.Dial(url, nil) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() subscribe := map[string]interface{}{ "time": time.Now().Unix(), "channel": "spot.candlesticks", "event": "subscribe", "payload": []string{"1m", "BTC_USDT"}, } msg, err := json.Marshal(subscribe) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+代码示例：
+package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" "net/http" ) func main() { url := "wss://api.gateio.ws/ws/v4/" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"timeUnit": []string{"microsecond"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() subscribe := map[string]interface{}{ "time": time.Now().Unix(), "channel": "spot.candlesticks", "event": "subscribe", "payload": []string{"1m", "BTC_USDT"}, } msg, err := json.Marshal(subscribe) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 订阅参数格式:
 | 字段 | 类型 | 必选 | 描述
@@ -389,9 +485,18 @@ TIP
 # 服务端推送
 通知示例：
-{ "time": 1606292600, "channel": "spot.candlesticks", "event": "update", "result": { "t": "1606292580", "v": "2362.32035", "c": "19128.1", "h": "19128.1", "l": "19128.1", "o": "19128.1", "n": "1m_BTC_USDT", "a": "3.8283", "w": true } }
+{ "time": 1606292600, "time_ms": 1606292600123, "channel": "spot.candlesticks", "event": "update", "result": { "t": "1606292580", "v": "2362.32035", "c": "19128.1", "h": "19128.1", "l": "19128.1", "o": "19128.1", "n": "1m_BTC_USDT", "a": "3.8283", "w": true } }
+请求 Header timeUnit: microsecond 开启后，在原有字段之外追加微秒字段。
+spot.candlesticks
+from websocket import create_connection ws = create_connection("wss://api.gateio.ws/ws/v4/", header={"timeUnit": "microsecond"})
+{ "time": 1606292600, "time_ms": 1606292600123, "time_us": 1606292600123456, "channel": "spot.candlesticks", "event": "update", "result": { "t": "1606292580", "t_us": 1606292580000000, "v": "2362.32035", "c": "19128.1", "h": "19128.1", "l": "19128.1", "o": "19128.1", "n": "1m_BTC_USDT", "a": "3.8283", "w": true } }
... (diff truncated, total 1198 lines) ...
```

### Gate.io Futures WebSocket v4 (`gate-futures-ws`)
- Source: https://www.gate.io/docs/developers/futures/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/futures/ws/zh_CN/

```diff
diff --git a/changelogs/gate-futures-ws.txt b/changelogs/gate-futures-ws.txt
index 5d22328..4c7428c 100644
--- a/changelogs/gate-futures-ws.txt
+++ b/changelogs/gate-futures-ws.txt
@@ -1,2 +1,6 @@
+- Python
+- Golang
+- python µs
+- golang µs
 # Gate Futures WebSocket v4.0.0
 Gate 提供简单而强大的 WebSocket API，将 Gate BTC、USDT 和 USD1 结算的永续合约交易状态集成到您的业务或应用程序中。
@@ -25,5 +29,13 @@ WebSocket 应用示例
 # !/usr/bin/env python # coding: utf-8 import hashlib import hmac import json import logging import time import threading from websocket import WebSocketApp logging.basicConfig(level=logging.INFO) logger = logging.getLogger(__name__) event = threading.Event() class GateWebSocketApp(WebSocketApp): def __init__(self, url, api_key, api_secret, **kwargs): super(GateWebSocketApp, self).__init__(url, **kwargs) self._api_key = api_key self._api_secret = api_secret def _send_ping(self): while not event.wait(10): self.last_ping_tm = time.time() if self.sock: try: self.sock.ping() except Exception as ex: logger.warning("send_ping routine terminated: {}".format(ex)) break try: self._request("futures.ping", auth_required=False) except Exception as e: raise e def _request(self, channel, event=None, payload=None, auth_required=True): current_time = int(time.time()) data = { "time": current_time, "channel": channel, "event": event, "payload": payload, } if auth_required: message = 'channel=%s&event=%s&time=%d' % (channel, event, current_time) data['auth'] = { "method": "api_key", "KEY": self._api_key, "SIGN": self.get_sign(message), } data = json.dumps(data) logger.info('request: %s', data) self.send(data) def get_sign(self, message): h = hmac.new(self._api_secret.encode("utf8"), message.encode("utf8"), hashlib.sha512) return h.hexdigest() def subscribe(self, channel, payload=None, auth_required=True): self._request(channel, "subscribe", payload, auth_required) def unsubscribe(self, channel, payload=None, auth_required=True): self._request(channel, "unsubscribe", payload, auth_required) def on_message(ws, message): # type: (GateWebSocketApp, str) -> None # handle message received logger.info("message received from server: {}".format(message)) def on_open(ws): # type: (GateWebSocketApp) -> None # subscribe to channels interested logger.info('websocket connected') ws.subscribe("futures.tickers", ['BTC_USDT'], False) # custom header custom_headers = { "X-Gate-Size-Decimal": "1" } if __name__ == "__main__": logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG) app = GateWebSocketApp("wss://fx-ws.gateio.ws/v4/ws/usdt", "YOUR_API_KEY", "YOUR_API_SECRET", on_open=on_open, on_message=on_message, header=custom_headers) app.run_forever(ping_interval=5)
 WebSocket 应用示例
+# !/usr/bin/env python # coding: utf-8 import hashlib import hmac import json import logging import time import threading from websocket import WebSocketApp logging.basicConfig(level=logging.INFO) logger = logging.getLogger(__name__) event = threading.Event() class GateWebSocketApp(WebSocketApp): def __init__(self, url, api_key, api_secret, **kwargs): super(GateWebSocketApp, self).__init__(url, **kwargs) self._api_key = api_key self._api_secret = api_secret def _send_ping(self): while not event.wait(10): self.last_ping_tm = time.time() if self.sock: try: self.sock.ping() except Exception as ex: logger.warning("send_ping routine terminated: {}".format(ex)) break try: self._request("futures.ping", auth_required=False) except Exception as e: raise e def _request(self, channel, event=None, payload=None, auth_required=True): current_time = int(time.time()) data = { "time": current_time, "channel": channel, "event": event, "payload": payload, } if auth_required: message = 'channel=%s&event=%s&time=%d' % (channel, event, current_time) data['auth'] = { "method": "api_key", "KEY": self._api_key, "SIGN": self.get_sign(message), } data = json.dumps(data) logger.info('request: %s', data) self.send(data) def get_sign(self, message): h = hmac.new(self._api_secret.encode("utf8"), message.encode("utf8"), hashlib.sha512) return h.hexdigest() def subscribe(self, channel, payload=None, auth_required=True): self._request(channel, "subscribe", payload, auth_required) def unsubscribe(self, channel, payload=None, auth_required=True): self._request(channel, "unsubscribe", payload, auth_required) def on_message(ws, message): # type: (GateWebSocketApp, str) -> None # handle message received logger.info("message received from server: {}".format(message)) def on_open(ws): # type: (GateWebSocketApp) -> None # subscribe to channels interested logger.info('websocket connected') ws.subscribe("futures.tickers", ['BTC_USDT'], False) # custom header custom_headers = { "X-Gate-Size-Decimal": "1", "timeUnit": "microsecond" } if __name__ == "__main__": logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG) app = GateWebSocketApp("wss://fx-ws.gateio.ws/v4/ws/usdt", "YOUR_API_KEY", "YOUR_API_SECRET", on_open=on_open, on_message=on_message, header=custom_headers) app.run_forever(ping_interval=5)
+WebSocket 应用示例
 package main import ( "crypto/hmac" "crypto/sha512" "crypto/tls" "encoding/hex" "encoding/json" "fmt" "io" "net/http" "net/url" "time" "github.com/gorilla/websocket" ) type Msg struct { Time int64 `json:"time"` Channel string `json:"channel"` Event string `json:"event"` Payload []string `json:"payload"` Auth *Auth `json:"auth"` } type Auth struct { Method string `json:"method"` KEY string `json:"KEY"` SIGN string `json:"SIGN"` } const ( Key = "YOUR_API_KEY" Secret = "YOUR_API_SECRETY" ) func sign(channel, event string, t int64) string { message := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, t) h2 := hmac.New(sha512.New, []byte(Secret)) io.WriteString(h2, message) return hex.EncodeToString(h2.Sum(nil)) } func (msg *Msg) sign() { signStr := sign(msg.Channel, msg.Event, msg.Time) msg.Auth = &Auth{ Method: "api_key", KEY: Key, SIGN: signStr, } } func (msg *Msg) send(c *websocket.Conn) error { msgByte, err := json.Marshal(msg) if err != nil { return err } return c.WriteMessage(websocket.TextMessage, msgByte) } func NewMsg(channel, event string, t int64, payload []string) *Msg { return &Msg{ Time: t, Channel: channel, Event: event, Payload: payload, } } func main() { u := url.URL{Scheme: "wss", Host: "fx-ws.gateio.ws", Path: "/v4/ws/usdt"} websocket.DefaultDialer.TLSClientConfig = &tls.Config{RootCAs: nil, InsecureSkipVerify: true} c, _, err := websocket.DefaultDialer.Dial(u.String(), http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { panic(err) } c.SetPingHandler(nil) // read msg go func() { for { _, message, err := c.ReadMessage() if err != nil { c.Close() panic(err) } fmt.Printf("recv: %s\n", message) } }() t := time.Now().Unix() pingMsg := NewMsg("futures.ping", "", t, []string{}) err = pingMsg.send(c) if err != nil { panic(err) } // subscribe order book orderBookMsg := NewMsg("futures.order_book", "subscribe", t, []string{"BTC_USDT"}) err = orderBookMsg.send(c) if err != nil { panic(err) } // subscribe positions positionsMsg := NewMsg("futures.positions", "subscribe", t, []string{"USERID", "BTC_USDT"}) positionsMsg.sign() err = positionsMsg.send(c) if err != nil { panic(err) } select {} }
+WebSocket 应用示例
+package main import ( "crypto/hmac" "crypto/sha512" "crypto/tls" "encoding/hex" "encoding/json" "fmt" "io" "net/http" "net/url" "time" "github.com/gorilla/websocket" ) type Msg struct { Time int64 `json:"time"` Channel string `json:"channel"` Event string `json:"event"` Payload []string `json:"payload"` Auth *Auth `json:"auth"` } type Auth struct { Method string `json:"method"` KEY string `json:"KEY"` SIGN string `json:"SIGN"` } const ( Key = "YOUR_API_KEY" Secret = "YOUR_API_SECRETY" ) func sign(channel, event string, t int64) string { message := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, t) h2 := hmac.New(sha512.New, []byte(Secret)) io.WriteString(h2, message) return hex.EncodeToString(h2.Sum(nil)) } func (msg *Msg) sign() { signStr := sign(msg.Channel, msg.Event, msg.Time) msg.Auth = &Auth{ Method: "api_key", KEY: Key, SIGN: signStr, } } func (msg *Msg) send(c *websocket.Conn) error { msgByte, err := json.Marshal(msg) if err != nil { return err } return c.WriteMessage(websocket.TextMessage, msgByte) } func NewMsg(channel, event string, t int64, payload []string) *Msg { return &Msg{ Time: t, Channel: channel, Event: event, Payload: payload, } } func main() { u := url.URL{Scheme: "wss", Host: "fx-ws.gateio.ws", Path: "/v4/ws/usdt"} websocket.DefaultDialer.TLSClientConfig = &tls.Config{RootCAs: nil, InsecureSkipVerify: true} c, _, err := websocket.DefaultDialer.Dial(u.String(), http.Header{"timeUnit": []string{"microsecond"}, "X-Gate-Size-Decimal": []string{"1"}}) if err != nil { panic(err) } c.SetPingHandler(nil) // read msg go func() { for { _, message, err := c.ReadMessage() if err != nil { c.Close() panic(err) } fmt.Printf("recv: %s\n", message) } }() t := time.Now().Unix() pingMsg := NewMsg("futures.ping", "", t, []string{}) err = pingMsg.send(c) if err != nil { panic(err) } // subscribe order book orderBookMsg := NewMsg("futures.order_book", "subscribe", t, []string{"BTC_USDT"}) err = orderBookMsg.send(c) if err != nil { panic(err) } // subscribe positions positionsMsg := NewMsg("futures.positions", "subscribe", t, []string{"USERID", "BTC_USDT"}) positionsMsg.sign() err = positionsMsg.send(c) if err != nil { panic(err) } select {} }
+2026-11-26
+- 请求 Header timeUnit: microsecond 可追加微秒字段，URL Query timeUnit=microsecond 同样生效。公有通道对所有连接生效，私有通道仅 OMS 3.0 生效。详见 微秒时间戳。
+2026-11-20
+- 向 API 用户开放 RPI（Retail Price Improvement）流动性接入功能。普通单笔下单可传 rpi_taker_access。详见 RPI 流动性接入（Speed Bump）。
 2026-11-19
 - 3.0 用户可在 futures.order_place、futures.order_cancel、futures.order_amend、futures.order_cancel_cp 的 payload.req_header 中传入 X-Gate-Client-Send-Us 和 X-Gate-Timeout-Window-Us。这两个参数在撮合引擎生效，撮合引擎按微秒发送时间和超时窗口拒绝过期请求。futures.order_batch_place、futures.order_cancel_ids、futures.order_list、futures.order_status 不转发这两个字段。详见 3.0 用户请求超时。
@@ -193,4 +205,5 @@ TIP
 | time | Integer | 是 | 响应时间
 | time_ms | Integer | 是 | 毫秒响应时间
+| time_us | Integer | 否 | 同 time 字段，微秒精度
 | channel | String | 是 | 响应频道
 | event | String | 是 | 响应频道事件 (update/all)
@@ -199,4 +212,30 @@ TIP
 注意：如果它是服务端发起的数据更新通知 那么 result 的类型是基于 channel 的，不同 channel 的 result 类型有所不同。
 但如果是对客户端订阅请求的响应，那么 result 为固定的 {"status": "success"}。 验证订阅请求是否成功，您只需要检查 error 字段是否为空即可，不需要再解析 result 字段。
+# 微秒时间戳
+握手时用下面任一方式开启，连接建立后不能修改：
+- Header：timeUnit: microsecond
+- URL Query：timeUnit=microsecond
+值必须是全小写 microsecond。Microsecond、空字符串、带空格都等于未开启。Header 的键名不区分大小写，Query 的键名区分大小写，必须是 timeUnit。两者任一命中即开启。不带该参数的连接与升级前一致。
+原有的秒、毫秒字段保留，只追加微秒字段。新增字段是整数。SBE 不追加这些字段。PB 与 JSON 使用同一套开关；未开启的 PB 帧与升级前一致。
+订阅确认、错误和 futures.pong 只在外层追加 time_us，result 里不补业务微秒。time_us 是服务端发出该条消息时的 Unix 微秒。仅 timeUnit: microsecond 开启后推送。
+URL 示例：wss://fx-ws.gateio.ws/v4/ws/usdt?timeUnit=microsecond
+# 公有通道
+已开启的连接都会追加，不区分是不是 OMS 3.0 用户。
+| 通道 | 保留 | 新增
+| futures.trades | create_time、create_time_ms | create_time_us
+| futures.order_book、futures.order_book_update、futures.obu、futures.rpi_order_book、futures.rpi_obu、futures.book_ticker | t（毫秒） | t_us
+| futures.tickers | t（毫秒） | t_us
+| futures.candlesticks | t（秒） | t_us
+| futures.public_liquidates | time、time_ms | time_us
+| futures.contract_stats | time（秒） | time_us
+各通道的微秒示例写在对应频道的推送说明中。
+# OMS 3.0 的私有通道
+已开启，并且该条消息处理时判定为 OMS 3.0，才追加。非 3.0 用户的私有推送与未开启时一致，没有外层 time_us，也没有业务微秒字段。
+| 通道 | 保留 | 新增
+| futures.orders、futures.orders_v2 | create_time、create_time_ms、update_time、update_time_ms、finish_time、finish_time_ms | create_time_us、update_time_us、finish_time_us
+| futures.usertrades | create_time、create_time_ms | create_time_us
+| futures.balances、futures.positions、futures.liquidates、futures.reduce_risk_limits、futures.auto_deleverages | time、time_ms | time_us
+各通道的微秒示例写在对应频道的推送说明中。
+已开启且为 OMS 3.0 时，下单、撤单、改单、查单的响应也会追加对应微秒字段。header 追加 time_us、response_time_us。订单对象追加 create_time_us、update_time_us、finish_time_us。futures.login 不追加。示例写在各接口的响应说明中。
 为了简单起见，下面的频道（channel）描述只给出对应频道的 payload 格式。
 # 错误
@@ -215,4 +254,8 @@ WebSocket 认证使用与 HTTP API 相同的签名计算方法，但具有 以
 # example WebSocket signature calculation implementation in Python import hmac, hashlib, json, time def gen_sign(channel, event, timestamp): # GateAPIv4 key pair api_key = 'YOUR_API_KEY' api_secret = 'YOUR_API_SECRET' s = 'channel=%s&event=%s&time=%d' % (channel, event, timestamp) sign = hmac.new(api_secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest() return {'method': 'api_key', 'KEY': api_key, 'SIGN': sign} request = { 'id': int(time.time() * 1e6), 'time': int(time.time()), 'channel': 'futures.orders', 'event': 'subscribe', 'payload': ["20011", "BTC_USDT"] } request['auth'] = gen_sign(request['channel'], request['event'], request['time']) print(json.dumps(request))
 代码示例
+# example WebSocket signature calculation implementation in Python import hmac, hashlib, json, time def gen_sign(channel, event, timestamp): # GateAPIv4 key pair api_key = 'YOUR_API_KEY' api_secret = 'YOUR_API_SECRET' s = 'channel=%s&event=%s&time=%d' % (channel, event, timestamp) sign = hmac.new(api_secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest() return {'method': 'api_key', 'KEY': api_key, 'SIGN': sign} request = { 'id': int(time.time() * 1e6), 'time': int(time.time()), 'channel': 'futures.orders', 'event': 'subscribe', 'payload': ["20011", "BTC_USDT"] } request['auth'] = gen_sign(request['channel'], request['event'], request['time']) print(json.dumps(request))
+代码示例
+package main import ( "crypto/hmac" "crypto/sha512" "encoding/hex" "encoding/json" "fmt" "time" ) func genSign(channel, event string, timestamp int64) map[string]string { apiKey := "YOUR_API_KEY" apiSecret := "YOUR_API_SECRET" s := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, timestamp) h := hmac.New(sha512.New, []byte(apiSecret)) h.Write([]byte(s)) sign := hex.EncodeToString(h.Sum(nil)) return map[string]string{ "method": "api_key", "KEY": apiKey, "SIGN": sign, } } func main() { timestamp := time.Now().Unix() request := map[string]interface{}{ "id": time.Now().UnixNano() / 1e3, "time": timestamp, "channel": "futures.orders", "event": "subscribe", "payload": []string{"20011", "BTC_USDT"}, } request["auth"] = genSign(request["channel"].(string), request["event"].(string), timestamp) jsonBytes, _ := json.Marshal(request) fmt.Println(string(jsonBytes)) }
+代码示例
 package main import ( "crypto/hmac" "crypto/sha512" "encoding/hex" "encoding/json" "fmt" "time" ) func genSign(channel, event string, timestamp int64) map[string]string { apiKey := "YOUR_API_KEY" apiSecret := "YOUR_API_SECRET" s := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, timestamp) h := hmac.New(sha512.New, []byte(apiSecret)) h.Write([]byte(s)) sign := hex.EncodeToString(h.Sum(nil)) return map[string]string{ "method": "api_key", "KEY": apiKey, "SIGN": sign, } } func main() { timestamp := time.Now().Unix() request := map[string]interface{}{ "id": time.Now().UnixNano() / 1e3, "time": timestamp, "channel": "futures.orders", "event": "subscribe", "payload": []string{"20011", "BTC_USDT"}, } request["auth"] = genSign(request["channel"].(string), request["event"].(string), timestamp) jsonBytes, _ := json.Marshal(request) fmt.Println(string(jsonBytes)) }
 您可以登录账户获取永续合约账户的 api_key 和 secret。
@@ -274,7 +317,19 @@ websocket rfc 协议 (opens new window)
 from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.ping"}') print(ws.recv())
 代码示例
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt", header={"timeUnit": "microsecond"}) ws.send('{"time" : 123456, "channel" : "futures.ping"}') print(ws.recv())
+代码示例
 package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() ping := map[string]interface{}{ "time": time.Now().Unix(), "channel": "futures.ping", } msg, err := json.Marshal(ping) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+代码示例
+package main import ( "encoding/json" "fmt" "log" "time" "github.com/gorilla/websocket" "net/http" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"timeUnit": []string{"microsecond"}, "X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() ping := map[string]interface{}{ "time": time.Now().Unix(), "channel": "futures.ping", } msg, err := json.Marshal(ping) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 futures.ping操作返回 JSON 结构如下：
 { "time": 1545404023, "time_ms": 1545404023123, "channel": "futures.pong", "event": "", "result": null }
+请求 Header timeUnit: microsecond 开启后，pong 只追加外层 time_us。
+futures.pong
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt", header={"timeUnit": "microsecond"})
+{ "time": 1545404023, "time_ms": 1545404023123, "time_us": 1545404023123456, "channel": "futures.pong", "event": "", "result": null }
+请求 Header timeUnit: microsecond 开启后，pong 只追加外层 time_us。
+futures.pong
+conn, _, err := websocket.DefaultDialer.Dial( "wss://fx-ws.gateio.ws/v4/ws/usdt", http.Header{"timeUnit": []string{"microsecond"}}, )
+{ "time": 1545404023, "time_ms": 1545404023123, "time_us": 1545404023123456, "channel": "futures.pong", "event": "", "result": null }
 # 请求参数
 - 频道
@@ -298,5 +353,9 @@ ticker是合约状态的高级概述。它向你展示了最高的， 最低的
 from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.tickers","event": "subscribe", "payload" : ["BTC_USDT"]}') print(ws.recv())
 代码示例
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt", header={"timeUnit": "microsecond"}) ws.send('{"time" : 123456, "channel" : "futures.tickers","event": "subscribe", "payload" : ["BTC_USDT"]}') print(ws.recv())
+代码示例
 package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.tickers","event":"subscribe","payload":["BTC_USDT"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+代码示例
+package main import ( "fmt" "log" "github.com/gorilla/websocket" "net/http" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"timeUnit": []string{"microsecond"}, "X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.tickers","event":"subscribe","payload":["BTC_USDT"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的订阅请求返回 JSON 结构如下：
 { "time": 1545404023, "time_ms": 1545404023123, "channel": "futures.tickers", "event": "subscribe", "result": { "status": "success" } }
@@ -312,4 +371,50 @@ subscribe
 # ticker 推送
 { "time": 1541659086, "time_ms": 1541659086123, "channel": "futures.tickers", "event": "update", "result": [ { "contract": "BTC_USDT", "last": "118.4", "change_percentage": "0.77", "change_from": "24h", "change_price": "0.91", "funding_rate": "-0.000114", "funding_rate_indicative": "0.01875", "mark_price": "118.35", "index_price": "118.36", "total_size": "73648.5", "volume_24h": "745487577", "volume_24h_btc": "117", "volume_24h_usd": "419950", "quanto_base_rate": "", "volume_24h_quote": "1665006", "volume_24h_settle": "178", "volume_24h_base": "5526", "low_24h": "99.2", "high_24h": "132.5", "price_type": "last", "t": 1541659086123 } ] }
+请求 Header timeUnit: microsecond 开启后，在原有字段之外追加微秒字段。
+futures.tickers
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt", header={"timeUnit": "microsecond"})
+{ "time": 1541659086, "time_ms": 1541659086123, "time_us": 1541659086123456, "channel": "futures.tickers", "event": "update", "result": [ { "contract": "BTC_USDT", "last": "118.4", "change_percentage": "0.77", "change_from": "24h", "change_price": "0.91", "funding_rate": "-0.000114", "funding_rate_indicative": "0.01875", "mark_price": "118.35", "index_price": "118.36", "total_size": "73648.5", "volume_24h": "745487577", "volume_24h_btc": "117", "volume_24h_usd": "419950", "quanto_base_rate": "", "volume_24h_quote": "1665006", "volume_24h_settle": "178", "volume_24h_base": "5526", "low_24h": "99.2", "high_24h": "132.5", "price_type": "last", "t": 1541659086123, "t_us": 1541659086123000 } ] }
+永续合约 24hr 价格变动情况推送
+# 推送参数
+- channel
+futures.tickers
+- event
+update
+- params
+| 名称 | 类型 | 描述
+| result | Array | Array of objects
+| 名称 | 类型 | 描述
+| contract | String | 合约名称
+| last | String | 最新成交价
+| change_percentage | String | 涨跌幅
+| funding_rate | String | 资金费率
+| funding_rate_indicative | String | 下一周期预测资金费率（已弃用，改用funding_rate）
+| mark_price | String | 标记价格
+| index_price | String | 指数价格
+| total_size | String | 总数量
+| volume_24h | String | 24 小时成交量
+| quanto_base_rate | String | 双币种合约中基础货币与结算货币的汇率。不存在于其他类型的合同中
+| volume_24h_btc | String | 近 24 小时 BTC 交易量（已弃用，请使用volume_24h_base、volume_24h_quote、volume_24h_settle代替）
+| volume_24h_usd | String | 近 24 小时美元交易量（已弃用，请使用volume_24h_base、volume_24h_quote、volume_24h_settle 代替）
+| volume_24h_quote | String | 近 24 小时交易量，以计价货币计
+| volume_24h_settle | String | 近 24 小时交易量，以结算货币计
+| volume_24h_base | String | 近 24 小时交易量，以基础货币计
+| low_24h | String | 近 24 小时最低交易价
+| high_24h | String | 近 24 小时最高交易价
+| change_from | String | 涨跌幅计算周期，如 24h
+| change_price | String | 涨跌额
+| price_type | String | 价格类型：last（最新价）、mark（标记价）、index（指数价）
+| t | Integer | 行情生成时间戳（毫秒）
+| event_type | String | 连接后首次推送为 snapshot，实时推送通常不返回该字段
+| t_us | Integer | 同 t 字段，微秒精度
+# 取消订阅
+代码示例
+import json from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") req = { "time": 123456, "channel": "futures.tickers", "event": "unsubscribe", "payload": ["BTC_USDT"] } ws.send(json.dumps(req)) print(ws.recv())
+代码示例
+import json from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt", header={"timeUnit": "microsecond"}) req = { "time": 123456, "channel": "futures.tickers", "event": "unsubscribe", "payload": ["BTC_USDT"] } ws.send(json.dumps(req)) print(ws.recv())
+请求 Header timeUnit: microsecond 开启后，在原有字段之外追加微秒字段。
+futures.tickers
+conn, _, err := websocket.DefaultDialer.Dial( "wss://fx-ws.gateio.ws/v4/ws/usdt", http.Header{"timeUnit": []string{"microsecond"}}, )
+{ "time": 1541659086, "time_ms": 1541659086123, "time_us": 1541659086123456, "channel": "futures.tickers", "event": "update", "result": [ { "contract": "BTC_USDT", "last": "118.4", "change_percentage": "0.77", "change_from": "24h", "change_price": "0.91", "funding_rate": "-0.000114", "funding_rate_indicative": "0.01875", "mark_price": "118.35", "index_price": "118.36", "total_size": "73648.5", "volume_24h": "745487577", "volume_24h_btc": "117", "volume_24h_usd": "419950", "quanto_base_rate": "", "volume_24h_quote": "1665006", "volume_24h_settle": "178", "volume_24h_base": "5526", "low_24h": "99.2", "high_24h": "132.5", "price_type": "last", "t": 1541659086123, "t_us": 1541659086123000 } ] }
 永续合约 24hr 价格变动情况推送
 # 推送参数
@@ -344,9 +449,14 @@ update
 | t | Integer | 行情生成时间戳（毫秒）
 | event_type | String | 连接后首次推送为 snapshot，实时推送通常不返回该字段
+| t_us | Integer | 同 t 字段，微秒精度
 # 取消订阅
 代码示例
 import json from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") req = { "time": 123456, "channel": "futures.tickers", "event": "unsubscribe", "payload": ["BTC_USDT"] } ws.send(json.dumps(req)) print(ws.recv())
 代码示例
+import json from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt", header={"timeUnit": "microsecond"}) req = { "time": 123456, "channel": "futures.tickers", "event": "unsubscribe", "payload": ["BTC_USDT"] } ws.send(json.dumps(req)) print(ws.recv())
+代码示例
 package main import ( "encoding/json" "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() req := map[string]interface{}{ "time": 123456, "channel": "futures.tickers", "event": "unsubscribe", "payload": []string{"BTC_USDT"}, } msg, err := json.Marshal(req) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+代码示例
+package main import ( "encoding/json" "fmt" "log" "github.com/gorilla/websocket" "net/http" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"timeUnit": []string{"microsecond"}, "X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() req := map[string]interface{}{ "time": 123456, "channel": "futures.tickers", "event": "unsubscribe", "payload": []string{"BTC_USDT"}, } msg, err := json.Marshal(req) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的命令返回 JSON 结构如下：
 { "time": 1545404900, "time_ms": 1545404900123, "channel": "futures.tickers", "event": "unsubscribe", "result": { "status": "success" } }
@@ -363,5 +473,9 @@ unsubscribe
 from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send('{"time" : 123456, "channel" : "futures.trades","event": "subscribe", "payload" : ["BTC_USDT"]}') print(ws.recv())
 代码示例
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt", header={"timeUnit": "microsecond"}) ws.send('{"time" : 123456, "channel" : "futures.trades","event": "subscribe", "payload" : ["BTC_USDT"]}') print(ws.recv())
+代码示例
 package main import ( "fmt" "log" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.trades","event":"subscribe","payload":["BTC_USDT"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+代码示例
+package main import ( "fmt" "log" "github.com/gorilla/websocket" "net/http" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, http.Header{"timeUnit": []string{"microsecond"}, "X-Gate-Size-Decimal": []string{"1"}}) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() msg := `{"time":123456,"channel":"futures.trades","event":"subscribe","payload":["BTC_USDT"]}` err = conn.WriteMessage(websocket.TextMessage, []byte(msg)) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
 上面的命令返回 JSON 结构如下：
 { "time": 1545405058, "time_ms": 1545405058123, "channel": "futures.trades", "event": "subscribe", "result": { "status": "success" } }
@@ -380,4 +494,8 @@ size 正数表示买家，负数表示卖家
 未携带 X-Gate-Size-Decimal: 1 请求头时，size 为整型（小数张数向下取整）：
 { "channel": "futures.trades", "event": "update", "time": 1541503698, "time_ms": 1541503698123, "result": [ { "size": -108, "id": 27753479, "create_time": 1545136464, "create_time_ms": 1545136464123, "price": "96.4", "contract": "BTC_USDT", "is_internal": true } ] }
+请求 Header timeUnit: microsecond 开启后，在原有字段之外追加微秒字段。
+futures.trades
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt", header={"timeUnit": "microsecond"})
+{ "channel": "futures.trades", "event": "update", "time": 1541503698, "time_ms": 1541503698123, "time_us": 1541503698123456, "result": [ { "size": -108, "id": 27753479, "create_time": 1545136464, "create_time_ms": 1545136464123, "create_time_us": 1545136464123000, "price": "96.4", "contract": "BTC_USDT", "is_internal": true } ] }
 通知最新交易更新
 # 推送参数
@@ -395,4 +513,5 @@ update
 | create_time | int | 交易消息创建时间
 | create_time_ms | int | 交易消息创建时间（以毫秒为单位）
+| create_time_us | Integer | 同 create_time 字段，微秒精度
 | price | string | 交易价格
 | is_internal | bool | 是否为内部成交。内部成交是指保险资金和 ADL 用户对强平指令的接管。由于不是市场深度上的正常撮合，交易价格可能会出现偏差，不会记录在 K 线上。如果不是内部交易，则该字段不会被返回。
@@ -401,5 +520,36 @@ update
 from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") ws.send( '{"time" : 123456, "channel" : "futures.trades", "event": "subscribe", "payload" : ["BTC_USDT"]}') print(ws.recv())
 代码示例
+from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt", header={"timeUnit": "microsecond"}) ws.send( '{"time" : 123456, "channel" : "futures.trades", "event": "subscribe", "payload" : ["BTC_USDT"]}') print(ws.recv())
+请求 Header timeUnit: microsecond 开启后，在原有字段之外追加微秒字段。
+futures.trades
+conn, _, err := websocket.DefaultDialer.Dial( "wss://fx-ws.gateio.ws/v4/ws/usdt", http.Header{"timeUnit": []string{"microsecond"}}, )
+{ "channel": "futures.trades", "event": "update", "time": 1541503698, "time_ms": 1541503698123, "time_us": 1541503698123456, "result": [ { "size": -108, "id": 27753479, "create_time": 1545136464, "create_time_ms": 1545136464123, "create_time_us": 1545136464123000, "price": "96.4", "contract": "BTC_USDT", "is_internal": true } ] }
... (diff truncated, total 1565 lines) ...
```
