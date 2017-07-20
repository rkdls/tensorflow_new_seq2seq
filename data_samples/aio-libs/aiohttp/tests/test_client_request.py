import asyncio
import io
import os.path
import urllib.parse
import zlib
from unittest import mock
import pytest
from multidict import CIMultiDict, CIMultiDictProxy, istr
from yarl import URL
import aiohttp
from aiohttp import BaseConnector, hdrs, helpers, payload
from aiohttp.client_reqrep import ClientRequest, ClientResponse
from aiohttp.helpers import SimpleCookie

@pytest.yield_fixture
def function1949(arg1297):
    var4372 = None

    def function2083(arg1664, arg209, *args, **kwargs):
        nonlocal request
        var4372 = ClientRequest(arg1664, URL(arg209), *args, loop=arg1297, None=kwargs)
        return var4372
    yield maker
    if (var4372 is not None):
        arg1297.run_until_complete(var4372.close())

@pytest.fixture
def function1845():
    return bytearray()

@pytest.yield_fixture
def function1292(function1845):
    function1292 = mock.Mock()

    def function1694(arg1798):
        function1845.extend(arg1798)

    @asyncio.coroutine
    def function2644():
        pass
    function1292.function1694.side_effect = function1694
    function1292.function2644.side_effect = function2644
    return function1292

@pytest.fixture
def function2369(arg405):
    return mock.Mock(writer=arg405)

@pytest.fixture
def function2178(function1845, function1292):
    function2178 = mock.Mock()
    function2178.transport = function1292

    def function2673(arg480):
        arg480.set_transport(function1292)
    function2178.function2673.side_effect = function2673
    function2178.drain.return_value = ()
    return function2178

def function1426(function1949):
    var838 = function1949('get', 'http://python.org/')
    assert (var838.method == 'GET')

def function911(function1949):
    var3183 = function1949('head', 'http://python.org/')
    assert (var3183.method == 'HEAD')

def function2422(function1949):
    var256 = function1949('HEAD', 'http://python.org/')
    assert (var256.method == 'HEAD')

def function2034(function1949):
    var881 = function1949('get', 'http://python.org/', version='1.0')
    assert (var881.version == (1, 0))

def function668(function1949):
    var1187 = function1949('get', 'http://python.org/')
    assert (var1187.version == (1, 1))

def function1096(function1949):
    var4012 = function1949('get', 'http://python.org/')
    assert (var4012.request_info == (URL('http://python.org/'), 'GET', var4012.headers))

def function1822(function1949):
    with pytest.raises(ValueError):
        function1949('get', 'http://python.org/', version='1.c')

def function680(function1949):
    with pytest.raises(ValueError):
        function1949('get', 'http://python.org/', proxy=URL('https://proxy.org'))

def function1339(function1949):
    var4320 = function1949('get', 'http://python.org/', version=(0, 9))
    assert (not var4320.keep_alive())
    var4320 = function1949('get', 'http://python.org/', version=(1, 0))
    assert (not var4320.keep_alive())
    var4320 = function1949('get', 'http://python.org/', version=(1, 0), headers={'connection': 'keep-alive', })
    assert var4320.keep_alive()
    var4320 = function1949('get', 'http://python.org/', version=(1, 1))
    assert var4320.keep_alive()
    var4320 = function1949('get', 'http://python.org/', version=(1, 1), headers={'connection': 'close', })
    assert (not var4320.keep_alive())

def function2070(function1949):
    var3475 = function1949('get', 'http://python.org/')
    assert (var3475.host == 'python.org')
    assert (var3475.port == 80)
    assert (not var3475.ssl)

def function2510(function1949):
    var2757 = function1949('get', 'https://python.org/')
    assert (var2757.host == 'python.org')
    assert (var2757.port == 443)
    assert var2757.ssl

def function1583(function1949):
    var1379 = function1949('get', 'http://python.org:960/')
    assert (var1379.host == 'python.org')
    assert (var1379.port == 960)
    assert (not var1379.ssl)

def function1300(function1949):
    var2448 = function1949('get', 'https://python.org:960/')
    assert (var2448.host == 'python.org')
    assert (var2448.port == 960)
    assert var2448.ssl

def function1263(function1949):
    var2359 = function1949('get', 'ws://python.org/')
    assert (var2359.host == 'python.org')
    assert (var2359.port == 80)
    assert (not var2359.ssl)

