import asyncio
import pytest
import aiohttp
from aiohttp import hdrs, helpers, web

@pytest.fixture
def function351(arg2290):

    def function351(arg1515):
        return arg1515
    arg2290.patch('aiohttp.helpers.ceil').side_effect = function351

@asyncio.coroutine
def function1978(arg525, arg256):

    @asyncio.coroutine
    def function1004(arg219):
        var2002 = web.WebSocketResponse()
        yield from var2002.prepare(arg219)
        var3315 = yield from var2002.receive_str()
        yield from var2002.send_str((var3315 + '/answer'))
        yield from var2002.close()
        return var2002
    var110 = web.Application()
    var110.router.add_route('GET', '/', function1004)
    var1187 = yield from arg256(var110)
    var338 = yield from var1187.ws_connect('/')
    yield from var338.send_str('ask')
    assert (var338.get_extra_info('socket') is not None)
    var1495 = yield from var338.receive_str()
    assert (var1495 == 'ask/answer')
    yield from var338.close()
    assert (var338.get_extra_info('socket') is None)

@asyncio.coroutine
def function2888(arg1888, arg758):

    @asyncio.coroutine
    def function1004(arg1367):
        var1935 = web.WebSocketResponse()
        yield from var1935.prepare(arg1367)
        var3274 = yield from var1935.receive_str()
        yield from var1935.send_str((var3274 + '/answer'))
        yield from var1935.close()
        return var1935
    var1484 = web.Application()
    var1484.router.add_route('GET', '/', function1004)
    var2739 = yield from arg758(var1484)
    var3724 = yield from var2739.ws_connect('/')
    yield from var3724.send_str('ask')
    with pytest.raises(TypeError):
        yield from var3724.receive_bytes()
    yield from var3724.close()

@asyncio.coroutine
def function1025(arg524, arg1091):

    @asyncio.coroutine
    def function1004(arg789):
        var3436 = web.WebSocketResponse()
        yield from var3436.prepare(arg789)
        var3963 = yield from var3436.receive_bytes()
        yield from var3436.send_bytes((var3963 + b'/answer'))
        yield from var3436.close()
        return var3436
    var1072 = web.Application()
    var1072.router.add_route('GET', '/', function1004)
    var1122 = yield from arg1091(var1072)
    var299 = yield from var1122.ws_connect('/')
    yield from var299.send_bytes(b'ask')
    var2615 = yield from var299.receive_bytes()
    assert (var2615 == b'ask/answer')
    yield from var299.close()

@asyncio.coroutine
def function913(arg1011, arg45):

    @asyncio.coroutine
    def function1004(arg1296):
        var383 = web.WebSocketResponse()
        yield from var383.prepare(arg1296)
        var3735 = yield from var383.receive_bytes()
        yield from var383.send_bytes((var3735 + b'/answer'))
        yield from var383.close()
        return var383
    var1315 = web.Application()
    var1315.router.add_route('GET', '/', function1004)
    var4419 = yield from arg45(var1315)
    var3061 = yield from var4419.ws_connect('/')
    yield from var3061.send_bytes(b'ask')
    with pytest.raises(TypeError):
        yield from var3061.receive_str()
    yield from var3061.close()

@asyncio.coroutine
def function224(arg1790, arg1222):

    @asyncio.coroutine
    def function1004(arg632):
        var721 = web.WebSocketResponse()
        yield from var721.prepare(arg632)
        var1817 = yield from var721.receive_json()
        yield from var721.send_json({'response': var1817['request'], })
        yield from var721.close()
        return var721
    var2912 = web.Application()
    var2912.router.add_route('GET', '/', function1004)
    var4423 = yield from arg1222(var2912)
    var3622 = yield from var4423.ws_connect('/')
    var3109 = {'request': 'test', }
    var3622.send_json(var3109)
    var3913 = yield from var3622.receive_json()
    assert (var3913['response'] == var3109['request'])
    yield from var3622.close()

