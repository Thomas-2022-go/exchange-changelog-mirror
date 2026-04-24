<!-- has_changes=true date=2026-04-24 -->
# Exchange API Changelog Diff

Generated: 2026-04-24 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (126374 bytes)

- [CHANGED] **Binance Derivatives (USDS-M / Coin-M / Options)** (`binance-derivatives`): 276 diff lines

- [CHANGED] **OKX V5** (`okx`): 376 diff lines

- [CHANGED] **Bitget (Spot + Futures)** (`bitget`): 730 diff lines

- [CHANGED] **Bybit V5** (`bybit`): 682 diff lines

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 625 diff lines

- [CHANGED] **Gate.io Spot WebSocket v4** (`gate-spot-ws`): 10 diff lines

- [CHANGED] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): 10 diff lines



## Changes

### Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`)
- Source: https://developers.binance.com/docs/derivatives/change-log
- Raw: https://developers.binance.com/docs/derivatives/change-log

```diff
diff --git a/changelogs/binance-derivatives.txt b/changelogs/binance-derivatives.txt
index 660cd1d..33992cf 100644
--- a/changelogs/binance-derivatives.txt
+++ b/changelogs/binance-derivatives.txt
@@ -1,23 +1,2 @@
-Change Log | Binance Open Platform
-Skip to main content
-Products
-▼
-Search
-Current
-All
-English
-English
-简体中文
-Derivatives Trading
-Change Log
-Introduction
-Quick Start
-USDⓈ-M Futures
-COIN-M Futures
-Portfolio Margin
-Portfolio Margin Pro
-Options Trading
-Change Log
-On this page
 Change Log
 2026-04-17
@@ -3416,247 +3395,2 @@ New order type
 TAKE_PROFIT
 .
-Next
-Introduction
-2026-04-17
-2026-04-15
-2026-04-14
-2026-04-13
-2026-04-10
-2026-04-09
-2026-04-08
-2026-04-06
-2026-04-02
-2026-03-19
-2026-03-16
-2026-03-11
-2026-03-05
-2026-01-09
-2026-01-07
-2025-12-29
-2025-12-11
-2025-12-10
-2025-12-09
-2025-11-25
-2025-11-19
-2025-11-18
-2025-11-12
-2025-11-10
-2025-11-06
-2025-10-21
-2025-10-20
-2025-10-14
-2025-10-09
-2025-08-11
-2025-07-25
-2025-07-02
-2025-04-23
-2025-04-15
-2025-02-28
-2025-02-20
-2025-01-20
-2025-01-13
-2025-01-06
-2024-12-19
-2024-12-17
-2024-12-02
-2024-11-04
-2024-11-01
-2024-10-29
-2024-10-24
-2024-10-21
-2024-10-15
-2024-10-14
-2024-10-11
-2024-10-10
-2024-10-08
-2024-09-27
-2024-09-19
-2024-09-06
-2024-09-05
-2024-09-03
-2024-08-26
-2024-08-23
-2024-08-07
-2024-08-06
-2024-07-24
-2024-07-17
-2024-06-19
-2024-05-22
-2024-04-19
-2024-04-09
-2024-04-01
-2024-03-11
-2024-02-09
-2024-01-24
-2024-01-19
-2024-01-11
-2024-01-08
-2023-12-12
-2023-11-15
-2023-11-01
-2023-11-01
-2023-10-19
-2023-10-19
-2023-10-19
-2023-10-16
-2023-10-16
-2023-10-11
-2023-09-25
-2023-09-25
-2023-09-22
-2023-09-20
-2023-09-20
-2023-09-19
-2023-09-07
-2023-09-05
-2023-09-04
-2023-08-31
-2023-08-31
-2023-08-29
-2023-08-29
-2023-08-25
-2023-08-19
-2023-08-18
-2023-08-14
-2023-08-14
-2023-07-28
-2023-07-21
-2023-07-20
-2023-07-19
-2023-07-18
-2023-07-18
-2023-07-13
-2023-07-13
-2023-07-12
-2023-07-11
-2023-07-04
-2023-06-28
-2023-06-22
-2023-06-22
-2023-06-19
-2023-06-16
-2023-06-14
-2023-06-14
-2023-06-01
-2023-05-31
-2023-05-30
-2023-05-05
-2023-05-04
-2023-04-17
-2023-04-17
-2023-03-28
-2023-03-08
-2023-02-02
-2023-01-11
-2023-01-04
-2022-12-16
-2022-12-16
-2022-12-13
-2022-12-09
-2022-11-29
-2022-11-29
-2022-11-18
-2022-11-16
-2022-11-03
-2022-10-13
-2022-10-13
-2022-09-22
-2022-09-22
-2022-09-20
-2022-09-14
-2022-09-05
-2022-08-22
-2022-07-27
-2022-07-27
-2022-06-28
-2022-06-28
-2022-04-28
-2022-04-14
-2022-03-01
-2022-02-18
-2022-02-10
-2021-12-30
-2021-11-02
-2021-08-18
-2021-08-17
-2021-07-23
-2021-07-06
-2021-07-06
-2021-06-15
-2021-05-06
... (diff truncated, total 276 lines) ...
```

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 62b0613..2f7f12d 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,16 +1,4 @@
 欧易 API接入指南 | 欧易技术对接 | 欧易
