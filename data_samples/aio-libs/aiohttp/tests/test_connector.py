'Tests of http client with custom Connector'
import asyncio
import gc
import os.path
import platform
import shutil
import socket
import ssl
import tempfile
import unittest
from unittest import mock
import pytest
from yarl import URL
import aiohttp
from aiohttp import client, helpers, web
from aiohttp.client import ClientRequest
from aiohttp.connector import Connection, _DNSCacheTable
from aiohttp.test_utils import unused_port

@pytest.fixture()
def function1139():
    'Connection key'
    return ('localhost1', 80, False)

@pytest.fixture
def function796():
    'Connection key'
    return ('localhost2', 80, False)

@pytest.fixture
def function921():
    'Connection key'
    return ('localhost', 80, True)

def function2210(arg2087):
    var1837 = aiohttp.BaseConnector(loop=arg2087)
    var1621 = mock.Mock(should_close=False)
    var1837._release('a', var1621)
    var3556 = var1837._conns
    var1287 = mock.Mock()
    arg2087.set_exception_handler(var1287)
    with pytest.warns(ResourceWarning):
        del conn
        gc.collect()
    assert (not var3556)
    var1621.close.assert_called_with()
    var1774 = {'connector': mock.ANY, 'connections': mock.ANY, 'message': 'Unclosed connector', }
    if arg2087.get_debug():
        var1774['source_traceback'] = mock.ANY
    var1287.assert_called_with(arg2087, var1774)

@pytest.mark.xfail
@asyncio.coroutine
def function1143(arg189):
    arg189.set_debug(True)
    var3296 = aiohttp.BaseConnector(loop=arg189, keepalive_timeout=0.01)
    var625 = mock.Mock()
    var3296._conns['a'] = [(var625, 'proto', 123)]
    var4454 = var3296._conns
    var2356 = mock.Mock()
    arg189.set_exception_handler(var2356)
    with pytest.warns(ResourceWarning):
        del conn
        yield from asyncio.sleep(0.01, loop=arg189)
        gc.collect()
    assert (not var4454)
    var625.close.assert_called_with()
    var247 = {'connector': mock.ANY, 'message': 'Unclosed connector', }
    if arg189.get_debug():
        var247['source_traceback'] = mock.ANY
    var2356.assert_called_with(arg189, var247)

def function521(arg2147):
    var2421 = aiohttp.BaseConnector(loop=arg2147)
    var2664 = mock.Mock()
    var2421._conns['a'] = [(var2664, 'proto', 123)]
    var1642 = var2421._conns
    var4296 = mock.Mock()
    arg2147.set_exception_handler(var4296)
    arg2147.close()
    with pytest.warns(ResourceWarning):
        del conn
        gc.collect()
    assert (not var1642)
    assert (not var2664.close.called)
    assert var4296.called

def function1879(arg863):
    var2190 = aiohttp.BaseConnector(loop=arg863)
    var4746 = mock.Mock()
    arg863.set_exception_handler(var4746)
    del conn
    assert (not var4746.called)

@asyncio.coroutine
def function2319(arg870):
    var966 = aiohttp.BaseConnector(loop=arg870)
    with pytest.raises(NotImplementedError):
        yield from var966._create_connection(object())

def function47(arg1532):
    var38 = aiohttp.BaseConnector(loop=arg1532)
    var38.close = mock.Mock()
    with conn as var682:
        assert (var38 is var682)
    assert var38.close.called

def function1580():
    with mock.patch('aiohttp.connector.asyncio') as var2331:
        var1024 = aiohttp.BaseConnector()
    assert (var1024._loop is var2331.get_event_loop.return_value)

def function1515(arg346):
    var1136 = mock.Mock()
    var2210 = aiohttp.BaseConnector(loop=arg346)
    assert (not var2210.closed)
    var2210._conns[('host', 8080, False)] = [(var1136, object())]
    var2210.close()
    assert (not var2210._conns)
    assert var1136.close.called
    assert var2210.closed

def function2098(arg1302):
    var573 = aiohttp.BaseConnector(loop=arg1302)
    assert (var573._get(1) is None)
    var51 = mock.Mock()
    var573._conns[1] = [(var51, arg1302.time())]
    assert (var573._get(1) == var51)
    var573.close()

def function332(arg602):
    var621 = aiohttp.BaseConnector(loop=arg602)
    assert (var621._get(('localhost', 80, False)) is None)
    var2059 = mock.Mock()
    var621._conns[('localhost', 80, False)] = [(var2059, (arg602.time() - 1000))]
    assert (var621._get(('localhost', 80, False)) is None)
    assert (not var621._conns)
    var621.close()

