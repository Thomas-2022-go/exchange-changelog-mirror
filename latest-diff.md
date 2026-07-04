<!-- has_changes=true date=2026-07-04 -->
# Exchange API Changelog Diff

Generated: 2026-07-04 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (131907 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (89162 bytes)

- [CHANGED] **OKX V5** (`okx`): 126 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (83441 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (34939 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120249 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 3dcd09b..956f418 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,91 +1,3 @@
 待发布内容
-交易产品价格限制 XYZ 参数
-最近更新：2026年6月23日
-为方便 API 用户动态获取合约价格限制参数而无需硬编码，OKX 现通过交易产品基础信息接口公开价格限制 X、Y、Z 参数。由这些参数推算出的价格限制可通过 GET / 获取限价 获取。详情参阅价格限制规则。本次变更预计于 2026年6月24日 在模拟盘上线，并于 2026年6月30日 正式上线。
-- 在以下接口新增返回参数 initPxLmtPct、floatPxLmtPct、maxPxLmtPct：
-  - GET / 获取交易产品基础信息（公共）
-  - GET / 获取交易产品基础信息（私有）
-返回参数
-| 参数名 | 类型 | 描述
-| initPxLmtPct | String | 合约上线后前 10 分钟内的初始价格限制区间，小数百分比，例如 0.05 = 5%。
-适用于 SPOT/MARGIN/SWAP/FUTURES；OPTION 和 EVENTS 返回 ""。
-| floatPxLmtPct | String | 常规交易期间的浮动价格限制区间，小数百分比，例如 0.03 = 3%。
-适用于 SPOT/MARGIN/SWAP/FUTURES；OPTION 和 EVENTS 返回 ""。
-| maxPxLmtPct | String | 最大价格限制上限（硬性上限），小数百分比，例如 0.15 = 15%。
-适用于 SPOT/MARGIN/SWAP/FUTURES；OPTION 和 EVENTS 返回 ""。
-OKUSD 申购、赎回与限额 — 新增 API 接口
-最近更新：2026年6月23日
-OKX 现新增 OKUSD 的 V5 API 支持。API 用户可通过接口以 1:1 汇率将 USDT 申购为 OKUSD、通过即时赎回（实时到账）或标准赎回（D+5 工作日）将 OKUSD 赎回为 USDT，并查询当日剩余申购及赎回限额。此变更预计将于 2026年7月2日 上线。
-获取 OKUSD 限额
-- 新增 GET /api/v5/finance/okusd/limits
-需要具有 read 权限的 API Key。频率限制：每 UID 每 2 秒 2 次请求。
-返回参数
-| 参数名 | 类型 | 描述
-| subLimit | Object | 申购限额信息
-| > maxSubAmt | String | 当日最大可申购数量（USDT），= min(personalDailyLimit - personalUsedAmt, platformDailyLimit - platformUsedAmt)
-| > personalDailyLimit | String | 用户 VIP 等级对应的每日申购上限（USDT）
-| > personalUsedAmt | String | 用户当日已申购金额（USDT）
-| > platformDailyLimit | String | 平台每日申购总上限（USDT）
-| > platformUsedAmt | String | 平台当日已申购金额（USDT）
-| fastRedeemLimit | Object | 即时赎回限额信息
-| > personalDailyLimit | String | 用户 VIP 等级对应每日即时赎回上限（OKUSD）
-| > personalUsedAmt | String | 用户当日已使用即时赎回额度（OKUSD）
-| > platformDailyLimit | String | 平台每日即时赎回总上限（OKUSD）
-| > platformUsedAmt | String | 平台当日已使用即时赎回额度（OKUSD）
-| > feeRate | String | 即时赎回手续费率，小数格式（如 "0.001" 表示 0.1%）
-| stdRedeemLimit | Object | 标准赎回（D+5）限额信息
-| > personalDailyLimit | String | 用户 VIP 等级对应每日标准赎回上限（OKUSD）
-| > personalUsedAmt | String | 用户当日已使用标准赎回额度（OKUSD）
-| > platformDailyLimit | String | 平台每日标准赎回总上限（OKUSD）
-| > platformUsedAmt | String | 平台当日已使用标准赎回额度（OKUSD）
-| > feeRate | String | 标准赎回手续费率，小数格式（如 "0.00025" 表示 0.025%）
-| ts | String | 服务器时间戳（Unix 毫秒）
-申购 OKUSD
-- 新增 POST /api/v5/finance/okusd/subscribe
-需要具有 trade 权限的 API Key。频率限制：每 UID 每 2 秒 1 次请求。
-请求参数
-| 参数名 | 类型 | 必填 | 描述
-| amt | String | 是 | 申购 USDT 数量。最小值：1。最多 8 位小数。
-返回参数
-| 参数名 | 类型 | 描述
-| ordId | String | 系统订单 ID
-| ccy | String | 申购货币，固定为 "USDT"
-| amt | String | 实际申购 USDT 数量
-| okusdAmt | String | 到账 OKUSD 数量（等于 amt，汇率 1:1，无申购手续费）
-| state | String | 订单状态：success / pending / failed
-| ts | String | 订单创建时间（Unix 毫秒）
-赎回 OKUSD
-- 新增 POST /api/v5/finance/okusd/redeem
-需要具有 trade 权限的 API Key。频率限制：每 UID 每 2 秒 1 次请求。
-即时赎回实时到账；标准赎回最长 D+5 工作日到账。
-请求参数
-| 参数名 | 类型 | 必填 | 描述
-| amt | String | 是 | 赎回 OKUSD 数量。最小值：1。最多 8 位小数。
-| redeemType | String | 是 | 赎回类型。1 = 即时赎回（实时到账）；2 = 标准赎回（D+5）
-返回参数
-| 参数名 | 类型 | 描述
-| ordId | String | 系统订单 ID
-| ccy | String | 赎回货币，固定为 "OKUSD"
-| amt | String | 赎回 OKUSD 数量
-| fee | String | 实收手续费（USDT），向下截断至 8 位小数
-| usdtAmt | String | 实际到账 USDT 数量 = amt - fee，向下截断至 8 位小数
-| redeemType | String | 赎回类型：1 = 即时赎回；2 = 标准赎回
-| state | String | 订单状态：processing / success / failed
-| estSettlementTime | String | 预计到账时间（Unix 毫秒）。即时赎回为当前时间；标准赎回为提交时间 + 5 工作日
-| ts | String | 订单创建时间（Unix 毫秒）
-- 新增错误码
-| 错误码 | HTTP 状态码 | 错误提示
-| 51763 | 200 | 您的账户不满足该产品的 VIP 等级准入要求
-| 51764 | 200 | 余额不足
-| 51765 | 200 | 超出您当日剩余配额 {x} USDT
-| 51766 | 200 | 平台当日申购限额已达上限
-| 51767 | 200 | 系统维护中，请稍后重试
-| 51768 | 200 | 超出您当日剩余即时赎回配额 {x} OKUSD
-| 51769 | 200 | 平台即时赎回限额已达上限
-| 51770 | 200 | 超出您当日剩余标准赎回配额 {x} OKUSD
-| 51771 | 200 | 平台标准赎回限额已达上限
-| 51772 | 200 | 即时赎回池余额不足
-| 51773 | 200 | 该功能在您所在地区暂不可用
-| 51774 | 200 | OKUSD API 正在维护中
 信号复制新增 API 接口
 最后更新：2026 年 5 月 14 日
@@ -173,4 +85,29 @@ OKX 将合约冷静期从仅前端 UI 拦截扩展至所有下单渠道，包括
 | 错误码 | HTTP 状态码 | 错误信息
 | 54094 | 200 | 下单失败，当前交易产品处于冷静期内，暂不支持下单。
+2026-07-03
+MM 币对分类类型
+获取当前做市商（MM）计划 SPOT 和 SWAP 产品的币对分类类型列表。
+- 新增接口：
+  - GET / 获取 MM 币对分类类型
+OKUSD 申购、赎回与限额 — 新增 API 接口
+OKX 现已新增 OKUSD 的 V5 API 支持。API 用户可通过接口以 1:1 汇率将 USDT 申购为 OKUSD、通过即时赎回（实时到账）或标准赎回（D+5 或 D+6 自然日，取决于提交时间）将 OKUSD 赎回为 USDT，并查询当日剩余申购及赎回限额。
+- 新增以下接口：
+  - GET / 查询限额
+  - POST / 申购 OKUSD
+  - POST / 赎回 OKUSD
+- 新增错误码 51763-51774，涉及 OKUSD 申购与赎回：
+  - 错误码 / 金融
+2026-06-30
+交易产品价格限制 XYZ 参数
+- 在以下接口新增返回参数 initPxLmtPct、floatPxLmtPct、maxPxLmtPct：
+  - GET / 获取交易产品基础信息（公共）
+  - GET / 获取交易产品基础信息（私有）
+| 参数名 | 类型 | 描述
+| initPxLmtPct | String | 合约上线后前 10 分钟内的初始价格限制区间，小数百分比，例如 0.05 代表 5%。通过 GET /api/v5/public/price-limit 可获取对应价格限制。
+适用于 SPOT/MARGIN/SWAP/FUTURES；OPTION 和 EVENTS 返回 ""。
+| floatPxLmtPct | String | 常规交易期间的浮动价格限制区间，小数百分比，例如 0.03 代表 3%。通过 GET /api/v5/public/price-limit 可获取对应价格限制。
+适用于 SPOT/MARGIN/SWAP/FUTURES；OPTION 和 EVENTS 返回 ""。
+| maxPxLmtPct | String | 最大价格限制上限（下单价格相对指数价格偏离的硬性上限），小数百分比，例如 0.15 代表 15%。通过 GET /api/v5/public/price-limit 可获取对应价格限制。
+适用于 SPOT/MARGIN/SWAP/FUTURES；OPTION 和 EVENTS 返回 ""。
 2026-06-23
 深度频道 checksum 字段废弃

```
