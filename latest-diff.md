<!-- has_changes=true date=2026-07-07 -->
# Exchange API Changelog Diff

Generated: 2026-07-07 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (131907 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (89162 bytes)

- [OK] OKX V5 (`okx`): no change (200456 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 15 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (34939 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120249 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index d814ec6..a5ced9b 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,10 @@
+2026-07-06​
+REST API​
+- Integration Guidance [UPDATE]
+  - Add Open API domains for Japan region users.
+2026-07-01​
+REST API​
+- Get Internal Deposit Records [UPDATE]
+  - Add new response field complianceStatus (internal transfer compliance collection status, only applicable to Bybit Turkey site users)
 2026-07-02​
 REST API​

```
