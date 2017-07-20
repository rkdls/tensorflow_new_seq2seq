import asyncio
import datetime
import json
import re
from unittest import mock
import pytest
from multidict import CIMultiDict
from aiohttp import HttpVersion, HttpVersion10, HttpVersion11, hdrs, signals
from aiohttp.test_utils import make_mocked_request
from aiohttp.web import ContentCoding, Response, StreamResponse, json_response

def function2384(arg1224, arg1877, arg1675=CIMultiDict(), arg1037=HttpVersion11, **kwargs):
    var157 = (kwargs.pop('app', None) or mock.Mock())
    var157._debug = False
    var157.on_response_prepare = signals.Signal(var157)
    var718 = (kwargs.pop('protocol', None) or mock.Mock())
    return make_mocked_request(arg1224, arg1877, arg1675, version=arg1037, protocol=var718, app=var157, None=kwargs)

@pytest.yield_fixture
def function1511():
    return bytearray()

@pytest.yield_fixture
def function2174(function1511):
    function2174 = mock.Mock()

    def function2080(arg1534):
        arg1534(function2174.transport)

    def function2260(arg203):
        function1511.extend(arg203)

    def function746(arg1430):
        function1511.extend(arg1430)

    def function2125(arg955, arg1992):
        arg1992 = (arg955 + ''.join([(((var3292 + ': ') + var4165) + '\r\n') for (var3292, var4165) in arg1992.items()]))
        arg1992 = (arg1992.encode('utf-8') + b'\r\n')
        function1511.extend(arg1992)

    @asyncio.coroutine
    def function2183(arg1991=b''):
        function1511.extend(arg1991)
    function2174.function2080.side_effect = function2080
    function2174.transport.function746.side_effect = function746
    function2174.function746.side_effect = function746
    function2174.function2183.side_effect = function2183
    function2174.function2125.side_effect = function2125
    function2174.function2260.side_effect = function2260
    function2174.drain.return_value = ()
    return function2174

def function2261():
    var872 = StreamResponse()
    assert (200 == var872.status)
    assert (var872.keep_alive is None)
    assert (var872.task is None)
    var4679 = mock.Mock()
    var872._req = var4679
    assert (var872.task is var4679.task)

def function984():
    var1034 = StreamResponse()
    assert (var1034.content_length is None)

def function456():
    var1885 = StreamResponse()
    var1885.content_length = 234
    assert (234 == var1885.content_length)

def function2398():
    var1264 = StreamResponse()
    var1264.enable_chunked_encoding()
    with pytest.raises(RuntimeError):
        var1264.content_length = 234

def function687():
    var4116 = StreamResponse()
    var4116.content_length = 1
    assert ('1' == var4116.headers['Content-Length'])
    var4116.content_length = None
    assert ('Content-Length' not in var4116.headers)

def function846():
    var4392 = StreamResponse()
    var4392.content_length = None
    assert ('Content-Length' not in var4392.headers)
    var4392.content_length = None
    assert ('Content-Length' not in var4392.headers)

def function2235():
    var4725 = StreamResponse()
    var4725.content_type = 'text/html'
    assert ('text/html' == var4725.headers['content-type'])

def function15():
    var1889 = StreamResponse()
    var1889.content_type = 'text/html'
    var1889.charset = 'koi8-r'
    assert ('text/html; charset=koi8-r' == var1889.headers['content-type'])

def function1309():
    var2926 = StreamResponse()
    assert (var2926.charset is None)

def function2259():
    var4030 = StreamResponse()
    var4030.content_type = 'text/html'
    var4030.charset = None
    assert (var4030.charset is None)

def function38():
    var2234 = StreamResponse()
    var2234.content_type = 'text/html'
    var2234.charset = 'koi8-r'
    var2234.charset = None
    assert (var2234.charset is None)

def function1756():
    var2474 = StreamResponse()
    with pytest.raises(RuntimeError):
        var2474.charset = 'koi8-r'

def function2450():
    var483 = StreamResponse()
    assert (var483.last_modified is None)

