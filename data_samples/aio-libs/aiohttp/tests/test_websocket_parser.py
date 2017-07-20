import random
import struct
from unittest import mock
import pytest
import aiohttp
from aiohttp import http_websocket
from aiohttp.http import WebSocketError, WSCloseCode, WSMessage, WSMsgType
from aiohttp.http_websocket import PACK_CLOSE_CODE, PACK_LEN1, PACK_LEN2, PACK_LEN3, WebSocketReader, _websocket_mask

def function2753(arg395, arg209, arg498=False, arg1608=False, arg251=True):
    'Send a frame over the websocket with message as its payload.'
    var3842 = len(arg395)
    if arg498:
        var3862 = 128
    else:
        var3862 = 0
    if arg251:
        var1847 = (128 | arg209)
    else:
        var1847 = arg209
    if (var3842 < 126):
        var3749 = PACK_LEN1(var1847, (var3842 | var3862))
    elif (var3842 < (1 << 16)):
        var3749 = PACK_LEN2(var1847, (126 | var3862), var3842)
    else:
        var3749 = PACK_LEN3(var1847, (127 | var3862), var3842)
    if arg498:
        var2025 = random.randrange(0, 4294967295)
        var2025 = var2025.to_bytes(4, 'big')
        arg395 = bytearray(arg395)
        _websocket_mask(var2025, arg395)
        if arg1608:
            return arg395
        else:
            return ((var3749 + var2025) + arg395)
    elif arg1608:
        return arg395
    else:
        return (var3749 + arg395)

def function2245(arg1698=1000, arg1844=b'', arg934=False):
    'Close the websocket, sending the specified code and message.'
    if isinstance(arg1844, str):
        arg1844 = arg1844.encode('utf-8')
    return function2753((PACK_CLOSE_CODE(arg1698) + arg1844), opcode=WSMsgType.CLOSE, noheader=arg934)

@pytest.fixture()
def function2574(arg1241):
    return aiohttp.DataQueue(loop=arg1241)

@pytest.fixture()
def function2564(function2574):
    return WebSocketReader(function2574)

def function2649(function2564):
    function2564.parse_frame(struct.pack('!BB', 1, 1))
    var2550 = function2564.parse_frame(b'1')
    (var2411, var1597, var4627) = var2550[0]
    assert ((0, 1, b'1') == (var2411, var1597, var4627))

def function1240(function2564):
    (var1901, var1145, var4611) = function2564.parse_frame(struct.pack('!BB', 1, 0))[0]
    assert ((0, 1, b'') == (var1901, var1145, var4611))

def function1982(function2564):
    function2564.parse_frame(struct.pack('!BB', 1, 126))
    function2564.parse_frame(struct.pack('!H', 4))
    var3244 = function2564.parse_frame(b'1234')
    (var2797, var4616, var1855) = var3244[0]
    assert ((0, 1, b'1234') == (var2797, var4616, var1855))

def function456(function2564):
    function2564.parse_frame(struct.pack('!BB', 1, 127))
    function2564.parse_frame(struct.pack('!Q', 4))
    (var1015, var4079, var2193) = function2564.parse_frame(b'1234')[0]
    assert ((0, 1, b'1234') == (var1015, var4079, var2193))

def function426(function2564):
    function2564.parse_frame(struct.pack('!BB', 1, 129))
    function2564.parse_frame(b'0001')
    (var3274, var2181, var493) = function2564.parse_frame(b'1')[0]
    assert ((0, 1, b'\x01') == (var3274, var2181, var493))

def function2113(function2574, function2564):
    with pytest.raises(WebSocketError):
        function2564.parse_frame(struct.pack('!BB', 96, 0))
        raise function2574.exception()

def function578(function2574, function2564):
    with pytest.raises(WebSocketError):
        function2564.parse_frame(struct.pack('!BB', 8, 0))
        raise function2574.exception()

def function335(function2574, function2564):
    with pytest.raises(WebSocketError):
        function2564.parse_frame(struct.pack('!BB', 0, 0))
        raise function2574.exception()

def function1340(function2574, function2564):
    with pytest.raises(WebSocketError):
        function2564.parse_frame(struct.pack('!BB', 136, 126))
        raise function2574.exception()

def function313(function2574, function2564):
    function2564.parse_frame = mock.Mock()
    function2564.parse_frame.return_value = [(1, WSMsgType.PING, b'data')]
    function2564.feed_data(b'')
    var3553 = function2574._buffer[0]
    assert (var3553 == ((WSMsgType.PING, b'data', ''), 4))

def function1791(function2574, function2564):
    function2564.parse_frame = mock.Mock()
    function2564.parse_frame.return_value = [(1, WSMsgType.PONG, b'data')]
    function2564.feed_data(b'')
    var2308 = function2574._buffer[0]
    assert (var2308 == ((WSMsgType.PONG, b'data', ''), 4))

