<!-- has_changes=true date=2026-10-28 -->
# Exchange API Changelog Diff

Generated: 2026-10-28 (Asia/Shanghai)

## Summary

- [CHANGED] **Binance Spot** (`binance-spot`): 25 diff lines

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 66 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 15 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42580 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (158964 bytes)



## Changes

### Binance Spot (`binance-spot`)
- Source: https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG
- Raw: https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md

```diff
diff --git a/changelogs/binance-spot.txt b/changelogs/binance-spot.txt
index 8b3dfe2..bd65c25 100644
--- a/changelogs/binance-spot.txt
+++ b/changelogs/binance-spot.txt
@@ -1,5 +1,12 @@
 # CHANGELOG for Binance's API
 
-**Last Updated: 2026-09-18**
+**Last Updated: 2026-10-27**
+
+### 2026-10-27
+
+- Added ExpiryReason(25056) in the [FIX API documentation](fix-api.md#executionreport-8)
+  which was previously undocumented but was announced in an [earlier update](#2026-03-09).
+
+---
 
 ### 2026-09-18
@@ -3239,5 +3246,5 @@ USER DATA STREAM
 
 - `Last quote asset transacted quantity` (as variable `Y`) added to execution reports. Represents
-  the `lastPrice` _ `lastQty` (`L` _ `l`).
+  the `lastPrice` \* `lastQty` (`L` \* `l`).
 
 ---

```

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 9224067..41d9ac7 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,5 +1,5 @@
 待发布内容
 WebSocket 8443 端口下线
-最近更新：2026年10月16日
+最近更新：2026年10月22日
 为配合网络基础设施升级，欧易将停止接受 8443 端口的 WebSocket 连接，Colo 连接同样适用：
 - 公网：2026年10月31日
@@ -18,15 +18,32 @@ WebSocket 8443 端口下线
   - 所有使用 8443 端口的 Colo WebSocket 连接。
 REST API 不受影响。
+新增错误码
+在上述日期之前，通过 8443 端口建立的连接在握手成功后会收到一条通知（event = notice），通知码如下。连接不会断开。
+| 错误码 | 错误消息
+| 64010 | WebSocket 8443 端口即将下线，请迁移至 443 端口。
 SBE 交易及私有数据
-最近更新：2026 年 9 月 30 日
+最近更新：2026 年 10 月 27 日
 欧易计划推出简单二进制编码（Simple Binary Encoding，SBE）交易服务，以及私有订单与成交数据服务。相关服务预计于 2026 年 11 月上旬上线模拟交易环境，并于 2026 年 12 月上旬上线生产环境。
 现有 REST API 和 JSON WebSocket API 不受影响。
 新增 SBE 服务
 | 服务 | 生产环境地址 | 模拟交易环境地址 | XML 模板
-| 交易 | wss://ws.okx.com/ws/v5/trade-sbe | wss://wspap.okx.com/ws/v5/trade-sbe | 下载
-| 私有数据 | wss://ws.okx.com/ws/v5/private-sbe | wss://wspap.okx.com/ws/v5/private-sbe | 下载
+| 交易 | wss://ws.okx.com/ws/v5/trade-sbe | wss://wspap.okx.com/ws/v5/trade-sbe | okx_sbe_trade_2_0.xml
+| 私有数据 | wss://ws.okx.com/ws/v5/private-sbe | wss://wspap.okx.com/ws/v5/private-sbe | okx_sbe_private_1_1.xml
 登录方式与现有的 SBE 行情数据服务一致。客户端需在 WebSocket HTTP Upgrade 请求头中提供 API key 和签名以完成鉴权。
 JSON 控制消息使用 opcode 为 1 的文本帧，SBE 消息使用 opcode 为 2 的二进制帧。
 相比 JSON 服务，SBE 消息的字段有所精简。完整的消息结构及字段定义请参考 XML 模板。