--->
 导航
-API接口
-🔥 Agent
-Broker接入
-最佳实践
-更新日志
-API接口
-Agent
-Broker接入
-最佳实践
-更新日志
-English
 待发布内容
 大宗商品产品
@@ -1813,5 +1801,4 @@ instIdCode
 instId
 。
-附带止盈止损支持动态涨跌幅（%）功能已上线实盘
 新增请求参数：
 POST / 下单
@@ -4481,6 +4468,4 @@ Boolean
 持仓频道
 账户余额和持仓频道
-开仓均价
-会随结算周期变化，特别是在交割合约全仓模式下，结算时开仓均价会更新为结算价格，同时新增头寸也会改变开仓均价。
 参数名
 类型
@@ -4747,6 +4732,4 @@ String
 2025-01-17
 组合保证金账户模式的保证金计算规则升级
-风险提示
-新的保证金计算规则会对您的账户风险率产生影响，请根据您的交易情况管理账户风险。
 为了提供更好的交易服务，欧易将升级组合保证金账户模式的保证金计算规则。
 详情见
@@ -5011,11 +4994,4 @@ websocket服务升级断线提示
 notice
 )。在推送服务升级前30秒会推送如下信息，告知用户WebSocket服务即将升级，请重新建立新的连接避免由于断线对用户造成的影响。
-推送示例
-{
-"event": "notice",
-"code": "64008",
-"msg": "The connection will soon be closed for a service upgrade. Please reconnect.",
-"connId": "a4d3ae55"
-}
 目前支持WebSocket公共频道(/ws/v5/public)和私有频道(/ws/v5/private)。
 2024-12-16
@@ -5622,5 +5598,4 @@ String
 闪兑相关接口调整
 闪兑
-闪兑结算从资金账户调整为交易账户。即闪兑资金来源从资金账户可用资产调整为交易账户可用资产，闪兑得到的资产也只存在于交易账户。
 新增错误码
 错误码
@@ -5710,5 +5685,4 @@ String
 ：一键还债卖出
 小额资产兑换
-原接口已下线，推荐使用 "一键兑换主流币"。
 接口下线
 小额资产兑换
@@ -5751,6 +5725,4 @@ String
 ：托管交易子账户 - Komainu
 2024-10-14
-现货模式支持借币
-更多详情参考：https://www.okx.com/zh-hans/help/borrow-in-spot-mode
 新增接口
 手动借/还币
@@ -6439,68 +6411,6 @@ rcvrFirstName
 rcvrLastName
 可以填"N/A"，地址信息可以填写公司注册地址。示例如下：
