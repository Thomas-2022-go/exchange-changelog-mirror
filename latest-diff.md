<!-- has_changes=true date=2026-08-12 -->
# Exchange API Changelog Diff

Generated: 2026-08-12 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132459 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 14 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 27 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (36766 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145596 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 763d12c..43ff114 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -49,7 +49,7 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 受影响的订单类型有：post_only、mmp_and_post_only、rpi（Retail Price Improvement）。
 其他订单类型如 limit（普通限价单）、market（市价单）、ioc、fok 订单推送行为保持不变。
+2026-08-11
 RPI 挂单价格间距与可见性规则更新
-最近更新：2026年8月7日
-RPI 挂单价格间距规则即将调整。间距规则的交叉校验与价格档位校验仅参考首个可见的对手方 RPI，不参考已隐藏的 RPI。RPI 的可见性同时决定 books-rpi 订单簿上展示的可成交 RPI 深度。本次不涉及任何接口、参数、枚举值或错误码的变更。本次变更预计于 2026年8月11日 上线。
+RPI 挂单价格间距规则的交叉校验与价格档位校验现仅参考首个可见的对手方 RPI，不参考已隐藏的 RPI。RPI 的可见性同时决定 books-rpi 订单簿上展示的可成交 RPI 深度。本次不涉及任何接口、参数、枚举值或错误码的变更。
 价格间距规则
 - 交叉校验与价格档位校验仅参考首个可见的对手方 RPI，不参考已隐藏的 RPI

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 47d0e25..bfae39a 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -3,11 +3,20 @@ REST API​
 - Get Transaction Log [UPDATE]
   - Add new response field displayType: display type for the transaction log entry, consistent with the UI display
+  - Add new "type", DIVIDEND_SETTLEMENT，indicates stock perps dividend
+- Get Full Depth Orderbook [UPDATE]
+  - Support Futures
+- Get Airdrop Products [UPDATE]
+  - Add new response fields personalApy and multiplier under yields: personal APR and personal coefficient for each yield coin
+  - Add new response field personalApy at the product level: sum of personal APR across all yield coins
+Websocket API​
+- Full Orderbook [UPDATE]
+  - Support Futures
 2026-08-09​
 REST API​
 - Integration Guidance
-  - Add Rest API integration method for Argentina users
+  - Add Rest API integration method for Brazil users
 Websocket API​
 - Connect
-  - Add websocket integration method for Argentina users
+  - Add websocket integration method for Brazil users
 2026-08-07​
 REST API​

```
