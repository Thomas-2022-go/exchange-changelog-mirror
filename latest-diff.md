<!-- has_changes=true date=2026-08-22 -->
# Exchange API Changelog Diff

Generated: 2026-08-22 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132451 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 45 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 21 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (37469 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (149534 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index c3fee3e..3068ffd 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -22,10 +22,10 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | 参数名 | 类型 | 描述
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
+2026-08-20
 WebSocket 订单频道推送行为调整
-最近更新：2026 年 8 月 10 日
-为了让客户能够更明确地判断 post-only（包括 mmp_and_post_only）与 rpi 新订单的最终状态，避免收到 state: live 后订单仍被撤销的场景，欧易将调整订单频道中 post-only 与 rpi 订单的 state: live 事件行为。
+为了让客户能够更明确地判断 post-only（包括 mmp_and_post_only）与 rpi 新订单的最终状态，避免收到 state: live 后订单仍被撤销的场景，欧易已调整订单频道中 post-only 与 rpi 订单的 state: live 事件行为。
 具体影响
 - state: live 事件的推送时机由订单接收后立即推送，调整为订单成功进入订单簿之后才推送（延后约 1 ms）。
-- 价格穿越 BBO 被撤单的挂单失败场景下，state: live 更新将被完全移除，只推送 state: canceled 更新。
+- 价格穿越 BBO 被撤单的挂单失败场景下，state: live 更新已被完全移除，只推送 state: canceled 更新。
 | 场景 | 调整前 | 调整后
 | post-only 订单挂单失败
@@ -45,5 +45,5 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 生效时间
 - 对于 rpi 订单（包括将要弃用的 elp 订单）：已上线 —— 模拟盘 —— 2026 年 7 月 23 日；实盘 —— 2026 年 7 月 28 日。
-- 对于 post_only 和 mmp_and_post_only 订单：模拟盘 —— 2026 年 8 月 10 日（已上线）；实盘 —— 2026 年 8 月 20 日。
+- 对于 post_only 和 mmp_and_post_only 订单：模拟盘 —— 2026 年 8 月 10 日（已上线）；实盘 —— 2026 年 8 月 20 日（已上线）。
 影响范围
 受影响的订单类型有：post_only、mmp_and_post_only、rpi（Retail Price Improvement）。
@@ -225,7 +225,7 @@ GET / 获取 GLP 当日表现
 权限：读取
 HTTP请求
-GET /api/v5/users/glp/today-performance
+GET /api/v5/users/glp/todayperformance
 请求示例
-GET /api/v5/users/glp/today-performance
+GET /api/v5/users/glp/todayperformance
 请求参数
 无。账户由登录态自动解析。
@@ -276,7 +276,7 @@ GET / 获取 GLP 历史表现
 权限：读取
 HTTP请求
-GET /api/v5/users/glp/historical-performance
+GET /api/v5/users/glp/historicalperformance
 请求示例
-GET /api/v5/users/glp/historical-performance?program=SPOT GET /api/v5/users/glp/historical-performance?program=SPOT&begin=1751299200000&end=1753804800000&limit=31
+GET /api/v5/users/glp/historicalperformance?program=SPOT GET /api/v5/users/glp/historicalperformance?program=SPOT&begin=1751299200000&end=1753804800000&limit=31
 请求参数
 | 参数名 | 类型 | 是否必须 | 描述

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 9d6d014..ddea632 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,16 @@
+2026-08-31​
+REST API​
+- Integration Guidance
+  - Add Rest API integration method for HongKong users
+Websocket API​
+- Connect
+  - Add websocket integration method for HongKong users
+2026-08-28​
+REST API​
+- Integration Guidance
+  - Add Rest API integration method for Argentina users
+Websocket API​
+- Connect
+  - Add websocket integration method for Argentina users
 2026-08-20​
 REST API​

```
