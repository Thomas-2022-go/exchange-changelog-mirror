<!-- has_changes=true date=2026-05-25 -->
# Exchange API Changelog Diff

Generated: 2026-05-25 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 11 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [OK] OKX V5 (`okx`): no change (194741 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (79714 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (29217 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139416 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index f36102e..1c0073a 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -712,5 +712,5 @@ The following changes will be available on **2025-08-28 starting at 07:00 UTC**:
       * REST API
       * WebSocket API
-* New [`MAX_NUM_ORDER_LISTS`](filters.md#max-num-order-lists) filter will be enabled, limiting the number of order lists to 20 per symbol.
+* New [`MAX_NUM_ORDER_LISTS`](filters.md#max_num_order_lists) filter will be enabled, limiting the number of order lists to 20 per symbol.
 * New [`MAX_NUM_ORDER_AMENDS`](filters.md#max_num_order_amends) filter will be enabled, limiting each order to a maximum of 10 amendments.
 

```
