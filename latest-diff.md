<!-- has_changes=true date=2026-05-23 -->
# Exchange API Changelog Diff

Generated: 2026-05-23 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (128989 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (86460 bytes)

- [CHANGED] **OKX V5** (`okx`): 31 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 47 diff lines

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (29217 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (116554 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (139416 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 8614c9d..715e0a9 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -1,3 +1,10 @@
 待发布内容
+WebSocket服务升级断线提示扩展至业务频道
+最后更新：2026 年 5 月 21 日
+WebSocket服务升级断线提示（错误码 64008）将扩展支持业务频道（/ws/v5/business）。
+在业务频道服务升级前60秒，将向用户推送如下消息，告知WebSocket连接即将断开。建议用户提前重新建立连接，以避免断线造成影响。
+该功能上线后将支持WebSocket公共频道(/ws/v5/public)、私有频道(/ws/v5/private)和业务频道(/ws/v5/business)。
+模拟盘上线日期：2026 年 6 月 4 日
+ 实盘上线日期：2026 年 6 月 11 日
 信号复制新增 API 接口
 最后更新：2026 年 5 月 14 日
@@ -36,4 +43,15 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
  1. books5 和 bbo-tbt 频道本身不包含 checksum 字段，不在本次变更范围内。
  2. WebSocket 连接已全面启用 TLS（wss://），具备防窃听、防篡改以及完整性校验的能力；结合 seqId/prevSeqId 的严格校验，可有效防止数据乱序、部分丢失或被恶意注入，实现与原 checksum 等效甚至更强的完整性保护。
+2026-05-22
+获取资金流水：新增 thirdPartyType 请求参数
+GET / 获取资金流水 新增可选请求参数 thirdPartyType，支持在母账户绑定多家第三方托管商时，按指定托管商筛选账单记录。
+不填时默认为 1（Copper），保持向后兼容。
+请求参数
+| 参数名 | 类型 | 是否必须 | 描述
+| thirdPartyType | String | 否 | 第三方托管类型。不填则默认为 1。
+1：Copper
+2：Komainu
+5：SCB
+6：CAAS
 2026-05-20
 新增专用 REST API 域名 openapi.okx.com

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index c88665b..2863f5f 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -1,2 +1,42 @@
+2026-05-26​
+Websocket API​
+- Order [UPDATE]
+  - Add new response fields rpiTakerAccess (whether the order has matched with an RPI order) and rpiMatchedQty (cumulative RPI matched quantity)
+2026-05-22​
+REST API​
+- Get Airdrop Products
+  - Add Byfi airdrop product endpoint
+- Get Airdrop Daily PnL Records
+  - Add Byfi airdrop daily pnl record endpoint
+PWM (Private Wealth Management) — New Endpoints
+- Get All Investment Plans [NEW]
+- Get Investment Plan Detail [NEW]
+- Get Pending Investment Plan Detail [NEW]
+- Claim Withdrawable Funds [NEW]
+- Get Asset Trend [NEW]
+- Get Fund Historical NAV [NEW]
+- Subscribe Investment Plan [NEW]
+- Invest More [NEW]
+- Redeem [NEW]
+- Get Investment Plan Orders [NEW]
+- Get Subscribable Product Info [NEW]
+- Create Customize Investment Plan [NEW]
+- Get All Funds [NEW]
+- Settle Fund Profit [NEW]
+- Create Fund [NEW]
+- Create Investment Plan [NEW]
+- Get Investment Plans [NEW]
+- Manage Investment Plan [NEW]
+- Get All Fund Orders [NEW]
+- Manage Order [NEW]
+- Create Fund Sub-Account [NEW]
+- Fund Transfer Between Sub-Accounts [NEW]
+- Get Fund Transfer Records [NEW]
+2026-05-21​
+REST API​
+- Get Order History [UPDATE]
+  - Add new response fields rpiTakerAccess (whether the order has matched with an RPI order) and rpiMatchedQty (cumulative RPI matched quantity)
+- Get Transaction Log [UPDATE]
+  - The api rate limit downgraded from 50 req/s to 25 req/s
 2026-05-14​
 REST API​

```
