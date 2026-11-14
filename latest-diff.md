<!-- has_changes=true date=2026-11-14 -->
# Exchange API Changelog Diff

Generated: 2026-11-14 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (146418 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 13 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3488 bytes)

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
index 06c7341..7ccd7a0 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -23,6 +23,6 @@ REST API 不受影响。
 | 64010 | WebSocket 8443 端口即将下线，请迁移至 443 端口。
 SBE 交易及私有数据
-最近更新：2026 年 11 月 12 日
-欧易计划推出简单二进制编码（Simple Binary Encoding，SBE）交易服务，以及私有订单与成交数据服务。相关服务预计于 2026 年 11 月 13 日上线模拟交易环境，并于 2026 年 12 月上旬上线生产环境。
+最近更新：2026 年 11 月 13 日
+欧易已于 2026 年 11 月 13 日在模拟交易环境上线简单二进制编码（Simple Binary Encoding，SBE）交易服务，以及私有订单与成交数据服务。相关服务预计于 2026 年 12 月上旬上线生产环境。
 现有 REST API 和 JSON WebSocket API 不受影响。
 新增 SBE 服务

```
