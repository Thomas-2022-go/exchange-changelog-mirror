<!-- has_changes=true date=2026-10-09 -->
# Exchange API Changelog Diff

Generated: 2026-10-09 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132590 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 11 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [OK] Bybit V5 (`bybit`): no change (97339 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42424 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (124213 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index bada7d4..972d0a4 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -4,5 +4,5 @@ WebSocket 8443 端口下线
 为配合网络基础设施升级，欧易将于 2026年10月31日 停止接受 8443 端口的 WebSocket 连接。所有受影响的域名现已支持 443 端口，在此之前两个端口均可正常连接。
 不兼容变更
-2026年10月31日 之后，连接 8443 端口将失败。请从 WebSocket 地址中删除 :8443。只需修改端口，域名和路径保持不变。wss:// 默认使用 443 端口，显式指定 :443 同样可以连接。本次调整适用于所有路径，包括 /ws/v5/public、/ws/v5/private 和 /ws/v5/business。
+2026年10月31日 之后，连接 8443 端口将失败。请从 WebSocket 地址中删除 :8443。只需修改端口，域名和路径保持不变。wss:// 默认使用 443 端口，显式指定 :443 同样可以连接。本次调整适用于所有路径，包括 /ws/v5/public、/ws/v5/private、/ws/v5/business，以及 Global 站的 /ws/v5/public-sbe。
 - 实盘
   - 变更前：wss://ws.okx.com:8443/ws/v5/public

```
