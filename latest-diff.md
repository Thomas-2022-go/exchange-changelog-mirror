<!-- has_changes=true date=2026-04-24 -->
# Exchange API Changelog Diff

Generated: 2026-04-24 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (126374 bytes)

- [CHANGED] **Binance Derivatives (USDS-M / Coin-M / Options)** (`binance-derivatives`): 4866 diff lines

- [CHANGED] **OKX V5** (`okx`): 24339 diff lines

- [CHANGED] **Bitget (Spot + Futures)** (`bitget`): 1022 diff lines

- [CHANGED] **Bybit V5** (`bybit`): 6176 diff lines

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 1833 diff lines

- [CHANGED] **Gate.io Spot WebSocket v4** (`gate-spot-ws`): 20293 diff lines

- [CHANGED] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): 25621 diff lines



## Changes

### Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`)
- Source: https://developers.binance.com/docs/derivatives/change-log
- Raw: https://developers.binance.com/docs/derivatives/change-log

```diff
diff --git a/changelogs/binance-derivatives.txt b/changelogs/binance-derivatives.txt
index 33992cf..3562301 100644
--- a/changelogs/binance-derivatives.txt
+++ b/changelogs/binance-derivatives.txt
@@ -1,1792 +1,1020 @@
 Change Log
-2026-04-17
-​
+2026-04-17​
 Portfolio Margin Pro
-User Data Stream:
-Add new event
-PM_PRO_ACCOUNT_UPDATE
-, which pushes account asset status every 5 seconds.
-2026-04-15
-​
+- User Data Stream:
+  - Add new event PM_PRO_ACCOUNT_UPDATE, which pushes account asset status every 5 seconds.
+2026-04-15​
 European Options
-Trade
-Cancel Multiple Option Orders - Corrected request weight from 1 to 5.
-2026-04-14
-​
+- Trade
+  - Cancel Multiple Option Orders - Corrected request weight from 1 to 5.
+2026-04-14​
 Portfolio Margin
-The following REST Endpoints and WebSocket User Data Streams will be enabled from 2026-04-28:
-REST:
-POST
-/papi/v1/um/algo/order
-DELETE
-/papi/v1/um/algo/order
-DELETE
-/papi/v1/um/algo/allOpenOrders
-GET
-/papi/v1/um/algo/algoOrder
-GET
-/papi/v1/um/algo/openAlgoOrders
-GET
-/papi/v1/um/algo/allAlgoOrders
-Websocket:
-ALGO_UPDATE
-: algo order update event
-The following REST Endpoints will be deprecated from 2026-04-28
-REST:
-POST
-/papi/v1/um/conditional/order
-DELETE
-/papi/v1/um/conditional/order
-DELETE
-/papi/v1/um/conditional/allOpenOrders
-GET
-/papi/v1/um/conditional/allOrders
-GET
-/papi/v1/um/conditional/openOrders
-GET
-/papi/v1/um/conditional/openOrder
-GET
-/papi/v1/um/conditional/orderHistory
-Please refer to
-announcement
-for API replacement
-2026-04-13
-​
+- The following REST Endpoints and WebSocket User Data Streams will be enabled from 2026-04-28:
+  - REST:
+    - POST /papi/v1/um/algo/order
+    - DELETE /papi/v1/um/algo/order
+    - DELETE /papi/v1/um/algo/allOpenOrders
+    - GET /papi/v1/um/algo/algoOrder
+    - GET /papi/v1/um/algo/openAlgoOrders
+    - GET /papi/v1/um/algo/allAlgoOrders
+  - Websocket:
+    - ALGO_UPDATE: algo order update event
+- The following REST Endpoints will be deprecated from 2026-04-28
+  - REST:
+    - POST /papi/v1/um/conditional/order
+    - DELETE /papi/v1/um/conditional/order
+    - DELETE /papi/v1/um/conditional/allOpenOrders
+    - GET /papi/v1/um/conditional/allOrders
+    - GET /papi/v1/um/conditional/openOrders
+    - GET /papi/v1/um/conditional/openOrder
+    - GET /papi/v1/um/conditional/orderHistory
+Please refer to announcement for API replacement
+2026-04-13​
 Portfolio Margin and Portfolio Margin Pro
 New REST APIs:
-POST /sapi/v1/portfolio/margin-call-level
-: Set the margin call level for a Portfolio Margin account. When the account's uniMMR drops to the specified level, a notification will be sent via email and SMS.
-GET /sapi/v1/portfolio/margin-call-level
-: Get the margin call level for a Portfolio Margin account.
-DELETE /sapi/v1/portfolio/margin-call-level
-: Delete the margin call level for a Portfolio Margin account.
-2026-04-10
-​
+- POST /sapi/v1/portfolio/margin-call-level : Set the margin call level for a Portfolio Margin account. When the account's uniMMR drops to the specified level, a notification will be sent via email and SMS.
+- GET /sapi/v1/portfolio/margin-call-level : Get the margin call level for a Portfolio Margin account.
+- DELETE /sapi/v1/portfolio/margin-call-level : Delete the margin call level for a Portfolio Margin account.
+2026-04-10​
 Effective Date: 2026-04-14
 COIN-M Futures / Portfolio Margin and Portfolio Margin Pro
-POST /dapi/v1/positionSide/dual
-and
-POST /papi/v1/cm/positionSide/dual
-CM
-dualSidePosition
-must now stay consistent with UM. If CM
-dualSidePosition
-is already the same as UM, changing it will be rejected.
-USDⓈ-M Futures
-Liquidation Order Streams (
-<symbol>@forceOrder
-) and All Market Liquidation Order Streams (
-!forceOrder@arr
-)
-Updated description: changed "only the latest one liquidation order" to "only the largest one liquidation order" within 1000ms.
-2026-04-09
-​
+- POST /dapi/v1/positionSide/dual and POST /papi/v1/cm/positionSide/dual
+  - CM dualSidePosition must now stay consistent with UM. If CM dualSidePosition is already the same as UM, changing it will be rejected.
+USDⓈ-M Futures
+- Liquidation Order Streams (<symbol>@forceOrder) and All Market Liquidation Order Streams (!forceOrder@arr)
+  - Updated description: changed "only the latest one liquidation order" to "only the largest one liquidation order" within 1000ms.
+2026-04-09​
 Portfolio Margin
-User Data Stream
-Event: Margin Order Update
-- Added new fields to the
-executionReport
-event payload:
-Cs
-,
-pl
-,
-pL
-,
-pY
-,
-eR
-.
-2026-04-08
-​
+- User Data Stream
+  - Event: Margin Order Update - Added new fields to the executionReport event payload: Cs, pl, pL, pY, eR.
+2026-04-08​
 Portfolio Margin
 New REST APIs:
-POST /papi/v1/um/stock/contract
-: sign TradFi-Perps agreement contract
-2026-04-06
-​
+- POST /papi/v1/um/stock/contract : sign TradFi-Perps agreement contract
+2026-04-06​
 USDⓈ-M Futures / COIN-M Futures / Portfolio Margin and Portfolio Margin Pro
-GET /fapi/v1/forceOrders
-,
-GET /dapi/v1/forceOrders
-,
-GET /papi/v1/um/forceOrders
-and
-GET /papi/v1/cm/forceOrders
-Added note: Only support querying data in the past 90 days.
-2026-04-02
-​
-USDⓈ-M Futures
-WebSocket
-Updated
-important websocket change notice
-with legacy URL decommissioning date:
-2026-04-23
-.
-2026-03-19
-​
+- GET /fapi/v1/forceOrders, GET /dapi/v1/forceOrders, GET /papi/v1/um/forceOrders and GET /papi/v1/cm/forceOrders
+  - Added note: Only support querying data in the past 90 days.
+2026-04-02​
+USDⓈ-M Futures
+- WebSocket
+  - Updated important websocket change notice with legacy URL decommissioning date: 2026-04-23.
+2026-03-19​
 USDⓈ-M Futures / COIN-M Futures
-GET /fapi/v1/historicalTrades
-and
-GET /dapi/v1/historicalTrades
-Updated data availability from the last 3 months to the last 1 month.
-2026-03-16
-​
+- GET /fapi/v1/historicalTrades and GET /dapi/v1/historicalTrades
+  - Updated data availability from the last 3 months to the last 1 month.
+2026-03-16​
 USDⓈ-M Futures
-Websocket Market Streams
-Add new field
-ap
-in
-Mark-Price-Stream
-and
-Mark-Price-Stream-for-All-market
... (diff truncated, total 4866 lines) ...
```

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 2f7f12d..5344b25 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,5154 +1,2149 @@
-欧易 API接入指南 | 欧易技术对接 | 欧易
-导航
 待发布内容
