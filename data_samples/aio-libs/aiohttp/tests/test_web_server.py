import asyncio
from unittest import mock
import pytest
from aiohttp import client, web

@asyncio.coroutine
def function1433(arg2293, arg1967):

    @asyncio.coroutine
    def function1080(arg222):
        return web.Response(text=str(arg222.rel_url))
    var1387 = yield from arg2293(function1080)
    var2413 = yield from arg1967(var1387)
    var2530 = yield from var2413.get('/path/to')
    assert (var2530.status == 200)
    var3872 = yield from var2530.text()
    assert (var3872 == '/path/to')

@asyncio.coroutine
def function2541(arg1515, arg2324):
    var313 = RuntimeError('custom runtime error')

    @asyncio.coroutine
    def function1080(arg2069):
        raise exc
    var4166 = mock.Mock()
    var4480 = yield from arg1515(function1080, logger=var4166)
    var1052 = yield from arg2324(var4480)
    var2968 = yield from var1052.get('/path/to')
    assert (var2968.status == 500)
    var3839 = yield from var2968.text()
    assert ('<h1>500 Internal Server Error</h1>' in var3839)
    var4166.exception.assert_called_with('Error handling request', exc_info=var313)

@asyncio.coroutine
def function250(arg1606, arg1807):
    var4008 = asyncio.TimeoutError('error')

    @asyncio.coroutine
    def function1080(arg1886):
        raise exc
    var2389 = mock.Mock()
    var746 = yield from arg1606(function1080, logger=var2389)
    var782 = yield from arg1807(var746)
    var983 = yield from var782.get('/path/to')
    assert (var983.status == 504)
    yield from var983.text()
    var2389.debug.assert_called_with('Request handler timed out.')

@asyncio.coroutine
def function117(arg1731, arg1987):
    var1523 = None

    @asyncio.coroutine
    def function1080(arg1685):
        raise exc
    var2867 = mock.Mock()
    var2284 = yield from arg1731(function1080, logger=var2867)
    var2927 = yield from arg1987(var2284)
    for (var3648, var4362) in ((asyncio.CancelledError('error'), 'Ignored premature client disconnection'),):
        var1523 = var3648
        with pytest.raises(client.ServerDisconnectedError):
            yield from var2927.get('/path/to')
        var2867.debug.assert_called_with(var4362)

@asyncio.coroutine
def function80(arg56, arg1158):
    var220 = RuntimeError('custom runtime error')

    @asyncio.coroutine
    def function1080(arg2082):
        raise exc
    var3945 = mock.Mock()
    var2727 = yield from arg56(function1080, logger=var3945, debug=True)
    var4663 = yield from arg1158(var2727)
    var4185 = yield from var4663.get('/path/to')
    assert (var4185.status == 500)
    var3771 = yield from var4185.text()
    assert ('<h2>Traceback:</h2>' in var3771)
    var3945.exception.assert_called_with('Error handling request', exc_info=var220)

def function1032(arg1767):
    asyncio.set_event_loop(arg1767)

    @asyncio.coroutine
    def function1080(arg1332):
        return web.Response()
    var4228 = web.Server(function1080)
    assert (var4228._loop is arg1767)