<!-- has_changes=true date=2026-05-28 -->
# Exchange API Changelog Diff

Generated: 2026-05-28 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128989 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [CHANGED] **OKX V5** (`okx`): 25 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (80145 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (29221 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (138977 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 715e0a9..f4ce97a 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,3 +1,20 @@
 待发布内容
+SPACEX 永续合约重命名
+最后更新：2026年5月27日
+为了优化用户交易体验，欧易将在 2026 年 6 月 1 日至 6 月 5 日（UTC）期间的某一天 将 SPACEXUSDT 永续合约更名为 SPCXUSDT 永续合约。
+- 更名时：
+  - 产品频道 会推送 instId: SPCX-USDT-SWAP, state: rebase 的更新数据，和 instId: SPCX-USDT-SWAP, state: live 的数据。
+- 更名后：
+  - 推送数据中的 instId instFamily, uly 会使用新的参数值。
+  - 平台将不再支持使用 instId: SPACEX-USDT-SWAP 以及 instFamily: SPACEX-USDT 订阅该合约的 WebSocket 频道，或是通过 OpenAPI 发送 HTTP 请求。请您在合约更名后使用 instId: SPCX-USDT-SWAP 或 instFamily: SPCX-USDT 进行相关交易。
+  - 先前使用 instId: SPACEX-USDT-SWAP 以及 instFamily: SPACEX-USDT 订阅的频道：
+    - 对于trades 和 以及 positions 频道的定时快照，旧的订阅仍然会推送数据，请在更名后使用新的参数值重新订阅。
+    - 对于深度频道，旧的订阅仍然会推送数据，需要先使用新的参数值取消订阅，再使用新的参数值重新订阅。
+    - 其他频道将不再推送任何数据，请在更名后使用新的参数值重新订阅。
+  - instIdCode 不发生变动。
+涉及到重命名的参数如下：
+| 值类型 | instId | uly | instFamily | ctValCcy
+| 改名前 | SPACEX-USDT-SWAP | SPACEX-USDT | SPACEX-USDT | SPACEX
+| 改名后 | SPCX-USDT-SWAP | SPCX-USDT | SPCX-USDT | SPCX
 WebSocket服务升级断线提示扩展至业务频道
 最后更新：2026 年 5 月 21 日

```