-大宗商品产品
-instCategory
-重新分类
-2026-04-15
-事件合约
-已有接口改动
-2026-04-13
-下单附带移动止盈止损
-2026-04-10
-活期借币
-交易产品基础信息
-历史市场数据
-ETH 质押 / SOL 质押
-2026-04-08
-2026-04-07
-交易手续费等级限制下调
-下线 WS 订单操作频道中的 instId 请求参数
-下单需要 KYC 二级或以上认证
-2026-03-31
-交易产品
-资金费率
-2026-03-26
-2026-03-24
-2026-03-18
-2026-03-13
-2026-03-10
-下单和改单接口新增返回字段 subCode，用于在 WebSocket 和 REST API 的响应中提供更详细的错误信息。
-一键还债支持跨币种保证金模式和组合保证金模式
-2026-03-04
-盘前变基合约
-2026-03-02
-SBE 行情数据
-交易产品基础信息
-2026-02-27
-2026-02-12
-2026-02-05
-2026-01-21
-2026-01-15
-XAUT 永续合约重命名
-2026-01-13
-2026-01-07
-2025-12-22
-2025-12-10
-手动借币限速规则变更
-2025-12-03
-2025-11-26
-订单接口
-行情数据
-撤单原因
-错误码
-2025-11-25
-获取交易产品基础信息接口/产品频道
-获取当前账户交易手续费费率
-2025-11-21
-ETH 质押赎回更新
-2025-11-20
-2025-11-13
-delta 中性策略模式
-新增接口
-查看账户配置
-获取市场借币杠杆利率和借币限额
-查看账户余额/账户频道
-查看持仓信息/持仓频道
-获取子账户最大可转余额
-撤单原因
-错误码
-稳定币分组出借APR逻辑更新
-2025-11-11
-充值记录脱敏显示
-2025-11-06
-2025-10-23
-获取交易产品基础信息接口新增持仓限制参数
-公告接口 pTime 语义更新 & businessPTime 字段新增
-2025-09-26
-新增请求参数
-USD 本位合约
-新增接口
-新增返回参数
-返回参数含义调整
-instFamily
-和
-uly
-参数说明">
-instFamily
-和
-uly
-参数说明
-新增错误码
-2025-09-17
-现货和杠杆交易以计价币种收取手续费
-2025-09-11
-2025-09-10
-询价
-获取询价单信息/询价频道
-执行报价
-MMP 相关接口
-获取大宗交易信息
-大宗交易频道
-公共成交数据
-错误码
-2025-09-09
-2025-09-04
-2025-09-02
-历史市场数据查询接口
-手动借币/还款接口限流调整
-2025-08-28
-2025-08-26
-2025-08-20
-统一 USD 深度优化
-2025-08-12
-2025-08-08
-2025-08-05
-2025-07-30
-2025-07-29
-2025-07-24
-新增自动赚币功能
-提现接口 - 新增 toAddrType 参数
-2025-07-08
-Open API 支持 USD 统一深度
-交易频道新增 seqId 字段
-成交频道新增clOrdId推送数据参数
-订单频道优化
-交易时效性优化
-2025-07-02
-2025-06-26
-2025-06-24
-2025-06-19
-2025-06-17
-买卖交易
-2025-06-13
-2025-06-03
-2025-05-30
-2025-05-29
-所有 WebSocket 订阅与响应新增 id 参数
-新增提前挂单相关返回参数
-2025-05-28
-DMA Broker 接口改造
-2025-05-27
-websocket服务升级断线提示调整
-2025-05-26
-2025-05-21
-2025-05-15
-2025-05-08
-2025-05-07
-2025-05-06
-交易产品接口、频道优化
-2025-04-28
-AWS域名已停止服务
-2025-04-24
-2025-04-17
-2025-04-02
-2025-03-26
-跨币种保证金账户质押币设置
-WebSocket 新增字段
-2025-03-21
-2025-03-19
-2025-03-18
-简单账户支持一件还债
-2025-03-12
-交割合约每日结算
-cancelSource 新增枚举值
-账户及持仓频道新增分页推送数据参数
-2025-03-03
-固定借贷/定期简单赚币接口下线
-固定借贷
-定期简单赚币
-2025-02-12
-支持交易货币或计价货币作为逐仓杠杆保证金
-2025-01-17
-组合保证金账户模式的保证金计算规则升级
-2025-01-15
-2025-01-07
-Oracle上链交易数据接口下线
-2024-12-31
-2024-12-18
-websocket服务升级断线提示
-2024-12-16
-2024-12-11
-2024-12-04
-2024-12-03
-2024-11-28
-2024-11-22
-2024-11-21
-固定借贷/定期简单赚币功能下线
-固定借贷接口调整
-定期简单赚币接口调整
-2024-11-20
-追逐限价委托
-2024-11-18
-2024-11-14
-2024-11-11
-2024-11-08
... (diff truncated, total 24339 lines) ...
```

### Bitget (Spot + Futures) (`bitget`)
- Source: https://www.bitget.com/api-doc/common/changelog
- Raw: https://www.bitget.fit/api-doc/common/changelog

```diff
diff --git a/changelogs/bitget.txt b/changelogs/bitget.txt
index 1b34441..bc64963 100644
--- a/changelogs/bitget.txt
+++ b/changelogs/bitget.txt
@@ -1,721 +1,383 @@
 Changelog
