<!-- has_changes=true date=2026-11-11 -->
# Exchange API Changelog Diff

Generated: 2026-11-11 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (137687 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 38 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3246 bytes)

- [OK] Bybit V5 (`bybit`): no change (100865 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (44528 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (130500 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (164576 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 8b98b83..1b073ed 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -23,6 +23,6 @@ REST API 不受影响。
 | 64010 | WebSocket 8443 端口即将下线，请迁移至 443 端口。
 SBE 交易及私有数据
-最近更新：2026 年 10 月 28 日
-欧易计划推出简单二进制编码（Simple Binary Encoding，SBE）交易服务，以及私有订单与成交数据服务。相关服务预计于 2026 年 11 月 11 日上线模拟交易环境，并于 2026 年 12 月上旬上线生产环境。
+最近更新：2026 年 11 月 10 日
+欧易计划推出简单二进制编码（Simple Binary Encoding，SBE）交易服务，以及私有订单与成交数据服务。相关服务预计于 2026 年 11 月 12 日上线模拟交易环境，并于 2026 年 12 月上旬上线生产环境。
 现有 REST API 和 JSON WebSocket API 不受影响。
 新增 SBE 服务
@@ -30,4 +30,5 @@ SBE 交易及私有数据
 | 交易 | wss://ws.okx.com/ws/v5/trade-sbe | wss://wspap.okx.com/ws/v5/trade-sbe | okx_sbe_trade_2_0.xml
 | 私有数据 | wss://ws.okx.com/ws/v5/private-sbe | wss://wspap.okx.com/ws/v5/private-sbe | okx_sbe_private_1_1.xml
+/ws/v5/trade-sbe 和 /ws/v5/private-sbe 两个 WebSocket 服务共享连接频率限制：每个 IP 每 5 分钟最多发起 500 次连接请求。
 登录方式与现有的 SBE 行情数据服务一致。客户端需在 WebSocket HTTP Upgrade 请求头中提供 API key 和签名以完成鉴权。
 JSON 控制消息使用 opcode 为 1 的文本帧，SBE 消息使用 opcode 为 2 的二进制帧。
@@ -79,4 +80,18 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | 参数名 | 类型 | 描述
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
+2026-11-05
+ELP 命名停止支持，请使用 RPI 命名
+2026-07-28 更新日志中弃用的 ELP 命名，已于 2026年10月31日后停止支持。请使用下表中的 RPI 命名。
+| 已停用的 ELP 命名 | RPI 命名
+| books-elp（WS 频道） | books-rpi
+| ordType：elp | ordType：rpi
+| isElpTakerAccess（请求参数） | rpiTakerAccess
+| elp（返回参数） | rpi
+| elpMaker（返回参数） | rpiMaker
+- WS / 深度频道
+- POST / 下单
+- WS / 下单
+- GET / 获取交易产品基础信息
+- GET / 获取当前账户交易手续费费率
 2026-10-27
 新增 RPI 最优买卖价深度频道 bbo-rpi-tbt

```
