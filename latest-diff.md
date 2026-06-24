<!-- has_changes=true date=2026-06-24 -->
# Exchange API Changelog Diff

Generated: 2026-06-24 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (130905 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (87509 bytes)

- [CHANGED] **OKX V5** (`okx`): 79 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 30 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (32707 bytes)

- [FAIL] **Gate.io Spot WebSocket v4** (`gate-spot-ws`): HTTPError

- [FAIL] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): HTTPError



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 208af69..5243184 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,6 +1,6 @@
 待发布内容
 交易产品价格限制 XYZ 参数
-最近更新：2026年6月18日
-为方便 API 用户动态获取合约价格限制参数而无需硬编码，OKX 现通过交易产品基础信息接口公开价格限制 X、Y、Z 参数。由这些参数推算出的价格限制可通过 GET / 获取限价 获取。详情参阅价格限制规则。本次变更预计于 2026年6月23日 上线。
+最近更新：2026年6月23日
+为方便 API 用户动态获取合约价格限制参数而无需硬编码，OKX 现通过交易产品基础信息接口公开价格限制 X、Y、Z 参数。由这些参数推算出的价格限制可通过 GET / 获取限价 获取。详情参阅价格限制规则。本次变更预计于 2026年6月24日 在模拟盘上线，并于 2026年6月30日 正式上线。
 - 在以下接口新增返回参数 initPxLmtPct、floatPxLmtPct、maxPxLmtPct：
   - GET / 获取交易产品基础信息（公共）
@@ -14,11 +14,4 @@
 | maxPxLmtPct | String | 最大价格限制上限（硬性上限），小数百分比，例如 0.15 = 15%。
 适用于 SPOT/MARGIN/SWAP/FUTURES；OPTION 和 EVENTS 返回 ""。
-WebSocket服务升级断线提示扩展至业务频道
-最后更新：2026 年 5 月 21 日
-WebSocket服务升级断线提示（错误码 64008）将扩展支持业务频道（/ws/v5/business）。
-在业务频道服务升级前60秒，将向用户推送如下消息，告知WebSocket连接即将断开。建议用户提前重新建立连接，以避免断线造成影响。
-该功能上线后将支持WebSocket公共频道(/ws/v5/public)、私有频道(/ws/v5/private)和业务频道(/ws/v5/business)。
-模拟盘上线日期：2026 年 6 月 4 日
- 实盘上线日期：2026 年 6 月 11 日
 信号复制新增 API 接口
 最后更新：2026 年 5 月 14 日
@@ -43,21 +36,7 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | 参数名 | 类型 | 描述
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
-深度频道 checksum 字段废弃
-最后更新：2026 年 6 月 9 日
-为了提升行情数据推送的效率和稳定性，以下深度频道将废弃全量快照和增量更新中的 checksum 字段。
-废弃后，checksum 字段仍会保留在全量快照和增量更新中，但其值将固定为 0，不应再用于数据完整性校验。请在废弃生效之前，改用 seqId/prevSeqId 校验数据的连续性和准确性。
-模拟盘已于 2026 年 6 月 2 日 废弃
- 实盘废弃日期：2026 年 6 月 23 日
-- 废弃全量快照和增量更新中的 checksum 字段（字段仍保留在推送中，但其值将固定为 0）。
-  - WS / 深度频道
-    - books
-    - books-l2-tbt
-    - books50-l2-tbt
-注意:
- 1. books5 和 bbo-tbt 频道本身不包含 checksum 字段，不在本次变更范围内。
- 2. WebSocket 连接已全面启用 TLS（wss://），具备防窃听、防篡改以及完整性校验的能力；结合 seqId/prevSeqId 的严格校验，可有效防止数据乱序、部分丢失或被恶意注入，实现与原 checksum 等效甚至更强的完整性保护。
 ELP 合并深度订单簿
-最近更新：2026年6月8日
-为简化 ELP 行情数据集成，OKX 将推出合并深度频道 books-elp-all，将非 ELP 与当前可交易的 ELP 流动性合并为单一数据流，用户无需再分别订阅 books 和 books-elp 并在客户端自行合并。该能力同时提供 WebSocket 与 REST 两种方式，预计于 2026年6月下旬 上线。
+最近更新：2026年6月23日
+为简化 ELP 行情数据集成，OKX 将推出合并深度频道 books-elp-all，将非 ELP 与当前可交易的 ELP 流动性合并为单一数据流，用户无需再分别订阅 books 和 books-elp 并在客户端自行合并。该能力同时提供 WebSocket 与 REST 两种方式，预计于 2026年7月中旬 在模拟盘上线，并于 2026年7月下旬 正式上线。
 - 通过 /ws/v5/business 端点（wss://ws.okx.com:8443/ws/v5/business）新增 WebSocket 频道 books-elp-all。400 档深度；初始全量推送 + 每 100 毫秒增量推送。推送合并非 ELP 和当前可交易 ELP 流动性的深度数据。不可交易的 ELP 订单在平台端过滤。
   - WS / books-elp-all 频道