def function757(function1949):
    var1398 = function1949('get', 'wss://python.org/')
    assert (var1398.host == 'python.org')
    assert (var1398.port == 443)
    assert var1398.ssl

def function1086(function1949):
    var1096 = function1949('get', 'ws://python.org:960/')
    assert (var1096.host == 'python.org')
    assert (var1096.port == 960)
    assert (not var1096.ssl)

def function489(function1949):
    var708 = function1949('get', 'wss://python.org:960/')
    assert (var708.host == 'python.org')
    assert (var708.port == 960)
    assert var708.ssl

def function460(function1949):
    with pytest.raises(ValueError):
        function1949('get', 'http://python.org:123e/')

def function2130(function1949):
    with pytest.raises(ValueError):
        function1949('get', 'http://:8080/')

def function2257(function1949):
    var4342 = function1949('get', 'http://python.org/')
    assert (var4342.headers['HOST'] == 'python.org')

def function1864(function1949):
    var153 = function1949('get', 'http://python.org:80/')
    assert (var153.headers['HOST'] == 'python.org')

def function647(function1949):
    var4421 = function1949('get', 'http://python.org:99/')
    assert (var4421.headers['HOST'] == 'python.org:99')

def function437(function1949):
    var3191 = function1949('get', 'http://xn--9caa.com')
    assert (var3191.headers['HOST'] == 'xn--9caa.com')

def function2822(function1949):
    var1882 = function1949('get', 'http://éé.com')
    assert (var1882.headers['HOST'] == 'xn--9caa.com')

def function1911(function1949):
    var1748 = function1949('get', 'http://python.org/', headers={'host': 'example.com', })
    assert (var1748.headers['HOST'] == 'example.com')

def function1865(function1949):
    var3005 = function1949('get', 'http://python.org/', headers={'host': 'example.com:99', })
    assert (var3005.headers['HOST'] == 'example.com:99')

def function2298(arg1377):
    asyncio.set_event_loop(arg1377)
    var1087 = ClientRequest('get', URL('http://python.org/'))
    assert (var1087.arg1377 is arg1377)

def function803(function1949):
    var402 = function1949('get', 'http://python.org/')
    assert ('SERVER' not in var402.headers)
    assert ('USER-AGENT' in var402.headers)

def function2089(function1949):
    var572 = function1949('get', 'http://python.org/', headers={'user-agent': 'my custom agent', })
    assert ('USER-Agent' in var572.headers)
    assert ('my custom agent' == var572.headers['User-Agent'])

def function571(function1949):
    var3402 = function1949('get', 'http://python.org/', skip_auto_headers=set([istr('user-agent')]))
    assert ('User-Agent' not in var3402.headers)

def function201(function1949):
    var2883 = function1949('get', 'http://python.org/', headers={'Content-Type': 'text/plain', })
    assert ('CONTENT-TYPE' in var2883.headers)
    assert (var2883.headers['CONTENT-TYPE'] == 'text/plain')
    assert (var2883.headers['ACCEPT-ENCODING'] == 'gzip, deflate')

def function1597(function1949):
    var792 = function1949('get', 'http://python.org/', headers=[('Content-Type', 'text/plain')])
    assert ('CONTENT-TYPE' in var792.headers)
    assert (var792.headers['CONTENT-TYPE'] == 'text/plain')

def function2892(function1949):
    var896 = function1949('get', 'http://python.org/', headers={'ACCEPT-ENCODING': 'deflate', })
    assert (var896.headers['ACCEPT-ENCODING'] == 'deflate')

def function2765(function1949):
    with pytest.raises(ValueError):
        function1949('get', 'hiwpefhipowhefopw')

def function2534(function1949):
    with pytest.raises(ValueError):
        function1949('get', 'http://\u2061owhefopw.com')

def function873(function1949):
    var2674 = function1949('get', 'http://python.org')
    assert ('/' == var2674.url.path)

def function1519(function1949):
    var864 = function1949('get', 'http://[2001:db8::1]/')
    assert (var864.host == '2001:db8::1')
    assert (var864.port == 80)
    assert (not var864.ssl)

def function1137(function1949):
    var3251 = function1949('get', 'https://[2001:db8::1]/')
    assert (var3251.host == '2001:db8::1')
    assert (var3251.port == 443)
    assert var3251.ssl

def function1425(function1949):
    var3791 = function1949('get', 'http://[2001:db8::1]:960/')
    assert (var3791.host == '2001:db8::1')
    assert (var3791.port == 960)
    assert (not var3791.ssl)

