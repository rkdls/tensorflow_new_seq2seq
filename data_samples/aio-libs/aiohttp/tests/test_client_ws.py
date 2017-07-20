import asyncio
import base64
import hashlib
import os
from unittest import mock
import pytest
import aiohttp
from aiohttp import client, hdrs, helpers
from aiohttp.http import WS_KEY
from aiohttp.log import ws_logger

@pytest.fixture
def function1058():
    return os.urandom(16)

@pytest.fixture
def function1528(function1058):
    return base64.b64encode(function1058)

@pytest.fixture
def function539(function1528):
    return base64.b64encode(hashlib.sha1((function1528 + WS_KEY)).digest()).decode()

@asyncio.coroutine
def function2180(function539, arg1977, function1058):
    var2162 = mock.Mock()
    var2162.status = 101
    var2162.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: ws_key, hdrs.SEC_WEBSOCKET_PROTOCOL: 'chat', }
    with mock.patch('aiohttp.client.os') as var2849:
        with mock.patch('aiohttp.client.ClientSession.get') as var2296:
            var2849.urandom.return_value = function1058
            var2296.return_value = helpers.create_future(arg1977)
            var2296.return_value.set_result(var2162)
            var3475 = yield from aiohttp.ClientSession(loop=arg1977).ws_connect('http://test.org', protocols=('t1', 't2', 'chat'))
    assert isinstance(var3475, client.ClientWebSocketResponse)
    assert (var3475.protocol == 'chat')
    assert (hdrs.ORIGIN not in var2296.call_args[1]['headers'])

@asyncio.coroutine
def function1797(function1058, arg423):
    var658 = mock.Mock()
    var658.status = 403
    with mock.patch('aiohttp.client.os') as var1749:
        with mock.patch('aiohttp.client.ClientSession.get') as var4285:
            var1749.urandom.return_value = function1058
            var4285.return_value = helpers.create_future(arg423)
            var4285.return_value.set_result(var658)
            var2381 = 'https://example.org/page.html'
            with pytest.raises(client.WSServerHandshakeError):
                yield from aiohttp.ClientSession(loop=arg423).ws_connect('http://test.org', origin=var2381)
    assert (hdrs.ORIGIN in var4285.call_args[1]['headers'])
    assert (var4285.call_args[1]['headers'][hdrs.ORIGIN] == var2381)

@asyncio.coroutine
def function1817(arg1192, function539, function1058):


    class Class132(client.ClientWebSocketResponse):

        def function2718(self, arg363=False):
            return 'customized!'
    var1258 = mock.Mock()
    var1258.status = 101
    var1258.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: ws_key, }
    with mock.patch('aiohttp.client.os') as var2749:
        with mock.patch('aiohttp.client.ClientSession.get') as var1071:
            var2749.urandom.return_value = function1058
            var1071.return_value = helpers.create_future(arg1192)
            var1071.return_value.set_result(var1258)
            var188 = yield from aiohttp.ClientSession(ws_response_class=Class132, loop=arg1192).ws_connect('http://test.org')
    assert (var188.read() == 'customized!')

@asyncio.coroutine
def function967(arg1386, function539, function1058):
    var4188 = mock.Mock()
    var4188.status = 500
    var4188.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: ws_key, }
    with mock.patch('aiohttp.client.os') as var251:
        with mock.patch('aiohttp.client.ClientSession.get') as var532:
            var251.urandom.return_value = function1058
            var532.return_value = helpers.create_future(arg1386)
            var532.return_value.set_result(var4188)
            with pytest.raises(client.WSServerHandshakeError) as var3681:
                yield from aiohttp.ClientSession(loop=arg1386).ws_connect('http://test.org', protocols=('t1', 't2', 'chat'))
    assert (var3681.value.message == 'Invalid response status')

