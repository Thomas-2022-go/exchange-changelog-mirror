<!-- has_changes=true date=2026-05-15 -->
# Exchange API Changelog Diff

Generated: 2026-05-15 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128997 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [CHANGED] **OKX V5** (`okx`): 87 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 17 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (29316 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139416 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 5b51be2..04933ad 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,3 +1,82 @@
 待发布内容
+ELP Maker 费率
+最近更新：2026年5月14日
+随着 ELP Maker 费率调整，在费率查询接口的返回参数 feeGroup 中新增 elpMaker 字段，用于展示 ELP Maker 有效费率。本次变更预计于 2026年5月20日 上线。详情请参阅公告。
+- 在 feeGroup 中新增返回参数 elpMaker：
+  - GET / 获取当前账户交易手续费费率
+返回参数
+| 参数名 | 类型 | 描述
+| > elpMaker | String | ELP Maker 有效费率。若 ELP 不适用于该交易产品，则返回 ""。不适用于 EVENTS instType。
+事件合约 — TickSize 精度调整
+最近更新：2026年5月14日
+事件合约的 TickSize 精度将从统一的 0.01 调整为分区间配置，在极端价格区间提供更精细的报价精度。本次变更预计于 2026年5月19日 上线。详情请参阅公告。
+交易产品基础信息接口中所有 EVENTS 产品的 tickSz 将从 "0.01" 变更为 "0.001"。该值现表示 tick band 中的最小精度（与 OPTION 行为一致）。请使用"获取期权价格梯度"接口传入 instType=EVENTS 查询各价格区间的精确 tickSz。
+如果您的应用依赖 EVENTS 产品的 tickSz 值进行价格校验，请在上线日期前完成相应调整。
+- 请求参数 instType 新增枚举值 EVENTS：
+  - GET / 获取期权价格梯度
+请求参数
+| 参数名 | 类型 | 是否必须 | 描述
+| instType | String | 是 | 产品类型。
+OPTION
+EVENTS
+返回参数
+| 参数名 | 类型 | 描述
+| instType | String | 产品类型
+| instFamily | String | 交易品种。仅适用于 OPTION
+| tickBand | Array of objects | 价格梯度。对于 EVENTS，返回适用于所有事件合约的统一价格梯度配置。
+| > minPx | String | 下单最低价格
+| > maxPx | String | 下单最高价格
+| > tickSz | String | 下单价格精度，如 0.001
+- 更新返回参数 tickSz 描述，新增 EVENTS 说明：
+  - 获取交易产品基础信息
+  - 获取交易产品基础信息
+  - 产品频道
+返回参数
+| 参数名 | 类型 | 描述
+| tickSz | String | 最小价格变动单位，如 0.0001。对于 OPTION/EVENTS，该值为 tick band 中的最小 tickSz。如需获取各价格区间的精确 tickSz，请使用"获取期权价格梯度"接口并传入对应的 instType 参数。
+- 返回参数 freq 新增枚举值 five_min 和 hourly：
+  - GET / 获取系列
+返回参数
+| 参数名 | 类型 | 描述
+| freq | String | 系列频率
+five_min
+fifteen_min
+hourly
+daily
+事件合约 — 取消鉴权
+最近更新：2026年5月14日
+事件合约公共数据接口将不再需要 API Key 鉴权。本次变更预计于 2026年5月19日 上线。
+- 以下接口的权限由 读取 变更为 公共（无需鉴权）：
+  - GET / 获取系列
+  - GET / 获取事件
+  - GET / 获取市场
+平台总持仓限制优化
+最近更新：2026年5月14日
+为增强风控管理能力，在现有 USD 维度限额基础上新增币量维度的平台持仓限额。本次变更预计于 2026年5月19日 上线。
+- 更新返回参数 maxPlatOILmt 描述；新增返回参数 maxPlatOICoinLmt，返回币量维度的平台持仓限额：
+  - GET / 获取交易产品基础信息
+返回参数
+| 参数名 | 类型 | 描述
+| maxPlatOILmt | String | 该产品的全平台最大持仓名义价值（USD）。当平台总持仓量（USD）达到或超过该值时，系统将拒绝所有用户对该产品的新开仓委托；否则订单通过校验。
+适用于 SWAP/FUTURES
+| maxPlatOICoinLmt | String | 该产品的全平台最大持仓名义价值（币量）。当平台总持仓量（币量）达到或超过该值时，系统将拒绝所有用户对该产品的新开仓委托；否则订单通过校验。
+适用于 SWAP/FUTURES
+- 更新错误码 54031 的错误提示文案
+错误码
+| 错误码 | HTTP 状态码 | 错误提示
+| 54031 | 200 | 下单失败，{param0}的平台持仓量已达到平台持仓限额，无法开仓，只能平仓。开仓请稍后再试。
+2026-05-14
+FD Broker
+获取返佣明细下载链接(FD)
+返佣明细 CSV 文件中新增两个字段，以支持经纪商更好地进行手续费和返佣归因。
+- GET / 获取返佣明细下载链接(FD)
+| 参数名 | 描述
+| uid | 账户 UID
+| clOrdId | 客户自定义订单ID。如果下单时未提供，则返回空字符串
+获取用户的 Broker 返佣信息
+type 返回参数新增枚举值 4，表示 MSA 账户无法获得 Broker 返佣。
+- GET / 获取用户的 Broker 返佣信息
+| 枚举值 | 说明
+| 4 | MSA 账户无法获得 Broker 返佣
 2026-05-11
 描述更新

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 1a08815..c88665b 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,3 +1,12 @@
 2026-05-14​
+REST API​
+- Get Affiliate User List [UPDATE]
+  - The size range update from [0, 1000] to [0, 100]
+- Get Affiliate Sub-Affiliate List [NEW]
+  - Add a new endpoint to query sub affiliates
+- Get API Key Information [UPDATE]
+  - Remove FiatBybitPay key from the response
+- Modify Master API Key [UPDATE]
+  - Remove FiatBybitPay key from the response
 Websocket API​
 - SBE Order Entry

```