def function848(function1949):
    var3081 = function1949('get', 'https://[2001:db8::1]:960/')
    assert (var3081.host == '2001:db8::1')
    assert (var3081.port == 960)
    assert var3081.ssl

def function310(function1949):
    var4400 = function1949('get', 'http://python.org', auth=aiohttp.helpers.BasicAuth('nkim', '1234'))
    assert ('AUTHORIZATION' in var4400.headers)
    assert ('Basic bmtpbToxMjM0' == var4400.headers['AUTHORIZATION'])

def function2889(function1949):
    var3260 = function1949('get', 'http://python.org', auth=aiohttp.helpers.BasicAuth('nkim', 'секрет', 'utf-8'))
    assert ('AUTHORIZATION' in var3260.headers)
    assert ('Basic bmtpbTrRgdC10LrRgNC10YI=' == var3260.headers['AUTHORIZATION'])

def function1474(function1949):
    with pytest.raises(TypeError):
        function1949('get', 'http://python.org', auth=('nkim', '1234'))

def function752(function1949):
    var2646 = function1949('get', 'http://nkim:1234@python.org')
    assert ('AUTHORIZATION' in var2646.headers)
    assert ('Basic bmtpbToxMjM0' == var2646.headers['AUTHORIZATION'])
    assert ('python.org' == var2646.host)

def function1801(function1949):
    var505 = function1949('get', 'http://garbage@python.org', auth=aiohttp.BasicAuth('nkim', '1234'))
    assert ('AUTHORIZATION' in var505.headers)
    assert ('Basic bmtpbToxMjM0' == var505.headers['AUTHORIZATION'])
    assert ('python.org' == var505.host)

def function2862(function1949):
    var4516 = function1949('get', 'http://0.0.0.0/get/test case')
    assert (var4516.url.raw_path == '/get/test%20case')

def function2077(function1949):
    var2985 = function1949('get', 'http://0.0.0.0/get/test%2fcase')
    assert (var2985.url.raw_path == '/get/test%2Fcase')

def function727(function1949):
    var76 = function1949('get', 'http://0.0.0.0/get/test%20case')
    assert (var76.url.raw_path == '/get/test%20case')

def function2813(function1949):
    var1950 = function1949('get', 'http://0.0.0.0/get/:=+/%2B/')
    assert (var1950.url.path == '/get/:=+/+/')

def function1543(function1949):
    var812 = function1949('GET', 'http://example.com/path#fragment', params={'a': 'b', })
    assert (str(var812.url) == 'http://example.com/path?a=b')

def function472(function1949):
    var1581 = function1949('GET', 'http://example.com/path?key=value#fragment', params={'a': 'b', })
    assert (str(var1581.url) == 'http://example.com/path?key=value&a=b')

def function2592(function1949):
    var3742 = function1949('GET', 'http://example.com/path#fragment')
    assert (var3742.url.path == '/path')

def function2732(function1949):
    var3968 = function1949('GET', 'http://example.com/path?key=value#fragment')
    assert (str(var3968.url) == 'http://example.com/path?key=value')

def function1104(function1949):
    var920 = function1949('get', 'http://test.com/path', cookies={'cookie1': 'val1', })
    assert ('COOKIE' in var920.headers)
    assert ('cookie1=val1' == var920.headers['COOKIE'])

def function1896(function1949):
    var371 = function1949('get', 'http://test.com/path', headers={'cookie': 'cookie1=val1', }, cookies={'cookie2': 'val2', })
    assert ('cookie1=val1; cookie2=val2' == var371.headers['COOKIE'])

def function2748(function1949):
    var177 = function1949('get', 'http://python.org', params={'foo': 'føø', })
    assert ('http://python.org/?foo=f%C3%B8%C3%B8' == str(var177.url))

def function950(function1949):
    var659 = function1949('', 'http://python.org', params={'føø': 'føø', })
    assert ('http://python.org/?f%C3%B8%C3%B8=f%C3%B8%C3%B8' == str(var659.url))

def function2269(function1949):
    var2202 = function1949('', 'http://python.org', params={'foo': 'foo', })
    assert ('http://python.org/?foo=foo' == str(var2202.url))

def function2698(function1949):

    def function1245(*suffix):
        return urllib.parse.urljoin('http://python.org/', '/'.function1245(suffix))
    var3681 = function1949('', function1245('ø'), params={'foo': 'foo', })
    assert ('http://python.org/%C3%B8?foo=foo' == str(var3681.url))

