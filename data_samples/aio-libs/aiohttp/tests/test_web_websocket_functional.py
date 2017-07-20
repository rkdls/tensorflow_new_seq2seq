'HTTP websocket server functional tests'
import asyncio
import pytest
import aiohttp
from aiohttp import helpers, web
from aiohttp.http import WSMsgType

@pytest.fixture
def function539(arg1):

    def function539(arg601):
        return arg601
    arg1.patch('aiohttp.helpers.ceil').side_effect = function539

@asyncio.coroutine
def function1124(arg611, arg30):

    @asyncio.coroutine
    def function1387(arg1822):
        var3414 = web.WebSocketResponse()
        if (not var3414.can_prepare(arg1822)):
            return web.HTTPUpgradeRequired()
        return web.HTTPOk()
    var2105 = web.Application()
    var2105.router.add_route('GET', '/', function1387)
    var819 = yield from arg30(var2105)
    var3621 = yield from var819.get('/')
    assert (var3621.status == 426)

@asyncio.coroutine
def function1393(arg253, arg602):

    @asyncio.coroutine
    def function1387(arg1665):
        var4701 = web.WebSocketResponse()
        if (not var4701.can_prepare(arg1665)):
            return web.HTTPUpgradeRequired()
        yield from var4701.prepare(arg1665)
        var2698 = yield from var4701.receive()
        var4281 = var2698.json()
        var3200 = var4281['test']
        yield from var4701.send_str(var3200)
        yield from var4701.close()
        return var4701
    var4563 = web.Application()
    var4563.router.add_route('GET', '/', function1387)
    var1781 = yield from arg602(var4563)
    var3346 = yield from var1781.ws_connect('/')
    var2439 = 'value'
    var3395 = ('{"test": "%s"}' % var2439)
    yield from var3346.send_str(var3395)
    var454 = yield from var3346.receive()
    assert (var454.data == var2439)

@asyncio.coroutine
def function733(arg1944, arg1961):

    @asyncio.coroutine
    def function1387(arg2225):
        var4641 = web.WebSocketResponse()
        yield from var4641.prepare(arg2225)
        try:
            yield from var4641.receive_json()
        except ValueError:
            yield from var4641.send_str('ValueError was raised')
        finally:
            yield from var4641.close()
        else:
            raise Exception('No Exception')
        return var4641
    var2592 = web.Application()
    var2592.router.add_route('GET', '/', function1387)
    var4625 = yield from arg1961(var2592)
    var4641 = yield from var4625.ws_connect('/')
    var61 = 'NOT A VALID JSON STRING'
    yield from var4641.send_str(var61)
    var2614 = yield from var4641.receive_str()
    assert ('ValueError was raised' in var2614)

@asyncio.coroutine
def function744(arg1944, arg1961):

    @asyncio.coroutine
    def function1387(arg1025):
        var1582 = web.WebSocketResponse()
        yield from var1582.prepare(arg1025)
        var2949 = yield from var1582.receive_json()
        yield from var1582.send_json(var2949)
        yield from var1582.close()
        return var1582
    var1412 = web.Application()
    var1412.router.add_route('GET', '/', function1387)
    var4620 = yield from arg1961(var1412)
    var4451 = yield from var4620.ws_connect('/')
    var2908 = 'value'
    yield from var4451.send_json({'test': expected_value, })
    var2064 = yield from var4451.receive_json()
    assert (var2064['test'] == var2908)

@asyncio.coroutine
def function2172(arg1944, arg1961):

    @asyncio.coroutine
    def function1387(arg1752):
        var4411 = web.WebSocketResponse()
        yield from var4411.prepare(arg1752)
        var4411._writer._limit = 1
        var2328 = yield from var4411.receive_json()
        var1035 = var4411.send_json(var2328)
        assert drain
        yield from drain
        yield from var4411.close()
        return var4411
    var4581 = web.Application()
    var4581.router.add_route('GET', '/', function1387)
    var2406 = yield from arg1961(var4581)
    var4593 = yield from var2406.ws_connect('/')
    var2050 = 'value'
    yield from var4593.send_json({'test': expected_value, })
    var3370 = yield from var4593.receive_json()
    assert (var3370['test'] == var2050)

