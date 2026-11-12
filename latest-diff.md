<!-- has_changes=true date=2026-11-12 -->
# Exchange API Changelog Diff

Generated: 2026-11-12 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 151 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 17 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [OK] Bybit V5 (`bybit`): no change (100865 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (44528 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (164576 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index 33439b3..6b6fef5 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -1,5 +1,145 @@
 # CHANGELOG for Binance's API
 
-**Last Updated: 2026-10-30**
+**Last Updated: 2026-11-11**
+
+### 2026-11-11
+
+- Error code documentation corrections:
+  - `PARAM_OVERFLOW` is [`-1018`](errors.md#-1018-param_overflow). It was previously documented as
+    `-1108`.
+  - [`-1108 BAD_ASSET`](errors.md#-1108-bad_asset) "Invalid asset." is now documented. It was
+    previously documented in the testnet [changelog](testnet/CHANGELOG.md#2026-10-28).
+
+**Notice: The changes in this section are being rolled out gradually, and will take approximately
+two weeks to complete.**
+
+#### New Features
+
+- `userDataStream.subscribe` and `userDataStream.subscribe.signature` now accept an optional
+  `filter` parameter controlling which events are delivered. Supports filtering by event type (`e`),
+  symbol (`s`), asset (`a`), and execution type (`x`).
+  - WebSocket API: See
+    [User Data Stream Subscription Filters](web-socket-api.md#user-data-stream-subscription-filters).
+  - Unknown symbols and assets in `filter` are rejected with
+    [`-1121`](errors.md#-1121-bad_symbol) and
+    [`-1108`](errors.md#-1108-bad_asset) respectively.
+
+#### General Changes
+
+- The `serverShutdown` event payload now includes a `T` field indicating when the WebSocket session
+  will be shut down.
+  - [WebSocket API](web-socket-api.md#server-shutdown)
+  - [WebSocket Streams](web-socket-streams.md#server-shutdown)
+  - [SBE Market Data Streams](sbe-market-data-streams.md#server-shutdown)
+  - In SBE sessions, the `T` field is only present in SBE schema 3:6 and later.
+- The error message from `-1015 TOO_MANY_ORDERS` has been changed to "Too many orders placed without
+  trading; current limit is X non-trading orders per Y. Unable to place new orders until trades occur
+  or window resets." See [`-1015`](errors.md#-1015-too_many_orders) and the
+  [Spot Unfilled Order Count Rules FAQ](faqs/order_count_decrement.md#spot-unfilled-order-count-rules).
+
+#### SBE
+
+- REST and WebSocket API SBE schema [spot_3_6.xml](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot_3_6.xml)
+  - The current schema 3:5 [spot_3_5.xml](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot_3_5.xml) is deprecated and
+    will be retired in 6 months per our
+    [schema deprecation policy](faqs/sbe_faq.md#regarding-legacy-support).
+  - Changes in schema 3:6:
+    - Existing `expiryReason` enum: new variants `Exhausted` (9) and
+      `InsufficientQuoteNotionalLimit` (10)
+    - `ServerShutdownEvent`: new field `shutdownTime`
+    - `ExchangeInfoResponse` (symbols group): new fields `marketQuoteNotionalLimitAllowed`,
+      `limitQuoteNotionalLimitAllowed`, `opoAllowed`
+    - `NewOrderResultResponse`, `NewOrderFullResponse`, `OrderResponse`, `CancelOrderResponse`,
+      `OrdersResponse`, `NewOrderListResultResponse`, `NewOrderListFullResponse`,
+      `CancelOrderListResponse`, `OrderAmendKeepPriorityResponse`, `ExecutionReportEvent`: new field
+      `quoteNotionalLimit`
+      - For more details on this field, see [New Features](#2026-11-20-new-features) below.
+    - `ExecutionReportEvent`: new field `effectiveSelfTradePreventionMode`
+      - For more details on this field, see [New Features](#2026-11-20-new-features) below.
+    - `NewOrderFullResponse` and `NewOrderListFullResponse.orderReports` `preventedMatches` group:
+      new field `effectiveSelfTradePreventionMode`
+      - For more details on this field, see [New Features](#2026-11-20-new-features) below.
+  - The [SBE lifecycle for Production](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/sbe_schema_lifecycle_prod.json) has
+    been updated to reflect this change.
+- FIX SBE schema [spot-fixsbe-1_2.xml](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot-fixsbe-1_2.xml)
+  - The current schema 1:1 [spot-fixsbe-1_1.xml](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/spot-fixsbe-1_1.xml) is
+    deprecated and will be retired in 6 months per our
+    [schema deprecation policy](faqs/sbe_faq.md#regarding-legacy-support).
+  - Changes in schema 1:2:
+    - Existing `expiryReason` enum: new variants `Exhausted` (9) and
+      `InsufficientQuoteNotionalLimit` (10)
+    - `ExecutionReport`, `OrderCancelRequestAndNewOrderSingle`, `NewOrderSingle`, `NewOrderList`
+      (`Orders` group): new field `QuoteNotionalLimit` (custom tag 25057)
+      - For more details on this field, see [New Features](#2026-11-20-new-features) below.
+    - `ExecutionReport`: new field `EffectiveSelfTradePreventionMode` (custom tag 25058)
+      - For more details on this field, see [New Features](#2026-11-20-new-features) below.
+  - The [FIX SBE lifecycle for Production](https://github.com/binance/binance-spot-api-docs/blob/master/sbe/schemas/sbe_fix_schema_lifecycle_prod.json)
+    has been updated to reflect this change.
+
+#### FIX API
+
+- The [QuickFix schema for FIX OE](https://github.com/binance/binance-spot-api-docs/blob/master/fix/schemas/spot-fix-oe.xml) has been updated:
+  - `ExpiryReason` (custom tag 25056): new values `EXHAUSTED` (9) and
+    `INSUFFICIENT_QUOTE_NOTIONAL_LIMIT` (10)
+  - `ExecutionReport`, `OrderCancelRequestAndNewOrderSingle`, `NewOrderSingle`, `NewOrderList`
+    (`Orders` group): new field `QuoteNotionalLimit` (custom tag 25057)
+    - For more details on this field, see [New Features](#2026-11-20-new-features) below.
+  - `ExecutionReport`: new field `EffectiveSelfTradePreventionMode` (custom tag 25058)
+    - For more details on this field, see [New Features](#2026-11-20-new-features) below.
+
+**Notice: The following changes will be available after 2026-11-20 07:00 UTC.**
+
+<a id="2026-11-20-new-features"></a>
+
+#### New Features
+
+- Orders on the `BUY` side accept a new optional parameter `quoteNotionalLimit`, which limits the
+  amount of the quote asset the order can spend.
+  **The time this feature will be enabled has not been decided.**
+  - Order lists accept `aboveQuoteNotionalLimit` / `belowQuoteNotionalLimit` (OCO) and
+    `workingQuoteNotionalLimit` / `pendingQuoteNotionalLimit` / `pendingAboveQuoteNotionalLimit` /
+    `pendingBelowQuoteNotionalLimit` (OTO, OTOCO, OPO, OPOCO). See
+    [Quote Notional Limit FAQ](faqs/quoteNotionalLimit.md).
+  - [REST API](rest-api.md#exchange-information) and
+    [WebSocket API](web-socket-api.md#exchange-information) `exchangeInfo` responses show whether a
+    symbol supports the parameter in the new fields `marketQuoteNotionalLimitAllowed` and
+    `limitQuoteNotionalLimitAllowed`.
+  - The new `expiryReason` value
+    [`INSUFFICIENT_QUOTE_NOTIONAL_LIMIT`](enums.md#expiry-reasons) is emitted when the
+    order's `quoteNotionalLimit` prevents the remaining quantity from executing or resting.
+  - SOR endpoints parse the parameter but reject it with
+    [`-1106`](errors.md#-1106-param_not_required).
+  - The legacy OCO endpoints (REST API `POST /api/v3/order/oco`, WebSocket API `orderList.place`) do
+    not accept the new parameters.
+- User Data Stream [`executionReport`](user-data-stream.md#order-update) events, FIX API
+  [`ExecutionReport<8>`](fix-api.md#executionreport-8) messages, and FULL order response
+  `preventedMatches[]` entries now carry an optional `effectiveSelfTradePreventionMode` (`eV` on
+  JSON streams, FIX tag `25058`) distinguishing the STP mode the engine applied from the one the
+  order was placed with. The field is only emitted on prevented-match reports and only when the
+  applied mode differs from the order's own `selfTradePreventionMode`. Values: `EXPIRE_MAKER`,
+  `EXPIRE_BOTH`, `DECREMENT` (never `NONE`, `EXPIRE_TAKER` or `TRANSFER`).
+
+#### General Changes
+
+- Orders amended down to their filled quantity or less now carry `expiryReason` =
+  [`EXHAUSTED`](enums.md#expiry-reasons). Previously, these orders expired without an
+  `expiryReason`.
+- `BUY` limit orders that trade on entry and then rest now release any order lock above what the
+  remaining quantity needs to rest (remaining quantity × limit price). The surplus, usually the
+  price improvement from the trade, is returned to `free` in the same balance update that the order
+  rests in. Previously, the surplus stayed locked until the order ended.
+  - Applies to `LIMIT` `GTC` orders, triggered `STOP_LOSS_LIMIT` and `TAKE_PROFIT_LIMIT` orders,
+    limit orders in order lists, and SOR orders. Iceberg orders keep the lock for their whole
+    remaining quantity, including the hidden part.
+
+#### Bug Fixes
+
+- SBE responses for canceling an order list now encode `listClientOrderId` as the
+  `listClientOrderId` of the original order list, matching the JSON response. Previously, SBE
+  responses encoded the `listClientOrderId` sent in the cancel request.
+  - REST API: `DELETE /api/v3/orderList`, `DELETE /api/v3/openOrders`
+  - WebSocket API: `orderList.cancel`, `openOrders.cancelAll`
+
+---
 
 ### 2026-10-30

```

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 1b073ed..df0bbeb 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -80,4 +80,12 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | 参数名 | 类型 | 描述
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
+2026-11-11
+开平仓模式下最大可开数量方向差异化计算
+在开平仓模式下，针对 SWAP 和 FUTURES 产品，计算最大可开数量时使用的梯度档位因子已区分多头和空头方向，同一杠杆倍数下多空方向的最大可开数量可能不同。
+- 更新以下返回参数的描述，以反映开平仓模式下方向差异化的梯度档位因子：
+  - estMaxAmt：GET / 获取杠杆倍数预估信息
+  - maxBuy、maxSell：GET / 获取最大可下单数量
+  - availBuy、availSell：GET / 获取最大可用余额/保证金
+- 更新 GET / 获取杠杆倍数预估信息 中请求参数 posSide 的描述，说明在开平仓模式下建议传入 long 或 short 以获取准确的方向差异化结果。
 2026-11-05
 ELP 命名停止支持，请使用 RPI 命名

```
