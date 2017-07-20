import asyncio
import contextlib
import gc
import re
import types
from unittest import mock
import pytest
from multidict import CIMultiDict, MultiDict
from yarl import URL
import aiohttp
from aiohttp import web
from aiohttp.client import ClientSession
from aiohttp.connector import BaseConnector, TCPConnector
from aiohttp.helpers import SimpleCookie

@pytest.fixture
def function647(arg2195):
    var3554 = BaseConnector(loop=arg2195)
    var1840 = mock.Mock()
    var3554._conns['a'] = [(var1840, 123)]
    return var3554

@pytest.yield_fixture
def function1293(arg2329):
    var1864 = None

    def function735(*args, **kwargs):
        nonlocal session
        var1864 = ClientSession(*args, loop=arg2329, None=kwargs)
        return var1864
    yield maker
    if (var1864 is not None):
        var1864.close()

@pytest.fixture
def function1750(function1293):
    return function1293()

@pytest.fixture
def function1034():
    return dict(headers={'Authorization': 'Basic ...', }, max_redirects=2, encoding='latin1', version=aiohttp.HttpVersion10, compress='deflate', chunked=True, expect100=True, read_until_eof=False)

@asyncio.coroutine
def function2206(function1293):
    function1750 = function1293()
    with pytest.warns(DeprecationWarning):
        yield from function1750.close()

def function357(function1293):
    function1750 = function1293(headers={'h1': 'header1', 'h2': 'header2', })
    assert (sorted(function1750._default_headers.items()) == [('H1', 'header1'), ('H2', 'header2')])

def function928(function1293):
    function1750 = function1293(headers=[('h1', 'header1'), ('h2', 'header2'), ('h3', 'header3')])
    assert (function1750._default_headers == CIMultiDict([('h1', 'header1'), ('h2', 'header2'), ('h3', 'header3')]))

def function1988(function1293):
    function1750 = function1293(headers=MultiDict([('h1', 'header1'), ('h2', 'header2'), ('h3', 'header3')]))
    assert (function1750._default_headers == CIMultiDict([('H1', 'header1'), ('H2', 'header2'), ('H3', 'header3')]))

def function1106(function1293):
    function1750 = function1293(headers=[('h1', 'header11'), ('h2', 'header21'), ('h1', 'header12')])
    assert (function1750._default_headers == CIMultiDict([('H1', 'header11'), ('H2', 'header21'), ('H1', 'header12')]))

def function506(function1293):
    function1750 = function1293(cookies={'c1': 'cookie1', 'c2': 'cookie2', })
    var1088 = function1750.cookie_jar.filter_cookies()
    assert (set(var1088) == {'c1', 'c2'})
    assert (var1088['c1'].value == 'cookie1')
    assert (var1088['c2'].value == 'cookie2')

def function2186(function1293):
    function1750 = function1293(cookies=[('c1', 'cookie1'), ('c2', 'cookie2')])
    var3328 = function1750.cookie_jar.filter_cookies()
    assert (set(var3328) == {'c1', 'c2'})
    assert (var3328['c1'].value == 'cookie1')
    assert (var3328['c2'].value == 'cookie2')

def function1917(function1293):
    function1750 = function1293(headers={'h1': 'header1', 'h2': 'header2', })
    var3670 = function1750._prepare_headers({'h1': 'h1', })
    assert isinstance(var3670, CIMultiDict)
    assert (var3670 == CIMultiDict([('h2', 'header2'), ('h1', 'h1')]))

def function960(function1293):
    function1750 = function1293(headers={'h1': 'header1', 'h2': 'header2', })
    var2616 = function1750._prepare_headers(MultiDict([('h1', 'h1')]))
    assert isinstance(var2616, CIMultiDict)
    assert (var2616 == CIMultiDict([('h2', 'header2'), ('h1', 'h1')]))

def function2305(function1293):
    function1750 = function1293(headers={'h1': 'header1', 'h2': 'header2', })
    var1194 = function1750._prepare_headers([('h1', 'h1')])
    assert isinstance(var1194, CIMultiDict)
    assert (var1194 == CIMultiDict([('h2', 'header2'), ('h1', 'h1')]))

def function1057(function1293):
    function1750 = function1293(headers={'h1': 'header1', 'h2': 'header2', })
    var3044 = function1750._prepare_headers([('h1', 'v1'), ('h1', 'v2')])
    assert isinstance(var3044, CIMultiDict)
    assert (var3044 == CIMultiDict([('H2', 'header2'), ('H1', 'v1'), ('H1', 'v2')]))