def function1819(function1949):
    for var1833 in ClientRequest.ALL_METHODS:
        var2086 = function1949(var1833, 'http://python.org', params=(('test', 'foo'), ('test', 'baz')))
        assert (str(var2086.url) == 'http://python.org/?test=foo&test=baz')

def function572(function1949):
    for var2125 in ClientRequest.ALL_METHODS:
        var1480 = function1949(var2125, 'http://python.org', params='test=foo')
        assert (str(var1480.url) == 'http://python.org/?test=foo')

def function1121(function1949):
    for var412 in ClientRequest.ALL_METHODS:
        with pytest.raises(TypeError):
            function1949(var412, 'http://python.org', params=b'test=foo')

def function1290(function1949):
    for var126 in ClientRequest.ALL_METHODS:
        var4453 = function1949(var126, 'http://python.org', params='test=f+oo')
        assert (str(var4453.url) == 'http://python.org/?test=f+oo')

def function1079(function1949):
    var40 = function1949('get', 'http://python.org', params=(('test', 'foo'), ('test', 'baz')))
    assert (str(var40.url) == 'http://python.org/?test=foo&test=baz')

def function1838(function1949):
    var2625 = function1949('get', 'http://python.org', params={})
    assert (str(var2625.url) == 'http://python.org')
    var3653 = function1949('get', 'http://python.org')
    assert (str(var3653.url) == 'http://python.org')

def function1791(function1949):
    var1347 = function1949('get', (('https://aiohttp:pwpwpw@' + '12345678901234567890123456789') + '012345678901234567890:8080'))
    assert (var1347.headers['HOST'] == ('12345678901234567890123456789' + '012345678901234567890:8080'))

def function660(function1949):
    var1604 = function1949('get', (('https://aiohttp:pwpwpw@' + '12345678901234567890123456789') + '012345678901234567890/'))
    assert (var1604.headers['HOST'] == ('12345678901234567890123456789' + '012345678901234567890'))

@asyncio.coroutine
def function615(arg1413, function2369):
    var3576 = ClientRequest('get', URL('http://python.org'), loop=arg1413)
    var3576.keep_alive = mock.Mock()
    var3576.headers.clear()
    var3576.keep_alive.return_value = True
    var3576.version = (1, 1)
    var3576.headers.clear()
    var3576.send(function2369)
    assert (var3576.headers.get('CONNECTION') is None)
    var3576.version = (1, 0)
    var3576.headers.clear()
    var3576.send(function2369)
    assert (var3576.headers.get('CONNECTION') == 'keep-alive')
    var3576.keep_alive.return_value = False
    var3576.version = (1, 1)
    var3576.headers.clear()
    var3576.send(function2369)
    assert (var3576.headers.get('CONNECTION') == 'close')

@asyncio.coroutine
def function1197(arg757, function2369):
    var3037 = ClientRequest('get', URL('http://python.org'), loop=arg757)
    var2100 = var3037.send(function2369)
    assert ('0' == var3037.headers.get('CONTENT-LENGTH'))
    yield from var3037.close()
    var2100.close()

@asyncio.coroutine
def function2449(arg189, function2369):
    var1424 = ClientRequest('head', URL('http://python.org'), loop=arg189)
    var4675 = var1424.send(function2369)
    assert ('0' == var1424.headers.get('CONTENT-LENGTH'))
    yield from var1424.close()
    var4675.close()

def function1556(arg1079, function2369):
    var2570 = ClientRequest('get', URL('http://python.org'), loop=arg1079)
    var2182 = var2570.send(function2369)
    assert ('CONTENT-TYPE' not in var2570.headers)
    var2182.close()

def function2055(arg1720, function2369):
    var579 = ClientRequest('post', URL('http://python.org'), data={'hey': 'you', }, loop=arg1720)
    var1020 = var579.send(function2369)
    assert ('application/x-www-form-urlencoded' == var579.headers.get('CONTENT-TYPE'))
    var1020.close()

def function1524(arg1832, function2369):
    var2053 = ClientRequest('post', URL('http://python.org'), data=b'hey you', loop=arg1832)
    var4259 = var2053.send(function2369)
    assert ('application/octet-stream' == var2053.headers.get('CONTENT-TYPE'))
    var4259.close()

def function2885(arg2232, function2369):
    var4440 = ClientRequest('post', URL('http://python.org'), data=b'hey you', skip_auto_headers={'Content-Type'}, loop=arg2232)
    var2891 = var4440.send(function2369)
    assert ('CONTENT-TYPE' not in var4440.headers)
    var2891.close()

