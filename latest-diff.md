<!-- has_changes=true date=2026-08-27 -->
# Exchange API Changelog Diff

Generated: 2026-08-27 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132451 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 14 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [CHANGED] **Bybit V5** (`bybit`): 38 diff lines

- [CHANGED] **KuCoin (Spot + Futures)** (`kucoin`): 45 diff lines

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (151847 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 3068ffd..551adc3 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -22,4 +22,9 @@ POST /api/v5/copytrade/create-sgl-link body { "orderId": "3556007031710728192",
 | 参数名 | 类型 | 描述
 | shortLink | String | 通用分享短链。接收方在 OKX App 中打开该链接后，下单面板将自动填入对应的订单参数。
+2026-08-26
+新增接口：获取 Delta 对冲币种
+部分代币化资产的币种名称与其追踪的标的资产不同，如 XAAPL 与 AAPL、BETH 与 ETH。由于此类币种共享同一标的资产，持有其中一方的仓位可对冲另一方的仓位。现可通过接口获取该对应关系。
+- 新增接口：
+  - 获取 Delta 对冲币种
 2026-08-20
 WebSocket 订单频道推送行为调整

```

### Bybit V5 (`bybit`)
- Source: https://bybit-exchange.github.io/docs/changelog/v5
- Raw: https://bybit-exchange.github.io/docs/changelog/v5

```diff
diff --git a/changelogs/bybit.txt b/changelogs/bybit.txt
index ddea632..82d3b2a 100644
--- a/changelogs/bybit.txt
+++ b/changelogs/bybit.txt
@@ -13,4 +13,33 @@ Websocket API​
 - Connect
   - Add websocket integration method for Argentina users
+2026-08-27​
+REST API​
+- Get Position Info [UPDATE]
+  - Add new response field netDeltaRatio: Net delta ratio.
+- Get Instruments Info [UPDATE]
+  - Add new field fullName, marketRegion, underlyingTicker to differentiate the symbols represent same stock but in different venues
+- Get Account Instruments Info [UPDATE]
+  - Add new field fullName, marketRegion, underlyingTicker to differentiate the symbols represent same stock but in different venues
+- Funding Account Transaction History [UPDATE]
+  - Add a new response field currcCursor, which is used to duplicate check
+Websocket API​
+- Position [UPDATE]
+  - Add new field netDeltaRatio: Net delta ratio.
+2026-08-25​
+REST API​
+- Batch Place Order [UPDATE]
+  - category=option reduces the batch size to 5
+- Batch Amend Order [UPDATE]
+  - category=option reduces the batch size to 5
+- Batch Cancel Order [UPDATE]
+  - category=option reduces the batch size to 5
+- Get Universal Transfer List [UPDATE]
+  - Add new request parameters fromMemberId, toMemberId, used to filter the transfer list by from/to account.
+  - Add new response fields withdrawReqId, depositReqId, the intenrally used req ID
+Websocket API​
+- WS order entry: Batch Create/Amend/Cancel Order [UPDATE]
+  - category=option reduces the batch size to 5
+- SBE order entry: Batch Request V5 [UPDATE]
+  - category=option reduces the batch size to 5
 2026-08-20​
 REST API​

```

### KuCoin (Spot + Futures) (`kucoin`)
- Source: https://www.kucoin.com/docs-new/change-log
- Raw: https://www.kucoin.com/docs-new/change-log

```diff
diff --git a/changelogs/kucoin.txt b/changelogs/kucoin.txt
index 8974b36..babd4b5 100644
--- a/changelogs/kucoin.txt
+++ b/changelogs/kucoin.txt
@@ -1,2 +1,40 @@
+2026.08.27 V2 Upgrade#
+1.
+The URLs of all UTA API V2 endpoints have been updated, and all endpoints have been upgraded to the V2 version.
+2.
+The following API parameters have been changed compared with V1:
+| Update Type | Endpoints | Update Info
+| [Modify] | UTA REST Get Account Currency Assets (Classic) | Rename response field: hold → locked
+| [Modify] | UTA REST Get Sub Account Currency Assets | Rename request field: UID → uid
+Update response structure and fields: accountList → accounts, currencyList → currencies, accountSubType → subAccountType, liabilityPrinciple → liabilityPrincipal, hold → locked
+Remove documented response enum value: accountType: OPTIONS
+| [Modify] | UTA REST Flex Transfer | Replace request field: type → transferType with INTERNAL, PARENT_TO_SUB, SUB_TO_PARENT, SUB_TO_SUB
+Replace optional request fields with required fields: fromAccountSymbol → fromAccountTag, toAccountSymbol → toAccountTag
+| [Modify] | UTA REST Get Deposit Address | Rename response fields: chainId → chain, to → toAccountType
+Response fields memo and remark are now optional
+| [Modify] | UTA REST Get Withdrawal Quotas | Rename request field: chainId → chain
+Add request fields: withdrawType (required), isInner (optional)
+Rename response fields: chainId → chain, remainAmount → remainingQuotaAmount, availableAmount → availableWithdrawAmount, withdrawMinFee → minWithdrawFee, innerWithdrawMinFee → minInnerWithdrawFee
+| [Modify] | UTA REST Get Currency | Change request field: currency is required now
+Rename chain-level response field: chainId → chain
+Add chain-level regex and fee fields: addressRegex, memoRegex, depositFeeRate, depositTierFee, fixedDepositFee, maxDepositFee, maxWithdrawFee
+| [Modify] | UTA REST Get Currencies | Update response structure and fields: items[] → list[], chainId → chain
+Remove currency-level fields: isMarginEnabled, isDebitEnabled
+Add chain-level regex and fee fields: addressRegex, memoRegex, depositFeeRate, depositTierFee, fixedDepositFee, maxDepositFee, maxWithdrawFee
+| [Modify] | UTA REST Get Fiat Price | Change request fields: base is required now
+currencies changed from a comma-separated string to a string array
+| [Modify] | UTA REST Get Symbol | Add response fields: maxMarketOrderSize, preMarketToPerpDate
+Update response enums: tradingStatus values: TradingEnabled, TradingDisabled, Init, Open, PrepareSettled, BeingSettled, Settled, Paused, Closed, CancelOnly; feeCategory: 1, 2, 3 → classA, classB, classC
+Update response field types: callauctionFirstStageStartTime, callauctionSecondStageStartTime, callauctionThirdStageStartTime, expiryTime, settlementTime, maxLeverage
+| [Modify] | UTA REST Withdraw | Rename request field: chainId → chain
+| [Add] | UTA REST Amend Order & UTA Websocket Amend Order | New endpoint
+| [Modify] | UTA REST Get Order Details & Get Order History | Response field cancelReason returns an enum value instead of a descriptive cancellation reason. Changes have been applied to both UTA API V1 and V2.
+| [Modify] | UTA REST Get Trade History | Add request field fillType to support querying all kinds of trade types
+| [Modify] | UTA Websocket Funding Fee | Add new request field symbols to support subscribing to multiple symbols and new response field lfr, representing the last funding fee rate corresponding to the last settlement time
+| [Add] | UTA Websocket All Funding Fee Rates | New endpoint
+| [Add] | UTA REST Get Current Funding Rate | New endpoint. Get current Futures funding rates by contract symbol or product type.
+| [Modify] | UTA REST Get Index Price | Fix symbol in/out: .KXBTUSDT → XBTUSDTM
+| [Modify] | UTA REST Get Futures Interest Rate Index | Add standard XBTUSDTM to the input parameter
+| [Modify] | UTA REST Get Klines | Add klineType to replace symbol suffix encoding; strip suffix from symbol (backward compatible); Symbol Naming Standard set to govern future interfaces
 2026.08.27#
 [Modify] For all UTA public WebSocket connections (FUTURES and SPOT), the welcome response sent after a successful connection now returns "data":"welcome" rather than "message":"welcome". A new pingTimeout field is also included, which indicates the estimated interval (in ms) within which the client should receive a pong message from the server.

```
