'Tests for aiohttp/protocol.py'
import asyncio
import unittest
import zlib
from unittest import mock
import pytest
from multidict import CIMultiDict
from yarl import URL
import aiohttp
from aiohttp import http_exceptions, streams
from aiohttp.http_parser import DeflateBuffer, HttpPayloadParser, HttpRequestParserPy, HttpResponseParserPy
var3427 = [HttpRequestParserPy]
var3801 = [HttpResponseParserPy]
try:
    from aiohttp import _http_parser
    var3427.append(_http_parser.HttpRequestParserC)
    var3801.append(_http_parser.HttpResponseParserC)
except ImportError:
    pass

@pytest.fixture
def function1111():
    return mock.Mock()

@pytest.fixture(params=var3427)
def function2080(arg1798, function1111, arg1282):
    'Parser implementations'
    return arg1282.param(function1111, arg1798, 8190, 32768, 8190)

@pytest.fixture(params=var3427)
def function2058(arg1351):
    'Request Parser class'
    return arg1351.param

@pytest.fixture(params=var3801)
def function105(arg2308, function1111, arg928):
    'Parser implementations'
    return arg928.param(function1111, arg2308, 8190, 32768, 8190)

@pytest.fixture(params=var3801)
def function2102(arg1172):
    'Parser implementations'
    return arg1172.param

def function1394(function2080):
    var324 = b'GET /test HTTP/1.1\r\ntest: line\r\n continue\r\ntest2: data\r\n\r\n'
    (var1443, var522, var3589) = function2080.feed_data(var324)
    assert (len(var1443) == 1)
    var4365 = var1443[0][0]
    assert (list(var4365.headers.items()) == [('Test', 'line continue'), ('Test2', 'data')])
    assert (var4365.raw_headers == ((b'test', b'line continue'), (b'test2', b'data')))
    assert (not var4365.should_close)
    assert (var4365.compression is None)
    assert (not var4365.var522)

def function2184(function2080):
    var1258 = b'GET /test HTTP/1.1\r\n\r\n'
    (var3604, var4047, var1431) = function2080.feed_data(var1258)
    assert (len(var3604) == 1)
    (var3401, var874) = var3604[0]
    assert (var3401.compression is None)
    assert (not var3401.var4047)
    assert (var3401.method == 'GET')
    assert (var3401.path == '/test')
    assert (var3401.version == (1, 1))

@asyncio.coroutine
def function1824(function2080):
    var2737 = b'GET /test HTTP/1.1\r\nContent-Length: 4\r\n\r\nbody'
    (var4175, var2987, var2094) = function2080.feed_data(var2737)
    assert (len(var4175) == 1)
    (var3057, var4180) = var4175[0]
    var1366 = yield from var4180.read(4)
    assert (var1366 == b'body')

def function1935(function2080):
    var3562 = b'GET /test HTTP/1.1\r\n'
    (var1169, var596, var2178) = function2080.feed_data(var3562)
    assert (len(var1169) == 0)
    assert (not var596)
    (var1169, var596, var2178) = function2080.feed_data(b'\r\n')
    assert (len(var1169) == 1)
    var483 = var1169[0][0]
    assert (var483.method == 'GET')

def function2891(function2080):
    var4073 = b'GET /test HTTP/1.1\r\n'
    var3700 = b'test: line\r'
    var1884 = b'\n continue\r\n\r\n'
    (var3964, var2265, var3898) = function2080.feed_data(var4073)
    assert (len(var3964) == 0)
    (var3964, var2265, var3898) = function2080.feed_data(var3700)
    assert (len(var3964) == 0)
    (var3964, var2265, var3898) = function2080.feed_data(var1884)
    assert (len(var3964) == 1)
    var1027 = var3964[0][0]
    assert (list(var1027.headers.items()) == [('Test', 'line continue')])
    assert (var1027.raw_headers == ((b'test', b'line continue'),))
    assert (not var1027.should_close)
    assert (var1027.compression is None)
    assert (not var1027.var2265)

