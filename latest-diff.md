<!-- has_changes=true date=2026-07-29 -->
# Exchange API Changelog Diff

Generated: 2026-07-29 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132459 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 40 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3590 bytes)

- [OK] Bybit V5 (`bybit`): no change (86947 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 18 diff lines

- [CHANGED] **Gate.io Spot WebSocket v4** (`gate-spot-ws`): 26 diff lines

- [CHANGED] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): 26 diff lines



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 495698f..8b95282 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -49,7 +49,7 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 受影响的订单类型有：post_only、mmp_and_post_only、rpi（Retail Price Improvement）。
 其他订单类型如 limit（普通限价单）、market（市价单）、ioc、fok 订单推送行为保持不变。
+2026-07-28
 ELP 更名为 RPI（散户价格优化）计划
-最近更新：2026年7月27日
-OKX 将品牌 Enhanced Liquidity Program（ELP） 更名为 Retail Price Improvement（散户价格优化，RPI）。本次变更包含新的 RPI 合并深度订单簿（books-rpi，同时提供 WebSocket 与 REST）、更名后的挂单类型 rpi（替代 elp）、扩展后的下单参数 rpiTakerAccess（替代 isElpTakerAccess）、用于 RPI 挂单价格间距规则的新参数 rpiPxRound，以及更名后的账户字段 rpi/rpiMaker。预计于 2026年7月23日 在模拟盘上线，并于 2026年7月28日 正式上线。
+OKX 将品牌 Enhanced Liquidity Program（ELP） 更名为 Retail Price Improvement（散户价格优化，RPI）。本次变更包含新的 RPI 合并深度订单簿（books-rpi，同时提供 WebSocket 与 REST）、更名后的挂单类型 rpi（替代 elp）、扩展后的下单参数 rpiTakerAccess（替代 isElpTakerAccess）、用于 RPI 挂单价格间距规则的新参数 rpiPxRound，以及更名后的账户字段 rpi/rpiMaker。
 ELP 命名弃用截止日期：2026年10月31日
 在此日期之前，OKX 将以两种不同方式并行运行 ELP 与 RPI 命名：
@@ -68,5 +68,5 @@ asks/bids 中的每个元素为 [price, totalQty, nonRpiQty, count]——totalQt
 REST 请求参数：instId（必填）、sz（每侧深度档数，最大 400，默认 1）。
 吃单参数：rpiTakerAccess（替代 isElpTakerAccess）
-- rpiTakerAccess 是 isElpTakerAccess 的更名并扩展，支持所有标准订单类型（limit、market、fok、ioc、optimal_limit_ioc；此前仅 ioc），并可在改单接口中设置。isElpTakerAccess 在弃用日期前将作为别名继续被接受（见上方迁移说明）。
+- rpiTakerAccess 是 isElpTakerAccess 的更名并扩展，支持所有标准订单类型（limit、market、fok、ioc；此前仅 ioc），并可在改单接口中设置。isElpTakerAccess 在弃用日期前将作为别名继续被接受（见上方迁移说明）。
 - 错误码 54045（此前用于非 ioc 订单尝试吃取 RPI 流动性时返回）已废弃——现在 rpiTakerAccess 对所有订单类型均有效，该错误码不再可能触发。
 均适用于下单/改单，REST + WS： - POST / 下单 - POST / 批量下单 - POST / 修改订单 - POST / 批量修改订单 - WS / 下单 - WS / 批量下单 - WS / 改单 - WS / 批量改单
@@ -110,4 +110,18 @@ RPI 挂单费率字段：rpiMaker（替代 elpMaker）
 - GET /api/v5/market/trades 返回字段 source 取值 1 的说明由"流动性增强计划订单"更新为 RPI 订单（原 ELP 订单）。返回的取值 1 本身不变，仅更新说明文字。
   - GET / 获取交易产品公共成交数据
+错误码变更
+错误消息由 ELP 更新为 RPI：
+| 错误码 | 原消息 | 更新后消息
+| 54039 | ELP 订单不支持仅减仓设置 | RPI 订单不支持仅减仓设置
+| 54040 | ELP 订单无法与止盈止损设置同时使用 | RPI 订单无法与止盈止损设置同时使用
+| 54041 | {param0} 不支持下 ELP 订单 | {param0} 不支持下 RPI 订单
+| 54042 | 您无法为 {param0} 下 ELP 订单 | 您无法为 {param0} 下 RPI 订单
+| 54043 | 您最多只能为 {param0} 下 {param1} 个 ELP 订单，请撤销部分订单后再试 | 您最多只能为 {param0} 下 {param1} 个 RPI 订单，请撤销部分订单后再试
+| 54044 | {param0} 不支持 ELP，你不能吃单 ELP 挂单 | {param0} 不支持 RPI，你不能吃单 RPI 挂单
+| 54046 | 你不能吃单 ELP 挂单 | 你不能吃单 RPI 挂单
+| 54049 | 由于系统繁忙，API 用户目前无法吃单 ELP 挂单。请将 isElpTakerAccess 设置为 false 以继续操作 | 由于系统繁忙，API 用户目前无法吃单 RPI 挂单。请将 rpiTakerAccess 设置为 false 以继续操作
+已弃用错误码：
+| 错误码 | 消息 | 原因
+| 54045 | OpenAPI 用户只能下 IOC 订单来吃单 ELP 挂单 | 已废弃——rpiTakerAccess 现适用于所有订单类型，不再限于 IOC。
 2026-07-24
 移除 speedBump 请求参数

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index 077ec0b..6df4d09 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,4 +1,13 @@
 WARNING
 The Pro API is currently in beta testing and should not be used in production trading environments.
