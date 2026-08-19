<!-- has_changes=true date=2026-08-19 -->
# Exchange API Changelog Diff

Generated: 2026-08-19 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132451 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 11 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [OK] Bybit V5 (`bybit`): no change (91216 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 9 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145596 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 4d8302f..a6de30f 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -51,5 +51,5 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 RPI 挂单最小名义金额限制
 最后更新：2026 年 8 月 17 日
-RPI 挂单（ordType: rpi 或 elp）现需满足最小名义金额门槛。低于门槛的订单将被拒绝，返回错误码 54051。已于 2026 年 8 月 17 日 上线模拟环境。生产环境将于 2026 年 8 月 19 日 起对部分币种（BTC/ETH/SNDK XPerp 及 XSNDK-USDT）进行灰度发布，2026 年 8 月 20 日 全量上线。
+RPI 挂单（ordType: rpi 或 elp）现需满足最小名义金额门槛。低于门槛的订单将被拒绝，返回错误码 54051。已于 2026 年 8 月 17 日 上线模拟环境。生产环境将于 2026 年 8 月 18 日上午 起对部分币种（BTC/ETH/SNDK XPerp 及 XSNDK-USDT）进行灰度发布，若无异常将于 2026 年 8 月 18 日下午 全量上线。
 各产品类型最低限额
 | 产品类型 | 最小名义金额

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index dec6d56..d4d770d 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,4 +1,2 @@
-WARNING
-The Pro API is currently in beta testing and should not be used in production trading environments.
 2026.08.18#
 [Modify] UTA REST Rate Limit, increase in UTA resource pool rate limit：

```
