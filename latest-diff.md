<!-- has_changes=true date=2026-07-09 -->
# Exchange API Changelog Diff

Generated: 2026-07-09 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (131907 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 162 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (83743 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (34939 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120249 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 956f418..f00be15 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -22,65 +22,100 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | 参数名 | 类型 | 描述
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
-ELP 合并深度订单簿
-最近更新：2026年6月23日
-为简化 ELP 行情数据集成，OKX 将推出合并深度频道 books-elp-all，将非 ELP 与当前可交易的 ELP 流动性合并为单一数据流，用户无需再分别订阅 books 和 books-elp 并在客户端自行合并。该能力同时提供 WebSocket 与 REST 两种方式，预计于 2026年7月中旬 在模拟盘上线，并于 2026年7月下旬 正式上线。
-- 通过 /ws/v5/business 端点（wss://ws.okx.com:8443/ws/v5/business）新增 WebSocket 频道 books-elp-all。400 档深度；初始全量推送 + 每 100 毫秒增量推送。推送合并非 ELP 和当前可交易 ELP 流动性的深度数据。不可交易的 ELP 订单在平台端过滤。
-  - WS / books-elp-all 频道
-asks 和 bids 中的每个元素是一个 4 元素数组：[price, totalQty, nonElpQty, orderCount]
-- price：深度价格
-- totalQty：该价格档位的总可见数量（非 ELP 数量 + 当前可交易 ELP 数量）。ELP 吃单用户应使用此字段作为完整可见深度。
-- nonElpQty：仅非 ELP（有机）数量。非 ELP 吃单用户应使用此字段作为其可用深度。
-- orderCount：该价格档位的可见订单数量（包括非 ELP 和当前可交易的 ELP 订单）。
-推送数据参数
+ELP 更名为 RPI（散户价格优化）计划
+最近更新：2026年7月8日
+OKX 将品牌 Enhanced Liquidity Program（ELP） 更名为 Retail Price Improvement（散户价格优化，RPI）。本次变更包含新的 RPI 合并深度订单簿（books-rpi，同时提供 WebSocket 与 REST）、更名后的挂单类型 rpi（替代 elp）、扩展后的下单参数 rpiTakerAccess（替代 isElpTakerAccess）、用于 RPI 挂单价格间距规则的新参数 rpiPxRound，以及更名后的账户字段 rpi/rpiMaker。预计于 2026年7月21日 在模拟盘上线，并于 2026年7月28日 正式上线。
+ELP 命名弃用截止日期：2026年10月31日
+在此日期之前，OKX 将以两种不同方式并行运行 ELP 与 RPI 命名：
+- 字段重命名——两者都被接受；当请求或响应中同时包含两者时，以 RPI 命名的字段为准：
+  - isElpTakerAccess → rpiTakerAccess
+  - elp → rpi
+  - elpMaker → rpiMaker
+- 取值重命名——互斥，只能二选一，不能同时传递：
+  - ordType: elp → ordType: rpi
+  - books-elp → books-rpi
+现有集成可继续正常运行，无需改动。ELP 命名将于上述截止日期后停止支持——请在此之前完成所有集成向 RPI 命名的迁移。
+新增合并深度：books-rpi（WS + REST）
+- 新增 books-rpi，将非 RPI（有机）与 RPI 流动性合并为单一深度数据流——同时提供公共 WebSocket 频道（/ws/v5/public，400 档深度，初始全量推送 + 每 100 毫秒增量推送）与 REST 接口（GET /api/v5/market/books-rpi，服务端每 200 毫秒刷新一次）。不提供 checksum，WS 序列一致性依赖 seqId/prevSeqId。取代 books-elp（见上方迁移说明）。
+  - WS / 深度频道
+asks/bids 中的每个元素为 [price, totalQty, nonRpiQty, count]——totalQty 为该档位的总深度，nonRpiQty 为其中仅有机的部分，count 为该档位的汇总订单数量。
+REST 请求参数：instId（必填）、sz（每侧深度档数，最大 400，默认 1）。
+吃单参数：rpiTakerAccess（替代 isElpTakerAccess）
+- rpiTakerAccess 是 isElpTakerAccess 的更名并扩展，支持所有标准订单类型（limit、market、fok、ioc、optimal_limit_ioc；此前仅 ioc），并可在改单接口中设置。isElpTakerAccess 在弃用日期前将作为别名继续被接受（见上方迁移说明）。
+- 错误码 54045（此前用于非 ioc 订单尝试吃取 RPI 流动性时返回）已废弃——现在 rpiTakerAccess 对所有订单类型均有效，该错误码不再可能触发。
+均适用于下单/改单，REST + WS： - POST / 下单 - POST / 批量下单 - POST / 修改订单 - POST / 批量修改订单 - WS / 下单 - WS / 批量下单 - WS / 改单 - WS / 批量改单
+| 参数名 | 类型 | 是否必须 | 描述
+| rpiTakerAccess | Boolean | 否 | 默认值为 false。
+设为 true 时，订单可使用 RPI 流动性，适用于所有标准订单类型（此前仅 ioc）。
+下单时，除 post_only 外的所有订单类型都会触发减速带机制；改单时，减速带适用于所有订单类型（包括 post_only）。
+改单时不会从原始订单继承，必须每次显式指定（省略则该次改单视为 false）。
+挂单类型：rpi（替代 elp）
+- 下 RPI 挂单时，请将 ordType 设为 rpi 而非 elp。elp 在弃用日期前将继续被接受（见上方迁移说明）——ordType 只能取一个值，二者选其一，不能同时传递。
+适用于下单，REST + WS： - POST / 下单 - POST / 批量下单 - WS / 下单 - WS / 批量下单
+挂单参数：rpiPxRound
+- rpiPxRound 为新增参数，用于 RPI 挂单价格间距规则（详见下文）。仅对 RPI 挂单（ordType: rpi）生效；对非 RPI 订单及 OPTION/EVENTS 将被忽略。
+均适用于下单/改单，REST + WS（接口列表同上方 rpiTakerAccess）。
+| 参数名 | 类型 | 是否必须 | 描述
+| rpiPxRound | Boolean | 否 | 默认值为 false。设为 true 时，违反间距规则的价格将自动向外取整至最近的可挂单、且不会吃单的价位，而非直接拒绝。
+- 在 orders WebSocket 私有频道新增 amendSource 枚举值 6：表示系统为满足 RPI 挂单价格间距规则（由 rpiPxRound 触发）而自动调整（取整）了订单价格。下单时，若发生取整，orders 频道会推送两次——一次为原始提交价格，另一次为取整后的价格（携带 amendSource: 6）；若价格无需取整，则不会有第二次推送。改单时，仅会推送一次，且直接为取整后的价格。
+  - WS / 订单频道
+RPI 挂单价格间距规则
+RPI 挂单需遵守间距规则（见下方 rpiMinLevel / rpiMinPxBand）。订单违反该规则时将被拒绝，除非 rpiPxRound 设为 true，此时价格会自动向外取整至最近的合规价位（见上方 rpiPxRound）。
+- 新增返回参数 rpiMinLevel 与 rpiMinPxBand，用于展示各产品的间距阈值。
+  - 获取交易产品基础信息（公共）
 | 参数名 | 类型 | 描述
-| asks | Array of Arrays | 卖方深度，每个元素为 [price, totalQty, nonElpQty, orderCount]
-| bids | Array of Arrays | 买方深度，每个元素为 [price, totalQty, nonElpQty, orderCount]
-| ts | String | 深度生成时间，Unix 时间戳的毫秒数格式，如 1779782400000
-| prevSeqId | Integer | 上一条推送消息的序列号，全量推送时 prevSeqId = -1
-| seqId | Integer | 当前推送消息的序列号
-- 新增 REST 接口用于获取 ELP 合并深度订单簿：
-  - GET / 获取产品深度
-GET / 获取 ELP 合并深度
-获取产品的 ELP 合并深度订单簿，合并非 ELP 和当前可交易的 ELP 流动性。数据每 200 毫秒更新一次。
-该接口不会立即返回数据，而是在服务端缓存更新后返回最新数据。
-限速：20 次/2s
-限速规则：IP
-权限：公共
-HTTP 请求
-GET /api/v5/market/books-elp-all
-请求示例
-GET /api/v5/market/books-elp-all?instId=BTC-USDT-SWAP
-请求参数
-| 参数名 | 类型 | 是否必须 | 描述
-| instId | String | 是 | 产品 ID，如 BTC-USDT-SWAP。仅支持已启用 ELP 的产品。
-| sz | String | 否 | 每侧深度档数，最大 400，默认 1
-返回示例
-{ "code": "0", "msg": "", "data": [ { "asks": [ ["67855.2", "0.5", "0.5", "1"], ["67856.0", "1.3", "1.0", "4"], ["67860.5", "0.3", "0", "1"] ], "bids": [ ["67854.8", "1.7", "1.2", "3"], ["67853.0", "0.8", "0.8", "1"] ], "ts": "1779782400000", "seqId": 123456 } ] }
+| rpiMinLevel | String | RPI 买一价与卖一价之间的最小间距，以有机价格档位数计。默认值为 5；事件合约（Event Contracts）为 0。
+| rpiMinPxBand | String | 满足间距规则所需的、与对方最优有机报价之间的最小距离，单位为基点（bps），例如 20。
+RPI 挂单权限字段：rpi（替代 elp）
+- 新增返回参数 rpi，用于表示 RPI 挂单权限。elp 在弃用日期前将作为别名继续被接受（见上方迁移说明）。
+  - 获取交易产品基础信息（私有）
+| 参数名 | 类型 | 描述
+| rpi | String | RPI 挂单权限。
+0：该产品未开通 RPI
+1：已开通，但当前用户无权限下 RPI 订单
+2：已开通且当前用户有权限
+返回 1/2 不代表当前存在 RPI 流动性。
+RPI 挂单费率字段：rpiMaker（替代 elpMaker）
+- 新增返回参数 rpiMaker，用于表示 RPI 挂单有效费率。elpMaker 在弃用日期前将作为别名继续被接受（见上方迁移说明）。
+  - 获取当前账户交易手续费费率
+| 参数名 | 类型 | 描述
+| rpiMaker | String | RPI 挂单有效费率，若该产品不适用 RPI 则返回 ""。
+成交来源字段：source
+- GET /api/v5/market/trades 返回字段 source 取值 1 的说明由"流动性增强计划订单"更新为 RPI 订单（原 ELP 订单）。返回的取值 1 本身不变，仅更新说明文字。
+  - GET / 获取交易产品公共成交数据
+2026-07-07
+事件合约 HIT 和 BETWEEN 结算方式
+OKX 预测市场现已支持两种新的结算方式 — hit（价格在事件窗口内触及目标行权价格）和 between（结算价格在指定范围内）——以及新频率 monthly（每月）。
+- 在以下接口/频道新增返回参数 capStrike 和 hitDir：
+  - GET / 获取市场
+  - WS / 事件合约市场频道
 返回参数
 | 参数名 | 类型 | 描述
-| asks | Array of Arrays | 卖方深度，每个元素为 [price, totalQty, nonElpQty, orderCount]
-| bids | Array of Arrays | 买方深度，每个元素为 [price, totalQty, nonElpQty, orderCount]
-| ts | String | 深度生成时间，Unix 时间戳的毫秒数格式，如 1779782400000
-| seqId | Integer | 当前推送消息的序列号
-ELP 吃单权限扩展至所有订单类型
-最近更新：2026年6月23日
-订单参数 isElpTakerAccess 将扩展支持所有订单类型（此前仅 ioc），并新增支持在改单接口中使用。本次变更预计于 2026年7月中旬 在模拟盘上线，并于 2026年7月下旬 正式上线。
-- 更新请求参数 isElpTakerAccess 的描述，以反映扩展的订单类型支持和改单行为：
-  - POST / 下单
-  - POST / 批量下单
-  - POST / 修改订单
-  - POST / 批量修改订单
-  - WS / 下单
-  - WS / 批量下单
-  - WS / 改单
-  - WS / 批量改单
-请求参数
-| 参数名 | 类型 | 是否必须 | 描述
-| isElpTakerAccess | Boolean | 否 | 默认值为 false。设为 true 时，订单可以使用 ELP 流动性。适用于所有订单类型。当 isElpTakerAccess 为 true 时，除 post_only 外的所有订单类型都会触发减速带机制；下单时 post_only 订单可免于减速带。isElpTakerAccess 也可在改单接口中使用，且不会从原始订单继承——必须在每次改单请求中显式重新指定（改单时省略则该次改单视为 false）。改单时，减速带适用于所有订单类型（包括 post_only）；如需改 post_only 订单且不想触发减速带，请在该次改单中不设置 isElpTakerAccess。
+| capStrike | String | between 结算方式中导致 YES 结果的最大到期值。"INF" 表示无上限（最高区间）。
+非 between 方式返回 ""。
+| hitDir | String | 触及方向。仅在结算方式为 hit 时适用。
+up：价格从下方触及
+dn：价格从上方触及
+""：不适用（非 hit 方式）
+- 在以下接口的 settlement 对象中，返回参数 method 新增枚举值：
+  - GET / 获取系列
+| 参数名 | 类型 | 描述
+| > method | String | 结算方式。
+price_up_down：价格涨跌
+price_above：价格高于
+hit：触及（价格触达行权价格，立即结算）
+between：区间（结算价格在 [floorStrike, capStrike) 范围内）
+- 在以下接口返回参数 freq 新增枚举值：
+  - GET / 获取系列
+| 参数名 | 类型 | 描述
+| freq | String | 系列频率。
+five_min
+fifteen_min
+hourly
+daily
+monthly
 合约冷静期下单拦截
-最近更新：2026年6月23日
-OKX 将合约冷静期从仅前端 UI 拦截扩展至所有下单渠道，包括 REST API 与 WebSocket。冷静期生效期间，覆盖标的下 SWAP 与 FUTURES 的非只减仓（reduce-only）订单将在服务端被拒绝；只减仓订单不受影响。
-预计上线时间：2026 年 7 月 7 日。
-新增错误码
+OKX 已将合约冷静期从仅前端 UI 拦截扩展至所有下单渠道，包括 REST API 与 WebSocket。冷静期生效期间，覆盖标的下 SWAP 与 FUTURES 的非只减仓（reduce-only）订单将在服务端被拒绝；只减仓订单不受影响。
+详情请参见公告：关于合约冷静期升级的通知。
+- 新增错误码：
 | 错误码 | HTTP 状态码 | 错误信息
 | 54094 | 200 | 下单失败，当前交易产品处于冷静期内，暂不支持下单。

```