def function391(function2574, function2564):
    function2564.parse_frame = mock.Mock()
    function2564.parse_frame.return_value = [(1, WSMsgType.CLOSE, b'')]
    function2564.feed_data(b'')
    var978 = function2574._buffer[0]
    assert (var978 == ((WSMsgType.CLOSE, 0, ''), 0))

def function2724(function2574, function2564):
    function2564.parse_frame = mock.Mock()
    function2564.parse_frame.return_value = [(1, WSMsgType.CLOSE, b'0112345')]
    function2564.feed_data(b'')
    var4135 = function2574._buffer[0]
    assert (var4135 == (WSMessage(WSMsgType.CLOSE, 12337, '12345'), 0))

def function1824(function2574, function2564):
    function2564.parse_frame = mock.Mock()
    function2564.parse_frame.return_value = [(1, WSMsgType.CLOSE, b'1')]
    function2564.feed_data(b'')
    assert isinstance(function2574.exception(), WebSocketError)
    assert (function2574.exception().code == WSCloseCode.PROTOCOL_ERROR)

def function338(function2574, function2564):
    var3831 = function2245(code=1)
    with pytest.raises(WebSocketError) as var1088:
        function2564._feed_data(var3831)
    assert (var1088.value.code == WSCloseCode.PROTOCOL_ERROR)

def function1950(function2564):
    var4020 = function2245(code=1000, message=b'\xf4\x90\x80\x80')
    with pytest.raises(WebSocketError) as var1530:
        function2564._feed_data(var4020)
    assert (var1530.value.code == WSCloseCode.INVALID_TEXT)

def function1292(function2574, function2564):
    function2564.parse_frame = mock.Mock()
    function2564.parse_frame.return_value = [(1, WSMsgType.CONTINUATION, b'')]
    with pytest.raises(WebSocketError):
        function2564.feed_data(b'')
        raise function2574.exception()

def function2333(function2574, function2564):
    var3300 = function2753(b'text', WSMsgType.TEXT)
    function2564._feed_data(var3300)
    var4412 = function2574._buffer[0]
    assert (var4412 == ((WSMsgType.TEXT, 'text', ''), 4))

def function1750(function2564):
    var2621 = function2753(b'\xf4\x90\x80\x80', WSMsgType.TEXT)
    with pytest.raises(WebSocketError) as var3541:
        function2564._feed_data(var2621)
    assert (var3541.value.code == WSCloseCode.INVALID_TEXT)

def function605(function2574, function2564):
    function2564.parse_frame = mock.Mock()
    function2564.parse_frame.return_value = [(1, WSMsgType.BINARY, b'binary')]
    function2564.feed_data(b'')
    var825 = function2574._buffer[0]
    assert (var825 == ((WSMsgType.BINARY, b'binary', ''), 6))

def function1009(function2574, function2564):
    var1174 = function2753(b'a', WSMsgType.TEXT)
    function2564._feed_data(var1174[:1])
    function2564._feed_data(var1174[1:])
    var1658 = function2574._buffer[0]
    assert (var1658 == (WSMessage(WSMsgType.TEXT, 'a', ''), 1))

def function2462(function2574, function2564):
    var2814 = function2753(b'line1', WSMsgType.TEXT, is_fin=False)
    function2564._feed_data(var2814)
    var2357 = function2753(b'line2', WSMsgType.CONTINUATION)
    function2564._feed_data(var2357)
    var582 = function2574._buffer[0]
    assert (var582 == (WSMessage(WSMsgType.TEXT, 'line1line2', ''), 10))

def function2790(function2574, function2564):
    function2564.parse_frame = mock.Mock()
    function2564.parse_frame.return_value = [(0, WSMsgType.TEXT, b'line1'), (0, WSMsgType.PING, b''), (1, WSMsgType.CONTINUATION, b'line2')]
    var2761 = function2753(b'line1', WSMsgType.TEXT, is_fin=False)
    function2564._feed_data(var2761)
    var2430 = function2753(b'', WSMsgType.PING)
    function2564._feed_data(var2430)
    var4041 = function2753(b'line2', WSMsgType.CONTINUATION)
    function2564._feed_data(var4041)
    var2958 = function2574._buffer[0]
    assert (var2958 == (WSMessage(WSMsgType.PING, b'', ''), 0))
    var2958 = function2574._buffer[1]
    assert (var2958 == (WSMessage(WSMsgType.TEXT, 'line1line2', ''), 10))