def function1720(arg505):
    var385 = aiohttp.BaseConnector(loop=arg505, enable_cleanup_closed=True)
    assert (var385._get(('localhost', 80, True)) is None)
    var331 = mock.Mock()
    var385._conns[('localhost', 80, True)] = [(var331, (arg505.time() - 1000))]
    assert (var385._get(('localhost', 80, True)) is None)
    assert (not var385._conns)
    assert (var385._cleanup_closed_transports == [var331.close.return_value])
    var385.close()

def function1328(arg650, function1139):
    var2859 = mock.Mock()
    var1017 = aiohttp.BaseConnector(loop=arg650, limit=5)
    var1017._release_waiter = mock.Mock()
    var1017._acquired.add(var2859)
    var1017._acquired_per_host[function1139].add(var2859)
    var1017._release_acquired(function1139, var2859)
    assert (0 == len(var1017._acquired))
    assert (0 == len(var1017._acquired_per_host))
    assert var1017._release_waiter.called
    var1017._release_acquired(function1139, var2859)
    assert (0 == len(var1017._acquired))
    assert (0 == len(var1017._acquired_per_host))
    var1017.close()

def function1844(arg1361, function1139):
    var3850 = mock.Mock()
    var4148 = aiohttp.BaseConnector(loop=arg1361, limit=5)
    var4148._release_waiter = mock.Mock()
    var4148._acquired.add(var3850)
    var4148._acquired_per_host[function1139].add(var3850)
    var4148._closed = True
    var4148._release_acquired(function1139, var3850)
    assert (1 == len(var4148._acquired))
    assert (1 == len(var4148._acquired_per_host[function1139]))
    assert (not var4148._release_waiter.called)
    var4148.close()

def function2371(arg1892, function1139):
    var1942 = aiohttp.BaseConnector(loop=arg1892)
    var1942._release_waiter = mock.Mock()
    var3242 = mock.Mock(should_close=False)
    var1942._acquired.add(var3242)
    var1942._acquired_per_host[function1139].add(var3242)
    var1942._release(function1139, var3242)
    assert var1942._release_waiter.called
    assert (var1942._conns[function1139][0][0] == var3242)
    assert (var1942._conns[function1139][0][1] == pytest.approx(arg1892.time(), abs=0.1))
    assert (not var1942._cleanup_closed_transports)
    var1942.close()

def function706(arg98, function921):
    var2857 = aiohttp.BaseConnector(loop=arg98, enable_cleanup_closed=True)
    var2857._release_waiter = mock.Mock()
    var1084 = mock.Mock()
    var2857._acquired.add(var1084)
    var2857._acquired_per_host[function921].add(var1084)
    var2857._release(function921, var1084, should_close=True)
    assert (var2857._cleanup_closed_transports == [var1084.close.return_value])
    var2857.close()

def function2052(arg655):
    var4017 = aiohttp.BaseConnector(loop=arg655)
    var3244 = mock.Mock()
    function1139 = 1
    var4017._acquired.add(var3244)
    var4017.close()
    var4017._release_waiters = mock.Mock()
    var4017._release_acquired = mock.Mock()
    var4017._release(function1139, var3244)
    assert (not var4017._release_waiters.called)
    assert (not var4017._release_acquired.called)

def function74(arg862, function1139, function796):
    var220 = aiohttp.BaseConnector(limit=0, loop=arg862)
    var540 = mock.Mock()
    var540.done.return_value = False
    var220._waiters[function1139].append(var540)
    var220._release_waiter()
    assert (len(var220._waiters) == 1)
    assert (not var540.done.called)
    var220.close()
    var220 = aiohttp.BaseConnector(loop=arg862)
    (var3630, var4422) = (mock.Mock(), mock.Mock())
    var3630.done.return_value = False
    var4422.done.return_value = False
    var220._waiters[function1139].append(var4422)
    var220._waiters[function796].append(var3630)
    var220._release_waiter()
    assert ((var3630.set_result.called and (not var4422.set_result.called)) or ((not var3630.set_result.called) and var4422.set_result.called))
    var220.close()
    var220 = aiohttp.BaseConnector(loop=arg862, limit=1)
    (var3630, var4422) = (mock.Mock(), mock.Mock())
    var3630.done.return_value = False
    var4422.done.return_value = False
    var220._waiters[function1139] = [var3630, var4422]
    var220._release_waiter()
    assert var3630.set_result.called
    assert (not var4422.set_result.called)
    var220.close()
    var220 = aiohttp.BaseConnector(loop=arg862, limit=1)
    (var3630, var4422) = (mock.Mock(), mock.Mock())
    var3630.done.return_value = True
    var4422.done.return_value = False
    var220._waiters[function1139] = [var3630, var4422]
    var220._release_waiter()
    assert (not var3630.set_result.called)
    assert (not var4422.set_result.called)
    var220.close()

