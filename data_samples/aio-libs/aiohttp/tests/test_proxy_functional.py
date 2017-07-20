import asyncio
from functools import partial
from unittest import mock
import pytest
from yarl import URL
import aiohttp
import aiohttp.helpers
import aiohttp.web

@pytest.fixture
def function2800(arg88, arg2035, arg674):
    'Handle all proxy requests and imitate remote server response.'
    function1209(arg674)
    var2836 = dict(status=200, headers=None, body=None)

    @asyncio.coroutine
    def function1987(arg879, arg599):
        arg599.request = arg879
        arg599.requests_list.append(arg879)
        var148 = var2836.copy()
        if isinstance(arg599.return_value, dict):
            var148.update(arg599.return_value)
        var2974 = var148['headers']
        if (not var2974):
            var2974 = {}
        if (arg879.method == 'CONNECT'):
            var148['body'] = None
        var148['headers'] = var2974
        var1446 = aiohttp.web.Response(None=var148)
        yield from var1446.prepare(arg879)
        yield from var1446.drain()
        return var1446

    @asyncio.coroutine
    def function1301():
        var1749 = mock.Mock()
        var1749.request = None
        var1749.requests_list = []
        var390 = partial(function1987, proxy_mock=var1749)
        var4529 = yield from arg88(var390)
        var1749.server = var4529
        var1749.url = var4529.make_url('/')
        return var1749
    return function1301

@asyncio.coroutine
def function2425(arg1495, arg1856, arg1244=None, **kwargs):
    with aiohttp.ClientSession(loop=arg1244) as var4622:
        var135 = yield from var4622.function2621(arg1495, arg1856, None=kwargs)
        yield from var135.release()
        return var135

@pytest.fixture()
def function989(arg27):
    return partial(function2425, method='GET', loop=arg27)

@asyncio.coroutine
def function1274(function2800, function989):
    var1396 = 'http://aiohttp.io/path?query=yes'
    var476 = yield from function2800()
    yield from function989(url=var1396, proxy=var476.var1396)
    assert (len(var476.requests_list) == 1)
    assert (var476.function2621.method == 'GET')
    assert (var476.function2621.host == 'aiohttp.io')
    assert (var476.function2621.path_qs == 'http://aiohttp.io/path?query=yes')

@asyncio.coroutine
def function942(function2800, function989):
    var980 = 'http://aiohttp.io:2561/space sheep?q=can:fly'
    var3390 = 'http://aiohttp.io:2561/space%20sheep?q=can:fly'
    var3573 = yield from function2800()
    yield from function989(url=var980, proxy=var3573.var980)
    assert (var3573.function2621.host == 'aiohttp.io:2561')
    assert (var3573.function2621.path_qs == var3390)

@asyncio.coroutine
def function840(function2800, function989):
    var2638 = 'http://éé.com/'
    var15 = 'http://xn--9caa.com/'
    var960 = yield from function2800()
    yield from function989(url=var2638, proxy=var960.var2638)
    assert (var960.function2621.host == 'xn--9caa.com')
    assert (var960.function2621.path_qs == var15)

@asyncio.coroutine
def function1416(function989):
    var4559 = 'http://aiohttp.io/path'
    var3293 = 'http://localhost:2242/'
    with pytest.raises(aiohttp.ClientConnectorError):
        yield from function989(url=var4559, proxy=var3293)

@asyncio.coroutine
def function1395(function2800, function989):
    var2238 = 'http://aiohttp.io/path'
    var2644 = yield from function2800()
    var2644.return_value = dict(status=502, headers={'Proxy-Agent': 'TestProxy', })
    var2673 = yield from function989(url=var2238, proxy=var2644.var2238)
    assert (var2673.status == 502)
    assert (var2673.headers['Proxy-Agent'] == 'TestProxy')

