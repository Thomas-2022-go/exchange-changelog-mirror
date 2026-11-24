<!-- has_changes=true date=2026-11-24 -->
# Exchange API Changelog Diff

Generated: 2026-11-24 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 20 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (220592 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3488 bytes)

- [OK] Bybit V5 (`bybit`): no change (101402 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (45900 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (166885 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index 6b6fef5..4f9fb9f 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -1,5 +1,14 @@
 # CHANGELOG for Binance's API
 
-**Last Updated: 2026-11-11**
+**Last Updated: 2026-11-24**
+
+### 2026-11-24
+
+- Order Book depth now supports additional levels. This affects the following endpoints:
+  - REST API: [`GET /api/v3/depth`](rest-api.md#order-book)
+  - WebSocket API: [`depth`](web-socket-api.md#order-book)
+  - FIX Market Data: [MarketDataRequest `<V>`](fix-api.md#marketdatarequest)
+
+---
 
 ### 2026-11-11

```
