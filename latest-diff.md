<!-- has_changes=true date=2026-08-01 -->
# Exchange API Changelog Diff

Generated: 2026-08-01 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132459 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 54 diff lines

- [CHANGED] **Bitget (Spot + Futures)** (`bitget`): 15 diff lines

- [OK] Bybit V5 (`bybit`): no change (89002 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (36254 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145596 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 16f855a..73614d5 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -23,6 +23,6 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
 WebSocket 订单频道推送行为调整
-最近更新：2026 年 7 月 22 日
-为了让客户能够更明确地判断 post-only（包括 mmp_and_post_only）与将要推出的 rpi 新订单的最终状态，避免收到 state: live 后订单仍被撤销的场景，欧易将调整订单频道中 post-only 与 rpi 订单的 state: live 事件行为。
+最近更新：2026 年 7 月 28 日
+为了让客户能够更明确地判断 post-only（包括 mmp_and_post_only）与 rpi 新订单的最终状态，避免收到 state: live 后订单仍被撤销的场景，欧易将调整订单频道中 post-only 与 rpi 订单的 state: live 事件行为。
 具体影响
 - state: live 事件的推送时机由订单接收后立即推送，调整为订单成功进入订单簿之后才推送（延后约 1 ms）。
@@ -38,11 +38,11 @@ WebSocket 订单频道推送行为调整
 | post-only 订单带 reduceOnly: true，
 size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0） | state: live（amendSource: 4，amendResult: 0） → state: live
-| 将要推出的 rpi 订单，rpiPxRound: false，
+| rpi 订单，rpiPxRound: false，
 挂单失败
 （不满足价格间距规则被撤单） | N/A | 只推 state: canceled（不会有 state: live）
-| 将要推出的 rpi 订单，rpiPxRound: true，
+| rpi 订单，rpiPxRound: true，
 并且 price 被修改 | N/A | state: live（amendSource: 6，amendResult: 0） → state: live
 生效时间
-- 对于 rpi 订单（包括将要弃用的 elp 订单）：模拟盘 —— 2026 年 7 月 23 日；实盘 —— 2026 年 7 月 28 日。
+- 对于 rpi 订单（包括将要弃用的 elp 订单）：已上线 —— 模拟盘 —— 2026 年 7 月 23 日；实盘 —— 2026 年 7 月 28 日。
 - 对于 post_only 和 mmp_and_post_only 订单：模拟盘和实盘均为 2026 年 8 月中旬。
 影响范围
@@ -71,5 +71,13 @@ REST 请求参数：instId（必填）、sz（每侧深度档数，最大 400，
 - rpiTakerAccess 是 isElpTakerAccess 的更名并扩展，支持所有标准订单类型（limit、market、fok、ioc；此前仅 ioc），并可在改单接口中设置。isElpTakerAccess 在弃用日期前将作为别名继续被接受（见上方迁移说明）。
 - 错误码 54045（此前用于非 ioc 订单尝试吃取 RPI 流动性时返回）已废弃——现在 rpiTakerAccess 对所有订单类型均有效，该错误码不再可能触发。
-均适用于下单/改单，REST + WS： - POST / 下单 - POST / 批量下单 - POST / 修改订单 - POST / 批量修改订单 - WS / 下单 - WS / 批量下单 - WS / 改单 - WS / 批量改单
+均适用于下单/改单，REST + WS：
+- POST / 下单
+- POST / 批量下单
+- POST / 修改订单
+- POST / 批量修改订单
+- WS / 下单
+- WS / 批量下单
+- WS / 改单
+- WS / 批量改单
 | 参数名 | 类型 | 是否必须 | 描述
 | rpiTakerAccess | Boolean | 否 | 默认值为 false。
@@ -79,5 +87,9 @@ REST 请求参数：instId（必填）、sz（每侧深度档数，最大 400，
 挂单类型：rpi（替代 elp）
 - 下 RPI 挂单时，请将 ordType 设为 rpi 而非 elp。elp 在弃用日期前将继续被接受（见上方迁移说明）——ordType 只能取一个值，二者选其一，不能同时传递。
-适用于下单，REST + WS： - POST / 下单 - POST / 批量下单 - WS / 下单 - WS / 批量下单
+适用于下单，REST + WS：
+- POST / 下单
+- POST / 批量下单
+- WS / 下单
+- WS / 批量下单
 挂单参数：rpiPxRound
 - rpiPxRound 为新增参数，用于 RPI 挂单价格间距规则（详见下文）。仅对 RPI 挂单（ordType: rpi）生效；对非 RPI 订单及 OPTION/EVENTS 将被忽略。

```

### Bitget (Spot + Futures) (`bitget`)
- Source: https://www.bitget.com/api-doc/common/changelog
- Raw: https://www.bitget.fit/api-doc/common/changelog

```diff
diff --git a/changelogs/bitget.txt b/changelogs/bitget.txt
index 538b638..6e70a80 100644
--- a/changelogs/bitget.txt
+++ b/changelogs/bitget.txt
@@ -26,5 +26,4 @@ Coin equity = Balance + Frozen margin + unrealized PnL
 | Available | The current available balance of a specific coin in the account for opening positions.
 Available = Balance + unrealized PnL
-Note: Realized PnL in the available balance can be used for opening futures positions but cannot be used to place spot orders.
 | UnrealisedPnL | The total profits of all futures positions settled in a specific coin in the account.
 Unrealized profits = Profits of USDT-M perpetual futures positions in cross margin mode + profits of USDC-M perpetual futures positions in cross margin mode + profits of coin-M perpetual futures positions in cross margin mode
@@ -38,4 +37,2 @@ Maintenance margin = Position value × maintenance margin rate
 Cross margin account's margin ratio = (maintenance margin + partial liquidation transaction fees)÷Account equity.
 Both maintenance margin and partial liquidation transaction fees are calculated by adding the position size and the open order size.
-Improved Readability​
-The Open API documentation has been revised and proofread, with unclear descriptions from previous versions clarified to reduce customer confusion.

```
