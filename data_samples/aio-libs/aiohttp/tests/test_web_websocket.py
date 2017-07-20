import asyncio
from unittest import mock
import pytest
from multidict import CIMultiDict
from aiohttp import WSMessage, WSMsgType, helpers, signals
from aiohttp.log import ws_logger
from aiohttp.test_utils import make_mocked_coro, make_mocked_request
from aiohttp.web import HTTPBadRequest, HTTPMethodNotAllowed, WebSocketResponse
from aiohttp.web_ws import WS_CLOSED_MESSAGE, WebSocketReady

@pytest.fixture
def function1902(arg511):
    var609 = mock.Mock()
    var609.loop = arg511
    var609._debug = False
    var609.on_response_prepare = signals.Signal(var609)
    return var609

@pytest.fixture
def function61():
    function61 = mock.Mock()
    function61.drain.return_value = ()
    function61.write_eof.return_value = ()
    return function61

@pytest.fixture
def function499():
    var2479 = mock.Mock()
    var2479.set_parser.return_value = var2479
    return var2479

@pytest.fixture
def function271(function1902, function499, function61):

    def function69(arg1660, arg103, arg1031=None, arg1602=False):
        if (arg1031 is None):
            arg1031 = CIMultiDict({'HOST': 'server.example.com', 'UPGRADE': 'websocket', 'CONNECTION': 'Upgrade', 'SEC-WEBSOCKET-KEY': 'dGhlIHNhbXBsZSBub25jZQ==', 'ORIGIN': 'http://example.com', 'SEC-WEBSOCKET-VERSION': '13', })
        if arg1602:
            arg1031['SEC-WEBSOCKET-PROTOCOL'] = 'chat, superchat'
        return make_mocked_request(arg1660, arg103, arg1031, app=function1902, protocol=function499, payload_writer=function61)
    return function69

def function2584():
    var1663 = WebSocketResponse()
    with pytest.raises(RuntimeError):
        var1663.ping()

def function1566():
    var4050 = WebSocketResponse()
    with pytest.raises(RuntimeError):
        var4050.pong()

def function742():
    var3256 = WebSocketResponse()
    with pytest.raises(RuntimeError):
        var3256.send_str('string')

def function2736():
    var708 = WebSocketResponse()
    with pytest.raises(RuntimeError):
        var708.send_bytes(b'bytes')

def function2225():
    var3068 = WebSocketResponse()
    with pytest.raises(RuntimeError):
        var3068.send_json({'type': 'json', })

@asyncio.coroutine
def function842():
    var1638 = WebSocketResponse()
    with pytest.raises(RuntimeError):
        yield from var1638.close()

@asyncio.coroutine
def function1593():
    var1675 = WebSocketResponse()
    with pytest.raises(RuntimeError):
        yield from var1675.receive_str()

@asyncio.coroutine
def function1966():
    var134 = WebSocketResponse()
    with pytest.raises(RuntimeError):
        yield from var134.receive_bytes()

@asyncio.coroutine
def function360():
    var468 = WebSocketResponse()
    with pytest.raises(RuntimeError):
        yield from var468.receive_json()

@asyncio.coroutine
def function2486(function271):
    var1174 = function271('GET', '/')
    var4064 = WebSocketResponse()
    yield from var4064.prepare(var1174)

    @asyncio.coroutine
    def function1900():
        return WSMessage(WSMsgType.BINARY, b'data', b'')
    var4064.receive = function1900
    with pytest.raises(TypeError):
        yield from var4064.receive_str()

@asyncio.coroutine
def function2630(function271):
    var2339 = function271('GET', '/')
    var3483 = WebSocketResponse()
    yield from var3483.prepare(var2339)

    @asyncio.coroutine
    def function1900():
        return WSMessage(WSMsgType.TEXT, 'data', b'')
    var3483.receive = function1900
    with pytest.raises(TypeError):
        yield from var3483.receive_bytes()

@asyncio.coroutine
def function2625(function271):
    var4377 = function271('GET', '/')
    var1358 = WebSocketResponse()
    yield from var1358.prepare(var4377)
    with pytest.raises(TypeError):
        var1358.send_str(b'bytes')

@asyncio.coroutine
def function612(function271):
    var540 = function271('GET', '/')
    var2482 = WebSocketResponse()
    yield from var2482.prepare(var540)
    with pytest.raises(TypeError):
        var2482.send_bytes('string')

@asyncio.coroutine
def function1324(function271):
    var3572 = function271('GET', '/')
    var2977 = WebSocketResponse()
    yield from var2977.prepare(var3572)
    with pytest.raises(TypeError):
        var2977.send_json(set())

def function2812():
    var550 = WebSocketResponse()
    with pytest.raises(RuntimeError):
        var550.write(b'data')