+2026.08.03#
+Discontinuation of the "Hidden Order" Feature#
+[Modify] Classic REST
+No longer supports the hidden, iceberg and visibleSize parameters. Requests containing these parameters will be rejected with error code "400413" with error message "Invaild order type, hidden and iceberg orders are not supported any more." .
+| # | Business Line | Endpoint
+| 1 | Spot Trading | Add Order ,Add Order Sync ,Add Order Test , Batch Add Orders , Batch Add Orders Sync , Add Stop Order
+| 2 | Margin Trading | Add Order , Add Order Test , Add Stop Order
+| 3 | Futures Trading | Add Order , Add Order Test , Batch Add Orders , Add Take Profit And Stop Loss Order
+| 4 | Copy Trading | Add Order, Add Order Test, Add Take Profit And Stop Loss Order
 2026.07.17#
 [Modify] UTA REST/WebSocket Get Order Book & Subscription

```

### Gate.io Spot WebSocket v4 (`gate-spot-ws`)
- Source: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/

```diff
diff --git a/changelogs/gate-spot-ws.txt b/changelogs/gate-spot-ws.txt
index d4ae56f..bd649bf 100644
--- a/changelogs/gate-spot-ws.txt
+++ b/changelogs/gate-spot-ws.txt
@@ -211,5 +211,8 @@ TIP
 # 服务升级通知
 服务在即将关闭进行升级时，会向当前连接主动推送一条系统通知，客户端收到后应尽快重连。
-服务端推送格式（SystemNotifyDTO）：
+频道（Channel）： spot.system
+事件（Event）： update
+当 channel 为 spot.system、event 为 update 且 result.type 为 upgrade 时，客户端可将该消息识别为服务升级通知。
+result 格式（SystemNotifyDTO）：
 | 字段 | 类型 | 说明
 | type | String | 通知类型，如 upgrade
@@ -217,5 +220,5 @@ TIP
 | data | Object | 可选，扩展数据
 示例（服务升级）：
-{ "type": "upgrade", "msg": "The connection will soon be closed for a service upgrade. Please reconnect." }
+{ "time": 1784800711, "time_ms": 1784800711140, "channel": "spot.system", "event": "update", "result": { "type": "upgrade", "msg": "The connection will soon be closed for a service upgrade. Please reconnect." } }
 # Tickers 频道
 spot.tickers
@@ -1537,3 +1540,3 @@ account: 指定查询账户。不指定默认现货，保证金和逐仓杠杆
 | »»label | String | 以字符串格式表示错误类型
 | »»message | String | 错误信息详情
-Last Updated: 7/2/2026, 7:08:59 AM
+Last Updated: 7/25/2026, 7:18:17 AM

```

### Gate.io Futures WebSocket v4 (`gate-futures-ws`)
- Source: https://www.gate.io/docs/developers/futures/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/futures/ws/zh_CN/

```diff
diff --git a/changelogs/gate-futures-ws.txt b/changelogs/gate-futures-ws.txt
index 9e30ffe..411f1ce 100644
--- a/changelogs/gate-futures-ws.txt
+++ b/changelogs/gate-futures-ws.txt
@@ -261,5 +261,8 @@ futures.ping
 # 服务升级通知
 服务在即将关闭进行升级时，会向当前连接主动推送一条系统通知，客户端收到后应尽快重连。
-服务端推送格式（SystemNotifyDTO）：
+频道（Channel）： futures.system
+事件（Event）： update
+当 channel 为 futures.system、event 为 update 且 result.type 为 upgrade 时，客户端可将该消息识别为服务升级通知。
+result 格式（SystemNotifyDTO）：
 | 字段 | 类型 | 说明
 | type | String | 通知类型，如 upgrade
@@ -267,5 +270,5 @@ futures.ping
 | data | Object | 可选，扩展数据
 示例（服务升级）：
-{ "type": "upgrade", "msg": "The connection will soon be closed for a service upgrade. Please reconnect." }
+{ "time": 1782378978, "time_ms": 1782378978107, "channel": "futures.system", "event": "update", "result": { "type": "upgrade", "msg": "The connection will soon be closed for a service upgrade. Please reconnect." } }
 # ticker 频道
 ticker是合约状态的高级概述。它向你展示了最高的， 最低的、最后的交易价格。它还包括每日交易量和价格等信息
@@ -2022,3 +2025,3 @@ req_param` API 订单模型的 JSON 字节数据:
 | »»label | String | 错误类型
 | »»message | String | 详细错误信息
-Last Updated: 6/25/2026, 1:23:11 AM
+Last Updated: 7/25/2026, 7:18:17 AM

```
