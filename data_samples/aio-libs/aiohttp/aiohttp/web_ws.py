import asyncio
import json
from collections import namedtuple
from . import hdrs
from .helpers import PY_35, PY_352, Timeout, call_later, create_future
from .http import WS_CLOSED_MESSAGE, WS_CLOSING_MESSAGE, HttpProcessingError, WebSocketError, WebSocketReader, WSMessage, WSMsgType, do_handshake
from .streams import FlowControlDataQueue
from .web_exceptions import HTTPBadRequest, HTTPInternalServerError, HTTPMethodNotAllowed
from .web_response import StreamResponse
var3961 = ('WebSocketResponse', 'WebSocketReady', 'MsgType', 'WSMsgType')
var2253 = 5
var2306 = WSMsgType


class Class345(namedtuple('WebSocketReady', 'ok protocol')):

    def __bool__(self):
        return self.ok


class Class87(StreamResponse):

    def __init__(self, *, timeout=10.0, receive_timeout=None, autoclose=True, autoping=True, heartbeat=None, protocols=()):
        super().__init__(status=101)
        self.attribute810 = protocols
        self.attribute1363 = None
        self.attribute850 = None
        self.attribute1344 = None
        self.attribute971 = False
        self.attribute2203 = False
        self.attribute1663 = 0
        self.attribute626 = None
        self.attribute0 = None
        self.attribute1763 = None
        self.attribute280 = None
        self.attribute386 = timeout
        self.attribute485 = receive_timeout
        self.attribute1740 = autoclose
        self.attribute2274 = autoping
        self.attribute1614 = heartbeat
        self.attribute1798 = None
        if (heartbeat is not None):
            self.attribute2228 = (heartbeat / 2.0)
        self.attribute1822 = None

    def function1314(self):
        if (self.attribute1822 is not None):
            self.attribute1822.cancel()
            self.attribute1822 = None
        if (self.attribute1798 is not None):
            self.attribute1798.cancel()
            self.attribute1798 = None

    def function2198(self):
        self.function1314()
        if (self.attribute1614 is not None):
            self.attribute1798 = call_later(self.function217, self.attribute1614, self.attribute0)

    def function217(self):
        if ((self.attribute1614 is not None) and (not self.attribute971)):
            self.function2501()
            if (self.attribute1822 is not None):
                self.attribute1822.cancel()
            self.attribute1822 = call_later(self.function2219, self.attribute2228, self.attribute0)

    def function2219(self):
        if ((self._req is not None) and (self._req.transport is not None)):
            self.attribute971 = True
            self.attribute626 = 1006
            self.attribute280 = asyncio.TimeoutError()
            self._req.transport.close()

    @asyncio.coroutine
    def function1607(self, arg1567):
        if (self._payload_writer is not None):
            return self._payload_writer
        (var1495, var1351) = self.function1595(arg1567)
        var2986 = yield from super().function1607(arg1567)
        self.function1152(arg1567, var1495, var1351)
        yield from var2986.drain()
        return var2986

    def function1595(self, arg861):
        self.attribute0 = arg861.app.loop
        try:
            (var4249, var791, var1355, var3934, var1879) = do_handshake(arg861.method, arg861.var791, arg861._protocol.var3934, self.attribute810)
        except HttpProcessingError as var4553:
            if (var4553.code == 405):
                raise HTTPMethodNotAllowed(arg861.method, [hdrs.METH_GET], body=b'')
            elif (var4553.code == 400):
                raise HTTPBadRequest(text=var4553.message, headers=var4553.var791)
            else:
                raise HTTPInternalServerError() from err
        self.function2198()
        if (self.var4249 != var4249):
            self.set_status(var4249)
        for (var1370, var2997) in var791:
            self.var791[var1370] = var2997
        self.force_close()
        return (var1879, var3934)

    def function1152(self, arg861, var1879, var3934):
        self.attribute1363 = var1879
        self.attribute850 = var3934
        self.attribute1344 = FlowControlDataQueue(arg861._protocol, limit=(2 ** 16), loop=self.attribute0)
        arg861.var1879.set_parser(WebSocketReader(self.attribute1344))

    def function1200(self, arg861):
        if (self.attribute850 is not None):
            raise RuntimeError('Already started')
        try:
            (var1355, var1355, var1355, var1355, var1879) = do_handshake(arg861.method, arg861.var791, arg861._protocol.var3934, self.attribute810)
        except HttpProcessingError:
            return Class345(False, None)
        else:
            return Class345(True, var1879)

    @property
    def function2084(self):
        return self.attribute971

    @property
    def function1574(self):
        return self.attribute626

    @property
    def function461(self):
        return self.attribute1363

    def function1799(self):
        return self.attribute280

    def function2501(self, arg810='b'):
        if (self.attribute850 is None):
            raise RuntimeError('Call .prepare() first')
        self.attribute850.function2501(arg810)

    def function599(self, arg1008='b'):
        if (self.attribute850 is None):
            raise RuntimeError('Call .prepare() first')
        self.attribute850.function599(arg1008)

    def function2096(self, arg1186):
        if (self.attribute850 is None):
            raise RuntimeError('Call .prepare() first')
        if (not isinstance(arg1186, str)):
            raise TypeError(('data argument must be str (%r)' % type(arg1186)))
        return self.attribute850.send(arg1186, binary=False)

    def function248(self, arg1447):
        if (self.attribute850 is None):
            raise RuntimeError('Call .prepare() first')
        if (not isinstance(arg1447, (bytes, bytearray, memoryview))):
            raise TypeError(('data argument must be byte-ish (%r)' % type(arg1447)))
        return self.attribute850.send(arg1447, binary=True)

    def function1496(self, arg1444, *, dumps=json.dumps):
        return self.function2096(dumps(arg1444))

    @asyncio.coroutine
    def function2080(self):
        if self.attribute839:
            return
        if (self._payload_writer is None):
            raise RuntimeError('Response has not been started')
        yield from self.function2792()
        self.attribute839 = True

    @asyncio.coroutine
    def function2792(self, *, code=1000, message=b''):
        if (self.attribute850 is None):
            raise RuntimeError('Call .prepare() first')
        self.function1314()
        if ((self.attribute1763 is not None) and (not self.attribute971)):
            self.attribute1344.feed_data(WS_CLOSING_MESSAGE, 0)
            yield from self.attribute1763
        if (not self.attribute971):
            self.attribute971 = True
            try:
                self.attribute850.function2792(code, message)
                yield from self.drain()
            except (asyncio.CancelledError, asyncio.TimeoutError):
                self.attribute626 = 1006
                raise
            except Exception as var2488:
                self.attribute626 = 1006
                self.attribute280 = var2488
                return True
            if self.attribute2203:
                return True
            try:
                with Timeout(self.attribute386, loop=self.attribute0):
                    var2466 = yield from self.attribute1344.read()
            except asyncio.CancelledError:
                self.attribute626 = 1006
                raise
            except Exception as var2488:
                self.attribute626 = 1006
                self.attribute280 = var2488
                return True
            if (var2466.type == WSMsgType.CLOSE):
                self.attribute626 = var2466.data
                return True
            self.attribute626 = 1006
            self.attribute280 = asyncio.TimeoutError()
            return True
        else:
            return False

    @asyncio.coroutine
    def function2485(self, arg580=None):
        if (self.attribute1344 is None):
            raise RuntimeError('Call .prepare() first')
        while True:
            if (self.attribute1763 is not None):
                raise RuntimeError('Concurrent call to receive() is not allowed')
            if self.attribute971:
                self.attribute1663 += 1
                if (self.attribute1663 >= var2253):
                    raise RuntimeError('WebSocket connection is closed.')
                return WS_CLOSED_MESSAGE
            elif self.attribute2203:
                return WS_CLOSING_MESSAGE
            try:
                self.attribute1763 = create_future(self.attribute0)
                try:
                    with Timeout((timeout or self.attribute485), loop=self.attribute0):
                        var2466 = yield from self.attribute1344.read()
                    self.function2198()
                finally:
                    var3717 = self.attribute1763
                    self.attribute1763 = None
                    var3717.set_result(True)
            except (asyncio.CancelledError, asyncio.TimeoutError) as var2488:
                self.attribute626 = 1006
                raise
            except WebSocketError as var2488:
                self.attribute626 = var2488.code
                yield from self.function2792(code=var2488.code)
                return WSMessage(WSMsgType.ERROR, var2488, None)
            except Exception as var2488:
                self.attribute280 = var2488
                self.attribute2203 = True
                self.attribute626 = 1006
                yield from self.function2792()
                return WSMessage(WSMsgType.ERROR, var2488, None)
            if (var2466.type == WSMsgType.CLOSE):
                self.attribute2203 = True
                self.attribute626 = var2466.data
                if ((not self.attribute971) and self.attribute1740):
                    yield from self.function2792()
            elif (var2466.type == WSMsgType.CLOSING):
                self.attribute2203 = True
            elif ((var2466.type == WSMsgType.PING) and self.attribute2274):
                self.function599(var2466.data)
                continue
            elif ((var2466.type == WSMsgType.PONG) and self.attribute2274):
                continue
            return var2466

    @asyncio.coroutine
    def function2147(self, *, timeout=None):
        var2466 = yield from self.function2485(arg580)
        if (var2466.type != WSMsgType.TEXT):
            raise TypeError('Received message {}:{!r} is not WSMsgType.TEXT'.format(var2466.type, var2466.data))
        return var2466.data

    @asyncio.coroutine
    def function275(self, *, timeout=None):
        var2466 = yield from self.function2485(arg580)
        if (var2466.type != WSMsgType.BINARY):
            raise TypeError('Received message {}:{!r} is not bytes'.format(var2466.type, var2466.data))
        return var2466.data

    @asyncio.coroutine
    def function2480(self, *, loads=json.loads, timeout=None):
        var2670 = yield from self.function2147(timeout=arg580)
        return loads(var2670)

    def function2337(self, arg50):
        raise RuntimeError('Cannot call .write() for websocket')
    if PY_35:

        def __aiter__(self):
            return self
        if (not PY_352):
            var4653 = asyncio.coroutine(var4653)

        @asyncio.coroutine
        def __anext__(self):
            var2466 = yield from self.function2485()
            if (var2466.type in (WSMsgType.CLOSE, WSMsgType.CLOSING, WSMsgType.CLOSED)):
                raise StopAsyncIteration
            return var2466