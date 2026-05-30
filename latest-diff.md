<!-- has_changes=true date=2026-05-30 -->
# Exchange API Changelog Diff

Generated: 2026-05-30 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128989 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [CHANGED] **OKX V5** (`okx`): 75 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (80145 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (29221 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (138977 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index f4ce97a..5c1dc9b 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,8 +1,8 @@
 待发布内容
 SPACEX 永续合约重命名
-最后更新：2026年5月27日
+最后更新：2026年5月28日
 为了优化用户交易体验，欧易将在 2026 年 6 月 1 日至 6 月 5 日（UTC）期间的某一天 将 SPACEXUSDT 永续合约更名为 SPCXUSDT 永续合约。
 - 更名时：
-  - 产品频道 会推送 instId: SPCX-USDT-SWAP, state: rebase 的更新数据，和 instId: SPCX-USDT-SWAP, state: live 的数据。
+  - 产品频道 会推送 instId: SPCX-USDT-SWAP, state: expired 的更新数据，和 instId: SPCX-USDT-SWAP, state: live 的数据。
 - 更名后：
   - 推送数据中的 instId instFamily, uly 会使用新的参数值。
@@ -60,4 +60,59 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
  1. books5 和 bbo-tbt 频道本身不包含 checksum 字段，不在本次变更范围内。
  2. WebSocket 连接已全面启用 TLS（wss://），具备防窃听、防篡改以及完整性校验的能力；结合 seqId/prevSeqId 的严格校验，可有效防止数据乱序、部分丢失或被恶意注入，实现与原 checksum 等效甚至更强的完整性保护。
+ELP 合并深度订单簿
+最近更新：2026年5月29日
+为简化 ELP 行情数据集成，OKX 将推出合并深度订单簿，将非 ELP 和当前可交易的 ELP 流动性合并为一个数据流。本次变更预计于 2026年6月11日 上线。
+- 在现有深度频道中新增 WebSocket 公共频道 books-elp-all。400 档深度；初始全量推送 + 每 100 毫秒增量推送。推送合并非 ELP 和当前可交易 ELP 流动性的深度数据。不可交易的 ELP 订单在平台端过滤。
+  - WS / 深度频道
+asks 和 bids 中的每个元素是一个 4 元素数组：[price, totalQty, nonElpQty, orderCount]
+- price：深度价格
+- totalQty：该价格档位的总可见数量（非 ELP 数量 + 当前可交易 ELP 数量）。ELP 吃单用户应使用此字段作为完整可见深度。
+- nonElpQty：仅非 ELP（有机）数量。非 ELP 吃单用户应使用此字段作为其可用深度。
+- orderCount：该价格档位的可见订单数量（包括非 ELP 和当前可交易的 ELP 订单）。
+推送数据参数
+| 参数名 | 类型 | 描述
+| asks | Array of Arrays | 卖方深度，每个元素为 [price, totalQty, nonElpQty, orderCount]
+| bids | Array of Arrays | 买方深度，每个元素为 [price, totalQty, nonElpQty, orderCount]
+| ts | String | 深度生成时间，Unix 时间戳的毫秒数格式，如 1779782400000
+| prevSeqId | Integer | 上一条推送消息的序列号，全量推送时 prevSeqId = -1
+| seqId | Integer | 当前推送消息的序列号
+- 新增 REST 接口用于获取 ELP 合并深度订单簿：
+  - GET / 获取产品深度
+GET / 获取 ELP 合并深度
+获取产品的 ELP 合并深度订单簿，合并非 ELP 和当前可交易的 ELP 流动性。仅支持已启用 ELP 的产品。
+限速：20 次/2s
+限速规则：IP
+权限：公共
+HTTP 请求
+GET /api/v5/market/books-elp-all
+请求示例
+GET /api/v5/market/books-elp-all?instId=BTC-USDT-SWAP
+请求参数
+| 参数名 | 类型 | 是否必须 | 描述
+| instId | String | 是 | 产品 ID，如 BTC-USDT-SWAP。仅支持已启用 ELP 的产品。
+| sz | String | 否 | 每侧深度档数，最大 400，默认 1
+返回示例
+{ "code": "0", "msg": "", "data": [ { "asks": [ ["67855.2", "0.5", "0.5", "1"], ["67856.0", "1.3", "1.0", "4"], ["67860.5", "0.3", "0", "1"] ], "bids": [ ["67854.8", "1.7", "1.2", "3"], ["67853.0", "0.8", "0.8", "1"] ], "ts": "1779782400000", "seqId": 123456 } ] }
+返回参数
+| 参数名 | 类型 | 描述
+| asks | Array of Arrays | 卖方深度，每个元素为 [price, totalQty, nonElpQty, orderCount]
+| bids | Array of Arrays | 买方深度，每个元素为 [price, totalQty, nonElpQty, orderCount]
+| ts | String | 深度生成时间，Unix 时间戳的毫秒数格式，如 1779782400000
+| seqId | Integer | 当前推送消息的序列号
+ELP 吃单权限扩展至所有订单类型
+最近更新：2026年5月29日
+订单参数 isElpTakerAccess 将扩展支持所有订单类型（此前仅 ioc），并新增支持在改单接口中使用。本次变更预计于 2026年6月9日 上线。
+- 更新请求参数 isElpTakerAccess 的描述，以反映扩展的订单类型支持和改单行为：
+  - POST / 下单
+  - POST / 批量下单
+  - POST / 修改订单
+  - POST / 批量修改订单
+  - WS / 下单
+  - WS / 批量下单
+  - WS / 改单
+  - WS / 批量改单
+请求参数
+| 参数名 | 类型 | 是否必须 | 描述
+| isElpTakerAccess | Boolean | 否 | 默认值为 false。设为 true 时，订单可以使用 ELP 流动性。适用于所有订单类型。当 isElpTakerAccess 为 true 时，除 post_only 外的所有订单类型都会触发减速带机制；下单时 post_only 订单可免于减速带。isElpTakerAccess 也可在改单接口中使用，且不会从原始订单继承——必须在每次改单请求中显式重新指定（改单时省略则该次改单视为 false）。改单时，减速带适用于所有订单类型（包括 post_only）；如需改 post_only 订单且不想触发减速带，请在该次改单中不设置 isElpTakerAccess。
 2026-05-22
 获取资金流水：新增 thirdPartyType 请求参数

```