@asyncio.coroutine
def function1301(arg1591, function539, function1058):
    var1498 = mock.Mock()
    var1498.status = 101
    var1498.headers = {hdrs.UPGRADE: 'test', hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: ws_key, }
    with mock.patch('aiohttp.client.os') as var4392:
        with mock.patch('aiohttp.client.ClientSession.get') as var1586:
            var4392.urandom.return_value = function1058
            var1586.return_value = helpers.create_future(arg1591)
            var1586.return_value.set_result(var1498)
            with pytest.raises(client.WSServerHandshakeError) as var1546:
                yield from aiohttp.ClientSession(loop=arg1591).ws_connect('http://test.org', protocols=('t1', 't2', 'chat'))
    assert (var1546.value.message == 'Invalid upgrade header')

@asyncio.coroutine
def function385(arg2077, function539, function1058):
    var1377 = mock.Mock()
    var1377.status = 101
    var1377.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: 'close', hdrs.SEC_WEBSOCKET_ACCEPT: ws_key, }
    with mock.patch('aiohttp.client.os') as var3187:
        with mock.patch('aiohttp.client.ClientSession.get') as var130:
            var3187.urandom.return_value = function1058
            var130.return_value = helpers.create_future(arg2077)
            var130.return_value.set_result(var1377)
            with pytest.raises(client.WSServerHandshakeError) as var289:
                yield from aiohttp.ClientSession(loop=arg2077).ws_connect('http://test.org', protocols=('t1', 't2', 'chat'))
    assert (var289.value.message == 'Invalid connection header')

@asyncio.coroutine
def function560(arg1428, function539, function1058):
    var2890 = mock.Mock()
    var2890.status = 101
    var2890.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: 'asdfasdfasdfasdfasdfasdf', }
    with mock.patch('aiohttp.client.os') as var3252:
        with mock.patch('aiohttp.client.ClientSession.get') as var3331:
            var3252.urandom.return_value = function1058
            var3331.return_value = helpers.create_future(arg1428)
            var3331.return_value.set_result(var2890)
            with pytest.raises(client.WSServerHandshakeError) as var3539:
                yield from aiohttp.ClientSession(loop=arg1428).ws_connect('http://test.org', protocols=('t1', 't2', 'chat'))
    assert (var3539.value.message == 'Invalid challenge response')

@asyncio.coroutine
def function1304(function539, arg1890, function1058):
    'Emulate a headers dict being reused for a second ws_connect.\n\n    In this scenario, we need to ensure that the newly generated secret key\n    is sent to the server, not the stale key.\n    '
    var1332 = {}

    @asyncio.coroutine
    def function1442():

        @asyncio.coroutine
        def function2316(*args, **kwargs):
            var967 = mock.Mock()
            var967.status = 101
            function1528 = kwargs.get('headers').get(hdrs.SEC_WEBSOCKET_KEY)
            var3573 = base64.b64encode(hashlib.sha1((base64.b64encode(base64.b64decode(function1528)) + WS_KEY)).digest()).decode()
            var967.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: accept, hdrs.SEC_WEBSOCKET_PROTOCOL: 'chat', }
            return var967
        with mock.patch('aiohttp.client.os') as var1705:
            with mock.patch('aiohttp.client.ClientSession.get', side_effect=function2316) as var902:
                var1705.urandom.return_value = function1058
                var2127 = yield from aiohttp.ClientSession(loop=arg1890).ws_connect('http://test.org', protocols=('t1', 't2', 'chat'), headers=var1332)
        assert isinstance(var2127, client.ClientWebSocketResponse)
        assert (var2127.protocol == 'chat')
        assert (hdrs.ORIGIN not in var902.call_args[1]['headers'])
    yield from function1442()
    function1058 = os.urandom(16)
    yield from function1442()

