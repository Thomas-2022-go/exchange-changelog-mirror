<!-- has_changes=true date=2026-05-01 -->
# Exchange API Changelog Diff

Generated: 2026-05-01 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (126608 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (85776 bytes)

- [CHANGED] **OKX V5** (`okx`): 58 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 13 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (28255 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139392 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 5344b25..48e59b6 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,8 +1,44 @@
 待发布内容
+Post-only 合约状态
+最近更新: 2026年4月29日
+产品状态新增 post_only 枚举值。合约处于 post_only 状态时，仅接受 post-only 限价单（以及对已有 post-only 订单的改单和撤单）；市价单、IOC、FOK 和普通限价单将被拒绝。预计 2026 年 5 月上线。
+产品接口/频道
+- 返回参数 state 新增枚举值 post_only
+  - 获取交易产品基础信息（私有）
+  - 获取交易产品基础信息（公共）
+  - 产品频道
+| 参数名 | 类型 | 描述
+| state | String | 产品状态
+live：交易中
+suspend：暂停中
+rebase：合约在变基中，不可交易，仅适用于SWAP
+post_only：仅接受 post-only 订单；已有 post-only 订单可改单和撤单。其他订单类型（市价单、IOC、FOK、普通限价单）将被拒绝。仅适用于 SWAP
+preopen：预上线，交割和期权合约轮转生成到开始交易；部分交易产品上线前
+test：测试中（测试产品，不可交易）
+2026-04-28
+已有接口改动
+- 返回参数 type 新增枚举值 risk_unit_type：
+  - 设置Delta中性预检查
+返回参数
+| 参数名 | 类型 | 描述
+| type | String | 不匹配信息类型
+risk_unit_type：该账户在Delta中性风险单元内，无法切换至通用模式。请在切换策略前将其从风险单元中移除。
+错误码
+| 错误码 | HTTP 状态码 | 错误提示
+| 59529 | 200 | 策略模式设置失败。该账户属于 Delta 中性策略风险单元，设置策略模式前，请先将该账户移出风险单元
+2026-04-24
+Stable Rewards
+OKX 新增 Stable Rewards 模块，自动为持有合格稳定币的用户每日发放奖励。
+- 新增以下接口：
+  - GET / 获取产品信息
+  - POST / 询价
+  - POST / 下单
+  - GET / 获取余额
+  - GET / 获取历史收益率
+  - GET / 获取订阅赎回历史
+2026-04-22
 大宗商品产品 instCategory 重新分类
-最近更新: 2026年4月13日
-部分产品的 instCategory 值将被重新分类。该变更预计于 2026年4月21日 上线实盘。
 不兼容变更
-以下产品当前 instCategory 返回值为 1（加密货币）。本次变更上线后，其 instCategory 将变更为 4（大宗商品）：
+以下产品的 instCategory 返回值已由 1（加密货币）变更为 4（大宗商品）：
 - XAU-USDT-SWAP
 - XAG-USDT-SWAP
@@ -17,5 +53,4 @@
 - 获取交易产品基础信息（公共）
 - 产品频道
-如果您的应用逻辑依赖这些产品的 instCategory 值，请在上线日期前完成相应调整。
 2026-04-15
 OKX 上线事件合约，支持公共数据、行情数据及交易账户相关接口。

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 2d8d8bb..200fa6a 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,8 @@
+2026-05-06​
+REST API​
+- Create Supply Order [UPDATE]
+  - Add new optional request parameter availableSource to specify the source account for supply (0: Funding Account, 1: Earn Flexible Account, 2: ALL, default: 0)
+- Cancel Supply Order [UPDATE]
+  - Add new optional request parameter refundedAccount to specify the account to receive the refund (0: Funding Account, 1: EasyEarn, default: 0)
 2026-04-27​
 REST API​

```