def function2745(arg358, function1139, function796):
    var999 = aiohttp.BaseConnector(loop=arg358, limit=0, limit_per_host=2)
    (var2197, var3549) = (mock.Mock(), mock.Mock())
    var2197.done.return_value = False
    var3549.done.return_value = False
    var999._waiters[function1139] = [var2197]
    var999._waiters[function796] = [var3549]
    var999._release_waiter()
    assert ((var2197.set_result.called and (not var3549.set_result.called)) or ((not var2197.set_result.called) and var3549.set_result.called))
    var999.close()

def function1301(arg761):
    var3507 = aiohttp.BaseConnector(loop=arg761)
    var3906 = mock.Mock(should_close=True)
    function1139 = ('localhost', 80, False)
    var3507._acquired.add(var3906)
    var3507._release(function1139, var3906)
    assert (not var3507._conns)
    assert var3906.close.called

@asyncio.coroutine
def function1100(arg360):
    var1273 = aiohttp.TCPConnector(loop=arg360, use_dns_cache=True)
    var1855 = yield from var1273._resolve_host('localhost', 8080)
    assert res
    for var1802 in var1855:
        if (var1802['family'] == socket.AF_INET):
            assert (var1802['host'] == '127.0.0.1')
            assert (var1802['hostname'] == 'localhost')
            assert (var1802['port'] == 8080)
        elif (var1802['family'] == socket.AF_INET6):
            assert (var1802['hostname'] == 'localhost')
            assert (var1802['port'] == 8080)
            if (platform.system() == 'Darwin'):
                assert (var1802['host'] in ('::1', 'fe80::1', 'fe80::1%lo0'))
            else:
                assert (var1802['host'] == '::1')

@asyncio.coroutine
def function2587():
    return ['127.0.0.1']

@asyncio.coroutine
def function2290(arg355):
    with mock.patch('aiohttp.connector.DefaultResolver') as var809:
        var2269 = aiohttp.TCPConnector(loop=arg355, use_dns_cache=True, ttl_dns_cache=10)
        var809().resolve.return_value = function2587()
        yield from var2269._resolve_host('localhost', 8080)
        yield from var2269._resolve_host('localhost', 8080)
        var809().resolve.assert_called_once_with('localhost', 8080, family=0)

@asyncio.coroutine
def function2697(arg803):
    with mock.patch('aiohttp.connector.DefaultResolver') as var4224:
        var4546 = aiohttp.TCPConnector(loop=arg803, use_dns_cache=True, ttl_dns_cache=10)
        var4224().resolve.return_value = function2587()
        yield from var4546._resolve_host('localhost', 8080)
        yield from var4546._resolve_host('localhost', 8080)
        var4224().resolve.assert_called_once_with('localhost', 8080, family=0)

@asyncio.coroutine
def function1355(arg2353):
    with mock.patch('aiohttp.connector.DefaultResolver') as var4054:
        var3609 = aiohttp.TCPConnector(loop=arg2353, use_dns_cache=False)
        var4054().resolve.return_value = function2587()
        yield from var3609._resolve_host('localhost', 8080)
        yield from var3609._resolve_host('localhost', 8080)
        var4054().resolve.assert_has_calls([mock.call('localhost', 8080, family=0), mock.call('localhost', 8080, family=0)])

def function2661(arg488):
    var482 = aiohttp.BaseConnector(loop=arg488)
    function1139 = ('127.0.0.1', 80, False)
    var482._conns[function1139] = []
    var2070 = var482._get(function1139)
    assert (var2070 is None)
    assert (not var482._conns)

def function1066(arg1760):
    var4221 = aiohttp.BaseConnector(loop=arg1760)
    function1139 = ('127.0.0.1', 80, False)
    var139 = mock.Mock(should_close=True)
    var4221._acquired.add(var139)
    var4221._release(function1139, var139)
    assert (not var4221._conns)

def function2355(arg173):
    function1139 = ('127.0.0.1', 80, False)
    var2376 = mock.Mock()
    var1499 = aiohttp.BaseConnector(loop=arg173)
    var1499._conns[function1139] = [(var2376, 1)]
    var196 = mock.Mock(should_close=True)
    var1499._acquired.add(var196)
    var1499._release(function1139, var196)
    assert (var1499._conns[function1139] == [(var2376, 1)])
    assert var196.close.called
    var1499.close()

def function953(arg1907):
    var1340 = aiohttp.BaseConnector(loop=arg1907)
    var3571 = mock.Mock(should_close=False)
    function1139 = 1
    var1340._acquired.add(var3571)
    var1340._release(function1139, var3571)
    var3888 = var1340._conns[1]
    assert (var3888[0][0] == var3571)
    assert (var3888[0][1] == pytest.approx(arg1907.time(), abs=0.01))
    assert (not var3571.close.called)
    var1340.close()

def function741(arg626):
    var3102 = aiohttp.BaseConnector(loop=arg626)
    var1632 = mock.Mock()
    function1139 = ('localhost', 80, False)
    var3102._acquired.add(var1632)
    var3102._release(function1139, var1632)
    assert var1632.close.called