def function1430(function2080):
    var1297 = b'GET /test HTTP/1.1\r\nSet-Cookie: c1=cookie1\r\nSet-Cookie: c2=cookie2\r\n\r\n'
    (var3835, var3758, var3705) = function2080.feed_data(var1297)
    assert (len(var3835) == 1)
    var4133 = var3835[0][0]
    assert (list(var4133.headers.items()) == [('Set-Cookie', 'c1=cookie1'), ('Set-Cookie', 'c2=cookie2')])
    assert (var4133.raw_headers == ((b'Set-Cookie', b'c1=cookie1'), (b'Set-Cookie', b'c2=cookie2')))
    assert (not var4133.should_close)
    assert (var4133.compression is None)

def function1586(function2080):
    var4324 = b'GET /test HTTP/1.0\r\n\r\n'
    (var1213, var2872, var1014) = function2080.feed_data(var4324)
    var4567 = var1213[0][0]
    assert var4567.should_close

def function1371(function2080):
    var4499 = b'GET /test HTTP/1.1\r\n\r\n'
    (var3054, var3952, var4547) = function2080.feed_data(var4499)
    var4425 = var3054[0][0]
    assert (not var4425.should_close)

def function1439(function2080):
    var985 = b'GET /test HTTP/1.1\r\nconnection: close\r\n\r\n'
    (var132, var3607, var4004) = function2080.feed_data(var985)
    var3684 = var132[0][0]
    assert var3684.should_close

def function755(function2080):
    var4207 = b'GET /test HTTP/1.0\r\nconnection: close\r\n\r\n'
    (var4575, var1321, var2099) = function2080.feed_data(var4207)
    var1145 = var4575[0][0]
    assert var1145.should_close

def function766(function2080):
    var1933 = b'GET /test HTTP/1.0\r\nconnection: keep-alive\r\n\r\n'
    (var1649, var2595, var1098) = function2080.feed_data(var1933)
    var2466 = var1649[0][0]
    assert (not var2466.should_close)

def function447(function2080):
    var721 = b'GET /test HTTP/1.1\r\nconnection: keep-alive\r\n\r\n'
    (var2943, var1709, var2190) = function2080.feed_data(var721)
    var3534 = var2943[0][0]
    assert (not var3534.should_close)

def function2641(function2080):
    var160 = b'GET /test HTTP/1.0\r\nconnection: test\r\n\r\n'
    (var3523, var1183, var1819) = function2080.feed_data(var160)
    var545 = var3523[0][0]
    assert var545.should_close

def function2622(function2080):
    var227 = b'GET /test HTTP/1.1\r\nconnection: test\r\n\r\n'
    (var1754, var2667, var1432) = function2080.feed_data(var227)
    var1970 = var1754[0][0]
    assert (not var1970.should_close)

def function1492(function2080):
    var537 = b'GET /test HTTP/1.1\r\ntransfer-encoding: chunked\r\n\r\n'
    (var758, var2893, var2228) = function2080.feed_data(var537)
    (var3291, var2841) = var758[0]
    assert var3291.chunked
    assert (not var2893)
    assert isinstance(var2841, streams.FlowControlStreamReader)

def function24(function2080):
    var727 = b'GET /test HTTP/1.1\r\nconnection: upgrade\r\nupgrade: websocket\r\n\r\n'
    (var3325, var2139, var3185) = function2080.feed_data(var727)
    var4662 = var3325[0][0]
    assert (not var4662.should_close)
    assert var4662.upgrade
    assert upgrade

def function282(function2080):
    var107 = b'GET /test HTTP/1.1\r\ncontent-encoding: deflate\r\n\r\n'
    (var1555, var2753, var811) = function2080.feed_data(var107)
    var3424 = var1555[0][0]
    assert (var3424.compression == 'deflate')

def function1090(function2080):
    var2568 = b'GET /test HTTP/1.1\r\ncontent-encoding: gzip\r\n\r\n'
    (var3943, var3233, var3571) = function2080.feed_data(var2568)
    var1238 = var3943[0][0]
    assert (var1238.compression == 'gzip')