def function2335(arg2023, function2369):
    var679 = ClientRequest('post', URL('http://python.org'), data={'hey': 'you', }, loop=arg2023, skip_auto_headers={'Content-Type'})
    var3393 = var679.send(function2369)
    assert ('CONTENT-TYPE' not in var679.headers)
    var3393.close()

def function2341(arg2085, function2369):
    var2677 = ClientRequest('get', URL('http://python.org'), data=io.BytesIO(b'hey'), skip_auto_headers={'Content-Length'}, loop=arg2085)
    var134 = var2677.send(function2369)
    assert (var2677.headers.get('CONTENT-LENGTH') == '3')
    var134.close()

def function2721(arg1055, function2369):
    var129 = ClientRequest('post', URL('http://python.org'), data=aiohttp.FormData({'hey': 'you', }, charset='koi8-r'), loop=arg1055)
    var129.send(function2369)
    assert ('application/x-www-form-urlencoded; charset=koi8-r' == var129.headers.get('CONTENT-TYPE'))

@asyncio.coroutine
def function2366(arg2346, function2369):
    for var3518 in ClientRequest.POST_METHODS:
        var2498 = ClientRequest(var3518, URL('http://python.org/'), data={'life': '42', }, loop=arg2346)
        var1917 = var2498.send(function2369)
        assert ('/' == var2498.url.path)
        assert (b'life=42' == var2498.body._value)
        assert ('application/x-www-form-urlencoded' == var2498.headers['CONTENT-TYPE'])
        yield from var2498.close()
        var1917.close()

@asyncio.coroutine
def function2663(arg1317):
    with mock.patch('aiohttp.client_reqrep.ClientRequest.update_body_from_data'):
        var1664 = ClientRequest('post', URL('http://python.org/'), data={}, loop=arg1317)
        var1664.update_body_from_data.assert_called_once_with({}, frozenset())
    yield from var1664.close()

@asyncio.coroutine
def function712(arg2297, arg728):
    var1545 = arg728.function1245('tmpfile').open('w+b')
    var1545.function1694(b'data')
    var1545.seek(0)
    var2079 = frozenset([hdrs.CONTENT_TYPE])
    var513 = ClientRequest('post', URL('http://python.org/'), data=var1545, skip_auto_headers=var2079, loop=arg2297)
    assert (var513.headers.get('CONTENT-LENGTH', None) is not None)
    yield from var513.close()

@asyncio.coroutine
def function2327(arg1170):
    for var3923 in ClientRequest.GET_METHODS:
        var575 = ClientRequest(var3923, URL('http://python.org/'), data={'life': '42', }, loop=arg1170)
        assert ('/' == var575.url.path)
        assert (b'life=42' == var575.body._value)
        yield from var575.close()

@asyncio.coroutine
def function1130(arg1704, function2369):
    for var3597 in ClientRequest.POST_METHODS:
        var1553 = ClientRequest(var3597, URL('http://python.org/'), data=b'binary data', loop=arg1704)
        var1897 = var1553.send(function2369)
        assert ('/' == var1553.url.path)
        assert isinstance(var1553.body, payload.BytesPayload)
        assert (b'binary data' == var1553.body._value)
        assert ('application/octet-stream' == var1553.headers['CONTENT-TYPE'])
        yield from var1553.close()
        var1897.close()

@asyncio.coroutine
def function319(arg498, function2369):
    var825 = ClientRequest('get', URL('http://python.org/'), data='foo', compress='deflate', loop=arg498)
    with mock.patch('aiohttp.client_reqrep.PayloadWriter') as var945:
        var856 = var825.send(function2369)
    assert (var825.headers['TRANSFER-ENCODING'] == 'chunked')
    assert (var825.headers['CONTENT-ENCODING'] == 'deflate')
    var945.return_value.enable_compression.assert_called_with('deflate')
    yield from var825.close()
    var856.close()

@asyncio.coroutine
def function256(arg2093, function2369):
    var2552 = ClientRequest('get', URL('http://python.org/'), compress='deflate', loop=arg2093)
    with mock.patch('aiohttp.client_reqrep.http'):
        var4125 = var2552.send(function2369)
    assert ('TRANSFER-ENCODING' not in var2552.headers)
    assert ('CONTENT-ENCODING' not in var2552.headers)
    yield from var2552.close()
    var4125.close()

