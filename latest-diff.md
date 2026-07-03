<!-- has_changes=true date=2026-07-03 -->
# Exchange API Changelog Diff

Generated: 2026-07-03 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (131907 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (89162 bytes)

- [OK] OKX V5 (`okx`): no change (202930 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 11 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (34939 bytes)

- [CHANGED] **Gate.io Spot WebSocket v4** (`gate-spot-ws`): 25 diff lines

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145353 bytes)



## Changes

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index 0102e29..d814ec6 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,3 +1,6 @@
 2026-07-02​
+REST API​
+- Alpha Predication Market [NEW]
+  - Added new endpoints for Alpha prediction market
 Websocket API​
 - SBE Fast Order [UPDATE]

```

### Gate.io Spot WebSocket v4 (`gate-spot-ws`)
- Source: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/

```diff
diff --git a/changelogs/gate-spot-ws.txt b/changelogs/gate-spot-ws.txt
index 4ee02b6..d4ae56f 100644
--- a/changelogs/gate-spot-ws.txt
+++ b/changelogs/gate-spot-ws.txt
@@ -10,4 +10,5 @@ Gate 提供了一个简单而健壮的 Websocket API 来集成现货交易状态
 Websocket 链接地址：
 - 线上交易: wss://api.gateio.ws/ws/v4/
+- 线上交易 SBE: wss://api.gateio.ws/ws/v4/ws/spot/sbe
 - 模拟盘交易: wss://ws-testnet.gate.com/v4/ws/spot
 - 模拟盘 SBE: wss://ws-testnet.gate.com/v4/ws/spot/sbe
@@ -142,7 +143,9 @@ WebSocket 认证使用与 Gate APIv4 API 相同的签名计算方法，即: HexE
 # 对接SBE
 - 使用地址，在现有的地址后添加 /sbe：
+  - 线上交易: wss://api.gateio.ws/ws/v4/ws/spot/sbe
   - testnet: wss://ws-testnet.gate.com/v4/ws/spot/sbe
 - schema 地址：
   - testnet: gate_spot_ws_latest.xml (opens new window)
+  - 线上交易: gate_spot_ws_latest.xml (opens new window)
 - 如果需要指定 sbe_schema_id，则通过 query 的形式传入 sbe_schema_id 参数，例如：wss://ws-testnet.gate.com/v4/ws/spot/sbe?sbe_schema_id=1
   - 目前支持的 sbe_schema_id 为 0 和 1；sbe_schema_id 为 0 用于客户端测试 sbe schema 不兼容升级的逻辑
@@ -1534,3 +1537,3 @@ account: 指定查询账户。不指定默认现货，保证金和逐仓杠杆
 | »»label | String | 以字符串格式表示错误类型
 | »»message | String | 错误信息详情
-Last Updated: 6/10/2026, 4:02:40 AM
+Last Updated: 7/2/2026, 7:08:59 AM

```