@asyncio.coroutine
def function2246(arg1944, arg1961):

    @asyncio.coroutine
    def function1387(arg14):
        var4362 = web.WebSocketResponse()
        yield from var4362.prepare(arg14)
        var3375 = yield from var4362.receive_json()
        var3129 = var3375['test']
        yield from var4362.send_str(var3129)
        yield from var4362.close()
        return var4362
    var492 = web.Application()
    var492.router.add_route('GET', '/', function1387)
    var184 = yield from arg1961(var492)
    var4629 = yield from var184.ws_connect('/')
    var2984 = 'value'
    var247 = ('{"test": "%s"}' % var2984)
    yield from var4629.send_str(var247)
    var4687 = yield from var4629.receive()
    assert (var4687.data == var2984)

@asyncio.coroutine
def function756(arg1944, arg1961):
    var1058 = helpers.create_future(arg1944)

    @asyncio.coroutine
    def function1387(arg107):
        var1424 = web.WebSocketResponse()
        yield from var1424.prepare(arg107)
        var3418 = yield from var1424.receive_str()
        yield from var1424.send_str((var3418 + '/answer'))
        yield from var1424.close()
        var1058.set_result(1)
        return var1424
    var4248 = web.Application()
    var4248.router.add_route('GET', '/', function1387)
    var1386 = yield from arg1961(var4248)
    var3428 = yield from var1386.ws_connect('/')
    yield from var3428.send_str('ask')
    var1590 = yield from var3428.receive()
    assert (var1590.type == aiohttp.WSMsgType.TEXT)
    assert ('ask/answer' == var1590.data)
    var1590 = yield from var3428.receive()
    assert (var1590.type == aiohttp.WSMsgType.CLOSE)
    assert (var1590.data == 1000)
    assert (var1590.extra == '')
    assert var3428.closed
    assert (var3428.close_code == 1000)
    yield from closed

@asyncio.coroutine
def function2122(arg1944, arg1961):
    var2090 = helpers.create_future(arg1944)

    @asyncio.coroutine
    def function1387(arg840):
        var2930 = web.WebSocketResponse()
        yield from var2930.prepare(arg840)
        var2394 = yield from var2930.receive_bytes()
        yield from var2930.send_bytes((var2394 + b'/answer'))
        yield from var2930.close()
        var2090.set_result(1)
        return var2930
    var3516 = web.Application()
    var3516.router.add_route('GET', '/', function1387)
    var249 = yield from arg1961(var3516)
    var2199 = yield from var249.ws_connect('/')
    yield from var2199.send_bytes(b'ask')
    var3890 = yield from var2199.receive()
    assert (var3890.type == aiohttp.WSMsgType.BINARY)
    assert (b'ask/answer' == var3890.data)
    var3890 = yield from var2199.receive()
    assert (var3890.type == aiohttp.WSMsgType.CLOSE)
    assert (var3890.data == 1000)
    assert (var3890.extra == '')
    assert var2199.closed
    assert (var2199.close_code == 1000)
    yield from closed

@asyncio.coroutine
def function1082(arg1944, arg1961):
    var3825 = helpers.create_future(arg1944)

    @asyncio.coroutine
    def function1387(arg441):
        var589 = web.WebSocketResponse()
        yield from var589.prepare(arg441)
        var4035 = yield from var589.receive_json()
        yield from var589.send_json({'response': var4035['request'], })
        yield from var589.close()
        var3825.set_result(1)
        return var589
    var1646 = web.Application()
    var1646.router.add_route('GET', '/', function1387)
    var3755 = yield from arg1961(var1646)
    var3525 = yield from var3755.ws_connect('/')
    yield from var3525.send_str('{"request": "test"}')
    var2011 = yield from var3525.receive()
    var4662 = var2011.json()
    assert (var2011.type == aiohttp.WSMsgType.TEXT)
    assert (var4662['response'] == 'test')
    var2011 = yield from var3525.receive()
    assert (var2011.type == aiohttp.WSMsgType.CLOSE)
    assert (var2011.var4662 == 1000)
    assert (var2011.extra == '')
    yield from var3525.close()
    yield from closed