-[January 29, 2026] Transfer Records Enable idLessThan Pagination Mode
-​
+[January 29, 2026] Transfer Records Enable idLessThan Pagination Mode​
 Interface:
-/api/v2/spot/account/transferRecords
-Changes：
-Enabled idLessThan pagination mode for retrieving transfer records; deprecated pageNum.
-[January 7, 2026] Optimization of Push Frequency for Websocket Order Book Channel (books1) in Classic Account (v2)
-​
+- /api/v2/spot/account/transferRecords Changes：
+- Enabled idLessThan pagination mode for retrieving transfer records; deprecated pageNum.
+[January 7, 2026] Optimization of Push Frequency for Websocket Order Book Channel (books1) in Classic Account (v2)​
 Websocket: Order Book Channel
-Adjustment Content: The push frequency of the order book channel (books1) is optimized to 10ms.
-[January 6, 2026] Added 'off_close' (Delisting Liquidation) to the enum values of the response parameter 'orderSource'.
-​
+ Adjustment Content: The push frequency of the order book channel (books1) is optimized to 10ms.
+[January 6, 2026] Added 'off_close' (Delisting Liquidation) to the enum values of the response parameter 'orderSource'.​
 Interface:
-/api/v2/mix/order/orders-pending, /api/v2/mix/order/orders-history
-Changes：
-Added 'off_close' (Delisting Liquidation) to the enum values of the response parameter 'orderSource'.
-[November 27, 2025] A new return field, 'liqPrice', has been added to the futures historical order.
-​
+- /api/v2/mix/order/orders-pending, /api/v2/mix/order/orders-history Changes：
+- Added 'off_close' (Delisting Liquidation) to the enum values of the response parameter 'orderSource'.
+[November 27, 2025] A new return field, 'liqPrice', has been added to the futures historical order.​
 Interface:
-/api/v2/mix/order/orders-history
-Changes：
-A new return field, 'liqPrice', has been added to the futures historical order.
-[November 26, 2025] Websocket Added new ADL notification channel
-​
+- /api/v2/mix/order/orders-history Changes：
+- A new return field, 'liqPrice', has been added to the futures historical order.
+[November 26, 2025] Websocket Added new ADL notification channel​
 Websocket: ADL notification channel
-Changes: Websocket Added new ADL notification channel
-[November 26, 2025] Add new FAQ Q15
-​
+ Changes: Websocket Added new ADL notification channel
+[November 26, 2025] Add new FAQ Q15​
 Changes:Add new FAQ Q15
-[November 19, 2025] New isRwa Field Added to Get Contract Information API Response
-​
+[November 19, 2025] New isRwa Field Added to Get Contract Information API Response​
 Interface:
-/api/v2/mix/market/contracts
+- /api/v2/mix/market/contracts
 Changes：
-New
-isRwa
-Field Added to Get Contract Information API Response
-[November 8, 2025] WebSocket has added a new futures equity channel.
-​
+- New isRwa Field Added to Get Contract Information API Response
+[November 8, 2025] WebSocket has added a new futures equity channel.​
 Websocket: futures equity channel
-Changes: WebSocket has added a new futures equity channel.
-[November 8, 2025] WebSocket Supports Broker API Code
-​
+ Changes: WebSocket has added a new futures equity channel.
+[November 8, 2025] WebSocket Supports Broker API Code​
 Websocket: place order channel
-Changes: The order placement channel supports passing the Broker API Code to receive rebates.
-[November 7, 2025] Add Maximum Openable Quantity API
-​
+ Changes: The order placement channel supports passing the Broker API Code to receive rebates.
+[November 7, 2025] Add Maximum Openable Quantity API​
 Interface:
-/api/v2/mix/account/max-open
+- /api/v2/mix/account/max-open
 Changes：
-Add Maximum Openable Quantity API
-[November 7, 2025] Add Estimated Liquidation Price API
-​
+- Add Maximum Openable Quantity API
+[November 7, 2025] Add Estimated Liquidation Price API​
 Interface:
-/api/v2/mix/account/liq-price
+- /api/v2/mix/account/liq-price
 Changes：
-Add Estimated Liquidation Price API
-[November 6, 2025] New broker commission inquiry interface added
-​
+- Add Estimated Liquidation Price API
+[November 6, 2025] New broker commission inquiry interface added​
 Interface:
-/api/v2/broker/total-commission
-/api/v2/broker/order-commission
-/api/v2/broker/rebate-info
+- /api/v2/broker/total-commission
+- /api/v2/broker/order-commission
+- /api/v2/broker/rebate-info
 Changes：
-New broker commission inquiry interface added
-[October 21, 2025] Add an endpoint for querying symbol with isolated margin mode in futures.
-​
+- New broker commission inquiry interface added
+[October 21, 2025] Add an endpoint for querying symbol with isolated margin mode in futures.​
 Interface: /api/v2/mix/account/isolated-symbols
-Changes：
-Add an endpoint for querying symbol with isolated margin mode in futures.
-[October 21, 2025] Optimization of the spot historical plan order endpoint
-​
+ Changes：
+- Add an endpoint for querying symbol with isolated margin mode in futures.
+[October 21, 2025] Optimization of the spot historical plan order endpoint​
 Interface: /api/v2/spot/trade/history-plan-order
-Changes：
--The request parameters
-symbol
-,
-startTime
-, and
-endTime
-are changed to optional.
-[October 14, 2025] Notice: Classic Account Error Code Optimization
-​
+ Changes： -The request parameters symbol, startTime, and endTime are changed to optional.
+[October 14, 2025] Notice: Classic Account Error Code Optimization​
 Scope of Impact:
 Classic Account v2-related APIs
-Optimization Content:
-Unified error code mapping: Resolves the issue where "different error codes correspond to the same error message", ensuring one code maps to one message and reducing recognition confusion.
-Standardized error message matching: Fixes the problem where "different error messages correspond to the same error code", enabling accurate matching between messages and codes and improving troubleshooting efficiency.
-[September 11, 2025] Newly Added Interfaces Related to union Margin
-​
-Changes：
-Newly Added — Query the USDT amount required for switching from union margin to single-currency margin /api/v2/mix/account/switch-union-usdt
-Newly Added — union Margin Conversion and Repayment API /api/v2/mix/account/union-convert
-Newly Added — union Margin Configuration Parameter API /api/v2/mix/account/union-config
-Newly Added — union Margin Currency Transfer Limit API /api/v2/mix/account/transfer-limits
-Newly Added — New union margin parameters in the WS Account Channel:
-unionTotalMargin
-(Margin Amount),
-unionAvailable
-(Available Margin),
-unionMm
-(Maintenance Margin),
-assetMode
-(Account Mode)
-Newly Added — New
-assetMode
-(Account Mode) parameter in the WS Position Channel
-[September 4, 2025] Notice: Adjustment to the transferId field in the sub-main account transfer records retrieval function. The transferId will be updated to the one returned during sub-main account transfers.
-​
+ Optimization Content:
+- Unified error code mapping: Resolves the issue where "different error codes correspond to the same error message", ensuring one code maps to one message and reducing recognition confusion.
+- Standardized error message matching: Fixes the problem where "different error messages correspond to the same error code", enabling accurate matching between messages and codes and improving troubleshooting efficiency.
+[September 11, 2025] Newly Added Interfaces Related to union Margin​
+Changes：
+- Newly Added — Query the USDT amount required for switching from union margin to single-currency margin /api/v2/mix/account/switch-union-usdt
+- Newly Added — union Margin Conversion and Repayment API /api/v2/mix/account/union-convert
+- Newly Added — union Margin Configuration Parameter API /api/v2/mix/account/union-config
+- Newly Added — union Margin Currency Transfer Limit API /api/v2/mix/account/transfer-limits
+- Newly Added — New union margin parameters in the WS Account Channel: unionTotalMargin (Margin Amount), unionAvailable (Available Margin), unionMm (Maintenance Margin), assetMode (Account Mode)
+- Newly Added — New assetMode (Account Mode) parameter in the WS Position Channel
+[September 4, 2025] Notice: Adjustment to the transferId field in the sub-main account transfer records retrieval function. The transferId will be updated to the one returned during sub-main account transfers.​
 Interface: /api/v2/spot/account/sub-main-trans-record
