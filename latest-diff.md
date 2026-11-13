<!-- has_changes=true date=2026-11-13 -->
# Exchange API Changelog Diff

Generated: 2026-11-13 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (146418 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 23 diff lines

- [CHANGED] **Bitget (Spot + Futures)** (`bitget`): 29 diff lines

- [OK] Bybit V5 (`bybit`): no change (100865 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (44528 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (164576 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index df0bbeb..06c7341 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -23,6 +23,6 @@ REST API 不受影响。
 | 64010 | WebSocket 8443 端口即将下线，请迁移至 443 端口。
 SBE 交易及私有数据
-最近更新：2026 年 11 月 10 日
-欧易计划推出简单二进制编码（Simple Binary Encoding，SBE）交易服务，以及私有订单与成交数据服务。相关服务预计于 2026 年 11 月 12 日上线模拟交易环境，并于 2026 年 12 月上旬上线生产环境。
+最近更新：2026 年 11 月 12 日
+欧易计划推出简单二进制编码（Simple Binary Encoding，SBE）交易服务，以及私有订单与成交数据服务。相关服务预计于 2026 年 11 月 13 日上线模拟交易环境，并于 2026 年 12 月上旬上线生产环境。
 现有 REST API 和 JSON WebSocket API 不受影响。
 新增 SBE 服务
@@ -80,4 +80,9 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | 参数名 | 类型 | 描述
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
+2026-11-12
+股票类衍生品公司行动查询
+新增公开接口，用于查询影响股票类衍生品的公司行动事件（现金分红、股票拆分、反向拆分、股票分红及分拆上市）。接口返回事件元数据、处理状态及对关联 OKX 产品的影响。
+- 新增接口：
+  - GET / 获取公司行动
 2026-11-11
 开平仓模式下最大可开数量方向差异化计算

```

### Bitget (Spot + Futures) (`bitget`)
- Source: https://www.bitget.com/api-doc/common/changelog
- Raw: https://www.bitget.fit/api-doc/common/changelog

```diff
diff --git a/changelogs/bitget.txt b/changelogs/bitget.txt
index 74efbdd..ebbdb16 100644
--- a/changelogs/bitget.txt
+++ b/changelogs/bitget.txt
@@ -1,18 +1,19 @@
 The unified account is a next-generation trading system introduced by Bitget, designed to allow users to trade spot and various derivatives using multiple crypto assets within a single account. This system simplifies the trading process by eliminating the need for fund transfers between different accounts. Moreover, profits and losses across different products can be calculated and offset together, enhancing capital efficiency.
 Comparison of Account Mode
-The Unified Account provides users with three new account modes to satisfy the trading preferences and needs of different users: Isolated margin mode, Basic Mode, and Advanced Mode.
+The Unified Account provides users with three new account modes to satisfy the trading preferences and needs of different users: Spot + Isolated Margin Mode, Stablecoin Margin Mode, and Multi-Asset Margin Mode.
+Note: These modes were previously named Isolated margin mode, Basic Mode, and Advanced Mode respectively. The API enum values (isolated / basic / advanced) remain unchanged.
 | Account mode | Feature | Available products | Margin support
-| Isolated margin mode | Each position carries independent risk, and PnL from one position does not affect others | 1. Spot
+| Spot + Isolated Margin Mode | Each position carries independent risk, and PnL from one position does not affect others | 1. Spot
 2. USDT-M Futures (isolated margin)
 3. USDC-M Futures (isolated margin) | Collateral settings are not supported
-| Basic mode | Improves capital efficiency, but only supports stablecoins as margin (no multi-asset collateral). | 1. Spot
+| Stablecoin Margin Mode | Improves capital efficiency, but only supports stablecoins as margin (no multi-asset collateral). | 1. Spot
 2. USDT-M Futures (cross/isolated margin)
 3. USDC-M Futures (cross/isolated margin) | USDT- and USDC-margined pairs share the same margin pool. Collateral settings are not supported
-| Advanced mode | Multiple assets can be used as margin based on their respective collateral ratios. Supports cross-currency risk hedging and maximizes capital efficiency. | 1. Spot
+| Multi-Asset Margin Mode | Multiple assets can be used as margin based on their respective collateral ratios. Supports cross-currency risk hedging and maximizes capital efficiency. | 1. Spot
 2. Spot margin
 3. USDT-M Futures (cross/isolated margin)
 4. USDC-M Futures (cross/isolated margin)
 5. Coin-M Futures (cross/isolated margin) | Collateral settings are supported.
-In Advanced Mode, all assets across product types can be used as shared margin, and PnL can be mutually offset. Please refer to this document for details.
+In Multi-Asset Margin Mode, all assets across product types can be used as shared margin, and PnL can be mutually offset. Please refer to this document for details.
 Asset-related Terminology
 | Term | Explanation

```
