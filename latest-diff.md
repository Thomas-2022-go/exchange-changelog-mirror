<!-- has_changes=true date=2026-07-15 -->
# Exchange API Changelog Diff

Generated: 2026-07-15 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (131907 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 12 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (84936 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (34939 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120249 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index aa563e0..96ca45d 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -125,4 +125,7 @@ RPI 挂单费率字段：rpiMaker（替代 elpMaker）
 - GET /api/v5/market/trades 返回字段 source 取值 1 的说明由"流动性增强计划订单"更新为 RPI 订单（原 ELP 订单）。返回的取值 1 本身不变，仅更新说明文字。
   - GET / 获取交易产品公共成交数据
+2026-07-14
+Stable Rewards 询价、下单及历史记录接口下线
+POST /api/v5/finance/stable-rewards/quote、POST /api/v5/finance/stable-rewards/trade 及 GET /api/v5/finance/stable-rewards/subscribe-redeem-history 接口已停用并从 API 中移除。如需交易 USDG 等稳定币，请使用标准订单簿交易 API。
 2026-07-07
 事件合约 HIT 和 BETWEEN 结算方式

```