def function29():
    var1802 = StreamResponse()
    var4318 = datetime.datetime(1990, 1, 2, 3, 4, 5, 0, datetime.timezone.utc)
    var1802.last_modified = 'Mon, 2 Jan 1990 03:04:05 GMT'
    assert (var1802.last_modified == var4318)

def function113():
    var752 = StreamResponse()
    var74 = datetime.datetime(1970, 1, 1, 0, 0, 0, 0, datetime.timezone.utc)
    var752.last_modified = 0
    assert (var752.last_modified == var74)
    var752.last_modified = 0.0
    assert (var752.last_modified == var74)

def function1786():
    var999 = StreamResponse()
    var2586 = datetime.datetime(2001, 2, 3, 4, 5, 6, 0, datetime.timezone.utc)
    var999.last_modified = var2586
    assert (var999.last_modified == var2586)

def function685():
    var3791 = StreamResponse()
    var3791.last_modified = 0
    var3791.last_modified = None
    assert (var3791.last_modified is None)

@asyncio.coroutine
def function1624():
    var610 = function2384('GET', '/', payload_writer=mock.Mock())
    var2962 = StreamResponse()
    assert (var2962.keep_alive is None)
    var894 = yield from var2962.prepare(var610)
    assert var894.function2125.called
    var2888 = yield from var2962.prepare(var610)
    assert (var894 is var2888)
    assert var2962.keep_alive
    var3874 = function2384('GET', '/')
    var3561 = yield from var2962.prepare(var3874)
    assert (var894 is var3561)

@asyncio.coroutine
def function1586():
    var1163 = function2384('GET', '/')
    var2418 = StreamResponse()
    assert (not var2418.chunked)
    var2418.enable_chunked_encoding()
    assert var2418.chunked
    var1931 = yield from var2418.prepare(var1163)
    assert var1931.chunked

def function2772():
    var1418 = StreamResponse()
    var1418.content_length = 234
    with pytest.raises(RuntimeError):
        var1418.enable_chunked_encoding()

@asyncio.coroutine
def function736():
    var4719 = function2384('GET', '/', payload_writer=mock.Mock())
    var2504 = StreamResponse()
    assert (not var2504.chunked)
    var2504.enable_chunked_encoding(chunk_size=8192)
    assert var2504.chunked
    var3835 = yield from var2504.prepare(var4719)
    assert var3835.chunked
    assert var3835.enable_chunking.called
    assert (var3835.filter is not None)

@asyncio.coroutine
def function1494():
    var4469 = function2384('GET', '/', version=HttpVersion10)
    var1413 = StreamResponse()
    var1413.enable_chunked_encoding()
    with pytest.raises(RuntimeError) as var4430:
        yield from var1413.prepare(var4469)
    assert re.match('Using chunked encoding is forbidden for HTTP/1.0', str(var4430.value))

@asyncio.coroutine
def function2558():
    var3802 = function2384('GET', '/', payload_writer=mock.Mock())
    var1551 = StreamResponse()
    assert (not var1551.chunked)
    assert (not var1551.compression)
    var1551.enable_compression()
    assert var1551.compression
    var1091 = yield from var1551.prepare(var3802)
    assert (not var1091.enable_compression.called)

@asyncio.coroutine
def function175():
    var3525 = function2384('GET', '/', payload_writer=mock.Mock())
    var1626 = StreamResponse()
    assert (not var1626.chunked)
    assert (not var1626.compression)
    var1626.enable_compression(force=True)
    assert var1626.compression
    var1656 = yield from var1626.prepare(var3525)
    assert var1656.enable_compression.called
    assert (var1656.filter is not None)

@asyncio.coroutine
def function1407():
    var1069 = function2384('GET', '/', payload_writer=mock.Mock())
    var2613 = StreamResponse()
    assert (not var2613.compression)
    var2613.enable_compression(force=False)
    assert var2613.compression
    var4447 = yield from var2613.prepare(var1069)
    assert (not var4447.enable_compression.called)

