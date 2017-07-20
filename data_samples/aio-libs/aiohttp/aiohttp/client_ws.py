'WebSocket client for asyncio.'
import asyncio
import json
from .client_exceptions import ClientError
from .helpers import PY_35, PY_352, Timeout, call_later, create_future
from .http import WS_CLOSED_MESSAGE, WS_CLOSING_MESSAGE, WebSocketError, WSMessage, WSMsgType


class Class321:

    def __init__(self, arg312, arg501, arg693, arg1016, arg1505, arg210, arg101, arg2033, *, receive_timeout=None, heartbeat=None):
        self.attribute1244 = arg1016
        self.attribute257 = arg1016.connection
        self.attribute1822 = arg501
        self.attribute459 = arg312
        self.attribute668 = arg693
        self.attribute10 = False
        self.attribute71 = False
        self.attribute1314 = None
        self.attribute758 = arg1505
        self.attribute1580 = receive_timeout
        self.attribute1153 = arg210
        self.attribute1413 = arg101
        self.attribute1388 = heartbeat
        self.attribute351 = None
        if (heartbeat is not None):
            self.attribute1004 = (heartbeat / 2.0)
        self.attribute1125 = None
        self.attribute650 = arg2033
        self.attribute98 = None
        self.attribute1713 = None
        self.function2113()

    def function1265(self):
        if (self.attribute1125 is not None):
            self.attribute1125.cancel()
            self.attribute1125 = None
        if (self.attribute351 is not None):
            self.attribute351.cancel()
            self.attribute351 = None

    def function2113(self):
        self.function1265()
        if (self.attribute1388 is not None):
            self.attribute351 = call_later(self.function1157, self.attribute1388, self.attribute650)

    def function1157(self):
        if ((self.attribute1388 is not None) and (not self.attribute10)):
            self.function1918()
            if (self.attribute1125 is not None):
                self.attribute1125.cancel()
            self.attribute1125 = call_later(self.function471, self.attribute1004, self.attribute650)

    def function471(self):
        if (not self.attribute10):
            self.attribute10 = True
            self.attribute1314 = 1006
            self.attribute1713 = asyncio.TimeoutError()
            self.attribute1244.close()

    @property
    def function2018(self):
        return self.attribute10

    @property
    def function2260(self):
        return self.attribute1314

    @property
    def function1869(self):
        return self.attribute668

    def function1796(self, arg677, arg1808=None):
        'extra info from connection transport'
        try:
            return self.attribute1244.connection.transport.function1796(arg677, arg1808)
        except:
            return arg1808

    def function1349(self):
        return self.attribute1713

    def function1918(self, arg1442='b'):
        self.attribute1822.function1918(arg1442)

    def function2181(self, arg1232='b'):
        self.attribute1822.function2181(arg1232)

    def function644(self, arg162):
        if (not isinstance(arg162, str)):
            raise TypeError(('data argument must be str (%r)' % type(arg162)))
        return self.attribute1822.send(arg162, binary=False)

    def function819(self, arg470):
        if (not isinstance(arg470, (bytes, bytearray, memoryview))):
            raise TypeError(('data argument must be byte-ish (%r)' % type(arg470)))
        return self.attribute1822.send(arg470, binary=True)

    def function2205(self, arg1185, *, dumps=json.dumps):
        return self.function644(dumps(arg1185))

    @asyncio.coroutine
    def function2368(self, *, code=1000, message=b''):
        if ((self.attribute98 is not None) and (not self.attribute10)):
            self.attribute459.feed_data(WS_CLOSING_MESSAGE, 0)
            yield from self.attribute98
        if (not self.attribute10):
            self.function1265()
            self.attribute10 = True
            try:
                self.attribute1822.function2368(code, message)
            except asyncio.CancelledError:
                self.attribute1314 = 1006
                self.attribute1244.function2368()
                raise
            except Exception as var525:
                self.attribute1314 = 1006
                self.attribute1713 = var525
                self.attribute1244.function2368()
                return True
            if self.attribute71:
                self.attribute1244.function2368()
                return True
            while True:
                try:
                    with Timeout(self.attribute758, loop=self.attribute650):
                        var52 = yield from self.attribute459.read()
                except asyncio.CancelledError:
                    self.attribute1314 = 1006
                    self.attribute1244.function2368()
                    raise
                except Exception as var525:
                    self.attribute1314 = 1006
                    self.attribute1713 = var525
                    self.attribute1244.function2368()
                    return True
                if (var52.type == WSMsgType.CLOSE):
                    self.attribute1314 = var52.data
                    self.attribute1244.function2368()
                    return True
        else:
            return False

    @asyncio.coroutine
    def function1959(self, arg1248=None):
        while True:
            if (self.attribute98 is not None):
                raise RuntimeError('Concurrent call to receive() is not allowed')
            if self.attribute10:
                return WS_CLOSED_MESSAGE
            elif self.attribute71:
                yield from self.function2368()
                return WS_CLOSED_MESSAGE
            try:
                self.attribute98 = create_future(self.attribute650)
                try:
                    with Timeout((timeout or self.attribute1580), loop=self.attribute650):
                        var52 = yield from self.attribute459.read()
                    self.function2113()
                finally:
                    var2137 = self.attribute98
                    self.attribute98 = None
                    var2137.set_result(True)
            except (asyncio.CancelledError, asyncio.TimeoutError):
                self.attribute1314 = 1006
                raise
            except ClientError:
                self.attribute10 = True
                self.attribute1314 = 1006
                return WS_CLOSED_MESSAGE
            except WebSocketError as var525:
                self.attribute1314 = var525.code
                yield from self.function2368(code=var525.code)
                return WSMessage(WSMsgType.ERROR, var525, None)
            except Exception as var525:
                self.attribute1713 = var525
                self.attribute71 = True
                self.attribute1314 = 1006
                yield from self.function2368()
                return WSMessage(WSMsgType.ERROR, var525, None)
            if (var52.type == WSMsgType.CLOSE):
                self.attribute71 = True
                self.attribute1314 = var52.data
                if ((not self.attribute10) and self.attribute1153):
                    yield from self.function2368()
            elif (var52.type == WSMsgType.CLOSING):
                self.attribute71 = True
            elif ((var52.type == WSMsgType.PING) and self.attribute1413):
                self.function2181(var52.data)
                continue
            elif ((var52.type == WSMsgType.PONG) and self.attribute1413):
                continue
            return var52

    @asyncio.coroutine
    def function858(self, *, timeout=None):
        var52 = yield from self.function1959(arg1248)
        if (var52.type != WSMsgType.TEXT):
            raise TypeError('Received message {}:{!r} is not str'.format(var52.type, var52.data))
        return var52.data

    @asyncio.coroutine
    def function2267(self, *, timeout=None):
        var52 = yield from self.function1959(arg1248)
        if (var52.type != WSMsgType.BINARY):
            raise TypeError('Received message {}:{!r} is not bytes'.format(var52.type, var52.data))
        return var52.data

    @asyncio.coroutine
    def function1176(self, *, loads=json.loads, timeout=None):
        var2727 = yield from self.function858(timeout=arg1248)
        return loads(var2727)
    if PY_35:

        def __aiter__(self):
            return self
        if (not PY_352):
            var1487 = asyncio.coroutine(var1487)

        @asyncio.coroutine
        def __anext__(self):
            var52 = yield from self.function1959()
            if (var52.type in (WSMsgType.CLOSE, WSMsgType.CLOSING, WSMsgType.CLOSED)):
                raise StopAsyncIteration
            return var52