@asyncio.coroutine
def function1488(arg2389):
    var1259 = mock.Mock()
    var1259.is_connected.return_value = True
    var300 = ClientRequest('GET', URL('http://host:80'), loop=arg2389)
    var1124 = aiohttp.BaseConnector(loop=arg2389)
    function1139 = ('host', 80, False)
    var1124._conns[function1139] = [(var1259, arg2389.time())]
    var1124._create_connection = mock.Mock()
    var1124._create_connection.return_value = helpers.create_future(arg2389)
    var1124._create_connection.return_value.set_result(var1259)
    var3050 = yield from var1124.connect(var300)
    assert (not var1124._create_connection.called)
    assert (var3050._protocol is var1259)
    assert (var3050.transport is var1259.transport)
    assert isinstance(var3050, Connection)
    var3050.close()

@asyncio.coroutine
def function2356(arg100):
    var2009 = aiohttp.BaseConnector(loop=arg100)
    var2009._create_connection = mock.Mock()
    var2009._create_connection.return_value = helpers.create_future(arg100)
    var3084 = OSError(1, 'permission error')
    var2009._create_connection.return_value.set_exception(var3084)
    with pytest.raises(aiohttp.ClientOSError) as var3108:
        var515 = mock.Mock()
        yield from var2009.connect(var515)
    assert (1 == var3108.value.errno)
    assert var3108.value.strerror.startswith('Cannot connect to')
    assert var3108.value.strerror.endswith('[permission error]')

def function830():
    var841 = mock.Mock()
    var841.time.return_value = 1.5
    var1240 = aiohttp.BaseConnector(loop=var841, keepalive_timeout=10, enable_cleanup_closed=True)
    assert (var1240._cleanup_handle is None)
    assert (var1240._cleanup_closed_handle is not None)

def function577():
    function1139 = ('localhost', 80, False)
    var2137 = {key: [(mock.Mock(), 10), (mock.Mock(), 300)], }
    var2137[function1139][0][0].is_connected.return_value = True
    var2137[function1139][1][0].is_connected.return_value = False
    var224 = mock.Mock()
    var224.time.return_value = 300
    var3563 = aiohttp.BaseConnector(loop=var224)
    var3563._conns = var2137
    var2450 = var3563._cleanup_handle = mock.Mock()
    var3563._cleanup()
    assert var2450.cancel.called
    assert (var3563._conns == {})
    assert (var3563._cleanup_handle is not None)

def function345():
    var4487 = mock.Mock()
    function1139 = ('localhost', 80, True)
    var1744 = {key: [(var4487, 10)], }
    var1079 = mock.Mock()
    var1079.time.return_value = 300
    var1940 = aiohttp.BaseConnector(loop=var1079, enable_cleanup_closed=True)
    var1940._conns = var1744
    var1551 = var1940._cleanup_handle = mock.Mock()
    var1940._cleanup()
    assert var1551.cancel.called
    assert (var1940._conns == {})
    assert (var1940._cleanup_closed_transports == [var4487.close.return_value])

def function1702():
    var4085 = {1: [(mock.Mock(), 300)], }
    var4085[1][0][0].is_connected.return_value = True
    var1638 = mock.Mock()
    var1638.time.return_value = 300
    var1065 = aiohttp.BaseConnector(loop=var1638, keepalive_timeout=10)
    var1065._conns = var4085
    var1065._cleanup()
    assert (var1065._conns == var4085)
    assert (var1065._cleanup_handle is not None)
    var1638.call_at.assert_called_with(310, mock.ANY, mock.ANY)
    var1065.close()

def function2647():
    function1139 = ('localhost', 80, False)
    var179 = {key: [(mock.Mock(), 290.1), (mock.Mock(), 305.1)], }
    var179[function1139][0][0].is_connected.return_value = True
    var4529 = mock.Mock()
    var4529.time.return_value = 308.5
    var2193 = aiohttp.BaseConnector(loop=var4529, keepalive_timeout=10)
    var2193._conns = var179
    var2193._cleanup()
    assert (var2193._conns == {key: [var179[function1139][1]], })
    assert (var2193._cleanup_handle is not None)
    var4529.call_at.assert_called_with(319, mock.ANY, mock.ANY)
    var2193.close()

def function2466(arg1298, arg958):
    if (not hasattr(arg1298, '__dict__')):
        pytest.skip('can not override loop attributes')
    arg958.spy(arg1298, 'call_at')
    var1434 = aiohttp.BaseConnector(loop=arg1298, enable_cleanup_closed=True)
    var1334 = mock.Mock()
    var1434._cleanup_closed_handle = var1724 = mock.Mock()
    var1434._cleanup_closed_transports = [var1334]
    var1434._cleanup_closed()
    assert var1334.abort.called
    assert (not var1434._cleanup_closed_transports)
    assert arg1298.call_at.called
    assert var1724.cancel.called

