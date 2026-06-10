<!-- has_changes=true date=2026-06-10 -->
# Exchange API Changelog Diff

Generated: 2026-06-10 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 24 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (87006 bytes)

- [OK] OKX V5 (`okx`): no change (199437 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 22 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (32707 bytes)

- [CHANGED] **Gate.io Spot WebSocket v4** (`gate-spot-ws`): 80 diff lines

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (138977 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index 57208e0..b8ac318 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -5,9 +5,17 @@
 ### 2026-06-09
 
+**Update:**
+
+The `serverShutdown` event will be sent when the **server is about to be shut down**; when you receive this event, please disconnect and open a new connection.
+
+All mention of a fixed time before the server shuts down has been removed from the documentation.
+
 * Documented the `serverShutdown` event in [SBE Market Data Streams](./sbe-market-data-streams.md#serverShutdown).
-  * `serverShutdown` event will be sent 10 minutes before disconnection.
-  * Please establish a new connection as soon as possible to prevent interruption.
+  * ~~`serverShutdown` event will be sent 10 minutes before disconnection.~~
+  * Please establish a new connection as soon as possible to prevent connection interruption.
   * Note that you will receive `serverShutdown` events in JSON in WebSocket text frames.
 
+* Updated the [Price Range Execution Rule FAQ](./faqs/price_range_execution_rules.md#external-reference-price-calculation-method-1) with new External Reference Price Calculation Methods.
+
 ---
 

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 941ee0b..132d898 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,3 +1,3 @@
-2026-06-11​
+2026-06-15​
 REST API​
 RWA (Real World Assets) — New Endpoints
@@ -7,4 +7,12 @@ RWA (Real World Assets) — New Endpoints
 - Get Order List [NEW]
 - Get NAV Chart [NEW]
+2026-06-10​
+REST API​
+- Withdraw [UPDATE]
+  - Added a new optional request parameter questionnaire, which can be used as a replacement for beneficiary. We recommend integrating this field as soon as possible.
+- Questionnaire [NEW]
+  - It is a questionnaire page that serves as a reference for deposit and withdrawal transactions to meet Travel Rule compliance requirements.
+- Submit Deposit Originator Info [NEW]
+  - A new endpoint has been introduced to submit the originator's compliance information when a deposit is flagged for Travel Rule review.
 2026-06-09​
 REST API​

```

### Gate.io Spot WebSocket v4 (`gate-spot-ws`)
- Source: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/

```diff
diff --git a/changelogs/gate-spot-ws.txt b/changelogs/gate-spot-ws.txt
index dff8154..4ee02b6 100644
--- a/changelogs/gate-spot-ws.txt
+++ b/changelogs/gate-spot-ws.txt
@@ -11,8 +11,13 @@ Websocket 链接地址：
 - 线上交易: wss://api.gateio.ws/ws/v4/
 - 模拟盘交易: wss://ws-testnet.gate.com/v4/ws/spot
+- 模拟盘 SBE: wss://ws-testnet.gate.com/v4/ws/spot/sbe
+TIP
+建议使用 SBE 以获取更快的行情和更小的带宽成本，具体使用查看 SBE 数据推送 章节。
 # SDK
 我们提供了 WebSocket SDK 来帮助开发者进行业务复用。
 SDK 的源代码 在 gatews (opens new window) GitHub 仓库。
 # 变更历史
+2026-06-09
+- 模拟盘新增 SBE（Simple Binary Encoding）二进制行情推送支持，具体使用查看 SBE 数据推送 章节。
 2026-03-31
 - spot.obu 模拟盘新增立即的首次快照推送，该次快照推送将会在订阅请求的响应之前推送。此行为与之前快照在订阅请求的响应之后推送不同，请注意该行为变更。
@@ -134,4 +139,56 @@ WebSocket 认证使用与 Gate APIv4 API 相同的签名计算方法，即: HexE
 - 身份验证信息在 auth 字段的请求主体中发送。
 您可以登录到控制台查看 Gate APIv4 密钥和秘密.
+# SBE 数据推送
+# 对接SBE
+- 使用地址，在现有的地址后添加 /sbe：
+  - testnet: wss://ws-testnet.gate.com/v4/ws/spot/sbe
+- schema 地址：
+  - testnet: gate_spot_ws_latest.xml (opens new window)
+- 如果需要指定 sbe_schema_id，则通过 query 的形式传入 sbe_schema_id 参数，例如：wss://ws-testnet.gate.com/v4/ws/spot/sbe?sbe_schema_id=1
+  - 目前支持的 sbe_schema_id 为 0 和 1；sbe_schema_id 为 0 用于客户端测试 sbe schema 不兼容升级的逻辑
+  - 不传入 sbe_schema_id 则默认使用最新的 schema 版本（当前为 1）
+  - 传入不合法的 sbe_schema_id 在连接之后会返回系统通知，并将 sbe_schema_id 调整为最新的 schema 版本
+  - 传入旧版本的 sbe_schema_id 在连接之后会返回系统通知，提醒更新新版本的 SBE schema，依旧使用客户端指定的旧版本 schema
+无效的 sbe_schema_id 的系统通知
+{ "time": 1770600979, "time_ms": 1770600979609, "channel": "spot.system", "event": "update", "result": { "type": "invalid_sbe_schema_id", "msg": "Your sbe_schema_id '011' does not exist, it has been adjusted to the default sbe_schema_id '1'." } }
+过时的 sbe_schema_id 的系统通知
+{ "time": 1770601096, "time_ms": 1770601096665, "channel": "spot.system", "event": "update", "result": { "type": "outdated_sbe_schema_id", "msg": "Your sbe_schema_id '0' is outdated, please upgrade to the latest version '1'." } }
+# SBE使用说明
+- 使用 JSON 进行请求和首次响应；使用 SBE 作为数据推送；
+- 同一条连接上同时存在 JSON 和 SBE 的消息，请使用 opcode 来区分数据：opcode 为 1 代表 JSON，opcode 为 2 代表 SBE。
+- SBE 的解码：
+  - MessageHeader：每条 SBE 二进制帧均为「MessageHeader + 消息体」。Header 为固定 8 字节（小端序，uint16 依次为 blockLength、templateId、schemaId、version），解码时必须先读 Header，再根据 schemaId 和 templateId 选择对应 Schema 与消息类型解码消息体。
+  - 解码流程建议：
+    - 读取 MessageHeader（固定 8 字节），得到 blockLength、templateId、schemaId、version。
+    - 根据 schemaId 选择解码器：0 → 使用旧版本（decimal 字段为字符串编码）进行解码；1 → 使用新版本（decimal 字段为 mantissa(int64) × 10^exponent(int8) 定点编码）进行解码。
+    - 根据 templateId 确定具体消息类型（如 publicTrade、orderBook、bbo 等），再按该 Schema 的布局解码消息体。
+- 使用 SBE 时，仅可订阅以下频道，其余频道不支持 SBE 推送。后续将扩展到其余频道。
+  - 订阅不支持 SBE 的频道时，将返回订阅失败的消息
+| 通道名 | templateId | 消息类型 | 说明
+| spot.tickers | 7 | ticker | 行情
+| spot.trades | 2 | publicTrade | 公共成交
+| spot.candlesticks | 6 | candlestick | K 线
+| spot.order_book | 4 | orderBook | 订单簿（全量深度）
+| spot.order_book_update | 5 | orderBookUpdate | 订单簿增量更新
+| spot.book_ticker | 1 | bbo | 最优买卖价（BBO）
+| spot.obu | 3 | obu | 订单簿增量（OBU）
+| spot.usertrades | 8 | userTrade | 用户成交
+| spot.orders | 9 | orders | 订单
+| spot.balances | 10 | balance | 现货余额
+| spot.margin_balances | 11 | marginBalance | 杠杆余额
+| spot.funding_balances | 12 | fundingBalance | 理财余额
+| spot.cross_balances | 13 | crossBalance | 全仓杠杆余额
+| spot.cross_loan | 14 | crossLoan | 全仓借贷
+| spot.priceorders | 15 | priceOrder | 价格条件单
+- 上表 templateId 以对应版本的 schema XML 为准。
+- 上述频道的 v2 版本（如 spot.trades_v2、spot.orders_v2、spot.usertrades_v2）复用相同的消息模板，同样支持 SBE 推送。
+订阅受支持的频道（以 spot.order_book 为例）。请求与首次响应均为 JSON，订阅成功后该频道数据以 SBE 二进制帧推送。
+客户端请求
+{ "time": 1770603400, "id": 123456789, "channel": "spot.order_book", "event": "subscribe", "payload": ["BTC_USDT", "5", "100ms"] }
+服务端响应（订阅的 JSON 确认）
+{ "time": 1770603400, "time_ms": 1770603400123, "channel": "spot.order_book", "event": "subscribe", "error": null, "result": { "status": "success" } }
+订阅成功后，该频道的订单簿数据将以 SBE 二进制帧（opcode 2）推送，使用 templateId 4（orderBook）解码。
+订阅不支持 SBE 的频道时将返回订阅失败：
+{ "time": 1770603321, "time_ms": 1770603321767, "conn_id": "57a8765578ea837e", "trace_id": "3c75ba05569b3b292a2f36cfdd90d868", "channel": "spot.system", "event": "subscribe", "payload": [ "20011" ], "error": { "code": 2, "message": "channel spot.system does not support SBE" }, "result": { "status": "fail" } }
 # System API
 系统 API 用于检索服务元信息，不用于订阅。
@@ -1477,3 +1534,3 @@ account: 指定查询账户。不指定默认现货，保证金和逐仓杠杆
 | »»label | String | 以字符串格式表示错误类型
 | »»message | String | 错误信息详情
-Last Updated: 4/27/2026, 10:15:14 AM
+Last Updated: 6/10/2026, 4:02:40 AM

```
