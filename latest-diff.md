<!-- has_changes=true date=2026-09-16 -->
# Exchange API Changelog Diff

Generated: 2026-09-16 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (131990 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 42 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3256 bytes)

- [OK] Bybit V5 (`bybit`): no change (95421 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 17 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (124213 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 739627c..3193fc8 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,5 +1,5 @@
 待发布内容
 欧易将进行 USD 现货交易对迁移
-最后更新：2026 年 9 月 2 日
+最后更新：2026 年 9 月 11 日
 OKX 将合并 USD 与 USDC 现货深度。作为本次调整的一部分，受影响的 Crypto-USD 现货产品将下线，用户需迁移至对应的 Crypto-USDC 产品。本次调整属于不兼容变更。更多详情，请根据所在地区参阅对应公告： USD 现货交易对迁移或 USDⓢ 现货交易对迁移，请以所在地区可访问的公告为准。
 USDC 交易对开放及并行期
@@ -39,4 +39,8 @@ POST /api/v5/account/activate-feature body { "feature": "1" }
 返回参数
 无
+新增错误码
+若账户尚未开通 USDC 交易功能，下单时将返回以下错误：
+| 错误码 | HTTP 状态码 | 错误提示
+| 54109 | 200 | 您尚未开通该币对交易。请登录 欧易 App 或官网，进入该币对交易页面并点击"交易"完成开通，或调用指定 API 接口开通后重试。
 信号复制新增 API 接口
 最后更新：2026 年 5 月 14 日
@@ -61,4 +65,21 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | 参数名 | 类型 | 描述
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
+2026-09-15
+RPI 挂单最小名义金额门槛
+RPI 挂单（ordType: rpi 或 elp）现按产品类型使用不同的最小名义金额门槛。低于适用门槛的订单将被拒绝，返回错误码 54051。生产环境自 2026年9月15日 起生效。
+各产品类型最低门槛
+| 产品类型 | 最小名义金额
+| SPOT | 500 USD
+| FUTURES | 2,000 USD
+| SWAP | 5,000 USD
+适用于所有 REST 及 WebSocket trade 操作：
+- POST / 下单
+- POST / 批量下单
+- POST / 修改订单
+- POST / 批量修改订单
+- WS / 下单
+- WS / 批量下单
+- WS / 改单
+- WS / 批量改单
 2026-08-26
 新增接口：获取 Delta 对冲币种

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index 2b8f562..c773e10 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,2 +1,12 @@
+2026.09.21#
+[Modify] UTA REST Get Trade History Add the fillPnl field, FillPnl data before 2026.9.05 (UTC-8) cannot be queried and will return ""
+[Modify] UTA Websocket Execution Add new field fP, FillPnl data before 2026.9.05 (UTC-8) cannot be queried and will return ""
+[Modify] Classic REST Get Symbol & Get All Symbols
+Add the response field assetClass ,subMarketType. Updated response field status:marketType marked as deprecated; use assetClass and subMarketType instead.
+[Modify] UTA REST Place Order& Get Order Details & UTA WebSocket Order
+Add brokerTag (≤50 chars) to all place-order interfaces, decoupling from capped tags (20 chars) to fix broker API order failures. Covers UTA REST/WebSocket order.
+New error code
+| Error Code | Message
+| 116241 | Positions in your associated accounts have reached the system risk limit. You can't open new positions or add to existing ones. Please use close position or reduce-only orders.
 2026.09.04#
 New error code

```