-链上提币到交易所钱包
-POST /api/v5/asset/withdrawal
-body
-{
-"amt":"1",
-"fee":"0.0005",
-"dest":"4",
-"ccy":"BTC",
-"chain":"BTC-Bitcoin",
-"toAddr":"17DKe3kkkkiiiiTvAKKi2vMPbm1Bz3CMKw",
-"rcvrInfo":{
-"walletType":"exchange",
-"exchId":"did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1",
-"rcvrFirstName":"Bruce",
-"rcvrLastName":"Wayne",
-"rcvrCountry":"United States",
-"rcvrCountrySubDivision":"California",
-"rcvrTownName":"San Jose",
-"rcvrStreetName":"Clementi Avenue 1"
-}
-}
-闪电网络提币到交易所钱包
-POST /api/v5/asset/withdrawal-lightning
-body
-{
-"invoice":"lnbc100u1psnnvhtpp5yq2x3q5hhrzsuxpwx7ptphwzc4k4wk0j3stp0099968m44cyjg9sdqqcqzpgxqzjcsp5hz",
-"ccy":"BTC",
-"rcvrInfo":{
-"walletType":"exchange",
-"exchId":"did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1",
-"rcvrFirstName":"Bruce",
-"rcvrLastName":"Wayne",
-"rcvrCountry":"United States",
-"rcvrCountrySubDivision":"California",
-"rcvrTownName":"San Jose",
-"rcvrStreetName":"Clementi Avenue 1"
-}
-}
 用户提币到私人钱包
 如果用户提币到私人钱包，不需要提供接收方信息。示例如下：
-链上提币到交易所钱包
-POST /api/v5/asset/withdrawal
-body
-{
-"amt":"1",
-"fee":"0.0005",
-"dest":"4",
-"ccy":"BTC",
-"chain":"BTC-Bitcoin",
-"toAddr":"17DKe3kkkkiiiiTvAKKi2vMPbm1Bz3CMKw",
-"rcvrInfo":{
-"walletType":"private"
-}
-}
-闪电网络提币到交易所钱包
-POST /api/v5/asset/withdrawal-lightning
-body
-{
-"invoice":"lnbc100u1psnnvhtpp5yq2x3q5hhrzsuxpwx7ptphwzc4k4wk0j3stp0099968m44cyjg9sdqqcqzpgxqzjcsp5hz",
-"ccy":"BTC",
-"rcvrInfo":{
-"walletType":"private"
-}
-}
 新增错误码
 当巴哈马主体用户没有传入新参数
@@ -6701,7 +6611,4 @@ String
 0.3
 2024-07-04
-如下调整可能会影响API提币
-2024年7月4日 15:00 (UTC+8) 起，欧易提币地址簿中现有的免验证地址的验证状态将在 30 天后过期。过期后的免认证地址将不会被允许通过API提币。
-详细内容见公告: https://www.okx.com/zh-hans/help/okx-introduces-30-day-verification-for-withdrawal-address-book
 2024-07-03
 新增参数枚举值
@@ -6771,5 +6678,4 @@ HTTP 状态码
 固定单个连接、交易产品维度不同深度频道的数据推送顺序。调整后，单个连接、交易产品维度，深度频道的推送顺序将被固定为：bbo-tbt -> books-l2-tbt -> books50-l2-tbt -> books -> books5。
 WS / 深度频道
-为了整体上更好的使用体验, Open API 已在实盘限制跟单功能, 详情如下
 仅支持白名单用户使用跟单功能，带单功能不受影响。
 首次跟单设置
@@ -6956,6 +6862,4 @@ String
 String
 24小时交易量，单元为交易货币或美元
-vol24h
-对于现货/U本位合约价差交易产品，以及U本位合约价差交易产品，交易量以交易货币为单位；对于币本位合约价差交易产品，交易量以USD为单位。
 2024-05-08
 新增接口
@@ -7668,5 +7572,4 @@ quick_margin
 GET / 获取账户限速
 2024-02-06
-已上线模拟盘，预计 2024/02/28 上线实盘
 新增接口
 仓位创建器
@@ -7790,5 +7693,4 @@ String
 合约模式
 2024-01-17
-Open API 已在实盘支持合约带单功能（仅支持 ND 子账号使用）
 新增接口和频道
 带单申请
