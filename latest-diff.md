<!-- has_changes=true date=2026-07-11 -->
# Exchange API Changelog Diff

Generated: 2026-07-11 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (131907 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 50 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 21 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (34939 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120249 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index f00be15..aa563e0 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,3 +1,45 @@
 待发布内容
+FUTURES 和 SWAP 计划委托支持追逐限价委托（Chase Order）
+最近更新：2026年7月9日
+FUTURES 和 SWAP 计划委托（Trigger Order）现可在触发时下发追逐限价委托（Chase Order）——advanceOrdType 新增取值 chase，其参数由新增数组 advChaseParams 承载。查询接口通过新增字段 subAlgoIdList 返回触发后生成的追逐委托 algoId；在计划委托触发前，可通过改单接口修改追逐值。预计于 2026年7月15日 在模拟盘上线，并于 2026年7月21日 正式上线。
+策略委托下单
+- advanceOrdType 新增取值 chase，并新增 advChaseParams 数组；orderPx 变更为条件必填（追逐委托不适用）。
+  - POST / 策略委托下单
+本期暂不支持追逐委托与附带止盈止损（attachAlgoOrds）同时设置。
+| 参数名 | 类型 | 是否必须 | 描述
+| advanceOrdType | String | 否 | 计划委托触发时下发的订单类型。
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
+| > maxChaseType | String | 最大追逐距离单位。
+| > maxChaseVal | String | 最大追逐距离值。
+| subAlgoIdList | Array of strings | 计划委托触发时生成的策略委托单 algoId。当 advanceOrdType 为 chase 时，在触发后存放生成的追逐委托 algoId，触发前为空。与 ordIdList 对应，后者记录生成的普通订单，对追逐委托始终为空。
 信号复制新增 API 接口
 最后更新：2026 年 5 月 14 日

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index a5ced9b..52425e8 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,16 @@
+2026-07-14​
+REST API​
+- Get Flexible Available Inventory [NEW]
+  - New endpoint to query the flexible available inventory (remaining borrowable amount from the lending pool) for a specified coin in spot margin trading
+- Get Fixed-Rate Available Inventory [NEW]
+  - New endpoint to query the available inventory for fixed-rate borrowing by currency, term, and annual rate
+2026-07-10​
+REST API​
+- Get Deposit Records (on-chain) [UPDATE]
+  - Added a new depositType enum: 50. If a deposit is classified as "depositType" = 50, the funds will not be credited to your account. Instead, you’ll need to log in to the Bybit website and withdraw the funds from there.
+- Get Sub Deposit Records (on-chain) [UPDATE]
+  - Added a new depositType enum: 50. If a deposit is classified as "depositType" = 50, the funds will not be credited to your account. Instead, you’ll need to log in to the Bybit website and withdraw the funds from there.
+- Get Sub Account Deposit Records [UPDATE]
+  - Added a new depositType enum: 50. If a deposit is classified as "depositType" = 50, the funds will not be credited to your account. Instead, you’ll need to log in to the Bybit website and withdraw the funds from there.
 2026-07-06​
 REST API​

```
