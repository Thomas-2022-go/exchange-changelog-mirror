<!-- has_changes=true date=2026-07-24 -->
# Exchange API Changelog Diff

Generated: 2026-07-24 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132274 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 204 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3590 bytes)

- [OK] Bybit V5 (`bybit`): no change (85946 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (35340 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120249 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index b4e5786..3873cfd 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,45 +1,11 @@
 待发布内容
-FUTURES 和 SWAP 计划委托支持追逐限价委托（Chase Order）
-最近更新：2026年7月9日
-FUTURES 和 SWAP 计划委托（Trigger Order）现可在触发时下发追逐限价委托（Chase Order）——advanceOrdType 新增取值 chase，其参数由新增数组 advChaseParams 承载。查询接口通过新增字段 subAlgoIdList 返回触发后生成的追逐委托 algoId；在计划委托触发前，可通过改单接口修改追逐值。预计于 2026年7月15日 在模拟盘上线，并于 2026年7月21日 正式上线。
-策略委托下单
-- advanceOrdType 新增取值 chase，并新增 advChaseParams 数组；orderPx 变更为条件必填（追逐委托不适用）。
-  - POST / 策略委托下单
-本期暂不支持追逐委托与附带止盈止损（attachAlgoOrds）同时设置。
-| 参数名 | 类型 | 是否必须 | 描述
-| advanceOrdType | String | 否 | 计划委托触发时下发的订单类型。
-fok、ioc 或 chase。
-chase 仅适用于 FUTURES 和 SWAP。
-默认为空（按 orderPx 下发限价或市价单）。
-| orderPx | String | 条件必填 | 计划委托触发时下发订单的价格。-1 表示市价。当 advanceOrdType 为 chase 时不适用（追逐委托无固定价格）。
-| advChaseParams | Array of objects | 条件必填 | 追逐参数。当 advanceOrdType 为 chase 时必填。
-| > chaseType | String | 条件必填 | 追逐距离单位。
-distance（默认）：与买一价/卖一价的绝对价格距离，以结算货币计。
-ratio：百分比。
-| > chaseVal | String | 条件必填 | 追逐值。当 chaseType 为 distance 时，为与买一价/卖一价的距离（以结算货币计）；当 ratio 时，0.1 表示 10%。
-默认值 0 表示直接跟随买一价/卖一价；大于 0 表示设置一个距离。
-| > maxChaseType | String | 条件必填 | 最大追逐距离单位。distance 或 ratio。须与 maxChaseVal 成对出现。
-| > maxChaseVal | String | 条件必填 | 最大追逐距离值。须为正数。须与 maxChaseType 成对出现。当偏离达到该值时，追逐委托自动撤单。
-修改策略委托订单
-- 新增 advChaseParams 改单字段，用于在计划委托挂单期间（触发前）调整追逐值。chaseType、maxChaseType 及追逐价格模式在下单时固定，不可修改。
-  - POST / 修改策略委托订单
-| 参数名 | 类型 | 是否必须 | 描述
-| advChaseParams | Array of objects | 条件必填 | 待修改的追逐参数。仅适用于 advanceOrdType 为 chase 的挂单中计划委托。
-| > newChaseVal | String | 条件必填 | 新的追逐值。非负数，按订单已有（不可修改）的 chaseType 解释。不可越过原 chaseVal 的 0 ↔ 非 0 边界——直接跟随买一价/卖一价（0）与设置距离（大于 0）两种模式不可互换。
-| > newMaxChaseVal | String | 条件必填 | 新的最大追逐距离值。须为正数，按已有（不可修改）的 maxChaseType 解释。仅在已启用最大追逐距离时适用。
-查询接口（委托单信息、委托单列表、WS 频道）
-- 新增返回参数 advanceOrdType（含新取值 chase）、advChaseParams，以及新增的 subAlgoIdList。
-  - GET / 获取策略委托单信息
-  - GET / 获取未完成策略委托单列表
-  - GET / 获取历史策略委托单列表
-  - WS / 策略委托订单频道
+移除 speedBump 请求参数
+最近更新：2026年7月21日
+事件合约减速带功能的 speedBump 请求参数不再生效。如果客户端仍然发送 speedBump，该参数将被静默忽略，不会产生任何影响。本次变更预计于 2026年7月24日 上线。
+- 在以下接口移除请求参数 speedBump：
+  - POST / 下单
+请求参数
 | 参数名 | 类型 | 描述
-| advanceOrdType | String | 计划委托的子订单类型。fok、ioc、chase 或空。
-| advChaseParams | Array of objects | 追逐参数。当 advanceOrdType 为 chase 时返回。
-| > chaseType | String | 追逐距离单位。distance 或 ratio。
-| > chaseVal | String | 追逐值。0 表示直接跟随买一价/卖一价；大于 0 表示距离。
-| > maxChaseType | String | 最大追逐距离单位。
-| > maxChaseVal | String | 最大追逐距离值。
-| subAlgoIdList | Array of strings | 计划委托触发时生成的策略委托单 algoId。当 advanceOrdType 为 chase 时，在触发后存放生成的追逐委托 algoId，触发前为空。与 ordIdList 对应，后者记录生成的普通订单，对追逐委托始终为空。
+| speedBump | String | 减速带。1：事件合约速度限制（延迟可能因市场情况调整，不提前通知）。
 信号复制新增 API 接口
 最后更新：2026 年 5 月 14 日
@@ -65,5 +31,5 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
 WebSocket 订单频道推送行为调整
-最近更新：2026 年 7 月 15 日
+最近更新：2026 年 7 月 22 日
 为了让客户能够更明确地判断 post-only（包括 mmp_and_post_only）与将要推出的 rpi 新订单的最终状态，避免收到 state: live 后订单仍被撤销的场景，欧易将调整订单频道中 post-only 与 rpi 订单的 state: live 事件行为。
 具体影响
@@ -86,5 +52,5 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 并且 price 被修改 | N/A | state: live（amendSource: 6，amendResult: 0） → state: live
 生效时间
-- 对于 rpi 订单：模拟盘 —— 2026 年 7 月 22 日；实盘 —— 2026 年 7 月 28 日。
+- 对于 rpi 订单（包括将要弃用的 elp 订单）：模拟盘 —— 2026 年 7 月 23 日；实盘 —— 2026 年 7 月 28 日。
 - 对于 post_only 和 mmp_and_post_only 订单：模拟盘和实盘均为 2026 年 8 月中旬。
 影响范围
@@ -152,4 +118,132 @@ RPI 挂单费率字段：rpiMaker（替代 elpMaker）
 - GET /api/v5/market/trades 返回字段 source 取值 1 的说明由"流动性增强计划订单"更新为 RPI 订单（原 ELP 订单）。返回的取值 1 本身不变，仅更新说明文字。
   - GET / 获取交易产品公共成交数据
+2026-07-23
+GLP 做市商表现 API
+新增两个只读接口，面向已加入 Global Liquidity Program (GLP) 的做市商查询自己的考核表现：当日快照（含当日及 MTD）和逐日历史记录。仅已加入且在有效期的 GLP 做市商可调用，子账户解析到其 master account。
+- 以下为新增接口：
+  - GET / 获取 GLP 当日表现
+  - GET / 获取 GLP 历史表现
+GET / 获取 GLP 当日表现
+获取当前账户在所有已加入 GLP 业务线（Spot / Perp / Expiry & Nitro）的当日和月度累计（MTD）表现快照。无需请求参数，账户由 API key 自动解析。
+限速：5次/2s
+限速规则：User ID
+权限：读取
+HTTP请求
+GET /api/v5/users/glp/today-performance
+请求示例
+GET /api/v5/users/glp/today-performance
+请求参数
+无。账户由登录态自动解析。
+返回示例
+{ "code": "0", "msg": "", "data": [ { "dataReady": true, "dataDate": "2026-07-13", "account": { "masterAccountId": "832545488879789797", "combinedAccountIds": ["832545488879789798"] }, "programs": [ { "program": "SPOT", "marketMakerBusinessId": "1", "enrollmentStatus": "ENROLLED", "marketMakerLevelId": "42", "enrolledTierDisplay": "Tier 1 Class A", "qualifyingPool": "TYPE_A", "qualifyingRows": ["TOTAL"], "daily": { "volume": { "typeA": {"maker": "1000000.00", "taker": "1000000.00"}, "typeBTotal": {"maker": "1000000.00", "taker": "1000000.00"}, "tradfiX2": {"maker": "1000000.00", "taker": "1000000.00"}, "total": {"maker": "2000000.00", "taker": "2000000.00"} }, "share": { "typeA": {"maker": "0.0000", "taker": "0.0000"}, "typeBAdj": {"maker": "0.0000", "taker": "0.0000"}, "total": {"maker": "0.0000", "taker": "0.0000"} } }, "mtd": { "volume": { "typeA": {"maker": "30000000.00", "taker": "30000000.00"}, "typeBTotal": {"maker": "30000000.00", "taker": "30000000.00"}, "tradfiX2": {"maker": "30000000.00", "taker": "30000000.00"}, "total": {"maker": "60000000.00", "taker": "60000000.00"} }, "share": { "typeA": {"maker": "0.0000", "taker": "0.0000"}, "typeBAdj": {"maker": "0.0000", "taker": "0.0000"}, "total": {"maker": "0.0000", "taker": "0.0000"} }, "mtdStatus": "QUALIFIED", "qualifyingShare": {"maker": "0.0000", "taker": "0.0000"} } } ] } ] }
+返回参数
+| 参数名 | 类型 | 描述
+| dataReady | Boolean | 该 dataDate 是否已有数据。为 false 时 programs 为空数组
+| dataDate | String | 数据快照日期，yyyy-MM-dd 格式（UTC+8）。通常为 T-1；T-1 计算未完成时回退 T-2
+| account | Object | 账户身份信息
+| > masterAccountId | String | master account ID
+| > combinedAccountIds | Array of strings | 同机构组的兄弟账户 ID（不含自己）。无组则为空数组
+| programs | Array of objects | 各已加入 GLP 业务线的表现数据。dataReady 为 false 时为空数组
+| > program | String | GLP 业务线标识。
+SPOT：现货
+PERP：永续合约
+FUT_NTO：交割合约 & Nitro
+| > marketMakerBusinessId | String | 该业务线的做市商 business ID
+| > enrollmentStatus | String | 加入状态。当前恒为 ENROLLED
+| > marketMakerLevelId | String | 当前档位 ID
+| > enrolledTierDisplay | String | 当前档位展示名，如 Tier 1 Class A
+| > qualifyingPool | String | 决定当前档位的池。
+TYPE_A
+TYPE_B_ADJ
+TYPE_A_AND_B
+| > qualifyingRows | Array of strings | 合格行 key，如 ["TOTAL"]
+| > daily | Object | 当日表现快照。包含 volume 和 share（结构见下方说明）
+| > mtd | Object | 月度累计表现。包含 volume、share（同 daily 结构），以及以下额外字段
+| >> mtdStatus | String | MTD 档位状态。
+QUALIFIED：达标
+UPGRADE：升档
+DOWNGRADE：降档
+| >> qualifyingShare | Object | 决定档位的池的份额。包含 maker（String）和 taker（String）
+交易量和份额结构
+daily 和 mtd 均包含 volume（交易量）和 share（份额）两个 Object。每个 Object 下含分类 key，每个分类为包含 maker（String）和 taker（String）字段的 Object。
+| 分类 | 在 volume 中 | 在 share 中 | 描述
+| typeA | 是 | 是 | Type A。FUT_NTO 时为 null
+| typeBTotal | 是 | 否 | Type B 合计。FUT_NTO 时为 null
+| typeBAdj | 否 | 是 | Type B 调整后。FUT_NTO 时为 null
+| tradfiX2 | 是 | 否 | TradFi 量（已 ×2）。FUT_NTO 时为 null
+| total | 是 | 是 | 各类型合计。始终存在
+- volume 值：美元名义量，String，保留 2 位小数（如 "1000000.00"）
+- share 值：小数字符串，4 位小数，无 % 后缀（如 "0.0000"）
+GET / 获取 GLP 历史表现
+获取单个 GLP 业务线的逐日表现记录，按日期降序排列（最新日期在前）。
+限速：5次/2s
+限速规则：User ID
+权限：读取
+HTTP请求
+GET /api/v5/users/glp/historical-performance
+请求示例
+GET /api/v5/users/glp/historical-performance?program=SPOT GET /api/v5/users/glp/historical-performance?program=SPOT&begin=1751299200000&end=1753804800000&limit=31
+请求参数
+| 参数名 | 类型 | 是否必须 | 描述
+| program | String | 是 | GLP 业务线标识。
+SPOT
+PERP
+FUT_NTO
+| begin | String | 否 | 开始日期过滤（含）。Unix 毫秒字符串，如 "1751299200000"。默认：当月 1 号（UTC+8）
+| end | String | 否 | 结束日期过滤（含）。Unix 毫秒字符串。默认：今天（UTC+8）
+| limit | String | 否 | 每页最大记录数。默认 "31"，最大 "100"
+返回示例
+{ "code": "0", "msg": "", "data": [ { "date": "2026-07-13", "volume": { "typeA": {"maker": "1000000.00", "taker": "1000000.00"}, "typeBTotal": {"maker": "1000000.00", "taker": "1000000.00"}, "tradfiX2": {"maker": "1000000.00", "taker": "1000000.00"}, "total": {"maker": "2000000.00", "taker": "2000000.00"} }, "share": { "typeA": {"maker": "0.0012", "taker": "0.0010"}, "typeBAdj": {"maker": "0.0008", "taker": "0.0007"}, "total": {"maker": "0.0010", "taker": "0.0009"} } }, { "date": "2026-07-12", "volume": { "typeA": {"maker": "950000.00", "taker": "980000.00"}, "typeBTotal": {"maker": "850000.00", "taker": "900000.00"}, "tradfiX2": {"maker": "800000.00", "taker": "820000.00"}, "total": {"maker": "1800000.00", "taker": "1880000.00"} }, "share": { "typeA": {"maker": "0.0011", "taker": "0.0009"}, "typeBAdj": {"maker": "0.0007", "taker": "0.0006"}, "total": {"maker": "0.0009", "taker": "0.0008"} } } ] }
+返回参数
+| 参数名 | 类型 | 描述
+| date | String | 日期，yyyy-MM-dd 格式（UTC+8）
+| volume | Object | 各池类型的交易量（美元名义，2 位小数）。结构同当日表现接口的 daily.volume
+| share | Object | 各池类型的市场份额（小数字符串，4 位小数，无 % 后缀）。结构同当日表现接口的 daily.share
+错误码
+| 错误码 | HTTP 状态码 | 错误提示
+| 50030 | 200 | 您无权使用此 API 端点
+| 50014 | 200 | 参数 {param0} 不能为空
+| 51000 | 200 | 参数错误
+| 50016 | 200 | 参数 {param0} 与参数 {param1} 不匹配
+FUTURES 和 SWAP 计划委托支持追逐限价委托（Chase Order）
+FUTURES 和 SWAP 计划委托（Trigger Order）现可在触发时下发追逐限价委托（Chase Order）——advanceOrdType 新增取值 chase，其参数由新增数组 advChaseParams 承载。查询接口通过新增字段 subAlgoIdList 返回触发后生成的追逐委托 algoId；在计划委托触发前，可通过改单接口修改追逐值。本期暂不支持追逐委托与附带止盈止损（attachAlgoOrds）同时设置。
+策略委托下单
+- advanceOrdType 新增取值 chase，并新增 advChaseParams 数组；orderPx 变更为条件必填（追逐委托不适用）。
+  - POST / 策略委托下单
+| 参数名 | 类型 | 是否必须 | 描述
+| advanceOrdType | String | 否 | 计划委托的子订单类型。
+fok、ioc 或 chase。
+chase 仅适用于 FUTURES 和 SWAP。
+默认为空（按 orderPx 下发限价或市价单）。
+| orderPx | String | 条件必填 | 计划委托触发时下发订单的价格。-1 表示市价。当 advanceOrdType 为 chase 时不适用（追逐委托无固定价格）。
+| advChaseParams | Array of objects | 条件必填 | 追逐参数。当 advanceOrdType 为 chase 时必填。
+| > chaseType | String | 条件必填 | 追逐距离单位。
+distance（默认）：与买一价/卖一价的绝对价格距离，以结算货币计。
+ratio：百分比。
+| > chaseVal | String | 条件必填 | 追逐值。当 chaseType 为 distance 时，为与买一价/卖一价的距离（以结算货币计）；当 ratio 时，0.1 表示 10%。
+默认值 0 表示直接跟随买一价/卖一价；大于 0 表示设置一个距离。
+| > maxChaseType | String | 条件必填 | 最大追逐距离单位。distance 或 ratio。须与 maxChaseVal 成对出现。
+| > maxChaseVal | String | 条件必填 | 最大追逐距离值。须为正数。须与 maxChaseType 成对出现。当偏离达到该值时，追逐委托自动撤单。
+修改策略委托订单
+- 新增 advChaseParams 改单字段，用于在计划委托挂单期间（触发前）调整追逐值。chaseType、maxChaseType 及追逐价格模式在下单时固定，不可修改。
+  - POST / 修改策略委托订单
+| 参数名 | 类型 | 是否必须 | 描述
+| advChaseParams | Array of objects | 条件必填 | 待修改的追逐参数。仅适用于 advanceOrdType 为 chase 的挂单中计划委托。
+| > newChaseVal | String | 条件必填 | 新的追逐值。非负数，按订单已有（不可修改）的 chaseType 解释。不可越过原 chaseVal 的 0 ↔ 非 0 边界——直接跟随买一价/卖一价（0）与设置距离（大于 0）两种模式不可互换。
+| > newMaxChaseVal | String | 条件必填 | 新的最大追逐距离值。须为正数，按已有（不可修改）的 maxChaseType 解释。仅在已启用最大追逐距离时适用。
+查询接口（委托单信息、委托单列表、WS 频道）
+- 新增返回参数 advanceOrdType（含新取值 chase）、advChaseParams，以及新增的 subAlgoIdList。
+  - GET / 获取策略委托单信息
+  - GET / 获取未完成策略委托单列表
+  - GET / 获取历史策略委托单列表
+  - WS / 策略委托订单频道
+| 参数名 | 类型 | 描述
+| advanceOrdType | String | 计划委托的子订单类型。fok、ioc、chase 或空。
+| advChaseParams | Array of objects | 追逐参数。当 advanceOrdType 为 chase 时返回。
+| > chaseType | String | 追逐距离单位。distance 或 ratio。
+| > chaseVal | String | 追逐值。0 表示直接跟随买一价/卖一价；大于 0 表示距离。
+| > maxChaseType | String | 最大追逐距离单位。distance 或 ratio。
... (diff truncated, total 204 lines) ...
```
