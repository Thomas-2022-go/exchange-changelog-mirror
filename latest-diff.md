<!-- has_changes=true date=2026-08-11 -->
# Exchange API Changelog Diff

Generated: 2026-08-11 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132459 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 18 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [OK] Bybit V5 (`bybit`): no change (90771 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 17 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145596 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index bdfe0aa..763d12c 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -23,5 +23,5 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
 WebSocket 订单频道推送行为调整
-最近更新：2026 年 7 月 28 日
+最近更新：2026 年 8 月 10 日
 为了让客户能够更明确地判断 post-only（包括 mmp_and_post_only）与 rpi 新订单的最终状态，避免收到 state: live 后订单仍被撤销的场景，欧易将调整订单频道中 post-only 与 rpi 订单的 state: live 事件行为。
 具体影响
@@ -45,5 +45,5 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 生效时间
 - 对于 rpi 订单（包括将要弃用的 elp 订单）：已上线 —— 模拟盘 —— 2026 年 7 月 23 日；实盘 —— 2026 年 7 月 28 日。
-- 对于 post_only 和 mmp_and_post_only 订单：模拟盘和实盘均为 2026 年 8 月中旬。
+- 对于 post_only 和 mmp_and_post_only 订单：模拟盘 —— 2026 年 8 月 10 日（已上线）；实盘 —— 2026 年 8 月 20 日。
 影响范围
 受影响的订单类型有：post_only、mmp_and_post_only、rpi（Retail Price Improvement）。

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index 1e799a4..a83c7a2 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,4 +1,12 @@
 WARNING
 The Pro API is currently in beta testing and should not be used in production trading environments.
+2026.08.12#
+[Modify] UTA REST Get Trade History When response param fillType is 'ADL', the liquidityRole will be empty instead of MAKER
+[Modify] UTA REST Get Position List (UTA) added response field
+updateTime: the latest time when the position is updated (including the leverage change and the size change for position)
+[Modify]
+Classic REST Add sub-account API &
+Classic REST Modify sub-account API
+When the permissions include Transfer (Withdraw), ipWhitelist is required. Otherwise, ipWhitelist is optional.
 2026.08.03#
 1. Discontinuation of the "Hidden Order" Feature#

```
