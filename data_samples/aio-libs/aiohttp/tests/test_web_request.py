import asyncio
from collections import MutableMapping
from unittest import mock
import pytest
from multidict import CIMultiDict, MultiDict
from yarl import URL
from aiohttp import HttpVersion
from aiohttp.streams import StreamReader
from aiohttp.test_utils import make_mocked_request
from aiohttp.web import HTTPRequestEntityTooLarge

@pytest.fixture
def function145():
    return make_mocked_request

def function1345(function145):
    var363 = function145('GET', '/path/to?a=1&b=2')
    assert ('GET' == var363.method)
    assert (HttpVersion(1, 1) == var363.version)
    assert (var363.host is None)
    assert ('/path/to?a=1&b=2' == var363.path_qs)
    assert ('/path/to' == var363.path)
    assert ('a=1&b=2' == var363.query_string)
    assert (CIMultiDict() == var363.var2510)
    assert (() == var363.raw_headers)
    assert (var363.message == var363._message)
    var4283 = var363.query
    assert (MultiDict([('a', '1'), ('b', '2')]) == var4283)
    assert (var4283 is var363.query)
    assert var363.keep_alive
    var2510 = CIMultiDict(FOO='bar')
    var2627 = mock.Mock()
    var3447 = mock.Mock()
    var3251 = mock.Mock()
    var363 = function145('GET', '/path/to?a=1&b=2', headers=var2510, protocol=var3447, payload=var2627, app=var3251)
    assert (var363.var3251 is var3251)
    assert (var363.content is var2627)
    assert (var363.var3447 is var3447)
    assert (var363.transport is var3447.transport)
    assert (var363.var2510 == var2510)
    assert (var363.raw_headers == ((b'Foo', b'bar'),))
    assert (var363.task is var363._task)
    with pytest.warns(DeprecationWarning):
        assert (var363.GET is var363.query)

def function2585(function145):
    var3191 = function145('GET', '/bar//foo/')
    assert ('/bar//foo/' == var3191.path)

def function1600(function145):
    var2327 = function145('Get', '/')
    assert ('application/octet-stream' == var2327.content_type)

def function479(function145):
    var3604 = function145('Get', '/', CIMultiDict([('CONTENT-TYPE', 'application/json')]))
    assert ('application/json' == var3604.content_type)

def function2488(function145):
    var1452 = function145('Get', '/', CIMultiDict([('CONTENT-TYPE', 'text/html; charset=UTF-8')]))
    assert ('text/html' == var1452.content_type)
    assert ('UTF-8' == var1452.charset)

def function502(function145):
    var3038 = function145('Get', '/', CIMultiDict([('CONTENT-TYPE', 'text/html; charset=UTF-8')]))
    assert ('UTF-8' == var3038.charset)
    assert ('text/html' == var3038.content_type)

def function928(function145):
    var1657 = function145('GET', '/yandsearch?text=%D1%82%D0%B5%D0%BA%D1%81%D1%82')
    assert ({'text': 'текст', } == var1657.query)

def function2166(function145):
    var800 = function145('GET', '/путь')
    assert ('/путь' == var800.path)

def function1073(function145):
    var1042 = function145('GET', '/путь')
    assert ('/путь' == var1042.raw_path)

def function1625(function145):
    var4346 = function145('Get', '/', CIMultiDict([('CONTENT-LENGTH', '123')]))
    assert (123 == var4346.content_length)

def function281(function145):
    var4591 = function145('GET', '/', version=HttpVersion(1, 0))
    assert (not var4591.keep_alive)

def function422(function145):
    var3920 = function145('GET', '/', closing=True)
    assert (not var3920.keep_alive)

@asyncio.coroutine
def function1852(function145):
    var1871 = function145('GET', '/')
    var3478 = yield from var1871.post()
    assert (CIMultiDict() == var3478)

@asyncio.coroutine
def function1182(function145):
    var4065 = function145('POST', '/', headers=CIMultiDict({'CONTENT-TYPE': 'something/weird', }))
    var2641 = yield from var4065.post()
    assert (CIMultiDict() == var2641)

