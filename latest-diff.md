<!-- has_changes=true date=2026-11-26 -->
# Exchange API Changelog Diff

Generated: 2026-11-26 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (146725 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 19 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3488 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 11 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (45900 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (166885 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 0d47e85..10f05d2 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -80,4 +80,14 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | 参数名 | 类型 | 描述
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
+2026-11-26
+GLP-C 做市商 API（Beta）
+在做市商申请板块的 /api/v5/users/glp-c/ 下新增六个 REST 接口。GLP-C（Global Liquidity Program - C）白名单账户可查询及注册产品，并查询分钟和小时报价考核结果。
+新增接口
+- GET / 获取 GLP-C 可参与产品
+- POST / 注册 GLP-C 产品
+- GET / 获取 GLP-C 注册统计
+- GET / 获取 GLP-C 分钟考核
+- GET / 获取 GLP-C 产品小时考核
+- GET / 获取 GLP-C 小时考核汇总
 2026-11-19
 国际转账规则充值接口

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 0d9eece..dfcd34d 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,6 @@
+2026-11-26​
+Websocket API​
+- Tickers [UPDATE]
+  - The Options push frequency has updated from 100ms to 300ms
 2026-11-23​
 REST API​

```