def function1889():
    var4181 = WebSocketReady(True, 'chat')
    assert (var4181.ok is True)
    assert (var4181.function499 == 'chat')

def function1027():
    var3638 = WebSocketReady(False, None)
    assert (var3638.ok is False)
    assert (var3638.function499 is None)

def function4():
    var4173 = WebSocketReady(True, None)
    assert (var4173.ok is True)
    assert (var4173.function499 is None)

def function2721():
    var1479 = WebSocketReady(True, None)
    assert (bool(var1479) is True)

def function1317():
    var3713 = WebSocketReady(False, None)
    assert (bool(var3713) is False)

def function1233(function271):
    var373 = function271('GET', '/', protocols=True)
    var725 = WebSocketResponse(protocols=('chat',))
    assert ((True, 'chat') == var725.can_prepare(var373))

def function801(function271):
    var2751 = function271('GET', '/')
    var281 = WebSocketResponse()
    assert ((True, None) == var281.can_prepare(var2751))

def function1547(function271):
    var3899 = function271('POST', '/')
    var3504 = WebSocketResponse()
    assert ((False, None) == var3504.can_prepare(var3899))

def function2006(function271):
    var32 = function271('GET', '/', headers=CIMultiDict({}))
    var133 = WebSocketResponse()
    assert ((False, None) == var133.can_prepare(var32))

@asyncio.coroutine
def function350(function271):
    var4234 = function271('GET', '/')
    var3290 = WebSocketResponse()
    yield from var3290.prepare(var4234)
    with pytest.raises(RuntimeError) as var847:
        var3290.can_prepare(var4234)
    assert ('Already started' in str(var847.value))

def function2110():
    var1585 = WebSocketResponse()
    assert (not var1585.closed)
    assert (var1585.close_code is None)

@asyncio.coroutine
def function2561(function271, arg922):
    var2863 = function271('GET', '/')
    var2278 = WebSocketResponse()
    yield from var2278.prepare(var2863)
    var2278._reader.feed_data(WS_CLOSED_MESSAGE, 0)
    yield from var2278.close()
    arg922.spy(ws_logger, 'warning')
    var2278.send_str('string')
    assert ws_logger.warning.called

@asyncio.coroutine
def function2783(function271, arg1739):
    var4570 = function271('GET', '/')
    var3309 = WebSocketResponse()
    yield from var3309.prepare(var4570)
    var3309._reader.feed_data(WS_CLOSED_MESSAGE, 0)
    yield from var3309.close()
    arg1739.spy(ws_logger, 'warning')
    var3309.send_bytes(b'bytes')
    assert ws_logger.warning.called

@asyncio.coroutine
def function1203(function271, arg476):
    var1953 = function271('GET', '/')
    var1605 = WebSocketResponse()
    yield from var1605.prepare(var1953)
    var1605._reader.feed_data(WS_CLOSED_MESSAGE, 0)
    yield from var1605.close()
    arg476.spy(ws_logger, 'warning')
    var1605.send_json({'type': 'json', })
    assert ws_logger.warning.called

@asyncio.coroutine
def function835(function271, arg1247):
    var816 = function271('GET', '/')
    var1269 = WebSocketResponse()
    yield from var1269.prepare(var816)
    var1269._reader.feed_data(WS_CLOSED_MESSAGE, 0)
    yield from var1269.close()
    arg1247.spy(ws_logger, 'warning')
    var1269.ping()
    assert ws_logger.warning.called

@asyncio.coroutine
def function2874(function271, arg512):
    var1102 = function271('GET', '/')
    var1066 = WebSocketResponse()
    yield from var1066.prepare(var1102)
    var1066._reader.feed_data(WS_CLOSED_MESSAGE, 0)
    yield from var1066.close()
    arg512.spy(ws_logger, 'warning')
    var1066.pong()
    assert ws_logger.warning.called

@asyncio.coroutine
def function716(function271, function61):
    var4554 = function271('GET', '/')
    var4135 = WebSocketResponse()
    yield from var4135.prepare(var4554)
    var4135._reader.feed_data(WS_CLOSED_MESSAGE, 0)
    assert yield from var4135.close(code=1, message='message1')
    assert var4135.closed
    assert (not yield from var4135.close(code=2, message='message2'))

@asyncio.coroutine
def function1314(function271):
    var183 = function271('POST', '/')
    var3527 = WebSocketResponse()
    with pytest.raises(HTTPMethodNotAllowed):
        yield from var3527.prepare(var183)

@asyncio.coroutine
def function1287(function271):
    var1020 = function271('GET', '/', headers=CIMultiDict({}))
    var1629 = WebSocketResponse()
    with pytest.raises(HTTPBadRequest):
        yield from var1629.prepare(var1020)

@asyncio.coroutine
def function1096():
    var4148 = WebSocketResponse()
    with pytest.raises(RuntimeError):
        yield from var4148.close()

