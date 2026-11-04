<!-- has_changes=true date=2026-11-04 -->
# Exchange API Changelog Diff

Generated: 2026-11-04 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (137687 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (219577 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 23 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (44528 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (164576 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 8b95625..721bc4a 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,18 @@
+2026-11-04​
+REST API​
+- Get Deposit Records (on-chain) [UPDATE]
+  - Add response field requestId.
+- Get Sub Deposit Records (on-chain) [UPDATE]
+  - Add response field requestId.
+2026-11-03​
+REST API​
+- Get API Key Information [UPDATE]
+  - Add the Compliance permission category. When granted, it returns ComplianceAppeal, which permits querying TM Onchain appeal status and submitting related materials.
+- Modify Master API Key [UPDATE]
+  - Support granting or revoking the ComplianceAppeal permission through the Compliance category. This is available only to Bybit global master accounts with read-write API keys.
+- Submit Quote [UPDATE]
+  - Add optional request parameter cancelAfterMs to automatically cancel an Event Contract quote. 0 uses quoteMaxValidMs; non-zero values cannot exceed quoteMaxValidMs.
+- Cancel All Quotes [NEW]
+  - Add POST /v5/event/cancel-all to cancel all active Event Contract quotes for a specified symbol.
 2026-10-29​
 REST API​

```