def function2401(arg163, arg808):
    var3239 = aiohttp.BaseConnector(loop=arg163, enable_cleanup_closed=False)
    var571 = mock.Mock()
    var3239._cleanup_closed_transports = [var571]
    var3239._cleanup_closed()
    assert var571.abort.called
    assert (not var3239._cleanup_closed_transports)

def function2692(arg731):
    var3938 = aiohttp.TCPConnector(loop=arg731)
    assert var3938.verify_ssl
    assert (var3938.fingerprint is None)
    assert var3938.use_dns_cache
    assert (var3938.family == 0)
    assert (var3938.cached_hosts == {})

def function2491(arg1596):
    var3447 = b'\xa2\x06G\xad\xaa\xf5\xd8\\J\x99^by;\x06='
    with pytest.warns(DeprecationWarning):
        var1390 = aiohttp.TCPConnector(loop=arg1596, fingerprint=var3447)
    assert (var1390.fingerprint == var3447)

def function446(arg1287):
    var1840 = b'\x00'
    with pytest.raises(ValueError):
        aiohttp.TCPConnector(loop=arg1287, fingerprint=var1840)

def function2062(arg817):
    var975 = aiohttp.TCPConnector(loop=arg817)
    var4031 = ['a', 'b']
    var975._cached_hosts.add(('localhost', 123), var4031)
    var975._cached_hosts.add(('localhost', 124), var4031)
    var975.clear_dns_cache('localhost', 123)
    assert (('localhost', 123) not in var975.cached_hosts)
    var975.clear_dns_cache('localhost', 123)
    assert (('localhost', 123) not in var975.cached_hosts)
    var975.clear_dns_cache()
    assert (var975.cached_hosts == {})

def function1374(arg606):
    var4448 = aiohttp.TCPConnector(loop=arg606)
    with pytest.raises(ValueError):
        var4448.clear_dns_cache('localhost')

def function1808(arg159):
    with pytest.raises(ValueError):
        aiohttp.TCPConnector(verify_ssl=False, ssl_context=ssl.SSLContext(ssl.PROTOCOL_SSLv23), loop=arg159)

def function1948(arg923):
    var1827 = aiohttp.TCPConnector(loop=arg923)
    var157 = var1827.ssl_context
    assert (var157 is var1827.ssl_context)

def function1424(arg760):
    var3936 = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    var4015 = aiohttp.TCPConnector(loop=arg760, ssl_context=var3936)
    assert (var3936 is var4015.ssl_context)

def function2547(arg1576):
    var2564 = mock.Mock()
    var2906 = aiohttp.BaseConnector(loop=arg1576)
    var2906._conns[1] = [(var2564, object())]
    var2906.close()
    assert (not var2906._conns)
    assert var2564.close.called
    assert var2906.closed
    var2906._conns = 'Invalid'
    var2906.close()
    assert var2906.closed

def function488(arg719):
    var967 = aiohttp.BaseConnector(loop=arg719)
    var967._release(1, mock.Mock(should_close=False))
    assert (var967._cleanup_handle is not None)
    var967.close()
    assert (var967._cleanup_handle is None)

def function2713(arg81):
    var2233 = mock.Mock()
    var3169 = aiohttp.BaseConnector(loop=arg81)
    var3169._cleanup_closed_transports.append(var2233)
    var3169.close()
    assert (not var3169._cleanup_closed_transports)
    assert var2233.abort.called
    assert var3169.closed

def function1956(arg534):
    var1804 = aiohttp.BaseConnector(loop=arg534, enable_cleanup_closed=True)
    assert (var1804._cleanup_closed_handle is not None)
    var1804.close()
    assert (var1804._cleanup_closed_handle is None)

def function823():
    var118 = asyncio.new_event_loop()
    asyncio.set_event_loop(var118)
    var1159 = aiohttp.BaseConnector()
    assert (var118 is var1159._loop)
    var118.close()

@asyncio.coroutine
def function2882(arg992, function1139):
    var105 = mock.Mock()
    var105.is_connected.return_value = True
    var1228 = ClientRequest('GET', URL('http://localhost1:80'), loop=arg992, response_class=mock.Mock())
    var50 = aiohttp.BaseConnector(loop=arg992, limit=1)
    var50._conns[function1139] = [(var105, arg992.time())]
    var50._create_connection = mock.Mock()
    var50._create_connection.return_value = helpers.create_future(arg992)
    var50._create_connection.return_value.set_result(var105)
    var2696 = yield from var50.connect(var1228)
    assert (var2696._protocol == var105)
    assert (1 == len(var50._acquired))
    assert (var105 in var50._acquired)
    assert (function1139 in var50._acquired_per_host)
    assert (var105 in var50._acquired_per_host[function1139])
    var2680 = False

    @asyncio.coroutine
    def function301():
        nonlocal acquired
        var4288 = yield from var50.connect(var1228)
        var2680 = True
        assert (1 == len(var50._acquired))
        assert (1 == len(var50._acquired_per_host[function1139]))
        var4288.release()
    var4679 = helpers.ensure_future(function301(), loop=arg992)
    yield from asyncio.sleep(0.01, loop=arg992)
    assert (not var2680)
    var2696.release()
    yield from asyncio.sleep(0, loop=arg992)
    assert acquired
    yield from task
    var50.close()