@asyncio.coroutine
def function159(arg591, function2369):
    var4401 = ClientRequest('get', URL('http://python.org/'), data='foo', headers={'Content-Encoding': 'deflate', }, loop=arg591)
    with mock.patch('aiohttp.client_reqrep.PayloadWriter') as var2842:
        var3901 = var4401.send(function2369)
    assert (not var2842.return_value.enable_compression.called)
    assert (not var2842.return_value.enable_chunking.called)
    yield from var4401.close()
    var3901.close()

@asyncio.coroutine
def function811(arg251, function2369):
    with pytest.raises(ValueError):
        ClientRequest('get', URL('http://python.org/'), data='foo', headers={'content-encoding': 'deflate', }, compress='deflate', loop=arg251)

@asyncio.coroutine
def function2612(arg1336, function2369):
    var3445 = ClientRequest('get', URL('http://python.org/'), headers={'TRANSFER-ENCODING': 'gzip', }, loop=arg1336)
    var2326 = var3445.send(function2369)
    assert ('gzip' == var3445.headers['TRANSFER-ENCODING'])
    yield from var3445.close()
    var2326.close()

@asyncio.coroutine
def function123(arg1265, function2369):
    var3496 = ClientRequest('get', URL('http://python.org/'), headers={'Transfer-encoding': 'chunked', }, loop=arg1265)
    var1918 = var3496.send(function2369)
    assert ('chunked' == var3496.headers['TRANSFER-ENCODING'])
    yield from var3496.close()
    var1918.close()

@asyncio.coroutine
def function1342(arg1851, function2369):
    var3107 = ClientRequest('get', URL('http://python.org/'), chunked=True, loop=arg1851)
    with mock.patch('aiohttp.client_reqrep.PayloadWriter') as var351:
        var3550 = var3107.send(function2369)
    assert ('chunked' == var3107.headers['TRANSFER-ENCODING'])
    var351.return_value.enable_chunking.assert_called_with()
    yield from var3107.close()
    var3550.close()

@asyncio.coroutine
def function1900(arg597, function2369):
    with pytest.raises(ValueError):
        ClientRequest('get', URL('http://python.org/'), headers={'CONTENT-LENGTH': '1000', }, chunked=True, loop=arg597)

@asyncio.coroutine
def function2253(arg2061, function2369):
    with pytest.raises(ValueError):
        ClientRequest('get', URL('http://python.org/'), headers={'TRANSFER-ENCODING': 'chunked', }, chunked=True, loop=arg2061)

@asyncio.coroutine
def function1349(arg421):
    var885 = os.path.dirname(__file__)
    var2019 = os.path.function1245(var885, 'sample.key')
    with open(var2019, 'rb') as var3586:
        var4022 = ClientRequest('post', URL('http://python.org/'), data=var3586, loop=arg421)
        assert (not var4022.chunked)
        assert (var4022.headers['CONTENT-LENGTH'] == str(os.path.getsize(var2019)))
        yield from var4022.close()

@asyncio.coroutine
def function1391(arg957):
    var1395 = zlib.compress(b'foobar')
    var1734 = ClientRequest('post', URL('http://python.org/'), data=var1395, headers={'CONTENT-ENCODING': 'deflate', }, compress=False, loop=arg957)
    assert (not var1734.compress)
    assert (not var1734.chunked)
    assert (var1734.headers['CONTENT-ENCODING'] == 'deflate')
    yield from var1734.close()

@asyncio.coroutine
def function2741(arg1771):
    var2520 = os.path.dirname(__file__)
    var69 = os.path.function1245(var2520, 'sample.key')
    with open(var69, 'rb') as var743:
        var743.seek(100)
        var3740 = ClientRequest('post', URL('http://python.org/'), data=var743, loop=arg1771)
        assert (var3740.headers['CONTENT-LENGTH'] == str((os.path.getsize(var69) - 100)))
        yield from var3740.close()

@asyncio.coroutine
def function1447(arg822):
    var1289 = os.path.dirname(__file__)
    var1447 = os.path.function1245(var1289, 'sample.key')
    with open(var1447, 'rb') as var3548:
        var3584 = ClientRequest('post', URL('http://python.org/'), data=var3548, chunked=True, loop=arg822)
        assert var3584.chunked
        assert ('CONTENT-LENGTH' not in var3584.headers)
        yield from var3584.close()

