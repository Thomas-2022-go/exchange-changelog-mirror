<!-- has_changes=true date=2026-05-16 -->
# Exchange API Changelog Diff

Generated: 2026-05-16 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128997 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [CHANGED] **OKX V5** (`okx`): 44 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (78327 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (29316 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139416 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 04933ad..9afac12 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -66,4 +66,33 @@ daily
 | 错误码 | HTTP 状态码 | 错误提示
 | 54031 | 200 | 下单失败，{param0}的平台持仓量已达到平台持仓限额，无法开仓，只能平仓。开仓请稍后再试。
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
+2026-05-15
+交易账户
+移仓
+新增说明：TradeFi仓位不支持移仓。尝试对TradeFi仓位执行移仓操作将返回错误码 70004。
+- POST / 移仓
+| 错误码 | 信息
+| 70004 | Invalid instrument ID {instId}
 2026-05-14
 FD Broker
@@ -89,4 +118,5 @@ type 返回参数新增枚举值 4，表示 MSA 账户无法获得 Broker 返佣
 | traded_away | 仅适用于报价方。同一笔询价单可能对一个报价方显示为 filled，而对另一个报价方显示为 traded_away。示例：询价方创建询价单 → 做市商A报价 pxA，做市商B报价 pxB → pxA 优于 pxB → 询价方执行做市商A的报价 → 做市商A看到 filled，做市商B看到 traded_away。
 - 更新大宗交易频道的描述，明确数据仅推送给询价方和成交的报价方，状态为 traded_away 的报价方将不会收到本频道的推送。
+- 在公共大宗交易频道中新增 blockTdId 与 rfqId 对应关系说明：普通询价单为一一对应；组合询价单中一个 rfqId 可能对应多个 blockTdId。作为交易对手方的用户可通过私有大宗交易频道进行两者的关联查询。
 2026-05-08
 新增接口

```