@asyncio.coroutine
def function2543(arg440, function1139):
    var4520 = mock.Mock()
    var4520.is_connected.return_value = True
    var1008 = ClientRequest('GET', URL('http://localhost1:80'), loop=arg440)
    var4698 = aiohttp.BaseConnector(loop=arg440, limit=1000, limit_per_host=1)
    var4698._conns[function1139] = [(var4520, arg440.time())]
    var4698._create_connection = mock.Mock()
    var4698._create_connection.return_value = helpers.create_future(arg440)
    var4698._create_connection.return_value.set_result(var4520)
    var3298 = False
    var4590 = yield from var4698.connect(var1008)

    @asyncio.coroutine
    def function301():
        nonlocal acquired
        var916 = yield from var4698.connect(var1008)
        var3298 = True
        assert (1 == len(var4698._acquired))
        assert (1 == len(var4698._acquired_per_host[function1139]))
        var916.release()
    var3195 = helpers.ensure_future(function301(), loop=arg440)
    yield from asyncio.sleep(0.01, loop=arg440)
    assert (not var3298)
    var4590.release()
    yield from asyncio.sleep(0, loop=arg440)
    assert acquired
    yield from task
    var4698.close()

@asyncio.coroutine
def function712(arg516, function1139):
    var4045 = mock.Mock()
    var4045.is_connected.return_value = True
    var384 = ClientRequest('GET', URL('http://localhost1:80'), loop=arg516)
    var3117 = aiohttp.BaseConnector(loop=arg516, limit=0, limit_per_host=1)
    var3117._conns[function1139] = [(var4045, arg516.time())]
    var3117._create_connection = mock.Mock()
    var3117._create_connection.return_value = helpers.create_future(arg516)
    var3117._create_connection.return_value.set_result(var4045)
    var4490 = False
    var712 = yield from var3117.connect(var384)

    @asyncio.coroutine
    def function301():
        nonlocal acquired
        var993 = yield from var3117.connect(var384)
        var4490 = True
        var993.release()
    var4482 = helpers.ensure_future(function301(), loop=arg516)
    yield from asyncio.sleep(0.01, loop=arg516)
    assert (not var4490)
    var712.release()
    yield from asyncio.sleep(0, loop=arg516)
    assert acquired
    yield from task
    var3117.close()

@asyncio.coroutine
def function2540(arg1260, function1139):
    var3583 = mock.Mock()
    var3583.is_connected.return_value = True
    var3002 = ClientRequest('GET', URL('http://localhost1:80'), loop=arg1260)
    var742 = aiohttp.BaseConnector(loop=arg1260, limit=0, limit_per_host=0)
    var742._conns[function1139] = [(var3583, arg1260.time())]
    var742._create_connection = mock.Mock()
    var742._create_connection.return_value = helpers.create_future(arg1260)
    var742._create_connection.return_value.set_result(var3583)
    var3355 = False
    var3007 = yield from var742.connect(var3002)

    @asyncio.coroutine
    def function301():
        nonlocal acquired
        var2225 = yield from var742.connect(var3002)
        var3355 = True
        assert (1 == len(var742._acquired))
        assert (1 == len(var742._acquired_per_host[function1139]))
        var2225.release()
    var2804 = helpers.ensure_future(function301(), loop=arg1260)
    yield from asyncio.sleep(0.01, loop=arg1260)
    assert acquired
    var3007.release()
    yield from task
    var742.close()

@asyncio.coroutine
def function2482(arg1887):
    var1803 = mock.Mock()
    var1803.is_connected.return_value = True
    var1828 = ClientRequest('GET', URL('http://host:80'), loop=arg1887)
    var3188 = aiohttp.BaseConnector(loop=arg1887, limit=1)
    function1139 = ('host', 80, False)
    var3188._conns[function1139] = [(var1803, arg1887.time())]
    var3188._create_connection = mock.Mock()
    var3188._create_connection.return_value = helpers.create_future(arg1887)
    var3188._create_connection.return_value.set_result(var1803)
    var907 = yield from var3188.connect(var1828)
    assert (var907._protocol == var1803)
    assert (var907.transport == var1803.transport)
    assert (1 == len(var3188._acquired))
    with pytest.raises(asyncio.TimeoutError):
        yield from asyncio.wait_for(var3188.connect(var1828), 0.01, loop=arg1887)
    var907.close()