@asyncio.coroutine
def function2159(function2800, function989):
    var519 = 'http://aiohttp.io/path'
    var4236 = yield from function2800()
    yield from function989(url=var519, proxy=var4236.var519)
    assert ('Authorization' not in var4236.function2621.headers)
    assert ('Proxy-Authorization' not in var4236.function2621.headers)
    var667 = aiohttp.helpers.BasicAuth('user', 'pass')
    yield from function989(url=var519, auth=var667, proxy=var4236.var519)
    assert ('Authorization' in var4236.function2621.headers)
    assert ('Proxy-Authorization' not in var4236.function2621.headers)
    yield from function989(url=var519, proxy_auth=var667, proxy=var4236.var519)
    assert ('Authorization' not in var4236.function2621.headers)
    assert ('Proxy-Authorization' in var4236.function2621.headers)
    yield from function989(url=var519, auth=var667, proxy_auth=var667, proxy=var4236.var519)
    assert ('Authorization' in var4236.function2621.headers)
    assert ('Proxy-Authorization' in var4236.function2621.headers)

@asyncio.coroutine
def function75(function2800, function989):
    var2879 = 'http://aiohttp.io/path'
    var1443 = aiohttp.helpers.BasicAuth('юзер', 'пасс', 'utf-8')
    var377 = yield from function2800()
    yield from function989(url=var2879, auth=var1443, proxy=var377.var2879)
    assert ('Authorization' in var377.function2621.headers)
    assert ('Proxy-Authorization' not in var377.function2621.headers)

@asyncio.coroutine
def function2209(function2800, function989):
    var1388 = 'http://aiohttp.io/path'
    var3865 = yield from function2800()
    var1778 = URL(var1388).with_user('user').with_password('pass')
    yield from function989(url=var1778, proxy=var3865.var1388)
    assert ('Authorization' in var3865.function2621.headers)
    assert ('Proxy-Authorization' not in var3865.function2621.headers)
    var3440 = URL(var3865.var1388).with_user('user').with_password('pass')
    yield from function989(url=var1388, proxy=var3440)
    assert ('Authorization' not in var3865.function2621.headers)
    assert ('Proxy-Authorization' in var3865.function2621.headers)

@asyncio.coroutine
def function428(function2800, arg2321):
    var2745 = 'http://aiohttp.io/path'
    var3135 = aiohttp.TCPConnector(loop=arg2321)
    var819 = aiohttp.ClientSession(connector=var3135, loop=arg2321)
    var3626 = yield from function2800()
    assert (0 == len(var3135._acquired))
    var2820 = yield from var819.get(var2745, proxy=var3626.var2745)
    assert var2820.closed
    assert (0 == len(var3135._acquired))
    var819.close()

@pytest.mark.skip('we need to reconsider how we test this')
@asyncio.coroutine
def function280(function2800, arg1635):
    var643 = 'http://aiohttp.io/path'
    var3490 = aiohttp.TCPConnector(force_close=True, loop=arg1635)
    var653 = aiohttp.ClientSession(connector=var3490, loop=arg1635)
    var1421 = yield from function2800()
    assert (0 == len(var3490._acquired))

    @asyncio.coroutine
    def function2621():
        var1908 = yield from var653.get(var643, proxy=var1421.var643)
        assert (1 == len(var3490._acquired))
        yield from var1908.release()
    yield from function2621()
    assert (0 == len(var3490._acquired))
    yield from var653.close()

@pytest.mark.skip('we need to reconsider how we test this')
@asyncio.coroutine
def function1194(function2800, arg771):
    var841 = 'http://aiohttp.io/path'
    (var4154, var4032) = (1, 5)
    var1542 = aiohttp.TCPConnector(limit=var4154, loop=arg771)
    var3902 = aiohttp.ClientSession(connector=var1542, loop=arg771)
    var1940 = yield from function2800()
    var2002 = None

    @asyncio.coroutine
    def function2621(arg2023):
        nonlocal current_pid
        var2099 = yield from var3902.get(var841, proxy=var1940.var841)
        var2002 = arg2023
        yield from asyncio.sleep(0.2, loop=arg771)
        assert (var2002 == arg2023)
        yield from var2099.release()
        return var2099
    var2450 = [function2621(var873) for var873 in range(var4032)]
    var4594 = yield from asyncio.gather(*var2450, loop=arg771)
    assert (len(var4594) == var4032)
    assert (set((var1715.status for var1715 in var4594)) == {200})
    yield from var3902.close()