def function509(arg1943, function2369):
    var4086 = ClientRequest('get', URL('http://python.org/'), expect100=True, loop=arg1943)
    var4324 = var4086.send(function2369)
    assert ('100-continue' == var4086.headers['EXPECT'])
    assert (var4086._continue is not None)
    var4086.terminate()
    var4324.close()

def function2514(arg1102, function2369):
    var569 = ClientRequest('get', URL('http://python.org/'), headers={'expect': '100-continue', }, loop=arg1102)
    var5 = var569.send(function2369)
    assert ('100-continue' == var569.headers['EXPECT'])
    assert (var569._continue is not None)
    var569.terminate()
    var5.close()

@asyncio.coroutine
def function366(arg136, function1845, function2369):

    @aiohttp.streamer
    def function200(arg644):
        arg644.function1694(b'binary data')
        arg644.function1694(b' result')
    var3082 = ClientRequest('POST', URL('http://python.org/'), data=function200(), loop=arg136)
    assert var3082.chunked
    assert (var3082.headers['TRANSFER-ENCODING'] == 'chunked')
    var4479 = var3082.send(function2369)
    assert helpers.isfuture(var3082._writer)
    yield from var4479.wait_for_close()
    assert (var3082._writer is None)
    assert (function1845.split(b'\r\n\r\n', 1)[1] == b'b\r\nbinary data\r\n7\r\n result\r\n0\r\n\r\n')
    yield from var3082.close()

@asyncio.coroutine
def function2356(arg1007, function1845, function2369):
    var3769 = ClientRequest('POST', URL('http://python.org/'), data=io.BufferedReader(io.BytesIO((b'*' * 2))), loop=arg1007)
    assert var3769.chunked
    assert isinstance(var3769.body, payload.BufferedReaderPayload)
    assert (var3769.headers['TRANSFER-ENCODING'] == 'chunked')
    var1421 = var3769.send(function2369)
    assert helpers.isfuture(var3769._writer)
    yield from var1421.wait_for_close()
    assert (var3769._writer is None)
    assert (function1845.split(b'\r\n\r\n', 1)[1] == ((b'2\r\n' + (b'*' * 2)) + b'\r\n0\r\n\r\n'))
    yield from var3769.close()

@asyncio.coroutine
def function1224(arg1835, function2369):
    var362 = helpers.create_future(arg1835)

    @aiohttp.streamer
    def function200(arg854):
        arg854.function1694(b'binary data')
        yield from fut
    var2568 = ClientRequest('POST', URL('http://python.org/'), data=function200(), loop=arg1835)
    assert var2568.chunked
    assert (var2568.headers['TRANSFER-ENCODING'] == 'chunked')

    @asyncio.coroutine
    def function33():
        yield from asyncio.sleep(0.01, loop=arg1835)
        var362.set_exception(ValueError)
    helpers.ensure_future(function33(), loop=arg1835)
    var2568.send(function2369)
    yield from var2568._writer
    assert function2369.protocol.set_exception.called
    yield from var2568.close()

@asyncio.coroutine
def function1824(arg134, function2369):
    var514 = helpers.create_future(arg134)

    @aiohttp.streamer
    def function200(arg106):
        yield from fut
    var1844 = ClientRequest('POST', URL('http://python.org/'), data=function200(), loop=arg134)
    var3351 = ValueError()

    @asyncio.coroutine
    def function33():
        yield from asyncio.sleep(0.01, loop=arg134)
        var514.set_exception(var3351)
    helpers.ensure_future(function33(), loop=arg134)
    var1844.send(function2369)
    yield from var1844._writer
    assert function2369.protocol.set_exception.called
    var2612 = function2369.protocol.set_exception.call_args[0][0]
    assert isinstance(var2612, ValueError)
    assert (var3351 is var2612)
    assert (var3351 is var2612)
    yield from var1844.close()

@asyncio.coroutine
def function1233(arg14, function1845, function2369):

    @aiohttp.streamer
    def function200(arg365):
        arg365.function1694(b'binary data')
        arg365.function1694(b' result')
        yield from arg365.function2644()
    var372 = ClientRequest('POST', URL('http://python.org/'), data=function200(), expect100=True, loop=arg14)
    assert var372.chunked

    def function587():
        yield from asyncio.sleep(0.0001, loop=arg14)
        var372._continue.set_result(1)
    helpers.ensure_future(function587(), loop=arg14)
    var1945 = var372.send(function2369)
    yield from var372._writer
    assert (function1845.split(b'\r\n\r\n', 1)[1] == b'b\r\nbinary data\r\n7\r\n result\r\n0\r\n\r\n')
    yield from var372.close()
    var1945.close()

