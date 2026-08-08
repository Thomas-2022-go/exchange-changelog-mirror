<!-- has_changes=true date=2026-08-08 -->
# Exchange API Changelog Diff

Generated: 2026-08-08 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132459 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 30 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 16 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (36254 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145596 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 404fa9b..bdfe0aa 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -49,4 +49,25 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 受影响的订单类型有：post_only、mmp_and_post_only、rpi（Retail Price Improvement）。
 其他订单类型如 limit（普通限价单）、market（市价单）、ioc、fok 订单推送行为保持不变。
+RPI 挂单价格间距与可见性规则更新
+最近更新：2026年8月7日
+RPI 挂单价格间距规则即将调整。间距规则的交叉校验与价格档位校验仅参考首个可见的对手方 RPI，不参考已隐藏的 RPI。RPI 的可见性同时决定 books-rpi 订单簿上展示的可成交 RPI 深度。本次不涉及任何接口、参数、枚举值或错误码的变更。本次变更预计于 2026年8月11日 上线。
+价格间距规则
+- 交叉校验与价格档位校验仅参考首个可见的对手方 RPI，不参考已隐藏的 RPI
+- 无可见对手方 RPI 时：交叉校验参考对手方有机最优买/卖价，价格档位校验通过
+- bps 校验参考对手方有机最优买/卖价，不参考 RPI（不变）
+- rpiPxRound 取整到首个可见对手方 RPI 之外的下一档，不参考已隐藏的 RPI
+可见性
+- 与对手方有机最优买/卖价交叉的 RPI 予以隐藏
+- 在有机价差内相互交叉的买方 RPI 与卖方 RPI 双方均予以隐藏
+改单
+- 以改单命令到达撮合引擎时的订单簿快照进行校验
+- 被改订单视为仍在订单簿中
+影响 RPI 挂单的下单与改单（ordType: rpi），以及 books-rpi 订单簿：
+- POST / 下单
+- POST / 修改订单
+- WS / 下单
+- WS / 改单
+- WS / 深度频道
+- GET / 获取 RPI 产品深度
 2026-08-06
 获取历史市场数据接口最大查询范围下调

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index d16ba7f..47d0e25 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -3,4 +3,11 @@ REST API​
 - Get Transaction Log [UPDATE]
   - Add new response field displayType: display type for the transaction log entry, consistent with the UI display
+2026-08-09​
+REST API​
+- Integration Guidance
+  - Add Rest API integration method for Argentina users
+Websocket API​
+- Connect
+  - Add websocket integration method for Argentina users
 2026-08-07​
 REST API​

```
