<!-- has_changes=true date=2026-10-26 -->
# Exchange API Changelog Diff

Generated: 2026-10-26 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (137124 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [OK] OKX V5 (`okx`): no change (217976 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 17 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42580 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (158964 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 198c079..5d52404 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,12 @@
+2026-10-20​
+REST API​
+- Get Referral Commission Records [NEW]
+  - Add POST /v5/referral/commission/records to query referral commission records.
+- Get Referral Campaign Rewards [NEW]
+  - Add POST /v5/referral/campaign/rewards to query referral rules and campaign task rewards.
+- Get Referral User Identity Profile [NEW]
+  - Add POST /v5/referral/user/identity-profile to query the authenticated user's referral identity and available commission information.
+- Get Referral User Invitations [NEW]
+  - Add POST /v5/referral/user/invitations to query the authenticated user's invitation records.
 2026-10-14​
 REST API​

```
