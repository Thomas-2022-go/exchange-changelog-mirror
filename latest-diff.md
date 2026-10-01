<!-- has_changes=true date=2026-10-01 -->
# Exchange API Changelog Diff

Generated: 2026-10-01 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132590 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 124 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [OK] Bybit V5 (`bybit`): no change (97001 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (42424 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (124213 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index dbde4d4..bada7d4 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,55 +1,37 @@
 待发布内容
-交易产品频道推送优化
-最后更新：2026 年 9 月 29 日
-OKX 计划于 2026 年 9 月 30 日优化交易产品频道的推送方式。
-在部分场景中，该频道将由全量推送改为增量推送，仅推送数据发生变化的产品。
-未来可能会有更多场景由全量推送改为增量推送，届时不再另行通知。
-客户端收到推送后，应根据 instId 更新本地产品缓存，不应假设每次推送均包含全量产品数据。
-欧易将进行 USD 现货交易对迁移
-最后更新：2026 年 9 月 28 日
-OKX 将合并 USD 与 USDC 现货深度。作为本次调整的一部分，受影响的 Crypto-USD 现货产品将下线，用户需迁移至对应的 Crypto-USDC 产品。本次调整属于不兼容变更。更多详情，请根据所在地区参阅对应公告： USD 现货交易对迁移或 USDⓢ 现货交易对迁移，请以所在地区可访问的公告为准。
-USDC 交易对开放及并行期
-自 2026 年 9 月 23 日下午 4:00（UTC+8） 起，OKX 将开放相关 Crypto-USDC 现货产品。自开放起至 2026 年 9 月 30 日下午 4:00（UTC+8） 相关 Crypto-USD 现货产品下线前，部分 Crypto-USD 产品及其对应的 Crypto-USDC 产品将同时开放交易。
-API 用户可在并行期内提前迁移至对应的 Crypto-USDC 产品 ID，适配 tradeQuoteCcy 的传参逻辑，并验证请求、返回及 WebSocket 订阅逻辑。
+WebSocket 8443 端口下线
+最近更新：2026年9月30日
+为配合网络基础设施升级，欧易将于 2026年10月31日 停止接受 8443 端口的 WebSocket 连接。所有受影响的域名现已支持 443 端口，在此之前两个端口均可正常连接。
 不兼容变更
-- 当前请求中使用 Crypto-USD 产品 ID 的用户，需在变更上线后改用对应的 Crypto-USDC 产品 ID。若下单返回错误码 54109，请调用 POST /api/v5/account/activate-feature 接口开通 USDC 交易功能；否则无需调用该接口。
-- 影响范围包括请求参数中包含 instId 或 instIdCode 的 REST API 和 WebSocket 频道，包括交易、订单查询、账户查询、策略交易、大宗交易、价差交易、行情请求及 WebSocket 订阅。
-- Crypto-USD 产品 ID 不会映射为 Crypto-USDC 产品 ID。变更上线后，继续使用已下线的 Crypto-USD instId 或 instIdCode 发起请求或订阅，可能会失败或返回空数据。
-- 返回参数将使用实际的 Crypto-USDC 产品 ID 或产品 ID Code。请在上线前更新请求构造、返回解析、订阅管理、产品缓存，以及所有依赖 instId 或 instIdCode 的业务逻辑。
-重要：迁移下单时需正确传入 tradeQuoteCcy
-tradeQuoteCcy 的默认值为 instId 中的计价币种。因此，如果仅将 instId 从 Crypto-USD 改为 Crypto-USDC，默认交易计价币种也会从 USD 变为 USDC。
-如果您当前交易 Crypto-USD 产品时未传入 tradeQuoteCcy，迁移至对应的 Crypto-USDC 产品后仍希望使用 USD 交易，则必须显式传入 tradeQuoteCcy=USD。
-| 场景 | 变更前 | 变更后
-| 继续使用 USD 交易 | "instId": "Crypto-USD"
-未传 tradeQuoteCcy | "instId": "Crypto-USDC"
-"tradeQuoteCcy": "USD"
-| 使用 USDC 交易 | "instId": "Crypto-USD"
-"tradeQuoteCcy": "USDC" | "instId": "Crypto-USDC"
-"tradeQuoteCcy": "USDC"；如果希望使用默认值 USDC，也可不传 tradeQuoteCcy
-下单前，请通过 获取交易产品基础信息（私有） 接口获取 tradeQuoteCcyList。传入的 tradeQuoteCcy 必须是当前产品及账户对应的 tradeQuoteCcyList 枚举值。
-该迁移规则也适用于其他使用相关请求参数计算可交易数量或提交现货订单的接口，包括 获取最大可用余额/保证金、获取最大可下单数量 及 获取交易产品最大可借。
-新增接口：开通 USDC 交易功能
-若下单返回错误码 54109，请调用以下接口为账户开通 USDC 交易功能；否则无需调用该接口。
-限速：5 次/2 秒
-限速规则：User ID
-HTTP 请求
-POST /api/v5/account/activate-feature
-请求示例
-POST /api/v5/account/activate-feature body { "feature": "1" }
-请求参数
-| 参数名 | 类型 | 是否必须 | 描述
-| feature | String | 是 | 要开通的具体功能
-1：USDC 订单簿交易功能。
-仅当下单返回错误码 54109 时，才需要调用该功能；否则无需调用。
-错误码 51773 仅表示不支持使用该激活功能。能否交易 Crypto-USDC 产品，以是否能够成功下单为准。
-母账户与子账户之间共享开通状态，母账户或任一子账户仅需调用一次。
-返回结果
-{ "code": "0", "msg": "", "data": [] }
-返回参数
-无
-新增错误码
-若账户尚未开通 USDC 交易功能，下单时将返回以下错误：
-| 错误码 | HTTP 状态码 | 错误提示
-| 54109 | 200 | 您尚未开通该币对交易。请登录 欧易 App 或官网，进入该币对交易页面并点击"交易"完成开通，或调用指定 API 接口开通后重试。
+2026年10月31日 之后，连接 8443 端口将失败。请从 WebSocket 地址中删除 :8443。只需修改端口，域名和路径保持不变。wss:// 默认使用 443 端口，显式指定 :443 同样可以连接。本次调整适用于所有路径，包括 /ws/v5/public、/ws/v5/private 和 /ws/v5/business。
+- 实盘
+  - 变更前：wss://ws.okx.com:8443/ws/v5/public
+  - 变更后：wss://ws.okx.com/ws/v5/public
+- 模拟盘
+  - 变更前：wss://wspap.okx.com:8443/ws/v5/public
+  - 变更后：wss://wspap.okx.com/ws/v5/public
+REST API 和 Colo 连接不受影响。
+SBE 交易及私有数据
+最近更新：2026 年 9 月 30 日
+欧易计划推出简单二进制编码（Simple Binary Encoding，SBE）交易服务，以及私有订单与成交数据服务。相关服务预计于 2026 年 11 月上旬上线模拟交易环境，并于 2026 年 12 月上旬上线生产环境。
+现有 REST API 和 JSON WebSocket API 不受影响。
+新增 SBE 服务
+| 服务 | 生产环境地址 | 模拟交易环境地址 | XML 模板
+| 交易 | wss://ws.okx.com/ws/v5/trade-sbe | wss://wspap.okx.com/ws/v5/trade-sbe | 下载
+| 私有数据 | wss://ws.okx.com/ws/v5/private-sbe | wss://wspap.okx.com/ws/v5/private-sbe | 下载
+登录方式与现有的 SBE 行情数据服务一致。客户端需在 WebSocket HTTP Upgrade 请求头中提供 API key 和签名以完成鉴权。
+JSON 控制消息使用 opcode 为 1 的文本帧，SBE 消息使用 opcode 为 2 的二进制帧。
+相比 JSON 服务，SBE 消息的字段有所精简。完整的消息结构及字段定义请参考 XML 模板。
+SBE 交易
+SBE 交易服务将支持以下操作：
+- 下单及批量下单
+- 改单及批量改单
+- 撤单及批量撤单
+批量操作最多支持 20 笔订单。SBE 交易支持 CASH 和 CROSS 交易模式。如需使用其他交易模式，请继续使用 JSON WebSocket 交易 API。
+SBE 私有数据
+SBE 私有数据服务将支持以下频道：
+- orders：创建订单或订单状态发生变化时推送更新。
+- fills：推送订单簿成交事件，仅面向 VIP4 及以上用户开放。
+两个频道首次订阅时均不推送快照。订阅请求及响应仍采用 JSON 格式，频道数据采用 SBE 编码。orders 频道支持按 instType 过滤，instIdCode 非必填；fills 频道的 instIdCode 也非必填。
 信号复制新增 API 接口
 最后更新：2026 年 5 月 14 日
@@ -74,4 +56,30 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | 参数名 | 类型 | 描述
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
+2026-09-30
+交易产品频道推送优化
+欧易已优化交易产品频道的推送方式。
+在部分场景中，该频道现已由全量推送改为增量推送，仅推送数据发生变化的产品。
+未来可能会有更多场景由全量推送改为增量推送，届时不再另行通知。客户端收到推送后，应根据 instId 更新本地产品缓存，不应假设每次推送均包含全量产品数据。
+USD 现货交易对迁移
+欧易已合并 USD 与 USDC 现货深度。受影响的 Crypto-USD 现货产品已下线，API 用户须使用对应的 Crypto-USDC 产品。
+迁移要求
+- 原先使用 Crypto-USD 产品 ID 的请求，现须改用对应的 Crypto-USDC 产品 ID。
+- 影响范围包括请求参数中包含 instId 或 instIdCode 的 REST API 和 WebSocket 频道。
+- Crypto-USD 产品 ID 不会映射为 Crypto-USDC 产品 ID。继续使用已下线的 Crypto-USD instId 或 instIdCode 发起请求或订阅，可能会失败或返回空数据。
+- 返回参数使用实际的 Crypto-USDC 产品 ID 或产品 ID Code。请更新请求构造、返回解析、订阅管理、产品缓存，以及所有依赖 instId 或 instIdCode 的业务逻辑。
+交易计价币种
+tradeQuoteCcy 的默认值为 instId 中的计价币种。因此，如果仅将 instId 从 Crypto-USD 改为 Crypto-USDC，默认交易计价币种也会从 USD 变为 USDC。
+迁移至对应的 Crypto-USDC 产品后，如需继续使用 USD 交易，请显式传入 tradeQuoteCcy=USD。
+| 场景 | 迁移前 | 迁移后
+| 继续使用 USD 交易 | "instId": "Crypto-USD"
+未传 tradeQuoteCcy | "instId": "Crypto-USDC"
+"tradeQuoteCcy": "USD"
+| 使用 USDC 交易 | "instId": "Crypto-USD"
+"tradeQuoteCcy": "USDC" | "instId": "Crypto-USDC"
+"tradeQuoteCcy": "USDC" 或不传 tradeQuoteCcy
+下单前，请通过 GET / 获取交易产品基础信息 获取支持的 tradeQuoteCcyList。
+开通 USDC 交易功能
+- 新增 POST / 开通功能。仅当下单返回错误码 54109 时才需调用该接口；否则无需调用。
+- 新增错误码 54109，详情请参阅 REST API 错误码。
 2026-09-15
 RPI 挂单最小名义金额门槛

```