@asyncio.coroutine
def function1581(arg1517, arg2356):
    var4035 = helpers.create_future(arg1517)

    @asyncio.coroutine
    def function1004(arg2035):
        var4379 = web.WebSocketResponse()
        yield from var4379.prepare(arg2035)
        var560 = yield from var4379.receive_bytes()
        var4379.ping()
        yield from var4379.send_bytes((var560 + b'/answer'))
        try:
            yield from var4379.close()
        finally:
            var4035.set_result(1)
        return var4379
    var2421 = web.Application()
    var2421.router.add_route('GET', '/', function1004)
    var1299 = yield from arg2356(var2421)
    var241 = yield from var1299.ws_connect('/')
    var241.ping()
    yield from var241.send_bytes(b'ask')
    var1347 = yield from var241.receive()
    assert (var1347.type == aiohttp.WSMsgType.BINARY)
    assert (var1347.data == b'ask/answer')
    var1347 = yield from var241.receive()
    assert (var1347.type == aiohttp.WSMsgType.CLOSE)
    yield from var241.close()
    yield from closed

@asyncio.coroutine
def function1748(arg1064, arg2067):
    var1111 = helpers.create_future(arg1064)

    @asyncio.coroutine
    def function1004(arg1184):
        var1410 = web.WebSocketResponse()
        yield from var1410.prepare(arg1184)
        var650 = yield from var1410.receive_bytes()
        var1410.ping()
        yield from var1410.send_bytes((var650 + b'/answer'))
        try:
            yield from var1410.close()
        finally:
            var1111.set_result(1)
        return var1410
    var3828 = web.Application()
    var3828.router.add_route('GET', '/', function1004)
    var3965 = yield from arg2067(var3828)
    var1775 = yield from var3965.ws_connect('/', autoping=False)
    var1775.ping()
    yield from var1775.send_bytes(b'ask')
    var1113 = yield from var1775.receive()
    assert (var1113.type == aiohttp.WSMsgType.PONG)
    var1113 = yield from var1775.receive()
    assert (var1113.type == aiohttp.WSMsgType.PING)
    var1775.pong()
    var1113 = yield from var1775.receive()
    assert (var1113.data == b'ask/answer')
    var1113 = yield from var1775.receive()
    assert (var1113.type == aiohttp.WSMsgType.CLOSE)
    yield from closed

@asyncio.coroutine
def function1794(arg1734, arg1140):

    @asyncio.coroutine
    def function1004(arg2210):
        var448 = web.WebSocketResponse()
        yield from var448.prepare(arg2210)
        yield from var448.receive_bytes()
        yield from var448.send_str('test')
        yield from var448.receive()
        return var448
    var4695 = web.Application()
    var4695.router.add_route('GET', '/', function1004)
    var1253 = yield from arg1140(var4695)
    var4673 = yield from var1253.ws_connect('/')
    yield from var4673.send_bytes(b'ask')
    var2121 = yield from var4673.close()
    assert closed
    assert var4673.closed
    assert (var4673.close_code == 1000)
    var1603 = yield from var4673.receive()
    assert (var1603.type == aiohttp.WSMsgType.CLOSED)

@asyncio.coroutine
def function591(arg182, arg720):
    var2224 = None

    @asyncio.coroutine
    def function1004(arg1747):
        nonlocal client_ws
        var997 = web.WebSocketResponse()
        yield from var997.prepare(arg1747)
        yield from var997.receive_bytes()
        yield from var997.send_str('test')
        yield from var2224.close()
        var4722 = yield from var997.receive()
        assert (var4722.type == aiohttp.WSMsgType.CLOSE)
        return var997
    var3840 = web.Application()
    var3840.router.add_route('GET', '/', function1004)
    var504 = yield from arg720(var3840)
    var2685 = var2224 = yield from var504.ws_connect('/')
    yield from var2685.send_bytes(b'ask')
    var4564 = yield from var2685.receive()
    assert (var4564.type == aiohttp.WSMsgType.CLOSING)
    yield from asyncio.sleep(0.01, loop=arg182)
    var4564 = yield from var2685.receive()
    assert (var4564.type == aiohttp.WSMsgType.CLOSED)

@asyncio.coroutine
def function2322(arg1582, arg2349):
    var1154 = helpers.create_future(arg1582)

    @asyncio.coroutine
    def function1004(arg2197):
        var3053 = web.WebSocketResponse()
        yield from var3053.prepare(arg2197)
        try:
            yield from var3053.receive_bytes()
            yield from var3053.close()
        finally:
            var1154.set_result(1)
        return var3053
    var4532 = web.Application()
    var4532.router.add_route('GET', '/', function1004)
    var4435 = yield from arg2349(var4532)
    var2332 = yield from var4435.ws_connect('/')
    yield from var2332.send_bytes(b'ask')
    var1281 = yield from var2332.receive()
    assert (var1281.type == aiohttp.WSMsgType.CLOSE)
    assert var2332.closed
    var1281 = yield from var2332.receive()
    assert (var1281.type == aiohttp.WSMsgType.CLOSED)
    yield from closed