-Changes：
-Previous generation rule: for transferId: Auto-incrementing ID
-New generation rule: for transferId: Snowflake algorithm
-[September 2, 2025] Add reason field for Get Upgrade Status
-​
+ Changes：
+- Previous generation rule: for transferId: Auto-incrementing ID
+- New generation rule: for transferId: Snowflake algorithm
+[September 2, 2025] Add reason field for Get Upgrade Status​
 Interface: /api/v2/spot/account/upgrade-status
-Changes：
-Add reason field for Get Upgrade Status
-[August 28, 2025] Notice: Optimization of Push Frequency for Websocket Order Book Channel (books1) in Classic Account (v2)
-​
+ Changes：
+- Add reason field for Get Upgrade Status
+[August 28, 2025] Notice: Optimization of Push Frequency for Websocket Order Book Channel (books1) in Classic Account (v2)​
 Websocket: Order Book Channel
-Adjustment Content: The push frequency of the order book channel (books1) is optimized to 20ms. The symbols for this optimization are: BTCUSDT, ETHUSDT, XRPUSDT, SOLUSDT, SUIUSDT, DOGEUSDT, ADAUSDT, PEPEUSDT, LINKUSDT, HBARUSDT
-[August 11, 2025] Agent commission API query supports fee deduction
-​
+ Adjustment Content: The push frequency of the order book channel (books1) is optimized to 20ms. The symbols for this optimization are: BTCUSDT, ETHUSDT, XRPUSDT, SOLUSDT, SUIUSDT, DOGEUSDT, ADAUSDT, PEPEUSDT, LINKUSDT, HBARUSDT
+[August 11, 2025] Agent commission API query supports fee deduction​
 Interface：/api/broker/v1/agent/commission-distribution;/api/broker/v1/agent/customer-commissions;
+ Changes：
+- Agent commission API query supports fee deduction details
+[August 11, 2025] API Global rate Limit Adjustment​
 Changes：
-Agent commission API query supports fee deduction details
-[August 11, 2025] API Global rate Limit Adjustment
-​
-Changes：
-There is an overall rate limit rule of 6,000 times per IP per minute. After the rate limit is triggered, the recovery time is adjusted from 1 minute to 5 minutes.
-[August 6, 2025] Add unrealizedPL field for sub-account futures asset info
... (diff truncated, total 1022 lines) ...
```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 71c6d19..fd6e0d2 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,4322 +1,1849 @@
-2026-04-23
-​
-REST API
-​
-Get Instruments Info
-[UPDATE]
-Add new field
-symbolId
-(spot)
-Get Account Instruments Info
-[UPDATE]
-Add new field
-symbolId
-(spot)
-2026-04-22
-​
-REST API
-​
-Get Affiliate User Info
-[UPDATE]
-Add new response fields:
-paySendAmount30Day
-,
-payFtt
-,
-cardFtt
-2026-04-21
-​
-REST API
-​
-Get Position Info
-[UPDATE]
-Add
-openTime
-Get Instruments Info
-[UPDATE]
-Add new
-symbolType
-enum values:
-stock
-(linear),
-forex
-(linear)
-Get Account Instruments Info
-[UPDATE]
-Add new
-symbolType
-enum values:
-stock
-(linear),
-forex
-(linear)
-Websocket API
-​
-Position
-[UPDATE]
-Add
-openTime
-2026-04-20
-​
-REST API
-​
-Sign Agreement
-[UPDATE]
-Add new request parameter
-categoryV2
-. New enum values will be added to
-categoryV2
-going forward; the existing
-category
-field remains supported
-2026-04-17
-​
-REST API
-​
-Withdraw
-[UPDATE]
-add a new required request param
-transactionPurpose
-for Bybit Turkey site users
-2026-04-16
-​
-REST API
-​
-Bybit Card adds new endpoints [NEW]
-Query Asset Records
-[NEW]
-Query Point Balance
-[NEW]
-Query Point Records
-[NEW]
-Query Tier Info
-[NEW]
-Query Mall Item List
-[NEW]
-Query Cashback Detail
-[NEW]
-2026-04-14
-​
-REST API
-​
-Earn adds new produc [UPDATE]
-Fixed Saving
-[NEW]
-Advanced-Earn adds new product [UPDATE]
-Discount Buy
-[NEW]
-2026-04-10
-​
-REST API
-​
-Advanced-Earn adds new product [UPDATE]
-Liquidity Mining
-[NEW]
-2026-04-09
-​
-REST API
-​
-Manual Repay
-[UPDATE]
-Manual Repay Without Asset Conversion
-[UPDATE]
-Add new request parameter
-repaymentType
-to specify whether to repay fixed-rate, floating-rate, or both liabilities
-Get Liability Info
-[NEW]
-Add a new endpoint to query liability details for a coin, including total, fixed-rate, floating-rate, spot, and derivatives borrow amounts
-Fixed-Rate Borrow
-[NEW]
-Add a new endpoint to place a fixed-rate borrow order with customizable annual rate, term, repayment type, and fill strategy
-Get Fixed-Rate Borrow Order Info
-[NEW]
-Add a new endpoint to query fixed-rate borrow order history with filtering by order ID, coin, status, and term
-Get Fixed-Rate Borrow Contract Info
-[NEW]
-Add a new endpoint to query fixed-rate borrow contract details including principal, interest, repayment time, and contract status
-Get Fixed-Rate Borrow Order Quote
-[NEW]
-Add a new endpoint to query available fixed-rate borrow quotes with sorting by annual rate, term, or quantity
-Renew Fixed-Rate Borrow
-[NEW]
-Add a new endpoint to renew a fixed-rate borrow contract, supporting full or partial renewal by quantity
-Get API Key Information
-[UPDATE]
-Add new response field
-FiatBitPay
-under
-permissions
-. The old field
-FiatBybitPay
-remains available during the transition period
-Modify Master API Key
-[UPDATE]
-Add new request parameter
-FiatBitPay
-under
-permissions
-. The old field
-FiatBybitPay
-remains available during the transition period
-2026-04-08
-​
-REST API
-​
-Support a new earn product [UPDATE]
-BYUSDT
-[NEW]
-2026-04-07
-​
-REST API
-​
-Advanced-Earn adds two new products [UPDATE]
-Smart Leverage
-[NEW]
-Double Win
-[NEW]
-2026-03-31
-​
-REST API
-​
-Set Deposit Account
-[UPDATE]
-Support setting Earn account
-Withdraw
-[UPDATE]
-accountType
-now supports Earn account
-Get Delay Withdraw Amount
-[UPDATE]
-Support querying Earn account balance when try to withdraw via Earn account
-2026-03-26
-​
-REST API
-​
... (diff truncated, total 6176 lines) ...
```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index bc77061..3e6e6fa 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,164 +1,40 @@
-Change Log - KUCOIN API
-KUCOIN API
-Home
-Change Log
-API DOC V1
-Language
-繁體中文
-Home
-Change Log
-API DOC V1
-Language
-繁體中文
-Kucoin
-Copy Page
-Sub Account
-Sub Account API
-Deposit
-Withdrawals
-Transfer
-Trade Fee
-Orders
-Orders
-Debit
-Credit
-Risk Limit
-Orders
-Positions
-Funding Fees
-Structured Earn - Dual
-Exchange Broker
-Spot Trading
-Private Channels
-Margin Trading
-Private Channels
-Futures Trading
-Private Channels
-Add/Cancel Order
-Spot Trading
-Margin Trading
-Futures Trading
-Affiliate
-Broker
-Copy Page
-Change Log
 WARNING
