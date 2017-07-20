'Tests for aiohttp/client.py'
import asyncio
import gc
from unittest import mock
import pytest
from yarl import URL
import aiohttp
from aiohttp import helpers, http
from aiohttp.client_reqrep import ClientResponse, RequestInfo

@asyncio.coroutine
def function1795():
    var3605 = mock.Mock()
    var1010 = mock.Mock()
    var286 = ClientResponse('get', URL('http://del-cl-resp.org'), request_info=var1010)
    var286._post_init(var3605)
    var3605.get_debug = mock.Mock()
    var3605.get_debug.return_value = True
    var4238 = mock.Mock()
    var4238.protocol = aiohttp.DataQueue(loop=var3605)
    var4238.protocol.set_response_params = mock.Mock()
    var4238.protocol.set_exception(http.HttpProcessingError())
    with pytest.raises(aiohttp.ClientResponseError) as var341:
        yield from var286.start(var4238)
    assert (var341.value.var1010 is var1010)

def function2323():
    var2243 = mock.Mock()
    var4294 = ClientResponse('get', URL('http://del-cl-resp.org'))
    var4294._post_init(var2243)
    var2243.get_debug = mock.Mock()
    var2243.get_debug.return_value = True
    var3199 = mock.Mock()
    var4294._closed = False
    var4294._connection = var3199
    var2243.set_exception_handler((lambda var2243, arg1218: None))
    with pytest.warns(ResourceWarning):
        del response
        gc.collect()
    var3199.release.assert_called_with()

def function803(arg788):
    var1700 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var1700._post_init(arg788)
    var1700._closed = False
    var1700._connection = mock.Mock()
    var1700.close()
    assert (var1700.connection is None)
    var1700.close()
    var1700.close()

def function1215(arg1953):
    var4737 = ClientResponse('get', URL('http://python.org'), continue100=object())
    var4737._post_init(arg1953)
    assert (var4737._continue is not None)
    var4737.close()

def function1138(arg16):
    var415 = ClientResponse('get', URL('http://python.org'))
    var415._post_init(arg16)
    assert (var415._continue is None)
    var415.close()

def function1503(arg348):
    var1432 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var1432._post_init(arg348)
    var1432.status = 200
    var1432.reason = 'Ok'
    assert ('<ClientResponse(http://def-cl-resp.org) [200 Ok]>' in repr(var1432))

def function845():
    var3868 = ClientResponse('get', URL('http://fake-host.org/λ'))
    assert ('<ClientResponse(http://fake-host.org/%CE%BB) [None None]>' in repr(var3868))

def function1952():
    var2518 = ClientResponse('get', URL('http://fake-host.org/path'))
    var2518.reason = 'λ'
    assert ('<ClientResponse(http://fake-host.org/path) [None \\u03bb]>' in repr(var2518))

def function1949():
    var477 = ClientResponse('get', URL('http://fake-host.org/'))
    with pytest.warns(DeprecationWarning):
        var477.url_obj

@asyncio.coroutine
def function1970(arg99):
    var2573 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var2573._post_init(arg99)

    def function539(*args, **kwargs):
        var2152 = helpers.create_future(arg99)
        var2152.set_result(b'payload')
        return var2152
    var921 = var2573.content = mock.Mock()
    var921.read.side_effect = function539
    var1639 = yield from var2573.read()
    assert (var1639 == b'payload')
    assert (var2573._connection is None)

@asyncio.coroutine
def function326(arg2089):
    var2878 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var2878._post_init(arg2089)
    var1996 = var2878.content = mock.Mock()
    var1996.read.return_value = helpers.create_future(arg2089)
    var1996.read.return_value.set_exception(ValueError)
    with pytest.raises(ValueError):
        yield from var2878.read()
    assert var2878._closed

@asyncio.coroutine
def function1548(arg2330):
    var3553 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var3553._post_init(arg2330)
    var261 = helpers.create_future(arg2330)
    var261.set_result(b'')
    var845 = var3553.content = mock.Mock()
    var845.readany.return_value = var261
    var3553.release()
    assert (var3553._connection is None)

@asyncio.coroutine
def function964(arg2199):
    var2701 = mock.Mock()
    var2701.protocol.upgraded = False

    def function1694(arg464):
        var941 = ClientResponse('get', URL('http://def-cl-resp.org'))
        var941._post_init(arg2199)
        var941._closed = False
        var941._connection = arg464
    function1694(var2701)
    assert var2701.release.called

@asyncio.coroutine
def function1293(arg1140):
    var407 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var407._post_init(arg1140)
    var407._closed = False
    var4608 = var407._connection = mock.Mock()
    var4608.protocol.upgraded = False
    var407._response_eof()
    assert var4608.release.called
    assert (var407._connection is None)

@asyncio.coroutine
def function1699(arg1057):
    var4056 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var4056._post_init(arg1057)
    var3042 = var4056._connection = mock.Mock()
    var3042.protocol.upgraded = True
    var4056._response_eof()
    assert (not var3042.release.called)
    assert (var4056._connection is var3042)

