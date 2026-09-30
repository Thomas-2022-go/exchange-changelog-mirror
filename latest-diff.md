<!-- has_changes=true date=2026-09-30 -->
# Exchange API Changelog Diff

Generated: 2026-09-30 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132590 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 28 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 16 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42424 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (124213 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 32d6c76..dbde4d4 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,3 +1,9 @@
 待发布内容
+交易产品频道推送优化
+最后更新：2026 年 9 月 29 日
+OKX 计划于 2026 年 9 月 30 日优化交易产品频道的推送方式。
+在部分场景中，该频道将由全量推送改为增量推送，仅推送数据发生变化的产品。
+未来可能会有更多场景由全量推送改为增量推送，届时不再另行通知。
+客户端收到推送后，应根据 instId 更新本地产品缓存，不应假设每次推送均包含全量产品数据。
 欧易将进行 USD 现货交易对迁移
 最后更新：2026 年 9 月 28 日
@@ -7,5 +13,5 @@ USDC 交易对开放及并行期
 API 用户可在并行期内提前迁移至对应的 Crypto-USDC 产品 ID，适配 tradeQuoteCcy 的传参逻辑，并验证请求、返回及 WebSocket 订阅逻辑。
 不兼容变更
-- 当前请求中使用 Crypto-USD 产品 ID 的用户，需在变更上线后改用对应的 Crypto-USDC 产品 ID。在开始交易 Crypto-USDC 产品前，请先调用 POST /api/v5/account/activate-feature 接口开通 USDC 交易功能。已经在交易 USDC 产品的账户不受影响。
+- 当前请求中使用 Crypto-USD 产品 ID 的用户，需在变更上线后改用对应的 Crypto-USDC 产品 ID。若下单返回错误码 54109，请调用 POST /api/v5/account/activate-feature 接口开通 USDC 交易功能；否则无需调用该接口。
 - 影响范围包括请求参数中包含 instId 或 instIdCode 的 REST API 和 WebSocket 频道，包括交易、订单查询、账户查询、策略交易、大宗交易、价差交易、行情请求及 WebSocket 订阅。
 - Crypto-USD 产品 ID 不会映射为 Crypto-USDC 产品 ID。变更上线后，继续使用已下线的 Crypto-USD instId 或 instIdCode 发起请求或订阅，可能会失败或返回空数据。
@@ -24,5 +30,5 @@ tradeQuoteCcy 的默认值为 instId 中的计价币种。因此，如果仅将
 该迁移规则也适用于其他使用相关请求参数计算可交易数量或提交现货订单的接口，包括 获取最大可用余额/保证金、获取最大可下单数量 及 获取交易产品最大可借。
 新增接口：开通 USDC 交易功能
-在开始交易 Crypto-USDC 产品前，请先调用以下接口为账户开通 USDC 交易功能。已经在交易 USDC 产品的账户不受影响。
+若下单返回错误码 54109，请调用以下接口为账户开通 USDC 交易功能；否则无需调用该接口。
 限速：5 次/2 秒
 限速规则：User ID

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index a31131c..89d3fc1 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,11 @@
+2026-09-29​
+REST API​
+- Get Instruments Info [UPDATE]
+  - Add new response field tags, an array of symbol tags such as ST. Applies to linear and inverse.
+- Batch Request Export Reports [NEW]
+  - Add POST /v5/fht/compliance/tax/private/batch_create to export multiple types of tax reports in a batch. Supports time ranges of up to 12 months and CSV/ORC formats.
+  - Set type=ALL to export all report types supported by the current site; the number value is ignored.
+- Get Batch Export Report Status [NEW]
+  - Add GET /v5/fht/compliance/tax/private/batch_query to query each task's status and download URL by batchId.
 2026-09-23​
 REST API​

```
