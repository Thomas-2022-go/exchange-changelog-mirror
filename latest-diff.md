<!-- has_changes=true date=2026-04-24 -->
# Exchange API Changelog Diff

Generated: 2026-04-24 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 17 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (85776 bytes)

- [OK] OKX V5 (`okx`): no change (186803 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (76797 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (28151 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116546 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139384 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index 7db4415..140eb18 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -3,4 +3,12 @@
 **Last Updated: 2026-04-17**
 
+### 2026-04-17
+
+The following will occur on **2026-05-05 at approximately 10:00 UTC**.
+
+* The update speed of the below SBE Market Data Streams will be changed **from 50ms to 25ms**:
+  * SBE Market Data Streams: [Diff Depth Streams](sbe-market-data-streams.md#diff-depth-streams)
+  * FIX SBE: [MarketDataIncrementalDepth](fix-api.md#marketdataincrementaldepth)
+
 
 ---

```
