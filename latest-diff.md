<!-- has_changes=true date=2026-06-30 -->
# Exchange API Changelog Diff

Generated: 2026-06-30 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (131160 bytes)

- [CHANGED] **Binance Derivatives (USDS-M / Coin-M / Options)** (`binance-derivatives`): 26 diff lines

- [OK] OKX V5 (`okx`): no change (202930 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (82998 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 29 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120099 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`)
- Source: https://developers.binance.com/docs/derivatives/change-log
- Raw: https://developers.binance.com/docs/derivatives/change-log

```diff
diff --git a/changelogs/binance-derivatives.txt b/changelogs/binance-derivatives.txt
index d7a5e4e..6a33c25 100644
--- a/changelogs/binance-derivatives.txt
+++ b/changelogs/binance-derivatives.txt
@@ -1,9 +1,20 @@
 Change Log
+2026-06-29​
+Time-sensitive Notice
+- POST /dapi/v1/countdownCancelAll (COIN-M Auto-Cancel All Open Orders / Countdown)
+  - The COIN-M countdown (auto-cancel) feature will be suspended on 2026-06-29 at 09:00 UTC (17:00 UTC+8) for the CM migration maintenance, and will be restored after CM resumes.
+  - Any countdown set before the suspension remains effective in the matching engine up until the snapshot is taken at maintenance shutdown.
+  - If the countdown timer set by the user is scheduled to fire after the maintenance snapshot, the countdown for those symbols will not take effect.
+2026-06-20​
+USDⓈ-M Futures
+- POST /fapi/v1/algoOrder (New Algo Order)
+  - Request Weight now follows the order rate limits: 1 on 10s order rate limit (X-MBX-ORDER-COUNT-10S) and 1 on 1min order rate limit (X-MBX-ORDER-COUNT-1M). IP weight remains 0.
 2026-06-16​
 Time-sensitive Notice
+- Please note the Futures COIN-M demo trading will be unavailable from 2026-06-16 02:00 till 10:00 UTC.
 - Update: The Futures COIN-M demo trading maintenance window is extended. The new window is from 2026-06-16 02:00:00 till 2026-06-22 10:00:00 (UTC). We appreciate your patience and understanding.
 2026-06-10​
 Effective Date: 2026-06-30
-COIN-M Futures architecture integration with USDⓈ-M Futures — REST endpoints, WebSocket streams, and account-level behavior changes. See Important CM-UM Integration Notice for the full list of affected endpoints and the action items.
+COIN-M Futures architecture integration with USDⓈ-M Futures — REST endpoints, WebSocket streams, and account-level behavior changes. See Important CM-UM Integration Notice for the full list of affected endpoints and the action items. For the detailed timeline, please refer to the announcement.
 2026-06-02​
 Effective Date: 2026-06-02

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index 1e88672..a570dbe 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,4 +1,24 @@
 WARNING
 The Pro API is currently in beta testing and should not be used in production trading environments.
+2026.07.01#
+[Add] UTA REST Get Client IP Address
+[Add] UTA REST Get Fiat Price
+[Modify] UTA REST Get Klines
+The symbol field has been updated. You can query corresponding K-line data via the values below:
+{symbol}-index-price: Index price K-line for contract trading pairs
+{symbol}-mark-price: Mark price K-line for contract trading pairs
+{symbol}-premium-index: Premium index K-line for contract trading pairs
+[Modify] UTA REST Get Ticker
+New fields added in response: priceChange, priceChangePercent, indexPrice, markPrice
+[Modify] UTA REST Get Account Currency Assets (UTA) . Added response field:
+collateralStatus: platform-level margin collateral status
+[Modify] UTA Websocket Balance. Added push field cS: platform-level margin collateral status
+[Modify] Classic REST Get Deposit List & Classic REST Get Deposit Detail . Add new response value：
+Added preConfirms: Min number for balance confirmation
+Added confirms: Confirmation number for balance unlock
+Added currentConfirms：Current deposit confirmation number
+[Add] UTA WebSocket Public Channel Funding Fee
+[Add] UTA WebSocket Public Channel Mark Price
+[Modify] Classic Websocket / Futures Trading / Private Channels / Positions /contract/positionAll topic. Added Funding Fee Settlement pushes for All Positions, added param symbol in response field data
 2026.06.17#
 [Modify] UTA API Orderbook Websocket

```
