'Tests for http/websocket.py'
import base64
import hashlib
import os
from unittest import mock
import multidict
import pytest
from yarl import URL
from aiohttp import http, http_exceptions
from aiohttp.http import WS_KEY, do_handshake

@pytest.fixture()
def function596():
    return mock.Mock()

@pytest.fixture()
def function1720():
    var810 = multidict.MultiDict()
    return http.RawRequestMessage('GET', '/path', (1, 0), var810, [], True, None, True, False, URL('/path'))

def function2240(arg1802=''):
    var1220 = base64.b64encode(os.urandom(16)).decode()
    var743 = [('Upgrade', 'websocket'), ('Connection', 'upgrade'), ('Sec-Websocket-Version', '13'), ('Sec-Websocket-Key', var1220)]
    if arg1802:
        var743 += [('Sec-Websocket-Protocol', arg1802)]
    return (var743, var1220)

def function1224(function1720, function596):
    with pytest.raises(http_exceptions.HttpProcessingError):
        do_handshake('POST', function1720.headers, function596)

def function2181(function1720, function596):
    with pytest.raises(http_exceptions.HttpBadRequest):
        do_handshake(function1720.method, function1720.headers, function596)

def function2321(function1720, function596):
    function1720.headers.extend([('Upgrade', 'websocket'), ('Connection', 'keep-alive')])
    with pytest.raises(http_exceptions.HttpBadRequest):
        do_handshake(function1720.method, function1720.headers, function596)

def function2348(function1720, function596):
    function1720.headers.extend([('Upgrade', 'websocket'), ('Connection', 'upgrade')])
    with pytest.raises(http_exceptions.HttpBadRequest):
        do_handshake(function1720.method, function1720.headers, function596)
    function1720.headers.extend([('Upgrade', 'websocket'), ('Connection', 'upgrade'), ('Sec-Websocket-Version', '1')])
    with pytest.raises(http_exceptions.HttpBadRequest):
        do_handshake(function1720.method, function1720.headers, function596)

def function2444(function1720, function596):
    function1720.headers.extend([('Upgrade', 'websocket'), ('Connection', 'upgrade'), ('Sec-Websocket-Version', '13')])
    with pytest.raises(http_exceptions.HttpBadRequest):
        do_handshake(function1720.method, function1720.headers, function596)
    function1720.headers.extend([('Upgrade', 'websocket'), ('Connection', 'upgrade'), ('Sec-Websocket-Version', '13'), ('Sec-Websocket-Key', '123')])
    with pytest.raises(http_exceptions.HttpBadRequest):
        do_handshake(function1720.method, function1720.headers, function596)
    var3913 = base64.b64encode(os.urandom(2))
    function1720.headers.extend([('Upgrade', 'websocket'), ('Connection', 'upgrade'), ('Sec-Websocket-Version', '13'), ('Sec-Websocket-Key', var3913.decode())])
    with pytest.raises(http_exceptions.HttpBadRequest):
        do_handshake(function1720.method, function1720.headers, function596)

def function466(function1720, function596):
    (var2670, var597) = function2240()
    function1720.var4463.extend(var2670)
    (var623, var4463, var3037, var603, var3161) = do_handshake(function1720.method, function1720.var4463, function596)
    assert (var623 == 101)
    assert (var3161 is None)
    var4577 = base64.b64encode(hashlib.sha1((var597.encode() + WS_KEY)).digest())
    var4463 = dict(var4463)
    assert (var4463['Sec-Websocket-Accept'] == var4577.decode())

def function2558(function1720, function596):
    'Tests if one protocol is returned by do_handshake'
    var1535 = 'chat'
    function1720.headers.extend(function2240(var1535)[0])
    (var793, var2315, var793, var793, var1343) = do_handshake(function1720.method, function1720.headers, function596, protocols=[var1535])
    assert (var1343 == var1535)
    var2315 = dict(var2315)
    assert (var2315['Sec-Websocket-Protocol'] == var1535)

def function975(function1720, function596):
    'Tests if the right protocol is selected given multiple'
    var68 = 'worse_proto'
    var688 = ['best', 'chat', 'worse_proto']
    var777 = 'worse_proto,chat'
    function1720.headers.extend(function2240(var777)[0])
    (var2450, var4433, var2450, var2450, var4712) = do_handshake(function1720.method, function1720.headers, function596, protocols=var688)
    assert (var4712 == var68)

def function2787(arg2248, function1720, function596):
    'Tests if a protocol mismatch handshake warns and returns None'
    var3592 = 'chat'
    function1720.headers.extend(function2240('test')[0])
    with arg2248('aiohttp.websocket') as var1878:
        (var424, var424, var424, var424, var789) = do_handshake(function1720.method, function1720.headers, function596, protocols=[var3592])
        assert (var789 is None)
    assert (var1878.records[(- 1)].msg == 'Client protocols %r don’t overlap server-known ones %r')