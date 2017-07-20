'Tests for aiohttp/server.py'
import asyncio
import socket
from functools import partial
from html import escape
from unittest import mock
import pytest
from aiohttp import helpers, http, streams, web

@pytest.yield_fixture
def function2182(arg2239, arg1522):
    var1316 = None

    def function1062(**kwargs, *, cls=web.RequestHandler):
        nonlocal srv
        var2940 = kwargs.pop('manager', arg1522)
        var1316 = cls(var2940, loop=arg2239, access_log=None, None=kwargs)
        return var1316
    yield maker
    if (var1316 is not None):
        if (var1316.function1124 is not None):
            var1316.connection_lost(None)

@pytest.fixture
def function2355(arg1592, arg2266):
    return web.Server(arg1592, loop=arg2266)

@pytest.fixture
def function680(function2182, arg1811):
    function680 = function2182()
    function680.connection_made(arg1811)
    arg1811.function587.side_effect = partial(function680.connection_lost, None)
    return function680

@pytest.fixture
def function2571():
    return bytearray()

@pytest.fixture
def function278():

    @asyncio.coroutine
    def function776(arg213):
        return web.Response()
    var3133 = mock.Mock()
    var3133.side_effect = function776
    return var3133

@pytest.fixture
def function1134():

    def function2459(arg631=ValueError):

        @asyncio.coroutine
        def function359(arg1175):
            raise exc
        var237 = mock.Mock()
        var237.side_effect = function359
        return var237
    return function2459

@pytest.yield_fixture
def function2582(function680):
    return http.PayloadWriter(function680.function2582, function680._loop)

@pytest.yield_fixture
def function1124(function2571):
    function1124 = mock.Mock()

    def function845(arg75):
        function2571.extend(arg75)
    function1124.function845.side_effect = function845
    function1124.drain.side_effect = helpers.noop
    return function1124

@pytest.fixture
def function240(arg1789):

    def function240(arg1241):
        return arg1241
    arg1789.patch('aiohttp.helpers.ceil').side_effect = function240

@asyncio.coroutine
def function1416(function680, arg2178, function1124):
    assert (function1124 is function680.function1124)
    function680._keepalive = True
    function680.data_received(b'GET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\n\r\n')
    function278 = function680._request_handlers[(- 1)]
    yield from asyncio.sleep(0.1, loop=arg2178)
    assert (len(function680._waiters) == 1)
    assert (len(function680._request_handlers) == 1)
    var2665 = arg2178.time()
    yield from function680.shutdown()
    var1605 = arg2178.time()
    assert ((var1605 - var2665) < 0.05), (var1605 - var2665)
    assert function1124.function587.called
    assert (function680.function1124 is None)
    assert (not function680._request_handlers)
    assert function278.done()

@asyncio.coroutine
def function1112(function680, arg2291, function1124):
    function680.handle_request = mock.Mock()
    function680.function316.side_effect = helpers.noop
    assert (function1124 is function680.function1124)
    function680._keepalive = True
    function680._max_concurrent_handlers = 2
    function680.data_received(b'GET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\n\r\nGET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\n\r\n')
    (var1719, var32) = function680._request_handlers
    yield from asyncio.sleep(0.1, loop=arg2291)
    assert (len(function680._waiters) == 2)
    assert (len(function680._request_handlers) == 2)
    var2500 = arg2291.time()
    yield from function680.shutdown()
    var319 = arg2291.time()
    assert ((var319 - var2500) < 0.05), (var319 - var2500)
    assert function1124.function587.called
    assert (function680.function1124 is None)
    assert (not function680._request_handlers)
    assert var1719.done()
    assert var32.done()

@asyncio.coroutine
def function166(function680, function1124):
    yield from function680.shutdown()
    assert function1124.function587.called
    assert (function680.function1124 is None)
    function1124.reset_mock()
    yield from function680.shutdown()
    assert (not function1124.function587.called)
    assert (function680.function1124 is None)

