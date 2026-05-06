<!-- has_changes=true date=2026-05-06 -->
# Exchange API Changelog Diff

Generated: 2026-05-06 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 51 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (85776 bytes)

- [CHANGED] **OKX V5** (`okx`): 28 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (77256 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (28255 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139392 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index c745ad1..98f4f24 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -1,5 +1,45 @@
 # CHANGELOG for Binance's API
 
-**Last Updated: 2026-04-28**
+**Last Updated: 2026-05-06**
+
+### 2026-05-06
+
+**Notice: The following changes will be deployed on 2026-05-08, starting at 06:00 UTC and may take several hours to complete.**
+
+* Added `serverShutdown` event to [WebSocket API](web-socket-api.md) and [WebSocket Streams](web-socket-streams.md).
+  * `serverShutdown` event will be sent 10 minutes before disconnection.
+
+* [`PERCENT_PRICE`](./filters.md#percent_price), [`PERCENT_PRICE_BY_SIDE`](./filters.md#percent_price_by_side), [`MIN_NOTIONAL`](./filters.md#min_notional), and [`NOTIONAL`](./filters.md#notional) filters now use [reference price](./faqs/price_range_execution_rules.md) when it exists and is non-null. The filters fall back to their previous behavior when the reference price does not exist or is null.
+
+* Market data for [Block Trades](https://www.binance.info/en/support/faq/detail/557f95eaf8fb4460aed0a891d42a1425).
+  * New Endpoints/Methods
+    * REST API:
+      * `GET /api/v3/historicalBlockTrades`
+    * WebSocket API:
+      * `blockTrades.historical`
+
+* Order query responses may include an [`expiryReason`](./enums.md#expiryreasons) field.
+  * This field is returned **only for expired orders** and helps users understand why an order expired, including cases where the order is expired due to the **execution price range rule**.
+  * This field is included in both JSON and SBE 3:4 responses.
+  * This applies to the following endpoint/method:
+    * REST API:
+      * `GET /api/v3/order`
+      * `GET /api/v3/allOrders`
+      * `GET /api/v3/orderList`
+      * `GET /api/v3/allOrderList`
+    * WebSocket API:
+      * `order.status`
+      * `allOrders`
+      * `orderList.status`
+      * `allOrderLists`
+
+* REST and WebSocket API SBE schema 3:4
+  * The current schema 3:3 [spot_3_3.xml](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot_3_3.xml) is deprecated and will be retired in 6 months as per our schema deprecation policy.
+  * Changes in schema 3:4:
+    * New message `BlockTradesResponse`
+    * New type `blockTradeId`
+    * New field `expiryReason` in `OrderResponse` and `OrdersResponse`
+
+---
 
 ### 2026-04-28

```

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 48e59b6..13344a0 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,19 +1,13 @@
 待发布内容
-Post-only 合约状态
-最近更新: 2026年4月29日
-产品状态新增 post_only 枚举值。合约处于 post_only 状态时，仅接受 post-only 限价单（以及对已有 post-only 订单的改单和撤单）；市价单、IOC、FOK 和普通限价单将被拒绝。预计 2026 年 5 月上线。
-产品接口/频道
-- 返回参数 state 新增枚举值 post_only
+2026-05-06
+已有接口改动
+- 返回参数 state 新增枚举值 post_only。合约处于 post_only 状态时，仅接受 post-only 限价单（以及对已有 post-only 订单的改单和撤单）；市价单、IOC、FOK 和普通限价单将被拒绝。仅适用于 SWAP：
   - 获取交易产品基础信息（私有）
   - 获取交易产品基础信息（公共）
   - 产品频道
+返回参数
 | 参数名 | 类型 | 描述
 | state | String | 产品状态
-live：交易中
-suspend：暂停中
-rebase：合约在变基中，不可交易，仅适用于SWAP
 post_only：仅接受 post-only 订单；已有 post-only 订单可改单和撤单。其他订单类型（市价单、IOC、FOK、普通限价单）将被拒绝。仅适用于 SWAP
-preopen：预上线，交割和期权合约轮转生成到开始交易；部分交易产品上线前
-test：测试中（测试产品，不可交易）
 2026-04-28
 已有接口改动

```
