<!-- has_changes=true date=2026-05-09 -->
# Exchange API Changelog Diff

Generated: 2026-05-09 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128717 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (85776 bytes)

- [CHANGED] **OKX V5** (`okx`): 55 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (77799 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (28342 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139392 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 00165cc..792cd64 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,3 +1,19 @@
 待发布内容
+2026-05-08
+新增接口
+- 节点（Affiliate）下新增以下接口：
+  - 获取节点业绩概览
+  - 获取直客列表
+  - 获取邀请链接列表
+  - 获取联合邀请人链接列表
+  - 获取二级节点列表
+新增返回参数
+- 在以下接口中新增返回参数 wdAmt、totalVol：
+  - 获取被邀请人返佣信息
+| 参数名 | 类型 | 描述
+| wdAmt | String | 累计提现金额，单位为 USDT。如果没有提现，返回 0。
+| totalVol | String | 生命周期累计交易量，单位为 USDT。如果没有交易，返回 0。
+限速变更
+- 获取被邀请人返佣信息 的限速由 20次/2s 调整为 3次/s。
 2026-05-07
 新增接口
@@ -29,13 +45,22 @@ reduce：减少余额
 | 59693 | 200 | {param0} 可转余额不足，部分资金被挂单或持仓占用，请取消订单或平仓后重试
 2026-05-06
+欧易推出现货及现货杠杆市价单（Market Side）自定义滑点容忍度功能，支持 OpenAPI 及 WebSocket。
 已有接口改动
-- 返回参数 state 新增枚举值 post_only。合约处于 post_only 状态时，仅接受 post-only 限价单（以及对已有 post-only 订单的改单和撤单）；市价单、IOC、FOK 和普通限价单将被拒绝。仅适用于 SWAP：
-  - 获取交易产品基础信息（私有）
-  - 获取交易产品基础信息（公共）
-  - 产品频道
-返回参数
-| 参数名 | 类型 | 描述
-| state | String | 产品状态
-post_only：仅接受 post-only 订单；已有 post-only 订单可改单和撤单。其他订单类型（市价单、IOC、FOK、普通限价单）将被拒绝。仅适用于 SWAP
+- 新增可选请求参数 slippagePct，适用于币币及币币杠杆市价单中 tgtCcy 为到手币种的场景（买单为 base_ccy，卖单为 quote_ccy）：
+  - POST / 下单
+  - POST / 批量下单
+  - WS / 下单
+  - WS / 批量下单
+请求参数
+| 参数名 | 类型 | 是否必须 | 描述
+| slippagePct | String | 否 | 币币、币币杠杆市价单（tgtCcy 为到手币种：买单为 base_ccy，卖单为 quote_ccy）的最大可接受滑点。
+取值范围：0 至 0.05（即 0% 至 5%，含边界），以百分比形式表示时最多保留 2 位小数，例如 0.01（1%）和 0.0123（1.23%）合法；0.01234（1.234%）将被拒绝。
+不填或为空时，默认为 0.00%。
+不支持改单修改滑点，如需调整请撤单重新提交。
+仅适用于币币和币币杠杆的市价单。
+错误码
+| 错误码 | HTTP 状态码 | 错误提示
+| 54084 | 200 | 滑点设置须介于 0% 至 5% 之间（含边界）。
+| 54085 | 200 | 滑点百分比小数位不可超过 2 位。
 2026-04-28
 已有接口改动

```
