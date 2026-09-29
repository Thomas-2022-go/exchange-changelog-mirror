<!-- has_changes=true date=2026-09-29 -->
# Exchange API Changelog Diff

Generated: 2026-09-29 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132590 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 21 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [OK] Bybit V5 (`bybit`): no change (96385 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42424 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (124213 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 3193fc8..32d6c76 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,5 +1,5 @@
 待发布内容
 欧易将进行 USD 现货交易对迁移
-最后更新：2026 年 9 月 11 日
+最后更新：2026 年 9 月 28 日
 OKX 将合并 USD 与 USDC 现货深度。作为本次调整的一部分，受影响的 Crypto-USD 现货产品将下线，用户需迁移至对应的 Crypto-USDC 产品。本次调整属于不兼容变更。更多详情，请根据所在地区参阅对应公告： USD 现货交易对迁移或 USDⓢ 现货交易对迁移，请以所在地区可访问的公告为准。
 USDC 交易对开放及并行期
@@ -34,5 +34,8 @@ POST /api/v5/account/activate-feature body { "feature": "1" }
 | 参数名 | 类型 | 是否必须 | 描述
 | feature | String | 是 | 要开通的具体功能
-1：USDC 订单簿交易功能。在开始交易 Crypto-USDC 产品前需先开通该功能。已经在交易 USDC 产品的账户不受影响。母账户与子账户之间不共享开通状态，每个母账户和子账户均需分别调用，且各自仅需调用一次。
+1：USDC 订单簿交易功能。
+仅当下单返回错误码 54109 时，才需要调用该功能；否则无需调用。
+错误码 51773 仅表示不支持使用该激活功能。能否交易 Crypto-USDC 产品，以是否能够成功下单为准。
+母账户与子账户之间共享开通状态，母账户或任一子账户仅需调用一次。
 返回结果
 { "code": "0", "msg": "", "data": [] }

```
