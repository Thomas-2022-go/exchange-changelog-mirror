<!-- has_changes=true date=2026-11-03 -->
# Exchange API Changelog Diff

Generated: 2026-11-03 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (137687 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 13 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [OK] Bybit V5 (`bybit`): no change (99034 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 26 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [CHANGED] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): 117 diff lines



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 41d9ac7..8b98b83 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -23,6 +23,6 @@ REST API 不受影响。
 | 64010 | WebSocket 8443 端口即将下线，请迁移至 443 端口。
 SBE 交易及私有数据
-最近更新：2026 年 10 月 27 日
-欧易计划推出简单二进制编码（Simple Binary Encoding，SBE）交易服务，以及私有订单与成交数据服务。相关服务预计于 2026 年 11 月上旬上线模拟交易环境，并于 2026 年 12 月上旬上线生产环境。
+最近更新：2026 年 10 月 28 日
+欧易计划推出简单二进制编码（Simple Binary Encoding，SBE）交易服务，以及私有订单与成交数据服务。相关服务预计于 2026 年 11 月 11 日上线模拟交易环境，并于 2026 年 12 月上旬上线生产环境。
 现有 REST API 和 JSON WebSocket API 不受影响。
 新增 SBE 服务

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index 68aea6e..22cfeef 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,4 +1,20 @@
+2026.11.06#
+[Add] UTA WebSocket Private Channel FundingFeeSettle
+[Modify] Classic REST Get Account Summary Info (V3)
+Updated response structure to V3:
+Removed: subQuantity, spotSubQuantity, futuresSubQuantity, marginSubQuantity, optionSubQuantity, maxSubQuantity, maxDefaultSubQuantity, maxSpotSubQuantity, maxFuturesSubQuantity, maxMarginSubQuantity, maxOptionSubQuantity
+Added: level, maxSharedSubCount, usedSharedSubCount
+Updated response required fields:
+level, maxSharedSubCount, usedSharedSubCount
+[Modify] UTA REST Add Sub Account
+Added optional request field:
+mode — CLASSIC creates a classic sub-account; UNIFIED creates a unified sub-account
+[Modify] Classic REST Add Sub Account (Classic)
+Updated summary:
+Add sub-account → Add Sub Account (Classic)
+Added optional request field:
+mode — CLASSIC creates a classic sub-account; UNIFIED creates a unified sub-account
 2026.11.02#
-[Modify] UTA REST Get Loan Market
+[Modify] UTA REST Get Orderbook
 API Access Adjustment
 Effective Time: November 2, 2026, at 17:00 (UTC+8)

```

### Gate.io Futures WebSocket v4 (`gate-futures-ws`)
- Source: https://www.gate.io/docs/developers/futures/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/futures/ws/zh_CN/

```diff
diff --git a/changelogs/gate-futures-ws.txt b/changelogs/gate-futures-ws.txt
index a142e5e..dcf2a0a 100644
--- a/changelogs/gate-futures-ws.txt
+++ b/changelogs/gate-futures-ws.txt
@@ -26,4 +26,8 @@ WebSocket 应用示例
 WebSocket 应用示例
 package main import ( "crypto/hmac" "crypto/sha512" "crypto/tls" "encoding/hex" "encoding/json" "fmt" "io" "net/http" "net/url" "time" "github.com/gorilla/websocket" ) type Msg struct { Time int64 `json:"time"` Channel string `json:"channel"` Event string `json:"event"` Payload []string `json:"payload"` Auth *Auth `json:"auth"` } type Auth struct { Method string `json:"method"` KEY string `json:"KEY"` SIGN string `json:"SIGN"` } const ( Key = "YOUR_API_KEY" Secret = "YOUR_API_SECRETY" ) func sign(channel, event string, t int64) string { message := fmt.Sprintf("channel=%s&event=%s&time=%d", channel, event, t) h2 := hmac.New(sha512.New, []byte(Secret)) io.WriteString(h2, message) return hex.EncodeToString(h2.Sum(nil)) } func (msg *Msg) sign() { signStr := sign(msg.Channel, msg.Event, msg.Time) msg.Auth = &Auth{ Method: "api_key", KEY: Key, SIGN: signStr, } } func (msg *Msg) send(c *websocket.Conn) error { msgByte, err := json.Marshal(msg) if err != nil { return err } return c.WriteMessage(websocket.TextMessage, msgByte) } func NewMsg(channel, event string, t int64, payload []string) *Msg { return &Msg{ Time: t, Channel: channel, Event: event, Payload: payload, } } func main() { u := url.URL{Scheme: "wss", Host: "fx-ws.gateio.ws", Path: "/v4/ws/usdt"} websocket.DefaultDialer.TLSClientConfig = &tls.Config{RootCAs: nil, InsecureSkipVerify: true} c, _, err := websocket.DefaultDialer.Dial(u.String(), http.Header{"X-Gate-Size-Decimal": []string{"1"}}) if err != nil { panic(err) } c.SetPingHandler(nil) // read msg go func() { for { _, message, err := c.ReadMessage() if err != nil { c.Close() panic(err) } fmt.Printf("recv: %s\n", message) } }() t := time.Now().Unix() pingMsg := NewMsg("futures.ping", "", t, []string{}) err = pingMsg.send(c) if err != nil { panic(err) } // subscribe order book orderBookMsg := NewMsg("futures.order_book", "subscribe", t, []string{"BTC_USDT"}) err = orderBookMsg.send(c) if err != nil { panic(err) } // subscribe positions positionsMsg := NewMsg("futures.positions", "subscribe", t, []string{"USERID", "BTC_USDT"}) positionsMsg.sign() err = positionsMsg.send(c) if err != nil { panic(err) } select {} }
+2026-10-22
+- 补充 futures.adl_warning 的功能说明、三种市场级风险状态的含义，以及其与单个用户仓位和实际 ADL 事件的关系。
+2026-10-16
+- 新增订单频道 futures.orders_v2，支持实盘和模拟盘，仅限 USDT 结算合约 API WebSocket 的 UTA3.0 用户。该 JSON 频道推送订单创建、成交、改单和撤单事件，包含订单管理系统（OMS）和撮合引擎（ME）的毫秒时间戳，不含清算信息。
 2026-10-14
 - 新增公开频道 futures.rpi_order_book，futures.rpi_obu 推送 RPI 深度全量快照
@@ -993,4 +997,17 @@ unsubscribe
 公共频道 futures.adl_warning 用于推送市场级 ADL 风险预警。
 该频道无需鉴权，仅支持 JSON 连接。
+市场级自动减仓（ADL）风险预警用于帮助用户了解某个合约市场发生 ADL 的风险变化。平台根据保险基金在该市场的持仓情况及对应市场限额判断风险状态，对外仅提供状态结果，不公开底层具体阈值和计算公式。
+用户需主动建立 WebSocket 连接并订阅对应频道或合约后才会收到推送；未订阅或断开连接后不会收到推送。
+# 状态说明
+| 状态 | 对外含义
+| normal | 市场发生 ADL 的概率较小，但突发的大幅市场波动可能产生大量强平单并触发 ADL。
+| warning | 市场发生 ADL 的概率较大，表示保险基金承接强平单的剩余能力有限，该市场接下来新产生的强平单很可能通过 ADL 执行。
+| adl_risk | 保险基金已无法再承接该市场的强平单，新产生的强平单只能通过 ADL 执行。该状态本身不代表 ADL 已经发生。
+# 补充说明
+- normal、warning、adl_risk 是市场级风险状态，不代表单个用户仓位一定会或不会被 ADL。
+- adl_risk 不等同于 ADL 已经发生，也不代表所有用户都会受到 ADL 影响。
+- 该状态仅用于帮助用户了解市场风险变化，不构成交易建议。
+- 用户基于该状态进行减仓、加仓、撤单、调整策略等操作，应自行承担对应交易结果。
+- 如需查询历史强平单记录，请参考查询强平委托历史 (opens new window)。
 # ADL 风险预警订阅
 订阅一个或多个合约：
@@ -1026,5 +1043,5 @@ futures.adl_warning
 | contract | String | 合约名称
 | settle | String | 小写结算币种，例如 btc、usdt 或 usd1
-| state | String | ADL 风险状态：normal、warning 或 adl_risk
+| state | String | 市场级 ADL 风险状态：normal、warning 或 adl_risk，详见状态说明
 | update_time | Integer | 风险状态的计算时间，Unix 毫秒
 warning 和 adl_risk 状态持续期间每秒推送一次。恢复为 normal 时只推送一次，不会重复推送。首次订阅时处于 normal 的合约不会发送首次快照。
@@ -1158,4 +1175,73 @@ futures.orders
 - event
 unsubscribe
+# 订单频道 V2
+支持环境：USDT 合约实盘和模拟盘。
+- 实盘：wss://fx-ws.gateio.ws/v4/ws/usdt
+- 模拟盘：wss://ws-testnet.gate.com/v4/ws/futures/usdt
+futures.orders_v2 实时推送撮合阶段、清算前的订单创建、成交、改单和撤销事件。仅支持 USDT 结算合约 API WebSocket 的 UTA3.0 用户，采用 JSON 编码；不支持 PB 和 SBE 订阅。
+本频道需要认证，以已认证用户决定推送的订单，并检查该用户的 UTA3.0 资格。payload 中提供的用户 ID 不能用于切换到其他账户。
+本频道不推送清算订单及清算信息。保留费率字段 mkfr，省略 fee、point_fee、role、refu、refr、tkfr 和 update_time；ME 时间使用 update_time_ms。
+同一连接可以独立订阅 futures.orders 和 futures.orders_v2。不能根据两个频道的消息到达先后推断事件顺序。账户迁移至 UTA3.0 后，重新订阅即可使用本频道。
+# 订单 V2 订阅
+请求使用 channel: "futures.orders_v2"、event: "subscribe"；根据认证章节，使用本频道名称、事件和请求时间生成签名。
+{ "time": 1628736847, "channel": "futures.orders_v2", "event": "subscribe", "payload": [ "BTC_USDT" ], "auth": { "method": "api_key", "KEY": "xxxx", "SIGN": "xxxx" } }
+{ "time": 1628736847, "time_ms": 1628736847320, "channel": "futures.orders_v2", "event": "subscribe", "result": { "status": "success" } }
+订阅参数：
+| 字段 | 类型 | 必选 | 描述
+| payload | Array[String] | 是 | 合约列表，可在首项携带用户 ID。例如 ["BTC_USDT"]、["20011", "BTC_USDT", "ETH_USDT"] 或 ["!all"]。
+列表中的单项也可以包含以逗号分隔的合约，例如 "BTC_USDT,ETH_USDT"。!all 表示订阅全部合约。多次订阅会累加合约；重复合约或与 !all 重叠的订阅不会重复推送。整批参数校验通过后才修改订阅，非法合约会使整个请求失败。
+订阅成功只返回确认消息，不发送历史订单快照。订阅后的第一条消息可能是已有订单的更新。断线期间错过的事件不会补发。
+订阅错误：
+| 错误码 | 说明
+| 2 | 非法用户 ID、非法合约、非 UTA3.0 账户或不支持的 PB/SBE 编码。
+| 3 | 服务无法查询账户资格。
+| 4 | 未认证或认证失败。
+# 订单 V2 推送
+全部订单事件均使用 event: "update"，result 为订单对象数组。
+{ "channel": "futures.orders_v2", "event": "update", "time": 1628736848, "time_ms": 1628736848325, "result": [ { "contract": "BTC_USDT", "create_time": 1628736847, "create_time_ms": 1628736847325, "fill_price": "40000.4", "finish_as": "filled", "finish_time": 1628736848, "finish_time_ms": 1628736848321, "iceberg": "0", "id": 4872460, "id_string": "4872460", "is_close": false, "is_liq": false, "is_reduce_only": false, "is_voucher": false, "left": "0", "mkfr": -0.00025, "price": "40000.4", "size": "1.5", "status": "finished", "text": "api", "tif": "gtc", "user": "20011", "update_id": 1, "update_time_ms": 1628736848320, "biz_info": "-", "stp_act": "-", "stp_id": "0", "amend_text": "-", "bbo": "-", "pos_margin_mode": "cross", "leverage": "10", "stop_loss_price": "", "stop_profit_price": "", "market_order_slip_ratio": "0.03" } ] }
+size、left、iceberg、price、fill_price 始终为十进制字符串，保留小数数量；是否设置 X-Gate-Size-Decimal: 1 不影响本频道的这些字段类型。
+create_time_ms 来自 OMS。订单创建事件的 update_time_ms 为订单到达 ME 的时间，后续成交、改单和撤销事件则为 ME 更新订单的时间。“创建事件”不等于新订阅连接收到的第一条消息。后续事件的 update_time_ms - create_time_ms 包含订单存续时间，不能用来表示本次改单或撤销的 OMS→ME 延迟。
+外层 time 和 time_ms 分别为 WS 消息封装的秒和毫秒时间戳；finish_time 和 finish_time_ms 沿用上游事件日志时间。这些时间不能替代 ME 的 update_time_ms。缺少有效正整数 OMS/ME 毫秒时间的消息不会推送，服务不会用本地时间补齐。
+订单字段：
+| 字段 | 类型 | 描述
+| contract | String | 合约名称。
+| create_time | Integer | OMS 订单创建时间，单位为秒。
+| create_time_ms | Integer | OMS 订单创建时间，单位为毫秒。
+| fill_price | String | 订单成交价格，以十进制字符串表示。
+| finish_as | String | 创建事件为 _new，未结束订单的更新事件为 _update。结束事件返回原因，例如 filled（完全成交）、cancelled（撤销）、ioc、poc、fok 或 stp；其他原因与 futures.orders 一致。
+| finish_time | Integer | 上游订单事件日志时间，单位为秒，不表示清算完成时间。
+| finish_time_ms | Integer | 上游订单事件日志时间，单位为毫秒，不表示 ME 更新时间。
+| iceberg | String | 冰山订单显示数量，以十进制字符串表示；普通订单为 "0"。
+| id | Integer | 订单 ID；客户端无法精确保留大整数时请使用 id_string。
+| id_string | String | 字符串形式的订单 ID。
+| is_close | Boolean | 是否为平仓订单。
+| is_liq | Boolean | 本频道始终为 false，不推送清算订单。
+| is_reduce_only | Boolean | 是否为只减仓订单。
+| is_voucher | Boolean | 是否为体验金订单。
+| left | String | 订单剩余数量，以十进制字符串表示。
+| mkfr | Float | Maker 费率，不表示清算后的手续费金额。
+| price | String | 订单价格，以十进制字符串表示；市价订单为 "0"。
+| size | String | 订单数量，以十进制字符串表示；正数为买入，负数为卖出。
+| status | String | 订单状态：open（等待交易）或 finished（已结束）。
+| text | String | 用户定义的订单信息。
+| tif | String | 订单有效期：gtc（成交前持续有效）、ioc（立即成交，否则取消）、poc（只挂单）或 fok（立即全部成交，否则取消）。
+| user | String | 用户 ID。
+| update_id | Integer | 订单更新 ID。
+| update_time_ms | Integer | ME 毫秒时间戳。创建事件为订单到达 ME 的时间；成交、改单或撤销事件为 ME 更新订单的时间。
+| biz_info | String | 本次订单更新附带的业务信息。
+| stp_act | String | 自成交防护策略：cn（取消最新订单）、co（取消最旧订单）、cb（全部取消）；未设置为 -。
+| stp_id | String | 自成交防护组 ID；未设置为 "0"。
+| amend_text | String | 用户改单时附带的自定义信息。
+| bbo | String | BBO 下单选项；未设置为 -。
+| pos_margin_mode | String | 仓位保证金模式：cross（全仓）或 isolated（逐仓）。
+| leverage | String | 杠杆倍数；上游未提供时为空字符串。
+| stop_loss_price | String | 止损价格；未设置时为空字符串。
+| stop_profit_price | String | 止盈价格；未设置时为空字符串。
+| market_order_slip_ratio | String | 市价单预设最大滑点比例；"0.03" 表示 3%，不代表实际滑点。
+# 订单 V2 取消订阅
+使用 event: "unsubscribe"，参数规则与订阅一致。payload: ["!all"] 清空当前连接对 futures.orders_v2 的全部订阅。取消订阅不重新查询 UTA3.0 资格。
+当前连接已订阅的合约即使下架，也仍可取消订阅；若请求中包含当前连接未订阅的未知合约，则整批请求失败，原有订阅保持不变。
+{ "time": 1628736849, "channel": "futures.orders_v2", "event": "unsubscribe", "payload": [ "!all" ], "auth": { "method": "api_key", "KEY": "xxxx", "SIGN": "xxxx" } }
+{ "time": 1628736849, "time_ms": 1628736849123, "channel": "futures.orders_v2", "event": "unsubscribe", "result": { "status": "success" } }
 # 用户私有成交频道
 提供接收用户交易的方式
@@ -2242,3 +2328,3 @@ req_param` API 订单模型的 JSON 字节数据:
 | »»label | String | 错误类型
 | »»message | String | 详细错误信息
-Last Updated: 10/14/2026, 7:46:30 AM
+Last Updated: 10/22/2026, 7:54:06 AM

```
