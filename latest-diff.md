<!-- has_changes=true date=2026-10-21 -->
# Exchange API Changelog Diff

Generated: 2026-10-21 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (137124 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (217976 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [OK] Bybit V5 (`bybit`): no change (97947 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 9 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (158964 bytes)



## Changes

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index c773e10..f45604f 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,2 +1,4 @@
+2026.10.21#
+[Remove] Classic REST Get Loan Market; Get Loan Market Interest Rate; Purchase; Modify Purchase; Get Purchase Orders; Redeem; Get Redeem Orders
 2026.09.21#
 [Modify] UTA REST Get Trade History Add the fillPnl field, FillPnl data before 2026.9.05 (UTC-8) cannot be queried and will return ""

```