@@ -7940,5 +7842,4 @@ tradeId
 请注意：爆仓或自动减仓后，仓位对应的tradeId将被设置为"0"。通过查询或推送，用户将收到"tradeId": "0"，直至该仓位有新的成交。
 2024-01-15
-已上线模拟盘，预计 2024/01/18 上线实盘
 新增返回参数
 查看账户余额
@@ -8263,5 +8164,4 @@ serviceType
 ：跟单交易
 2023-11-30
-Open API 已在实盘支持合约跟单功能
 新增接口和频道
 首次跟单设置
@@ -8602,5 +8502,4 @@ HTTP 状态码
 单笔订单价值不能超过 {maxOrderValue} USD
 2023-11-10
-现货带单功能已在实盘开放
 当前仅白名单用户可使用，将于11月中旬开放该功能
 新增请求参数枚举值：
@@ -8790,5 +8689,4 @@ String
 ,
 期权
-分批止盈功能已上线实盘
 对于下单和改单，原有附带止盈止损的参数会从文档上隐藏，建议使用新的参数。
 新增请求参数：
@@ -9268,5 +9166,4 @@ String
 String
... (diff truncated, total 376 lines) ...
```

### Bitget (Spot + Futures) (`bitget`)
- Source: https://www.bitget.com/api-doc/common/changelog
- Raw: https://www.bitget.fit/api-doc/common/changelog

```diff
diff --git a/changelogs/bitget.txt b/changelogs/bitget.txt
index 80f2feb..1b34441 100644
--- a/changelogs/bitget.txt
+++ b/changelogs/bitget.txt
@@ -1,42 +1,4 @@
-Changelog | Bitget API
-Skip to main content
-Common
-Spot
-Futures
-Broker
-Affiliate
-Margin
-Copy Trading
-Earn
-Inst Loan
-UTA
-English
-English
-简体中文
-Bitget API Introduction
-V2 API Update Guide
 Changelog
-Quick Start
-FAQ
-SDK
-Signature
-Signature Sample
-Websocket API
-Notice
-API Domain
-Public
-Tax
-Demo Trading
-P2P
-Trading Insights
-Virtual Subaccount
-Assets
-Convert
-BGB-Convert
-Changelog
-On this page
-Changelog
-[January 29, 2026]
-Transfer Records Enable idLessThan Pagination Mode
+[January 29, 2026] Transfer Records Enable idLessThan Pagination Mode
 ​
 Interface:
@@ -44,11 +6,9 @@ Interface:
 Changes：
 Enabled idLessThan pagination mode for retrieving transfer records; deprecated pageNum.
-[January 7, 2026]
-Optimization of Push Frequency for Websocket Order Book Channel (books1) in Classic Account (v2)
+[January 7, 2026] Optimization of Push Frequency for Websocket Order Book Channel (books1) in Classic Account (v2)
 ​
 Websocket: Order Book Channel
 Adjustment Content: The push frequency of the order book channel (books1) is optimized to 10ms.
-[January 6, 2026]
-Added 'off_close' (Delisting Liquidation) to the enum values of the response parameter 'orderSource'.
+[January 6, 2026] Added 'off_close' (Delisting Liquidation) to the enum values of the response parameter 'orderSource'.
 ​
 Interface:
@@ -56,6 +16,5 @@ Interface:
 Changes：
 Added 'off_close' (Delisting Liquidation) to the enum values of the response parameter 'orderSource'.
-[November 27, 2025]
-A new return field, 'liqPrice', has been added to the futures historical order.
+[November 27, 2025] A new return field, 'liqPrice', has been added to the futures historical order.
 ​
 Interface:
@@ -63,15 +22,12 @@ Interface:
 Changes：
 A new return field, 'liqPrice', has been added to the futures historical order.
-[November 26, 2025]
-Websocket Added new ADL notification channel
+[November 26, 2025] Websocket Added new ADL notification channel
 ​
 Websocket: ADL notification channel
 Changes: Websocket Added new ADL notification channel
-[November 26, 2025]
-Add new FAQ Q15
+[November 26, 2025] Add new FAQ Q15
 ​
 Changes:Add new FAQ Q15