@@ -99,6 +78,6 @@ GET /api/v5/market/books-elp-all?instId=BTC-USDT-SWAP
 | seqId | Integer | 当前推送消息的序列号
 ELP 吃单权限扩展至所有订单类型
-最近更新：2026年6月8日
-订单参数 isElpTakerAccess 将扩展支持所有订单类型（此前仅 ioc），并新增支持在改单接口中使用。本次变更预计于 2026年6月下旬 上线。
+最近更新：2026年6月23日
+订单参数 isElpTakerAccess 将扩展支持所有订单类型（此前仅 ioc），并新增支持在改单接口中使用。本次变更预计于 2026年7月中旬 在模拟盘上线，并于 2026年7月下旬 正式上线。
 - 更新请求参数 isElpTakerAccess 的描述，以反映扩展的订单类型支持和改单行为：
   - POST / 下单
@@ -113,5 +92,20 @@ ELP 吃单权限扩展至所有订单类型
 | 参数名 | 类型 | 是否必须 | 描述
 | isElpTakerAccess | Boolean | 否 | 默认值为 false。设为 true 时，订单可以使用 ELP 流动性。适用于所有订单类型。当 isElpTakerAccess 为 true 时，除 post_only 外的所有订单类型都会触发减速带机制；下单时 post_only 订单可免于减速带。isElpTakerAccess 也可在改单接口中使用，且不会从原始订单继承——必须在每次改单请求中显式重新指定（改单时省略则该次改单视为 false）。改单时，减速带适用于所有订单类型（包括 post_only）；如需改 post_only 订单且不想触发减速带，请在该次改单中不设置 isElpTakerAccess。
+2026-06-23
+深度频道 checksum 字段废弃
+为了提升行情数据推送的效率和稳定性，以下深度频道已废弃全量快照和增量更新中的 checksum 字段。checksum 字段仍保留在全量快照和增量更新中，但其值固定为 0，不应再用于数据完整性校验。请改用 seqId/prevSeqId 校验数据的连续性和准确性。
+- 废弃全量快照和增量更新中的 checksum 字段（字段仍保留在推送中，但其值固定为 0）。
+  - WS / 深度频道
+    - books
+    - books-l2-tbt
+    - books50-l2-tbt
+注意:
+ 1. books5 和 bbo-tbt 频道本身不包含 checksum 字段，不在本次变更范围内。
+ 2. WebSocket 连接已全面启用 TLS（wss://），具备防窃听、防篡改以及完整性校验的能力；结合 seqId/prevSeqId 的严格校验，可有效防止数据乱序、部分丢失或被恶意注入，实现与原 checksum 等效甚至更强的完整性保护。
 2026-06-11
+WebSocket服务升级断线提示扩展至业务频道
+WebSocket服务升级断线提示（错误码 64008）已扩展支持业务频道（/ws/v5/business）。
+在业务频道服务升级前60秒，将向用户推送如下消息，告知WebSocket连接即将断开。建议用户提前重新建立连接，以避免断线造成影响。
+该功能已支持WebSocket公共频道(/ws/v5/public)、私有频道(/ws/v5/private)和业务频道(/ws/v5/business)。
 申请账单流水（自 2021 年）：限速放宽
 POST / 申请账单流水（自 2021 年） 的限速由 12 次/天 调整为 1 次/10s（按用户维度）。

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 025789d..c317899 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,6 +1,16 @@
+2026-06-23​
+REST API​
+- Get Coin Delta Amount [NEW]
+  - New endpoint to query coin delta amount details for institutional loan hedge product
+- Get Product Info [UPDATE]
+  - Add new response field productType (0: Default, 1: CTA, 2: Hedge)
 2026-06-16​
 REST API​
 - Get Futures Leverage [NEW]
   - Add a new endpoint to get futures leverage in one request
+- Get Coupon List [NEW]
+  - New endpoint to query interest-rate coupons and Dual Assets reward cards
+- Stake / Redeem [UPDATE]
+  - Add new optional request parameter interestCard (interest bonus card, only applicable to FlexibleSaving Stake orders)
 Alpha LP — New Endpoints
 - Execute LP Stake [NEW]
@@ -12,8 +22,4 @@ Alpha LP — New Endpoints
 - Get LP Pool List [NEW]
 - Get LP Position List [NEW]
-- Get Coupon List [NEW]
-  - New endpoint to query interest-rate coupons and Dual Assets reward cards
-- Stake / Redeem [UPDATE]
-  - Add new optional request parameter interestCard (interest bonus card, only applicable to FlexibleSaving Stake orders)
 2026-06-15​
 REST API​

```
