<!-- has_changes=true date=2026-07-17 -->
# Exchange API Changelog Diff

Generated: 2026-07-17 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 21 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 58 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 20 diff lines

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 15 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120249 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index d766d64..ee3af7c 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -1,5 +1,15 @@
 # CHANGELOG for Binance's API
 
-**Last Updated: 2026-07-01**
+**Last Updated: 2026-07-17**
+
+### 2026-07-17
+
+The following will occur on **2026-08-04 at approximately 07:00 UTC**.
+
+* The update speed of the below SBE Market Data Streams will be changed **from 25ms to 20ms**:
+  * SBE Market Data Streams: [Diff Depth Streams](sbe-market-data-streams.md#diff-depth-streams)
+  * FIX SBE: [MarketDataIncrementalDepth](fix-api.md#marketdataincrementaldepth)
+
+---
 
 ### 2026-07-01

```

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 96ca45d..cebc4a4 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -64,4 +64,31 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | 参数名 | 类型 | 描述
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
+WebSocket 订单频道推送行为调整
+最近更新：2026 年 7 月 15 日
+为了让客户能够更明确地判断 post-only（包括 mmp_and_post_only）与将要推出的 rpi 新订单的最终状态，避免收到 state: live 后订单仍被撤销的场景，欧易将调整订单频道中 post-only 与 rpi 订单的 state: live 事件行为。
+具体影响
+- state: live 事件的推送时机由订单接收后立即推送，调整为订单成功进入订单簿之后才推送（延后约 1 ms）。
+- 价格穿越 BBO 被撤单的挂单失败场景下，state: live 更新将被完全移除，只推送 state: canceled 更新。
+| 场景 | 调整前 | 调整后
+| post-only 订单挂单失败
+（价格穿越 BBO 被撤单） | state: live → state: canceled | 只推 state: canceled（不再有 state: live）
+| post-only 订单成功挂单 | 立即推 state: live | state: live（延后约 1 ms）
+| post-only 订单成功挂单后被吃单
+（一次成交） | state: live → state: filled | state: live（延后约 1 ms） → state: filled
+| post-only 订单成功挂单后被吃单
+（多次部分成交） | state: live → state: partially_filled → state: filled | state: live（延后约 1 ms） → state: partially_filled → state: filled
+| post-only 订单带 reduceOnly: true，
+size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0） | state: live（amendSource: 4，amendResult: 0） → state: live
+| 将要推出的 rpi 订单，rpiPxRound: false，
+挂单失败
+（不满足价格间距规则被撤单） | N/A | 只推 state: canceled（不会有 state: live）
+| 将要推出的 rpi 订单，rpiPxRound: true，
+并且 price 被修改 | N/A | state: live（amendSource: 6，amendResult: 0） → state: live
+生效时间
+- 对于 rpi 订单：模拟盘 —— 2026 年 7 月 21 日；实盘 —— 2026 年 7 月 28 日。
+- 对于 post_only 和 mmp_and_post_only 订单：模拟盘和实盘均为 2026 年 8 月中旬。
+影响范围
+受影响的订单类型有：post_only、mmp_and_post_only、rpi（Retail Price Improvement）。
+其他订单类型如 limit（普通限价单）、market（市价单）、ioc、fok 订单推送行为保持不变。
 ELP 更名为 RPI（散户价格优化）计划
 最近更新：2026年7月8日
@@ -125,4 +152,21 @@ RPI 挂单费率字段：rpiMaker（替代 elpMaker）
 - GET /api/v5/market/trades 返回字段 source 取值 1 的说明由"流动性增强计划订单"更新为 RPI 订单（原 ELP 订单）。返回的取值 1 本身不变，仅更新说明文字。
   - GET / 获取交易产品公共成交数据
+2026-07-16
+交易产品接口支持 Pre-market X-Perp
+欧易现已支持 Pre-market X-Perp —— 一种在标的代币正式上线前于盘前阶段交易的永续型 FUTURES 合约。Pre-market X-Perp 通过 ruleType = pre_market 与 instType = FUTURES 组合进行标识。当其转换为正常 X-Perp 后，ruleType 变为 xperp，并且 preMktSwTime 会填充为转换时间戳。
+- 以下接口扩展为返回 Pre-market X-Perp 合约（通过 instType=FUTURES 查询）：
+  - GET / 获取交易产品基础信息（public）
+  - GET / 获取交易产品基础信息（private）
+  - WS / 产品频道
+- 扩展以下响应参数的适用范围：
+| 参数名 | 类型 | 描述
+| ruleType | String | 交易规则类型。
+normal
+pre_market：盘前交易产品（含 Pre-market X-Perp FUTURES）
+rebase_contract
+xperp
+Pre-market X-Perp 在盘前阶段返回 pre_market，转换为正常 X-Perp 后变为 xperp。
+| preMktSwTime | String | 盘前交易产品切换为正常交易的时间，Unix 时间戳，单位为毫秒。
+仅适用于盘前 SWAP 与 Pre-market X-Perp FUTURES。当 Pre-market X-Perp 转换为正常 X-Perp 时填充。
 2026-07-14
 Stable Rewards 询价、下单及历史记录接口下线

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 52425e8..f1671a7 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,15 @@
+2026-07-16​
+REST API​
+- Get Full Depth Orderbook [NEW]
+  - You can get up to 10,000 depths per side (Spot)
+- Get Deposit Records (on-chain) [UPDATE]
+  - Added new depositStatus values, 7, 70011, 70012, 70013. For details on each status, please refer to Deposit Status enum definitions⁠
+- Get Sub Deposit Records (on-chain) [UPDATE]
+  - Added new depositStatus values, 7, 70011, 70012, 70013. For details on each status, please refer to Deposit Status enum definitions⁠
+- Get Sub Account Deposit Records [UPDATE]
+  - Added new depositStatus values, 7, 70011, 70012, 70013. For details on each status, please refer to Deposit Status enum definitions⁠
+Websocket API​
+- Full Orderbook [NEW]
+  - You can subscribe full depths orderbook channel (Spot)
 2026-07-14​
 REST API​

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index a570dbe..077ec0b 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,4 +1,10 @@
 WARNING
 The Pro API is currently in beta testing and should not be used in production trading environments.
+2026.07.17#
+[Modify] UTA REST/WebSocket Get Order Book & Subscription
+The system automatically identifies call auction status based on the symbol field and returns relevant order book data.
+[Add] UTA REST Get Interest Rate Index
+[Add] UTA REST Platform 24h Market Statistics
+[Add] UTA REST/WS Get Call Auction Info & Subscription supports querying details such as the price range during call auction.
 2026.07.01#
 [Add] UTA REST Get Client IP Address

```
