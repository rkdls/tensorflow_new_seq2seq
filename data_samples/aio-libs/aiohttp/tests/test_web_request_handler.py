import asyncio
from unittest import mock
from aiohttp import web
from aiohttp.test_utils import make_mocked_coro, make_mocked_request

def function710(arg1269):
    var2986 = web.Application()
    var3646 = var2986.make_handler(loop=arg1269)
    var2957 = var3646()
    assert ('<RequestHandler none:none disconnected>' == repr(var2957))
    var2957.transport = object()
    var1649 = make_mocked_request('GET', '/index.html')
    var2957._request = var1649
    assert ('<RequestHandler none:none connected>' == repr(var2957))

def function2432(arg999):
    var310 = web.Application()
    var661 = var310.make_handler(loop=arg999)
    assert (var661.connections == [])
    var3260 = object()
    var1579 = object()
    var661.connection_made(var3260, var1579)
    assert (var661.connections == [var3260])
    var661.connection_lost(var3260, None)
    assert (var661.connections == [])

@asyncio.coroutine
def function2507(arg2116):
    var3615 = web.Application()
    var3599 = var3615.make_handler(loop=arg2116)
    var3438 = mock.Mock()
    var3438.shutdown = make_mocked_coro(mock.Mock())
    var3990 = mock.Mock()
    var3599.connection_made(var3438, var3990)
    yield from var3599.finish_connections()
    var3599.connection_lost(var3438, None)
    assert (var3599.connections == [])
    var3438.shutdown.assert_called_with(None)

@asyncio.coroutine
def function617(arg162):
    var3167 = web.Application()
    var2510 = var3167.make_handler(loop=arg162)
    var2195 = mock.Mock()
    var2195.shutdown = make_mocked_coro(mock.Mock())
    var3192 = mock.Mock()
    var2510.connection_made(var2195, var3192)
    yield from var2510.finish_connections(timeout=0.1)
    var2510.connection_lost(var2195, None)
    assert (var2510.connections == [])
    var2195.shutdown.assert_called_with(0.1)