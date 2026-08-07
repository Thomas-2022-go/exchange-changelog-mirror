<!-- has_changes=true date=2026-08-07 -->
# Exchange API Changelog Diff

Generated: 2026-08-07 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132459 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 14 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 45 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (36254 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145596 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 4b762ea..404fa9b 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -49,4 +49,9 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 受影响的订单类型有：post_only、mmp_and_post_only、rpi（Retail Price Improvement）。
 其他订单类型如 limit（普通限价单）、market（市价单）、ioc、fok 订单推送行为保持不变。
+2026-08-06
+获取历史市场数据接口最大查询范围下调
+获取历史市场数据 接口的最大查询范围已由 20 下调至 10。
+| 参数名 | 类型 | 描述
+| begin | String | 最大范围：日度 10 天，月度 10 个月（此前为 20 天 / 20 个月）。
 2026-08-03
 联盟受邀用户接口新增 UID、加入时间筛选与滚动窗口成交量

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index d5e3b21..d16ba7f 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,33 @@
+2026-08-11​
+REST API​
+- Get Transaction Log [UPDATE]
+  - Add new response field displayType: display type for the transaction log entry, consistent with the UI display
+2026-08-07​
+REST API​
+Crypto Loan (Fixed-Term)
+- Get Available Inventory [NEW]
+  - New endpoint to query available lending pool inventory for fixed-term loan
+- Create Borrow Order [UPDATE]
+  - Add new request parameter strategyType: PARTIAL (allow partial fill, default); FULL (full fill only)
+- Get Borrow Order Info [UPDATE]
+  - Add new response field strategyType: PARTIAL (allow partial fill, default); FULL (full fill only)
+Crypto Loan (Flexible)
+- Get Available Inventory [NEW]
+  - New endpoint to query available lending pool inventory for flexible loan
+2026-08-06​
+REST API​
+- Move Position [UPDATE]
+  - TradFi perpetual contracts (including forex, stock, and commodities) are now supported
+- Switch Position Mode [UPDATE]
+  - USDT futures, USDC perpetual, Inverse perpetual, and Inverse futures now support both one-way and hedge-mode
+- Get Order History [UPDATE]
+  - smpGroup field type changed from integer to string
+- Get Open Orders [UPDATE]
+  - smpGroup field type changed from integer to string
+- Get Trade Behaviour Config [UPDATE]
+  - Add new response field smpType: user SMP (Self-Match Prevention) type configuration. 0: default; 1: cancel taker; 2: cancel maker; 3: cancel both
+Websocket API​
+- Order [UPDATE]
+  - smpGroup field type changed from integer to string
 2026-08-04​
 REST API​
@@ -4,4 +35,6 @@ REST API​
   - Kazakhstan (KAZ) derivatives: SMP is now mandatory for all derivative orders
   - Turkey (TUR), Kazakhstan (KAZ), Georgia (GEO) spot: smpType of None, invalid value, or missing value is automatically set to CancelMaker
+- Upgrade to Unified Account Pro [UPDATE]
+  - Upgrading from UTA PUBLIC to UTA PRO is prohibited daily between 07:55 and 08:05 UTC+0
 2026-07-30​
 REST API​

```