-[November 19, 2025]
-New isRwa Field Added to Get Contract Information API Response
+[November 19, 2025] New isRwa Field Added to Get Contract Information API Response
 ​
 Interface:
@@ -81,16 +37,13 @@ New
 isRwa
 Field Added to Get Contract Information API Response
-[November 8, 2025]
-WebSocket has added a new futures equity channel.
+[November 8, 2025] WebSocket has added a new futures equity channel.
 ​
 Websocket: futures equity channel
 Changes: WebSocket has added a new futures equity channel.
-[November 8, 2025]
-WebSocket Supports Broker API Code
+[November 8, 2025] WebSocket Supports Broker API Code
 ​
 Websocket: place order channel
 Changes: The order placement channel supports passing the Broker API Code to receive rebates.
-[November 7, 2025]
-Add Maximum Openable Quantity API
+[November 7, 2025] Add Maximum Openable Quantity API
 ​
 Interface:
@@ -98,6 +51,5 @@ Interface:
 Changes：
 Add Maximum Openable Quantity API
-[November 7, 2025]
-Add Estimated Liquidation Price API
+[November 7, 2025] Add Estimated Liquidation Price API
 ​
 Interface:
@@ -105,6 +57,5 @@ Interface:
 Changes：
 Add Estimated Liquidation Price API
-[November 6, 2025]
-New broker commission inquiry interface added
+[November 6, 2025] New broker commission inquiry interface added
 ​
 Interface:
@@ -114,12 +65,10 @@ Interface:
 Changes：
 New broker commission inquiry interface added
-[October 21, 2025]
-Add an endpoint for querying symbol with isolated margin mode in futures.
+[October 21, 2025] Add an endpoint for querying symbol with isolated margin mode in futures.
 ​
 Interface: /api/v2/mix/account/isolated-symbols
 Changes：
 Add an endpoint for querying symbol with isolated margin mode in futures.
-[October 21, 2025]
-Optimization of the spot historical plan order endpoint
+[October 21, 2025] Optimization of the spot historical plan order endpoint
 ​
 Interface: /api/v2/spot/trade/history-plan-order
@@ -132,6 +81,5 @@ startTime
 endTime
 are changed to optional.
-[October 14, 2025]
-Notice: Classic Account Error Code Optimization
+[October 14, 2025] Notice: Classic Account Error Code Optimization
 ​
 Scope of Impact:
@@ -140,6 +88,5 @@ Optimization Content:
 Unified error code mapping: Resolves the issue where "different error codes correspond to the same error message", ensuring one code maps to one message and reducing recognition confusion.
 Standardized error message matching: Fixes the problem where "different error messages correspond to the same error code", enabling accurate matching between messages and codes and improving troubleshooting efficiency.
-[September 11, 2025]
-Newly Added Interfaces Related to union Margin
+[September 11, 2025] Newly Added Interfaces Related to union Margin
 ​
 Changes：
@@ -160,6 +107,5 @@ Newly Added — New
 assetMode
 (Account Mode) parameter in the WS Position Channel
-[September 4, 2025]
-Notice: Adjustment to the transferId field in the sub-main account transfer records retrieval function. The transferId will be updated to the one returned during sub-main account transfers.
+[September 4, 2025] Notice: Adjustment to the transferId field in the sub-main account transfer records retrieval function. The transferId will be updated to the one returned during sub-main account transfers.
 ​
 Interface: /api/v2/spot/account/sub-main-trans-record
@@ -167,46 +113,38 @@ Changes：
 Previous generation rule: for transferId: Auto-incrementing ID
 New generation rule: for transferId: Snowflake algorithm
-[September 2, 2025]
-Add reason field for Get Upgrade Status
+[September 2, 2025] Add reason field for Get Upgrade Status
 ​
 Interface: /api/v2/spot/account/upgrade-status
 Changes：
 Add reason field for Get Upgrade Status
