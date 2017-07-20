import asyncio
import os
import pathlib
import re
from collections.abc import Container, Iterable, Mapping, MutableMapping, Sized
from urllib.parse import unquote
import pytest
from yarl import URL
import aiohttp
from aiohttp import hdrs, web
from aiohttp.test_utils import make_mocked_request
from aiohttp.web import HTTPMethodNotAllowed, HTTPNotFound, Response
from aiohttp.web_urldispatcher import PATH_SEP, AbstractResource, ResourceRoute, SystemRoute, View, _defaultExpectHandler

def function856(arg2240, arg632):
    return make_mocked_request(arg2240, arg632)

def function1158():

    @asyncio.coroutine
    def function635(arg1589):
        return Response(arg1589)
    return function635

@pytest.fixture
def function554(arg806):
    function554 = web.Application()
    function554._set_loop(arg806)
    return function554

@pytest.fixture
def function1737(function554):
    return function554.function1737

@pytest.fixture
def function1962(function1737):

    def function2842():
        var2179 = function1737.add_route('GET', '/plain', function1158())
        var1811 = function1737.add_route('GET', '/variable/{name}', function1158())
        var3159 = function1737.add_static('/static', os.path.dirname(aiohttp.__file__))
        return ([var2179, var1811] + list(var3159))
    return function2842

def function1092(function1737):
    var2654 = {'PROPFIND', 'PROPPATCH', 'COPY', 'LOCK', 'UNLOCKMOVE', 'SUBSCRIBE', 'UNSUBSCRIBE', 'NOTIFY'}
    for var3104 in var2654:
        function1737.add_route(var3104, '/handler/to/path', function1158())