def function525(function2080):
    var2050 = b'GET /test HTTP/1.1\r\ncontent-encoding: compress\r\n\r\n'
    (var352, var4377, var3041) = function2080.feed_data(var2050)
    var2636 = var352[0][0]
    assert (not var2636.compression)

def function2387(function2080):
    var1810 = b'CONNECT www.google.com HTTP/1.1\r\ncontent-length: 0\r\n\r\n'
    (var1929, var2706, var1111) = function2080.feed_data(var1810)
    (var2743, var4558) = var1929[0]
    assert upgrade
    assert isinstance(var4558, streams.FlowControlStreamReader)

def function1092(function2080):
    var237 = b'GET /test HTTP/1.1\r\nSEC-WEBSOCKET-KEY1: line\r\n\r\n'
    with pytest.raises(http_exceptions.BadHttpMessage):
        function2080.feed_data(var237)

def function1748(function2080):
    var630 = b'GET /test HTTP/1.1\r\ncontent-length: line\r\n\r\n'
    with pytest.raises(http_exceptions.BadHttpMessage):
        function2080.feed_data(var630)

def function2222(function2080):
    var4138 = b'GET /test HTTP/1.1\r\ncontent-length: -1\r\n\r\n'
    with pytest.raises(http_exceptions.BadHttpMessage):
        function2080.feed_data(var4138)

def function779(function2080):
    var4486 = b'GET /test HTTP/1.1\r\ntest line\r\n\r\n'
    with pytest.raises(http_exceptions.BadHttpMessage):
        function2080.feed_data(var4486)

def function2771(function2080):
    var4260 = b'GET /test HTTP/1.1\r\ntest[]: line\r\n\r\n'
    with pytest.raises(http_exceptions.BadHttpMessage):
        function2080.feed_data(var4260)

def function776(function2080):
    var3944 = ((b'test' * 10) * 1024)
    var2818 = ((b'GET /test HTTP/1.1\r\n' + var3944) + b':data\r\n\r\n')
    with pytest.raises(http_exceptions.LineTooLong):
        function2080.feed_data(var2818)

def function2774(function2080):
    var1947 = ((b'test' * 10) * 1024)
    var4715 = ((b'GET /test HTTP/1.1\r\ndata:' + var1947) + b'\r\n\r\n')
    with pytest.raises(http_exceptions.LineTooLong):
        function2080.feed_data(var4715)

def function2749(function2080):
    var2933 = ((b'test' * 10) * 1024)
    var67 = ((b'GET /test HTTP/1.1\r\ndata: test\r\n ' + var2933) + b'\r\n\r\n')
    with pytest.raises(http_exceptions.LineTooLong):
        function2080.feed_data(var67)

def function86(function2080):
    var3674 = b'GET /path HTTP/1.1\r\n\r\n'
    (var4367, var4284, var228) = function2080.feed_data(var3674)
    var2146 = var4367[0][0]
    assert (var2146 == ('GET', '/path', (1, 1), CIMultiDict(), (), False, None, False, False, URL('/path')))

def function2081(function2080):
    var4145 = b'getpath \r\n\r\n'
    with pytest.raises(http_exceptions.BadStatusLine):
        function2080.feed_data(var4145)

def function432(function2080):
    var2894 = b'GET /test HTTP/1.1\r\nconnection: upgrade\r\nupgrade: websocket\r\n\r\nsome raw data'
    (var2472, var4026, var736) = function2080.feed_data(var2894)
    var1626 = var2472[0][0]
    assert (not var1626.should_close)
    assert var1626.upgrade
    assert upgrade
    assert (var736 == b'some raw data')

def function342(function2080):
    var2029 = 'GET /path HTTP/1.1\r\nx-test:тест\r\n\r\n'.encode('utf-8')
    (var3199, var3769, var2793) = function2080.feed_data(var2029)
    var4287 = var3199[0][0]
    assert (var4287 == ('GET', '/path', (1, 1), CIMultiDict([('X-TEST', 'тест')]), ((b'x-test', 'тест'.encode('utf-8')),), False, None, False, False, URL('/path')))

