<!-- has_changes=true date=2026-05-17 -->
# Exchange API Changelog Diff

Generated: 2026-05-17 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128997 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [CHANGED] **OKX V5** (`okx`): 31 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (78327 bytes)

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 15 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139416 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 9afac12..01f2556 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -95,4 +95,26 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | 错误码 | 信息
 | 70004 | Invalid instrument ID {instId}
+跟单
+带单交易员唯一标识码（uniqueCode）
+更新了所有跟单接口中 uniqueCode 参数的描述。带单交易员唯一标识码现支持16位和18位两种格式：
+- POST / 首次跟单设置
+- POST / 修改跟单设置
+- POST / 停止跟单
+- GET / 获取跟单设置
+- GET / 批量获取杠杆倍数
+- GET / 获取跟单人信息
+- GET / 获取跟单人信息（私有）
+- GET / 获取交易员带单情况
+- GET / 获取交易员带单情况（私有）
+- GET / 获取交易员收益日表现
+- GET / 获取交易员收益日表现（私有）
+- GET / 获取交易员收益周表现
+- GET / 获取交易员收益周表现（私有）
+- GET / 获取交易员币种偏好
+- GET / 获取交易员币种偏好（私有）
+- GET / 获取交易员当前带单
+- GET / 获取交易员当前带单（私有）
+- GET / 获取交易员历史带单
+- GET / 获取交易员历史带单（私有）
 2026-05-14
 FD Broker

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index 7036f1e..5eb0126 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -4,8 +4,8 @@ The Pro API is currently in beta testing and should not be used in production tr
 [Modify] Pro Websocket Private Channel Order
 Added new enum value MATCH for the response field eT, supporting pushing MATCH events for UTA FUTURES trading
-[Modify] Get Pro REST Position List (UTA)
+[Modify] Pro REST Get Position List (UTA)
 Added response field:
 adlPercentage：ADL ranking percentage of the futures position. For example, a value of 0.12 represents 12%.
-[Modify] Pro Websocket Position Push
+[Modify] Pro Websocket Position
 Added response field:
 adl: ADL ranking percentage of the futures position. For example, a value of 0.12 represents 12%.

```
