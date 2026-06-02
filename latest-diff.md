<!-- has_changes=true date=2026-06-02 -->
# Exchange API Changelog Diff

Generated: 2026-06-02 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128989 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [CHANGED] **OKX V5** (`okx`): 45 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (80145 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 43 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (138977 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 5c1dc9b..57790b8 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,8 +1,12 @@
 待发布内容
 SPACEX 永续合约重命名
-最后更新：2026年5月28日
-为了优化用户交易体验，欧易将在 2026 年 6 月 1 日至 6 月 5 日（UTC）期间的某一天 将 SPACEXUSDT 永续合约更名为 SPCXUSDT 永续合约。
+最后更新：2026年6月1日
+为了优化用户交易体验，欧易将于 2026 年 6 月 2 日 将 SPACEXUSDT 永续合约更名为 SPCXUSDT 永续合约。更多内容请参考公告详情
 - 更名时：
-  - 产品频道 会推送 instId: SPCX-USDT-SWAP, state: expired 的更新数据，和 instId: SPCX-USDT-SWAP, state: live 的数据。
+  - 产品频道 将按以下顺序推送更新数据：
+    - instId: SPACEX-USDT-SWAP, state: expired
+    - instId: SPCX-USDT-SWAP, state: rebase
+    - instId: SPCX-USDT-SWAP, state: post_only
+    - instId: SPCX-USDT-SWAP, state: live
 - 更名后：
   - 推送数据中的 instId instFamily, uly 会使用新的参数值。
@@ -60,4 +64,24 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
  1. books5 和 bbo-tbt 频道本身不包含 checksum 字段，不在本次变更范围内。
  2. WebSocket 连接已全面启用 TLS（wss://），具备防窃听、防篡改以及完整性校验的能力；结合 seqId/prevSeqId 的严格校验，可有效防止数据乱序、部分丢失或被恶意注入，实现与原 checksum 等效甚至更强的完整性保护。
+风险保证金 API 更新 — REST 日级快照与 WS 推送变更
+最近更新：2026年5月29日
+为优化风险保证金数据披露，REST GET /api/v5/public/insurance-fund 接口和 WS adl-warning 频道将进行以下变更。本次变更预计于 2026年6月9日 上线。
+不兼容变更
+WS adl-warning 频道将停止在 normal 状态下推送数据。所有字段保留在推送响应中，但以下字段将返回空值（""）。如果您的应用依赖 normal 状态推送或这些字段的值，请在上线日期前完成相应调整。
+- 更新了 regular_update 类型的描述。数据粒度从分钟级变更为日级快照。数据在每日结算后更新一次（约 UTC 08:00）。type 字段保留 regular_update 值，但关联字段将返回空值：
+  - GET / 获取风险保证金余额
+- WS adl-warning 频道将停止在 normal 状态下推送数据。在 warning 或 adl 状态下，数据继续每秒推送一次。所有字段保留，但以下字段将返回空值（""）：
+  - WS / 自动减仓预警频道
+WS 推送数据中将返回空值的字段
+| 参数名 | 类型 | 描述
+| > ccy | String | 风险保证金余额对应币种。将返回 ""
+| > maxBal | String | 过去八小时内的风险保证金余额最大值。将返回 ""
+| > maxBalTs | String | 过去八小时内风险保证金余额最大值对应的时间戳。将返回 ""
+| > adlType | String | 关于自动减仓的事件。将返回 ""
+| > adlBal | String | 触发自动减仓的风险保证金余额。将返回 ""
+| > adlRecBal | String | 自动减仓结束的风险保证金余额。将返回 ""
+| > decRate | String | 风险保证金实时下降率（已弃用）。将返回 ""
+| > adlRate | String | 触发自动减仓的风险保证金下降率（已弃用）。将返回 ""
+| > adlRecRate | String | 自动减仓结束的风险保证金下降率（已弃用）。将返回 ""
 ELP 合并深度订单簿
 最近更新：2026年5月29日

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index 852f962..ec007a6 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,4 +1,38 @@
 WARNING
 The Pro API is currently in beta testing and should not be used in production trading environments.
+2026.06.03#
+1. UTA API Upgrade#
+Currently, certain Pro API endpoints are compatible with both Classic Accounts and Unified Trading Accounts (UTA). Moving forward, we will continue to focus on the Unified Trading Account framework and further enhance the UTA API with new capabilities and feature optimizations. Compatibility support related to Classic Accounts will enter maintenance mode and will no longer be the primary focus for future feature development, performance improvements, or long-term platform evolution.
+[Adjustment Details]
+The Pro API will be upgraded to the UTA API, which will primarily support the Unified Trading Account (UTA) going forward.
+Compatibility support related to the Classic Account within UTA API will enter maintenance mode.
+If you are currently using the “Pro API + Classic Account” model, we strongly recommend completing one of the following migration options as soon as possible:
+Switch to the Unified Trading Account (UTA) mode for trading;
+Continue using the Classic API for Classic Account trading.
+This will help ensure a smooth migration and uninterrupted trading operations.
+2. API Upgrades#
+[Modify] UTA REST Get Position List (UTA), added response field:
+positionMargin: Margin occupied by the futures position.
+riskRatio: Risk ratio of an isolated futures position.
+[Modify] UTA Websocket Position, added response field:
+pM: Margin occupied by the futures position.
+r: Risk ratio of an isolated futures position. For example, 0.65 represents 65%.
+[Modify] Classic REST Get Deposit List & Classic REST Get Deposit Detail. The endpoints have added the following status return values to display more detailed deposit statuses:
+ROLLBACKING : Reversing deposit. Please wait.
+ROLLBACK : Deposit reversed. No funds have been credited to the account. Please contact support for assistance.
+WAIT_RISK_MGT: The deposit is undergoing standard risk verification. Please contact support for assistance.
+RISK_MGT_REJECTED : The deposit is rejected after risk verification. Please contact support to submit required information for review.
+PRE_SUCCESS: Funds have been credited to the account ahead of final Block confirmation.
+WAIT_TRM_MGT: The deposit is undergoing standard compliance verification. Please contact support for assistance.
+TRM_MGT_REJECTED : The deposit is rejected after risk verification. Please contact support to submit required information for review.
+[Add] UTA REST Batch Modify Margin Mode ,batch modifies the margin mode for futures positions
+[Add] UTA REST Modify Isolated Futures Margin ,extract or add margin for Isolated Futures position
+[Modify] UTA REST Place Order ,add new field 'closeOrder' to support closing position for specified symbol
+[Modify] UTA REST Get Transfer Quotas ,add new enum 'UNIFIED' in feild 'accountType' in query params and response params
+[Modify] UTA Error Code updated to the new version, split into the following modules: UTA General, UTA Account Opening, UTA Order, UTA Account, UTA Position, UTA Spot Trading, UTA Leverage, UTA Futures Trading, UTA Loan
+[Add] Fast API Apply for Fast Withdrawal
+Support user-defined API key permissions in the OAuth authorization flow, including granting withdrawal permissions
+New permission: Fast Withdrawal (Fast API withdrawal permission)
+Support API withdrawal with 2FA verification
 2026.05.15#
 [Modify] Pro REST Get Position List (UTA)

```
