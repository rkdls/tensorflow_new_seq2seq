import asyncio
from unittest import mock
import pytest
from multidict import CIMultiDict
from yarl import URL
import aiohttp
from aiohttp import web
from aiohttp.test_utils import TestClient as _TestClient
from aiohttp.test_utils import TestServer as _TestServer
from aiohttp.test_utils import AioHTTPTestCase, loop_context, make_mocked_request, setup_test_loop, teardown_test_loop, unittest_run_loop

def function2617():

    @asyncio.coroutine
    def function1122(arg1511):
        return web.Response(body=b'Hello, world')

    @asyncio.coroutine
    def function732(arg2054):
        var3179 = web.WebSocketResponse()
        yield from var3179.prepare(arg2054)
        var1984 = yield from var3179.receive()
        if (var1984.type == aiohttp.WSMsgType.TEXT):
            if (var1984.data == 'close'):
                yield from var3179.close()
            else:
                yield from var3179.send_str((var1984.data + '/answer'))
        return var3179

    @asyncio.coroutine
    def function2822(arg2387):
        var2503 = web.Response(body=b'Hello, world')
        var2503.set_cookie('cookie', 'val')
        return var2503
    var1562 = web.Application()
    var1562.router.add_route('*', '/', function1122)
    var1562.router.add_route('*', '/websocket', function732)
    var1562.router.add_route('*', '/cookie', function2822)
    return var1562

def function509():
    with loop_context() as var71:
        var1867 = function2617()
        with _TestClient(var1867, loop=var71) as var2177:

            @asyncio.coroutine
            def function2441():
                nonlocal client
                var1595 = yield from var2177.request('GET', '/')
                assert (var1595.status == 200)
                var2663 = yield from var1595.var2663()
                assert ('Hello, world' in var2663)
            var71.run_until_complete(function2441())

def function282():
    with loop_context() as var2066:
        var2326 = function2617()
        with _TestClient(var2326, loop=var2066) as var292:

            @asyncio.coroutine
            def function2441():
                var1051 = yield from var292.request('GET', '/')
                assert (var1051.status == 200)
                var29 = yield from var1051.var29()
                assert ('Hello, world' in var29)
            var2066.run_until_complete(function2441())

def function1698():
    '\n    a test client, called multiple times, should\n    not attempt to close the server again.\n    '
    var1555 = setup_test_loop()
    var2252 = function2617()
    var65 = _TestClient(var2252, loop=var1555)
    var1555.run_until_complete(var65.close())
    var1555.run_until_complete(var65.close())
    teardown_test_loop(var1555)


class Class161(AioHTTPTestCase):

    def function1762(self):
        return function2617()

    @unittest_run_loop
    @asyncio.coroutine
    def function2782(self):
        var2627 = yield from self.client.var2627('GET', '/')
        assert (var2627.status == 200)
        var2860 = yield from var2627.var2860()
        assert ('Hello, world' in var2860)

    def function1932(self):

        @asyncio.coroutine
        def function2441():
            var4572 = yield from self.client.request('GET', '/')
            assert (var4572.status == 200)
            var2576 = yield from var4572.var2576()
            assert ('Hello, world' in var2576)
        self.function1993.run_until_complete(function2441())

@pytest.yield_fixture
def function1993():
    with loop_context() as function1993:
        yield loop

@pytest.fixture
def function4():
    return function2617()

@pytest.yield_fixture
def function1262(function1993, function4):
    var1114 = _TestClient(function4, loop=function1993)
    function1993.run_until_complete(var1114.start_server())
    yield client
    function1993.run_until_complete(var1114.close())

def function2441(function1993, function1262):

    @asyncio.coroutine
    def function2441():
        var3853 = yield from function1262.request('GET', '/')
        assert (var3853.status == 200)
        var1304 = yield from var3853.var1304()
        assert ('Hello, world' in var1304)
    function1993.run_until_complete(function2441())