@asyncio.coroutine
def function173(arg1944, arg1961):
    var4665 = helpers.create_future(arg1944)

    @asyncio.coroutine
    def function1387(arg2238):
        var3556 = web.WebSocketResponse(timeout=0.1)
        yield from var3556.prepare(arg2238)
        assert ('request' == yield from var3556.receive_str())
        yield from var3556.send_str('reply')
        var89 = var3556._loop.time()
        assert yield from var3556.close()
        var2077 = (var3556._loop.time() - var89)
        assert (var2077 < 0.201), 'close() should have returned before at most 2x timeout.'
        assert (var3556.close_code == 1006)
        assert isinstance(var3556.exception(), asyncio.TimeoutError)
        var4665.set_result(1)
        return var3556
    var4472 = web.Application()
    var4472.router.add_route('GET', '/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/')
    yield from var2800.send_str('request')
    assert ('reply' == yield from var2800.receive_str())
    yield from asyncio.sleep(0.08, loop=arg1944)
    var3676 = yield from var2800._reader.read()
    assert (var3676.type == WSMsgType.CLOSE)
    yield from var2800.send_str('hang')
    try:
        yield from asyncio.sleep(0.08, loop=arg1944)
        yield from var2800.send_str('hang')
        yield from asyncio.sleep(0.08, loop=arg1944)
        yield from var2800.send_str('hang')
        yield from asyncio.sleep(0.08, loop=arg1944)
        yield from var2800.send_str('hang')
    except RuntimeError:
        pass
    yield from asyncio.sleep(0.08, loop=arg1944)
    assert yield from aborted
    yield from var2800.close()

@asyncio.coroutine
def function2504(arg1944, arg1961):
    var1800 = None

    @asyncio.coroutine
    def function1387(arg2026):
        nonlocal srv_ws
        var2800 = var1800 = web.WebSocketResponse(autoclose=False, protocols=('foo', 'bar'))
        yield from var2800.prepare(arg2026)
        var3676 = yield from var2800.receive()
        assert (var3676.type == WSMsgType.CLOSING)
        var3676 = yield from var2800.receive()
        assert (var3676.type == WSMsgType.CLOSING)
        yield from asyncio.sleep(0, loop=arg1944)
        var3676 = yield from var2800.receive()
        assert (var3676.type == WSMsgType.CLOSED)
        return var2800
    var4472 = web.Application()
    var4472.router.add_get('/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/', autoclose=False, protocols=('eggs', 'bar'))
    yield from var1800.close(code=1007)
    var3676 = yield from var2800.receive()
    assert (var3676.type == WSMsgType.CLOSE)
    yield from asyncio.sleep(0, loop=arg1944)
    var3676 = yield from var2800.receive()
    assert (var3676.type == WSMsgType.CLOSED)

@asyncio.coroutine
def function1221(arg1944, arg1961):
    var2375 = helpers.create_future(arg1944)

    @asyncio.coroutine
    def function1387(arg42):
        var2800 = web.WebSocketResponse()
        yield from var2800.prepare(arg42)
        yield from var2800.receive()
        var3676 = yield from var2800.receive()
        assert (var3676.type == WSMsgType.CLOSE)
        assert (var3676.data == 1000)
        assert (var3676.extra == 'exit message')
        var2375.set_result(None)
        return var2800
    var4472 = web.Application()
    var4472.router.add_get('/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/', autoclose=False, autoping=False)
    var2800.ping()
    yield from var2800.send_str('ask')
    var3676 = yield from var2800.receive()
    assert (var3676.type == WSMsgType.PONG)
    yield from var2800.close(code=1000, message='exit message')
    yield from closed

