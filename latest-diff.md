<!-- has_changes=true date=2026-07-30 -->
# Exchange API Changelog Diff

Generated: 2026-07-30 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132459 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 10 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3590 bytes)

- [OK] Bybit V5 (`bybit`): no change (86947 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (36077 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145596 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 8b95282..16f855a 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -65,4 +65,5 @@ ELP 命名弃用截止日期：2026年10月31日
 - 新增 books-rpi，将非 RPI（有机）与 RPI 流动性合并为单一深度数据流——同时提供公共 WebSocket 频道（/ws/v5/public，400 档深度，初始全量推送 + 每 100 毫秒增量推送）与 REST 接口（GET /api/v5/market/books-rpi，服务端每 200 毫秒刷新一次）。不提供 checksum，WS 序列一致性依赖 seqId/prevSeqId。取代 books-elp（见上方迁移说明）。
   - WS / 深度频道
+  - GET / 获取 RPI 产品深度
 asks/bids 中的每个元素为 [price, totalQty, nonRpiQty, count]——totalQty 为该档位的总深度，nonRpiQty 为其中仅有机的部分，count 为该档位的汇总订单数量。
 REST 请求参数：instId（必填）、sz（每侧深度档数，最大 400，默认 1）。

```