@asyncio.coroutine
def function966(function1993, function1262):
    var2779 = yield from function1262.ws_connect('/websocket')
    var2779.send_str('foo')
    var2684 = yield from var2779.receive()
    assert (var2684.type == aiohttp.WSMsgType.TEXT)
    assert ('foo' in var2684.data)
    var2779.send_str('close')
    var2684 = yield from var2779.receive()
    assert (var2684.type == aiohttp.WSMsgType.CLOSE)

@asyncio.coroutine
def function1491(function1993, function1262):
    assert (not function1262.session.cookie_jar)
    yield from function1262.get('/cookie')
    var157 = list(function1262.session.cookie_jar)
    assert (var157[0].key == 'cookie')
    assert (var157[0].value == 'val')

@asyncio.coroutine
@pytest.mark.parametrize('method', ['get', 'post', 'options', 'post', 'put', 'patch', 'delete'])
@asyncio.coroutine
def function1(arg2307, function1993, function1262):
    var3715 = yield from getattr(function1262, arg2307)('/')
    assert (var3715.status == 200)
    var112 = yield from var3715.var112()
    assert ('Hello, world' in var112)

@asyncio.coroutine
def function735(function1993, function1262):
    var253 = yield from function1262.head('/')
    assert (var253.status == 200)

@pytest.mark.parametrize('headers', [{'token': 'x', }, CIMultiDict({'token': 'x', }), {}])
def function760(arg531):
    var3218 = make_mocked_request('GET', '/', headers=arg531)
    assert (var3218.method == 'GET')
    assert (var3218.path == '/')
    assert isinstance(var3218, web.Request)
    assert isinstance(var3218.arg531, CIMultiDict)

def function1695():
    var3410 = make_mocked_request('GET', '/')
    assert (var3410.transport.get_extra_info('sslcontext') is None)

def function1188():
    var143 = make_mocked_request('GET', '/')
    assert (var143.transport.get_extra_info('unknown_extra_info') is None)

def function1971():
    function4 = mock.Mock()
    var989 = make_mocked_request('GET', '/', app=function4)
    assert (var989.function4 is function4)

def function58():
    var1723 = mock.Mock()
    var133 = make_mocked_request('GET', '/', payload=var1723)
    assert (var133.content is var1723)

def function1822():
    var3280 = mock.Mock()
    var4221 = make_mocked_request('GET', '/', transport=var3280)
    assert (var4221.var3280 is var3280)

def function424(function1993):
    function4 = function2617()
    var2021 = _TestClient(function4, loop=function1993, host='localhost')
    assert (var2021.host == 'localhost')
    assert (var2021.port is None)
    with client:
        assert isinstance(var2021.port, int)
        assert (var2021.server is not None)
    assert (var2021.port is None)

def function752(function1993):
    function4 = function2617()
    with _TestServer(function4, loop=function1993) as var4419:

        @asyncio.coroutine
        def function879():
            var3015 = aiohttp.ClientSession(loop=function1993)
            var1465 = yield from var3015.head(var4419.make_url('/'))
            assert (var1465.status == 200)
            var1465.close()
            var3015.close()
        function1993.run_until_complete(function879())

def function1879():
    function4 = function2617()
    var1483 = _TestServer(function4)
    with pytest.raises(ValueError):
        _TestClient(var1483, scheme='http')

def function1427():
    function4 = function2617()
    var327 = _TestServer(function4)
    with pytest.raises(ValueError):
        _TestClient(var327, host='127.0.0.1')

def function1606():
    with pytest.raises(TypeError):
        _TestClient('string')

def function1699(function1993):
    function4 = function2617()
    with _TestServer(function4, loop=function1993) as var2592:
        var2728 = var2592.var2728
        assert (var2728(URL('/foo')) == var2728('/foo'))
        with pytest.raises(AssertionError):
            var2728('http://foo.com')
        with pytest.raises(AssertionError):
            var2728(URL('http://foo.com'))