def function2239(function2080):
    var676 = 'GET /path HTTP/1.1\r\nx-test:тест\r\n\r\n'.encode('cp1251')
    var4108 = function2080.feed_data(var676)[0][0][0]
    assert (var4108 == ('GET', '/path', (1, 1), CIMultiDict([('X-TEST', 'тест'.encode('cp1251').decode('utf-8', 'surrogateescape'))]), ((b'x-test', 'тест'.encode('cp1251')),), False, None, False, False, URL('/path')))

def function196(function2080):
    var3084 = b'GET //path HTTP/1.1\r\n\r\n'
    var4698 = function2080.feed_data(var3084)[0][0][0]
    assert (var4698[:(- 1)] == ('GET', '//path', (1, 1), CIMultiDict(), (), False, None, False, False))

def function557(function2080):
    with pytest.raises(http_exceptions.BadStatusLine):
        function2080.feed_data(b'!12%()+=~$ /get HTTP/1.1\r\n\r\n')

def function2293(function2080):
    with pytest.raises(http_exceptions.BadHttpMessage):
        function2080.feed_data(b'GET //get HT/11\r\n\r\n')

def function1084(function2080):
    with pytest.raises(http_exceptions.LineTooLong):
        function2080.feed_data(((b'GET /path' + ((b'test' * 10) * 1024)) + b' HTTP/1.1\r\n\r\n'))

def function2316(function105):
    var1427 = 'HTTP/1.1 200 Ok\r\nx-test:тест\r\n\r\n'.encode('utf-8')
    (var1655, var209, var4707) = function105.feed_data(var1427)
    assert (len(var1655) == 1)
    var3302 = var1655[0][0]
    assert (var3302.version == (1, 1))
    assert (var3302.code == 200)
    assert (var3302.reason == 'Ok')
    assert (var3302.headers == CIMultiDict([('X-TEST', 'тест')]))
    assert (var3302.raw_headers == ((b'x-test', 'тест'.encode('utf-8')),))
    assert (not var209)
    assert (not var4707)

def function765(function105):
    with pytest.raises(http_exceptions.LineTooLong):
        function105.feed_data(((b'HTTP/1.1 200 Ok' + ((b'test' * 10) * 1024)) + b'\r\n\r\n'))

def function1679(function105):
    with pytest.raises(http_exceptions.BadHttpMessage):
        function105.feed_data(b'HT/11 200 Ok\r\n\r\n')

def function720(function105):
    var706 = function105.feed_data(b'HTTP/1.1 200\r\n\r\n')[0][0][0]
    assert (var706.version == (1, 1))
    assert (var706.code == 200)
    assert (not var706.reason)

def function2511(function105):
    with pytest.raises(http_exceptions.BadHttpMessage):
        function105.feed_data(b'HTT/1\r\n\r\n')

def function2379(function105):
    var3755 = function105.feed_data(b'HTTP/1.1 99 test\r\n\r\n')[0][0][0]
    assert (var3755.code == 99)

def function1625(function105):
    with pytest.raises(http_exceptions.BadHttpMessage):
        function105.feed_data(b'HTTP/1.1 9999 test\r\n\r\n')

def function2888(function105):
    with pytest.raises(http_exceptions.BadHttpMessage):
        function105.feed_data(b'HTTP/1.1 ttt test\r\n\r\n')

def function1888(function2080):
    var2063 = b'GET /test HTTP/1.1\r\ntransfer-encoding: chunked\r\n\r\n'
    (var709, var471) = function2080.feed_data(var2063)[0][0]
    assert var709.chunked
    assert (not var471.is_eof())
    assert isinstance(var471, streams.FlowControlStreamReader)
    function2080.feed_data(b'4\r\ndata\r\n4\r\nline\r\n0\r\n\r\n')
    assert (b'dataline' == b''.join((d for var1434 in var471._buffer)))
    assert var471.is_eof()