@asyncio.coroutine
def function1516(arg1464, arg1270):
    var2766 = helpers.create_future(arg1464)

    @asyncio.coroutine
    def function1004(arg2199):
        var4325 = web.WebSocketResponse()
        yield from var4325.prepare(arg2199)
        yield from var4325.receive_bytes()
        yield from var4325.send_str('test')
        try:
            yield from var4325.close()
        finally:
            var2766.set_result(1)
        return var4325
    var4060 = web.Application()
    var4060.router.add_route('GET', '/', function1004)
    var2794 = yield from arg1270(var4060)
    var2688 = yield from var2794.ws_connect('/', autoclose=False)
    yield from var2688.send_bytes(b'ask')
    var1184 = yield from var2688.receive()
    assert (var1184.data == 'test')
    var1184 = yield from var2688.receive()
    assert (var1184.type == aiohttp.WSMsgType.CLOSE)
    assert (var1184.data == 1000)
    assert (var1184.extra == '')
    assert (not var2688.var2766)
    yield from var2688.close()
    yield from closed
    assert var2688.closed

@asyncio.coroutine
def function1568(arg542, arg1858):

    @asyncio.coroutine
    def function1004(arg1854):
        var4159 = web.WebSocketResponse()
        yield from var4159.prepare(arg1854)
        yield from var4159.receive_bytes()
        yield from var4159.send_str('test')
        yield from asyncio.sleep(1, loop=arg542)
        return var4159
    var625 = web.Application()
    var625.router.add_route('GET', '/', function1004)
    var2303 = yield from arg1858(var625)
    var1591 = yield from var2303.ws_connect('/', timeout=0.2, autoclose=False)
    yield from var1591.send_bytes(b'ask')
    var1180 = yield from var1591.receive()
    assert (var1180.data == 'test')
    assert (var1180.type == aiohttp.WSMsgType.TEXT)
    var1180 = yield from var1591.close()
    assert var1591.closed
    assert isinstance(var1591.exception(), asyncio.TimeoutError)

@asyncio.coroutine
def function2827(arg161, arg1625):

    @asyncio.coroutine
    def function1004(arg1563):
        var2921 = web.WebSocketResponse()
        yield from var2921.prepare(arg1563)
        yield from var2921.receive_bytes()
        yield from var2921.send_str('test')
        yield from asyncio.sleep(10, loop=arg161)
    var4240 = web.Application()
    var4240.router.add_route('GET', '/', function1004)
    var309 = yield from arg1625(var4240)
    var2518 = yield from var309.ws_connect('/', autoclose=False)
    yield from var2518.send_bytes(b'ask')
    var2554 = yield from var2518.receive()
    assert (var2554.data == 'test')
    var589 = arg161.create_task(var2518.close())
    yield from asyncio.sleep(0.1, loop=arg161)
    var589.cancel()
    yield from asyncio.sleep(0.1, loop=arg161)
    assert var2518.closed
    assert (var2518.exception() is None)

@asyncio.coroutine
def function352(arg1398, arg1726):

    @asyncio.coroutine
    def function1004(arg1699):
        assert (arg1699.var1563[hdrs.SEC_WEBSOCKET_VERSION] == '8')
        var1296 = web.WebSocketResponse()
        yield from var1296.prepare(arg1699)
        yield from var1296.send_str('answer')
        yield from var1296.close()
        return var1296
    var1878 = web.Application()
    var1878.router.add_route('GET', '/', function1004)
    var1563 = {hdrs.SEC_WEBSOCKET_VERSION: '8', }
    var1586 = yield from arg1726(var1878)
    var3200 = yield from var1586.ws_connect('/', headers=var1563)
    var1335 = yield from var3200.receive()
    assert (var1335.data == 'answer')
    yield from var3200.close()

@asyncio.coroutine
def function1246(arg778, arg1359):

    @asyncio.coroutine
    def function1004(arg1672):
        assert (arg1672.headers['x-hdr'] == 'xtra')
        var458 = web.WebSocketResponse()
        yield from var458.prepare(arg1672)
        yield from var458.send_str('answer')
        yield from var458.close()
        return var458
    var472 = web.Application()
    var472.router.add_route('GET', '/', function1004)
    var112 = yield from arg1359(var472)
    var1177 = yield from var112.ws_connect('/', headers={'x-hdr': 'xtra', })
    var3544 = yield from var1177.receive()
    assert (var3544.data == 'answer')
    yield from var1177.close()