@asyncio.coroutine
def function2684(arg572):

    def function2342(arg2275):
        var4270 = aiohttp.BaseConnector(limit=1, loop=arg572)
        var4270._create_connection = mock.Mock()
        var4270._create_connection.return_value = helpers.create_future(arg572)
        var4270._create_connection.return_value.set_exception(arg2275)
        with pytest.raises(Exception):
            var3072 = mock.Mock()
            yield from var4270.connect(var3072)
        assert (not var4270._waiters)
    function2342(OSError(1, 'permission error'))
    function2342(RuntimeError())
    function2342(asyncio.TimeoutError())

@asyncio.coroutine
def function445(arg695):
    var1449 = mock.Mock()
    var1449.should_close = False
    var1449.is_connected.return_value = True
    var908 = ClientRequest('GET', URL('http://host:80'), loop=arg695)
    var363 = 2
    var1227 = 0
    var1057 = aiohttp.BaseConnector(limit=var363, loop=arg695)

    @asyncio.coroutine
    def function108(var908):
        nonlocal num_connections
        var1227 += 1
        yield from asyncio.sleep(0, loop=arg695)
        var1449 = mock.Mock(should_close=False)
        var1449.is_connected.return_value = True
        return var1449
    var1057._create_connection = function108
    var1976 = 10
    var1459 = 0
    var944 = (var363 + 1)

    @asyncio.coroutine
    def function301(arg584=True):
        nonlocal num_requests
        if (var1459 == var1976):
            return
        var1459 += 1
        if (not arg584):
            var1363 = yield from var1057.connect(var908)
            yield from asyncio.sleep(0, loop=arg695)
            var1363.release()
        var4461 = [helpers.ensure_future(function301(start=False), loop=arg695) for var1953 in range(var944)]
        yield from asyncio.wait(var4461, loop=arg695)
    yield from function301()
    var1057.close()
    assert (var363 == var1227)

@asyncio.coroutine
def function2259(arg434):
    var2000 = mock.Mock()
    var2000.is_connected.return_value = True
    var2073 = ClientRequest('GET', URL('http://host:80'), loop=arg434)
    var4176 = aiohttp.BaseConnector(loop=arg434, limit=1)
    function1139 = ('host', 80, False)
    var4176._conns[function1139] = [(var2000, arg434.time())]
    var4176._create_connection = mock.Mock()
    var4176._create_connection.return_value = helpers.create_future(arg434)
    var4176._create_connection.return_value.set_result(var2000)
    var2138 = yield from var4176.connect(var2073)
    assert (1 == len(var4176._acquired))
    var4176.close()
    assert (0 == len(var4176._acquired))
    assert var4176.closed
    var2000.close.assert_called_with()
    assert (not var2138.closed)
    var2138.close()
    assert var2138.closed

def function865(arg575):
    var3762 = aiohttp.BaseConnector(loop=arg575)
    assert (not var3762.force_close)

def function2629(arg2080):
    var2817 = aiohttp.BaseConnector(loop=arg2080, limit=15)
    assert (15 == var2817.limit)
    var2817.close()

def function2243(arg1869):
    var3992 = aiohttp.BaseConnector(loop=arg1869, limit_per_host=15)
    assert (15 == var3992.limit_per_host)
    var3992.close()

def function566(arg1098):
    var2418 = aiohttp.BaseConnector(loop=arg1098)
    assert (var2418.limit == 100)
    var2418.close()

def function1550(arg646):
    var2102 = aiohttp.BaseConnector(loop=arg646)
    assert (var2102.limit_per_host == 0)
    var2102.close()

def function558(arg14):
    with pytest.raises(ValueError):
        aiohttp.BaseConnector(loop=arg14, keepalive_timeout=30, force_close=True)
    var1606 = aiohttp.BaseConnector(loop=arg14, force_close=True, keepalive_timeout=None)
    assert conn
    var1606 = aiohttp.BaseConnector(loop=arg14, force_close=True)
    assert conn

@asyncio.coroutine
def function1502(arg108, arg750):

    @asyncio.coroutine
    def function2076(arg622):
        return web.HTTPOk()
    var134 = web.Application()
    var134.router.add_get('/', function2076)
    var2494 = yield from arg108(var134)
    var4046 = yield from var2494.get('/')
    assert (var4046.status == 200)

def function2285(arg982):
    var2287 = aiohttp.TCPConnector(loop=arg982)
    assert var2287.use_dns_cache