@asyncio.coroutine
def function1085(arg378):
    var3038 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var3038._post_init(arg378)
    var3038._closed = False
    var1776 = var3038._connection = mock.Mock()
    var1776.protocol = None
    var3038._response_eof()
    assert var1776.release.called
    assert (var3038._connection is None)

@asyncio.coroutine
def function2288(arg2017):
    var1261 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var1261._post_init(arg2017)

    def function539(*args, **kwargs):
        var3438 = helpers.create_future(arg2017)
        var3438.set_result('{"тест": "пройден"}'.encode('cp1251'))
        return var3438
    var1261.headers = {'Content-Type': 'application/json;charset=cp1251', }
    var911 = var1261.content = mock.Mock()
    var911.read.side_effect = function539
    var635 = yield from var1261.text()
    assert (var635 == '{"тест": "пройден"}')
    assert (var1261._connection is None)

@asyncio.coroutine
def function147(arg316):
    var711 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var711._post_init(arg316)

    def function539(*args, **kwargs):
        var4616 = helpers.create_future(arg316)
        var4616.set_result('{"тестkey": "пройденvalue"}'.encode('cp1251'))
        return var4616
    var711.headers = {'Content-Type': 'application/json;charset=utf-8', }
    var3762 = var711.content = mock.Mock()
    var3762.read.side_effect = function539
    with pytest.raises(UnicodeDecodeError):
        yield from var711.text()
    var378 = yield from var711.text(errors='ignore')
    assert (var378 == '{"key": "value"}')
    assert (var711._connection is None)

@asyncio.coroutine
def function2573(arg2220):
    var2405 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var2405._post_init(arg2220)

    def function539(*args, **kwargs):
        var406 = helpers.create_future(arg2220)
        var406.set_result('{"тест": "пройден"}'.encode('cp1251'))
        return var406
    var2405.headers = {'Content-Type': 'application/json', }
    var2746 = var2405.content = mock.Mock()
    var2746.read.side_effect = function539
    var2405._get_encoding = mock.Mock()
    var4317 = yield from var2405.text(encoding='cp1251')
    assert (var4317 == '{"тест": "пройден"}')
    assert (var2405._connection is None)
    assert (not var2405._get_encoding.called)

@asyncio.coroutine
def function2693(arg1500):
    var2238 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var2238._post_init(arg1500)

    def function539(*args, **kwargs):
        var1927 = helpers.create_future(arg1500)
        var1927.set_result('{"тест": "пройден"}'.encode('cp1251'))
        return var1927
    var2238.headers = {'Content-Type': 'text/plain', }
    var2403 = var2238.content = mock.Mock()
    var2403.read.side_effect = function539
    yield from var2238.read()
    var549 = yield from var2238.text()
    assert (var549 == '{"тест": "пройден"}')
    assert (var2238._connection is None)

@asyncio.coroutine
def function2123(arg578):
    var3280 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var3280._post_init(arg578)

    def function539(*args, **kwargs):
        var1870 = helpers.create_future(arg578)
        var1870.set_result('{"тест": "пройден"}'.encode('cp1251'))
        return var1870
    var3280.headers = {'Content-Type': 'application/json;charset=cp1251', }
    var4675 = var3280.content = mock.Mock()
    var4675.read.side_effect = function539
    var2254 = yield from var3280.text()
    assert (var2254 == '{"тест": "пройден"}')
    assert (var3280._connection is None)

@asyncio.coroutine
def function1742(arg2358):
    var3471 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var3471._post_init(arg2358)

    def function539(*args, **kwargs):
        var4493 = helpers.create_future(arg2358)
        var4493.set_result('{"тест": "пройден"}'.encode('cp1251'))
        return var4493
    var3471.headers = {'Content-Type': 'application/json;charset=cp1251', }
    var1659 = var3471.content = mock.Mock()
    var1659.read.side_effect = function539
    var140 = yield from var3471.json()
    assert (var140 == {'тест': 'пройден', })
    assert (var3471._connection is None)

@asyncio.coroutine
def function2838(arg539):
    var174 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var174._post_init(arg539)
    var174.headers = {'Content-Type': 'application/json;charset=cp1251', }
    var174._content = b'data'

    def function1044(arg322):
        return (arg322 + '-custom')
    var1322 = yield from var174.json(loads=function1044)
    assert (var1322 == 'data-custom')

@asyncio.coroutine
def function267(arg1917):
    var3267 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var3267._post_init(arg1917)
    var3267.headers = {'Content-Type': 'data/octet-stream', }
    var3267._content = b''
    with pytest.raises(aiohttp.ClientResponseError) as var2577:
        yield from var3267.json()
    assert (var2577.value.request_info == var3267.request_info)
    var107 = yield from var3267.json(content_type=None)
    assert (var107 is None)