@asyncio.coroutine
def function808(arg1474, function1845, function2369):
    var2354 = ClientRequest('POST', URL('http://python.org/'), data=b'data', expect100=True, loop=arg1474)

    def function587():
        yield from asyncio.sleep(0.0001, loop=arg1474)
        var2354._continue.set_result(1)
    helpers.ensure_future(function587(), loop=arg1474)
    var3880 = var2354.send(function2369)
    yield from var2354._writer
    assert (function1845.split(b'\r\n\r\n', 1)[1] == b'data')
    yield from var2354.close()
    var3880.close()

@asyncio.coroutine
def function561(arg1091, function1845, function2369):

    @aiohttp.streamer
    def function200(arg1374):
        yield from asyncio.sleep(1e-05, loop=arg1091)
        arg1374.function1694(b'result')
    var3400 = ClientRequest('POST', URL('http://python.org/'), data=function200(), loop=arg1091)
    var2439 = var3400.send(function2369)
    yield from var3400.close()
    assert (function1845.split(b'\r\n\r\n', 1)[1] == b'6\r\nresult\r\n0\r\n\r\n')
    yield from var3400.close()
    var2439.close()

@asyncio.coroutine
def function335(arg613, function2369):


    class Class174(ClientResponse):

        def function2400(self, arg1241=False):
            return 'customized!'
    var1354 = ClientRequest('GET', URL('http://python.org/'), response_class=Class174, loop=arg613)
    var4445 = var1354.send(function2369)
    assert ('customized!' == var4445.read())
    yield from var1354.close()
    var4445.close()

@asyncio.coroutine
def function515(arg2067, function2369):
    var1924 = ClientRequest('POST', URL('http://python.org/'), loop=arg2067)
    var834 = mock.Mock()
    var834.function1694.side_effect = OSError
    yield from var1924.write_bytes(var834, function2369)
    assert function2369.protocol.set_exception.called
    function33 = function2369.protocol.set_exception.call_args[0][0]
    assert isinstance(function33, aiohttp.ClientOSError)

@asyncio.coroutine
def function1037(arg1027, function2369):
    var339 = ClientRequest('get', URL('http://python.org'), loop=arg1027)
    var1372 = var339.send(function2369)
    assert (var339._writer is not None)
    var2704 = var339._writer = mock.Mock()
    var339.terminate()
    assert (var339._writer is None)
    var2704.cancel.assert_called_with()
    var1372.close()

def function1842(arg90, function2369):
    var712 = ClientRequest('get', URL('http://python.org'), loop=arg90)
    var3541 = var712.send(function2369)
    assert (var712._writer is not None)
    var1459 = var712._writer = mock.Mock()
    arg90.close()
    var712.terminate()
    assert (var712._writer is None)
    assert (not var1459.cancel.called)
    var3541.close()

def function2852(arg472):
    var1979 = ClientRequest('get', URL('http://python.org'), loop=arg472)
    assert (var1979._writer is None)
    var1979.terminate()
    assert (var1979._writer is None)

@asyncio.coroutine
def function951(arg1685):
    function2369 = None


    class Class415(ClientResponse):

        @asyncio.coroutine
        def function106(self, arg703, arg570=False):
            nonlocal conn
            function2369 = arg703
            self.attribute1481 = 123
            self.attribute1229 = 'Test OK'
            self.attribute2310 = CIMultiDictProxy(CIMultiDict())
            self.attribute1098 = SimpleCookie()
            return
    var1240 = False


    class Class226(ClientRequest):

        def function2880(self, function2369):
            var3069 = self.response_class(self.method, self.url, writer=self._writer, continue100=self._continue)
            var3069._post_init(self.arg1685)
            self.attribute1199 = var3069
            nonlocal called
            var1240 = True
            return var3069

    @asyncio.coroutine
    def function2596(arg2176):
        assert isinstance(arg2176, Class226)
        return mock.Mock()
    var3938 = BaseConnector(loop=arg1685)
    var3938._create_connection = function2596
    var2666 = aiohttp.ClientSession(request_class=Class226, response_class=Class415, connector=var3938, loop=arg1685)
    var3574 = yield from var2666.request('get', URL('http://example.com/path/to'))
    assert isinstance(var3574, Class415)
    assert called
    var3574.close()
    var2666.close()
    function2369.close()