@asyncio.coroutine
def function2606():
    var4376 = function2384('GET', '/', headers=CIMultiDict({hdrs.ACCEPT_ENCODING: 'gzip, deflate', }))
    var1673 = StreamResponse()
    assert (not var1673.chunked)
    assert (not var1673.compression)
    var1673.enable_compression()
    assert var1673.compression
    var1240 = yield from var1673.prepare(var4376)
    var1240.enable_compression.assert_called_with('deflate')
    assert ('deflate' == var1673.headers.get(hdrs.CONTENT_ENCODING))
    assert (var1240.filter is not None)

@asyncio.coroutine
def function403():
    var2812 = function2384('GET', '/', headers=CIMultiDict({hdrs.ACCEPT_ENCODING: 'gzip, deflate', }))
    var2213 = StreamResponse()
    var2213.enable_compression(ContentCoding.deflate)
    assert var2213.compression
    var3172 = yield from var2213.prepare(var2812)
    var3172.enable_compression.assert_called_with('deflate')
    assert ('deflate' == var2213.headers.get(hdrs.CONTENT_ENCODING))

@asyncio.coroutine
def function1517():
    var4371 = function2384('GET', '/')
    var184 = StreamResponse()
    var184.enable_compression(ContentCoding.deflate)
    assert var184.compression
    var1445 = yield from var184.prepare(var4371)
    var1445.enable_compression.assert_called_with('deflate')
    assert ('deflate' == var184.headers.get(hdrs.CONTENT_ENCODING))

@asyncio.coroutine
def function2593():
    var3118 = function2384('GET', '/', headers=CIMultiDict({hdrs.ACCEPT_ENCODING: 'gzip, deflate', }))
    var420 = StreamResponse()
    var420.enable_compression(ContentCoding.gzip)
    assert var420.compression
    var1027 = yield from var420.prepare(var3118)
    var1027.enable_compression.assert_called_with('gzip')
    assert ('gzip' == var420.headers.get(hdrs.CONTENT_ENCODING))

@asyncio.coroutine
def function1795():
    var4714 = function2384('GET', '/')
    var3362 = StreamResponse()
    var3362.enable_compression(ContentCoding.gzip)
    assert var3362.compression
    var3443 = yield from var3362.prepare(var4714)
    var3443.enable_compression.assert_called_with('gzip')
    assert ('gzip' == var3362.headers.get(hdrs.CONTENT_ENCODING))

@asyncio.coroutine
def function1550():
    var2485 = function2384('GET', '/')
    var1186 = Response(body=b'answer')
    var1186.enable_compression(ContentCoding.gzip)
    yield from var1186.prepare(var2485)
    assert (var1186.content_length is None)

@asyncio.coroutine
def function1800():
    var2489 = StreamResponse()
    yield from var2489.prepare(function2384('GET', '/'))
    with pytest.raises(AssertionError):
        var2489.function746(123)

def function1072():
    var4017 = StreamResponse()
    with pytest.raises(RuntimeError):
        var4017.function746(b'data')

@asyncio.coroutine
def function1863():
    var1545 = StreamResponse()
    function2174 = mock.Mock()
    var2362 = yield from var1545.prepare(function2384('GET', '/', writer=function2174))
    var2362.write_eof = mock.Mock()
    var2362.function2183.return_value = ()
    var1545.function746(b'data')
    yield from var1545.function2183()
    function2174.function746.reset_mock()
    with pytest.raises(RuntimeError):
        var1545.function746(b'next data')
    assert (not function2174.function746.called)

@asyncio.coroutine
def function1319():
    var850 = StreamResponse()
    yield from var850.prepare(function2384('GET', '/'))
    assert var850.prepared
    var850.function746(b'data')
    yield from var850.function2183()
    assert (not var850.prepared)
    var185 = repr(var850)
    assert (var185 == '<StreamResponse OK eof>')

@asyncio.coroutine
def function481():
    var379 = StreamResponse()
    with pytest.raises(AssertionError):
        yield from var379.function2183()

@asyncio.coroutine
def function1553():
    var2941 = StreamResponse()
    function2174 = mock.Mock()
    var1373 = yield from var2941.prepare(function2384('GET', '/'))
    var1373.write = mock.Mock()
    var1373.write_eof = mock.Mock()
    var1373.function2183.return_value = ()
    var2941.function746(b'data')
    assert var1373.function746.called
    yield from var2941.function2183()
    var1373.function746.reset_mock()
    yield from var2941.function2183()
    assert (not function2174.function746.called)