@asyncio.coroutine
def function1459(arg1097):
    var264 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var264._post_init(arg1097)

    def function539(*args, **kwargs):
        var3346 = helpers.create_future(arg1097)
        var3346.set_result('{"тест": "пройден"}'.encode('cp1251'))
        return var3346
    var264.headers = {'Content-Type': 'application/json;charset=utf8', }
    var1378 = var264.content = mock.Mock()
    var1378.read.side_effect = function539
    var264._get_encoding = mock.Mock()
    var1666 = yield from var264.json(encoding='cp1251')
    assert (var1666 == {'тест': 'пройден', })
    assert (var264._connection is None)
    assert (not var264._get_encoding.called)

@pytest.mark.xfail
def function552(arg2307):


    class Class407(ClientResponse):
        var4285 = aiohttp.StreamReader
    var2007 = Class407('get', URL('http://my-cl-resp.org'))
    var2007._post_init(arg2307)
    var2007._connection = mock.Mock()
    assert isinstance(var2007.content, aiohttp.StreamReader)
    var2007.close()

def function1187(arg1916):
    var2712 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var2712._post_init(arg1916)
    var2712.headers = {'Content-Type': 'application/json', }
    with mock.patch('aiohttp.client_reqrep.chardet') as var1253:
        var1253.detect.return_value = {'encoding': None, }
        assert (var2712._get_encoding() == 'utf-8')

def function715():
    var475 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var475.status = 200
    var475.reason = 'OK'
    var475.raise_for_status()

def function2051():
    var4504 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var4504.status = 409
    var4504.reason = 'CONFLICT'
    with pytest.raises(aiohttp.ClientResponseError) as var4362:
        var4504.raise_for_status()
    assert (str(var4362.value.code) == '409')
    assert (str(var4362.value.message) == 'CONFLICT')

def function2477():
    var481 = ClientResponse('get', URL('http://del-cl-resp.org'))
    assert ('del-cl-resp.org' == var481.host)

def function1616():
    var1369 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var1369.headers = {'Content-Type': 'application/json;charset=cp1251', }
    assert ('application/json' == var1369.content_type)

def function1650():
    var3575 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var3575.headers = {}
    assert ('application/octet-stream' == var3575.content_type)

def function2273():
    var4264 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var4264.headers = {'Content-Type': 'application/json;charset=cp1251', }
    assert ('cp1251' == var4264.charset)

def function1612():
    var3518 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var3518.headers = {}
    assert (var3518.charset is None)

def function2174():
    var3248 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var3248.headers = {'Content-Type': 'application/json', }
    assert (var3248.charset is None)

def function747():
    var2568 = 'http://def-cl-resp.org'
    var4719 = {'Content-Type': 'application/json;charset=cp1251', }
    var4270 = ClientResponse('get', URL(var2568), request_info=RequestInfo(var2568, 'get', var4719))
    assert (var2568 == var4270.request_info.var2568)
    assert ('get' == var4270.request_info.method)
    assert (var4719 == var4270.request_info.var4719)

def function939():
    var625 = 'http://def-cl-resp.org'
    var1356 = ClientResponse('get', URL(var625))
    assert (var1356.request_info is None)

def function1027():
    var3093 = 'http://def-cl-resp.org'
    var2620 = {'Content-Type': 'application/json;charset=cp1251', }
    var2181 = ClientResponse('get', URL(var3093), request_info=RequestInfo(var3093, 'get', var2620))
    var2181.status = 409
    var2181.reason = 'CONFLICT'
    with pytest.raises(aiohttp.ClientResponseError) as var3927:
        var2181.raise_for_status()
    assert (var3927.value.request_info == var2181.request_info)

def function1514():
    var390 = 'http://def-cl-resp.org'
    var2584 = {'Content-Type': 'application/json;charset=cp1251', }
    var3327 = ClientResponse('get', URL(var390), request_info=RequestInfo(var390, 'get', var2584))
    var3327.status = 409
    var3327.reason = 'CONFLICT'
    with pytest.raises(aiohttp.ClientResponseError) as var3517:
        var3327.raise_for_status()
    assert (() == var3517.value.history)

def function1037():
    var1677 = 'http://def-cl-resp.org'
    var4324 = 'http://def-cl-resp.org/index.htm'
    var1525 = {'Content-Type': 'application/json;charset=cp1251', 'Location': url, }
    var545 = {'Content-Type': 'application/json;charset=cp1251', }
    var891 = ClientResponse('get', URL(var4324), request_info=RequestInfo(var4324, 'get', var545))
    var891.status = 409
    var891.reason = 'CONFLICT'
    var828 = ClientResponse('get', URL(var1677), request_info=RequestInfo(var4324, 'get', var545))
    var828.headers = var1525
    var828.status = 301
    var828.reason = 'REDIRECT'
    var891._history = [var828]
    with pytest.raises(aiohttp.ClientResponseError) as var3479:
        var891.raise_for_status()
    assert ([var828] == var3479.value.history)