@asyncio.coroutine
def function971(arg1297, function539, function1058):
    var1080 = mock.Mock()
    var1080.status = 101
    var1080.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: ws_key, }
    with mock.patch('aiohttp.client.WebSocketWriter') as var3469:
        with mock.patch('aiohttp.client.os') as var2214:
            with mock.patch('aiohttp.client.ClientSession.get') as var1630:
                var2214.urandom.return_value = function1058
                var1630.return_value = helpers.create_future(arg1297)
                var1630.return_value.set_result(var1080)
                var326 = var3469.return_value = mock.Mock()
                var4076 = aiohttp.ClientSession(loop=arg1297)
                var1080 = yield from var4076.ws_connect('http://test.org')
                assert (not var1080.closed)
                var1080._reader.feed_data(aiohttp.WSMessage(aiohttp.WSMsgType.CLOSE, b'', b''), 0)
                var3741 = yield from var1080.close()
                var326.close.assert_called_with(1000, b'')
                assert var1080.closed
                assert res
                assert (var1080.exception() is None)
                var3741 = yield from var1080.close()
                assert (not var3741)
                assert (var326.close.call_count == 1)
                var4076.close()

@asyncio.coroutine
def function2315(arg1211, function539, function1058):
    var2521 = mock.Mock()
    var2521.status = 101
    var2521.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: ws_key, }
    with mock.patch('aiohttp.client.WebSocketWriter') as var1229:
        with mock.patch('aiohttp.client.os') as var3401:
            with mock.patch('aiohttp.client.ClientSession.get') as var910:
                var3401.urandom.return_value = function1058
                var910.return_value = helpers.create_future(arg1211)
                var910.return_value.set_result(var2521)
                var1229.return_value = mock.Mock()
                var1939 = aiohttp.ClientSession(loop=arg1211)
                var2521 = yield from var1939.ws_connect('http://test.org')
                assert (not var2521.closed)
                var1685 = ValueError()
                var2521._reader.set_exception(var1685)
                yield from var2521.close()
                assert var2521.closed
                assert (var2521.exception() is var1685)
                var1939.close()

@asyncio.coroutine
def function775(arg1464, function539, function1058):
    var1296 = mock.Mock()
    var1296.status = 101
    var1296.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: ws_key, }
    with mock.patch('aiohttp.client.WebSocketWriter') as var203:
        with mock.patch('aiohttp.client.os') as var2983:
            with mock.patch('aiohttp.client.ClientSession.get') as var248:
                var2983.urandom.return_value = function1058
                var248.return_value = helpers.create_future(arg1464)
                var248.return_value.set_result(var1296)
                var1687 = var203.return_value = mock.Mock()
                var1296 = yield from aiohttp.ClientSession(loop=arg1464).ws_connect('http://test.org')
                assert (not var1296.closed)
                var2637 = ValueError()
                var1687.close.side_effect = var2637
                yield from var1296.close()
                assert var1296.closed
                assert (var1296.exception() is var2637)
                var1296._closed = False
                var1687.close.side_effect = asyncio.CancelledError()
                with pytest.raises(asyncio.CancelledError):
                    yield from var1296.close()

@asyncio.coroutine
def function1129(function539, function1058, arg1707, arg1443):
    var1326 = mock.Mock()
    var1326.status = 101
    var1326.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: ws_key, }
    with mock.patch('aiohttp.client.os') as var1496:
        with mock.patch('aiohttp.client.ClientSession.get') as var60:
            var1496.urandom.return_value = function1058
            var60.return_value = helpers.create_future(arg1707)
            var60.return_value.set_result(var1326)
            var1326 = yield from aiohttp.ClientSession(loop=arg1707).ws_connect('http://test.org')
            var1326._writer._closing = True
            arg1443.spy(ws_logger, 'warning')
            for (var2255, var495) in ((var1326.ping, ()), (var1326.pong, ()), (var1326.send_str, ('s',)), (var1326.send_bytes, (b'b',)), (var1326.send_json, ({},))):
                var2255(*var495)
                assert ws_logger.warning.called
                ws_logger.warning.reset_mock()