@asyncio.coroutine
def function1062():
    var1034 = WebSocketResponse()
    with pytest.raises(RuntimeError):
        yield from var1034.write_eof()

@asyncio.coroutine
def function2567(function271):
    var424 = function271('GET', '/')
    var4602 = WebSocketResponse()
    yield from var4602.prepare(var424)
    var4602._reader.feed_data(WS_CLOSED_MESSAGE, 0)
    yield from var4602.close()
    yield from var4602.write_eof()
    yield from var4602.write_eof()
    yield from var4602.write_eof()

@asyncio.coroutine
def function2536(function271, arg68):
    var3402 = function271('GET', '/')
    var3771 = WebSocketResponse()
    yield from var3771.prepare(var3402)
    var3771._reader = mock.Mock()
    var2011 = ValueError()
    var1794 = helpers.create_future(arg68)
    var1794.set_exception(var2011)
    var3771._reader.read = make_mocked_coro(var1794)
    var3771._payload_writer.drain = mock.Mock()
    var3771._payload_writer.drain.return_value = helpers.create_future(arg68)
    var3771._payload_writer.drain.return_value.set_result(True)
    var2571 = yield from var3771.function1900()
    assert (var2571.type == WSMsgType.ERROR)
    assert (var2571.type is var2571.tp)
    assert (var2571.data is var2011)
    assert (var3771.exception() is var2011)

@asyncio.coroutine
def function2691(function271, arg857):
    var342 = function271('GET', '/')
    var4624 = WebSocketResponse()
    yield from var4624.prepare(var342)
    var4624._reader = mock.Mock()
    var3438 = helpers.create_future(arg857)
    var3438.set_exception(asyncio.CancelledError())
    var4624._reader.read = make_mocked_coro(var3438)
    with pytest.raises(asyncio.CancelledError):
        yield from var4624.function1900()

@asyncio.coroutine
def function2107(function271, arg2001):
    var1118 = function271('GET', '/')
    var3191 = WebSocketResponse()
    yield from var3191.prepare(var1118)
    var3191._reader = mock.Mock()
    var4512 = helpers.create_future(arg2001)
    var4512.set_exception(asyncio.TimeoutError())
    var3191._reader.read = make_mocked_coro(var4512)
    with pytest.raises(asyncio.TimeoutError):
        yield from var3191.function1900()

@asyncio.coroutine
def function2740(function271):
    var975 = function271('GET', '/')
    var3594 = WebSocketResponse()
    yield from var3594.prepare(var975)
    var3594._reader.feed_data(WS_CLOSED_MESSAGE, 0)
    yield from var3594.close()
    yield from var3594.function1900()
    yield from var3594.function1900()
    yield from var3594.function1900()
    yield from var3594.function1900()
    with pytest.raises(RuntimeError):
        yield from var3594.function1900()

@asyncio.coroutine
def function2521(function271):
    var4739 = function271('GET', '/')
    var1693 = WebSocketResponse()
    yield from var1693.prepare(var4739)
    var1693._waiting = True
    with pytest.raises(RuntimeError):
        yield from var1693.function1900()

@asyncio.coroutine
def function479(function271, arg926, arg363):
    var1796 = function271('GET', '/')
    var300 = WebSocketResponse()
    yield from var300.prepare(var1796)
    var300._reader = mock.Mock()
    var4357 = ValueError()
    var300._reader.read.return_value = helpers.create_future(arg926)
    var300._reader.read.return_value.set_exception(var4357)
    var300._payload_writer.drain = mock.Mock()
    var300._payload_writer.drain.return_value = helpers.create_future(arg926)
    var300._payload_writer.drain.return_value.set_result(True)
    yield from var300.close()
    assert var300.closed
    assert (var300.exception() is var4357)
    var300._closed = False
    var300._reader.read.return_value = helpers.create_future(arg926)
    var300._reader.read.return_value.set_exception(asyncio.CancelledError())
    with pytest.raises(asyncio.CancelledError):
        yield from var300.close()
    assert (var300.close_code == 1006)

@asyncio.coroutine
def function113(function271):
    var2027 = function271('GET', '/')
    var2897 = WebSocketResponse()
    yield from var2897.prepare(var2027)
    var962 = ValueError()
    var2897._writer = mock.Mock()
    var2897._writer.close.side_effect = var962
    yield from var2897.close()
    assert var2897.closed
    assert (var2897.exception() is var962)
    var2897._closed = False
    var2897._writer.close.side_effect = asyncio.CancelledError()
    with pytest.raises(asyncio.CancelledError):
        yield from var2897.close()

@asyncio.coroutine
def function265(function271):
    var2045 = function271('GET', '/')
    var4391 = WebSocketResponse()
    var4138 = yield from var4391.prepare(var2045)
    var1947 = yield from var4391.prepare(var2045)
    assert (var4138 is var1947)