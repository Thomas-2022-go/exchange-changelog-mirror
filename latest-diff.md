<!-- has_changes=true date=2026-05-14 -->
# Exchange API Changelog Diff

Generated: 2026-05-14 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128997 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [CHANGED] **OKX V5** (`okx`): 39 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 11 diff lines

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 31 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139416 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 792cd64..5b51be2 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,3 +1,13 @@
 待发布内容
+2026-05-11
+描述更新
+- 更新了以下大宗交易接口中 state 参数的描述，以说明 filled 与 traded_away 的区别：
+  - 创建询价单
+  - 获取询价单
+  - 询价单频道
+| 值 | 描述
+| filled | 表示询价单已成功按照做市商的报价成交。
+| traded_away | 仅适用于报价方。同一笔询价单可能对一个报价方显示为 filled，而对另一个报价方显示为 traded_away。示例：询价方创建询价单 → 做市商A报价 pxA，做市商B报价 pxB → pxA 优于 pxB → 询价方执行做市商A的报价 → 做市商A看到 filled，做市商B看到 traded_away。
+- 更新大宗交易频道的描述，明确数据仅推送给询价方和成交的报价方，状态为 traded_away 的报价方将不会收到本频道的推送。
 2026-05-08
 新增接口
@@ -45,5 +55,6 @@ reduce：减少余额
 | 59693 | 200 | {param0} 可转余额不足，部分资金被挂单或持仓占用，请取消订单或平仓后重试
 2026-05-06
-欧易推出现货及现货杠杆市价单（Market Side）自定义滑点容忍度功能，支持 OpenAPI 及 WebSocket。
+- 欧易推出现货及现货杠杆市价单（Market Side）自定义滑点容忍度功能，支持 OpenAPI 及 WebSocket。
+- SWAP 合约新增产品状态枚举值 post_only，处于该状态时仅接受 post-only 限价单。
 已有接口改动
 - 新增可选请求参数 slippagePct，适用于币币及币币杠杆市价单中 tgtCcy 为到手币种的场景（买单为 base_ccy，卖单为 quote_ccy）：
@@ -63,4 +74,12 @@ reduce：减少余额
 | 54084 | 200 | 滑点设置须介于 0% 至 5% 之间（含边界）。
 | 54085 | 200 | 滑点百分比小数位不可超过 2 位。
+- 返回参数 state 新增枚举值 post_only。合约处于 post_only 状态时，仅接受 post-only 限价单（以及对已有 post-only 订单的改单和撤单）；市价单、IOC、FOK 和普通限价单将被拒绝。仅适用于 SWAP：
+  - 获取交易产品基础信息（私有）
+  - 获取交易产品基础信息（公共）
+  - 产品频道
+返回参数
+| 参数名 | 类型 | 描述
+| state | String | 产品状态
+post_only：仅接受 post-only 订单；已有 post-only 订单可改单和撤单。其他订单类型（市价单、IOC、FOK、普通限价单）将被拒绝。仅适用于 SWAP
 2026-04-28
 已有接口改动

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index ce04575..1a08815 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,6 @@
+2026-05-14​
+Websocket API​
+- SBE Order Entry
+  - XML template has been updated. 1. Update retMsg type from "varString8" to "varString16"; 2. Remove createAt from "BatchCreateRespV5"
 2026-05-07​
 REST API​

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index cb791b3..7036f1e 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,4 +1,26 @@
 WARNING
 The Pro API is currently in beta testing and should not be used in production trading environments.
+2026.05.15#
+[Modify] Pro Websocket Private Channel Order
+Added new enum value MATCH for the response field eT, supporting pushing MATCH events for UTA FUTURES trading
+[Modify] Get Pro REST Position List (UTA)
+Added response field:
+adlPercentage：ADL ranking percentage of the futures position. For example, a value of 0.12 represents 12%.
+[Modify] Pro Websocket Position Push
+Added response field:
+adl: ADL ranking percentage of the futures position. For example, a value of 0.12 represents 12%.
+[Modify] Pro REST Batch Cancel Orders by Symbol
+Added new enum value:MARGIN
+[Modify] Classic REST Get Trade History
+For liquidation orders, the tradeType will return the value: liquid
+[Add] Pro REST Get API Key Info
+[Add] Pro REST Add Sub-Account
+[Add] Pro REST Add Sub-Account API
+[Add] Pro REST Delete Sub-Account API
+[Add] Pro REST Get Deposit Address
+[Add] Pro REST Get Withdrawal Quotas
+[Add] Pro REST Withdraw
+[Add] Pro REST Cancel Withdrawal
+[Add] Pro REST Get KYC Region
 2026.05.08#
 [Margin Deprecate] Get ETF Info: Deprecated the /api/v3/etf/info endpoint.

```