-[August 28, 2025]
-Notice: Optimization of Push Frequency for Websocket Order Book Channel (books1) in Classic Account (v2)
+[August 28, 2025] Notice: Optimization of Push Frequency for Websocket Order Book Channel (books1) in Classic Account (v2)
 ​
 Websocket: Order Book Channel
 Adjustment Content: The push frequency of the order book channel (books1) is optimized to 20ms. The symbols for this optimization are: BTCUSDT, ETHUSDT, XRPUSDT, SOLUSDT, SUIUSDT, DOGEUSDT, ADAUSDT, PEPEUSDT, LINKUSDT, HBARUSDT
-[August 11, 2025]
-Agent commission API query supports fee deduction
+[August 11, 2025] Agent commission API query supports fee deduction
 ​
 Interface：/api/broker/v1/agent/commission-distribution;/api/broker/v1/agent/customer-commissions;
 Changes：
 Agent commission API query supports fee deduction details
-[August 11, 2025]
-API Global rate Limit Adjustment
+[August 11, 2025] API Global rate Limit Adjustment
 ​
 Changes：
 There is an overall rate limit rule of 6,000 times per IP per minute. After the rate limit is triggered, the recovery time is adjusted from 1 minute to 5 minutes.
-[August 6, 2025]
-Add unrealizedPL field for sub-account futures asset info
+[August 6, 2025] Add unrealizedPL field for sub-account futures asset info
 ​
 Interface：/api/v2/broker/account/subaccount-future-assets
 Changes：
 Add unrealizedPL field for sub-account futures asset info
... (diff truncated, total 730 lines) ...
```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index f8516aa..71c6d19 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,24 +1,2 @@
-V5 | Bybit API Documentation
-Skip to main content
-V5 API
-P2P Trading
-Bybit Pay
-Tax API V3
-Extras
-Pilot Features
-Changelog
-API Explorer
-FAQ
-Self Match Prevention
-How To Start Copy Trading
-DMM Listing
-English
-English
-中文（台灣）
-Search
-V5
-V5
-On this page
-V5
 2026-04-23
 ​
@@ -105,6 +83,5 @@ for Bybit Turkey site users
 REST API
 ​
-Bybit Card adds new endpoints
-[NEW]
+Bybit Card adds new endpoints [NEW]
 Query Asset Records
 [NEW]
@@ -123,10 +100,8 @@ Query Cashback Detail
 REST API
 ​
-Earn adds new produc
-[UPDATE]
+Earn adds new produc [UPDATE]
 Fixed Saving
 [NEW]
-Advanced-Earn adds new product
-[UPDATE]
+Advanced-Earn adds new product [UPDATE]
 Discount Buy
 [NEW]
@@ -135,6 +110,5 @@ Discount Buy
 REST API
 ​
-Advanced-Earn adds new product
-[UPDATE]
+Advanced-Earn adds new product [UPDATE]
 Liquidity Mining
 [NEW]
@@ -190,6 +164,5 @@ remains available during the transition period
 REST API
 ​
-Support a new earn product
-[UPDATE]
+Support a new earn product [UPDATE]
 BYUSDT
 [NEW]
@@ -198,6 +171,5 @@ BYUSDT
 REST API
 ​
-Advanced-Earn adds two new products
-[UPDATE]
+Advanced-Earn adds two new products [UPDATE]
 Smart Leverage
 [NEW]
@@ -883,10 +855,8 @@ and the
 help centre
 for details.
-Earn API
-[NEW]
+Earn API [NEW]
 Get Yield History
 Get Hourly Yield History
-Earn API
-[UPDATE]
+Earn API [UPDATE]
 Get Stake/Redeem Order History
 Add request parameters
@@ -911,14 +881,7 @@ slippageTolerance
 has been adjusted, where:
 TickSize
-has changed from
-[5, 2000]
-to
-[1, 10000]
-,
+has changed from [5, 2000] to [1, 10000],
 Percent
-has changed from
-[0.05, 1]
-to
-[0.01, 10]
+has changed from [0.05, 1] to [0.01, 10]
 Get Instruments Info
 [UPDATE]
@@ -1780,6 +1743,5 @@ request
 REST API
 ​
-Earn API
-[NEW]
+Earn API [NEW]
 Get Product Info
 Stake / Redeem
@@ -1791,6 +1753,5 @@ All Liquidation
 [NEW]
 A new topic to get full liquidation occurred in Bybit exchange.
-Liquidation
-[DEPRECATE]
+Liquidation [DEPRECATE]
 The old one only pushes 1 liquidation per second, it can be discarded.
 2025-02-19
@@ -2099,6 +2060,5 @@ REST API
 ​
 Crypto Loan
-APIs are released to production
-[NEW]
+APIs are released to production [NEW]
 2024-09-29
 ​
@@ -3754,9 +3714,5 @@ Add a new API to get server time
 Set Disconnect Cancel All
 [Option]
-Expand configurable disconnection window time from
-[10, 300]
-to
-[3, 300]
-seconds
+Expand configurable disconnection window time from [10, 300] to [3, 300] seconds
 2023-06-26
 ​
@@ -4365,542 +4321,2 @@ to timestamp (ms)
 predicatedFundingRate
 has been removed from stream
-2026-04-23
-REST API
-2026-04-22
-REST API
-2026-04-21
-REST API
-Websocket API
-2026-04-20
-REST API
-2026-04-17
-REST API
-2026-04-16
-REST API
-2026-04-14
-REST API
-2026-04-10
-REST API
-2026-04-09
-REST API
-2026-04-08
-REST API
-2026-04-07
-REST API
-2026-03-31
-REST API
-2026-03-26
-REST API
-2026-03-24
-REST API
-2026-03-23
-REST API
-2026-03-20
-REST API
-2026-03-19
-WebSocket
-REST API
-2026-03-17
-WebSocket
-2026-03-13
-REST API
-2026-03-12
-REST API
-2026-03-09
-REST API
-2026-03-06
-REST API
-2026-03-05
-REST API
-2026-03-03
-REST API
-2026-02-12
-REST API
-2026-02-10
-REST API
-2026-02-04
-REST API
-2026-01-28
-REST API
... (diff truncated, total 682 lines) ...
```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index dd451a5..bc77061 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -12,524 +12,33 @@ Language
 繁體中文
 Kucoin