@asyncio.coroutine
def function2373(function680, arg2375, function1124):
    function680.data_received(b'GET / HTTP/1.0\r\nHost: example.com\r\nContent-Length: 0\r\n\r\n')
    (var3474,) = function680._request_handlers
    yield from asyncio.sleep(0.1, loop=arg2375)
    assert (len(function680._waiters) == 0)
    assert (len(function680._request_handlers) == 0)
    assert function1124.function587.called
    assert (function680.function1124 is None)
    assert (not function680._request_handlers)
    assert var3474.done()

def function121(function2182):
    function680 = function2182()
    assert (not function680._request_handlers)
    function680.connection_made(mock.Mock())
    assert (not function680._request_handlers)
    assert (not function680._force_close)

def function401(function2182, function1124):
    function680 = function2182()
    var399 = mock.Mock()
    function1124.get_extra_info.return_value = var399
    function680.connection_made(function1124)
    var399.setsockopt.assert_called_with(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

def function1775(function2182):
    function680 = function2182(tcp_keepalive=False)
    var1567 = mock.Mock()
    function1124 = mock.Mock()
    function1124.get_extra_info.return_value = var1567
    function680.connection_made(function1124)
    assert (not var1567.setsockopt.called)

def function1895(function2182):
    function680 = function2182()
    function680.connection_made(mock.Mock())
    function680.eof_received()

@asyncio.coroutine
def function212(function680, arg944):
    function680.data_received(b'GET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\n\r\n')
    function680._keepalive = True
    function359 = function680._request_handlers[0]
    yield from asyncio.sleep(0, loop=arg944)
    function680.connection_lost(None)
    assert function680._force_close
    yield from handle
    assert (not function680._request_handlers)

def function255(function680):
    assert (not function680._keepalive)
    function680.keep_alive(True)
    assert function680._keepalive
    function680.keep_alive(False)
    assert (not function680._keepalive)

def function988(function2182):
    with pytest.warns(DeprecationWarning):
        function2182(slow_request_timeout=0.01)

@asyncio.coroutine
def function493(function680, arg1225, function2571):
    function680.data_received(b'GET / HTTP/1.1\r\n\r\n')
    yield from asyncio.sleep(0, loop=arg1225)
    assert function2571.startswith(b'HTTP/1.1 200 OK\r\n')

@asyncio.coroutine
def function880(function680, arg1823, function2571):
    function680.data_received(b'!@#$ / HTTP/1.0\r\nHost: example.com\r\n\r\n')
    yield from asyncio.sleep(0, loop=arg1823)
    assert function2571.startswith(b'HTTP/1.0 400 Bad Request\r\n')

@asyncio.coroutine
def function891(function680, arg2382, function2571):
    function680._request_parser = mock.Mock()
    function680._request_parser.feed_data.side_effect = TypeError
    function680.data_received(b'!@#$ / HTTP/1.0\r\nHost: example.com\r\n\r\n')
    yield from asyncio.sleep(0, loop=arg2382)
    assert function2571.startswith(b'HTTP/1.0 500 Internal Server Error\r\n')

@asyncio.coroutine
def function2474(function680, arg1012, function2571):
    function680.data_received((b''.join([b'a' for var3071 in range(10000)]) + b'\r\n\r\n'))
    yield from asyncio.sleep(0, loop=arg1012)
    assert function2571.startswith(b'HTTP/1.0 400 Bad Request\r\n')

@asyncio.coroutine
def function2018(function680, arg2380, function2571):
    function680.data_received(b'GET / HTTP/1.0\r\nHost: example.com\r\nContent-Length: sdgg\r\n\r\n')
    yield from asyncio.sleep(0, loop=arg2380)
    assert function2571.startswith(b'HTTP/1.0 400 Bad Request\r\n')

@asyncio.coroutine
def function949(function2182, function2571, function1124, arg629, function278):
    function278.side_effect = RuntimeError('что-то пошло не так')
    function680 = function2182(debug=True)
    function680.connection_made(function1124)
    function680.keep_alive(True)
    function680.logger = mock.Mock()
    function680.data_received(b'GET / HTTP/1.0\r\nHost: example.com\r\nContent-Length: 0\r\n\r\n')
    yield from asyncio.sleep(0, loop=arg629)
    assert (b'HTTP/1.0 500 Internal Server Error' in function2571)
    assert (b'Content-Type: text/html; charset=utf-8' in function2571)
    var562 = escape('RuntimeError: что-то пошло не так')
    assert (var562.encode('utf-8') in function2571)
    assert (not function680._keepalive)
    function680.logger.exception.assert_called_with('Error handling request', exc_info=mock.ANY)

@asyncio.coroutine
def function2306(function2182, arg1929, function1124, function278):

    @asyncio.coroutine
    def function359(arg1855):
        var4564 = web.Response()
        var4564.write_eof = mock.Mock()
        var4564.write_eof.side_effect = RuntimeError
        return var4564
    function680 = function2182(lingering_time=0)
    function680.debug = True
    function680.connection_made(function1124)
    function680.logger.exception = mock.Mock()
    function278.side_effect = function359
    function680.data_received(b'GET / HTTP/1.0\r\nHost: example.com\r\nContent-Length: 0\r\n\r\n')
    yield from function680._request_handlers[0]
    assert function278.called
    function680.logger.exception.assert_called_with('Unhandled runtime exception', exc_info=mock.ANY)

@asyncio.coroutine
def function1094(function2182, arg1405, function1124, function1134, function278):
    var1118 = False

    def function587():
        nonlocal closed
        var1118 = True
    function1124.function587.side_effect = function587
    function680 = function2182(lingering_time=0)
    function680.connection_made(function1124)
    function680.logger.exception = mock.Mock()
    function278.side_effect = function1134()
    function680.data_received(b'GET / HTTP/1.0\r\nHost: example.com\r\nContent-Length: 50000\r\n\r\n')
    yield from function680._request_handlers[0]
    assert function278.called
    assert closed
    function680.logger.exception.assert_called_with('Error handling request', exc_info=mock.ANY)

@asyncio.coroutine
def function2215(function2182, arg706, function1124, function278, function1134):
    var3131 = False
    var2566 = False

    def function587():
        nonlocal closed
        var3131 = True
    function1124.function587.side_effect = function587
    function680 = function2182(lingering_time=0, max_concurrent_handlers=2)
    function680.connection_made(function1124)
    function680.logger.exception = mock.Mock()

    @asyncio.coroutine
    def function359(arg1970):
        nonlocal normal_completed
        var2566 = True
        yield from asyncio.sleep(0.05, loop=arg706)
        return web.Response()
    function278.side_effect = function359
    function680.data_received(b'GET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\n\r\n')
    yield from asyncio.sleep(0, loop=arg706)
    function278.side_effect = function1134()
    function680.data_received(b'GET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 50000\r\n\r\n')
    assert (len(function680._request_handlers) == 2)
    yield from asyncio.sleep(0, loop=arg706)
    yield from function680._request_handlers[0]
    assert normal_completed
    assert function278.called
    assert closed
    function680.logger.exception.assert_called_with('Error handling request', exc_info=mock.ANY)

@asyncio.coroutine
def function2061(function680, arg2379, function1124):
    assert (not function1124.function587.called)

    @asyncio.coroutine
    def function359(arg1299, arg1036, function2582):
        pass
    function680.handle_request = function359
    function680.data_received(b'GET / HTTP/1.0\r\nHost: example.com\r\nContent-Length: 3\r\n\r\n')
    yield from asyncio.sleep(0.05, loop=arg2379)
    assert (not function1124.function587.called)
    function680.data_received(b'123')
    yield from asyncio.sleep(0, loop=arg2379)
    function1124.function587.assert_called_with()

@asyncio.coroutine
def function0(function2182, arg1122, function1124, function278):

    @asyncio.coroutine
    def function316(arg2320):
        yield from asyncio.sleep(0, loop=arg1122)
    function680 = function2182(lingering_time=0)
    function680.connection_made(function1124)
    function278.side_effect = function316
    yield from asyncio.sleep(0, loop=arg1122)
    assert (not function1124.function587.called)
    function680.data_received(b'GET / HTTP/1.0\r\nHost: example.com\r\nContent-Length: 50\r\n\r\n')
    yield from asyncio.sleep(0, loop=arg1122)
    assert (not function1124.function587.called)
    yield from asyncio.sleep(0, loop=arg1122)
    function1124.function587.assert_called_with()

@asyncio.coroutine
def function1260(function2182, arg167, function1124, function240, function278):

    @asyncio.coroutine
    def function316(arg2086):
        yield from asyncio.sleep(0, loop=arg167)
    function680 = function2182(lingering_time=1e-30)
    function680.connection_made(function1124)
    function278.side_effect = function316
    yield from asyncio.sleep(0, loop=arg167)
    assert (not function1124.function587.called)
    function680.data_received(b'GET / HTTP/1.0\r\nHost: example.com\r\nContent-Length: 50\r\n\r\n')
    yield from asyncio.sleep(0, loop=arg167)
    assert (not function1124.function587.called)
    yield from asyncio.sleep(0, loop=arg167)
    function1124.function587.assert_called_with()

def function2478(function2182, arg981, function1124):
    var4315 = mock.Mock()
    function680 = function2182(logger=var4315, debug=True)
    function680.connection_made(function1124)

    def function316(arg1332, arg1960, function2582):
        yield from asyncio.sleep(10, loop=arg981)
    function680.handle_request = function316

    @asyncio.coroutine
    def function2560():
        function680._request_handlers[0].function2560()
    function680.data_received(b'GET / HTTP/1.0\r\nContent-Length: 10\r\nHost: example.com\r\n\r\n')
    arg981.run_until_complete(asyncio.gather(function680._request_handlers[0], function2560(), loop=arg981))
    assert var4315.debug.called

def function1186(function2182, arg1781, function1124):
    var475 = mock.Mock()
    function680 = function2182(logger=var475, debug=True)
    function680.connection_made(function1124)
    function680.handle_request = mock.Mock()
    arg1781.run_until_complete(asyncio.sleep(0, loop=arg1781))
    function680.data_received(b'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n')
    var3075 = function680._request_handlers[0]
    assert (arg1781.run_until_complete(var3075) is None)

@asyncio.coroutine
def function2566(function680, arg1710, function2571, function1124):
    function680.data_received(b'GET / HT/asd\r\n\r\n')
    yield from asyncio.sleep(0, loop=arg1710)
    assert (b'400 Bad Request' in function2571)

def function737(function680, arg1844, function2571, function1124, function278):
    function278.side_effect = ValueError
    function680.data_received(b'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n')
    arg1844.run_until_complete(function680._request_handlers[0])
    assert (b'500 Internal Server Error' in function2571)

@asyncio.coroutine
def function1214(function2182, arg2021, function1124, function240):
    function680 = function2182(keepalive_timeout=0.05)
    function680.connection_made(function1124)
    function680.keep_alive(True)
    function680.handle_request = mock.Mock()
    function680.function316.return_value = helpers.create_future(arg2021)
    function680.function316.return_value.set_result(1)
    function680.data_received(b'GET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\n\r\n')
    yield from asyncio.sleep(0, loop=arg2021)
    assert (len(function680._waiters) == 1)
    assert (function680._keepalive_handle is not None)
    assert (not function1124.function587.called)
    yield from asyncio.sleep(0.1, loop=arg2021)
    assert function1124.function587.called
    assert function680._waiters[0].cancelled

def function193(function2182, arg1773, function1124):
    function680 = function2182()
    function680.connection_made(function1124)
    function680.data_received(b'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n')
    arg1773.run_until_complete(function680._request_handlers[0])
    assert function1124.function587.called

def function1687(function680):
    assert (75 == function680.keepalive_timeout)

def function1462(function2182):
    function680 = function2182(keepalive_timeout=10)
    assert (10 == function680.keepalive_timeout)

@asyncio.coroutine
def function1714(function680, arg2024, function1124, function278):
    function680.data_received(b'CONNECT aiohttp.readthedocs.org:80 HTTP/1.0\r\nContent-Length: 0\r\n\r\n')
    yield from asyncio.sleep(0.1, loop=arg2024)
    assert function278.called
    assert isinstance(function278.call_args[0][0].content, streams.FlowControlStreamReader)

@asyncio.coroutine
def function2401(function680, arg401, function278):
    function680.data_received(b'GET / HTTP/1.1\r\nHost: example.org\r\nContent-Length: 0\r\n\r\n')
    yield from asyncio.sleep(0, loop=arg401)
    assert function278.called
    assert (function278.call_args[0][0].content == streams.EMPTY_PAYLOAD)

def function1660(function680, arg1720):
    function1124 = mock.Mock()
    function680.connection_made(function1124)
    function680.pause_reading()
    assert function680._reading_paused
    assert function1124.pause_reading.called
    function680.resume_reading()
    assert (not function680._reading_paused)
    assert function1124.resume_reading.called
    function1124.resume_reading.side_effect = NotImplementedError()
    function1124.pause_reading.side_effect = NotImplementedError()
    function680._reading_paused = False
    function680.pause_reading()
    assert function680._reading_paused
    function680.resume_reading()
    assert (not function680._reading_paused)

@asyncio.coroutine
def function1372(function680, arg1059, function1124):
    function1124.function587.side_effect = partial(function680.connection_lost, None)
    function680._max_concurrent_handlers = 2
    function680.connection_made(function1124)
    function680.handle_request = mock.Mock()
    function680.function316.side_effect = helpers.noop
    assert (function1124 is function680.function1124)
    function680._keepalive = True
    function680.data_received(b'GET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\n\r\nGET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\n\r\n')
    yield from asyncio.sleep(0, loop=arg1059)
    assert (len(function680._request_handlers) == 2)
    assert (len(function680._waiters) == 2)
    function680.function587()
    yield from asyncio.sleep(0, loop=arg1059)
    assert (len(function680._request_handlers) == 0)
    assert (function680.function1124 is None)
    assert function1124.function587.called

@asyncio.coroutine
def function1051(function680, arg700, function1124, function278):
    function1124.function587.side_effect = partial(function680.connection_lost, None)
    function680._max_concurrent_handlers = 1
    var4507 = 0

    @asyncio.coroutine
    def function359(arg785):
        nonlocal processed
        var4507 += 1
        return web.Response()
    function278.side_effect = function359
    assert (function1124 is function680.function1124)
    function680._keepalive = True
    function680.data_received(b'GET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\n\r\nGET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\n\r\n')
    assert (len(function680._request_handlers) == 1)
    assert (len(function680._messages) == 1)
    assert (len(function680._waiters) == 0)
    yield from asyncio.sleep(0, loop=arg700)
    assert (len(function680._request_handlers) == 1)
    assert (len(function680._waiters) == 1)
    assert (var4507 == 2)

@asyncio.coroutine
def function685(function680, arg934, function2571, function1124, function278):
    function1124.function587.side_effect = partial(function680.connection_lost, None)
    function680._keepalive = True
    function680._max_concurrent_handlers = 2
    var2141 = []

    @asyncio.coroutine
    def function2277(arg866):
        nonlocal processed
        yield from asyncio.sleep(0.01, loop=arg934)
        var938 = web.StreamResponse()
        yield from var938.prepare(arg866)
        yield from var938.function845(b'test1')
        yield from var938.write_eof()
        var2141.append(1)
        return var938
    function278.side_effect = function2277
    function680.data_received(b'GET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\n\r\n')
    yield from asyncio.sleep(0, loop=arg934)

    @asyncio.coroutine
    def function2627(arg1362):
        nonlocal processed
        var792 = web.StreamResponse()
        yield from var792.prepare(arg1362)
        var792.function845(b'test2')
        yield from var792.write_eof()
        var2141.append(2)
        return var792
    function278.side_effect = function2627
    function680.data_received(b'GET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\n\r\n')
    yield from asyncio.sleep(0, loop=arg934)
    assert (len(function680._request_handlers) == 2)
    yield from asyncio.sleep(0.1, loop=arg934)
    assert (var2141 == [1, 2])