@asyncio.coroutine
def function2885():
    var2881 = StreamResponse()
    yield from var2881.prepare(function2384('GET', '/'))
    with mock.patch('aiohttp.http_writer.noop') as var947:
        assert (var947 == var2881.function746(b'data'))

@asyncio.coroutine
def function559():
    var3706 = StreamResponse()
    yield from var3706.prepare(function2384('GET', '/'))
    with mock.patch('aiohttp.http_writer.noop') as var349:
        assert (var349.return_value == var3706.function746(b''))

def function1990():
    var1341 = StreamResponse()
    assert (var1341.keep_alive is None)
    var1341.force_close()
    assert (var1341.keep_alive is False)

@asyncio.coroutine
def function1069():
    var1210 = StreamResponse()
    yield from var1210.prepare(function2384('GET', '/'))
    with pytest.warns(DeprecationWarning):
        assert var1210.output_length

def function1874():
    var1043 = StreamResponse()
    assert (var1043.cookies == {})
    assert (str(var1043.cookies) == '')
    var1043.set_cookie('name', 'value')
    assert (str(var1043.cookies) == 'Set-Cookie: name=value; Path=/')
    var1043.set_cookie('name', 'other_value')
    assert (str(var1043.cookies) == 'Set-Cookie: name=other_value; Path=/')
    var1043.cookies['name'] = 'another_other_value'
    var1043.cookies['name']['max-age'] = 10
    assert (str(var1043.cookies) == 'Set-Cookie: name=another_other_value; Max-Age=10; Path=/')
    var1043.del_cookie('name')
    var1171 = 'Set-Cookie: name=("")?; expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=0; Path=/'
    assert re.match(var1171, str(var1043.cookies))
    var1043.set_cookie('name', 'value', domain='local.host')
    var1171 = 'Set-Cookie: name=value; Domain=local.host; Path=/'
    assert (str(var1043.cookies) == var1171)

def function2704():
    var3576 = StreamResponse()
    assert (var3576.cookies == {})
    var3576.set_cookie('name', 'value', path='/some/path')
    assert (str(var3576.cookies) == 'Set-Cookie: name=value; Path=/some/path')
    var3576.set_cookie('name', 'value', expires='123')
    assert (str(var3576.cookies) == 'Set-Cookie: name=value; expires=123; Path=/')
    var3576.set_cookie('name', 'value', domain='example.com', path='/home', expires='123', max_age='10', secure=True, httponly=True, version='2.0')
    assert (str(var3576.cookies).lower() == 'set-cookie: name=value; domain=example.com; expires=123; httponly; max-age=10; path=/home; secure; version=2.0')

def function2283():
    var914 = StreamResponse()
    assert (var914.cookies == {})
    assert (str(var914.cookies) == '')
    var914.del_cookie('name')
    var1988 = 'Set-Cookie: name=("")?; expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=0; Path=/'
    assert re.match(var1988, str(var914.cookies))

def function84():
    var1604 = StreamResponse()
    var1604.del_cookie('name')
    var1604.set_cookie('name', 'val')
    var4530 = 'Set-Cookie: name=val; Path=/'
    assert (str(var1604.cookies) == var4530)

def function2039():
    var3160 = StreamResponse()
    var3160.set_status(200, 'Everithing is fine!')
    assert (200 == var3160.status)
    assert ('Everithing is fine!' == var3160.reason)

@asyncio.coroutine
def function2600():
    var1612 = function2384('GET', '/')
    var873 = StreamResponse()
    var873.force_close()
    assert (not var873.keep_alive)
    yield from var873.prepare(var1612)
    assert (not var873.keep_alive)

@asyncio.coroutine
def function2635():
    var3564 = function2384('GET', '/path/to')
    var1028 = StreamResponse(reason=301)
    yield from var1028.prepare(var3564)
    assert ('<StreamResponse 301 GET /path/to >' == repr(var1028))

