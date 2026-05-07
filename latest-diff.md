<!-- has_changes=true date=2026-05-07 -->
# Exchange API Changelog Diff

Generated: 2026-05-07 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 11 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (85776 bytes)

- [CHANGED] **OKX V5** (`okx`): 36 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 25 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (28255 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139392 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index 98f4f24..cb1559e 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -7,5 +7,5 @@
 **Notice: The following changes will be deployed on 2026-05-08, starting at 06:00 UTC and may take several hours to complete.**
 
-* Added `serverShutdown` event to [WebSocket API](web-socket-api.md) and [WebSocket Streams](web-socket-streams.md).
+* Added `serverShutdown` event to [WebSocket API](./web-socket-api.md#serverShutdown) and [WebSocket Streams](./web-socket-streams.md#serverShutdown).
   * `serverShutdown` event will be sent 10 minutes before disconnection.
 

```

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 13344a0..00165cc 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,3 +1,31 @@
 待发布内容
+2026-05-07
+新增接口
+- 以下为新增接口，仅适用于模拟交易环境：
+  - 调整模拟盘余额
+请求参数
+| 参数名 | 类型 | 是否必须 | 描述
+| type | String | 是 | 调整方向。
+increase：增加余额
+reduce：减少余额
+每次请求只能选择一个方向，不可同时包含增加和减少。
+| adjustments | Array | 是 | 币种调整列表，至少包含一项，不允许重复币种。
+| > ccy | String | 是 | 币种。支持：BTC ETH USDT OKB
+| > amt | String | 是 | 调整数量。必须为非负数，小数位数不超过该币种精度。
+单次增加上限：BTC：1，ETH：1，USDT：5000，OKB：100。
+减少操作无单次数量限制，仅受可用余额 ≥ 0 约束。
+返回参数
+| 参数名 | 类型 | 描述
+| remainCnt | String | 当日剩余增加余额次数。减少操作也会返回该字段，但减少操作不消耗次数。
+| totalCnt | String | 每日增加余额总次数（默认为 3）。
+| details | Array | 各币种操作详情。
+| > ccy | String | 币种。
+| > amt | String | 实际调整数量。
+| > bal | String | 操作后该币种的余额。
+错误码
+| 错误码 | HTTP 状态码 | 错误提示
+| 59691 | 200 | 每日增加余额次数已达上限{param0}，请于 UTC 0:00 后重试或重置模拟盘
+| 59692 | 200 | {param0} 余额不足，操作后余额不可小于零
+| 59693 | 200 | {param0} 可转余额不足，部分资金被挂单或持仓占用，请取消订单或平仓后重试
 2026-05-06
 已有接口改动

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 200fa6a..ce04575 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,6 @@
+2026-05-07​
+REST API​
+- Get Staked Position [UPDATE]
+  - Add new response fields availableAmount (redeemable amount) and freezeDetails (freeze detail list with amount and description)
 2026-05-06​
 REST API​
@@ -5,4 +9,13 @@ REST API​
 - Cancel Supply Order [UPDATE]
   - Add new optional request parameter refundedAccount to specify the account to receive the refund (0: Funding Account, 1: EasyEarn, default: 0)
+2026-04-30​
+REST API​
+- Get Instruments Info [UPDATE]
+  - Add new field symbolId (futures & options)
+- Get Account Instruments Info [UPDATE]
+  - Add new field symbolId (futures)
+- Get Coin Information [UPDATE]
+  - Add withdrawMax to indicate the max amount per transaction per chain that can be withdrawn, "-1" means no limit
+  - Deprecate field remainAmount
 2026-04-27​
 REST API​

```