@asyncio.coroutine
def function408(function145):
    var4537 = function145('GET', '/')
    var2625 = yield from var4537.post()
    var3022 = yield from var4537.post()
    assert (var2625 is var3022)

def function1367(function145):
    var3037 = function145('GET', '/')
    assert (var3037.var4730 == {})
    var4730 = var3037.var4730
    assert (var4730 is var3037.var4730)

def function569(function145):
    var3404 = CIMultiDict(COOKIE='cookie1=value1; cookie2=value2')
    var747 = function145('GET', '/', headers=var3404)
    assert (var747.cookies == {'cookie1': 'value1', 'cookie2': 'value2', })

def function2355(function145):
    var3949 = CIMultiDict(COOKIE='name=value')
    var2899 = function145('GET', '/', headers=var3949)
    assert (var2899.cookies == {'name': 'value', })
    with pytest.raises(TypeError):
        var2899.cookies['my'] = 'value'

def function2745(function145):
    var2917 = function145('GET', '/')
    assert (var2917._match_info is var2917.match_info)

def function1024(function145):
    var327 = function145('GET', '/')
    assert isinstance(var327, MutableMapping)
    var327['key'] = 'value'
    assert ('value' == var327['key'])

def function1022(function145):
    var3950 = function145('GET', '/')
    var3950['key'] = 'value'
    assert ('value' == var3950['key'])
    del var3950['key']
    assert ('key' not in var3950)

def function2844(function145):
    var1189 = function145('GET', '/')
    assert (len(var1189) == 0)
    var1189['key'] = 'value'
    assert (len(var1189) == 1)

def function1707(function145):
    var3338 = function145('GET', '/')
    var3338['key'] = 'value'
    var3338['key2'] = 'value2'
    assert (set(var3338) == {'key', 'key2'})

def function2768(function145):
    var3127 = function145('GET', '/path/to')
    assert ('<Request GET /path/to >' == repr(var3127))

def function2442(function145):
    var511 = function145('GET', '/path/🐕🌈')
    assert ('<Request GET /path/\\U0001f415\\U0001f308 >' == repr(var511))

def function496(function145):
    var1954 = function145('GET', '/')
    assert ('http' == var1954.scheme)
    assert (var1954.secure is False)

def function1178(function145):
    var1603 = function145('GET', '/', sslcontext=True)
    assert ('https' == var1603.scheme)
    assert (var1603.secure is True)

def function571(function145):
    var2587 = function145('GET', '/', secure_proxy_ssl_header=('X-HEADER', '1'), headers=CIMultiDict({'X-HEADER': '1', }))
    assert ('https' == var2587.scheme)
    assert (var2587.secure is True)

def function473(function145):
    var971 = function145('GET', '/', secure_proxy_ssl_header=('X-HEADER', '1'), headers=CIMultiDict({'X-HEADER': '0', }))
    assert ('http' == var971.scheme)
    assert (var971.secure is False)

def function2593(function145):
    var3462 = 'by=identifier;for=identifier;host=identifier;proto=identifier'
    var296 = function145('GET', '/', headers=CIMultiDict({'Forwarded': header, }))
    assert (var296.forwarded[0]['by'] == 'identifier')
    assert (var296.forwarded[0]['for'] == 'identifier')
    assert (var296.forwarded[0]['host'] == 'identifier')
    assert (var296.forwarded[0]['proto'] == 'identifier')

def function989(function145):
    var3302 = 'bY=identifier;fOr=identifier;HOst=identifier;pRoTO=identifier'
    var1307 = function145('GET', '/', headers=CIMultiDict({'Forwarded': header, }))
    assert (var1307.forwarded[0]['by'] == 'identifier')
    assert (var1307.forwarded[0]['for'] == 'identifier')
    assert (var1307.forwarded[0]['host'] == 'identifier')
    assert (var1307.forwarded[0]['proto'] == 'identifier')