-Home
 Copy Page
-Introduction
-Authentication
-Enums Definitions
-Terms Definitions
-SDK
-OpenClaw
-Rate Limit
-Change Log
-User Service
-Market Making Incentive Scheme
-VIP Fast Track
-Broker Program
-Pro REST
-Introduction
-Market Data
-Get Announcements
-Get Currency
-Get Currencies
-Get Symbol
-Get Ticker
-Get OrderBook
-Get Klines
-Get Trades
-Get Collateral Ratio
-Get Cross Margin Config
-Get Index Price
-Get Current Funding Rate
-Get History Funding Rate
-Get Position Tiers
-Get Futures Open Interest
-Get Service Status
-Get Third-Party Custody Currencies
-Get Borrowable Currencies
-Account
-Get Account Overview (UTA)
-Get Account Currency Assets (UTA)
-Get Account Currency Assets (Classic)
-Get Sub Account Currency Assets
-Get Transfer Quotas
-Flex Transfer
-Set Sub Account Transfer Permission
-Get Account Mode
-Set Account Mode
-Get Fee Rate
-Get Account Ledger
-Get Interest History (UTA)
-Modify Futures Leverage (UTA)
-Get Deposit Address
-Get Third-Party Custody Account Currency Limits
-Modify Leverage Margin Cross (UTA)
-Get Leverage (UTA)
-Get Borrowing Rates and Limits
-Orders
-Place Order
-Batch Place Order (Classic)
-Cancel Order
-Batch Cancel Orders By ID
-Batch Cancel Orders By Symbol
-Get Order Details
-Get Open Order List
-Get Order History
-Get Trade History
-Set DCP (Classic)
-Get DCP (Classic)
-Positions
-Get Position List (UTA)
-Get Positions History (UTA)
-Get Account Position Tiers
-Get Private Funding Fee History
-VIP Lending
-Introduction
-Get Collateral Ratio
-Get Loan Info
-Get Accounts
-Pro WebSocket
-Base Info
-Introduction
-Get Private Token - Pro API Private Channels
-Public Channels
-Kline
-Ticker
-Orderbook
-Trade
-Private Channels
-Order
-Balance
-Execution
-Execution Lite
-Position
-Leverage
-LiquidationWarning
-Add/Cancel Order
-Add Order
-Cancel Order
-Classic REST
-Account Info
-Account & Funding
-Get Account Summary Info
-Get Apikey Info
-Get Account Type - Spot
-Get Account List - Spot
-Get Account Detail - Spot
-Get Account - Cross Margin
-Get Account - Isolated Margin
-Get Account - Futures
-Get Account Ledgers - Spot/Margin
-Get Account Ledgers - Trade_hf
-Get Account Ledgers - Margin_hf
-Get Account Ledgers - Futures
 Sub Account
