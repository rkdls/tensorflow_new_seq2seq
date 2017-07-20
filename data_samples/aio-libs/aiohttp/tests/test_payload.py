import asyncio
import pytest
from aiohttp import payload

@pytest.fixture
def function332():
    var1353 = payload.PAYLOAD_REGISTRY
    var839 = payload.PAYLOAD_REGISTRY = payload.PayloadRegistry()
    yield reg
    payload.PAYLOAD_REGISTRY = var1353


class Class409(payload.Payload):

    @asyncio.coroutine
    def function2042(self, arg1926):
        pass

def function1023(function332):


    class Class57:
        pass
    payload.register_payload(Class409, Class57)
    var674 = payload.get_payload(Class57())
    assert isinstance(var674, Class409)

def function651():
    var2614 = Class409('test', encoding='utf-8', filename='test.txt')
    assert (var2614._value == 'test')
    assert (var2614._encoding == 'utf-8')
    assert (var2614.size is None)
    assert (var2614.filename == 'test.txt')
    assert (var2614.content_type == 'text/plain')

def function1690():
    var2913 = Class409('test', headers={'content-type': 'application/json', })
    assert (var2913.content_type == 'application/json')

def function2834():
    var422 = payload.StringPayload('test')
    assert (var422.encoding == 'utf-8')
    assert (var422.content_type == 'text/plain; charset=utf-8')
    var422 = payload.StringPayload('test', encoding='koi8-r')
    assert (var422.encoding == 'koi8-r')
    assert (var422.content_type == 'text/plain; charset=koi8-r')
    var422 = payload.StringPayload('test', content_type='text/plain; charset=koi8-r')
    assert (var422.encoding == 'koi8-r')
    assert (var422.content_type == 'text/plain; charset=koi8-r')