@asyncio.coroutine
def function957(function539, function1058, arg95):
    var390 = mock.Mock()
    var390.status = 101
    var390.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: ws_key, }
    with mock.patch('aiohttp.client.WebSocketWriter') as var4401:
        with mock.patch('aiohttp.client.os') as var3432:
            with mock.patch('aiohttp.client.ClientSession.get') as var1628:
                var3432.urandom.return_value = function1058
                var1628.return_value = helpers.create_future(arg95)
                var1628.return_value.set_result(var390)
                var4401.return_value = mock.Mock()
                var390 = yield from aiohttp.ClientSession(loop=arg95).ws_connect('http://test.org')
                pytest.raises(TypeError, var390.send_str, b's')
                pytest.raises(TypeError, var390.send_bytes, 'b')
                pytest.raises(TypeError, var390.send_json, set())

@asyncio.coroutine
def function2615(function539, function1058, arg1452):
    var2005 = mock.Mock()
    var2005.status = 101
    var2005.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: ws_key, }
    with mock.patch('aiohttp.client.WebSocketWriter') as var2694:
        with mock.patch('aiohttp.client.os') as var4340:
            with mock.patch('aiohttp.client.ClientSession.get') as var3884:
                var4340.urandom.return_value = function1058
                var3884.return_value = helpers.create_future(arg1452)
                var3884.return_value.set_result(var2005)
                var2694.return_value = mock.Mock()
                var3898 = aiohttp.ClientSession(loop=arg1452)
                var3140 = yield from var3898.ws_connect('http://test.org')
                var304 = ValueError()
                var3140._reader.set_exception(var304)
                var1275 = yield from var3140.receive()
                assert (var1275.type == aiohttp.WSMsgType.ERROR)
                assert (var1275.type is var1275.tp)
                assert (var3140.exception() is var304)
                var3898.close()

@asyncio.coroutine
def function1826(arg1150):
    var1607 = client.ClientWebSocketResponse(mock.Mock(), mock.Mock(), mock.Mock(), mock.Mock(), 10.0, True, True, arg1150)
    var1607._waiting = True
    with pytest.raises(RuntimeError):
        yield from var1607.receive()

@asyncio.coroutine
def function224(arg236, function539, function1058):
    var1447 = mock.Mock()
    var1447.status = 500
    var1447.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: ws_key, }
    with mock.patch('aiohttp.client.os') as var2656:
        with mock.patch('aiohttp.client.ClientSession.get') as var3482:
            var2656.urandom.return_value = function1058
            var3482.return_value = helpers.create_future(arg236)
            var3482.return_value.set_result(var1447)
            with pytest.raises(client.WSServerHandshakeError):
                yield from aiohttp.ClientSession(loop=arg236).ws_connect('http://test.org', protocols=('t1', 't2', 'chat'))
            var1447.close.assert_called_with()

@asyncio.coroutine
def function1247(function539, arg461, function1058):
    var3647 = mock.Mock()
    var3647.status = 101
    var3647.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: ws_key, hdrs.SEC_WEBSOCKET_PROTOCOL: 'other,another', }
    with mock.patch('aiohttp.client.os') as var2941:
        with mock.patch('aiohttp.client.ClientSession.get') as var2161:
            var2941.urandom.return_value = function1058
            var2161.return_value = helpers.create_future(arg461)
            var2161.return_value.set_result(var3647)
            var2190 = yield from aiohttp.ClientSession(loop=arg461).ws_connect('http://test.org', protocols=('t1', 't2', 'chat'))
    assert (var2190.protocol is None)

@asyncio.coroutine
def function463(function539, arg2031, function1058):
    var4179 = mock.Mock()
    var4179.status = 101
    var4179.headers = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_ACCEPT: ws_key, hdrs.SEC_WEBSOCKET_PROTOCOL: 'other,another', }
    with mock.patch('aiohttp.client.os') as var1009:
        with mock.patch('aiohttp.client.ClientSession.get') as var110:
            var1009.urandom.return_value = function1058
            var110.return_value = helpers.create_future(arg2031)
            var110.return_value.set_result(var4179)
            var2855 = aiohttp.TCPConnector(loop=arg2031, force_close=True)
            var2565 = yield from aiohttp.ClientSession(connector=var2855, loop=arg2031).ws_connect('http://test.org', protocols=('t1', 't2', 'chat'))
    assert (var2565.protocol is None)
    del res