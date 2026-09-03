<!-- has_changes=true date=2026-09-03 -->
# Exchange API Changelog Diff

Generated: 2026-09-03 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (131990 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 47 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [OK] Bybit V5 (`bybit`): no change (94713 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42000 bytes)

- [CHANGED] **Gate.io Spot WebSocket v4** (`gate-spot-ws`): 252 diff lines

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 551adc3..739627c 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,3 +1,42 @@
 待发布内容
+欧易将进行 USD 现货交易对迁移
+最后更新：2026 年 9 月 2 日
+OKX 将合并 USD 与 USDC 现货深度。作为本次调整的一部分，受影响的 Crypto-USD 现货产品将下线，用户需迁移至对应的 Crypto-USDC 产品。本次调整属于不兼容变更。更多详情，请根据所在地区参阅对应公告： USD 现货交易对迁移或 USDⓢ 现货交易对迁移，请以所在地区可访问的公告为准。
+USDC 交易对开放及并行期
+自 2026 年 9 月 23 日下午 4:00（UTC+8） 起，OKX 将开放相关 Crypto-USDC 现货产品。自开放起至 2026 年 9 月 30 日下午 4:00（UTC+8） 相关 Crypto-USD 现货产品下线前，部分 Crypto-USD 产品及其对应的 Crypto-USDC 产品将同时开放交易。
+API 用户可在并行期内提前迁移至对应的 Crypto-USDC 产品 ID，适配 tradeQuoteCcy 的传参逻辑，并验证请求、返回及 WebSocket 订阅逻辑。
+不兼容变更
+- 当前请求中使用 Crypto-USD 产品 ID 的用户，需在变更上线后改用对应的 Crypto-USDC 产品 ID。在开始交易 Crypto-USDC 产品前，请先调用 POST /api/v5/account/activate-feature 接口开通 USDC 交易功能。已经在交易 USDC 产品的账户不受影响。
+- 影响范围包括请求参数中包含 instId 或 instIdCode 的 REST API 和 WebSocket 频道，包括交易、订单查询、账户查询、策略交易、大宗交易、价差交易、行情请求及 WebSocket 订阅。
+- Crypto-USD 产品 ID 不会映射为 Crypto-USDC 产品 ID。变更上线后，继续使用已下线的 Crypto-USD instId 或 instIdCode 发起请求或订阅，可能会失败或返回空数据。
+- 返回参数将使用实际的 Crypto-USDC 产品 ID 或产品 ID Code。请在上线前更新请求构造、返回解析、订阅管理、产品缓存，以及所有依赖 instId 或 instIdCode 的业务逻辑。
+重要：迁移下单时需正确传入 tradeQuoteCcy
+tradeQuoteCcy 的默认值为 instId 中的计价币种。因此，如果仅将 instId 从 Crypto-USD 改为 Crypto-USDC，默认交易计价币种也会从 USD 变为 USDC。
+如果您当前交易 Crypto-USD 产品时未传入 tradeQuoteCcy，迁移至对应的 Crypto-USDC 产品后仍希望使用 USD 交易，则必须显式传入 tradeQuoteCcy=USD。
+| 场景 | 变更前 | 变更后
+| 继续使用 USD 交易 | "instId": "Crypto-USD"
+未传 tradeQuoteCcy | "instId": "Crypto-USDC"
+"tradeQuoteCcy": "USD"
+| 使用 USDC 交易 | "instId": "Crypto-USD"
+"tradeQuoteCcy": "USDC" | "instId": "Crypto-USDC"
+"tradeQuoteCcy": "USDC"；如果希望使用默认值 USDC，也可不传 tradeQuoteCcy
+下单前，请通过 获取交易产品基础信息（私有） 接口获取 tradeQuoteCcyList。传入的 tradeQuoteCcy 必须是当前产品及账户对应的 tradeQuoteCcyList 枚举值。
+该迁移规则也适用于其他使用相关请求参数计算可交易数量或提交现货订单的接口，包括 获取最大可用余额/保证金、获取最大可下单数量 及 获取交易产品最大可借。
+新增接口：开通 USDC 交易功能
+在开始交易 Crypto-USDC 产品前，请先调用以下接口为账户开通 USDC 交易功能。已经在交易 USDC 产品的账户不受影响。
+限速：5 次/2 秒
+限速规则：User ID
+HTTP 请求
+POST /api/v5/account/activate-feature
+请求示例
+POST /api/v5/account/activate-feature body { "feature": "1" }
+请求参数
+| 参数名 | 类型 | 是否必须 | 描述
+| feature | String | 是 | 要开通的具体功能
+1：USDC 订单簿交易功能。在开始交易 Crypto-USDC 产品前需先开通该功能。已经在交易 USDC 产品的账户不受影响。母账户与子账户之间不共享开通状态，每个母账户和子账户均需分别调用，且各自仅需调用一次。
+返回结果
+{ "code": "0", "msg": "", "data": [] }
+返回参数
+无
 信号复制新增 API 接口
 最后更新：2026 年 5 月 14 日

```

### Gate.io Spot WebSocket v4 (`gate-spot-ws`)
- Source: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/

```diff
diff --git a/changelogs/gate-spot-ws.txt b/changelogs/gate-spot-ws.txt
index bd649bf..aff8da4 100644
--- a/changelogs/gate-spot-ws.txt
+++ b/changelogs/gate-spot-ws.txt
@@ -19,4 +19,11 @@ TIP
 SDK 的源代码 在 gatews (opens new window) GitHub 仓库。
 # 变更历史
+2026-08-31
+- spot.order_place 单笔和批量下单新增 trade_quote；RESULT 和 FULL 结果在下游返回实际计价资产时输出该字段。
+- spot.order_cancel_cp 新增 trade_quote，用于仅撤销使用指定实际计价资产的订单。
+- 成交、用户成交和订单推送新增统一订单簿字段 stock、money 和 trade_mode。
+- 本期仅启用计价侧统一交易（trade_mode=1）；。
+- 订单 finish_as 新增 unified_check_failed。
+- SBE Schema 2 在 publicTrade、userTrade 和 orders 模板中新增统一订单簿字段。
 2026-06-09
 - 模拟盘新增 SBE（Simple Binary Encoding）二进制行情推送支持，具体使用查看 SBE 数据推送 章节。
@@ -145,16 +152,14 @@ WebSocket 认证使用与 Gate APIv4 API 相同的签名计算方法，即: HexE
   - 线上交易: wss://api.gateio.ws/ws/v4/ws/spot/sbe
   - testnet: wss://ws-testnet.gate.com/v4/ws/spot/sbe
-- schema 地址：
+- Schema 1 XML 文件：
   - testnet: gate_spot_ws_latest.xml (opens new window)
   - 线上交易: gate_spot_ws_latest.xml (opens new window)
-- 如果需要指定 sbe_schema_id，则通过 query 的形式传入 sbe_schema_id 参数，例如：wss://ws-testnet.gate.com/v4/ws/spot/sbe?sbe_schema_id=1
-  - 目前支持的 sbe_schema_id 为 0 和 1；sbe_schema_id 为 0 用于客户端测试 sbe schema 不兼容升级的逻辑
-  - 不传入 sbe_schema_id 则默认使用最新的 schema 版本（当前为 1）
-  - 传入不合法的 sbe_schema_id 在连接之后会返回系统通知，并将 sbe_schema_id 调整为最新的 schema 版本
-  - 传入旧版本的 sbe_schema_id 在连接之后会返回系统通知，提醒更新新版本的 SBE schema，依旧使用客户端指定的旧版本 schema
-无效的 sbe_schema_id 的系统通知
-{ "time": 1770600979, "time_ms": 1770600979609, "channel": "spot.system", "event": "update", "result": { "type": "invalid_sbe_schema_id", "msg": "Your sbe_schema_id '011' does not exist, it has been adjusted to the default sbe_schema_id '1'." } }
-过时的 sbe_schema_id 的系统通知
-{ "time": 1770601096, "time_ms": 1770601096665, "channel": "spot.system", "event": "update", "result": { "type": "outdated_sbe_schema_id", "msg": "Your sbe_schema_id '0' is outdated, please upgrade to the latest version '1'." } }
+- 上述两个公开 XML 文件当前均为 schemaId=1，不能用于解码请求 sbe_schema_id=2 后收到的消息。
+- Schema 2 将以独立文件 gate_spot_ws_v2.0.0.xml 对外发布。在对应公开目录提供该 XML 文件之前，客户端必须继续使用 Schema 1，不得请求 sbe_schema_id=2。
+- Schema 2 XML 文件公开后，可通过 query 参数指定 sbe_schema_id，例如：wss://ws-testnet.gate.com/v4/ws/spot/sbe?sbe_schema_id=2
+  - 目前支持的 sbe_schema_id 为 0、1 和 2；sbe_schema_id 为 0 用于客户端测试 sbe schema 不兼容升级的逻辑
+  - 不传入 sbe_schema_id 时默认使用 Schema 1；需要接收统一订单簿字段时必须显式指定 sbe_schema_id=2
+  - publicTrade、userTrade 和 orders 模板中的统一订单簿字段（stock、money 和 trade_mode）需要使用 sbe_schema_id=2。Schema 0 和 1 保持原有布局。
+  - 不支持的 sbe_schema_id 会回退到默认 Schema 1；仍受支持的旧版本继续使用客户端指定的布局
 # SBE使用说明
 - 使用 JSON 进行请求和首次响应；使用 SBE 作为数据推送；
@@ -164,5 +169,5 @@ WebSocket 认证使用与 Gate APIv4 API 相同的签名计算方法，即: HexE
   - 解码流程建议：
     - 读取 MessageHeader（固定 8 字节），得到 blockLength、templateId、schemaId、version。
-    - 根据 schemaId 选择解码器：0 → 使用旧版本（decimal 字段为字符串编码）进行解码；1 → 使用新版本（decimal 字段为 mantissa(int64) × 10^exponent(int8) 定点编码）进行解码。
+    - 根据 schemaId 选择解码器：0 → 使用字符串 decimal 的旧布局；1 → 使用定点 decimal 布局；2 → 使用增加统一订单簿字段的定点布局。不能用其他 schema 的布局解码当前帧。
     - 根据 templateId 确定具体消息类型（如 publicTrade、orderBook、bbo 等），再按该 Schema 的布局解码消息体。
 - 使用 SBE 时，仅可订阅以下频道，其余频道不支持 SBE 推送。后续将扩展到其余频道。
@@ -171,4 +176,5 @@ WebSocket 认证使用与 Gate APIv4 API 相同的签名计算方法，即: HexE
 | spot.tickers | 7 | ticker | 行情
 | spot.trades | 2 | publicTrade | 公共成交
+| spot.f_trades | 2 | publicTrade | 过滤公共成交
 | spot.candlesticks | 6 | candlestick | K 线
 | spot.order_book | 4 | orderBook | 订单簿（全量深度）
@@ -186,4 +192,14 @@ WebSocket 认证使用与 Gate APIv4 API 相同的签名计算方法，即: HexE
 - 上表 templateId 以对应版本的 schema XML 为准。
 - 上述频道的 v2 版本（如 spot.trades_v2、spot.orders_v2、spot.usertrades_v2）复用相同的消息模板，同样支持 SBE 推送。
+SBE Schema 2 的统一订单簿新增字段：
+| 模板 | 作用域 | SBE 字段 | ID | JSON 字段 | 说明
+| publicTrade (templateId 2) | 消息 | tradeMode | 12 | trade_mode | 交易模式
+| publicTrade (templateId 2) | 消息 | stock / money | 203 / 204 | stock / money | 实际基础/计价资产
+| userTrade (templateId 8) | trades 分组 | tradeMode | 13 | trade_mode | 交易模式
+| userTrade (templateId 8) | trades 分组 | stock / money | 206 / 207 | stock / money | 实际基础/计价资产
+| orders (templateId 9) | result 分组 | tradeMode | 28 | trade_mode | 交易模式
+| orders (templateId 9) | result 分组 | stock / money | 213 / 214 | stock / money | 实际基础/计价资产
+orders 模板在旧 Schema 中已经包含 finishAs（Schema 1 和 2 中均为 id=210）。unified_check_failed 只是新增字符串取值，不要求使用 Schema 2。
+spot.usertrades_v2 的 JSON 推送仍不包含 fee、fee_currency、point_fee 和 gt_fee。为保持二进制兼容，共用的 SBE userTrade 模板会保留固定手续费字段；该频道中这些字段解码为 0 或空字符串。
 订阅受支持的频道（以 spot.order_book 为例）。请求与首次响应均为 JSON，订阅成功后该频道数据以 SBE 二进制帧推送。
 客户端请求
@@ -270,5 +286,5 @@ TIP
 # 服务端推送
 通知示例：
-{ "time": 1606292218, "channel": "spot.trades", "event": "update", "result": { "id": 309143071, "create_time": 1606292218, "create_time_ms": "1606292218213.4578", "side": "sell", "currency_pair": "GT_USDT", "amount": "16.4700000000", "price": "0.4705000000", "range": "2390902-2390902", "id_market": 917144 } }
+{ "time": 1606292218, "channel": "spot.trades", "event": "update", "result": { "id": 309143071, "create_time": 1606292218, "create_time_ms": "1606292218213.4578", "side": "sell", "currency_pair": "BTC_USD", "amount": "16.4700000000", "price": "0.4705000000", "range": "2390902-2390902", "id_market": 917144, "stock": "BTC", "money": "USDC", "trade_mode": 1 } }
 请注意，公共交易频道只通知交易中的吃单方。下面的私有用户交易频道将通知所有与用户相关的交易。
 通知结果格式：
@@ -284,4 +300,8 @@ TIP
 | » range | String | 成交范围(格式: "开始 ID-结束 ID")
 | » id_market | Integer | 按市场成交ID
+| » stock | String | 该笔成交实际使用的基础资产
+| » money | String | 该笔成交实际使用的计价资产
+| » trade_mode | Integer | 交易模式：0 普通市场、1 计价侧统一、2 基础侧统一、3 两侧统一
+在统一订单簿中，currency_pair 仍为订阅的名义市场（例如 BTC_USD），stock 和 money 表示该笔成交实际使用的资产。
 # 字段数据枚举
 | Property | Value
@@ -306,5 +326,5 @@ TIP
 # 服务端推送
 通知示例：
-{ "time": 1606292218, "channel": "spot.trades_v2", "event": "update", "result": { "id": 309143071, "create_time": 1606292218, "create_time_ms": "1606292218213.4578", "side": "sell", "currency_pair": "GT_USDT", "amount": "16.4700000000", "price": "0.4705000000", "range": "2390902-2390902", "id_market": 917144 } }
+{ "time": 1606292218, "channel": "spot.trades_v2", "event": "update", "result": { "id": 309143071, "create_time": 1606292218, "create_time_ms": "1606292218213.4578", "side": "sell", "currency_pair": "BTC_USD", "amount": "16.4700000000", "price": "0.4705000000", "range": "2390902-2390902", "id_market": 917144, "stock": "BTC", "money": "USDC", "trade_mode": 1 } }
 请注意，公共交易频道只通知交易中的吃单方。下面的私有用户交易频道将通知所有与用户相关的交易。
 通知结果格式：
@@ -320,4 +340,8 @@ TIP
 | » range | String | 成交范围(格式: "开始 ID-结束 ID")
 | » id_market | Integer | 按市场成交ID
+| » stock | String | 该笔成交实际使用的基础资产
+| » money | String | 该笔成交实际使用的计价资产
+| » trade_mode | Integer | 交易模式：0 普通市场、1 计价侧统一、2 基础侧统一、3 两侧统一
+在统一订单簿中，currency_pair 仍为订阅的名义市场，stock 和 money 表示该笔成交实际使用的资产。
 # 字段数据枚举
 | Property | Value
@@ -579,6 +603,7 @@ WARNING
 # 服务端推送
 通知示例：
-{ "time": 1694655225, "time_ms": 1694655225315, "channel": "spot.orders", "event": "update", "result": [ { "id": "399123456", "text": "t-testtext", "create_time": "1694655225", "update_time": "1694655225", "currency_pair": "BTC_USDT", "type": "limit", "account": "spot", "side": "sell", "amount": "0.0001", "price": "26253.3", "time_in_force": "gtc", "left": "0.0001", "filled_total": "0", "filled_amount": "812.8", "avg_deal_price": "0", "fee": "0", "fee_currency": "USDT", "point_fee": "0", "gt_fee": "0", "rebated_fee": "0", "rebated_fee_currency": "USDT", "create_time_ms": "1694655225315", "update_time_ms": "1694655225315", "user": 3497082, "event": "put", "stp_id": 0, "stp_act": "-", "finish_as": "open", "biz_info": "-", "amend_text": "-", "slippage": "0.05" } ] }
+{ "time": 1694655225, "time_ms": 1694655225315, "channel": "spot.orders", "event": "update", "result": [ { "id": "399123456", "text": "t-testtext", "create_time": "1694655225", "update_time": "1694655225", "currency_pair": "BTC_USD", "stock": "BTC", "money": "USDC", "trade_mode": 1, "type": "limit", "account": "spot", "side": "sell", "amount": "0.0001", "price": "26253.3", "time_in_force": "gtc", "left": "0.0001", "filled_total": "0", "filled_amount": "812.8", "avg_deal_price": "0", "fee": "0", "fee_currency": "USDC", "point_fee": "0", "gt_fee": "0", "rebated_fee": "0", "rebated_fee_currency": "USDC", "create_time_ms": "1694655225315", "update_time_ms": "1694655225315", "user": 3497082, "event": "put", "stp_id": 0, "stp_act": "-", "finish_as": "open", "biz_info": "-", "amend_text": "-", "slippage": "0.05" } ] }
 更新的订单列表。请注意，可能会在一条通知中更新多个货币对的订单。
+在统一订单簿中，currency_pair 仍为名义市场，stock 和 money 表示订单实际使用的资产。
 通知结果格式：
 | 字段 | 类型 | 描述
@@ -596,4 +621,7 @@ WARNING
  - finish: 订单关闭或者取消
 | » currency_pair | String | 交易货币对
+| » stock | String | 订单实际使用的基础资产
+| » money | String | 订单实际使用的计价资产
+| » trade_mode | Integer | 交易模式：0 普通市场、1 计价侧统一、2 基础侧统一、3 两侧统一
 | » type | String | 订单类型
 | » account | String | 账户类型. spot - 现货账户; margin - 杠杆账户; cross_margin - 全仓杠杆账户; unified - 统一账户
@@ -634,4 +662,5 @@ WARNING
 - small：订单数量太小
 - liquidate_cancelled：爆仓取消
+- unified_check_failed：统一市场校验失败，例如实际交易资产不受支持，或市场/币种处于暂停状态
 - -：未知
 | »amend_text | String | 用户在修改订单时添加的自定义数据。
@@ -675,6 +704,7 @@ WARNING
 # 服务端推送
 通知示例：
-{ "time": 1736238443, "time_ms": 1736238443516, "channel": "spot.orders_v2", "event": "update", "result": [ { "id": "769689142776", "text": "t-poc1736238443494", "create_time": "1736238443", "update_time": "1736238443", "currency_pair": "OM_USDT", "type": "limit", "account": "spot", "side": "buy", "amount": "0.78", "price": "3.9147", "time_in_force": "poc", "left": "0", "filled_total": "3.053466", "filled_amount": "812.8", "avg_deal_price": "3.9147", "fee_currency": "OM", "gt_discount": true, "rebated_fee_currency": "OM", "create_time_ms": "1736238443503", "update_time_ms": "1736238443506", "user": 3128780, "event": "finish", "stp_id": 0, "stp_act": "-", "finish_as": "filled", "biz_info": "-", "amend_text": "-", "slippage": "0.05" } ] }
+{ "time": 1736238443, "time_ms": 1736238443516, "channel": "spot.orders_v2", "event": "update", "result": [ { "id": "769689142776", "text": "t-poc1736238443494", "create_time": "1736238443", "update_time": "1736238443", "currency_pair": "BTC_USD", "stock": "BTC", "money": "USDC", "trade_mode": 1, "type": "limit", "account": "spot", "side": "buy", "amount": "0.78", "price": "3.9147", "time_in_force": "poc", "left": "0", "filled_total": "3.053466", "filled_amount": "812.8", "avg_deal_price": "3.9147", "fee_currency": "USDC", "gt_discount": true, "rebated_fee_currency": "USDC", "create_time_ms": "1736238443503", "update_time_ms": "1736238443506", "user": 3128780, "event": "finish", "stp_id": 0, "stp_act": "-", "finish_as": "filled", "biz_info": "-", "amend_text": "-", "slippage": "0.05" } ] }
 更新的订单列表。请注意，可能会在一条通知中更新多个货币对的订单。
+在统一订单簿中，currency_pair 仍为名义市场，stock 和 money 表示订单实际使用的资产。
 通知结果格式：
 | 字段 | 类型 | 描述
@@ -692,4 +722,7 @@ WARNING
  - finish: 订单关闭或者取消
 | » currency_pair | String | 交易货币对
+| » stock | String | 订单实际使用的基础资产
+| » money | String | 订单实际使用的计价资产
+| » trade_mode | Integer | 交易模式：0 普通市场、1 计价侧统一、2 基础侧统一、3 两侧统一
 | » type | String | 订单类型
 | » account | String | 账户类型. spot - 现货账户; margin - 杠杆账户; cross_margin - 全仓杠杆账户; unified - 统一账户
@@ -726,4 +759,5 @@ WARNING
 - small：订单数量太小
 - liquidate_cancelled：爆仓取消
+- unified_check_failed：统一市场校验失败，例如实际交易资产不受支持，或市场/币种处于暂停状态
 - -：未知
 | »amend_text | String | 用户在修改订单时添加的自定义数据。
@@ -766,6 +800,7 @@ WARNING
 # 服务端推送
 通知示例：
-{ "time": 1605176741, "channel": "spot.usertrades", "event": "update", "result": [ { "id": 5736713, "user_id": 1000001, "order_id": "30784428", "currency_pair": "BTC_USDT", "create_time": 1605176741, "create_time_ms": "1605176741123.456", "side": "sell", "amount": "1.00000000", "role": "taker", "price": "10000.00000000", "fee": "0.00200000000000", "point_fee": "0", "gt_fee": "0", "text": "apiv4", "id_market": 917144 } ] }
+{ "time": 1605176741, "channel": "spot.usertrades", "event": "update", "result": [ { "id": 5736713, "user_id": 1000001, "order_id": "30784428", "currency_pair": "BTC_USD", "create_time": 1605176741, "create_time_ms": "1605176741123.456", "side": "sell", "amount": "1.00000000", "role": "taker", "price": "10000.00000000", "fee": "0.00200000000000", "point_fee": "0", "gt_fee": "0", "text": "apiv4", "id_market": 917144, "stock": "BTC", "money": "USDC", "trade_mode": 1 } ] }
 更新的用户交易列表。
+在统一订单簿中，currency_pair 仍为名义市场，stock 和 money 表示该笔成交实际使用的资产。
 通知结果格式：
 | 字段 | 类型 | 描述
@@ -787,4 +822,7 @@ WARNING
 | » text | String | 用户自定义信息
 | » id_market | Integer | 按市场成交ID
+| » stock | String | 该笔成交实际使用的基础资产
+| » money | String | 该笔成交实际使用的计价资产
+| » trade_mode | Integer | 交易模式：0 普通市场、1 计价侧统一、2 基础侧统一、3 两侧统一
 # 字段枚举值
 | Property | Value
@@ -812,6 +850,7 @@ WARNING
 # 服务端推送
 通知示例：
-{ "time": 1736237480, "time_ms": 1736237480397, "channel": "spot.usertrades_v2", "event": "update", "result": [ { "id": 12855056637, "user_id": 3128780, "order_id": "769683030088", "currency_pair": "PENGU_USDT", "create_time": 1736237480, "create_time_ms": "1736237480369.211", "side": "sell", "amount": "32462.7", "role": "maker", "price": "0.041828", "text": "t-poc1736237480359", "amend_text": "-", "biz_info": "-", "id_market": 917144 } ] }
+{ "time": 1736237480, "time_ms": 1736237480397, "channel": "spot.usertrades_v2", "event": "update", "result": [ { "id": 12855056637, "user_id": 3128780, "order_id": "769683030088", "currency_pair": "BTC_USD", "create_time": 1736237480, "create_time_ms": "1736237480369.211", "side": "sell", "amount": "32462.7", "role": "maker", "price": "0.041828", "text": "t-poc1736237480359", "amend_text": "-", "biz_info": "-", "id_market": 917144, "stock": "BTC", "money": "USDC", "trade_mode": 1 } ] }
 更新的用户交易列表。
+在统一订单簿中，currency_pair 仍为名义市场，stock 和 money 表示该笔成交实际使用的资产。该轻量频道仍不包含 fee、fee_currency、point_fee 和 gt_fee。
 通知结果格式：
 | 字段 | 类型 | 描述
@@ -830,4 +869,7 @@ WARNING
 | » biz_info | String | 交易价
 | » id_market | Integer | 按市场成交ID
+| » stock | String | 该笔成交实际使用的基础资产
+| » money | String | 该笔成交实际使用的计价资产
+| » trade_mode | Integer | 交易模式：0 普通市场、1 计价侧统一、2 基础侧统一、3 两侧统一
 # 字段枚举值
 | Property | Value
@@ -1067,5 +1109,5 @@ package main import ( "crypto/hmac" "crypto/sha512" "crypto/tls" "encoding/hex"
 # Websocket API 服务端推送
 服务端 ack 推送示例
-{ "request_id": "request-2", "ack": true, "header": { "response_time": "1681985856667", "status": "200", "channel": "spot.order_place", "event": "api", "client_id": "::1-0x140033dc0c0", "x_in_time": 1681985856667508, "x_out_time": 1681985856667598, "conn_id": "5e74253e9c793974", "conn_trace_id": "1bde5aaa0acf2f5f48edfd4392e1fa68", "trace_id": "e410abb5f74b4afc519e67920548838d", "x_gate_ratelimit_requests_remain": 9, "x_gate_ratelimit_limit": 10, "x_gate_ratelimit_reset_timestamp": 1681985856667 }, "data": { "result": { "req_id": "request-2", "req_header": null, "req_param": { "text": "t-my-custom-id", "currency_pair": "GT_USDT", "type": "limit", "account": "spot", "side": "buy", "amount": "1", "price": "1" } } } }
+{ "request_id": "request-2", "ack": true, "header": { "response_time": "1681985856667", "status": "200", "channel": "spot.order_place", "event": "api", "client_id": "::1-0x140033dc0c0", "x_in_time": 1681985856667508, "x_out_time": 1681985856667598, "conn_id": "5e74253e9c793974", "conn_trace_id": "1bde5aaa0acf2f5f48edfd4392e1fa68", "trace_id": "e410abb5f74b4afc519e67920548838d", "x_gate_ratelimit_requests_remain": 9, "x_gate_ratelimit_limit": 10, "x_gate_ratelimit_reset_timestamp": 1681985856667 }, "data": { "result": { "req_id": "request-2", "req_header": null, "req_param": { "text": "t-my-custom-id", "currency_pair": "BTC_USD", "trade_quote": "USDC", "type": "limit", "account": "spot", "side": "buy", "amount": "1", "price": "1" } } } }
 服务端 api 推送示例
 { "request_id": "request-2", "header": { "response_time": "1681986204784", "status": "200", "channel": "spot.order_place", "event": "api", "client_id": "::1-0x140001623c0", "x_in_time": 1681985856667508, "x_out_time": 1681985856667598, "conn_id": "5e74253e9c793974", "conn_trace_id": "1bde5aaa0acf2f5f48edfd4392e1fa68", "trace_id": "e410abb5f74b4afc519e67920548838d", "x_gate_ratelimit_requests_remain": 9, "x_gate_ratelimit_limit": 10, "x_gate_ratelimit_reset_timestamp": 1681986204784 }, "data": { "result": { "id": "1700664330", "text": "t-my-custom-id", "amend_text": "-", "create_time": "1681986204", "update_time": "1681986204", "create_time_ms": 1681986204832, "update_time_ms": 1681986204832, "status": "open", "currency_pair": "GT_USDT", "type": "limit", "account": "spot", "side": "buy", "amount": "1", "price": "1", "time_in_force": "gtc", "iceberg": "0", "left": "1", "fill_price": "0", "filled_total": "0", "fee": "0", "fee_currency": "GT", "point_fee": "0", "gt_fee": "0", "gt_maker_fee": "0.0015", "gt_taker_fee": "0.0015", "gt_discount": true, "rebated_fee": "0", "rebated_fee_currency": "USDT", "stp_id": 1, "stp_act": "cn", "finish_as": "open" } } }
@@ -1156,12 +1198,12 @@ POST /spot/orders POST /spot/batch_orders
 # 下单请求
 代码示例：请求前要先登录
-#!/usr/bin/python import time import json # pip install websocket_client from websocket import create_connection placeParam = {"text":"t-my-custom-id","currency_pair":"GT_USDT","type":"limit","account":"spot","side":"buy","amount":"1","price":"1"} batchPlaceParam = [ {"text":"t-my-custom-id-1","currency_pair":"GT_USDT","type":"limit","account":"spot","side":"buy","amount":"1","price":"1"}, {"text":"t-my-custom-id-2","currency_pair":"GT_USDT","type":"limit","account":"spot","side":"buy","amount":"1","price":"1.1"} ] ws = create_connection("wss://api.gateio.ws/ws/v4/") channel = "spot.order_place" # refer to the Authentication section for a WebSocket API code example # create a order ws.send(json.dumps({ "time":int(time.time()), "channel":channel, "event":"api", "payload":{ "req_id":"test_1", # create a order "req_param": placeParam # batch orders # "req_param": batchPlaceParam } })) for i in range(2): data = ws.recv() print("data: ", data)
+#!/usr/bin/python import time import json # pip install websocket_client from websocket import create_connection placeParam = {"text":"t-my-custom-id","currency_pair":"BTC_USD","trade_quote":"USDC","type":"limit","account":"spot","side":"buy","amount":"1","price":"1"} batchPlaceParam = [ {"text":"t-my-custom-id-1","currency_pair":"BTC_USD","trade_quote":"USDC","type":"limit","account":"spot","side":"buy","amount":"1","price":"1"}, {"text":"t-my-custom-id-2","currency_pair":"ETH_USD","trade_quote":"USDG","type":"limit","account":"spot","side":"buy","amount":"1","price":"1.1"} ] ws = create_connection("wss://api.gateio.ws/ws/v4/") channel = "spot.order_place" # refer to the Authentication section for a WebSocket API code example # create a order ws.send(json.dumps({ "time":int(time.time()), "channel":channel, "event":"api", "payload":{ "req_id":"test_1", # create a order "req_param": placeParam # batch orders # "req_param": batchPlaceParam } })) for i in range(2): data = ws.recv() print("data: ", data)
 代码示例：请求前要先登录
-package main import ( "crypto/hmac" "crypto/sha512" "crypto/tls" "encoding/hex" "encoding/json" "fmt" "github.com/gorilla/websocket" "net/url" "strconv" "time" ) // example WebSocket create order in go func main() { u := url.URL{Scheme: "ws", Host: "xxxx", Path: "xxx"} websocket.DefaultDialer.TLSClientConfig = &tls.Config{RootCAs: nil, InsecureSkipVerify: true} c, _, err := websocket.DefaultDialer.Dial(u.String(), nil) if err != nil { panic(err) } c.SetPingHandler(nil) // read msg go func() { for { _, message, err := c.ReadMessage() if err != nil { c.Close() panic(err) } fmt.Printf("recv: %s\n", message) } }() // warn: before order, you should login first, pls refer to the channel `spot.login`; // order_place orderParam := OrderParam{ Text: "t-123456", CurrencyPair: "ETH_BTC", Type: "limit", Account: "spot", Side: "buy", Iceberg: "0", Amount: "1", Price: "5.00032", TimeInForce: "gtc", AutoBorrow: false, StpAct: "cn", } paramBytes, _ := json.Marshal(orderParam) requestId := fmt.Sprintf("%d-%d", time.Now().UnixMilli(), 1) order_place := ApiRequest{ Time: time.Now().Unix(), Channel: "spot.order_place", Event: "api", Payload: ApiPayload{ RequestId: requestId, RequestParam: []byte(paramBytes), }, } orderPlaceReqByte, _ := json.Marshal(order_place) err = c.WriteMessage(websocket.TextMessage, orderPlaceReqByte) if err != nil { panic(err) } select {} } type ApiRequest struct { App string `json:"app,omitempty"` Time int64 `json:"time"` Id *int64 `json:"id,omitempty"` Channel string `json:"channel"` Event string `json:"event"` Payload ApiPayload `json:"payload"` } type ApiPayload struct { ApiKey string `json:"api_key,omitempty"` Signature string `json:"signature,omitempty"` Timestamp string `json:"timestamp,omitempty"` RequestId string `json:"req_id,omitempty"` RequestParam json.RawMessage `json:"req_param,omitempty"` } type OrderParam struct { Text string `json:"text,omitempty"` CurrencyPair string `json:"currency_pair,omitempty"` Type string `json:"type,omitempty"` Account string `json:"account,omitempty"` Side string `json:"side,omitempty"` Iceberg string `json:"iceberg,omitempty"` Amount string `json:"amount,omitempty"` Price string `json:"price,omitempty"` TimeInForce string `json:"time_in_force,omitempty"` AutoBorrow bool `json:"auto_borrow,omitempty"` StpAct string `json:"stp_act,omitempty"` }
+package main import ( "crypto/hmac" "crypto/sha512" "crypto/tls" "encoding/hex" "encoding/json" "fmt" "github.com/gorilla/websocket" "net/url" "strconv" "time" ) // example WebSocket create order in go func main() { u := url.URL{Scheme: "ws", Host: "xxxx", Path: "xxx"} websocket.DefaultDialer.TLSClientConfig = &tls.Config{RootCAs: nil, InsecureSkipVerify: true} c, _, err := websocket.DefaultDialer.Dial(u.String(), nil) if err != nil { panic(err) } c.SetPingHandler(nil) // read msg go func() { for { _, message, err := c.ReadMessage() if err != nil { c.Close() panic(err) } fmt.Printf("recv: %s\n", message) } }() // warn: before order, you should login first, pls refer to the channel `spot.login`; // order_place orderParam := OrderParam{ Text: "t-123456", CurrencyPair: "BTC_USD", TradeQuote: "USDC", Type: "limit", Account: "spot", Side: "buy", Iceberg: "0", Amount: "1", Price: "5.00032", TimeInForce: "gtc", AutoBorrow: false, StpAct: "cn", } requestParam := interface{}(orderParam) // 批量下单时改为序列化 []OrderParam；每个订单分别携带自己的 trade_quote。 // requestParam = []OrderParam{orderParam, {CurrencyPair: "ETH_USD", TradeQuote: "USDG", Type: "limit", Account: "spot", Side: "sell", Amount: "1", Price: "3000"}} paramBytes, _ := json.Marshal(requestParam) requestId := fmt.Sprintf("%d-%d", time.Now().UnixMilli(), 1) order_place := ApiRequest{ Time: time.Now().Unix(), Channel: "spot.order_place", Event: "api", Payload: ApiPayload{ RequestId: requestId, RequestParam: []byte(paramBytes), }, } orderPlaceReqByte, _ := json.Marshal(order_place) err = c.WriteMessage(websocket.TextMessage, orderPlaceReqByte) if err != nil { panic(err) } select {} } type ApiRequest struct { App string `json:"app,omitempty"` Time int64 `json:"time"` Id *int64 `json:"id,omitempty"` Channel string `json:"channel"` Event string `json:"event"` Payload ApiPayload `json:"payload"` } type ApiPayload struct { ApiKey string `json:"api_key,omitempty"` Signature string `json:"signature,omitempty"` Timestamp string `json:"timestamp,omitempty"` RequestId string `json:"req_id,omitempty"` RequestParam json.RawMessage `json:"req_param,omitempty"` } type OrderParam struct { Text string `json:"text,omitempty"` CurrencyPair string `json:"currency_pair,omitempty"` TradeQuote string `json:"trade_quote,omitempty"` Type string `json:"type,omitempty"` Account string `json:"account,omitempty"` Side string `json:"side,omitempty"` Iceberg string `json:"iceberg,omitempty"` Amount string `json:"amount,omitempty"` Price string `json:"price,omitempty"` TimeInForce string `json:"time_in_force,omitempty"` AutoBorrow bool `json:"auto_borrow,omitempty"` StpAct string `json:"stp_act,omitempty"` }
 请求参数示例
 下单
-{ "time": 1681986203, "channel": "spot.order_place", "event": "api", "payload": { "req_id": "request-2", "req_param": { "text": "t-my-custom-id", "currency_pair": "GT_USDT", "type": "limit", "account": "spot", "side": "buy", "amount": "1", "price": "1" } } }
+{ "time": 1681986203, "channel": "spot.order_place", "event": "api", "payload": { "req_id": "request-2", "req_param": { "text": "t-my-custom-id", "currency_pair": "BTC_USD", "trade_quote": "USDC", "type": "limit", "account": "spot", "side": "buy", "amount": "1", "price": "1" } } }
... (diff truncated, total 252 lines) ...
```
