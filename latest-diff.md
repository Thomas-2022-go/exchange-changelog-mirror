<!-- has_changes=true date=2026-08-04 -->
# Exchange API Changelog Diff

Generated: 2026-08-04 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (132459 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (1 bytes)

- [CHANGED] **OKX V5** (`okx`): 20 diff lines

- [OK] Bitget (Spot + Futures) (`bitget`): no change (3293 bytes)

- [OK] Bybit V5 (`bybit`): no change (89002 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (36254 bytes)

- [OK] Gate.io Spot WebSocket v4 (`gate-spot-ws`): no change (120484 bytes)

- [OK] Gate.io Futures WebSocket v4 (`gate-futures-ws`): no change (145596 bytes)



## Changes

### OKX V5 (`okx`)
- Source: https://www.okx.com/docs-v5/log_zh/
- Raw: https://www.okx.com/docs-v5/log_zh/

```diff
diff --git a/changelogs/okx.txt b/changelogs/okx.txt
index 73614d5..4b762ea 100644
--- a/changelogs/okx.txt
+++ b/changelogs/okx.txt
@@ -49,4 +49,15 @@ size 被修改 | state: live → state: live（amendSource: 4，amendResult: 0
 受影响的订单类型有：post_only、mmp_and_post_only、rpi（Retail Price Improvement）。
 其他订单类型如 limit（普通限价单）、market（市价单）、ioc、fok 订单推送行为保持不变。
+2026-08-03
+联盟受邀用户接口新增 UID、加入时间筛选与滚动窗口成交量
+- 获取直客列表 新增请求参数：
+| 参数名 | 类型 | 是否必须 | 描述
+| uid | String | 否 | 按外部 UID 精确匹配。单个或最多 100 个 UID，以逗号分隔。无法解析的 UID 静默跳过；若全部无法解析，返回空页。
+| joinTimeBegin | String | 条件必填 | 按 joinTime 过滤的下界，Unix时间戳的毫秒数格式，包含端点。需与 joinTimeEnd 同时传入；区间不超过 90 天，且不早于当前时间 180 天前。
+| joinTimeEnd | String | 条件必填 | 按 joinTime 过滤的上界，Unix时间戳的毫秒数格式，包含端点。需与 joinTimeBegin 同时传入。
+- 获取被邀请人返佣信息 新增请求参数 periodType 与响应字段 volPeriod：
+| 参数名 | 类型 | 描述
+| periodType（请求） | String | volPeriod 的统计窗口：last_7d、last_30d、this_month、last_month、total、today、this_week。不传时不返回 volPeriod。
+| volPeriod（响应） | String | 所选 periodType 窗口内的交易量，单位为 USDT。仅当传入 periodType 时返回。窗口内无交易时返回 0。
 2026-07-28
 ELP 更名为 RPI（散户价格优化）计划

```