def function2693(function145):
    var4292 = 'BY=identifier'
    var996 = function145('GET', '/', headers=CIMultiDict({'Forwarded': header, }))
    assert (var996.forwarded[0]['by'] == 'identifier')

def function910(function145):
    var311 = 'By=identifier1,BY=identifier2,  By=identifier3 ,  BY=identifier4'
    var3035 = function145('GET', '/', headers=CIMultiDict({'Forwarded': header, }))
    assert (len(var3035.forwarded) == 4)
    assert (var3035.forwarded[0]['by'] == 'identifier1')
    assert (var3035.forwarded[1]['by'] == 'identifier2')
    assert (var3035.forwarded[2]['by'] == 'identifier3')
    assert (var3035.forwarded[3]['by'] == 'identifier4')

def function305(function145):
    var317 = 'BY=identifier;pROTO="\\lala lan\\d\\~ 123\\!&"'
    var3095 = function145('GET', '/', headers=CIMultiDict({'Forwarded': header, }))
    assert (var3095.forwarded[0]['by'] == 'identifier')
    assert (var3095.forwarded[0]['proto'] == 'lala land~ 123!&')

def function1821(function145):
    var4617 = CIMultiDict()
    var4617.add('Forwarded', 'By=identifier1;for=identifier2, BY=identifier3')
    var4617.add('Forwarded', 'By=identifier4;fOr=identifier5')
    var3152 = function145('GET', '/', headers=var4617)
    assert (len(var3152.forwarded) == 3)
    assert (var3152.forwarded[0]['by'] == 'identifier1')
    assert (var3152.forwarded[0]['for'] == 'identifier2')
    assert (var3152.forwarded[1]['by'] == 'identifier3')
    assert (var3152.forwarded[2]['by'] == 'identifier4')
    assert (var3152.forwarded[2]['for'] == 'identifier5')

def function1561(function145):
    var3735 = function145('GET', '/', headers=CIMultiDict({'Forwarded': 'by=;for=;host=;proto=https', }))
    assert ('https' == var3735.scheme)
    assert (var3735.secure is True)

def function760(function145):
    var725 = function145('GET', '/', headers=CIMultiDict({'Forwarded': 'malformed value', }))
    assert ('http' == var725.scheme)
    assert (var725.secure is False)

def function88(function145):
    var4439 = function145('GET', '/', headers=CIMultiDict({'X-Forwarded-Proto': 'https', }))
    assert ('https' == var4439.scheme)
    assert (var4439.secure is True)

def function1463(function145):
    var3664 = function145('GET', '/', headers=CIMultiDict({'X-Forwarded-Proto': 'http', }))
    assert ('http' == var3664.scheme)
    assert (var3664.secure is False)

def function10(function145):
    var2518 = CIMultiDict()
    var2518.add('Forwarded', 'By=identifier1;for=identifier2, BY=identifier3')
    var2518.add('Forwarded', 'by=;for=;host=example.com')
    var3961 = function145('GET', '/', headers=var2518)
    assert (var3961.host == 'example.com')

def function2480(function145):
    var2714 = function145('GET', '/', headers=CIMultiDict({'Forwarded': 'malformed value', }))
    assert (var2714.host is None)

def function1008(function145):
    var1409 = function145('GET', '/', headers=CIMultiDict({'X-Forwarded-Host': 'example.com', }))
    assert (var1409.host == 'example.com')

def function2037(function145):
    var3850 = function145('GET', '/', headers=CIMultiDict({'Host': 'example.com', }))
    assert (var3850.host == 'example.com')

def function2642(function145):
    var8 = function145('GET', '/', headers=CIMultiDict({'X-HEADER': 'aaa', }))
    assert (var8.raw_headers == ((b'X-Header', b'aaa'),))

def function1470(function145):
    var4149 = function145('GET', '/path')
    assert (URL('/path') == var4149.rel_url)

def function2570(function145):
    var2498 = function145('GET', '/path', headers={'HOST': 'example.com', })
    assert (URL('http://example.com/path') == var2498.url)