-Add sub-account
-Add sub-account Margin Permission
-Add sub-account Futures Permission
-Get sub-account List - Summary Info
-Get sub-account Detail - Balance
-Get sub-account List - Spot Balance (V2)
-Get sub-account List - Futures Balance (V2)
 Sub Account API
-Get sub-account API List
-Add sub-account API
-Modify sub-account API
-Delete sub-account API
 Deposit
-Add Deposit Address (V3)
-Get Deposit Address (V3)
-Get Deposit History
 Withdrawals
-Get Withdrawal Quotas
-Withdraw (V3)
-Cancel Withdrawal
-Get Withdrawal History
-Get Withdrawal History By ID
 Transfer
-Get Transfer Quotas
-Flex Transfer
 Trade Fee
-Get Basic Fee - Spot/Margin
-Get Actual Fee - Spot/Margin
-Get Actual Fee - Futures
-Spot Trading
-Market Data
-Get Announcements
-Get Currency
-Get All Currencies
-Get Symbol
-Get All Symbols
-Get Ticker
-Get All Tickers
-Get Trade History
-Get Klines
-Get Part OrderBook
-Get Full OrderBook
-Get Call Auction Part OrderBook
-Get Call Auction Info
-Get Fiat Price
-Get 24hr Stats
-Get Market List
-Get Client IP Address
-Get Server Time
-Get Service Status
-Get KYC Regions
 Orders
-Add Order
-Add Order Sync
-Add Order Test
-Batch Add Orders
-Batch Add Orders Sync
-Cancel Order By OrderId
-Cancel Order By OrderId Sync
-Cancel Order By ClientOid
-Cancel Order By ClientOid Sync
-Cancel Partial Order
-Cancel All Orders By Symbol
-Cancel All Orders
-Modify Order
-Get Order By OrderId
-Get Order By ClientOid
-Get Symbols With Open Order
-Get Open Orders
-Get Open Orders By Page
-Get Closed Orders
-Get Trade History
-Get DCP
-Set DCP
-Add Stop Order
-Cancel Stop Order By ClientOid
-Cancel Stop Order By OrderId
-Batch Cancel Stop Orders
-Get Stop Orders List
-Get Stop Order By OrderId
-Get Stop Order By ClientOid
... (diff truncated, total 625 lines) ...
```

### Gate.io Spot WebSocket v4 (`gate-spot-ws`)
- Source: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/

```diff
diff --git a/changelogs/gate-spot-ws.txt b/changelogs/gate-spot-ws.txt
index 3b7b648..023517b 100644
--- a/changelogs/gate-spot-ws.txt
+++ b/changelogs/gate-spot-ws.txt
@@ -10,5 +10,4 @@ CrossEx
 🔥 Agent
 公告
-Search
 现货 WebSocket v4
 Websocket API 概述

```

### Gate.io Futures WebSocket v4 (`gate-futures-ws`)
- Source: https://www.gate.io/docs/developers/futures/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/futures/ws/zh_CN/

```diff
diff --git a/changelogs/gate-futures-ws.txt b/changelogs/gate-futures-ws.txt
index 473f2f5..ade8ab6 100644
--- a/changelogs/gate-futures-ws.txt
+++ b/changelogs/gate-futures-ws.txt
@@ -10,5 +10,4 @@ CrossEx
 🔥 Agent
 公告
-Search
 Gate 永续合约 WebSocket v4
 服务地址

```