def function1660(function2574, function2564):
    function2564.parse_frame = mock.Mock()
    function2564.parse_frame.return_value = [(0, WSMsgType.TEXT, b'line1'), (1, WSMsgType.TEXT, b'line2')]
    with pytest.raises(WebSocketError):
        function2564._feed_data(b'')

def function950(function2574, function2564):
    function2564.parse_frame = mock.Mock()
    function2564.parse_frame.return_value = [(0, WSMsgType.TEXT, b'line1'), (0, WSMsgType.CLOSE, function2245(1002, b'test', noheader=True)), (1, WSMsgType.CONTINUATION, b'line2')]
    function2564.feed_data(b'')
    var1440 = function2574._buffer[0]
    assert res, (WSMessage(WSMsgType.CLOSE, 1002, 'test'), 0)
    var1440 = function2574._buffer[1]
    assert (var1440 == (WSMessage(WSMsgType.TEXT, 'line1line2', ''), 10))

def function916(function2574, function2564):
    function2564.parse_frame = mock.Mock()
    function2564.parse_frame.return_value = [(0, WSMsgType.TEXT, b'line1'), (0, WSMsgType.CLOSE, function2245(1000, b'\xf4\x90\x80\x80', noheader=True)), (1, WSMsgType.CONTINUATION, b'line2')]
    with pytest.raises(WebSocketError) as var722:
        function2564._feed_data(b'')
    assert (var722.value.code == WSCloseCode.INVALID_TEXT)

def function257(function2574, function2564):
    function2564.parse_frame = mock.Mock()
    function2564.parse_frame.return_value = [(0, WSMsgType.TEXT, b'line1'), (0, WSMsgType.CLOSE, function2245(1, b'test', noheader=True)), (1, WSMsgType.CONTINUATION, b'line2')]
    with pytest.raises(WebSocketError) as var3011:
        function2564._feed_data(b'')
    assert (var3011.value.code == WSCloseCode.PROTOCOL_ERROR)

def function1469(function2574, function2564):
    function2564.parse_frame = mock.Mock()
    function2564.parse_frame.return_value = [(0, WSMsgType.TEXT, b'line1'), (0, WSMsgType.CLOSE, b'1'), (1, WSMsgType.CONTINUATION, b'line2')]
    with pytest.raises(WebSocketError) as var1202:
        function2564._feed_data(b'')
    assert var1202.value.code, WSCloseCode.PROTOCOL_ERROR

def function2305(function2574, function2564):
    function2564.parse_frame = mock.Mock()
    function2564.parse_frame.return_value = [(0, WSMsgType.TEXT, b'line1'), (0, WSMsgType.CLOSE, b''), (1, WSMsgType.CONTINUATION, b'line2')]
    function2564.feed_data(b'')
    var4580 = function2574._buffer[0]
    assert res, (WSMessage(WSMsgType.CLOSE, 0, ''), 0)
    var4580 = function2574._buffer[1]
    assert (var4580 == (WSMessage(WSMsgType.TEXT, 'line1line2', ''), 10))
var3579 = b'some very long data for masking by websocket'
var1366 = b'1234'
var2839 = b'B]^Q\x11DVFH\x12_[_U\x13PPFR\x14W]A\x14\\S@_X\\T\x14SK\x13CTP@[RYV@'

def function2283():
    var1042 = bytearray(var3579)
    http_websocket._websocket_mask_python(var1366, var1042)
    assert (var1042 == var2839)

@pytest.mark.skipif((not hasattr(http_websocket, '_websocket_mask_cython')), reason='Requires Cython')
def function648():
    var2712 = bytearray(var3579)
    http_websocket._websocket_mask_cython(var1366, var2712)
    assert (var2712 == var2839)

def function1404():
    var2800 = bytearray()
    http_websocket._websocket_mask_python(var1366, var2800)
    assert (var2800 == bytearray())

@pytest.mark.skipif((not hasattr(http_websocket, '_websocket_mask_cython')), reason='Requires Cython')
def function1900():
    var1706 = bytearray()
    http_websocket._websocket_mask_cython(var1366, var1706)
    assert (var1706 == bytearray())

def function1169():
    assert (aiohttp.WSMsgType.TEXT == aiohttp.WSMsgType.text)
    assert (aiohttp.WSMsgType.BINARY == aiohttp.WSMsgType.binary)
    assert (aiohttp.WSMsgType.PING == aiohttp.WSMsgType.ping)
    assert (aiohttp.WSMsgType.PONG == aiohttp.WSMsgType.pong)
    assert (aiohttp.WSMsgType.CLOSE == aiohttp.WSMsgType.close)
    assert (aiohttp.WSMsgType.CLOSED == aiohttp.WSMsgType.closed)
    assert (aiohttp.WSMsgType.ERROR == aiohttp.WSMsgType.error)