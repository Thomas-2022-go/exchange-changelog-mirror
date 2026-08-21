<!-- has_changes=true date=2026-08-21 -->
# Exchange API Changelog Diff

Generated: 2026-08-21 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132451 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (214550 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [OK] Bybit V5 (`bybit`): no change (92211 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (37469 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [CHANGED] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): 172 diff lines



## Changes

### Gate.io Futures WebSocket v4 (`gate-futures-ws`)
- Source: https://www.gate.io/docs/developers/futures/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/futures/ws/zh_CN/

```diff
diff --git a/changelogs/gate-futures-ws.txt b/changelogs/gate-futures-ws.txt
index 411f1ce..9817219 100644
--- a/changelogs/gate-futures-ws.txt
+++ b/changelogs/gate-futures-ws.txt
@@ -1,7 +1,7 @@
 # Gate Futures WebSocket v4.0.0
-Gate 提供简单而强大的 Websocket API，将 Gate BTCUSDT 永续合约交易状态集成到您的业务或应用程序中。
+Gate 提供简单而强大的 WebSocket API，将 Gate BTC、USDT 和 USD1 结算的永续合约交易状态集成到您的业务或应用程序中。
 我们在 Python 和 Golang 中有语言绑定，将来还会有更多！您可以在右侧的深色区域中查看代码示例，并且可以通过右上角的选项卡切换示例的编程语言
 # 服务地址
-我们提供 BTC/USDT 结算永续合约交易服务器地址，您可以根据自己的情况选择其中之一
+我们提供 BTC、USDT 和 USD1 结算永续合约交易服务器地址，您可以根据自己的情况选择其中之一。
 # BTC Contract
 地址列表:
@@ -13,4 +13,8 @@ Gate 提供简单而强大的 Websocket API，将 Gate BTCUSDT 永续合约交
 - 线上SBE: wss://fx-ws.gateio.ws/v4/ws/usdt/sbe
 - 模拟盘交易: wss://ws-testnet.gate.com/v4/ws/futures/usdt
+# USD1 Contract
+地址列表:
+- 线上交易: wss://fx-ws.gateio.ws/v4/ws/usd1
+- 合约示例: BTC_USD1
 TIP
 建议使用SBE以获取更快的行情和更小的带宽成本
@@ -22,4 +26,9 @@ WebSocket 应用示例
 WebSocket 应用示例
 package main import ( "crypto/hmac" "crypto/sha512" "crypto/tls" "encoding/hex" "encoding/json" "fmt" "io" "net/http" "net/url" "time" "github.com/gorilla/websocket" ) type Msg struct { Time int64 `json:"time"` Channel string `json:"channel"` Event string `json:"event"` Payload []string `json:"payload"` Auth *Auth `json:"auth"` } type Auth struct { Method string `json:"method"` KEY string `json:"KEY"` SIGN string `json:"SIGN"` } const ( Key = "YOUR_API_KEY" Secret = "YOUR_API_SECRETY" ) func sign(channel, event string, t int64) string { message := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, t) h2 := hmac.New(sha512.New, []byte(Secret)) io.WriteString(h2, message) return hex.EncodeToString(h2.Sum(nil)) } func (msg *Msg) sign() { signStr := sign(msg.Channel, msg.Event, msg.Time) msg.Auth = &Auth{ Method: "api_key", KEY: Key, SIGN: signStr, } } func (msg *Msg) send(c *websocket.Conn) error { msgByte, err := json.Marshal(msg) if err != nil { return err } return c.WriteMessage(websocket.TextMessage, msgByte) } func NewMsg(channel, event string, t int64, payload []string) *Msg { return &Msg{ Time: t, Channel: channel, Event: event, Payload: payload, } } func main() { u := url.URL{Scheme: "wss", Host: "fx-ws.gateio.ws", Path: "/v4/ws/usdt"} websocket.DefaultDialer.TLSClientConfig = &tls.Config{RootCAs: nil, InsecureSkipVerify: true} c, _, err := websocket.DefaultDialer.Dial(u.String(), http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { panic(err) } c.SetPingHandler(nil) // read msg go func() { for { _, message, err := c.ReadMessage() if err != nil { c.Close() panic(err) } fmt.Printf("recv: %s\n", message) } }() t := time.Now().Unix() pingMsg := NewMsg("futures.ping", "", t, []string{}) err = pingMsg.send(c) if err != nil { panic(err) } // subscribe order book orderBookMsg := NewMsg("futures.order_book", "subscribe", t, []string{"BTC_USDT"}) err = orderBookMsg.send(c) if err != nil { panic(err) } // subscribe positions positionsMsg := NewMsg("futures.positions", "subscribe", t, []string{"USERID", "BTC_USDT"}) positionsMsg.sign() err = positionsMsg.send(c) if err != nil { panic(err) } select {} }
+2026-08-20
+- 新增频道 futures.contract_info，推送合约精度信息（张乘数、下单价格精度、标记价格精度）与风险限额档位变更
+- 频道 futures.public_liquidates 调整为聚合推送：同一合约在一个聚合周期内的多笔强平订单将合并为数组批量推送，不再丢弃周期内的其他强平订单
+2026-08-19
+- 新增 USD1 结算永续合约 WebSocket 支持，线上地址为 wss://fx-ws.gateio.ws/v4/ws/usd1，settle 值使用小写 usd1
 2026-04-14
 - 部分频道支持SBE数据推送: futures.trades、futures.obu、futures.book_ticker、futures.tickers、futures.candlesticks、futures.order_book、futures.order_book_update、futures.usertrades、futures.positions、futures.orders。
@@ -687,5 +696,5 @@ futures.candlesticks
 unsubscribe
 # 公共强平订单频道
-提供一种接收Gate强平订单信息的方式,每个合约每1秒最多推一条强平订单数据
+提供一种接收Gate强平订单信息的方式。同一合约在一个聚合周期（默认1秒）内产生的强平订单将聚合为数组批量推送；当单个合约缓存的强平订单数量达到上限（默认20笔）时，将立即提前推送
 # 公共强平订单订阅
 如果您想订阅所有合约中的强平订单推送，请在订阅请求列表中使用 !all
@@ -706,7 +715,7 @@ subscribe
 | contract | String | 是 | 合约名称列表
 # 公共强平订单推送
-{ "channel": "futures.public_liquidates", "event": "update", "time": 1541505434, "time_ms": 1541505434123, "result": [ { "price": "215.1", "size": "-124.5", "time": 1541486601, "contract": "BTC_USDT" } ] }
+{ "channel": "futures.public_liquidates", "event": "update", "time": 1541505434, "time_ms": 1541505434123, "result": [ { "price": "215.1", "size": "-124.5", "time": 1541486601123, "contract": "BTC_USDT" }, { "price": "215.2", "size": "-10.5", "time": 1541486601456, "contract": "BTC_USDT" } ] }
 未携带 X-Gate-Size-Decimal: 1 请求头时，size 为整型：
-{ "channel": "futures.public_liquidates", "event": "update", "time": 1541505434, "time_ms": 1541505434123, "result": [ { "price": "215.1", "size": -124, "time": 1541486601, "contract": "BTC_USDT" } ] }
+{ "channel": "futures.public_liquidates", "event": "update", "time": 1541505434, "time_ms": 1541505434123, "result": [ { "price": "215.1", "size": -124, "time": 1541486601123, "contract": "BTC_USDT" }, { "price": "215.2", "size": -10, "time": 1541486601456, "contract": "BTC_USDT" } ] }
 推送公共强制平仓更新
 # 推送参数
@@ -717,9 +726,9 @@ update
 - params
 | 名称 | 类型 | 描述
-| result | Array | Array of objects
+| result | Array | 同一合约在聚合周期内的全部强平订单列表，可能包含多笔记录
 | 名称 | 类型 | 描述
 | price | Float | 订单价格
 | size | String/Integer | 强平订单数量
-| time_ms | Integer | 时间（以毫秒为单位）
+| time | Integer | 强平时间（以毫秒为单位）
 | contract | String | 合约名称
 # 取消订阅
@@ -736,4 +745,66 @@ futures.public_liquidates
 - event
 unsubscribe
+# 合约信息频道
+contract_info 通道允许您接收合约精度信息（张乘数、下单价格精度、标记价格精度）与风险限额档位的变更推送
+# 合约信息订阅
+如果您想订阅所有合约的信息推送，请在订阅请求列表中使用 !all
+代码示例
+import json from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") req = { "time": 123456, "channel": "futures.contract_info", "event": "subscribe", "payload": ["BTC_USDT"], } ws.send(json.dumps(req)) print(ws.recv())
+代码示例
+package main import ( "fmt" "log" "encoding/json" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, nil) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() req := map[string]interface{}{ "time": 123456, "channel": "futures.contract_info", "event": "subscribe", "payload": []string{"BTC_USDT"}, } msg, err := json.Marshal(req) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+上面的命令返回 JSON 结构如下：
+{ "time": 1545459681, "time_ms": 1545459681123, "channel": "futures.contract_info", "event": "subscribe", "result": { "status": "success" } }
+订阅合约信息推送
+# 请求参数
+- channel
+futures.contract_info
+- event
+subscribe
+- params
+| 名称 | 类型 | 必选 | 描述
+| contract | String | 是 | 合约名称列表
+# 合约信息推送
+订阅成功后，若服务端已有该合约的缓存快照，将立即推送一条 event 为 all 的全量消息；此后当合约精度信息或风险限额档位发生变更时，将推送 event 为 update 的消息。仅精度信息变更时，update 消息可能不携带 risk_limit_tiers 字段。
+订阅成功后的首次推送（event=all）：
+{ "channel": "futures.contract_info", "event": "all", "time": 1541505434, "time_ms": 1541505434123, "result": { "contract": "BTC_USDT", "quanto_multiplier": "0.0001", "order_price_round": "0.1", "mark_price_round": "0.01", "risk_limit_tiers": [ { "tier": 1, "risk_limit": "1000000", "initial_rate": "0.01", "maintenance_rate": "0.005", "leverage_max": "100", "contract": "BTC_USDT", "deduction": "0" } ] } }
+合约信息变更推送（event=update）：
+{ "channel": "futures.contract_info", "event": "update", "time": 1541505434, "time_ms": 1541505434123, "result": { "contract": "BTC_USDT", "quanto_multiplier": "0.0001", "order_price_round": "0.5", "mark_price_round": "0.01" } }
+推送合约信息更新
+# 推送参数
+- channel
+futures.contract_info
+- event
+all / update
+- params
+| 名称 | 类型 | 描述
+| result | Object | 合约信息对象，event 为 all 时表示当前快照，update 时表示变更后的最新信息
+| 名称 | 类型 | 描述
+| contract | String | 合约名称
+| quanto_multiplier | String | 张乘数
+| order_price_round | String | 下单价格精度
+| mark_price_round | String | 标记价格精度
+| risk_limit_tiers | Array | 风险限额档位列表，仅精度信息变更时可能不携带
+risk_limit_tiers 字段说明：
+| 名称 | 类型 | 描述
+| tier | Integer | 档位
+| risk_limit | String | 风险限额
+| initial_rate | String | 初始保证金率
+| maintenance_rate | String | 维持保证金率
+| leverage_max | String | 最大杠杆倍数
+| contract | String | 合约名称
+| deduction | String | 维持保证金速算额
+# 取消订阅
+代码示例
+import json from websocket import create_connection ws = create_connection("wss://fx-ws.gateio.ws/v4/ws/usdt") req = { "time": 123456, "channel": "futures.contract_info", "event": "unsubscribe", "payload": ["BTC_USDT"], } ws.send(json.dumps(req)) print(ws.recv())
+代码示例
+package main import ( "fmt" "log" "encoding/json" "github.com/gorilla/websocket" ) func main() { url := "wss://fx-ws.gateio.ws/v4/ws/usdt" conn, _, err := websocket.DefaultDialer.Dial(url, nil) if err != nil { log.Fatal("dial error:", err) } defer conn.Close() req := map[string]interface{}{ "time": 123456, "channel": "futures.contract_info", "event": "unsubscribe", "payload": []string{"BTC_USDT"}, } msg, err := json.Marshal(req) if err != nil { log.Fatal("json marshal error:", err) } err = conn.WriteMessage(websocket.TextMessage, msg) if err != nil { log.Fatal("write message error:", err) } _, message, err := conn.ReadMessage() if err != nil { log.Fatal("read message error:", err) } fmt.Println(string(message)) }
+上面的命令返回 JSON 结构如下：
+{ "time": 1545459681, "time_ms": 1545459681123, "channel": "futures.contract_info", "event": "unsubscribe", "result": { "status": "success" } }
+取消订阅合约信息更新
+# 请求参数
+- channel
+futures.contract_info
+- event
+unsubscribe
 # 合约统计信息频道
 contract_stats 通道允许您获取合约统计信息
@@ -897,22 +968,4 @@ type=market 时仅支持 ioc 和 fok
 | id_string | String | 订单 ID 字符串形式
 | is_voucher | Bool | 是否体验金订单
-| biz_info | String | 用户备注的修改信息
-| stp_act | String | 自成交防范策略
-| stp_id | String | STP 组 ID
-| amend_text | String | 改单备注
-| role | String | 成交角色
-| fee | Float | 手续费
-| point_fee | Float | 点卡手续费
-| bbo | String | BBO 下单选项
-| pos_margin_mode | String | 仓位保证金模式
-| leverage | String | 杠杆（字符串）
-| stop_profit | Object | 止盈扩展信息，含 tp/op/type
-| stop_loss | Object | 止损扩展信息，含 tp/op/type
-| id_string | String | 订单 ID 字符串形式
-| is_voucher | Bool | 是否体验金订单
-| biz_info | String | 用户备注的修改信息
-| stp_act | String | 自成交防范策略
-| stp_id | String | STP 组 ID
-| amend_text | String | 改单备注
 | role | String | 成交角色
 | fee | Float | 手续费
@@ -1002,7 +1055,4 @@ update
 | biz_info | String | 业务备注信息
 | close_size | String | 平仓数量
-| amend_text | String | 改单备注
-| biz_info | String | 业务备注信息
-| close_size | String | 平仓数量
 # 取消订阅
 代码示例
@@ -1362,6 +1412,4 @@ update
 | pos_margin_mode | String | 仓位保证金模式（逐仓/全仓等）
 | lever | String | 杠杆信息（逐步替代 leverage 等字段）
-| pos_margin_mode | String | 仓位保证金模式（逐仓/全仓等）
-| lever | String | 杠杆信息（逐步替代 leverage 等字段）
 # 取消订阅
 代码示例
@@ -2025,3 +2073,3 @@ req_param` API 订单模型的 JSON 字节数据:
 | »»label | String | 错误类型
 | »»message | String | 详细错误信息
-Last Updated: 7/25/2026, 7:18:17 AM
+Last Updated: 8/20/2026, 9:53:30 AM

```
