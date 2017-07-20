import random
from unittest import mock
import pytest
from aiohttp.http import WebSocketWriter

@pytest.fixture
def function2289():
    return mock.Mock()

@pytest.fixture
def function1090(function2289):
    return WebSocketWriter(function2289, use_mask=False)

def function1903(function2289, function1090):
    function1090.pong()
    function2289.transport.write.assert_called_with(b'\x8a\x00')

def function706(function2289, function1090):
    function1090.ping()
    function2289.transport.write.assert_called_with(b'\x89\x00')

def function1792(function2289, function1090):
    function1090.send(b'text')
    function2289.transport.write.assert_called_with(b'\x81\x04text')

def function1985(function2289, function1090):
    function1090.send('binary', True)
    function2289.transport.write.assert_called_with(b'\x82\x06binary')

def function696(function2289, function1090):
    function1090.send((b'b' * 127), True)
    assert function2289.transport.write.call_args[0][0].startswith(b'\x82~\x00\x7fb')

def function871(function2289, function1090):
    function1090.send((b'b' * 65537), True)
    assert (function2289.transport.write.call_args_list[0][0][0] == b'\x82\x7f\x00\x00\x00\x00\x00\x01\x00\x01')
    assert (function2289.transport.write.call_args_list[1][0][0] == (b'b' * 65537))

def function244(function2289, function1090):
    function1090.close(1001, 'msg')
    function2289.transport.write.assert_called_with(b'\x88\x05\x03\xe9msg')
    function1090.close(1001, b'msg')
    function2289.transport.write.assert_called_with(b'\x88\x05\x03\xe9msg')
    function1090.close(1012, b'msg')
    function2289.transport.write.assert_called_with(b'\x88\x05\x03\xf4msg')

def function2772(function2289, function1090):
    function1090 = WebSocketWriter(function2289, use_mask=True, random=random.Random(123))
    function1090.send(b'text')
    function2289.transport.write.assert_called_with(b'\x81\x84\rg\xb3fy\x02\xcb\x12')