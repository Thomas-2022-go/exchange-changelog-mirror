<!-- has_changes=true date=2026-08-20 -->
# Exchange API Changelog Diff

Generated: 2026-08-20 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132451 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 27 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 24 diff lines

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 12 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145596 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index a6de30f..c3fee3e 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -49,7 +49,7 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 受影响的订单类型有：post_only、mmp_and_post_only、rpi（Retail Price Improvement）。
 其他订单类型如 limit（普通限价单）、market（市价单）、ioc、fok 订单推送行为保持不变。
+2026-08-18
 RPI 挂单最小名义金额限制
-最后更新：2026 年 8 月 17 日
-RPI 挂单（ordType: rpi 或 elp）现需满足最小名义金额门槛。低于门槛的订单将被拒绝，返回错误码 54051。已于 2026 年 8 月 17 日 上线模拟环境。生产环境将于 2026 年 8 月 18 日上午 起对部分币种（BTC/ETH/SNDK XPerp 及 XSNDK-USDT）进行灰度发布，若无异常将于 2026 年 8 月 18 日下午 全量上线。
+RPI 挂单（ordType: rpi 或 elp）现需满足最小名义金额门槛。低于门槛的订单将被拒绝，返回错误码 54051。生产环境自 2026年8月18日 起生效。
 各产品类型最低限额
 | 产品类型 | 最小名义金额
@@ -57,5 +57,5 @@ RPI 挂单（ordType: rpi 或 elp）现需满足最小名义金额门槛。低
 | SPOT | 1,000 USD
 | EVENTS | 不适用
-本规则独立于各币种现有的最小下单量（minSz）校验——RPI 订单需同时满足两者。
+本规则独立于各产品现有的最小下单量（minSz）校验——RPI 订单需同时满足两者。
 下单
 名义金额低于适用门槛的 RPI 订单将被拒绝，返回 54051。批量请求中每条子订单独立校验——未通过的子订单返回自身 sCode: 54051，其余子订单不受影响。
@@ -68,4 +68,5 @@ RPI 挂单（ordType: rpi 或 elp）现需满足最小名义金额门槛。低
 本规则生效前已在架的 RPI 挂单不受影响。校验仅适用于上线后新提交的下单与改单请求。
 错误码
+新增错误码：
 | 错误码 | 消息
 | 54051 | RPI 订单被拒绝。订单价值低于 RPI 订单所需的最低金额（{param0} USD）。

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index bfae39a..9d6d014 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,19 @@
+2026-08-20​
+REST API​
+- Get Broker Earning [UPDATE]
+  - bizType request parameter and response field now support new value FIAT_CONVERT (Fiat Convert)
+  - totalEarningCat adds new field fiatConvert: rebate records for Fiat Convert trading
+- Enum [UPDATE]
+  - execType: remove CorporateAction; add ForwardSplitSettle (forward stock split fractional share settlement), ReverseSplitSettle (reverse stock split fractional share settlement), Dividend (dividend distribution)
+- Enum [UPDATE]
+  - type(uta-translog): add FORWARD_SPLIT_SETTLE (forward stock split fractional share settlement), REVERSE_SPLIT_SETTLE (reverse stock split fractional share settlement)
+2026-08-18​
+REST API​
+- Asset Overview [UPDATE]
+  - UnifiedTradingAccount now returns a categories breakdown (crypto and stocks) instead of a flat coinDetail list
+2026-08-13​
+REST API​
+- Reinvest [UPDATE]
+  - Add new optional request parameter leverage: leverage multiplier (integer only, passed as string); defaults to "1" (no leverage)
 2026-08-11​
 REST API​

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index d4d770d..cd3077b 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,2 +1,7 @@
+2026.08.20#
+[Modify] UTA REST Get Trade History When fillType is ADL/LIQUID/SETTLEMENT, size must be returned as positive values.
+[Modify] UTA Websocket Execution When fillType/fT is ADL/LIQUID/SETTLEMENT, q(quantity) must be returned as positive values.
+[Add] Classic REST Exchange Broker Set Markup Fee
+[Add] Classic REST Exchange Broker Get Markup Fee
 2026.08.18#
 [Modify] UTA REST Rate Limit, increase in UTA resource pool rate limit：

```