class Class335(unittest.TestCase):

    def function2118(self):
        self.function2076 = None
        self.attribute2155 = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def function704(self):
        if self.function2076:
            self.attribute2155.run_until_complete(self.function2076.finish_connections())
        self.attribute2155.stop()
        self.attribute2155.run_forever()
        self.attribute2155.close()
        gc.collect()

    @asyncio.coroutine
    def function364(self, arg809, arg651, function2076):
        var4478 = web.Application()
        var4478.router.add_route(arg809, arg651, function2076)
        var2497 = unused_port()
        self.function2076 = var4478.make_handler(loop=self.attribute2155, tcp_keepalive=False)
        var1808 = yield from self.attribute2155.function364(self.function2076, '127.0.0.1', var2497)
        var3846 = ('http://127.0.0.1:{}'.format(var2497) + arg651)
        self.addCleanup(var1808.close)
        return (var4478, var1808, var3846)

    @asyncio.coroutine
    def function1842(self, arg669, arg444, function2076):
        var2934 = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, var2934)
        var2915 = web.Application()
        var2915.router.add_route(arg669, arg444, function2076)
        self.function2076 = var2915.make_handler(loop=self.attribute2155, tcp_keepalive=False, access_log=None)
        var2598 = os.arg444.join(var2934, 'socket.sock')
        var4712 = yield from self.attribute2155.function1842(self.function2076, var2598)
        var2852 = ('http://127.0.0.1' + arg444)
        self.addCleanup(var4712.close)
        return (var2915, var4712, var2852, var2598)

    def function629(self):

        @asyncio.coroutine
        def function2076(arg515):
            return web.HTTPOk()
        (var1025, var3974, var3655) = self.attribute2155.run_until_complete(self.function364('get', '/', function2076))
        var3252 = unused_port()
        var3067 = aiohttp.TCPConnector(loop=self.attribute2155, local_addr=('127.0.0.1', var3252))
        var1487 = aiohttp.ClientSession(connector=var3067)
        var4580 = self.attribute2155.run_until_complete(var1487.request('get', var3655))
        var4580.release()
        var4733 = next(iter(var3067._conns.values()))[0][0]
        self.assertEqual(var4733.transport._sock.getsockname(), ('127.0.0.1', var3252))
        var4580.close()
        var1487.close()
        var3067.close()

    @unittest.skipUnless(hasattr(socket, 'AF_UNIX'), 'requires unix')
    def function697(self):

        @asyncio.coroutine
        def function2076(arg2088):
            return web.HTTPOk()
        (var4696, var901, var2948, var3337) = self.attribute2155.run_until_complete(self.function1842('get', '/', function2076))
        var561 = aiohttp.UnixConnector(var3337, loop=self.attribute2155)
        self.assertEqual(var3337, var561.path)
        var3724 = client.ClientSession(connector=var561, loop=self.attribute2155)
        var2317 = self.attribute2155.run_until_complete(var3724.request('get', var2948))
        self.assertEqual(var2317.status, 200)
        var2317.close()
        var3724.close()

    def function2871(self):
        var2476 = mock.MagicMock()
        var1524 = aiohttp.TCPConnector(resolver=var2476, loop=self.attribute2155)
        var3551 = ClientRequest('GET', URL('http://127.0.0.1:{}'.format(unused_port())), loop=self.attribute2155, response_class=mock.Mock())
        with self.assertRaises(OSError):
            self.attribute2155.run_until_complete(var1524.connect(var3551))
        var2476.resolve.assert_not_called()


class Class69:

    @pytest.fixture
    def function1574(self):
        return _DNSCacheTable()

    def function2013(self, function1574):
        function1574.add('localhost', ['127.0.0.1'])
        function1574.add('foo', ['127.0.0.2'])
        assert (function1574.addrs == {'localhost': ['127.0.0.1'], 'foo': ['127.0.0.2'], })

    def function2080(self, function1574):
        function1574.add('localhost', ['127.0.0.1'])
        function1574.remove('localhost')
        assert (function1574.addrs == {})

    def function432(self, function1574):
        function1574.add('localhost', ['127.0.0.1'])
        function1574.clear()
        assert (function1574.addrs == {})

    def function1101(self, function1574):
        function1574.add('localhost', ['127.0.0.1'])
        assert (not function1574.expired('localhost'))

    def function498(self):
        function1574 = _DNSCacheTable(ttl=0.1)
        function1574.add('localhost', ['127.0.0.1'])
        assert (not function1574.expired('localhost'))

    @asyncio.coroutine
    def function1400(self, arg1496):
        function1574 = _DNSCacheTable(ttl=0.01)
        function1574.add('localhost', ['127.0.0.1'])
        yield from asyncio.sleep(0.01, loop=arg1496)
        assert function1574.expired('localhost')

    def function1360(self, function1574):
        function1574.add('foo', ['127.0.0.1', '127.0.0.2'])
        var3474 = list(function1574.next_addrs('foo'))
        assert (var3474 == ['127.0.0.1', '127.0.0.2'])
        var3474 = function1574.next_addrs('foo')
        assert (next(var3474) == '127.0.0.1')
        var3474 = function1574.next_addrs('foo')
        assert (next(var3474) == '127.0.0.2')