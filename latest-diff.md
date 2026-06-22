<!-- has_changes=true date=2026-06-22 -->
# Exchange API Changelog Diff

Generated: 2026-06-22 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 20 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (87509 bytes)

- [OK] OKX V5 (`okx`): no change (199931 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (82759 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (32707 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120099 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (138977 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index 86ffecf..3d6d528 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -1,5 +1,14 @@
 # CHANGELOG for Binance's API
 
-**Last Updated: 2026-06-10**
+**Last Updated: 2026-06-22**
+
+### 2026-06-22
+
+REST and WebSocket API:
+
+* Reminder that SBE 3:1 schema will be retired on 2026-06-29, [6 months after being deprecated](faqs/sbe_faq.md#sbe-schema).
+* The [SBE lifecycle for Production](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/sbe_schema_lifecycle_prod.json) has been updated to reflect this change.
+
+---
 
 ### 2026-06-10

```