def function866(function1750, function1034):
    with mock.patch('aiohttp.client.ClientSession._request') as var3261:
        function1750.get('http://test.example.com', params={'x': 1, }, None=function1034)
    assert var3261.called, '`ClientSession._request` not called'
    assert (list(var3261.call_args) == [('GET', 'http://test.example.com'), dict(params={'x': 1, }, allow_redirects=True, None=function1034)])

def function809(function1750, function1034):
    with mock.patch('aiohttp.client.ClientSession._request') as var3186:
        function1750.options('http://opt.example.com', params={'x': 2, }, None=function1034)
    assert var3186.called, '`ClientSession._request` not called'
    assert (list(var3186.call_args) == [('OPTIONS', 'http://opt.example.com'), dict(params={'x': 2, }, allow_redirects=True, None=function1034)])

def function2874(function1750, function1034):
    with mock.patch('aiohttp.client.ClientSession._request') as var3637:
        function1750.head('http://head.example.com', params={'x': 2, }, None=function1034)
    assert var3637.called, '`ClientSession._request` not called'
    assert (list(var3637.call_args) == [('HEAD', 'http://head.example.com'), dict(params={'x': 2, }, allow_redirects=False, None=function1034)])

def function2687(function1750, function1034):
    with mock.patch('aiohttp.client.ClientSession._request') as var2990:
        function1750.post('http://post.example.com', params={'x': 2, }, data='Some_data', None=function1034)
    assert var2990.called, '`ClientSession._request` not called'
    assert (list(var2990.call_args) == [('POST', 'http://post.example.com'), dict(params={'x': 2, }, data='Some_data', None=function1034)])

def function2396(function1750, function1034):
    with mock.patch('aiohttp.client.ClientSession._request') as var308:
        function1750.put('http://put.example.com', params={'x': 2, }, data='Some_data', None=function1034)
    assert var308.called, '`ClientSession._request` not called'
    assert (list(var308.call_args) == [('PUT', 'http://put.example.com'), dict(params={'x': 2, }, data='Some_data', None=function1034)])

def function2299(function1750, function1034):
    with mock.patch('aiohttp.client.ClientSession._request') as var3280:
        function1750.patch('http://patch.example.com', params={'x': 2, }, data='Some_data', None=function1034)
    assert var3280.called, '`ClientSession._request` not called'
    assert (list(var3280.call_args) == [('PATCH', 'http://patch.example.com'), dict(params={'x': 2, }, data='Some_data', None=function1034)])

def function1819(function1750, function1034):
    with mock.patch('aiohttp.client.ClientSession._request') as var1578:
        function1750.delete('http://delete.example.com', params={'x': 2, }, None=function1034)
    assert var1578.called, '`ClientSession._request` not called'
    assert (list(var1578.call_args) == [('DELETE', 'http://delete.example.com'), dict(params={'x': 2, }, None=function1034)])

def function1360(function1293, function647):
    function1750 = function1293(connector=function647)
    function1750.close()
    assert (function1750.function647 is None)
    assert function647.closed

def function2398(function1750):
    assert (not function1750.closed)
    function1750.close()
    assert function1750.closed

def function141(function1293, arg1054, arg38):
    function647 = TCPConnector(loop=arg1054)
    arg38.spy(function647, 'close')
    function1750 = function1293(connector=function647)
    assert (function1750.function647 is function647)
    function1750.close()
    assert function647.close.called
    function647.close()

def function2254(function1293, arg614, arg2067):
    function1750 = function1293()
    function647 = function1750.function647
    arg2067.spy(function1750.function647, 'close')
    function1750.close()
    assert function647.close.called

def function522(arg1948):
    with contextlib.ExitStack() as var745:
        var557 = asyncio.new_event_loop()
        var745.enter_context(contextlib.closing(var557))
        function647 = TCPConnector(loop=var557)
        var745.enter_context(contextlib.closing(function647))
        with pytest.raises(RuntimeError) as var4549:
            ClientSession(connector=function647, loop=arg1948)
        assert re.match('Session and connector has to use same event loop', str(var4549.value))

def function2872(function1750):
    var626 = function1750.function647
    try:
        assert (not var626.closed)
        function1750.detach()
        assert (function1750.function647 is None)
        assert function1750.closed
        assert (not var626.closed)
    finally:
        var626.close()