def function927():
    var2314 = StreamResponse(reason=301)
    assert ('<StreamResponse 301 not prepared>' == repr(var2314))

@asyncio.coroutine
def function1301():
    var2551 = function2384('GET', '/', version=HttpVersion10)
    var2174 = StreamResponse()
    yield from var2174.prepare(var2551)
    assert (not var2174.keep_alive)

@asyncio.coroutine
def function2153():
    var616 = CIMultiDict(Connection='keep-alive')
    var4227 = function2384('GET', '/', version=HttpVersion10, headers=var616)
    var4227._message = var4227._message._replace(should_close=False)
    var4525 = StreamResponse()
    yield from var4525.prepare(var4227)
    assert var4525.keep_alive

@asyncio.coroutine
def function242():
    var1699 = CIMultiDict(Connection='keep-alive')
    var4470 = function2384('GET', '/', version=HttpVersion(0, 9), headers=var1699)
    var3430 = StreamResponse()
    yield from var3430.prepare(var4470)
    assert (not var3430.keep_alive)

def function1937():
    var4220 = function2384('GET', '/')
    var2845 = StreamResponse()
    var7 = yield from var2845.prepare(var4220)
    var2781 = yield from var2845.prepare(var4220)
    assert (var7 is var2781)

@asyncio.coroutine
def function1294():
    var2937 = mock.Mock()
    var3046 = function2384('GET', '/', app=var2937)
    var1489 = StreamResponse()
    var818 = mock.Mock()
    var2937.on_response_prepare.append(var818)
    yield from var1489.prepare(var3046)
    var818.assert_called_with(var3046, var1489)

def function1952():
    var363 = StreamResponse()
    with pytest.raises(AssertionError):
        var363.tcp_nodelay

def function1386():
    var564 = StreamResponse()
    with pytest.raises(AssertionError):
        var564.set_tcp_nodelay(True)

@asyncio.coroutine
def function2556():
    var2122 = StreamResponse()
    function2174 = mock.Mock()
    function2174.tcp_nodelay = False
    var3632 = function2384('GET', '/', payload_writer=function2174)
    yield from var2122.prepare(var3632)
    assert (not var2122.tcp_nodelay)

def function872():
    var98 = StreamResponse()
    function2174 = mock.Mock()
    var1553 = function2384('GET', '/', payload_writer=function2174)
    yield from var98.prepare(var1553)
    var98.set_tcp_nodelay(True)
    function2174.set_tcp_nodelay.assert_called_with(True)

def function2781():
    var569 = StreamResponse()
    with pytest.raises(AssertionError):
        var569.tcp_cork

def function716():
    var1261 = StreamResponse()
    with pytest.raises(AssertionError):
        var1261.set_tcp_cork(True)

@asyncio.coroutine
def function645():
    var3602 = StreamResponse()
    function2174 = mock.Mock()
    function2174.tcp_cork = False
    var2319 = function2384('GET', '/', payload_writer=function2174)
    yield from var3602.prepare(var2319)
    assert (not var3602.tcp_cork)

def function1002():
    var130 = StreamResponse()
    function2174 = mock.Mock()
    var3541 = function2384('GET', '/', payload_writer=function2174)
    yield from var130.prepare(var3541)
    var130.set_tcp_cork(True)
    function2174.set_tcp_cork.assert_called_with(True)

def function1558():
    var2313 = Response()
    assert (200 == var2313.status)
    assert ('OK' == var2313.reason)
    assert (var2313.body is None)
    assert (var2313.content_length == 0)
    assert ('CONTENT-LENGTH' not in var2313.headers)

def function1171():
    var4509 = Response(body=b'body', status=201, headers={'Age': '12', 'DATE': 'date', })
    assert (201 == var4509.status)
    assert (b'body' == var4509.body)
    assert (var4509.headers['AGE'] == '12')
    var4509._start(mock.Mock(version=HttpVersion11))
    assert (4 == var4509.content_length)
    assert (var4509.headers['CONTENT-LENGTH'] == '4')

