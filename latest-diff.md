<!-- has_changes=true date=2026-09-18 -->
# Exchange API Changelog Diff

Generated: 2026-09-18 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 25 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (217257 bytes)

- [CHANGED] **Bitget (Spot + Futures)** (`bitget`): 9 diff lines

- [OK] Bybit V5 (`bybit`): no change (95421 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42424 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (124213 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index 1562d08..d2dc26c 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -1,5 +1,19 @@
 # CHANGELOG for Binance's API
 
-**Last Updated: 2026-09-02**
+**Last Updated: 2026-09-18**
+
+### 2026-09-18
+
+REST and WebSocket API:
+
+* Reminder that SBE 3:2 schema will be retired on 2026-09-25, [6 months after being deprecated](./faqs/sbe_faq.md#regarding-legacy-support).
+* The [SBE lifecycle for Production](./sbe/schemas/sbe_schema_lifecycle_prod.json) has been updated to reflect this change.
+
+FIX API:
+
+* Reminder that FIX SBE 1:0 schema will be retired on 2026-09-25, [6 months after being deprecated](./faqs/sbe_faq.md#regarding-legacy-support).
+* The [FIX SBE lifecycle for Production](./sbe/schemas/sbe_fix_schema_lifecycle_prod.json) has been updated to reflect this change.
+
+---
 
 ### 2026-09-02

```

### Bitget (Spot + Futures) (`bitget`)
- Source: https://www.bitget.com/api-doc/common/changelog
- Raw: https://www.bitget.fit/api-doc/common/changelog

```diff
diff --git a/changelogs/bitget.txt b/changelogs/bitget.txt
index ae205ac..74efbdd 100644
--- a/changelogs/bitget.txt
+++ b/changelogs/bitget.txt
@@ -33,3 +33,3 @@ Maintenance margin = Position value × maintenance margin rate
 Cross margin account's margin ratio = (maintenance margin + partial liquidation transaction fees) ÷ Account equity.
 Both maintenance margin and partial liquidation transaction fees are calculated by adding the position size and the open order size.
-Reality Trading Guide
+Quick Start

```