-The
-Pro API
-is currently in
-beta testing
-and
-should not be used in production trading environments
-.
-2026.04.19
-#
-[Add]
-Modify Leverage Margin Cross (UTA)
-[Add]
-Get Leverage (UTA)
-[Add]
-Get Private Funding Fee History
-[Add]
-Get Borrowing Rates and Limits
-[Add]
-Get Borrowable Currencies
+The Pro API is currently in beta testing and should not be used in production trading environments.
+2026.04.19#
+[Add] Modify Leverage Margin Cross (UTA)
+[Add] Get Leverage (UTA)
+[Add] Get Private Funding Fee History
+[Add] Get Borrowing Rates and Limits
+[Add] Get Borrowable Currencies
 [Add] added new value “MARGIN” in field “tradeType” in following API
-Place Order
-,
-Cancel Order
-,
-Batch Cancel Orders By ID
-,
-Get Order Details
-,
-Get Order History
-,
-Get Trade History
-,
-Get Open Order List
-[Modify]
-Get Current Funding Rate
-added new fields in the response: “currentGranularity”, “newGranularity”, "newGranularityStartTime"
-[Modify]
-Get Account Currency Assets
-add new fields in the response: “potentialBorrow”
+Place Order, Cancel Order, Batch Cancel Orders By ID, Get Order Details, Get Order History, Get Trade History, Get Open Order List
+[Modify] Get Current Funding Rate added new fields in the response: “currentGranularity”, “newGranularity”, "newGranularityStartTime"
+[Modify] Get Account Currency Assets add new fields in the response: “potentialBorrow”
 [Modify] Pro WebSocket Private Channels
-#
-Channel
-Parameter
-Change
-1
-Order
-tradeType
-Added new value “UNIFIED”in subscribe field “tradeType”，supporting simultaneous push for UTA Spot and Margin, and separate push for UTA Futures.
-2
-Leverage
-c, tT, mM
-Added new feild “c” currency, “tT” tradeType, “mM” marginMode in response.
+| # | Channel | Parameter | Change
+| 1 | Order | tradeType | Added new value “UNIFIED”in subscribe field “tradeType”，supporting simultaneous push for UTA Spot and Margin, and separate push for UTA Futures.
+| 2 | Leverage | c, tT, mM | Added new feild “c” currency, “tT” tradeType, “mM” marginMode in response.
 [Modify] Pro WebSocket Public Channels
-#
-Channel
-Parameter
-Change
-1
-Ticker
-symbols
-Added new field in subscribe: “symbols”.
-2026.04.09
-#
-[Modify]
-Get Position List (UTA)
-:
+| # | Channel | Parameter | Change
+| 1 | Ticker | symbols | Added new field in subscribe: “symbols”.
+2026.04.09#
+[Modify] Get Position List (UTA):
 1.
 Added new fields in the request "pageSize", "pageNumber"
 2.
 Added new fields in the response "liquidationPrice"
-[Add]
-Get Third-Party Custody Currencies
-[Add]
-Get Third-Party Custody Account Currency Limits
-2026.03.30
-#
-[Add] Pro WebSocket Private Channel:
-Execution Lite
+[Add] Get Third-Party Custody Currencies
+[Add] Get Third-Party Custody Account Currency Limits
+2026.03.30#
+[Add] Pro WebSocket Private Channel: Execution Lite
 [Modify] Pro WebSocket Private Channels