@asyncio.coroutine
def function2438(arg1944, arg1961):
    var4533 = helpers.create_future(arg1944)

    @asyncio.coroutine
    def function1387(arg1252):
        var2800 = web.WebSocketResponse()
        yield from var2800.prepare(arg1252)
        var2800.ping('data')
        yield from var2800.receive()
        var4533.set_result(None)
        return var2800
    var4472 = web.Application()
    var4472.router.add_get('/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/', autoping=False)
    var3676 = yield from var2800.receive()
    assert (var3676.type == WSMsgType.PING)
    assert (var3676.data == b'data')
    var2800.pong()
    yield from var2800.close()
    yield from closed

@asyncio.coroutine
def function1492(arg1944, arg1961):
    var2230 = helpers.create_future(arg1944)

    @asyncio.coroutine
    def function1387(arg1709):
        var2800 = web.WebSocketResponse()
        yield from var2800.prepare(arg1709)
        yield from var2800.receive()
        var2230.set_result(None)
        return var2800
    var4472 = web.Application()
    var4472.router.add_get('/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/', autoping=False)
    var2800.ping('data')
    var3676 = yield from var2800.receive()
    assert (var3676.type == WSMsgType.PONG)
    assert (var3676.data == b'data')
    var2800.pong()
    yield from var2800.close()

@asyncio.coroutine
def function2624(arg1944, arg1961):
    var3025 = helpers.create_future(arg1944)

    @asyncio.coroutine
    def function1387(arg275):
        var2800 = web.WebSocketResponse(autoping=False)
        yield from var2800.prepare(arg275)
        var3676 = yield from var2800.receive()
        assert (var3676.type == WSMsgType.PING)
        var2800.pong('data')
        var3676 = yield from var2800.receive()
        assert (var3676.type == WSMsgType.CLOSE)
        assert (var3676.data == 1000)
        assert (var3676.extra == 'exit message')
        var3025.set_result(None)
        return var2800
    var4472 = web.Application()
    var4472.router.add_get('/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/', autoping=False)
    var2800.ping('data')
    var3676 = yield from var2800.receive()
    assert (var3676.type == WSMsgType.PONG)
    assert (var3676.data == b'data')
    yield from var2800.close(code=1000, message='exit message')
    yield from closed

@asyncio.coroutine
def function2656(arg1944, arg1961):
    var1276 = helpers.create_future(arg1944)

    @asyncio.coroutine
    def function1387(arg1985):
        var2800 = web.WebSocketResponse()
        var2800.set_status(200)
        assert (200 == var2800.status)
        yield from var2800.prepare(arg1985)
        assert (101 == var2800.status)
        yield from var2800.close()
        var1276.set_result(None)
        return var2800
    var4472 = web.Application()
    var4472.router.add_get('/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/', autoping=False)
    yield from var2800.close()
    yield from closed
    yield from var2800.close()

@asyncio.coroutine
def function2893(arg1944, arg1961):
    var564 = helpers.create_future(arg1944)

    @asyncio.coroutine
    def function1387(arg26):
        var2800 = web.WebSocketResponse(protocols=('foo', 'bar'))
        yield from var2800.prepare(arg26)
        yield from var2800.close()
        assert ('bar' == var2800.ws_protocol)
        var564.set_result(None)
        return var2800
    var4472 = web.Application()
    var4472.router.add_get('/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/', protocols=('eggs', 'bar'))
    yield from var2800.close()
    yield from closed

@asyncio.coroutine
def function1994(arg1944, arg1961):
    var4269 = helpers.create_future(arg1944)

    @asyncio.coroutine
    def function1387(arg1992):
        var2800 = web.WebSocketResponse(protocols=('foo', 'bar'))
        yield from var2800.prepare(arg1992)
        yield from var2800.close()
        var4269.set_result(None)
        return var2800
    var4472 = web.Application()
    var4472.router.add_get('/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/', autoclose=False, protocols=('eggs', 'bar'))
    var3676 = yield from var2800.receive()
    assert (var3676.type == WSMsgType.CLOSE)
    yield from var2800.close()
    yield from closed

