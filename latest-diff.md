<!-- has_changes=true date=2026-07-22 -->
# Exchange API Changelog Diff

Generated: 2026-07-22 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132274 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (206336 bytes)

- [CHANGED] **Bitget (Spot + Futures)** (`bitget`): 429 diff lines

- [CHANGED] **Bybit V5** (`bybit`): 12 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (35340 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120249 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### Bitget (Spot + Futures) (`bitget`)
- Source: https://www.bitget.com/api-doc/common/changelog
- Raw: https://www.bitget.fit/api-doc/common/changelog

```diff
diff --git a/changelogs/bitget.txt b/changelogs/bitget.txt
index bc64963..538b638 100644
--- a/changelogs/bitget.txt
+++ b/changelogs/bitget.txt
@@ -1,383 +1,41 @@
-Changelog
-[January 29, 2026] Transfer Records Enable idLessThan Pagination Mode​
-Interface:
-- /api/v2/spot/account/transferRecords Changes：
-- Enabled idLessThan pagination mode for retrieving transfer records; deprecated pageNum.
-[January 7, 2026] Optimization of Push Frequency for Websocket Order Book Channel (books1) in Classic Account (v2)​
-Websocket: Order Book Channel
- Adjustment Content: The push frequency of the order book channel (books1) is optimized to 10ms.
-[January 6, 2026] Added 'off_close' (Delisting Liquidation) to the enum values of the response parameter 'orderSource'.​
-Interface:
-- /api/v2/mix/order/orders-pending, /api/v2/mix/order/orders-history Changes：
-- Added 'off_close' (Delisting Liquidation) to the enum values of the response parameter 'orderSource'.
-[November 27, 2025] A new return field, 'liqPrice', has been added to the futures historical order.​
-Interface:
-- /api/v2/mix/order/orders-history Changes：
-- A new return field, 'liqPrice', has been added to the futures historical order.
-[November 26, 2025] Websocket Added new ADL notification channel​
-Websocket: ADL notification channel
- Changes: Websocket Added new ADL notification channel
-[November 26, 2025] Add new FAQ Q15​
-Changes:Add new FAQ Q15
-[November 19, 2025] New isRwa Field Added to Get Contract Information API Response​
-Interface:
-- /api/v2/mix/market/contracts
-Changes：
-- New isRwa Field Added to Get Contract Information API Response
-[November 8, 2025] WebSocket has added a new futures equity channel.​
-Websocket: futures equity channel
- Changes: WebSocket has added a new futures equity channel.
-[November 8, 2025] WebSocket Supports Broker API Code​
-Websocket: place order channel
- Changes: The order placement channel supports passing the Broker API Code to receive rebates.
-[November 7, 2025] Add Maximum Openable Quantity API​
-Interface:
-- /api/v2/mix/account/max-open
-Changes：
-- Add Maximum Openable Quantity API
-[November 7, 2025] Add Estimated Liquidation Price API​
-Interface:
-- /api/v2/mix/account/liq-price
-Changes：
-- Add Estimated Liquidation Price API
-[November 6, 2025] New broker commission inquiry interface added​
-Interface:
-- /api/v2/broker/total-commission
-- /api/v2/broker/order-commission
-- /api/v2/broker/rebate-info
-Changes：
-- New broker commission inquiry interface added
-[October 21, 2025] Add an endpoint for querying symbol with isolated margin mode in futures.​
-Interface: /api/v2/mix/account/isolated-symbols
- Changes：
-- Add an endpoint for querying symbol with isolated margin mode in futures.
-[October 21, 2025] Optimization of the spot historical plan order endpoint​
-Interface: /api/v2/spot/trade/history-plan-order
- Changes： -The request parameters symbol, startTime, and endTime are changed to optional.
-[October 14, 2025] Notice: Classic Account Error Code Optimization​
-Scope of Impact:
-Classic Account v2-related APIs
- Optimization Content:
-- Unified error code mapping: Resolves the issue where "different error codes correspond to the same error message", ensuring one code maps to one message and reducing recognition confusion.
-- Standardized error message matching: Fixes the problem where "different error messages correspond to the same error code", enabling accurate matching between messages and codes and improving troubleshooting efficiency.
-[September 11, 2025] Newly Added Interfaces Related to union Margin​
-Changes：
-- Newly Added — Query the USDT amount required for switching from union margin to single-currency margin /api/v2/mix/account/switch-union-usdt
-- Newly Added — union Margin Conversion and Repayment API /api/v2/mix/account/union-convert
-- Newly Added — union Margin Configuration Parameter API /api/v2/mix/account/union-config
-- Newly Added — union Margin Currency Transfer Limit API /api/v2/mix/account/transfer-limits
-- Newly Added — New union margin parameters in the WS Account Channel: unionTotalMargin (Margin Amount), unionAvailable (Available Margin), unionMm (Maintenance Margin), assetMode (Account Mode)
-- Newly Added — New assetMode (Account Mode) parameter in the WS Position Channel
-[September 4, 2025] Notice: Adjustment to the transferId field in the sub-main account transfer records retrieval function. The transferId will be updated to the one returned during sub-main account transfers.​
-Interface: /api/v2/spot/account/sub-main-trans-record
- Changes：
-- Previous generation rule: for transferId: Auto-incrementing ID
-- New generation rule: for transferId: Snowflake algorithm
-[September 2, 2025] Add reason field for Get Upgrade Status​
-Interface: /api/v2/spot/account/upgrade-status
- Changes：
-- Add reason field for Get Upgrade Status
-[August 28, 2025] Notice: Optimization of Push Frequency for Websocket Order Book Channel (books1) in Classic Account (v2)​
-Websocket: Order Book Channel
- Adjustment Content: The push frequency of the order book channel (books1) is optimized to 20ms. The symbols for this optimization are: BTCUSDT, ETHUSDT, XRPUSDT, SOLUSDT, SUIUSDT, DOGEUSDT, ADAUSDT, PEPEUSDT, LINKUSDT, HBARUSDT
-[August 11, 2025] Agent commission API query supports fee deduction​
-Interface：/api/broker/v1/agent/commission-distribution;/api/broker/v1/agent/customer-commissions;
- Changes：
-- Agent commission API query supports fee deduction details
-[August 11, 2025] API Global rate Limit Adjustment​
-Changes：
-- There is an overall rate limit rule of 6,000 times per IP per minute. After the rate limit is triggered, the recovery time is adjusted from 1 minute to 5 minutes.
-[August 6, 2025] Add unrealizedPL field for sub-account futures asset info​
-Interface：/api/v2/broker/account/subaccount-future-assets
- Changes：
-- Add unrealizedPL field for sub-account futures asset info
-[August 6, 2025] Add marginCoin field for historical transaction details​
-Interface：/api/v2/mix/order/fill-history
- Changes：
-- Add marginCoin field for historical transaction details
-[August 4, 2025] Delisting of Futures Demo Pairs​
-Futures demo pairs have been delisted. Please use the demo trading for simulated trading.
-[July 31, 2025] Optimization of the futures order placement interface logic​
-Interface： /api/v2/mix/order/place-order
-Changes：
-- before: In hedge mode, if the existing quantity is equal to the limit close order of the position, a newly added market close order will report an error due to insufficient position and will not automatically cancel the limit order that has occupied the position.
-- after: In hedge mode, if the existing quantity is equal to the limit close order of the position, a newly added market close order will automatically cancel the limit order that has occupied the position (consistent with Web/APP).
-[July 29, 2025] Optimize ADL API ranking logic.​
-Interface：/api/v2/mix/position/adlRank Changes：
-- Optimize the ranking logic of the ADL API on the server side.Add a new field "rank" and deprecated the field "adlRank".
-[July 16, 2025] Add New Account Mode Switching API​
-Interface：/api/v2/spot/account/upgrade, /api/v2/spot/account/upgrade-status Adjustment:
-- Add New Account Mode Switching API
-[July 14, 2025] Futures leverage adjustment API supports setting long/short leverage ratios separately.​
-Interface： /api/v2/mix/account/set-leverage
- Changes：
-- Futures leverage adjustment API supports setting long/short leverage ratios separately.
-[July 14, 2025] Position take-profit/stop-loss API supports setting custom IDs for take-profit and stop-loss orders separately.​
-Interface： /api/v2/mix/order/place-pos-tpsl
- Changes：
-- Position take-profit/stop-loss API supports setting custom IDs for take-profit and stop-loss orders separately.
-[July 14, 2025] The interface for obtaining the list of historical contract positions has added a position mode field.​
-Interface： /api/v2/mix/position/history-position
- Changes：
-- The interface return parameters have added posMode (position mode), with enumeration values including one_way_mode (one-way position) and hedge_mode (hedge mode/two-way position).
-[July 8, 2025] WebSocket futures position channel adds mark price parameter​
-Channels: futures position channel Changes：
-- WebSocket futures position channel adds mark price parameter
-[July 1, 2025] WebSocket Adds Order Placement and Cancellation Channels​
-Channels: Place Order，Cancel Order
-Changes：
-- Adds Order Placement and Cancellation Channels
-[Jun 17, 2025]Spot merged trading depth, spot trading depth, futures merged depth interfaces: ts field adjustment​
-Interface：/api/v2/mix/market/merge-depth,/api/v2/spot/market/orderbook,/api/v2/spot/market/merge-depth
-Changes：
-- Spot merged trading depth, spot trading depth, and futures merged depth interfaces: ts field adjusted to matching engine timestamp
-[Jun 16, 2025] The ADL ranking interface has added the position direction.​
-Interface：/api/v2/mix/position/adlRank
- Changes：
-- The ADL ranking interface has added the position direction holdSide field。
-[June 09, 2025] Get Contract Information Adds Maximum Order Quantity Fields​
-Interface：/api/v2/mix/market/contracts
- Changes：
-- Added maxMarketOrderQty field for the maximum quantity of a single market order.
-- Added maxOrderQty field for the maximum quantity of a single limit order.
-[May 19, 2025] Update on Regular Release Date​
-The current fixed regular release date for backend is every Tuesday, Wednesday, and Thursday from 14:00 PM to 17:00 PM (UTC +8)(Except for emergency upgrade).
-During the regular release time window, the RestAPI may return 45001, 40725, or 40808 error responses. Users can retry after receiving these error responses. WebSocket connections may be disconnected during the release period. WebSocket users are advised to implement a reconnection mechanism in their code.
-[May 19,2025] Adjustment of the Spot place-plan-order API​
-Interface：/api/v2/spot/trade/place-plan-order
-Changes：
-- The force field was invalid when placing an order and has been deleted.
-[May 14, 2025] New version: Order-taking staff API Key creation interface adds currency pair range description.​
-Interface：/api/v2/copy/mix-trader/create-copy-api
- Changes：
-- New: Added description for order-taking currency pair range.
-[May 09, 2025] Obtain the adjustment of the input parameters for the current funding rate.​
-Interface：/api/v2/mix/market/current-fund-rate
-Changes：
-- Obtain that the request parameter symbol of the current funding rate is changed to be non-mandatory.
-[May 09, 2025] Optimized the API for retrieving spot assets of sub-accounts.​
-Interface：/api/v2/spot/account/subaccount-assets
-Changes：
-- Added pagination parameters: idLessThan (pagination cursor) and limit (items per page).
-- Added return field: id (cursor ID)
-[May 09, 2025] Optimized the API for querying announcements.​
-Interface：/api/v2/public/annoucements
-Changes：
-- New announcement types added
-product_updates: Product Updates
-security: Security
-api_trading: API Trading
-- Added pagination parameters: cursor (pagination cursor ID) and limit (items per page).
-- Deprecated announcement type: trading_competitions_promotions (Trading Competitions and Promotions)
-- The return field annDesc (Announcement Description) is deprecated.
-[May 08, 2025] Interface for adding leverage interest rate records​
-Interface： /api/v2/margin/interest-rate-record Changes：
-- The interface for adding leverage interest rate records supports users to query the interest rate record data based on the trading pairs.
-[May 08, 2025] Optimization of the query range for public transaction details of spot/contract.​
-Interface： /api/v2/spot/market/fills-history; /api/v2/mix/market/fills-history；
-Changes：
-- Adjust the time span from 7 days to 90 days, which means it supports querying public transaction data from the past three months.
-[May 08, 2025] Add preset stop - profit and stop - loss execution prices for contract orders.​
-Interface： /api/v2/mix/order/place-order
-Changes：
-- Add request parameters
-presetStopSurplusExecutePrice Preset stop-profit execution price
-presetStopLossExecutePrice Preset stop-loss execution price
-[May 08, 2025] Add "utime" to the WebSocket push for cross-margin/isolated-margin leverage order channels.​
-Channels: Cross-margin Leverage Order Channel, Isolated-margin Leverage Order Channel
-Changes：
-- Add to the push data utime
-[Apr 30,2025] For the trading details of the WS futures, push fields are added to the spot/futures depth channels.​
-Channels: futures Trading Details Channel, Spot Depth Channel, Contract Depth Channel
-Changes:
-- Add the clientOid field to the pushed information of the futures Trading Details Channel.
-- Add the seq field to the pushed information of the Spot Depth Channel and the futures Depth Channel.
-[Apr 23, 2025] Added groupType enumeration for get account bills.​
... (diff truncated, total 429 lines) ...
```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index f1671a7..07d09a7 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,7 @@
+2026-07-21​
+Websocket API​
+- Fast Order Response [UPDATE]
+  - Option now is available
+  - XML version upgrades to v2, added four response fields
 2026-07-16​
 REST API​

```
