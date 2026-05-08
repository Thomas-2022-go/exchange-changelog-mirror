<!-- has_changes=true date=2026-05-08 -->
# Exchange API Changelog Diff

Generated: 2026-05-08 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128717 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (85776 bytes)

- [OK] OKX V5 (`okx`): no change (188233 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (77799 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 11 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139392 bytes)



## Changes

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index bb4fbd3..cb791b3 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,4 +1,6 @@
 WARNING
 The Pro API is currently in beta testing and should not be used in production trading environments.
+2026.05.08#
+[Margin Deprecate] Get ETF Info: Deprecated the /api/v3/etf/info endpoint.
 2026.04.28#
 [Modify] Get Account Ledger：

```
