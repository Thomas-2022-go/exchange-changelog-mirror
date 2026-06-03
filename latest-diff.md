<!-- has_changes=true date=2026-06-03 -->
# Exchange API Changelog Diff

Generated: 2026-06-03 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128989 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [CHANGED] **OKX V5** (`okx`): 76 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 11 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (32538 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (138977 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 57790b8..b58aefd 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,24 +1,3 @@
 待发布内容
-SPACEX 永续合约重命名
-最后更新：2026年6月1日
-为了优化用户交易体验，欧易将于 2026 年 6 月 2 日 将 SPACEXUSDT 永续合约更名为 SPCXUSDT 永续合约。更多内容请参考公告详情
-- 更名时：
-  - 产品频道 将按以下顺序推送更新数据：
-    - instId: SPACEX-USDT-SWAP, state: expired
-    - instId: SPCX-USDT-SWAP, state: rebase
-    - instId: SPCX-USDT-SWAP, state: post_only
-    - instId: SPCX-USDT-SWAP, state: live
-- 更名后：
-  - 推送数据中的 instId instFamily, uly 会使用新的参数值。
-  - 平台将不再支持使用 instId: SPACEX-USDT-SWAP 以及 instFamily: SPACEX-USDT 订阅该合约的 WebSocket 频道，或是通过 OpenAPI 发送 HTTP 请求。请您在合约更名后使用 instId: SPCX-USDT-SWAP 或 instFamily: SPCX-USDT 进行相关交易。
-  - 先前使用 instId: SPACEX-USDT-SWAP 以及 instFamily: SPACEX-USDT 订阅的频道：
-    - 对于trades 和 以及 positions 频道的定时快照，旧的订阅仍然会推送数据，请在更名后使用新的参数值重新订阅。
-    - 对于深度频道，旧的订阅仍然会推送数据，需要先使用新的参数值取消订阅，再使用新的参数值重新订阅。
-    - 其他频道将不再推送任何数据，请在更名后使用新的参数值重新订阅。
-  - instIdCode 不发生变动。
-涉及到重命名的参数如下：
-| 值类型 | instId | uly | instFamily | ctValCcy
-| 改名前 | SPACEX-USDT-SWAP | SPACEX-USDT | SPACEX-USDT | SPACEX
-| 改名后 | SPCX-USDT-SWAP | SPCX-USDT | SPCX-USDT | SPCX
 WebSocket服务升级断线提示扩展至业务频道
 最后更新：2026 年 5 月 21 日
@@ -85,8 +64,8 @@ WS 推送数据中将返回空值的字段
 | > adlRecRate | String | 自动减仓结束的风险保证金下降率（已弃用）。将返回 ""
 ELP 合并深度订单簿
-最近更新：2026年5月29日
-为简化 ELP 行情数据集成，OKX 将推出合并深度订单簿，将非 ELP 和当前可交易的 ELP 流动性合并为一个数据流。本次变更预计于 2026年6月11日 上线。
-- 在现有深度频道中新增 WebSocket 公共频道 books-elp-all。400 档深度；初始全量推送 + 每 100 毫秒增量推送。推送合并非 ELP 和当前可交易 ELP 流动性的深度数据。不可交易的 ELP 订单在平台端过滤。
-  - WS / 深度频道
+最近更新：2026年6月2日
+为简化 ELP 行情数据集成，OKX 将推出合并深度频道 books-elp-all，将非 ELP 与当前可交易的 ELP 流动性合并为单一数据流，用户无需再分别订阅 books 和 books-elp 并在客户端自行合并。该能力同时提供 WebSocket 与 REST 两种方式，预计于 2026年6月11日 上线。
+- 通过 /ws/v5/business 端点（wss://ws.okx.com:8443/ws/v5/business）新增 WebSocket 频道 books-elp-all。400 档深度；初始全量推送 + 每 100 毫秒增量推送。推送合并非 ELP 和当前可交易 ELP 流动性的深度数据。不可交易的 ELP 订单在平台端过滤。
+  - WS / books-elp-all 频道
 asks 和 bids 中的每个元素是一个 4 元素数组：[price, totalQty, nonElpQty, orderCount]
 - price：深度价格
@@ -104,5 +83,6 @@ asks 和 bids 中的每个元素是一个 4 元素数组：[price, totalQty, non
   - GET / 获取产品深度
 GET / 获取 ELP 合并深度
-获取产品的 ELP 合并深度订单簿，合并非 ELP 和当前可交易的 ELP 流动性。仅支持已启用 ELP 的产品。
+获取产品的 ELP 合并深度订单簿，合并非 ELP 和当前可交易的 ELP 流动性。数据每 200 毫秒更新一次。
+该接口不会立即返回数据，而是在服务端缓存更新后返回最新数据。
 限速：20 次/2s
 限速规则：IP
@@ -139,4 +119,25 @@ ELP 吃单权限扩展至所有订单类型
 | 参数名 | 类型 | 是否必须 | 描述
 | isElpTakerAccess | Boolean | 否 | 默认值为 false。设为 true 时，订单可以使用 ELP 流动性。适用于所有订单类型。当 isElpTakerAccess 为 true 时，除 post_only 外的所有订单类型都会触发减速带机制；下单时 post_only 订单可免于减速带。isElpTakerAccess 也可在改单接口中使用，且不会从原始订单继承——必须在每次改单请求中显式重新指定（改单时省略则该次改单视为 false）。改单时，减速带适用于所有订单类型（包括 post_only）；如需改 post_only 订单且不想触发减速带，请在该次改单中不设置 isElpTakerAccess。
+2026-06-02
+SPACEX 永续合约重命名
+为了优化用户交易体验，欧易已于 2026 年 6 月 2 日 将 SPACEXUSDT 永续合约更名为 SPCXUSDT 永续合约。更多内容请参考公告详情
+- 更名时：
+  - 产品频道 已按以下顺序推送更新数据：
+    - instId: SPACEX-USDT-SWAP, state: expired
+    - instId: SPCX-USDT-SWAP, state: rebase
+    - instId: SPCX-USDT-SWAP, state: post_only
+    - instId: SPCX-USDT-SWAP, state: live
+- 更名后：
+  - 推送数据中的 instId instFamily, uly 会使用新的参数值。
+  - 平台将不再支持使用 instId: SPACEX-USDT-SWAP 以及 instFamily: SPACEX-USDT 订阅该合约的 WebSocket 频道，或是通过 OpenAPI 发送 HTTP 请求。请您在合约更名后使用 instId: SPCX-USDT-SWAP 或 instFamily: SPCX-USDT 进行相关交易。
+  - 先前使用 instId: SPACEX-USDT-SWAP 以及 instFamily: SPACEX-USDT 订阅的频道：
+    - 对于trades 和 以及 positions 频道的定时快照，旧的订阅仍然会推送数据，请在更名后使用新的参数值重新订阅。
+    - 对于深度频道，旧的订阅仍然会推送数据，需要先使用新的参数值取消订阅，再使用新的参数值重新订阅。
+    - 其他频道将不再推送任何数据，请在更名后使用新的参数值重新订阅。
+  - instIdCode 不发生变动。
+涉及到重命名的参数如下：
+| 值类型 | instId | uly | instFamily | ctValCcy
+| 改名前 | SPACEX-USDT-SWAP | SPACEX-USDT | SPACEX-USDT | SPACEX
+| 改名后 | SPCX-USDT-SWAP | SPCX-USDT | SPCX-USDT | SPCX
 2026-05-22
 获取资金流水：新增 thirdPartyType 请求参数

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 8d05e30..92c3fbd 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,6 @@
+2026-06-02​
+Websocket API​
+- SBE Order Entry [UPDATE]
+  - SBE Order Entry is now available in production.
 2026-05-28​
 REST API​

```