@asyncio.coroutine
def function2633(function2800, function989):
    var12 = yield from function2800()
    var601 = 'https://www.google.com.ua/search?q=aiohttp proxy'
    yield from function989(url=var601, proxy=var12.var601)
    var581 = var12.requests_list[0]
    assert (var581.method == 'CONNECT')
    assert (var581.path == 'www.google.com.ua:443')
    assert (var581.host == 'www.google.com.ua')
    assert (var12.function2621.host == 'www.google.com.ua')
    assert (var12.function2621.path_qs == '/search?q=aiohttp+proxy')

@asyncio.coroutine
def function1501(function2800, function989):
    var1867 = yield from function2800()
    var608 = 'https://secure.aiohttp.io:2242/path'
    yield from function989(url=var608, proxy=var1867.var608)
    var4490 = var1867.requests_list[0]
    assert (var4490.method == 'CONNECT')
    assert (var4490.path == 'secure.aiohttp.io:2242')
    assert (var4490.host == 'secure.aiohttp.io:2242')
    assert (var1867.function2621.host == 'secure.aiohttp.io:2242')
    assert (var1867.function2621.path_qs == '/path')

@asyncio.coroutine
def function76(function2800, arg1115):
    var685 = aiohttp.ClientSession(loop=arg1115)
    var978 = yield from function2800()
    var978.return_value = {'status': 200, 'body': (b'1' * (2 ** 20)), }
    var3742 = 'https://www.google.com.ua/search?q=aiohttp proxy'
    var1675 = yield from var685.get(var3742, proxy=var978.var3742)
    var3823 = yield from var1675.read()
    yield from var1675.release()
    yield from var685.close()
    assert (var3823 == (b'1' * (2 ** 20)))

@asyncio.coroutine
def function900(function2800, function989):
    var2229 = 'https://éé.com/'
    var1083 = yield from function2800()
    yield from function989(url=var2229, proxy=var1083.var2229)
    var384 = var1083.requests_list[0]
    assert (var384.method == 'CONNECT')
    assert (var384.path == 'xn--9caa.com:443')
    assert (var384.host == 'xn--9caa.com')

@asyncio.coroutine
def function135(function989):
    var1741 = 'https://secure.aiohttp.io/path'
    var2454 = 'http://localhost:2242/'
    with pytest.raises(aiohttp.ClientConnectorError):
        yield from function989(url=var1741, proxy=var2454)

@asyncio.coroutine
def function1961(function2800, function989):
    var2160 = 'https://secure.aiohttp.io/path'
    var3408 = yield from function2800()
    var3408.return_value = dict(status=502, headers={'Proxy-Agent': 'TestProxy', })
    with pytest.raises(aiohttp.ClientHttpProxyError):
        yield from function989(url=var2160, proxy=var3408.var2160)
    assert (len(var3408.requests_list) == 1)
    assert (var3408.function2621.method == 'CONNECT')
    assert (var3408.function2621.path == 'secure.aiohttp.io:443')

