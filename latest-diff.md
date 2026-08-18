<!-- has_changes=true date=2026-08-18 -->
# Exchange API Changelog Diff

Generated: 2026-08-18 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132451 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 39 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [OK] Bybit V5 (`bybit`): no change (91216 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 25 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145596 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 43ff114..4d8302f 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -49,4 +49,34 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 受影响的订单类型有：post_only、mmp_and_post_only、rpi（Retail Price Improvement）。
 其他订单类型如 limit（普通限价单）、market（市价单）、ioc、fok 订单推送行为保持不变。
+RPI 挂单最小名义金额限制
+最后更新：2026 年 8 月 17 日
+RPI 挂单（ordType: rpi 或 elp）现需满足最小名义金额门槛。低于门槛的订单将被拒绝，返回错误码 54051。已于 2026 年 8 月 17 日 上线模拟环境。生产环境将于 2026 年 8 月 19 日 起对部分币种（BTC/ETH/SNDK XPerp 及 XSNDK-USDT）进行灰度发布，2026 年 8 月 20 日 全量上线。
+各产品类型最低限额
+| 产品类型 | 最小名义金额
+| SWAP / FUTURES | 10,000 USD
+| SPOT | 1,000 USD
+| EVENTS | 不适用
+本规则独立于各币种现有的最小下单量（minSz）校验——RPI 订单需同时满足两者。
+下单
+名义金额低于适用门槛的 RPI 订单将被拒绝，返回 54051。批量请求中每条子订单独立校验——未通过的子订单返回自身 sCode: 54051，其余子订单不受影响。
+非 RPI 订单（包括 rpiTakerAccess: true 的 taker 订单）不受本规则影响。
+改单
+- 包含 newSz 的改单（无论是否同时修改 newPx）将按改后数量重新校验最小名义金额。若改后名义金额低于门槛，该次改单被拒绝，返回 54051；原订单继续有效。
+- 仅修改 newPx（不含 newSz）的改单不重新校验本规则。
+批量改单请求中每条子订单独立校验——行为与单笔改单一致。
+存量订单
+本规则生效前已在架的 RPI 挂单不受影响。校验仅适用于上线后新提交的下单与改单请求。
+错误码
+| 错误码 | 消息
+| 54051 | RPI 订单被拒绝。订单价值低于 RPI 订单所需的最低金额（{param0} USD）。
+适用于所有 REST 及 WebSocket trade 操作：
+- POST / 下单
+- POST / 批量下单
+- POST / 修改订单
+- POST / 批量修改订单
+- WS / 下单
+- WS / 批量下单
+- WS / 改单
+- WS / 批量改单
 2026-08-11
 RPI 挂单价格间距与可见性规则更新

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index a83c7a2..dec6d56 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,4 +1,20 @@
 WARNING
 The Pro API is currently in beta testing and should not be used in production trading environments.
+2026.08.18#
+[Modify] UTA REST Rate Limit, increase in UTA resource pool rate limit：
+| Level | Current UTA rate limit | Before UTA rate limit
+| VIP0 | 300/s | 200/s
+| VIP1 | 400/s | 400/s
+| VIP2 | 450/s | 450/s
+| VIP3 | 500/s | 500/s
+| VIP4 | 750/s | 500/s
+| VIP5 | 900/s | 700/s
+| VIP6 | 1100/s | 850/s
+| VIP7 | 1200/s | 1000/s
+| VIP8 | 1500/s | 1350/s
+| VIP9 | 2000/s | 1700/s
+| VIP10 | 2500/s | 2000/s
+| VIP11 | 3500/s | 2500/s
+| VIP12 | 4000/s | 3000/s
 2026.08.12#
 [Modify] UTA REST Get Trade History When response param fillType is 'ADL', the liquidityRole will be empty instead of MAKER

```
