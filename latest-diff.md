<!-- has_changes=true date=2026-04-27 -->
# Exchange API Changelog Diff

Generated: 2026-04-27 (Asia/Shanghai)

## Summary

- [OK] Binance Spot (`binance-spot`): no change (126374 bytes)

- [OK] Binance Derivatives (USDS-M / Coin-M / Options) (`binance-derivatives`): no change (85776 bytes)

- [OK] OKX V5 (`okx`): no change (186803 bytes)

- [OK] Bitget (Spot + Futures) (`bitget`): no change (26700 bytes)

- [OK] Bybit V5 (`bybit`): no change (76797 bytes)

- [OK] KuCoin (Spot + Futures) (`kucoin`): no change (28151 bytes)

- [CHANGED] **Gate.io Spot WebSocket v4** (`gate-spot-ws`): 14 diff lines

- [CHANGED] **Gate.io Futures WebSocket v4** (`gate-futures-ws`): 14 diff lines



## Changes

### Gate.io Spot WebSocket v4 (`gate-spot-ws`)
- Source: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/apiv4/ws/zh_CN/

```diff
diff --git a/changelogs/gate-spot-ws.txt b/changelogs/gate-spot-ws.txt
index 5880089..2567e1d 100644
--- a/changelogs/gate-spot-ws.txt
+++ b/changelogs/gate-spot-ws.txt
@@ -1,3 +1,3 @@
-# 现货 WebSocket v4
+# Spot WebSocket v4.0.0
 WebSocket 应用示例
 # !/usr/bin/env python # coding: utf-8 import hashlib import hmac import json import logging import time import threading # pip install -U websocket_client from websocket import WebSocketApp logging.basicConfig(level=logging.INFO) logger = logging.getLogger(__name__) event = threading.Event() class GateWebSocketApp(WebSocketApp): def __init__(self, url, api_key, api_secret, **kwargs): super(GateWebSocketApp, self).__init__(url, **kwargs) self._api_key = api_key self._api_secret = api_secret def _send_ping(self): while not event.wait(10): self.last_ping_tm = time.time() if self.sock: try: self.sock.ping() except Exception as ex: logger.warning("send_ping routine terminated: {}".format(ex)) break try: self._request("spot.ping", auth_required=False) except Exception as e: raise e def _request(self, channel, event=None, payload=None, auth_required=True): current_time = int(time.time()) data = { "time": current_time, "channel": channel, "event": event, "payload": payload, } if auth_required: message = 'channel=%s&event=%s&time=%d' % (channel, event, current_time) data['auth'] = { "method": "api_key", "KEY": self._api_key, "SIGN": self.get_sign(message), } data = json.dumps(data) logger.info('request: %s', data) self.send(data) def get_sign(self, message): h = hmac.new(self._api_secret.encode("utf8"), message.encode("utf8"), hashlib.sha512) return h.hexdigest() def subscribe(self, channel, payload=None, auth_required=True): self._request(channel, "subscribe", payload, auth_required) def unsubscribe(self, channel, payload=None, auth_required=True): self._request(channel, "unsubscribe", payload, auth_required) def on_message(ws, message): # type: (GateWebSocketApp, str) -> None # handle whatever message you received logger.info("message received from server: {}".format(message)) def on_open(ws): # type: (GateWebSocketApp) -> None # subscribe to channels interested logger.info('websocket connected') ws.subscribe("spot.trades", ['BTC_USDT'], False) if __name__ == "__main__": logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG) app = GateWebSocketApp("wss://api.gateio.ws/ws/v4/", "YOUR_API_KEY", "YOUR_API_SECRET", on_open=on_open, on_message=on_message) app.run_forever(ping_interval=5)
@@ -1477,3 +1477,3 @@ account: 指定查询账户。不指定默认现货，保证金和逐仓杠杆
 | »»label | String | 以字符串格式表示错误类型
 | »»message | String | 错误信息详情
-Last Updated: 4/1/2026, 3:20:41 AM
+Last Updated: 4/26/2026, 6:24:01 AM

```

### Gate.io Futures WebSocket v4 (`gate-futures-ws`)
- Source: https://www.gate.io/docs/developers/futures/ws/zh_CN/
- Raw: https://www.gate.io/docs/developers/futures/ws/zh_CN/

```diff
diff --git a/changelogs/gate-futures-ws.txt b/changelogs/gate-futures-ws.txt
index f2bd378..9f3884f 100644
--- a/changelogs/gate-futures-ws.txt
+++ b/changelogs/gate-futures-ws.txt
@@ -1,3 +1,3 @@
-# Gate 永续合约 WebSocket v4
+# Gate Futures WebSocket v4.0.0
 Gate 提供简单而强大的 Websocket API，将 Gate BTCUSDT 永续合约交易状态集成到您的业务或应用程序中。
 我们在 Python 和 Golang 中有语言绑定，将来还会有更多！您可以在右侧的深色区域中查看代码示例，并且可以通过右上角的选项卡切换示例的编程语言
@@ -1947,3 +1947,3 @@ req_param` API 订单模型的 JSON 字节数据:
 | »»label | String | 错误类型
 | »»message | String | 详细错误信息
-Last Updated: 4/14/2026, 1:16:45 AM
+Last Updated: 4/27/2026, 1:01:38 AM

```