-#
-Channel
-Parameter
-Change
-1
-Order
-eT
-Added
-match
-as a new enum value for the Event Type response field
-eT
-. In addition, the order entry time is generated by the Risk Engine in Classic mode and by the Match Engine in UTA mode(Currently only available for Spot).
-2
-Balance
-accountType
-Changed the
-accountType
-enum value in the subscription message from
-TRADING
-to
-SPOT
-. Although
-TRADING
-is still accepted at present, it is recommended to use
-SPOT
-going forward.
+| # | Channel | Parameter | Change
+| 1 | Order | eT | Added match as a new enum value for the Event Type response field eT. In addition, the order entry time is generated by the Risk Engine in Classic mode and by the Match Engine in UTA mode(Currently only available for Spot).
+| 2 | Balance | accountType | Changed the accountType enum value in the subscription message from TRADING to SPOT. Although TRADING is still accepted at present, it is recommended to use SPOT going forward.
 [Optimize] Pro WebSocket Private Channels
-#
-Channel
-Change
-1
-Orderbook
-Switched BBO pushes to the high-speed channel to further reduce latency.
-2
-Trade
-Switched pushes to the high-speed channel to further reduce latency.
-2026.03.04
-#
+| # | Channel | Change
+| 1 | Orderbook | Switched BBO pushes to the high-speed channel to further reduce latency.
+| 2 | Trade | Switched pushes to the high-speed channel to further reduce latency.
+2026.03.04#
 SPOT Margin HF Migration Completed
 Parameter Unification & LF Endpoint Deprecation
@@ -167,214 +43,35 @@ https://www.kucoin.com/announcement/kucoin-margin-notice-250702
 KuCoin Margin APIs have completed the high-frequency (HF) migration. All low-frequency (LF) accounts for SPOT Margin have been migrated to HF accounts. Effective immediately, please use HF APIs for SPOT Margin trading and related operations.
 Change Summary
... (diff truncated, total 1833 lines) ...
```

### Gate.io Spot WebSocket v4 (`gate-spot-ws`)
- Source: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/

```diff
diff --git a/changelogs/gate-spot-ws.txt b/changelogs/gate-spot-ws.txt
index 023517b..5880089 100644
--- a/changelogs/gate-spot-ws.txt
+++ b/changelogs/gate-spot-ws.txt
@@ -1,19137 +1,1479 @@
-Gate Spot WebSocketAPI v4 Reference | Gate API v4
-现货&杠杆
-永续合约
-交割合约
-TradFi
-期权
-统一账户
-Alpha
-CrossEx
-🔥 Agent
-公告
-现货 WebSocket v4
-Websocket API 概述
-鉴权
-System API
-应用层 ping/pong 消息
-apiv4
-现货 Websocket V4
-Websocket API 概述
-鉴权
-System API
-应用层 Ping/Pong 消息
-服务升级通知
-Tickers 频道
-客户端订阅
-服务端推送
-公共成交频道
-客户端订阅
-服务端推送
-公共成交频道V2（停止维护）
-客户端订阅
-服务端推送
-K 线频道
-客户端订阅
-服务端推送
-订单簿/深度频道
-最优买卖价
-深度增量更新频道
-深度全量更新频道
-深度频道V2
-维护本地深度
-深度频道V2订阅
-深度V2订阅推送
-深度频道V2取消订阅
-订单频道
-客户端订阅
-服务端推送
-订单频道V2（轻量级通道）
-客户端订阅
-服务端推送
-用户私有成交频道
-客户端订阅
-服务端推送
-用户私有成交频道V2（轻量级通道）
-客户端订阅
-服务端推送
-现货余额频道
-客户端订阅
-服务端推送
-保证金余额频道
-客户端订阅
-服务端推送
-借贷余额频道
-客户端订阅
-服务端推送
-全仓杠杆余额频道
-客户端订阅
-服务端推送
-全仓保证金借贷频道 (废弃)
-客户端订阅
-服务端推送
-自动订单频道
-客户端订阅
-服务端推送
-现货账户交易
-Websocket API
-Login
-下单
-取消订单
-取消所有 Id 列表内的订单
-使用指定的货币对取消所有订单
-修改订单
-订单状态
-查询订单列表
-#
-现货 WebSocket v4
+# 现货 WebSocket v4
 WebSocket 应用示例
