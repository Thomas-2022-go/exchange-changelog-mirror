<!-- has_changes=true date=2026-05-20 -->
# Exchange API Changelog Diff

Generated: 2026-05-20 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128997 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [CHANGED] **OKX V5** (`okx`): 119 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (78327 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (29217 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139416 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 01f2556..89eef13 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -8,7 +8,63 @@ ELP Maker 费率
 | 参数名 | 类型 | 描述
 | > elpMaker | String | ELP Maker 有效费率。若 ELP 不适用于该交易产品，则返回 ""。不适用于 EVENTS instType。
+信号复制新增 API 接口
+最后更新：2026 年 5 月 14 日
+OKX 将为信号复制（订单分享）功能新增 API 支持。API 用户现在可以通过传入订单 ID，以编程方式生成通用分享短链。短链将订单参数（合约、方向、杠杆、价格、止盈止损等）存储在服务端。接收方打开链接后，OKX App 下单面板将自动填入对应参数。
+此功能仅支持 USDT 保证金永续合约，使用前需确保账户已开启信号复制功能。
+生成信号复制短链
+- 生成信号复制短链
+- 新增接口 POST /api/v5/copytrade/create-sgl-link。
+- 请求体中传入 orderId 和 instId，订单必须属于请求账户。
+- 仅支持 USDT 保证金永续合约（instId 以 -USDT-SWAP 结尾），其他产品类型将返回错误。
+- 返回 shortLink——通用 OKX App 短链，接收方打开后下单面板将自动填入对应订单参数。
+- 限速：每用户每秒 10 次。
+请求示例
+POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192", "instId": "ADA-USDT-SWAP" }
+请求参数
+| 参数名 | 类型 | 是否必须 | 描述
+| orderId | String | 是 | 订单 ID，必须属于请求账户。
+| instId | String | 是 | 产品 ID，如 BTC-USDT-SWAP，仅支持 USDT 保证金永续合约。
+返回示例
+{ "code": "0", "data": [ { "shortLink": "https://www.okx.com/ul/1xJ7nV" } ], "msg": "" }
+返回参数
+| 参数名 | 类型 | 描述
+| shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
+深度频道 checksum 字段废弃
+最后更新：2026 年 5 月 19 日
+为了提升行情数据推送的效率和稳定性，以下深度频道将废弃全量快照和增量更新中的 checksum 字段。
+废弃后，checksum 字段仍会保留在全量快照和增量更新中，但其值将固定为 0，不应再用于数据完整性校验。请在废弃生效之前，改用 seqId/prevSeqId 校验数据的连续性和准确性。
+模拟盘废弃日期：2026 年 6 月 2 日
+ 实盘废弃日期：2026 年 6 月 23 日
+- 废弃全量快照和增量更新中的 checksum 字段（字段仍保留在推送中，但其值将固定为 0）。
+  - WS / 深度频道
+    - books
+    - books-l2-tbt
+    - books50-l2-tbt
+注意:
+ 1. books5 和 bbo-tbt 频道本身不包含 checksum 字段，不在本次变更范围内。
+ 2. WebSocket 连接已全面启用 TLS（wss://），具备防窃听、防篡改以及完整性校验的能力；结合 seqId/prevSeqId 的严格校验，可有效防止数据乱序、部分丢失或被恶意注入，实现与原 checksum 等效甚至更强的完整性保护。
+2026-05-19
+- 平台持仓限额优化 — 新增币量维度限额字段及错误码 54031。
+- 事件合约 — 取消公共数据接口鉴权要求。
+- 事件合约 — TickSize 精度调整及新增系列频率枚举值。
+事件合约 — 取消鉴权
+- 以下接口的权限由 读取 变更为 公共（无需鉴权）：
+  - GET / 获取系列
+  - GET / 获取事件
+  - GET / 获取市场
+平台持仓限额优化 — 新增币量维度限额字段及错误码 54031
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
 事件合约 — TickSize 精度调整
-最近更新：2026年5月14日
-事件合约的 TickSize 精度将从统一的 0.01 调整为分区间配置，在极端价格区间提供更精细的报价精度。本次变更预计于 2026年5月19日 上线。详情请参阅公告。
 交易产品基础信息接口中所有 EVENTS 产品的 tickSz 将从 "0.01" 变更为 "0.001"。该值现表示 tick band 中的最小精度（与 OPTION 行为一致）。请使用"获取期权价格梯度"接口传入 instType=EVENTS 查询各价格区间的精确 tickSz。
 如果您的应用依赖 EVENTS 产品的 tickSz 值进行价格校验，请在上线日期前完成相应调整。
@@ -44,48 +100,4 @@ fifteen_min
 hourly
 daily
-事件合约 — 取消鉴权
-最近更新：2026年5月14日
-事件合约公共数据接口将不再需要 API Key 鉴权。本次变更预计于 2026年5月19日 上线。
-- 以下接口的权限由 读取 变更为 公共（无需鉴权）：
-  - GET / 获取系列
-  - GET / 获取事件
-  - GET / 获取市场
-平台总持仓限制优化
-最近更新：2026年5月14日
-为增强风控管理能力，在现有 USD 维度限额基础上新增币量维度的平台持仓限额。本次变更预计于 2026年5月19日 上线。
-- 更新返回参数 maxPlatOILmt 描述；新增返回参数 maxPlatOICoinLmt，返回币量维度的平台持仓限额：
-  - GET / 获取交易产品基础信息
-返回参数
-| 参数名 | 类型 | 描述
-| maxPlatOILmt | String | 该产品的全平台最大持仓名义价值（USD）。当平台总持仓量（USD）达到或超过该值时，系统将拒绝所有用户对该产品的新开仓委托；否则订单通过校验。
-适用于 SWAP/FUTURES
-| maxPlatOICoinLmt | String | 该产品的全平台最大持仓名义价值（币量）。当平台总持仓量（币量）达到或超过该值时，系统将拒绝所有用户对该产品的新开仓委托；否则订单通过校验。
-适用于 SWAP/FUTURES
-- 更新错误码 54031 的错误提示文案
-错误码
-| 错误码 | HTTP 状态码 | 错误提示
-| 54031 | 200 | 下单失败，{param0}的平台持仓量已达到平台持仓限额，无法开仓，只能平仓。开仓请稍后再试。
-信号复制新增 API 接口
-最后更新：2026 年 5 月 14 日
-OKX 将为信号复制（订单分享）功能新增 API 支持。API 用户现在可以通过传入订单 ID，以编程方式生成通用分享短链。短链将订单参数（合约、方向、杠杆、价格、止盈止损等）存储在服务端。接收方打开链接后，OKX App 下单面板将自动填入对应参数。
-此功能仅支持 USDT 保证金永续合约，使用前需确保账户已开启信号复制功能。
-生成信号复制短链
-- 生成信号复制短链
-- 新增接口 POST /api/v5/copytrade/create-sgl-link。
-- 请求体中传入 orderId 和 instId，订单必须属于请求账户。
-- 仅支持 USDT 保证金永续合约（instId 以 -USDT-SWAP 结尾），其他产品类型将返回错误。
-- 返回 shortLink——通用 OKX App 短链，接收方打开后下单面板将自动填入对应订单参数。
-- 限速：每用户每秒 10 次。
-请求示例
-POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192", "instId": "ADA-USDT-SWAP" }
-请求参数
-| 参数名 | 类型 | 是否必须 | 描述
-| orderId | String | 是 | 订单 ID，必须属于请求账户。
-| instId | String | 是 | 产品 ID，如 BTC-USDT-SWAP，仅支持 USDT 保证金永续合约。
-返回示例
-{ "code": "0", "data": [ { "shortLink": "https://www.okx.com/ul/1xJ7nV" } ], "msg": "" }
-返回参数
-| 参数名 | 类型 | 描述
-| shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
 2026-05-15
 交易账户

```
