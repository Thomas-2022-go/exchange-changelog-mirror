<!-- has_changes=true date=2026-09-07 -->
# Exchange API Changelog Diff

Generated: 2026-09-07 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (131990 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 47 diff lines

- [CHANGED] **Bitget (Spot + Futures)** (`bitget`): 30 diff lines

- [OK] Bybit V5 (`bybit`): no change (94713 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42000 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (124213 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 739627c..551adc3 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,42 +1,3 @@
 待发布内容
-欧易将进行 USD 现货交易对迁移
-最后更新：2026 年 9 月 2 日
-OKX 将合并 USD 与 USDC 现货深度。作为本次调整的一部分，受影响的 Crypto-USD 现货产品将下线，用户需迁移至对应的 Crypto-USDC 产品。本次调整属于不兼容变更。更多详情，请根据所在地区参阅对应公告： USD 现货交易对迁移或 USDⓢ 现货交易对迁移，请以所在地区可访问的公告为准。
-USDC 交易对开放及并行期
-自 2026 年 9 月 23 日下午 4:00（UTC+8） 起，OKX 将开放相关 Crypto-USDC 现货产品。自开放起至 2026 年 9 月 30 日下午 4:00（UTC+8） 相关 Crypto-USD 现货产品下线前，部分 Crypto-USD 产品及其对应的 Crypto-USDC 产品将同时开放交易。
-API 用户可在并行期内提前迁移至对应的 Crypto-USDC 产品 ID，适配 tradeQuoteCcy 的传参逻辑，并验证请求、返回及 WebSocket 订阅逻辑。
-不兼容变更
-- 当前请求中使用 Crypto-USD 产品 ID 的用户，需在变更上线后改用对应的 Crypto-USDC 产品 ID。在开始交易 Crypto-USDC 产品前，请先调用 POST /api/v5/account/activate-feature 接口开通 USDC 交易功能。已经在交易 USDC 产品的账户不受影响。
-- 影响范围包括请求参数中包含 instId 或 instIdCode 的 REST API 和 WebSocket 频道，包括交易、订单查询、账户查询、策略交易、大宗交易、价差交易、行情请求及 WebSocket 订阅。
-- Crypto-USD 产品 ID 不会映射为 Crypto-USDC 产品 ID。变更上线后，继续使用已下线的 Crypto-USD instId 或 instIdCode 发起请求或订阅，可能会失败或返回空数据。
-- 返回参数将使用实际的 Crypto-USDC 产品 ID 或产品 ID Code。请在上线前更新请求构造、返回解析、订阅管理、产品缓存，以及所有依赖 instId 或 instIdCode 的业务逻辑。
-重要：迁移下单时需正确传入 tradeQuoteCcy
-tradeQuoteCcy 的默认值为 instId 中的计价币种。因此，如果仅将 instId 从 Crypto-USD 改为 Crypto-USDC，默认交易计价币种也会从 USD 变为 USDC。
-如果您当前交易 Crypto-USD 产品时未传入 tradeQuoteCcy，迁移至对应的 Crypto-USDC 产品后仍希望使用 USD 交易，则必须显式传入 tradeQuoteCcy=USD。
-| 场景 | 变更前 | 变更后
-| 继续使用 USD 交易 | "instId": "Crypto-USD"
-未传 tradeQuoteCcy | "instId": "Crypto-USDC"
-"tradeQuoteCcy": "USD"
-| 使用 USDC 交易 | "instId": "Crypto-USD"
-"tradeQuoteCcy": "USDC" | "instId": "Crypto-USDC"
-"tradeQuoteCcy": "USDC"；如果希望使用默认值 USDC，也可不传 tradeQuoteCcy
-下单前，请通过 获取交易产品基础信息（私有） 接口获取 tradeQuoteCcyList。传入的 tradeQuoteCcy 必须是当前产品及账户对应的 tradeQuoteCcyList 枚举值。
-该迁移规则也适用于其他使用相关请求参数计算可交易数量或提交现货订单的接口，包括 获取最大可用余额/保证金、获取最大可下单数量 及 获取交易产品最大可借。
-新增接口：开通 USDC 交易功能
-在开始交易 Crypto-USDC 产品前，请先调用以下接口为账户开通 USDC 交易功能。已经在交易 USDC 产品的账户不受影响。
-限速：5 次/2 秒
-限速规则：User ID
-HTTP 请求
-POST /api/v5/account/activate-feature
-请求示例
-POST /api/v5/account/activate-feature body { "feature": "1" }
-请求参数
-| 参数名 | 类型 | 是否必须 | 描述
-| feature | String | 是 | 要开通的具体功能
-1：USDC 订单簿交易功能。在开始交易 Crypto-USDC 产品前需先开通该功能。已经在交易 USDC 产品的账户不受影响。母账户与子账户之间不共享开通状态，每个母账户和子账户均需分别调用，且各自仅需调用一次。
-返回结果
-{ "code": "0", "msg": "", "data": [] }
-返回参数
-无
 信号复制新增 API 接口
 最后更新：2026 年 5 月 14 日

```

### Bitget (Spot + Futures) (`bitget`)
- Source: https://www.bitget.com/api-doc/common/changelog
- Raw: https://www.bitget.fit/api-doc/common/changelog

```diff
diff --git a/changelogs/bitget.txt b/changelogs/bitget.txt
index 6e70a80..ae205ac 100644
--- a/changelogs/bitget.txt
+++ b/changelogs/bitget.txt
@@ -1,7 +1,4 @@
-Unified Trading Account
-Copy Page
-Unified Trading Account
 The unified account is a next-generation trading system introduced by Bitget, designed to allow users to trade spot and various derivatives using multiple crypto assets within a single account. This system simplifies the trading process by eliminating the need for fund transfers between different accounts. Moreover, profits and losses across different products can be calculated and offset together, enhancing capital efficiency.
-Comparison of Account Mode​
+Comparison of Account Mode
 The Unified Account provides users with three new account modes to satisfy the trading preferences and needs of different users: Isolated margin mode, Basic Mode, and Advanced Mode.
 | Account mode | Feature | Available products | Margin support
@@ -17,7 +14,6 @@ The Unified Account provides users with three new account modes to satisfy the t
 4. USDC-M Futures (cross/isolated margin)
 5. Coin-M Futures (cross/isolated margin) | Collateral settings are supported.
-In Advanced Mode, all assets across product types can be used as shared margin, and PnL can be mutually offset.
- Please refer to this document for details.
-Asset-related Terminology​
+In Advanced Mode, all assets across product types can be used as shared margin, and PnL can be mutually offset. Please refer to this document for details.
+Asset-related Terminology
 | Term | Explanation
 | Equity | The total equity of a specific coin in the cross margin account.
@@ -35,4 +31,5 @@ Maintenance margin = Sum[quantity of coin in cross margin positions × coin pric
 Maintenance margin = Position value × maintenance margin rate
 | Margin rate | A risk measurement indicator for cross margin accounts.
-Cross margin account's margin ratio = (maintenance margin + partial liquidation transaction fees)÷Account equity.
+Cross margin account's margin ratio = (maintenance margin + partial liquidation transaction fees) ÷ Account equity.
 Both maintenance margin and partial liquidation transaction fees are calculated by adding the position size and the open order size.
+Reality Trading Guide

```
