<!-- has_changes=true date=2026-09-02 -->
# Exchange API Changelog Diff

Generated: 2026-09-02 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 19 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (214695 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [OK] Bybit V5 (`bybit`): no change (94713 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 11 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index f32930e..1562d08 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -1,5 +1,13 @@
 # CHANGELOG for Binance's API
 
-**Last Updated: 2026-07-27**
+**Last Updated: 2026-09-02**
+
+### 2026-09-02
+
+#### FIX API
+
+* Removed the top-level `Symbol (55)` field from `ListStatus <N>` in the [QuickFIX Order Entry schema](./fix/schemas/spot-fix-oe.xml) and API documentation since, as [previously announced](#2025-11-28) the API no longer emits this field.
+
+---
 
 ### 2026-07-27

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index babd4b5..1e88015 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,2 +1,6 @@
+2026.09.04#
+New error code
+| Error Code | Message
+| 110188 | Too many requests right now. The system is busy. Please try again late.
 2026.08.27 V2 Upgrade#
 1.

```