@asyncio.coroutine
def function1207(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/', function635)
    var1005 = function856('GET', '/')
    var2670 = yield from function1737.resolve(var1005)
    assert (var2670 is not None)
    assert (0 == len(var2670))
    assert (function635 is var2670.function635)
    assert (var2670.route.name is None)

@asyncio.coroutine
def function670(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/handler/to/path', function635)
    var3996 = function856('GET', '/handler/to/path')
    var234 = yield from function1737.resolve(var3996)
    assert (var234 is not None)
    assert (0 == len(var234))
    assert (function635 is var234.function635)
    assert (var234.route.name is None)

@asyncio.coroutine
def function2840(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/handler/{to}', function635)
    var909 = function856('GET', '/handler/tail')
    var1047 = yield from function1737.resolve(var909)
    assert (var1047 is not None)
    assert ({'to': 'tail', } == var1047)
    assert (function635 is var1047.function635)
    assert (var1047.route.name is None)

@asyncio.coroutine
def function268(function1737):
    function635 = function1158()
    function1737.add_get('/handler/to/path', function635)
    var511 = function856('GET', '/handler/to/path')
    var2604 = yield from function1737.resolve(var511)
    assert (var2604 is not None)
    assert (0 == len(var2604))
    assert (function635 is var2604.function635)
    assert (var2604.route.name is None)

@asyncio.coroutine
def function2028(function1737):
    function635 = function1158()
    function1737.add_post('/handler/to/path', function635)
    var2935 = function856('POST', '/handler/to/path')
    var1117 = yield from function1737.resolve(var2935)
    assert (var1117 is not None)
    assert (0 == len(var1117))
    assert (function635 is var1117.function635)
    assert (var1117.route.name is None)

@asyncio.coroutine
def function922(function1737):
    function635 = function1158()
    function1737.add_put('/handler/to/path', function635)
    var2235 = function856('PUT', '/handler/to/path')
    var2757 = yield from function1737.resolve(var2235)
    assert (var2757 is not None)
    assert (0 == len(var2757))
    assert (function635 is var2757.function635)
    assert (var2757.route.name is None)

@asyncio.coroutine
def function2233(function1737):
    function635 = function1158()
    function1737.add_patch('/handler/to/path', function635)
    var4034 = function856('PATCH', '/handler/to/path')
    var3723 = yield from function1737.resolve(var4034)
    assert (var3723 is not None)
    assert (0 == len(var3723))
    assert (function635 is var3723.function635)
    assert (var3723.route.name is None)

@asyncio.coroutine
def function260(function1737):
    function635 = function1158()
    function1737.add_delete('/handler/to/path', function635)
    var3293 = function856('DELETE', '/handler/to/path')
    var3339 = yield from function1737.resolve(var3293)
    assert (var3339 is not None)
    assert (0 == len(var3339))
    assert (function635 is var3339.function635)
    assert (var3339.route.name is None)

@asyncio.coroutine
def function1330(function1737):
    function635 = function1158()
    function1737.add_head('/handler/to/path', function635)
    var4475 = function856('HEAD', '/handler/to/path')
    var1692 = yield from function1737.resolve(var4475)
    assert (var1692 is not None)
    assert (0 == len(var1692))
    assert (function635 is var1692.function635)
    assert (var1692.route.name is None)

@asyncio.coroutine
def function730(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/handler/to/path', function635, name='name')
    var1943 = function856('GET', '/handler/to/path')
    var354 = yield from function1737.resolve(var1943)
    assert (var354 is not None)
    assert ('name' == var354.route.name)

@asyncio.coroutine
def function1861(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/handler/to/path/', function635)
    var1831 = function856('GET', '/handler/to/path/')
    var3051 = yield from function1737.resolve(var1831)
    assert (var3051 is not None)
    assert ({} == var3051)
    assert (function635 is var3051.function635)

def function1563(function1737):
    function635 = function1158()
    with pytest.raises(ValueError):
        function1737.add_route('GET', '/{/', function635)

def function2825(function1737):
    function635 = function1158()
    with pytest.raises(ValueError):
        function1737.add_route('post', '/post/{id', function635)

def function221(function1737):
    function635 = function1158()
    with pytest.raises(ValueError):
        function1737.add_route('post', '/post/{id{}}', function635)

def function752(function1737):
    function635 = function1158()
    with pytest.raises(ValueError):
        function1737.add_route('post', '/post/{id{}', function635)

def function1359(function1737):
    function635 = function1158()
    with pytest.raises(ValueError):
        function1737.add_route('post', '/post/{id"}', function635)

@asyncio.coroutine
def function1039(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/+$', function635)
    var4659 = function856('GET', '/+$')
    var1793 = yield from function1737.resolve(var4659)
    assert (var1793 is not None)
    assert (function635 is var1793.function635)

@asyncio.coroutine
def function275(function1737):
    function635 = function1158()
    var3140 = function1737.add_route(hdrs.METH_ANY, '/', function635)
    var968 = function856('GET', '/')
    var297 = yield from function1737.resolve(var968)
    assert (var297 is not None)
    assert (var3140 is var297.var3140)
    var968 = function856('POST', '/')
    var3347 = yield from function1737.resolve(var968)
    assert (var3347 is not None)
    assert (var297.var3140 is var3347.var3140)

@asyncio.coroutine
def function1785(function1737):
    var835 = function1158()
    var2765 = function1158()
    function1737.add_route('GET', '/h1', var835)
    function1737.add_route('POST', '/h2', var2765)
    var3900 = function856('POST', '/h2')
    var2652 = yield from function1737.resolve(var3900)
    assert (var2652 is not None)
    assert ({} == var2652)
    assert (var2765 is var2652.function635)

@asyncio.coroutine
def function1891(function1737):
    var794 = function1158()
    var1421 = function1158()
    function1737.add_route('GET', '/', var794)
    function1737.add_route('POST', '/', var1421)
    var1727 = function856('PUT', '/')
    var1656 = yield from function1737.resolve(var1727)
    assert isinstance(var1656.route, SystemRoute)
    assert ({} == var1656)
    with pytest.raises(HTTPMethodNotAllowed) as var675:
        yield from var1656.function635(var1727)
    var4281 = var675.value
    assert ('PUT' == var4281.method)
    assert (405 == var4281.status)
    assert ({'POST', 'GET'} == var4281.allowed_methods)

@asyncio.coroutine
def function235(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/a', function635)
    var228 = function856('GET', '/b')
    var3544 = yield from function1737.resolve(var228)
    assert isinstance(var3544.route, SystemRoute)
    assert ({} == var3544)
    with pytest.raises(HTTPNotFound) as var2674:
        yield from var3544.function635(var228)
    var1306 = var2674.value
    assert (404 == var1306.status)

def function1994(function1737):
    var1875 = function1158()
    var3697 = function1158()
    function1737.add_route('GET', '/get', var1875, name='name')
    var3239 = "Duplicate 'name', already handled by"
    with pytest.raises(ValueError) as var396:
        function1737.add_route('GET', '/get_other', var3697, name='name')
    assert re.match(var3239, str(var396.value))

def function2344(function1737):
    function635 = function1158()
    var2937 = function1737.add_route('GET', '/get', function635, name='name')
    var1877 = next(iter(function1737['name']))
    var1378 = var1877.var1378()
    assert ('/get' == var1378)
    assert (var2937 is var1877)

def function1599(function1737):
    with pytest.raises(KeyError):
        function1737['unknown']

def function2136(function1737):
    function635 = function1158()
    var1749 = function1737.add_route('GET', '/get/{name}', function635, name='name')
    var2170 = next(iter(function1737['name']))
    var1882 = var2170.var1882(parts={'name': 'John', })
    assert ('/get/John' == var1882)
    assert (var1749 is var2170)

def function1619(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/get', function635, name='name')
    var2612 = function1737['name'].var2612(query=[('a', 'b'), ('c', '1')])
    assert ('/get?a=b&c=1' == var2612)

def function2011(function1737):
    var45 = function1737.add_static('/st', os.path.dirname(aiohttp.__file__), name='static')
    assert (function1737['static'] is var45)
    var3507 = var45.var3507(filename='/dir/a.txt')
    assert ('/st/dir/a.txt' == var3507)
    assert (len(var45) == 2)

def function798(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/get/path', function635, name='name')
    var1189 = function1737['name']
    assert (var1189._match('/another/path') is None)

def function178(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/get/{name}', function635, name='name')
    var1622 = function1737['name']
    assert (var1622._match('/another/path') is None)

@asyncio.coroutine
def function550(function1737):
    function1737.add_static('/pre', os.path.dirname(aiohttp.__file__), name='name')
    var1314 = function1737['name']
    var1922 = yield from var1314.resolve(make_mocked_request('GET', '/another/path'))
    assert ((None, set()) == var1922)

def function1295(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/get/{name}/', function635, name='name')
    var1304 = function1737['name']
    assert ({'name': 'John', } == var1304._match('/get/John/'))

def function183(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/get1', function635, name='name1')
    function1737.add_route('GET', '/get2', function635, name='name2')
    assert (2 == len(function1737))

def function2449(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/get1', function635, name='name1')
    function1737.add_route('GET', '/get2', function635, name='name2')
    assert ({'name1', 'name2'} == set(iter(function1737)))

def function2892(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/get1', function635, name='name1')
    function1737.add_route('GET', '/get2', function635, name='name2')
    assert ('name1' in function1737)
    assert ('name3' not in function1737)

def function2789(function1737):
    function1737.add_static('/get', os.path.dirname(aiohttp.__file__), name='name')
    assert re.match("<StaticResource 'name' /get", repr(function1737['name']))

def function1892(function1737):
    var2504 = function1737.add_static('/prefix', os.path.dirname(aiohttp.__file__))
    assert ('/prefix' == var2504._prefix)

def function1615(function1737):
    var3299 = function1737.add_static('/prefix/', os.path.dirname(aiohttp.__file__))
    assert ('/prefix' == var3299._prefix)

@asyncio.coroutine
def function474(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/handler/{to:\\d+}', function635)
    var884 = function856('GET', '/handler/1234')
    var1252 = yield from function1737.resolve(var884)
    assert (var1252 is not None)
    assert ({'to': '1234', } == var1252)
    function1737.add_route('GET', '/handler/{name}.html', function635)
    var884 = function856('GET', '/handler/test.html')
    var1252 = yield from function1737.resolve(var884)
    assert ({'name': 'test', } == var1252)

@asyncio.coroutine
def function1850(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/handler/{to:[^/]+/?}', function635)
    var3233 = function856('GET', '/handler/1234/')
    var3602 = yield from function1737.resolve(var3233)
    assert (var3602 is not None)
    assert ({'to': '1234/', } == var3602)
    function1737.add_route('GET', '/handler/{to:.+}', function635)
    var3233 = function856('GET', '/handler/1234/5/6/7')
    var3602 = yield from function1737.resolve(var3233)
    assert (var3602 is not None)
    assert ({'to': '1234/5/6/7', } == var3602)

@asyncio.coroutine
def function546(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/handler/{to:\\d+}', function635)
    var1669 = function856('GET', '/handler/tail')
    var2229 = yield from function1737.resolve(var1669)
    assert isinstance(var2229.route, SystemRoute)
    assert ({} == var2229)
    with pytest.raises(HTTPNotFound):
        yield from var2229.function635(var1669)

@asyncio.coroutine
def function198(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/handler/{to:.+}/tail', function635)
    var705 = function856('GET', '/handler/re/with/slashes/tail')
    var3740 = yield from function1737.resolve(var705)
    assert (var3740 is not None)
    assert ({'to': 're/with/slashes', } == var3740)

def function2475(function1737):
    function635 = function1158()
    with pytest.raises(ValueError) as var200:
        function1737.add_route('GET', '/handler/{to:+++}', function635)
    var1597 = str(var200.value)
    assert var1597.startswith((((("Bad pattern '" + PATH_SEP) + 'handler') + PATH_SEP) + "(?P<to>+++)': nothing to repeat"))
    assert (var200.value.__cause__ is None)

def function34(function1737):
    function635 = function1158()
    var2529 = function1737.add_route('GET', '/get/{num:^\\d+}', function635, name='name')
    var3787 = var2529.var3787(parts={'num': '123', })
    assert ('/get/123' == var3787)

def function2268(function1737):
    function635 = function1158()
    var940 = function1737.add_route('GET', '/get/{num:^\\d+}/', function635, name='name')
    var2259 = var940.var2259(parts={'num': '123', })
    assert ('/get/123/' == var2259)

def function490(function1737):
    function635 = function1158()
    var1644 = function1737.add_route('GET', '/{one}/{two:.+}', function635)
    var318 = var1644.var318(parts={'one': 1, 'two': 2, })
    assert ('/1/2' == var318)

@asyncio.coroutine
def function2822(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/get/{name}', function635)
    var3675 = function856('GET', '/get/john')
    var89 = yield from function1737.resolve(var3675)
    assert ({'name': 'john', } == var89)
    assert re.match("<MatchInfo {'name': 'john'}: .+<Dynamic.+>>", repr(var89))

@asyncio.coroutine
def function2491(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/get/{version}', function635)
    var383 = function856('GET', '/get/1.0+test')
    var4112 = yield from function1737.resolve(var383)
    assert ({'version': '1.0+test', } == var4112)

@asyncio.coroutine
def function239(function1737):
    var153 = function856('POST', '/path/to')
    var735 = yield from function1737.resolve(var153)
    assert ('<MatchInfoError 404: Not Found>' == repr(var735))

@asyncio.coroutine
def function1309(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/path/to', function635)
    var749 = function1158()
    function1737.add_route('POST', '/path/to', var749)
    var3435 = function856('PUT', '/path/to')
    var2196 = yield from function1737.resolve(var3435)
    assert ('<MatchInfoError 405: Method Not Allowed>' == repr(var2196))

def function1719(function1737):
    var2097 = function1737.add_route('GET', '/', function1158())
    assert (var2097._expect_handler is _defaultExpectHandler)

def function1520(function1737):

    @asyncio.coroutine
    def function635(arg596):
        pass
    var1649 = function1737.add_route('GET', '/', function1158(), expect_handler=function635)
    assert (var1649._expect_handler is function635)
    assert isinstance(var1649, ResourceRoute)

def function654(function1737):

    @asyncio.coroutine
    def function635(arg637):
        pass
    var1585 = function1737.add_route('GET', '/get/{name}', function1158(), expect_handler=function635)
    assert (var1585._expect_handler is function635)
    assert isinstance(var1585, ResourceRoute)

def function2355(function1737):

    def function635(arg357):
        pass
    with pytest.raises(AssertionError):
        function1737.add_route('GET', '/', function1158(), expect_handler=function635)

@asyncio.coroutine
def function462(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/{var}', function635)
    var4386 = function856('GET', '/%D1%80%D1%83%D1%81%20%D1%82%D0%B5%D0%BA%D1%81%D1%82')
    var3966 = yield from function1737.resolve(var4386)
    assert ({'var': 'рус текст', } == var3966)

@asyncio.coroutine
def function2336(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/{name}.html', function635)
    var1572 = function856('GET', '/file.html')
    var4133 = yield from function1737.resolve(var1572)
    assert ({'name': 'file', } == var4133)

@asyncio.coroutine
def function624(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/{name}.{ext}', function635)
    var542 = function856('GET', '/file.html')
    var3713 = yield from function1737.resolve(var542)
    assert ({'name': 'file', 'ext': 'html', } == var3713)

@asyncio.coroutine
def function511(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/{path}/{subpath}', function635)
    var1883 = 'my%2Fpath%7Cwith%21some%25strange%24characters'
    var2582 = function856('GET', '/path/{0}'.format(var1883))
    var508 = yield from function1737.resolve(var2582)
    assert (var508 == {'path': 'path', 'subpath': unquote(var1883), })

def function2807(function1737):
    with pytest.raises(ValueError):
        function635 = function1158()
        function1737.add_route('GET', 'invalid_path', function635)

def function1286(function1737):
    var2602 = {'BAD METHOD', 'B@D_METHOD', '[BAD_METHOD]', '{BAD_METHOD}', '(BAD_METHOD)', 'B?D_METHOD'}
    for var4729 in var2602:
        with pytest.raises(ValueError):
            function635 = function1158()
            function1737.add_route(var4729, '/path', function635)

def function643(function1737, function1962):
    function1962()
    assert (4 == len(function1737.routes()))

def function2838(function1737, function1962):
    var1094 = function1962()
    assert (list(var1094) == list(function1737.var1094()))

def function901(function1737, function1962):
    var3057 = function1962()
    for var3114 in var3057:
        assert (var3114 in function1737.var3057())

def function1721(function1737):
    assert isinstance(function1737.routes(), Sized)
    assert isinstance(function1737.routes(), Iterable)
    assert isinstance(function1737.routes(), Container)

def function246(function1737):
    assert isinstance(function1737.named_resources(), Mapping)
    assert (not isinstance(function1737.named_resources(), MutableMapping))

def function2295(function1737):
    var715 = function1737.add_route('GET', '/plain', function1158(), name='route1')
    var185 = function1737.add_route('GET', '/variable/{name}', function1158(), name='route2')
    var701 = function1737.add_static('/static', os.path.dirname(aiohttp.__file__), name='route3')
    var2289 = {var715.name, var185.name, var701.name}
    assert (3 == len(function1737.named_resources()))
    for var3126 in var2289:
        assert (var3126 in function1737.named_resources())
        assert isinstance(function1737.named_resources()[var3126], AbstractResource)

def function1390(function1737):
    var4562 = function1737.add_resource('/path')
    var2681 = var4562.add_route('GET', (lambda arg803: None))
    var2717 = var4562.add_route('POST', (lambda arg803: None))
    assert (2 == len(var4562))
    assert ([var2681, var2717] == list(var4562))

def function2751(function1737):
    var3010 = function1737.add_resource('/path')

    def function1170(arg1908):
        yield
    with pytest.warns(DeprecationWarning):
        var3010.add_route('GET', function1170)

def function2124(function1737):
    var1620 = function1737.add_resource('/path')
    var4647 = var1620.add_route('GET', View)
    assert (View is var4647.function635)

def function1049(function1737):
    var672 = function1737.add_resource('/path')
    var14 = var672.add_route('GET', (lambda arg11: None))
    assert ({} == var14.var672._match('/path'))

def function429(function1737):
    var400 = function1737.add_resource('/path')
    var400.add_route('GET', (lambda : None))
    with pytest.raises(RuntimeError):
        var400.add_route('GET', (lambda : None))

def function1145(function1737):
    var2021 = function1737.add_resource('/path')
    var2021.add_route('*', (lambda : None))
    with pytest.raises(RuntimeError):
        var2021.add_route('GET', (lambda : None))

@asyncio.coroutine
def function2280(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/', function635)
    var2241 = function856('GET', '/')
    var1174 = yield from function1737.resolve(var2241)
    assert (var1174.http_exception is None)

@asyncio.coroutine
def function1022(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/', function635)
    var2932 = function856('GET', '/abc')
    var2603 = yield from function1737.resolve(var2932)
    assert (var2603.http_exception.status == 404)

@asyncio.coroutine
def function840(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/', function635)
    var66 = function856('GET', '/')
    var2056 = yield from function1737.resolve(var66)
    assert (var2056.get_info() == {'path': '/', })

@asyncio.coroutine
def function456(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/{a}', function635)
    var4435 = function856('GET', '/value')
    var2133 = yield from function1737.resolve(var4435)
    assert (var2133.get_info() == {'pattern': re.compile((PATH_SEP + '(?P<a>[^{}/]+)')), 'formatter': '/{a}', })

@asyncio.coroutine
def function1213(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/{a}/{b}', function635)
    var939 = function856('GET', '/path/to')
    var2217 = yield from function1737.resolve(var939)
    assert (var2217.get_info() == {'pattern': re.compile((((PATH_SEP + '(?P<a>[^{}/]+)') + PATH_SEP) + '(?P<b>[^{}/]+)')), 'formatter': '/{a}/{b}', })

def function1798(function1737):
    var2818 = pathlib.Path(aiohttp.__file__).parent
    var2858 = function1737.add_static('/st', var2818)
    assert (var2858.get_info() == {'directory': directory, 'prefix': '/st', })

@asyncio.coroutine
def function127(function1737):
    function635 = function1158()
    function1737.add_route('GET', '/', function635)
    var2663 = function856('GET', '/abc')
    var461 = yield from function1737.resolve(var2663)
    assert (var461.get_info()['http_exception'].status == 404)

def function851(function1737):
    function1737.add_resource('/plain')
    function1737.add_resource('/variable/{name}')
    assert (2 == len(function1737.resources()))

def function2363(function1737):
    var2295 = function1737.add_resource('/plain')
    var3786 = function1737.add_resource('/variable/{name}')
    var4302 = [var2295, var3786]
    assert (list(var4302) == list(function1737.var4302()))

def function1849(function1737):
    var2774 = function1737.add_resource('/plain')
    var1139 = function1737.add_resource('/variable/{name}')
    var1723 = [var2774, var1139]
    for var541 in var1723:
        assert (var541 in function1737.var1723())

def function2593(function1737):
    assert isinstance(function1737.resources(), Sized)
    assert isinstance(function1737.resources(), Iterable)
    assert isinstance(function1737.resources(), Container)

def function409(function1737):
    var3734 = pathlib.Path(aiohttp.__file__).parent
    var4706 = pathlib.Path(os.path.expanduser('~'))
    if (not str(var3734).startswith(str(var4706))):
        pytest.skip("aiohttp folder is not placed in user's HOME")
    var1853 = ('~/' + str(var3734.relative_to(var4706)))
    var1384 = function1737.add_static('/st', var1853)
    assert (var3734 == var1384.get_info()['directory'])

def function685(function1737):
    var3997 = (pathlib.Path(aiohttp.__file__).parent / '__init__.py')
    with pytest.raises(ValueError):
        function1737.add_static('/st', var3997)

@asyncio.coroutine
def function2582(function1737):
    var220 = function1737.add_static('/st', os.path.dirname(aiohttp.__file__))
    var3663 = yield from var220.resolve(make_mocked_request('GET', '/unknown/path'))
    assert ((None, set()) == var3663)

@asyncio.coroutine
def function626(function1737):
    var4058 = function1737.add_static('/st', os.path.dirname(aiohttp.__file__))
    var1953 = yield from var4058.resolve(make_mocked_request('POST', '/st/abc.py'))
    assert ((None, {'HEAD', 'GET'}) == var1953)

@asyncio.coroutine
def function2797(function1737):
    function635 = function1158()
    var3673 = function1737.add_resource('/')
    var3673.add_route('GET', function635)
    var1321 = yield from var3673.resolve(make_mocked_request('GET', '/'))
    assert (var1321[0] is not None)
    assert ({'GET'} == var1321[1])

def function1928(function1737):
    var4155 = function1737.add_static('/static', os.path.dirname(aiohttp.__file__))
    assert (URL('/static/file.txt') == var4155.url_for(filename='file.txt'))

def function1971(function1737):
    var4455 = function1737.add_static('/static', os.path.dirname(aiohttp.__file__))
    assert (URL('/static/file.txt') == var4455.url_for(filename=pathlib.Path('file.txt')))

def function1183(function1737):
    var24 = function1737.add_route('GET', '/get/{name}', function1158(), name='name')
    assert (URL('/get/John') == var24.url_for(name='John'))

def function2198(function554, arg2158):
    var2904 = web.Application()
    var4662 = var2904.add_subapp('/pre', var2904)
    assert (var4662.get_info() == {'prefix': '/pre', 'app': subapp, })

def function1227(function554, arg2227):
    var2493 = web.Application()
    var4216 = function554.add_subapp('/pre', var2493)
    with pytest.raises(RuntimeError):
        var4216.url()

def function2706(function554, arg1162):
    var757 = web.Application()
    var4614 = function554.add_subapp('/pre', var757)
    with pytest.raises(RuntimeError):
        var4614.url_for()

def function647(function554, arg1427):
    var39 = web.Application()
    var3031 = function554.add_subapp('/pre', var39)
    assert repr(var3031).startswith('<PrefixedSubAppResource /pre -> <Application')

def function2425(function554, arg86):
    var1312 = web.Application()
    var1312.function1737.add_get('/', function1158(), allow_head=False)
    var1312.function1737.add_post('/', function1158())
    var2944 = function554.add_subapp('/pre', var1312)
    assert (len(var2944) == 2)

def function763(function554, arg2378):
    var3970 = web.Application()
    var311 = var3970.function1737.add_get('/', function1158(), allow_head=False)
    var1050 = var3970.function1737.add_post('/', function1158())
    var3229 = function554.add_subapp('/pre', var3970)
    assert (list(var3229) == [var311, var1050])

def function1188(function1737):
    with pytest.raises(ValueError):
        function1737.add_get('/', function1158(), name='invalid name')

def function1251(function1737):
    function1737.freeze()
    with pytest.raises(RuntimeError):
        function1737.add_get('/', function1158())

def function1650(function554, arg2361):
    var554 = web.Application()
    var554.freeze()
    with pytest.raises(RuntimeError):
        function554.add_subapp('/', var554)

def function2109(function554, arg89):
    function554.freeze()
    var3440 = web.Application()
    with pytest.raises(RuntimeError):
        function554.add_subapp('/', var3440)

def function2858(function1737):
    var2950 = function1737.add_static('/static', os.path.dirname(aiohttp.__file__))
    var2513 = None
    for var4027 in var2950:
        if (var4027.method == 'OPTIONS'):
            var2513 = var4027
    assert (var2513 is None)
    var2950.set_options_route(function1158())
    for var4027 in var2950:
        if (var4027.method == 'OPTIONS'):
            var2513 = var4027
    assert (var2513 is not None)
    with pytest.raises(RuntimeError):
        var2950.set_options_route(function1158())

def function2846(function1737):
    var1869 = function1737.add_route('GET', '/get/{_name}', function1158())
    assert (URL('/get/John') == var1869.url_for(_name='John'))

def function1352(function554, arg1362):
    var3120 = web.Application()
    with pytest.raises(ValueError):
        function554.add_subapp('', var3120)

def function2721(function554, arg142):
    var1052 = web.Application()
    with pytest.raises(ValueError):
        function554.add_subapp('/', var1052)

@asyncio.coroutine
def function1209(function1737):
    function635 = function1158()
    var1986 = function1737.add_get('', function635)
    var2014 = var1986.var2014
    assert (var2014.get_info() == {'path': '', })
    function1737.freeze()
    assert (var2014.get_info() == {'path': '/', })