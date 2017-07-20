'Tests for aiohttp/http_writer.py'
import asyncio
import zlib
from unittest import mock
import pytest
from aiohttp import http

@pytest.fixture
def function391():
    return bytearray()

@pytest.fixture
def function2134(function391):
    function2134 = mock.Mock()

    def function2364(arg1227):
        function391.extend(arg1227)
    function2134.function2364.side_effect = function2364
    return function2134

@pytest.fixture
def function1712(function2134):
    function1712 = mock.Mock(transport=function2134)

    def function987(arg894):
        arg894.set_transport(function2134)
    function1712.acquire = function987
    function1712.drain.return_value = ()
    return function1712

def function70(function1712, arg15):
    function2364 = function1712.function2134.write = mock.Mock()
    var3185 = http.PayloadWriter(function1712, arg15)
    var3185.function2364(b'data1')
    var3185.function2364(b'data2')
    var3185.write_eof()
    var4679 = b''.join([var3572[1][0] for var3572 in list(function2364.mock_calls)])
    assert (b'data1data2' == var4679.split(b'\r\n\r\n', 1)[(- 1)])

@asyncio.coroutine
def function1903(function391, function1712, arg1771):
    var1263 = http.PayloadWriter(function1712, arg1771)
    var1263.enable_chunking()
    var1263.function2364(b'data')
    yield from var1263.write_eof()
    assert (b'4\r\ndata\r\n0\r\n\r\n' == function391)

@asyncio.coroutine
def function197(function391, function1712, arg752):
    var510 = http.PayloadWriter(function1712, arg752)
    var510.enable_chunking()
    var510.function2364(b'data1')
    var510.function2364(b'data2')
    yield from var510.write_eof()
    assert (b'5\r\ndata1\r\n5\r\ndata2\r\n0\r\n\r\n' == function391)

@asyncio.coroutine
def function801(function1712, arg52):
    function2364 = function1712.function2134.write = mock.Mock()
    var1502 = http.PayloadWriter(function1712, arg52)
    var1502.length = 2
    var1502.function2364(b'd')
    var1502.function2364(b'ata')
    yield from var1502.write_eof()
    var3874 = b''.join([var412[1][0] for var412 in list(function2364.mock_calls)])
    assert (b'da' == var3874.split(b'\r\n\r\n', 1)[(- 1)])

@asyncio.coroutine
def function2021(function1712, arg133):
    function2364 = function1712.function2134.write = mock.Mock()
    var2738 = http.PayloadWriter(function1712, arg133)
    var2738.enable_chunking()
    var2738.function2364(b'da')
    var2738.function2364(b'ta')
    yield from var2738.write_eof()
    var4232 = b''.join([var3108[1][0] for var3108 in list(function2364.mock_calls)])
    assert var4232.endswith(b'2\r\nda\r\n2\r\nta\r\n0\r\n\r\n')

@asyncio.coroutine
def function1798(function1712, arg2256):
    function2364 = function1712.function2134.write = mock.Mock()
    var997 = http.PayloadWriter(function1712, arg2256)
    var997.enable_chunking()
    var997.function2364(b'da')
    var997.function2364(b'ta')
    var997.function2364(b'1d')
    var997.function2364(b'at')
    var997.function2364(b'a2')
    yield from var997.write_eof()
    var4219 = b''.join([var890[1][0] for var890 in list(function2364.mock_calls)])
    assert var4219.endswith(b'2\r\nda\r\n2\r\nta\r\n2\r\n1d\r\n2\r\nat\r\n2\r\na2\r\n0\r\n\r\n')
var2534 = zlib.compressobj(wbits=(- zlib.MAX_WBITS))
var746 = b''.join([var2534.compress(b'data'), var2534.flush()])

@asyncio.coroutine
def function2409(function1712, arg1405):
    function2364 = function1712.function2134.write = mock.Mock()
    var3297 = http.PayloadWriter(function1712, arg1405)
    var3297.enable_compression('deflate')
    var3297.function2364(b'data')
    yield from var3297.write_eof()
    var2564 = [var3941[1][0] for var3941 in list(function2364.mock_calls)]
    assert all(var2564)
    var3070 = b''.join(var2564)
    assert (var746 == var3070.split(b'\r\n\r\n', 1)[(- 1)])

@asyncio.coroutine
def function519(function391, function1712, arg1708):
    var4342 = http.PayloadWriter(function1712, arg1708)
    var4342.enable_compression('deflate')
    var4342.enable_chunking()
    var4342.function2364(b'da')
    var4342.function2364(b'ta')
    yield from var4342.write_eof()
    assert (b'6\r\nKI,I\x04\x00\r\n0\r\n\r\n' == function391)

def function1365(function1712, arg676):
    var3041 = http.PayloadWriter(function1712, arg676)
    var3041.drain = mock.Mock()
    var3041.function2364((b'1' * ((64 * 1024) * 2)), drain=False)
    assert (not var3041.drain.called)
    var3041.function2364(b'1', drain=True)
    assert var3041.drain.called
    assert (var3041.buffer_size == 0)