def function776():
    var1497 = make_mocked_request('GET', '/path')
    var4444 = var1497.clone()
    assert (var4444.method == 'GET')
    assert (var4444.rel_url == URL('/path'))

def function1488():
    var1215 = make_mocked_request('GET', '/path')
    var1503 = var1215.clone(method='POST')
    assert (var1503.method == 'POST')
    assert (var1503.rel_url == URL('/path'))

def function1051():
    var1985 = make_mocked_request('GET', '/path')
    var4343 = var1985.clone(rel_url=URL('/path2'))
    assert (var4343.rel_url == URL('/path2'))

def function1432():
    var1549 = make_mocked_request('GET', '/path')
    var2162 = var1549.clone(rel_url='/path2')
    assert (var2162.rel_url == URL('/path2'))

def function2299():
    var1450 = make_mocked_request('GET', '/path', headers={'A': 'B', })
    var1011 = var1450.clone(headers=CIMultiDict({'B': 'C', }))
    assert (var1011.headers == CIMultiDict({'B': 'C', }))
    assert (var1011.raw_headers == ((b'B', b'C'),))

def function575():
    var582 = make_mocked_request('GET', '/path', headers={'A': 'B', })
    var570 = var582.clone(headers={'B': 'C', })
    assert (var570.headers == CIMultiDict({'B': 'C', }))
    assert (var570.raw_headers == ((b'B', b'C'),))

@asyncio.coroutine
def function2261(arg225):
    var1504 = StreamReader(loop=arg225)
    var1504.feed_data(b'data')
    var1504.feed_eof()
    var4253 = make_mocked_request('GET', '/path', payload=var1504)
    yield from var4253.read()
    with pytest.raises(RuntimeError):
        var4253.clone()

@asyncio.coroutine
def function2708(arg1590):
    var4562 = StreamReader(loop=arg1590)
    var868 = ((1024 ** 2) * b'x')
    var42 = (var868 + b'x')
    var4562.feed_data(var42)
    var4562.feed_eof()
    var1665 = make_mocked_request('POST', '/', payload=var4562)
    with pytest.raises(HTTPRequestEntityTooLarge) as var4182:
        yield from var1665.read()
    assert (var4182.value.status_code == 413)

@asyncio.coroutine
def function2019(arg903):
    var527 = StreamReader(loop=arg903)
    var2480 = ((1024 ** 2) * b'x')
    var2565 = (var2480 + b'x')
    var527.feed_data(var2565)
    var527.feed_eof()
    var253 = ((1024 ** 2) + 2)
    var151 = make_mocked_request('POST', '/', payload=var527, client_max_size=var253)
    var1953 = yield from var151.read()
    assert (len(var1953) == ((1024 ** 2) + 1))

@asyncio.coroutine
def function79(arg2239):
    var1935 = StreamReader(loop=arg2239)
    var1935.feed_data(b'-----------------------------326931944431359\r\nContent-Disposition: form-data; name="a"\r\n\r\nb\r\n-----------------------------326931944431359\r\nContent-Disposition: form-data; name="c"\r\n\r\nd\r\n-----------------------------326931944431359--\r\n')
    var2159 = 'multipart/form-data; boundary=---------------------------326931944431359'
    var1935.feed_eof()
    var1574 = make_mocked_request('POST', '/', headers={'CONTENT-TYPE': content_type, }, payload=var1935)
    var1449 = yield from var1574.post()
    assert (dict(var1449) == {'a': 'b', 'c': 'd', })

@asyncio.coroutine
def function543(arg1299):
    var4619 = StreamReader(loop=arg1299)
    var4228 = ((1024 ** 2) * b'x')
    var3630 = (var4228 + b'x')
    var4619.feed_data(var3630)
    var4619.feed_eof()
    var2133 = None
    var2226 = make_mocked_request('POST', '/', payload=var4619, client_max_size=var2133)
    var763 = yield from var2226.read()
    assert (len(var763) == ((1024 ** 2) + 1))