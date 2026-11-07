<!-- has_changes=true date=2026-11-07 -->
# Exchange API Changelog Diff

Generated: 2026-11-07 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (137687 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (219577 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 15 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (44528 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (164576 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 9960cf1..12dfc66 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,10 @@
+2026-11-09​
+REST API​
+- Set Auto Repay Mode [UPDATE]
+  - When currency is omitted and autoRepayMode is enabled, the setting is now a global switch: it also applies to currencies that become borrowable after the setting is saved. Single-currency settings are unchanged.
+- Get Trade Auto Repay [NEW]
+  - Add GET /v5/spot-margin-trade/get-trade-auto-repay to retrieve the Unified account's trade auto repayment switch.
+- Set Trade Auto Repay [NEW]
+  - Add POST /v5/spot-margin-trade/set-trade-auto-repay to update the Unified account's trade auto repayment switch.
 2026-11-05​
 REST API​

```
