<!-- has_changes=true date=2026-07-08 -->
# Exchange API Changelog Diff

Generated: 2026-07-08 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (131907 bytes)

- [CHANGED] **Binance Derivatives (USDS-M / Coin-M / Options)** (`binance-derivatives`): 1883 diff lines

- [OK] OKX V5 (`okx`): no change (200456 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (83743 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (34939 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120249 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`)
- Source: https://developers.binance.com/docs/derivatives/change-log
- Raw: https://developers.binance.com/docs/derivatives/change-log

```diff
diff --git a/changelogs/binance-derivatives.txt b/changelogs/binance-derivatives.txt
index 03ed814..8b13789 100644
--- a/changelogs/binance-derivatives.txt
+++ b/changelogs/binance-derivatives.txt
@@ -1,1877 +1 @@
-Change Log
-2026-06-30​
-COIN-M Futures
-- GET /dapi/v1/constituents (Index Constituents)
-  - Response now includes weight and price fields for each constituent, consistent with the USDⓈ-M Futures endpoint (GET /fapi/v1/constituents).
-- GET /dapi/v1/pmAccountInfo (Classic Portfolio Margin Account Information) is no longer in use. Please use GET /fapi/v1/pmAccountInfo instead.
-- WebSocket Stream <pair>@indexPrice (Index Price Stream)
-  - The pair field in the response payload has been renamed from "i" to "s".
-  - The <pair>@indexPrice@1s (1000ms) variant has been removed. The stream is now available as <pair>@indexPrice only, with an update speed of 1000ms.
-2026-06-29​
-Time-sensitive Notice
-- POST /dapi/v1/countdownCancelAll (COIN-M Auto-Cancel All Open Orders / Countdown)
-  - The COIN-M countdown (auto-cancel) feature will be suspended on 2026-06-29 at 09:00 UTC (17:00 UTC+8) for the CM migration maintenance, and will be restored after CM resumes.
-  - Any countdown set before the suspension remains effective in the matching engine up until the snapshot is taken at maintenance shutdown.
-  - If the countdown timer set by the user is scheduled to fire after the maintenance snapshot, the countdown for those symbols will not take effect.
-2026-06-20​
-USDⓈ-M Futures
-- POST /fapi/v1/algoOrder (New Algo Order)
-  - Request Weight now follows the order rate limits: 1 on 10s order rate limit (X-MBX-ORDER-COUNT-10S) and 1 on 1min order rate limit (X-MBX-ORDER-COUNT-1M). IP weight remains 0.
-2026-06-16​
-Time-sensitive Notice
-- Please note the Futures COIN-M demo trading will be unavailable from 2026-06-16 02:00 till 10:00 UTC.
-- Update: The Futures COIN-M demo trading maintenance window is extended. The new window is from 2026-06-16 02:00:00 till 2026-06-22 10:00:00 (UTC). We appreciate your patience and understanding.
-2026-06-10​
-Effective Date: 2026-06-30
-COIN-M Futures architecture integration with USDⓈ-M Futures — REST endpoints, WebSocket streams, and account-level behavior changes. See Important CM-UM Integration Notice for the full list of affected endpoints and the action items. For the detailed timeline, please refer to the announcement.
-2026-06-02​
-Effective Date: 2026-06-02
-USDⓈ-M Futures
-- GET /fapi/v1/tradingSchedule (Trading Schedule)
-  - Extended time range from 7 days forward to 7 days backward and 7 days forward starting from the day prior to the query time.
-  - Added Korean equity market (KR_EQUITY) support. Korean equity market session types: REGULAR and NO_TRADING.
-- WebSocket Stream tradingSession (Trading Session Stream)
-  - Added Korean equity market support.
-  - Added new event type KR_EquityUpdate. Korean equity market session types: REGULAR and NO_TRADING.
-2026-05-11​
-Effective Date: 2026-05-13
-USDⓈ-M Futures
-- POST /fapi/v1/positionSide/dual
-  - New error code -4531: When changing UM dualSidePosition, the system will automatically sync CM dualSidePosition. If the CM account has any open position or open order, the sync cannot proceed and the UM position mode change will be rejected with error code -4531.
-  - Error payload:
-{
- "code": -4531,
- "msg": "Position mode change requires syncing UM and CM. Please close any open positions or orders in CM and try again."
-}
-  - Note: This error code is temporary and will only be active until CM enters Guard (approximately 1 month). After CM enters Guard, this error will no longer occur.
-2026-04-17​
-Portfolio Margin Pro
-- User Data Stream:
-  - Add new event PM_PRO_ACCOUNT_UPDATE, which pushes account asset status every 5 seconds.
-2026-04-15​
-European Options
-- Trade
-  - Cancel Multiple Option Orders - Corrected request weight from 1 to 5.
-2026-04-14​
-Portfolio Margin
-- The following REST Endpoints and WebSocket User Data Streams will be enabled from 2026-04-28:
-  - REST:
-    - POST /papi/v1/um/algo/order
-    - DELETE /papi/v1/um/algo/order
-    - DELETE /papi/v1/um/algo/allOpenOrders
-    - GET /papi/v1/um/algo/algoOrder
-    - GET /papi/v1/um/algo/openAlgoOrders
-    - GET /papi/v1/um/algo/allAlgoOrders
-  - Websocket:
-    - ALGO_UPDATE: algo order update event
-- The following REST Endpoints will be deprecated from 2026-04-28
-  - REST:
-    - POST /papi/v1/um/conditional/order
-    - DELETE /papi/v1/um/conditional/order
-    - DELETE /papi/v1/um/conditional/allOpenOrders
-    - GET /papi/v1/um/conditional/allOrders
-    - GET /papi/v1/um/conditional/openOrders
-    - GET /papi/v1/um/conditional/openOrder
-    - GET /papi/v1/um/conditional/orderHistory
-Please refer to announcement for API replacement
-2026-04-13​
-Portfolio Margin and Portfolio Margin Pro
-New REST APIs:
-- POST /sapi/v1/portfolio/margin-call-level : Set the margin call level for a Portfolio Margin account. When the account's uniMMR drops to the specified level, a notification will be sent via email and SMS.
-- GET /sapi/v1/portfolio/margin-call-level : Get the margin call level for a Portfolio Margin account.
-- DELETE /sapi/v1/portfolio/margin-call-level : Delete the margin call level for a Portfolio Margin account.
-2026-04-10​
-Effective Date: 2026-04-14
-COIN-M Futures / Portfolio Margin and Portfolio Margin Pro
-- POST /dapi/v1/positionSide/dual and POST /papi/v1/cm/positionSide/dual
-  - CM dualSidePosition must now stay consistent with UM. If CM dualSidePosition is already the same as UM, changing it will be rejected.
-USDⓈ-M Futures
-- Liquidation Order Streams (<symbol>@forceOrder) and All Market Liquidation Order Streams (!forceOrder@arr)
-  - Updated description: changed "only the latest one liquidation order" to "only the largest one liquidation order" within 1000ms.
-2026-04-09​
-Portfolio Margin
-- User Data Stream
-  - Event: Margin Order Update - Added new fields to the executionReport event payload: Cs, pl, pL, pY, eR.
-2026-04-08​
-Portfolio Margin
-New REST APIs:
-- POST /papi/v1/um/stock/contract : sign TradFi-Perps agreement contract
-2026-04-06​
-USDⓈ-M Futures / COIN-M Futures / Portfolio Margin and Portfolio Margin Pro
-- GET /fapi/v1/forceOrders, GET /dapi/v1/forceOrders, GET /papi/v1/um/forceOrders and GET /papi/v1/cm/forceOrders
-  - Added note: Only support querying data in the past 90 days.
-2026-04-02​
-USDⓈ-M Futures
-- WebSocket
-  - Updated important websocket change notice with legacy URL decommissioning date: 2026-04-23.
-2026-03-19​
-USDⓈ-M Futures / COIN-M Futures
-- GET /fapi/v1/historicalTrades and GET /dapi/v1/historicalTrades
-  - Updated data availability from the last 3 months to the last 1 month.
-2026-03-16​
-USDⓈ-M Futures
-- Websocket Market Streams
-  - Add new field ap in Mark-Price-Stream and Mark-Price-Stream-for-All-market to show mark price moving average.
-2026-03-11​
-Option
-- Effective on 2026-03-19
-- Self-Trade Prevention:
-  - Similar to USDⓈ-M Futures, Self-Trade Prevention (aka STP) is added to the system. This prevents orders from matching with orders from the same account, or accounts under the same tradeGroupId
-  - User can set selfTradePreventionMode when placing new orders. All option symbols support the following STP mode:
-    - EXPIRE_MAKER: expire maker order when STP trigger
-    - EXPIRE_TAKER: expire taker order when STP trigger
-    - EXPIRE_BOTH: expire taker and maker order when STP trigger
-- REST Update:
-  - New order status EXPIRED_IN_MATCH - This means that the order expired due to STP being triggered.
-  - Add optional parameter selfTradePreventionMode in the endpoints below to set order's STP mode:
-    - POST /eapi/v1/order
-    - POST /eapi/v1/batchOrders
-  - Add new field selfTradePreventionMode in response of the endpoints below to show order's STP mode:
-    - POST /eapi/v1/order
-    - POST /eapi/v1/batchOrders
-    - GET /eapi/v1/order
-    - GET /eapi/v1/openOrders
-    - PUT /eapi/v1/order
-    - PUT /eapi/v1/batchOrders
-    - DELETE /eapi/v1/order
-    - DELETE /eapi/v1/batchOrders
-- WEBSOCKET User Data Stream:
-  - Add new field V in ORDER_TRADE_UPDATE to order STP mode.
-2026-03-05​
-USDⓈ-M Futures
-- WebSocket
-  - Add important websocket change notice.
-  - Added URL PATH section to all websocket market stream pages indicating the new base URL path (/public, /market).
-  - Added URL PATH section to all user data stream event pages indicating the new base URL path (/private).
-2026-01-09​
-Portfolio Margin and Portfolio Margin Pro
-- New endpoints for switch to Delta Mode:
-  - POST /sapi/v1/portfolio/delta-mode: Switch the Delta Mode for existing PM PRO / PM RETAIL accounts.
-  - GET /sapi/v1/portfolio/delta-mode: Query the Delta mode status of current account.
-2026-01-07​
-Option
-- New REST APIs:
-  - GET /eapi/v1/commission: query user commission rate
-2025-12-29​
-USDⓈ-M Futures
-- The parameter "filterType": "MAX_NUM_ALGO_ORDERS" has been removed from the endpoint GET /fapi/v1/exchangeInfo. The condtional order limits is 200 across all symbols.
-- Effective on 2025-12-31, field nq will be available in <symbol>@aggTrade stream. For this new field, only normal market trades will be aggregated， which means the trades involving RPI orders won't be aggregated.
-2025-12-11​
-USDⓈ-M Futures
-- New REST APIs:
-  - GET /fapi/v1/tradingSchedule: query trading session schedules for a one-week period
-  - POST /fapi/v1/stock/contract: sign TradFi-Perps agreement contract
-- New Websocket API:
-  - tradingSession: query current trading session information
-2025-12-10​
-- Since conditional orders have been migrated to the Algo Service, the event CONDITIONAL_ORDER_TRIGGER_REJECT will be deprecated effective December 15, 2025. Any conditional order rejection reasons are provided within the ALGO_UPDATE event.
-2025-12-09​
-COIN-M Futures
-- Effective on 2025-12-10, Order expire reason field er will be available in ORDER_TRADE_UPDATE stream.
-2025-11-25​
-USDⓈ-M Futures
-- Effective on 2025-11-26, RPI commisson fee is available in the response of User Commission Rate endpoint
-  - REST
-    - GET /fapi/v1/commissionRate
-- New endpoints to fetch RPI order book
-  - REST
-    - GET /fapi/v1/rpiDepth
-  - WebSocket
-    - <symbol>@rpiDepth@500ms
-2025-11-19​
-USDⓈ-M Futures
-- REST API
-  - GET /fapi/v1/symbolAdlRisk: New endpoints to query ADL risk rating
-2025-11-18​
-USDⓈ-M Futures
-- The RPI order is introduced to USDⓈ-M Futures
-  - New time-in-force ENUM value - RPI is supported in
-    - REST
-      - POST /fapi/v1/order
-      - POST /fapi/v1/batchOrders
-    - WebSocket
-      - order.place
-  - New fields in the market data response - Boolean "IsRPITrade" available in
-    - REST
... (diff truncated, total 1883 lines) ...
```