def function807(function2080):
    var2577 = b'GET /test HTTP/1.1\r\ntransfer-encoding: chunked\r\n\r\n'
    (var2244, var4527) = function2080.feed_data(var2577)[0][0]
    (var2341, var4669, var2571) = function2080.feed_data(b'4\r\ndata\r\n4\r\nline\r\n0\r\n\r\nPOST /test2 HTTP/1.1\r\ntransfer-encoding: chunked\r\n\r\n')
    assert (b'dataline' == b''.join((d for var902 in var4527._buffer)))
    assert var4527.is_eof()
    assert (len(var2341) == 1)
    (var3248, var589) = var2341[0]
    assert (var3248.method == 'POST')
    assert var3248.chunked
    assert (not var589.is_eof())

def function2333(function2080):
    var4196 = b'GET /test HTTP/1.1\r\ntransfer-encoding: chunked\r\n\r\n'
    (var4688, var1264) = function2080.feed_data(var4196)[0][0]
    function2080.feed_data(b'4\r\ndata\r')
    function2080.feed_data(b'\n4')
    function2080.feed_data(b'\r')
    function2080.feed_data(b'\n')
    function2080.feed_data(b'line\r\n0\r\n')
    function2080.feed_data(b'test: test\r\n')
    assert (b'dataline' == b''.join((d for var746 in var1264._buffer)))
    assert (not var1264.is_eof())
    function2080.feed_data(b'\r\n')
    assert (b'dataline' == b''.join((d for var746 in var1264._buffer)))
    assert var1264.is_eof()

def function1594(function2080):
    var4410 = b'GET /test HTTP/1.1\r\ntransfer-encoding: chunked\r\n\r\n'
    (var1116, var4434) = function2080.feed_data(var4410)[0][0]
    function2080.feed_data(b'4;test\r\ndata\r\n4\r\nline\r\n0\r\ntest: test\r\n\r\n')
    assert (b'dataline' == b''.join((d for var2263 in var4434._buffer)))
    assert var4434.is_eof()

def function2636(arg1485, function1111, function2058):
    function2080 = function2058(function1111, arg1485, readall=True)
    var1861 = b'POST /test HTTP/1.1\r\n\r\n'
    (var1103, var3661) = function2080.feed_data(var1861)[0][0]
    assert var3661.is_eof()

def function1994(arg415, function1111, function2102):
    function2080 = function2102(function1111, arg415, response_with_body=False)
    var402 = b'HTTP/1.1 200 Ok\r\ncontent-length: 10\r\n\r\n'
    (var2567, var4531) = function2080.feed_data(var402)[0][0]
    assert var4531.is_eof()

def function2665(function105):
    var1197 = b'HTTP/1.1 200 Ok\r\ncontent-length: 4\r\n\r\n'
    (var798, var1280) = function105.feed_data(var1197)[0][0]
    assert (not var1280.is_eof())
    function105.feed_data(b'da')
    function105.feed_data(b't')
    function105.feed_data(b'aHT')
    assert var1280.is_eof()
    assert (b'data' == b''.join((d for var4548 in var1280._buffer)))

def function838(function2080):
    var828 = b'PUT / HTTP/1.1\r\n\r\n'
    (var362, var1217) = function2080.feed_data(var828)[0][0]
    assert var1217.is_eof()


