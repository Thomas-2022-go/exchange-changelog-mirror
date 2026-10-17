<!-- has_changes=true date=2026-10-17 -->
# Exchange API Changelog Diff

Generated: 2026-10-17 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (137124 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 36 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [OK] Bybit V5 (`bybit`): no change (97947 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42424 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (158964 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 3774e83..9224067 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,15 +1,21 @@
 待发布内容
 WebSocket 8443 端口下线
-最近更新：2026年9月30日
-为配合网络基础设施升级，欧易将于 2026年10月31日 停止接受 8443 端口的 WebSocket 连接。所有受影响的域名现已支持 443 端口，在此之前两个端口均可正常连接。
+最近更新：2026年10月16日
+为配合网络基础设施升级，欧易将停止接受 8443 端口的 WebSocket 连接，Colo 连接同样适用：
+- 公网：2026年10月31日
+- Colo：2026年11月16日
+所有受影响的域名（包括 Colo）现已支持 443 端口，在上述日期之前两个端口均可正常连接。
 不兼容变更
-2026年10月31日 之后，连接 8443 端口将失败。请从 WebSocket 地址中删除 :8443。只需修改端口，域名和路径保持不变。wss:// 默认使用 443 端口，显式指定 :443 同样可以连接。本次调整适用于所有路径，包括 /ws/v5/public、/ws/v5/private、/ws/v5/business，以及 Global 站的 /ws/v5/public-sbe。
-- 实盘
-  - 变更前：wss://ws.okx.com:8443/ws/v5/public
-  - 变更后：wss://ws.okx.com/ws/v5/public
-- 模拟盘
-  - 变更前：wss://wspap.okx.com:8443/ws/v5/public
-  - 变更后：wss://wspap.okx.com/ws/v5/public
-REST API 和 Colo 连接不受影响。
+上述日期之后，连接 8443 端口将失败。请从 WebSocket 地址中删除 :8443。只需修改端口，域名和路径保持不变。wss:// 默认使用 443 端口，显式指定 :443 同样可以连接。本次调整适用于所有路径，包括 /ws/v5/public、/ws/v5/private、/ws/v5/business，以及 Global 站的 /ws/v5/public-sbe。
+- 公网，自 2026年10月31日 起
+  - 实盘
+    - 变更前：wss://ws.okx.com:8443/ws/v5/public
+    - 变更后：wss://ws.okx.com/ws/v5/public
+  - 模拟盘
+    - 变更前：wss://wspap.okx.com:8443/ws/v5/public
+    - 变更后：wss://wspap.okx.com/ws/v5/public
+- Colo，自 2026年11月16日 起
+  - 所有使用 8443 端口的 Colo WebSocket 连接。
+REST API 不受影响。
 SBE 交易及私有数据
 最近更新：2026 年 9 月 30 日

```
