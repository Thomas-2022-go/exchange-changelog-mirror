<!-- has_changes=true date=2026-07-18 -->
# Exchange API Changelog Diff

Generated: 2026-07-18 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132274 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 25 diff lines

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
index cebc4a4..f34fbaf 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -92,5 +92,5 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 其他订单类型如 limit（普通限价单）、market（市价单）、ioc、fok 订单推送行为保持不变。
 ELP 更名为 RPI（散户价格优化）计划
-最近更新：2026年7月8日
+最近更新：2026年7月17日
 OKX 将品牌 Enhanced Liquidity Program（ELP） 更名为 Retail Price Improvement（散户价格优化，RPI）。本次变更包含新的 RPI 合并深度订单簿（books-rpi，同时提供 WebSocket 与 REST）、更名后的挂单类型 rpi（替代 elp）、扩展后的下单参数 rpiTakerAccess（替代 isElpTakerAccess）、用于 RPI 挂单价格间距规则的新参数 rpiPxRound，以及更名后的账户字段 rpi/rpiMaker。预计于 2026年7月21日 在模拟盘上线，并于 2026年7月28日 正式上线。
 ELP 命名弃用截止日期：2026年10月31日
@@ -126,5 +126,5 @@ REST 请求参数：instId（必填）、sz（每侧深度档数，最大 400，
 | 参数名 | 类型 | 是否必须 | 描述
 | rpiPxRound | Boolean | 否 | 默认值为 false。设为 true 时，违反间距规则的价格将自动向外取整至最近的可挂单、且不会吃单的价位，而非直接拒绝。
-- 在 orders WebSocket 私有频道新增 amendSource 枚举值 6：表示系统为满足 RPI 挂单价格间距规则（由 rpiPxRound 触发）而自动调整（取整）了订单价格。下单时，若发生取整，orders 频道会推送两次——一次为原始提交价格，另一次为取整后的价格（携带 amendSource: 6）；若价格无需取整，则不会有第二次推送。改单时，仅会推送一次，且直接为取整后的价格。
+- 在 orders WebSocket 私有频道新增 amendSource 枚举值 6：表示系统为满足 RPI 挂单价格间距规则（由 rpiPxRound 触发）而自动调整（取整）了订单价格。
   - WS / 订单频道
 RPI 挂单价格间距规则
@@ -133,5 +133,5 @@ RPI 挂单需遵守间距规则（见下方 rpiMinLevel / rpiMinPxBand）。订
   - 获取交易产品基础信息（公共）
 | 参数名 | 类型 | 描述
-| rpiMinLevel | String | RPI 买一价与卖一价之间的最小间距，以有机价格档位数计。默认值为 5；事件合约（Event Contracts）为 0。
+| rpiMinLevel | String | RPI 买一价与卖一价之间的最小间距，以有机价格档位数计。默认值为 4；事件合约（Event Contracts）为 0。
 | rpiMinPxBand | String | 满足间距规则所需的、与对方最优有机报价之间的最小距离，单位为基点（bps），例如 20。
 RPI 挂单权限字段：rpi（替代 elp）

```
