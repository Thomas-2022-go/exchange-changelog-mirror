<!-- has_changes=true date=2026-06-09 -->
# Exchange API Changelog Diff

Generated: 2026-06-09 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 20 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (87006 bytes)

- [CHANGED] **OKX V5** (`okx`): 43 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (81117 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (32707 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (138977 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index dc1c110..57208e0 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -1,5 +1,14 @@
 # CHANGELOG for Binance's API
 
-**Last Updated: 2026-05-11**
+**Last Updated: 2026-06-09**
+
+### 2026-06-09
+
+* Documented the `serverShutdown` event in [SBE Market Data Streams](./sbe-market-data-streams.md#serverShutdown).
+  * `serverShutdown` event will be sent 10 minutes before disconnection.
+  * Please establish a new connection as soon as possible to prevent interruption.
+  * Note that you will receive `serverShutdown` events in JSON in WebSocket text frames.
+
+---
 
 ### 2026-05-11

```

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index b58aefd..59152ca 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -64,6 +64,6 @@ WS 推送数据中将返回空值的字段
 | > adlRecRate | String | 自动减仓结束的风险保证金下降率（已弃用）。将返回 ""
 ELP 合并深度订单簿
-最近更新：2026年6月2日
-为简化 ELP 行情数据集成，OKX 将推出合并深度频道 books-elp-all，将非 ELP 与当前可交易的 ELP 流动性合并为单一数据流，用户无需再分别订阅 books 和 books-elp 并在客户端自行合并。该能力同时提供 WebSocket 与 REST 两种方式，预计于 2026年6月11日 上线。
+最近更新：2026年6月8日
+为简化 ELP 行情数据集成，OKX 将推出合并深度频道 books-elp-all，将非 ELP 与当前可交易的 ELP 流动性合并为单一数据流，用户无需再分别订阅 books 和 books-elp 并在客户端自行合并。该能力同时提供 WebSocket 与 REST 两种方式，预计于 2026年6月下旬 上线。
 - 通过 /ws/v5/business 端点（wss://ws.okx.com:8443/ws/v5/business）新增 WebSocket 频道 books-elp-all。400 档深度；初始全量推送 + 每 100 毫秒增量推送。推送合并非 ELP 和当前可交易 ELP 流动性的深度数据。不可交易的 ELP 订单在平台端过滤。
   - WS / books-elp-all 频道
@@ -105,6 +105,6 @@ GET /api/v5/market/books-elp-all?instId=BTC-USDT-SWAP
 | seqId | Integer | 当前推送消息的序列号
 ELP 吃单权限扩展至所有订单类型
-最近更新：2026年5月29日
-订单参数 isElpTakerAccess 将扩展支持所有订单类型（此前仅 ioc），并新增支持在改单接口中使用。本次变更预计于 2026年6月9日 上线。
+最近更新：2026年6月8日
+订单参数 isElpTakerAccess 将扩展支持所有订单类型（此前仅 ioc），并新增支持在改单接口中使用。本次变更预计于 2026年6月下旬 上线。
 - 更新请求参数 isElpTakerAccess 的描述，以反映扩展的订单类型支持和改单行为：
   - POST / 下单
@@ -119,4 +119,14 @@ ELP 吃单权限扩展至所有订单类型
 | 参数名 | 类型 | 是否必须 | 描述
 | isElpTakerAccess | Boolean | 否 | 默认值为 false。设为 true 时，订单可以使用 ELP 流动性。适用于所有订单类型。当 isElpTakerAccess 为 true 时，除 post_only 外的所有订单类型都会触发减速带机制；下单时 post_only 订单可免于减速带。isElpTakerAccess 也可在改单接口中使用，且不会从原始订单继承——必须在每次改单请求中显式重新指定（改单时省略则该次改单视为 false）。改单时，减速带适用于所有订单类型（包括 post_only）；如需改 post_only 订单且不想触发减速带，请在该次改单中不设置 isElpTakerAccess。
+2026-06-05
+获取资金流水全历史：新增 thirdPartyType 请求参数
+GET / 获取资金流水全历史 新增可选请求参数 thirdPartyType，支持在母账户绑定多家第三方托管商时，按指定托管商筛选账单记录。
+不填时默认为 1（Copper），保持向后兼容。
+请求参数
+| 参数名 | 类型 | 是否必须 | 描述
+| thirdPartyType | String | 否 | 第三方托管类型。不填则默认为 1。
+1：Copper
+2：Komainu
+5：SCB
 2026-06-02
 SPACEX 永续合约重命名
@@ -150,5 +160,4 @@ GET / 获取资金流水 新增可选请求参数 thirdPartyType，支持在母
 2：Komainu
 5：SCB
-6：CAAS
 2026-05-20
 新增专用 REST API 域名 openapi.okx.com

```
