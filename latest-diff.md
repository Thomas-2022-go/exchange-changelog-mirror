<!-- has_changes=true date=2026-11-20 -->
# Exchange API Changelog Diff

Generated: 2026-11-20 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (146418 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 15 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3488 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 13 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (45900 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (166885 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 7ccd7a0..0d47e85 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -80,4 +80,10 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | 参数名 | 类型 | 描述
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
+2026-11-19
+国际转账规则充值接口
+- 新增以下接口文档：
+  - GET / 获取因国际转账规则而锁定的充值记录
+  - POST / 解锁国际转账规则充值
+- 错误码 58385–58389 已加入资金账户错误码列表。
 2026-11-12
 股票类衍生品公司行动查询

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 83e0919..10194b6 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,8 @@
+2026-11-20​
+REST API​
+- Query Card List [NEW]
+  - Add a new endpoint to query Bybit card list.
+- Query Card Limit [NEW]
+  - Add a new endpoint to query Bybit card limit.
 2026-11-17​
 REST API​

```