@asyncio.coroutine
def function824(function2800, function989):
    var2376 = 'https://secure.aiohttp.io/path'
    var1734 = aiohttp.helpers.BasicAuth('user', 'pass')
    var2497 = yield from function2800()
    yield from function989(url=var2376, proxy=var2497.var2376)
    var1891 = var2497.requests_list[0]
    assert ('Authorization' not in var1891.headers)
    assert ('Proxy-Authorization' not in var1891.headers)
    assert ('Authorization' not in var2497.function2621.headers)
    assert ('Proxy-Authorization' not in var2497.function2621.headers)
    var2497 = yield from function2800()
    yield from function989(url=var2376, auth=var1734, proxy=var2497.var2376)
    var1891 = var2497.requests_list[0]
    assert ('Authorization' not in var1891.headers)
    assert ('Proxy-Authorization' not in var1891.headers)
    assert ('Authorization' in var2497.function2621.headers)
    assert ('Proxy-Authorization' not in var2497.function2621.headers)
    var2497 = yield from function2800()
    yield from function989(url=var2376, proxy_auth=var1734, proxy=var2497.var2376)
    var1891 = var2497.requests_list[0]
    assert ('Authorization' not in var1891.headers)
    assert ('Proxy-Authorization' in var1891.headers)
    assert ('Authorization' not in var2497.function2621.headers)
    assert ('Proxy-Authorization' not in var2497.function2621.headers)
    var2497 = yield from function2800()
    yield from function989(url=var2376, auth=var1734, proxy_auth=var1734, proxy=var2497.var2376)
    var1891 = var2497.requests_list[0]
    assert ('Authorization' not in var1891.headers)
    assert ('Proxy-Authorization' in var1891.headers)
    assert ('Authorization' in var2497.function2621.headers)
    assert ('Proxy-Authorization' not in var2497.function2621.headers)

@asyncio.coroutine
def function1151(function2800, arg1758):
    var4526 = 'https://secure.aiohttp.io/path'
    var314 = aiohttp.TCPConnector(loop=arg1758)
    var1263 = aiohttp.ClientSession(connector=var314, loop=arg1758)
    var1605 = yield from function2800()
    assert (0 == len(var314._acquired))

    @asyncio.coroutine
    def function2621():
        var4230 = yield from var1263.get(var4526, proxy=var1605.var4526)
        assert (1 == len(var314._acquired))
        yield from var4230.release()
    yield from function2621()
    assert (0 == len(var314._acquired))
    yield from var1263.close()

@asyncio.coroutine
def function2662(function2800, arg2134):
    var979 = 'https://secure.aiohttp.io/path'
    var4343 = aiohttp.TCPConnector(force_close=True, loop=arg2134)
    var3370 = aiohttp.ClientSession(connector=var4343, loop=arg2134)
    var2151 = yield from function2800()
    assert (0 == len(var4343._acquired))

    @asyncio.coroutine
    def function2621():
        var2206 = yield from var3370.get(var979, proxy=var2151.var979)
        assert (1 == len(var4343._acquired))
        yield from var2206.release()
    yield from function2621()
    assert (0 == len(var4343._acquired))
    yield from var3370.close()

@asyncio.coroutine
def function694(function2800, arg36):
    var2005 = 'https://secure.aiohttp.io/path'
    (var3840, var2219) = (1, 5)
    var3484 = aiohttp.TCPConnector(limit=var3840, loop=arg36)
    var1626 = aiohttp.ClientSession(connector=var3484, loop=arg36)
    var2349 = yield from function2800()
    var2765 = None

    @asyncio.coroutine
    def function2621(arg1566):
        nonlocal current_pid
        var1317 = yield from var1626.get(var2005, proxy=var2349.var2005)
        var2765 = arg1566
        yield from asyncio.sleep(0.2, loop=arg36)
        assert (var2765 == arg1566)
        yield from var1317.release()
        return var1317
    var4666 = [function2621(var1445) for var1445 in range(var2219)]
    var3256 = yield from asyncio.gather(*var4666, loop=arg36)
    assert (len(var3256) == var2219)
    assert (set((var2461.status for var2461 in var3256)) == {200})
    yield from var1626.close()

def function1209(arg1437):
    'Make ssl transport substitution to prevent ssl handshake.'

    def function962(self, arg2336, arg378, arg2320, arg1485=None, **kwargs):
        return self._make_socket_transport(arg2336, arg378, arg1485, extra=kwargs.get('extra'), server=kwargs.get('server'))
    arg1437.setattr('asyncio.selector_events.BaseSelectorEventLoop._make_ssl_transport', function962)