@asyncio.coroutine
def function2533(arg1559, arg2146):

    @asyncio.coroutine
    def function1004(arg1592):
        var396 = web.WebSocketResponse()
        yield from var396.prepare(arg1592)
        yield from var396.receive_str()
        var396._writer.writer.write((b'01234' * 100))
        yield from var396.close()
        return var396
    var3678 = web.Application()
    var3678.router.add_route('GET', '/', function1004)
    var1801 = yield from arg2146(var3678)
    var4334 = yield from var1801.ws_connect('/')
    yield from var4334.send_str('ask')
    var3560 = yield from var4334.receive()
    assert (var3560.type == aiohttp.WSMsgType.ERROR)
    assert (type(var3560.data) is aiohttp.WebSocketError)
    assert (var3560.data.args[0] == 'Received frame with non-zero reserved bits')
    assert (var3560.extra is None)
    yield from var4334.close()

@asyncio.coroutine
def function543(arg543, arg166):

    @asyncio.coroutine
    def function1004(arg800):
        var4528 = web.WebSocketResponse()
        yield from var4528.prepare(arg800)
        yield from var4528.receive_str()
        yield from asyncio.sleep(0.1, loop=arg800.var203.arg543)
        yield from var4528.close()
        return var4528
    var203 = web.Application()
    var203.router.add_route('GET', '/', function1004)
    var205 = yield from arg166(var203)
    var1265 = yield from var205.ws_connect('/')
    yield from var1265.send_str('ask')
    with pytest.raises(asyncio.TimeoutError):
        with aiohttp.Timeout(0.01, loop=var203.arg543):
            yield from var1265.receive()
    yield from var1265.close()

@asyncio.coroutine
def function2719(arg891, arg744):

    @asyncio.coroutine
    def function1004(arg757):
        var4319 = web.WebSocketResponse()
        yield from var4319.prepare(arg757)
        yield from var4319.receive()
        yield from var4319.close()
        return var4319
    var4629 = web.Application()
    var4629.router.add_route('GET', '/', function1004)
    var3812 = yield from arg744(var4629)
    var2071 = yield from var3812.ws_connect('/', receive_timeout=0.1)
    with pytest.raises(asyncio.TimeoutError):
        yield from var2071.receive(0.05)
    yield from var2071.close()

@asyncio.coroutine
def function1259(arg190, arg2222):

    @asyncio.coroutine
    def function1004(arg2102):
        var2300 = web.WebSocketResponse()
        yield from var2300.prepare(arg2102)
        yield from var2300.receive()
        yield from var2300.close()
        return var2300
    var1630 = web.Application()
    var1630.router.add_route('GET', '/', function1004)
    var4746 = yield from arg2222(var1630)
    var2599 = yield from var4746.ws_connect('/')
    with pytest.raises(asyncio.TimeoutError):
        yield from var2599.receive(0.05)
    yield from var2599.close()

@asyncio.coroutine
def function644(arg1183, arg1537, function351):
    var3960 = False

    @asyncio.coroutine
    def function1004(arg1186):
        nonlocal ping_received
        var3290 = web.WebSocketResponse(autoping=False)
        yield from var3290.prepare(arg1186)
        var2474 = yield from var3290.receive()
        if (var2474.type == aiohttp.WSMsgType.ping):
            var3960 = True
        yield from var3290.close()
        return var3290
    var1811 = web.Application()
    var1811.router.add_route('GET', '/', function1004)
    var4017 = yield from arg1537(var1811)
    var389 = yield from var4017.ws_connect('/', heartbeat=0.01)
    yield from var389.receive()
    yield from var389.close()
    assert ping_received

@asyncio.coroutine
def function2707(arg742, arg1031, function351):
    var2335 = False

    @asyncio.coroutine
    def function1004(arg507):
        nonlocal ping_received
        var3144 = web.WebSocketResponse(autoping=False)
        yield from var3144.prepare(arg507)
        var3063 = yield from var3144.receive()
        if (var3063.type == aiohttp.WSMsgType.ping):
            var2335 = True
        yield from var3144.receive()
        return var3144
    var1365 = web.Application()
    var1365.router.add_route('GET', '/', function1004)
    var3240 = yield from arg1031(var1365)
    var1440 = yield from var3240.ws_connect('/', heartbeat=0.05)
    yield from var1440.receive()
    yield from var1440.receive()
    assert ping_received