-# !/usr/bin/env python
-# coding: utf-8
-import
-hashlib
-import
-hmac
-import
-json
-import
-logging
-import
-time
-import
-threading
-# pip install -U websocket_client
-from
-websocket
-import
-WebSocketApp
-logging
-.
-basicConfig
-(
-level
-=
-logging
-.
-INFO
-)
-logger
-=
-logging
-.
-getLogger
-(
-__name__
-)
-event
-=
-threading
-.
-Event
-(
-)
-class
-GateWebSocketApp
-(
-WebSocketApp
-)
-:
-def
-__init__
-(
-self
-,
-url
-,
-api_key
-,
-api_secret
-,
-**
-kwargs
-)
-:
-super
-(
-GateWebSocketApp
-,
-self
-)
-.
-__init__
-(
-url
-,
-**
-kwargs
-)
-self
-.
-_api_key
-=
-api_key
-self
-.
-_api_secret
-=
-api_secret
-def
-_send_ping
-(
-self
-)
-:
-while
-not
-event
-.
-wait
-(
-10
-)
-:
-self
-.
-last_ping_tm
... (diff truncated, total 20293 lines) ...
```

### Gate.io Futures WebSocket v4 (`gate-futures-ws`)
- Source: https://www.gate.io/docs/developers/futures/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/futures/ws/zh_CN/

```diff
diff --git a/changelogs/gate-futures-ws.txt b/changelogs/gate-futures-ws.txt
index ade8ab6..f2bd378 100644
--- a/changelogs/gate-futures-ws.txt
+++ b/changelogs/gate-futures-ws.txt
@@ -1,8519 +1,852 @@
-Gate API v4
-现货&杠杆
-永续合约
-交割合约
-TradFi
-期权
-统一账户
-Alpha
-CrossEx
-🔥 Agent
-公告
-Gate 永续合约 WebSocket v4
-服务地址
-变更日志
-Websocket API 概述
-鉴权
-futures
-Gate 永续合约 Websocket V4
-服务地址
-变更日志
-Websocket API 概述
-鉴权
-Sbe 数据推送
-对接Sbe
-Sbe使用说明
-System API
-Ping/Pong
-服务升级通知
-Ticker 频道
-订阅操作
-Ticker 推送
-取消订阅
-公有成交频道
-公有成交订阅
-公有成交推送
-取消订阅
-深度频道
-深度全量更新频道
-全量深度推送
-全量深度取消订阅
-最佳买卖价订阅
-最佳买卖价的推送
-最佳买卖价的取消订阅
-合约深度更新推送订阅
-深度更新推送
-深度更新取消订阅
-深度频道V2
-维护本地深度
-深度频道V2订阅
-深度V2订阅推送
-深度频道V2取消订阅
-K 线频道
-K 线订阅
-K 线消息推送
-取消订阅
-公共强平订单频道
-公共强平订单订阅
-公共强平订单推送
-取消订阅
-合约统计信息频道
-订阅操作
-Contract_stats 推送
-取消订阅
-订单频道
-订单订阅
-订单推送
-取消订阅
-用户私有成交频道
-用户私有成交订阅
-用户私有成交推送
-取消订阅
-强制平仓频道
-清算订阅
-强制平仓推送
-取消订阅
-自动减仓频道
-自动减仓订阅
-自动减仓推送
-取消订阅
-平仓频道
-平仓订阅
-平仓信息推送
-取消订阅
-余额频道
-余额信息订阅
-余额更新推送
-取消订阅
-降低风险率频道
-降低风险率订阅
-降低风险率推送
-取消订阅
-仓位频道
-仓位订阅
-仓位信息推送
-取消订阅
-仓位 Adl 排名频道
-仓位 Adl 订阅
-仓位 Adl 信息推送
-取消订阅
-自动订单频道
-自动订单订阅
-自动订单消息推送
-取消订阅
-账户交易 API
-Websocket 交易 API
-登录
-下单
-批量下单
-订单取消
-取消所有 Id 列表内的订单
-取消匹配的未结束订单
-修改订单
-获取订单列表
-查询订单详情
-#
-Gate 永续合约 WebSocket v4
+# Gate 永续合约 WebSocket v4
 Gate 提供简单而强大的 Websocket API，将 Gate BTCUSDT 永续合约交易状态集成到您的业务或应用程序中。
-我们在
-Python
-和
-Golang
-中有语言绑定，将来还会有更多！您可以在右侧的深色区域中查看代码示例，并且可以通过右上角的选项卡切换示例的编程语言
-#
-服务地址
+我们在 Python 和 Golang 中有语言绑定，将来还会有更多！您可以在右侧的深色区域中查看代码示例，并且可以通过右上角的选项卡切换示例的编程语言
+# 服务地址
 我们提供 BTC/USDT 结算永续合约交易服务器地址，您可以根据自己的情况选择其中之一
-#
-BTC Contract
+# BTC Contract
 地址列表:
-线上交易:
-wss://fx-ws.gateio.ws/v4/ws/btc
-模拟盘交易:
-wss://fx-ws-testnet.gateio.ws/v4/ws/btc
-#
-USDT Contract
+- 线上交易: wss://fx-ws.gateio.ws/v4/ws/btc
+- 模拟盘交易: wss://fx-ws-testnet.gateio.ws/v4/ws/btc
+# USDT Contract
 地址列表:
-线上交易:
-wss://fx-ws.gateio.ws/v4/ws/usdt
-线上SBE:
-wss://fx-ws.gateio.ws/v4/ws/usdt/sbe
-模拟盘交易:
-wss://ws-testnet.gate.com/v4/ws/futures/usdt
+- 线上交易: wss://fx-ws.gateio.ws/v4/ws/usdt
+- 线上SBE: wss://fx-ws.gateio.ws/v4/ws/usdt/sbe
+- 模拟盘交易: wss://ws-testnet.gate.com/v4/ws/futures/usdt
 TIP
 建议使用SBE以获取更快的行情和更小的带宽成本
 WARNING
-如果你使用老的服务地址(
-wss://fx-ws.gateio.ws/v4/ws
-或
-wss://fx-ws-testnet.gateio.ws/v4/ws
-), 将默认是 BTC 结算的 websocket 服务.
-#
-变更日志
+如果你使用老的服务地址(wss://fx-ws.gateio.ws/v4/ws 或 wss://fx-ws-testnet.gateio.ws/v4/ws), 将默认是 BTC 结算的 websocket 服务.
+# 变更日志
 WebSocket 应用示例
-# !/usr/bin/env python
-# coding: utf-8
-import
-hashlib
-import
-hmac
-import
-json
-import
-logging
-import
-time
-import
-threading
-from
-websocket
-import
-WebSocketApp
-logging
-.
-basicConfig
-(
-level
-=
-logging
-.
-INFO
-)
-logger
-=
-logging
... (diff truncated, total 25621 lines) ...
```
