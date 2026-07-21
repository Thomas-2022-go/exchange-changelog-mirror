<!-- has_changes=true date=2026-07-21 -->
# Exchange API Changelog Diff

Generated: 2026-07-21 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132274 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 20 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (85682 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (35340 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120249 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index f34fbaf..b4e5786 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -86,5 +86,5 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 并且 price 被修改 | N/A | state: live（amendSource: 6，amendResult: 0） → state: live
 生效时间
-- 对于 rpi 订单：模拟盘 —— 2026 年 7 月 21 日；实盘 —— 2026 年 7 月 28 日。
+- 对于 rpi 订单：模拟盘 —— 2026 年 7 月 22 日；实盘 —— 2026 年 7 月 28 日。
 - 对于 post_only 和 mmp_and_post_only 订单：模拟盘和实盘均为 2026 年 8 月中旬。
 影响范围
@@ -92,6 +92,6 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 其他订单类型如 limit（普通限价单）、market（市价单）、ioc、fok 订单推送行为保持不变。
 ELP 更名为 RPI（散户价格优化）计划
-最近更新：2026年7月17日
-OKX 将品牌 Enhanced Liquidity Program（ELP） 更名为 Retail Price Improvement（散户价格优化，RPI）。本次变更包含新的 RPI 合并深度订单簿（books-rpi，同时提供 WebSocket 与 REST）、更名后的挂单类型 rpi（替代 elp）、扩展后的下单参数 rpiTakerAccess（替代 isElpTakerAccess）、用于 RPI 挂单价格间距规则的新参数 rpiPxRound，以及更名后的账户字段 rpi/rpiMaker。预计于 2026年7月21日 在模拟盘上线，并于 2026年7月28日 正式上线。
+最近更新：2026年7月20日
+OKX 将品牌 Enhanced Liquidity Program（ELP） 更名为 Retail Price Improvement（散户价格优化，RPI）。本次变更包含新的 RPI 合并深度订单簿（books-rpi，同时提供 WebSocket 与 REST）、更名后的挂单类型 rpi（替代 elp）、扩展后的下单参数 rpiTakerAccess（替代 isElpTakerAccess）、用于 RPI 挂单价格间距规则的新参数 rpiPxRound，以及更名后的账户字段 rpi/rpiMaker。预计于 2026年7月23日 在模拟盘上线，并于 2026年7月28日 正式上线。
 ELP 命名弃用截止日期：2026年10月31日
 在此日期之前，OKX 将以两种不同方式并行运行 ELP 与 RPI 命名：

```