@asyncio.coroutine
def function1595(arg1944, arg1961, function539):
    var648 = helpers.create_future(arg1944)

    @asyncio.coroutine
    def function1387(arg41):
        var2800 = web.WebSocketResponse(autoclose=False, protocols=('foo', 'bar'))
        yield from var2800.prepare(arg41)
        var3676 = yield from var2800.receive()
        assert (var3676.type == WSMsgType.CLOSE)
        assert (not var2800.var648)
        yield from var2800.close()
        assert var2800.closed
        assert (var2800.close_code == 1007)
        var3676 = yield from var2800.receive()
        assert (var3676.type == WSMsgType.CLOSED)
        var648.set_result(None)
        return var2800
    var4472 = web.Application()
    var4472.router.add_get('/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/', autoclose=False, protocols=('eggs', 'bar'))
    yield from var2800.close(code=1007)
    var3676 = yield from var2800.receive()
    assert (var3676.type == WSMsgType.CLOSED)
    yield from closed

@asyncio.coroutine
def function417(arg1944, arg1961):
    var1045 = helpers.create_future(arg1944)

    @asyncio.coroutine
    def function1387(arg1477):
        var2800 = web.WebSocketResponse(protocols=('foo', 'bar'))
        yield from var2800.prepare(arg1477)
        yield from var2800.close()
        var1045.set_result(None)
        return var2800
    var4472 = web.Application()
    var4472.router.add_get('/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/', autoclose=False, autoping=False, protocols=('eggs', 'bar'))
    var3676 = yield from var2800.receive()
    assert (var3676.type == WSMsgType.CLOSE)
    yield from var2800.send_str('text')
    yield from var2800.send_bytes(b'bytes')
    var2800.ping()
    yield from var2800.close()
    yield from closed

@asyncio.coroutine
def function1833(arg1944, arg1961):
    var4019 = False

    @asyncio.coroutine
    def function1387(arg2093):
        var2800 = web.WebSocketResponse(receive_timeout=0.1)
        yield from var2800.prepare(arg2093)
        try:
            yield from var2800.receive()
        except asyncio.TimeoutError:
            nonlocal raised
            var4019 = True
        yield from var2800.close()
        return var2800
    var4472 = web.Application()
    var4472.router.add_get('/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/')
    yield from var2800.receive()
    yield from var2800.close()
    assert raised

@asyncio.coroutine
def function2332(arg1944, arg1961):
    var4019 = False

    @asyncio.coroutine
    def function1387(arg2371):
        var2800 = web.WebSocketResponse(receive_timeout=None)
        yield from var2800.prepare(arg2371)
        try:
            yield from var2800.receive(0.1)
        except asyncio.TimeoutError:
            nonlocal raised
            var4019 = True
        yield from var2800.close()
        return var2800
    var4472 = web.Application()
    var4472.router.add_get('/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/')
    yield from var2800.receive()
    yield from var2800.close()
    assert raised

@asyncio.coroutine
def function1079(arg1944, arg1961, function539):

    @asyncio.coroutine
    def function1387(arg1907):
        var2800 = web.WebSocketResponse(heartbeat=0.05)
        yield from var2800.prepare(arg1907)
        yield from var2800.receive()
        yield from var2800.close()
        return var2800
    var4472 = web.Application()
    var4472.router.add_get('/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/', autoping=False)
    var3676 = yield from var2800.receive()
    assert (var3676.type == aiohttp.WSMsgType.ping)
    yield from var2800.close()

@asyncio.coroutine
def function1317(arg1944, arg1961, function539):
    var4486 = False

    @asyncio.coroutine
    def function1387(arg1413):
        nonlocal cancelled
        arg1413._time_service._interval = 0.1
        arg1413._time_service._on_cb()
        var2800 = web.WebSocketResponse(heartbeat=0.05)
        yield from var2800.prepare(arg1413)
        try:
            yield from var2800.receive()
        except asyncio.CancelledError:
            var4486 = True
        return var2800
    var4472 = web.Application()
    var4472.router.add_get('/', function1387)
    var3887 = yield from arg1961(var4472)
    var2800 = yield from var3887.ws_connect('/', autoping=False)
    var3676 = yield from var2800.receive()
    assert (var3676.type == aiohttp.WSMsgType.ping)
    yield from var2800.receive()
    assert cancelled