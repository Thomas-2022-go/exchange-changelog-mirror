<!-- has_changes=true date=2026-07-31 -->
# Exchange API Changelog Diff

Generated: 2026-07-31 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132459 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (212390 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3590 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 43 diff lines

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 21 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145596 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index bd3d854..d5e3b21 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -4,4 +4,27 @@ REST API​
   - Kazakhstan (KAZ) derivatives: SMP is now mandatory for all derivative orders
   - Turkey (TUR), Kazakhstan (KAZ), Georgia (GEO) spot: smpType of None, invalid value, or missing value is automatically set to CancelMaker
+2026-07-30​
+REST API​
+- Get Account Instruments Info [UPDATE]
+  - Updated the RPI permission model from account-level to symbol-level. Users can now submit RPI orders on any symbol that supports RPI, without requiring account-specific RPI permissions. Check the definition of isPublicRpiand and myRpiPermission
+- Get Coin Delta Amount [UPDATE]
+  - Add new response field riskUnitDelta (risk unit delta value)
+- Create RFQ [UPDATE]
+  - Added hedge request parameter: optional Delta Hedge leg for linear perpetual / linear delivery futures. Supports category, symbol, side, qty, and optional price
+  - When anonymous is true, the deskCode returned by Get RFQs is an empty string
+- Create Quote [UPDATE]
+  - Quoting the hedge leg is optional. Include it in quoteBuyList or quoteSellList. If the RFQ carries a hedge price, omitting the price when quoting will fall back to the RFQ price
+- Execute Quote [UPDATE]
+  - Added isHedge request parameter: set to true to simultaneously execute the hedge leg in the RFQ. Direction is determined by quoteSide. Default: false
+- Get RFQs (real-time) [UPDATE]
+  - Added response fields: anonymous (boolean), hedge (array of objects with category, symbol, side, qty, price)
+- Get RFQs [UPDATE]
+  - Added response fields: anonymous (boolean), hedge (array of objects with category, symbol, side, qty, price)
+- Get Quotes (real-time) [UPDATE]
+  - Added response field anonymous (boolean); added isHedge (boolean) to each item in quoteBuyList and quoteSellList
+- Get Quotes [UPDATE]
+  - Added response field anonymous (boolean); added isHedge (boolean) to each item in quoteBuyList and quoteSellList
+- Get RFQ Details [NEW]
+  - New endpoint to retrieve historical RFQ information with full details including active quotes (quoteList) and trade execution results (tradeLegs)
 2026-07-28​
 REST API​
@@ -128,4 +151,10 @@ REST API​
 - Submit Deposit Originator Info [NEW]
   - A new endpoint has been introduced to submit the originator's compliance information when a deposit is flagged for Travel Rule review.
+- Get Deposit Records (on-chain) [UPDATE]
+  - add response field travelRuleStatus
+- Get Sub Deposit Records (on-chain) [UPDATE]
+  - add response field travelRuleStatus
+- Get Sub Account Deposit Records [UPDATE]
+  - add response field travelRuleStatus
 - Get Fee Group Structure [UPDATE]
   - Add a new fee group groupId="9", G9(TradFi). There are no symbols in this group until June 16, 2026

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index 6df4d09..1e799a4 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -2,5 +2,5 @@ WARNING
 The Pro API is currently in beta testing and should not be used in production trading environments.
 2026.08.03#
-Discontinuation of the "Hidden Order" Feature#
+1. Discontinuation of the "Hidden Order" Feature#
 [Modify] Classic REST
 No longer supports the hidden, iceberg and visibleSize parameters. Requests containing these parameters will be rejected with error code "400413" with error message "Invaild order type, hidden and iceberg orders are not supported any more." .
@@ -10,4 +10,9 @@ No longer supports the hidden, iceberg and visibleSize parameters. Requests cont
 | 3 | Futures Trading | Add Order , Add Order Test , Batch Add Orders , Add Take Profit And Stop Loss Order
 | 4 | Copy Trading | Add Order, Add Order Test, Add Take Profit And Stop Loss Order
+2. Endpoints Update#
+[Add] UTA REST Get Sub-account List
+[Add] UTA REST KCS Fee Deduction Management
+[Add] UTA REST Get Deposit History
+[Add] UTA REST Get Withdrawal History
 2026.07.17#
 [Modify] UTA REST/WebSocket Get Order Book & Subscription

```