def function482():
    var3335 = Response(content_type='application/json')
    assert (200 == var3335.status)
    assert ('OK' == var3335.reason)
    assert (0 == var3335.content_length)
    assert (CIMultiDict([('CONTENT-TYPE', 'application/json')]) == var3335.headers)

def function938():
    with pytest.raises(ValueError):
        Response(body=b'123', text='test text')

def function524():
    var1443 = Response(text='test text')
    assert (200 == var1443.status)
    assert ('OK' == var1443.reason)
    assert (9 == var1443.content_length)
    assert (CIMultiDict([('CONTENT-TYPE', 'text/plain; charset=utf-8')]) == var1443.headers)
    assert (var1443.body == b'test text')
    assert (var1443.text == 'test text')
    var1443.headers['DATE'] = 'date'
    var1443._start(mock.Mock(version=HttpVersion11))
    assert (var1443.headers['CONTENT-LENGTH'] == '9')

def function1584():
    var3071 = Response(text='текст', charset='koi8-r')
    assert ('текст'.encode('koi8-r') == var3071.body)
    assert ('koi8-r' == var3071.charset)

def function1752():
    var490 = Response(text='test test', charset=None)
    assert ('utf-8' == var490.charset)

def function398():
    with pytest.raises(ValueError):
        Response(text='test test', content_type='text/plain; charset=utf-8')

def function1583():
    var2003 = Response(content_type='text/plain', charset='koi8-r')
    assert ('koi8-r' == var2003.charset)

def function316():
    with pytest.raises(ValueError):
        Response(headers={'Content-Type': 'application/json', }, content_type='text/html', text='text')

def function2497():
    with pytest.raises(ValueError):
        Response(headers={'Content-Type': 'application/json', }, charset='koi8-r', text='text')

def function302():
    with pytest.raises(ValueError):
        Response(headers={'Content-Type': 'application/json', }, content_type='text/html')

def function2609():
    with pytest.raises(ValueError):
        Response(headers={'Content-Type': 'application/json', }, charset='koi8-r')

def function292():
    var3239 = Response(body=b'data')
    with pytest.raises(ValueError):
        var3239.body = 123
    assert (b'data' == var3239.body)
    assert (4 == var3239.content_length)
    var3239.headers['DATE'] = 'date'
    var3239._start(mock.Mock(version=HttpVersion11))
    assert (var3239.headers['CONTENT-LENGTH'] == '4')
    assert (4 == var3239.content_length)

def function897():
    var3897 = Response(text='test')
    with pytest.raises(AssertionError):
        var3897.text = b'123'
    assert (b'test' == var3897.body)
    assert (4 == var3897.content_length)

def function567():
    var396 = Response()
    with pytest.raises(RuntimeError):
        var396.content_length = 1

@asyncio.coroutine
def function513(function1511, function2174):
    var4181 = function2384('GET', '/', payload_writer=function2174)
    var8 = Response()
    yield from var8.prepare(var4181)
    yield from var8.function2183()
    var3169 = function1511.decode('utf8')
    assert re.match('HTTP/1.1 200 OK\r\nContent-Length: 0\r\nContent-Type: application/octet-stream\r\nDate: .+\r\nServer: .+\r\n\r\n', var3169)

@asyncio.coroutine
def function386(function1511, function2174):
    var1649 = function2384('GET', '/', payload_writer=function2174)
    var2841 = Response(body=b'data')
    yield from var2841.prepare(var1649)
    yield from var2841.function2183()
    var3753 = function1511.decode('utf8')
    assert re.match('HTTP/1.1 200 OK\r\nContent-Length: 4\r\nContent-Type: application/octet-stream\r\nDate: .+\r\nServer: .+\r\n\r\ndata', var3753)

@asyncio.coroutine
def function1766(function1511, function2174):
    var2218 = Response()
    var2218.cookies['name'] = 'value'
    var1777 = function2384('GET', '/', payload_writer=function2174)
    yield from var2218.prepare(var1777)
    yield from var2218.function2183()
    var4192 = function1511.decode('utf8')
    assert re.match('HTTP/1.1 200 OK\r\nContent-Length: 0\r\nSet-Cookie: name=value\r\nContent-Type: application/octet-stream\r\nDate: .+\r\nServer: .+\r\n\r\n', var4192)

