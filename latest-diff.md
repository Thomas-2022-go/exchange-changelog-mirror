<!-- has_changes=true date=2026-07-28 -->
# Exchange API Changelog Diff

Generated: 2026-07-28 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 17 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 43 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3590 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 28 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (35340 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120249 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index ee3af7c..032d2a3 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -1,5 +1,11 @@
 # CHANGELOG for Binance's API
 
-**Last Updated: 2026-07-17**
+**Last Updated: 2026-07-27**
+
+### 2026-07-27
+
+* Updated [Price Range Execution Rule](./faqs/price_range_execution_rules.md#externalCalculationId4) with additional External Reference Price Calculation Methods.
+
+---
 
 ### 2026-07-17

```

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 3873cfd..495698f 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,11 +1,3 @@
 待发布内容
-移除 speedBump 请求参数
-最近更新：2026年7月21日
-事件合约减速带功能的 speedBump 请求参数不再生效。如果客户端仍然发送 speedBump，该参数将被静默忽略，不会产生任何影响。本次变更预计于 2026年7月24日 上线。
-- 在以下接口移除请求参数 speedBump：
-  - POST / 下单
-请求参数
-| 参数名 | 类型 | 描述
-| speedBump | String | 减速带。1：事件合约速度限制（延迟可能因市场情况调整，不提前通知）。
 信号复制新增 API 接口
 最后更新：2026 年 5 月 14 日
@@ -58,5 +50,5 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 其他订单类型如 limit（普通限价单）、market（市价单）、ioc、fok 订单推送行为保持不变。
 ELP 更名为 RPI（散户价格优化）计划
-最近更新：2026年7月20日
+最近更新：2026年7月27日
 OKX 将品牌 Enhanced Liquidity Program（ELP） 更名为 Retail Price Improvement（散户价格优化，RPI）。本次变更包含新的 RPI 合并深度订单簿（books-rpi，同时提供 WebSocket 与 REST）、更名后的挂单类型 rpi（替代 elp）、扩展后的下单参数 rpiTakerAccess（替代 isElpTakerAccess）、用于 RPI 挂单价格间距规则的新参数 rpiPxRound，以及更名后的账户字段 rpi/rpiMaker。预计于 2026年7月23日 在模拟盘上线，并于 2026年7月28日 正式上线。
 ELP 命名弃用截止日期：2026年10月31日
@@ -82,5 +74,5 @@ REST 请求参数：instId（必填）、sz（每侧深度档数，最大 400，
 | rpiTakerAccess | Boolean | 否 | 默认值为 false。
 设为 true 时，订单可使用 RPI 流动性，适用于所有标准订单类型（此前仅 ioc）。
-下单时，除 post_only 外的所有订单类型都会触发减速带机制；改单时，减速带适用于所有订单类型（包括 post_only）。
+当 rpiTakerAccess 为 true 时，减速带机制在下单和改单时均适用于所有 ordType，包括 post_only。
 改单时不会从原始订单继承，必须每次显式指定（省略则该次改单视为 false）。
 挂单类型：rpi（替代 elp）
@@ -118,4 +110,12 @@ RPI 挂单费率字段：rpiMaker（替代 elpMaker）
 - GET /api/v5/market/trades 返回字段 source 取值 1 的说明由"流动性增强计划订单"更新为 RPI 订单（原 ELP 订单）。返回的取值 1 本身不变，仅更新说明文字。
   - GET / 获取交易产品公共成交数据
+2026-07-24
+移除 speedBump 请求参数
+事件合约减速带功能的 speedBump 请求参数不再生效。如果客户端仍然发送 speedBump，该参数将被静默忽略，不会产生任何影响。
+- 在以下接口移除请求参数 speedBump：
+  - POST / 下单
+请求参数
+| 参数名 | 类型 | 描述
+| speedBump | String | 减速带。1：事件合约速度限制（延迟可能因市场情况调整，不提前通知）。
 2026-07-23
 GLP 做市商表现 API

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 4e4dc9c..bd3d854 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,23 @@
+2026-08-04​
+REST API​
+- Self Match Prevention [UPDATE]
+  - Kazakhstan (KAZ) derivatives: SMP is now mandatory for all derivative orders
+  - Turkey (TUR), Kazakhstan (KAZ), Georgia (GEO) spot: smpType of None, invalid value, or missing value is automatically set to CancelMaker
+2026-07-28​
+REST API​
+Spot-X Launchpool — New endpoints
+- Get Launchpool Project List [NEW]
+- Get Launchpool User Activity Log [NEW]
+- Get Launchpool Current Staking [NEW]
+- Get Launchpool User History [NEW]
+Spot-X Puzzle — New endpoints
+- Get Puzzle Project List [NEW]
+Spot-X Token Splash — New endpoints
+- Get Token Splash Project List [NEW]
+- Get Token Splash User Activity Params [NEW]
+2026-07-27​
+REST API​
+- Get Referral Code [NEW]
+  - New endpoint to query the referral codes owned by the current user and their corresponding referral registration links. Sub-accounts return the master account's referral codes
 2026-07-24​
 REST API​

```
