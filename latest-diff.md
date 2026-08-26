<!-- has_changes=true date=2026-08-26 -->
# Exchange API Changelog Diff

Generated: 2026-08-26 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132451 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (214540 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [OK] Bybit V5 (`bybit`): no change (92575 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (37983 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [CHANGED] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): 71 diff lines



## Changes

### Gate.io Futures WebSocket v4 (`gate-futures-ws`)
- Source: https://www.gate.io/docs/developers/futures/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/futures/ws/zh_CN/

```diff
diff --git a/changelogs/gate-futures-ws.txt b/changelogs/gate-futures-ws.txt
index 9817219..776d5cd 100644
--- a/changelogs/gate-futures-ws.txt
+++ b/changelogs/gate-futures-ws.txt
@@ -26,4 +26,6 @@ WebSocket 应用示例
 WebSocket 应用示例
 package main import ( "crypto/hmac" "crypto/sha512" "crypto/tls" "encoding/hex" "encoding/json" "fmt" "io" "net/http" "net/url" "time" "github.com/gorilla/websocket" ) type Msg struct { Time int64 `json:"time"` Channel string `json:"channel"` Event string `json:"event"` Payload []string `json:"payload"` Auth *Auth `json:"auth"` } type Auth struct { Method string `json:"method"` KEY string `json:"KEY"` SIGN string `json:"SIGN"` } const ( Key = "YOUR_API_KEY" Secret = "YOUR_API_SECRETY" ) func sign(channel, event string, t int64) string { message := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, t) h2 := hmac.New(sha512.New, []byte(Secret)) io.WriteString(h2, message) return hex.EncodeToString(h2.Sum(nil)) } func (msg *Msg) sign() { signStr := sign(msg.Channel, msg.Event, msg.Time) msg.Auth = &Auth{ Method: "api_key", KEY: Key, SIGN: signStr, } } func (msg *Msg) send(c *websocket.Conn) error { msgByte, err := json.Marshal(msg) if err != nil { return err } return c.WriteMessage(websocket.TextMessage, msgByte) } func NewMsg(channel, event string, t int64, payload []string) *Msg { return &Msg{ Time: t, Channel: channel, Event: event, Payload: payload, } } func main() { u := url.URL{Scheme: "wss", Host: "fx-ws.gateio.ws", Path: "/v4/ws/usdt"} websocket.DefaultDialer.TLSClientConfig = &tls.Config{RootCAs: nil, InsecureSkipVerify: true} c, _, err := websocket.DefaultDialer.Dial(u.String(), http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { panic(err) } c.SetPingHandler(nil) // read msg go func() { for { _, message, err := c.ReadMessage() if err != nil { c.Close() panic(err) } fmt.Printf("recv: %s\n", message) } }() t := time.Now().Unix() pingMsg := NewMsg("futures.ping", "", t, []string{}) err = pingMsg.send(c) if err != nil { panic(err) } // subscribe order book orderBookMsg := NewMsg("futures.order_book", "subscribe", t, []string{"BTC_USDT"}) err = orderBookMsg.send(c) if err != nil { panic(err) } // subscribe positions positionsMsg := NewMsg("futures.positions", "subscribe", t, []string{"USERID", "BTC_USDT"}) positionsMsg.sign() err = positionsMsg.send(c) if err != nil { panic(err) } select {} }
+2026-08-25
+- 新增市场级 ADL 风险预警公共频道 futures.adl_warning
 2026-08-20
 - 新增频道 futures.contract_info，推送合约精度信息（张乘数、下单价格精度、标记价格精度）与风险限额档位变更
@@ -871,4 +873,54 @@ unsubscribe
 | interval | String | Yes | Interval : "1m", "5m", "15m", "30m", "1h", "4h", "8h", "1d", "3d", "7d"
 注意：contract为unsub_all，表示全部取消
+# ADL 风险预警频道
+公共频道 futures.adl_warning 用于推送市场级 ADL 风险预警。
+该频道无需鉴权，仅支持 JSON 连接。
+# ADL 风险预警订阅
+订阅一个或多个合约：
+{ "time": 1781234567, "channel": "futures.adl_warning", "event": "subscribe", "payload": ["BTC_USDT", "ETH_USDT"] }
+订阅当前连接结算币种下的全部合约：
+{ "time": 1781234567, "channel": "futures.adl_warning", "event": "subscribe", "payload": ["!all"] }
+订阅命中的合约当前全部为 normal 时，服务端只返回订阅响应：
+{ "time": 1781234567, "time_ms": 1781234567123, "channel": "futures.adl_warning", "event": "subscribe", "payload": ["BTC_USDT", "ETH_USDT"], "result": { "status": "success" } }
+# 请求参数
+- channel
+futures.adl_warning
+- event
+subscribe
+- params
+| 参数 | 类型 | 是否必需 | 描述
+| contract | String | 是 | 合约名称。支持传入多个合约；仅传入 !all 时订阅当前结算币种下的全部合约
+payload 不能为空。!all 不能与具体合约名称混用，指定的合约必须属于当前连接的结算币种。重复的合约名称会被忽略。
+如果订阅命中的合约已经处于 warning 或 adl_risk，对应的 event=all 首次快照会先于订阅响应发送。
+# ADL 风险预警推送
+订阅后的首次风险快照：
+{ "time": 1781234567, "time_ms": 1781234567123, "channel": "futures.adl_warning", "event": "all", "result": { "contract": "BTC_USDT", "settle": "usdt", "state": "warning", "update_time": 1781234567000 } }
+风险状态推送：
+{ "time": 1781234568, "time_ms": 1781234568123, "channel": "futures.adl_warning", "event": "update", "result": { "contract": "BTC_USDT", "settle": "usdt", "state": "adl_risk", "update_time": 1781234567000 } }
+恢复状态推送：
+{ "time": 1781234578, "time_ms": 1781234578123, "channel": "futures.adl_warning", "event": "update", "result": { "contract": "BTC_USDT", "settle": "usdt", "state": "normal", "update_time": 1781234577000 } }
+# 推送参数
+- channel
+futures.adl_warning
+- event
+首次风险快照为 all，后续推送为 update
+- params
+| 字段 | 类型 | 描述
+| contract | String | 合约名称
+| settle | String | 小写结算币种，例如 btc、usdt 或 usd1
+| state | String | ADL 风险状态：normal、warning 或 adl_risk
+| update_time | Integer | 风险状态的计算时间，Unix 毫秒
+warning 和 adl_risk 状态持续期间每秒推送一次。恢复为 normal 时只推送一次，不会重复推送。首次订阅时处于 normal 的合约不会发送首次快照。
+# 取消 ADL 风险预警订阅
+{ "time": 1781234579, "channel": "futures.adl_warning", "event": "unsubscribe", "payload": ["BTC_USDT", "ETH_USDT"] }
+服务端返回：
+{ "time": 1781234579, "time_ms": 1781234579123, "channel": "futures.adl_warning", "event": "unsubscribe", "payload": ["BTC_USDT", "ETH_USDT"], "result": { "status": "success" } }
+# 请求参数
+- channel
+futures.adl_warning
+- event
+unsubscribe
+- params
+与订阅使用相同的 payload 规则。使用 ["!all"] 取消全部合约订阅。
 # 订单频道
 提供接收用户订单的推送
@@ -2073,3 +2125,3 @@ req_param` API 订单模型的 JSON 字节数据:
 | »»label | String | 错误类型
 | »»message | String | 详细错误信息
-Last Updated: 8/20/2026, 9:53:30 AM
+Last Updated: 8/25/2026, 6:35:20 AM

```