def function693():
    var34 = Response()
    var34.content_type = 'text/html'
    var34.text = 'text'
    assert ('text' == var34.text)
    assert (b'text' == var34.body)
    assert ('text/html' == var34.content_type)

def function934():
    var4233 = Response()
    var4233.content_type = 'text/plain'
    var4233.charset = 'KOI8-R'
    var4233.text = 'текст'
    assert ('текст' == var4233.text)
    assert ('текст'.encode('koi8-r') == var4233.body)
    assert ('koi8-r' == var4233.charset)

def function1529():
    var3969 = StreamResponse()
    assert (var3969.content_type == 'application/octet-stream')

def function2422():
    var1768 = Response()
    assert (var1768.content_type == 'application/octet-stream')

def function326():
    var4518 = Response(text='text')
    assert (var4518.content_type == 'text/plain')

def function563():
    var2458 = Response(body=b'body')
    assert (var2458.content_type == 'application/octet-stream')

def function579():
    var411 = StreamResponse()
    assert (not var411.prepared)

@asyncio.coroutine
def function2734():
    var1727 = StreamResponse()
    yield from var1727.prepare(function2384('GET', '/'))
    assert var1727.prepared

@asyncio.coroutine
def function1781():
    var407 = StreamResponse()
    with pytest.raises(AssertionError):
        yield from var407.drain()

@asyncio.coroutine
def function306():
    var4123 = StreamResponse()
    yield from var4123.prepare(function2384('GET', '/'))
    with pytest.raises(AssertionError):
        var4123.set_status(400)

def function349():
    with pytest.raises(TypeError):
        Response(text=b'data')

def function1465():
    var3732 = Response(text='data', content_type='text/html')
    assert ('data' == var3732.text)
    assert ('text/html' == var3732.content_type)

def function1692():
    var3531 = Response(text='текст', headers={'Content-Type': 'text/html; charset=koi8-r', })
    assert ('текст'.encode('koi8-r') == var3531.body)
    assert ('text/html' == var3531.content_type)
    assert ('koi8-r' == var3531.charset)

def function1864():
    var3689 = CIMultiDict({'Content-Type': 'text/html; charset=koi8-r', })
    var3629 = Response(text='текст', headers=var3689)
    assert ('текст'.encode('koi8-r') == var3629.body)
    assert ('text/html' == var3629.content_type)
    assert ('koi8-r' == var3629.charset)

def function1765():
    var4745 = CIMultiDict({'Content-Type': 'text/html; charset=koi8-r', })
    var2246 = Response(body='текст'.encode('koi8-r'), headers=var4745)
    assert ('текст'.encode('koi8-r') == var2246.body)
    assert ('text/html' == var2246.content_type)
    assert ('koi8-r' == var2246.charset)

def function920():
    var3221 = Response(status=200)
    assert (var3221.body is None)
    assert (var3221.text is None)

def function329():
    var2552 = Response(headers={'Content-Length': 123, })
    assert (var2552.content_length == 123)


class Class106:

    def function1052(self):
        var3776 = json_response('')
        assert ('application/json' == var3776.content_type)

    def function1200(self):
        var4076 = json_response(text=json.dumps('jaysawn'))
        assert (var4076.text == json.dumps('jaysawn'))

    def function676(self):
        with pytest.raises(ValueError) as var2020:
            json_response(data='foo', text='bar')
        var2606 = 'only one of data, text, or body should be specified'
        assert (var2606 == var2020.value.args[0])

    def function1720(self):
        with pytest.raises(ValueError) as var3037:
            json_response(data='foo', body=b'bar')
        var2256 = 'only one of data, text, or body should be specified'
        assert (var2256 == var3037.value.args[0])

    def function2175(self):
        var2416 = json_response({'foo': 42, })
        assert (json.dumps({'foo': 42, }) == var2416.text)

    def function1476(self):
        var598 = json_response({'foo': 42, }, content_type='application/vnd.json+api')
        assert ('application/vnd.json+api' == var598.content_type)