+XML 模板更新
+XML 模板已在服务上线前更新。请使用上方最新版本的模板生成编码器和解码器。
+交易：okx_sbe_trade_2_0.xml
+- Schema id 从 1 调整为 2，version 仍为 0，semanticVersion 调整为 2.0.0。消息结构发生变化，请使用此模板重新生成编码器和解码器。
+- 单笔及批量下单请求新增可选字段 rpiPxRound（RPI 价格取整）和 reduceOnly（只减仓）；单笔及批量改单请求新增可选字段 rpiPxRound。
+- 单笔及批量下单、改单请求中的 expTime 更名为 expTimeUs；所有下单、改单、撤单响应中的 ts 更名为 tsUs。这些字段的时间单位仍为微秒。
+- 单笔及批量下单响应移除 instIdCode，后续定长字段前移，字段 ID 随之调整。
+- 单笔下单、改单、撤单响应新增变长 UTF-8 错误信息 msg。
+- 批量下单、改单、撤单响应中的 data 分组更名为 results，结果按请求顺序排列，最多 20 条；新增 sMsgDetails 分组，通过从 0 开始的 resultIndex 将逐笔错误信息 sMsg 关联至 results，并新增批次级错误信息 msg。msg 和 sMsg 均使用 varString16，即以 uint16 为长度前缀的变长 UTF-8 字符串。
+私有数据：okx_sbe_private_1_1.xml
+- Schema id 仍为 1，version 从 0 调整为 1，semanticVersion 调整为 1.1.0。
+- orders 消息新增可选字段 reduceOnly（只减仓标识，booleanEnum：FALSE=0、TRUE=1）和 avgPxMantissa（成交均价尾数，共用 pxExponent）。两个字段均标记为 sinceVersion="1"。
+- orders 中的 fillTime、uTime、cTime 分别更名为 fillTimeUs、uTimeUs、cTimeUs；fills 中的 ts 更名为 tsUs。时间单位仍为微秒，更名字段的 ID 和类型保持不变。
 SBE 交易
 SBE 交易服务将支持以下操作：
@@ -62,4 +79,18 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | 参数名 | 类型 | 描述
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
+2026-10-27
+新增 RPI 最优买卖价深度频道 bbo-rpi-tbt
+新增公共 WebSocket 频道 bbo-rpi-tbt，推送由全部挂单 RPI 订单构成的 RPI 最优买价和卖价（1档），包含与有机最优买卖价或彼此交叉、因而不在 books-rpi 中展示的隐藏 RPI 订单。推送频率和数据格式与 bbo-tbt 一致：首次推1档快照数据，之后每10毫秒在1档快照数据有变化时推送一次。无需登录，无交易手续费等级限制。
+- WS / 深度频道
+请求参数
+| 参数 | 类型 | 是否必须 | 描述
+| > channel | String | 是 | 频道名
+bbo-rpi-tbt
+推送数据参数
+| 参数 | 类型 | 描述
+| > asks | Array of Arrays | 卖方深度
+对于 bbo-rpi-tbt，仅返回RPI订单，包含隐藏的RPI订单。卖方无RPI订单时返回 []。
+| > bids | Array of Arrays | 买方深度
+对于 bbo-rpi-tbt，仅返回RPI订单，包含隐藏的RPI订单。买方无RPI订单时返回 []。
 2026-09-30
 交易产品频道推送优化

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 5d52404..8b95625 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,10 @@
+2026-10-29​
+REST API​
+- Query Fixed-Rate Borrow Penalty Interest [NEW]
+  - Add GET /v5/spot-margin-trade/fixedborrow-interest-accrued to query fixed-rate borrow penalty interest records.
+- Cancel Fixed-Rate Borrow Order [NEW]
+  - Add POST /v5/spot-margin-trade/fixedborrow-order-cancel to request cancellation of an eligible fixed-rate borrow order.
+- Get Corporate Actions [NEW]
+  - Add GET /v5/market/corporate-action to query current corporate actions, including stock splits and dividends.
 2026-10-20​
 REST API​

```