class Class205(unittest.TestCase):

    def function151(self):
        self.attribute1609 = mock.Mock()
        asyncio.set_event_loop(None)

    def function1736(self):
        var4070 = aiohttp.FlowControlDataQueue(self.attribute1609)
        var4592 = HttpPayloadParser(var4070, readall=True)
        var4592.feed_data(b'data')
        var4592.feed_eof()
        self.assertTrue(var4070.is_eof())
        self.assertEqual([(bytearray(b'data'), 4)], list(var4070._buffer))

    def function654(self):
        var3970 = aiohttp.FlowControlDataQueue(self.attribute1609)
        var952 = HttpPayloadParser(var3970, method='PUT')
        self.assertTrue(var3970.is_eof())
        self.assertTrue(var952.done)

    def function1379(self):
        var1319 = aiohttp.FlowControlDataQueue(self.attribute1609)
        var703 = HttpPayloadParser(var1319, length=4)
        var703.feed_data(b'da')
        with pytest.raises(http_exceptions.ContentLengthError):
            var703.feed_eof()

    def function1441(self):
        var532 = aiohttp.FlowControlDataQueue(self.attribute1609)
        var1249 = HttpPayloadParser(var532, chunked=True)
        self.assertRaises(http_exceptions.TransferEncodingError, var1249.feed_data, b'blah\r\n')
        self.assertIsInstance(var532.exception(), http_exceptions.TransferEncodingError)

    def function2679(self):
        var942 = aiohttp.FlowControlDataQueue(self.attribute1609)
        var2692 = HttpPayloadParser(var942, length=2)
        (var3201, var2572) = var2692.feed_data(b'1245')
        self.assertTrue(var3201)
        self.assertEqual(b'12', b''.join((d for (var64, var3572) in var942._buffer)))
        self.assertEqual(b'45', var2572)
    var167 = zlib.compressobj(wbits=(- zlib.MAX_WBITS))
    var1089 = b''.join([var167.compress(b'data'), var167.flush()])

    def function167(self):
        var377 = len(self.var1089)
        var4646 = aiohttp.FlowControlDataQueue(self.attribute1609)
        var4316 = HttpPayloadParser(var4646, length=var377, compression='deflate')
        var4316.feed_data(self.var1089)
        self.assertEqual(b'data', b''.join((d for (var702, var1491) in var4646._buffer)))
        self.assertTrue(var4646.is_eof())

    def function1758(self):
        var2213 = aiohttp.FlowControlDataQueue(self.attribute1609)
        var1764 = HttpPayloadParser(var2213, length=0)
        self.assertTrue(var1764.done)
        self.assertTrue(var2213.is_eof())


class Class19(unittest.TestCase):

    def function1848(self):
        self.attribute1675 = mock.Mock()
        asyncio.set_event_loop(None)

    def function660(self):
        var3553 = aiohttp.FlowControlDataQueue(self.attribute1675)
        var119 = DeflateBuffer(var3553, 'deflate')
        var119.zlib = mock.Mock()
        var119.zlib.decompress.return_value = b'line'
        var119.feed_data(b'data', 4)
        self.assertEqual([b'line'], list((d for (var719, var2543) in var3553._buffer)))

    def function641(self):
        var1278 = aiohttp.FlowControlDataQueue(self.attribute1675)
        var1584 = DeflateBuffer(var1278, 'deflate')
        var2970 = ValueError()
        var1584.zlib = mock.Mock()
        var1584.zlib.decompress.side_effect = var2970
        self.assertRaises(http_exceptions.ContentEncodingError, var1584.feed_data, b'data', 4)

    def function946(self):
        var3443 = aiohttp.FlowControlDataQueue(self.attribute1675)
        var4336 = DeflateBuffer(var3443, 'deflate')
        var4336.zlib = mock.Mock()
        var4336.zlib.flush.return_value = b'line'
        var4336.feed_eof()
        self.assertEqual([b'line'], list((d for (var3003, var4630) in var3443._buffer)))
        self.assertTrue(var3443._eof)

    def function751(self):
        var711 = aiohttp.FlowControlDataQueue(self.attribute1675)
        var3846 = DeflateBuffer(var711, 'deflate')
        var3846.zlib = mock.Mock()
        var3846.zlib.flush.return_value = b'line'
        var3846.zlib.eof = False
        self.assertRaises(http_exceptions.ContentEncodingError, var3846.feed_eof)

    def function279(self):
        var2756 = aiohttp.FlowControlDataQueue(self.attribute1675)
        var4405 = DeflateBuffer(var2756, 'deflate')
        var4405.feed_eof()
        self.assertTrue(var2756.at_eof())