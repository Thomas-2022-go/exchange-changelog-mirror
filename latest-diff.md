<!-- has_changes=true date=2026-07-01 -->
# Exchange API Changelog Diff

Generated: 2026-07-01 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 26 diff lines

- [CHANGED] **Binance Derivatives (USDS-M / Coin-M / Options)** (`binance-derivatives`): 16 diff lines

- [OK] OKX V5 (`okx`): no change (202930 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 16 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (34939 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120099 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index 76c5a07..d766d64 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -1,5 +1,20 @@
 # CHANGELOG for Binance's API
 
-**Last Updated: 2026-06-24**
+**Last Updated: 2026-07-01**
+
+### 2026-07-01
+
+**Notice: The following changes will occur on 2026-07-07 and will take a few days to complete.**
+
+#### New Features
+
+* The new `symbolStatus` value `CANCEL_ONLY` can appear in Exchange Information responses.
+    * REST API: `GET /api/v3/exchangeInfo`
+    * WebSocket API: `exchangeInfo`
+* REST and WebSocket API SBE schema [spot_3_5.xml](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot_3_5.xml)
+  * The current schema 3:4 [spot_3_4.xml](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot_3_4.xml) is deprecated and will be retired in 6 months as per our schema deprecation policy.
+  * Changes in schema 3:5:
+    * Updated `symbolStatus` enum: new variant `CANCEL_ONLY`
+---
 
 ### 2026-06-24

```

### Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`)
- Source: https://developers.binance.com/docs/derivatives/change-log
- Raw: https://developers.binance.com/docs/derivatives/change-log

```diff
diff --git a/changelogs/binance-derivatives.txt b/changelogs/binance-derivatives.txt
index 6a33c25..03ed814 100644
--- a/changelogs/binance-derivatives.txt
+++ b/changelogs/binance-derivatives.txt
@@ -1,3 +1,11 @@
 Change Log
+2026-06-30​
+COIN-M Futures
+- GET /dapi/v1/constituents (Index Constituents)
+  - Response now includes weight and price fields for each constituent, consistent with the USDⓈ-M Futures endpoint (GET /fapi/v1/constituents).
+- GET /dapi/v1/pmAccountInfo (Classic Portfolio Margin Account Information) is no longer in use. Please use GET /fapi/v1/pmAccountInfo instead.
+- WebSocket Stream <pair>@indexPrice (Index Price Stream)
+  - The pair field in the response payload has been renamed from "i" to "s".
+  - The <pair>@indexPrice@1s (1000ms) variant has been removed. The stream is now available as <pair>@indexPrice only, with an update speed of 1000ms.
 2026-06-29​
 Time-sensitive Notice

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index c317899..0102e29 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,11 @@
+2026-07-02​
+Websocket API​
+- SBE Fast Order [UPDATE]
+  - The Fast Order XML template version is updated to 1.
+  - A new response field, liquidity, is added to indicate whether the corresponding order execution is Maker or Taker.
+2026-06-29​
+REST API​
+- Get Order List [UPDATE]
+  - Add new response fields: fromAccount, toAccount, externalEventType
 2026-06-23​
 REST API​

```
