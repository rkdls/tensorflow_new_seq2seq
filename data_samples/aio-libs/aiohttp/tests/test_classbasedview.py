import asyncio
from unittest import mock
import pytest
from aiohttp import web
from aiohttp.web_urldispatcher import View

def function2168():
    var2326 = mock.Mock()
    var1498 = View(var2326)
    assert (var1498.var2326 is var2326)

@asyncio.coroutine
def function904():
    var2702 = web.Response(text='OK')


    class Class256(View):

        @asyncio.coroutine
        def function1104(self):
            return var2702
    var2840 = mock.Mock()
    var2840._method = 'GET'
    var1203 = yield from Class256(var2840)
    assert (var2702 is var1203)

@asyncio.coroutine
def function2668():


    class Class245(View):

        @asyncio.coroutine
        def function2749(self):
            return web.Response(text='OK')
        var1217 = function2749
    var1924 = mock.Mock()
    var1924.method = 'UNKNOWN'
    with pytest.raises(web.HTTPMethodNotAllowed) as var3407:
        yield from Class245(var1924)
    assert (var3407.value.headers['allow'] == 'GET,OPTIONS')
    assert (var3407.value.status == 405)

@asyncio.coroutine
def function2123():


    class Class85(View):

        @asyncio.coroutine
        def function1248(self):
            return web.Response(text='OK')
        var4095 = var3276 = function1248
    var1865 = mock.Mock()
    var1865.method = 'POST'
    with pytest.raises(web.HTTPMethodNotAllowed) as var1509:
        yield from Class85(var1865)
    assert (var1509.value.headers['allow'] == 'DELETE,GET,OPTIONS')
    assert (var1509.value.status == 405)