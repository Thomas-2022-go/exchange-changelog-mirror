<!-- has_changes=true date=2026-10-30 -->
# Exchange API Changelog Diff

Generated: 2026-10-30 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 22 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (219574 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [OK] Bybit V5 (`bybit`): no change (99034 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 32 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (158964 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index bd65c25..33439b3 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -1,5 +1,16 @@
 # CHANGELOG for Binance's API
 
-**Last Updated: 2026-10-27**
+**Last Updated: 2026-10-30**
+
+### 2026-10-30
+
+REST and WebSocket API:
+
+- Reminder that SBE 3:3 schema will be retired on 2026-11-09,
+  [6 months after being deprecated](faqs/sbe_faq.md#sbe-schema).
+- The [SBE lifecycle for Production](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/sbe_schema_lifecycle_prod.json) has
+  been updated to reflect this change.
+
+---
 
 ### 2026-10-27

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index f45604f..68aea6e 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,2 +1,27 @@
+2026.11.02#
+[Modify] UTA REST Get Loan Market
+API Access Adjustment
+Effective Time: November 2, 2026, at 17:00 (UTC+8)
+1.
+The endpoint will be changed from a private endpoint to a public endpoint. Authentication will no longer be required.
+2.
+Orderbook Depth Parameter Adjustment
+The Orderbook depth parameter will be changed from an enumerated type to a String type, allowing users to specify a wider range of depth values, as well as FULL.
+3.
+API Rate Limit Weight Adjustment
+The endpoint's rate limit weight will be adjusted based on the requested Orderbook depth, as follows:
+Orderbook Depth
+| Orderbook Depth | API Weight
+| 1–20 | 5
+| 21–100 | 20
+| 101–500 | 50
+| 501 and above, or FULL | 250
+4.
+Rate Limit Pool and API Channel Adjustments
+Rate Limit Pool: Public Pool
+API Channel: Public
+5.
+Impact on Existing Users
+If you have already integrated this endpoint, these changes will not affect your existing API calls, and you can continue using the endpoint as usual. Please pay attention to the updated rate limit weights and adjust your request frequency accordingly.
 2026.10.21#
 [Remove] Classic REST Get Loan Market; Get Loan Market Interest Rate; Purchase; Modify Purchase; Get Purchase Orders; Redeem; Get Redeem Orders

```