@asyncio.coroutine
def function1408(function1750):
    function1750.close()
    with pytest.raises(RuntimeError):
        yield from function1750.request('get', '/')

def function2127(function1750):
    var4491 = function1750.function647
    assert (not function1750.closed)
    var4491.close()
    assert function1750.closed

def function176(function647, function1293):
    function1750 = function1293(connector=function647)
    function1750.close()
    assert (function1750.function647 is None)
    function1750.close()
    assert function1750.closed
    assert function647.closed

def function2052(function647, arg1666):
    function1750 = ClientSession(connector=function647, loop=arg1666)
    arg1666.set_exception_handler((lambda arg1666, arg516: None))
    with pytest.warns(ResourceWarning):
        del session
        gc.collect()

def function1873(function647, arg1538):
    with ClientSession(loop=arg1538, connector=function647) as function1750:
        pass
    assert function1750.closed

def function546(function647, function1293, arg1193):
    function1750 = ClientSession(connector=function647, loop=None)
    try:
        assert function1750._loop, loop
    finally:
        function1750.close()

@asyncio.coroutine
def function491(function1293):
    var3143 = OSError(1, 'permission error')
    var647 = mock.Mock()
    var87 = mock.Mock(return_value=var647)
    var647.send = mock.Mock(side_effect=var3143)
    function1750 = function1293(request_class=var87)

    @asyncio.coroutine
    def function98(var647):
        return mock.Mock()
    function1750._connector._create_connection = function98
    with pytest.raises(aiohttp.ClientOSError) as var582:
        yield from function1750.request('get', 'http://example.com')
    var3295 = var582.value
    assert (var3295.errno == var3143.errno)
    assert (var3295.strerror == var3143.strerror)

@asyncio.coroutine
def function2899(arg397):
    yield from asyncio.sleep(0, loop=arg397)
    with aiohttp.ClientSession(loop=arg397) as var1023:
        var790 = var1023.get('http://example.com')
        next(var790)
        assert isinstance(var790.gi_frame, types.FrameType)
        assert (not var790.gi_running)
        assert isinstance(var790.gi_code, types.CodeType)
        yield from asyncio.sleep(0.1, loop=arg397)

@asyncio.coroutine
def function430(arg1293, arg1134):
    var1006 = None
    var2622 = mock.Mock()
    var2622.filter_cookies.return_value = None

    @asyncio.coroutine
    def function2386(arg848):
        nonlocal req_url
        var1006 = ('http://%s/' % arg848.host)
        var3943 = web.Response()
        var3943.set_cookie('response', 'resp_value')
        return var3943
    var3241 = web.Application()
    var3241.router.add_route('GET', '/', function2386)
    function1750 = yield from arg1134(var3241, cookies={'request': 'req_value', }, cookie_jar=var2622)
    var2622.update_cookies.assert_called_with({'request': 'req_value', })
    var2622.update_cookies.reset_mock()
    var1885 = yield from function1750.get('/')
    yield from var1885.release()
    var2622.filter_cookies.assert_called_with(URL(var1006))
    assert var2622.update_cookies.called
    var2299 = var2622.update_cookies.call_args[0][0]
    assert isinstance(var2299, SimpleCookie)
    assert ('response' in var2299)
    assert (var2299['response'].value == 'resp_value')

def function1155(arg1079):
    function1750 = aiohttp.ClientSession(loop=arg1079)
    assert (function1750.version == aiohttp.HttpVersion11)

def function1052(arg1600):
    function1750 = aiohttp.ClientSession(loop=arg1600)
    assert (function1750.arg1600 is arg1600)
    function1750.close()

def function1007(function1750, function1034):
    with mock.patch('aiohttp.client.ClientSession._request') as var1990:
        function1750.get('http://test.example.com', proxy='http://proxy.com', None=function1034)
    assert var1990.called, '`ClientSession._request` not called'
    assert (list(var1990.call_args) == [('GET', 'http://test.example.com'), dict(allow_redirects=True, proxy='http://proxy.com', None=function1034)])

def function2364():
    var22 = asyncio.new_event_loop()
    asyncio.set_event_loop(var22)
    with pytest.warns(ResourceWarning):
        function1750 = aiohttp.ClientSession()
        assert (function1750._loop is var22)
        function1750.close()
    asyncio.set_event_loop(None)
    var22.close()