import asyncio
from unittest import mock
import pytest
from aiohttp import helpers, log, web
from aiohttp.abc import AbstractRouter

def function1008(arg1758):
    var4487 = web.Application(loop=arg1758)
    assert (arg1758 is var4487.arg1758)
    assert (var4487.logger is log.web_logger)

def function200():
    var3751 = web.Application()
    assert (var3751 is var3751())

def function1744():
    var3795 = web.Application()
    assert (var3795.loop is None)

def function2782(arg129):
    var3800 = web.Application()
    var3800._set_loop(arg129)
    assert (var3800.arg129 is arg129)

def function346(arg1889):
    asyncio.set_event_loop(arg1889)
    var4582 = web.Application()
    var4582._set_loop(None)
    assert (var4582.arg1889 is arg1889)

def function2399(arg1290):
    var1788 = web.Application()
    var1788._set_loop(arg1290)
    assert (var1788.arg1290 is arg1290)
    with pytest.raises(RuntimeError):
        var1788._set_loop(loop=object())

def function408(arg185):
    var3615 = web.Application()
    var2372 = mock.Mock()
    var3615.on_loop_available.append(var2372)
    var3615._set_loop(arg185)
    var2372.assert_called_with(var3615)

@pytest.mark.parametrize('debug', [True, False])
def function2647(arg955, arg1537, arg816):
    var2335 = web.Application(debug=arg816)
    var4701 = arg1537.patch('aiohttp.web.Server')
    var2335.make_handler(loop=arg955)
    var4701.assert_called_with(var2335._handle, request_factory=var2335._make_request, loop=arg955, debug=arg816)

def function51(arg765, arg749):
    var2128 = web.Application(handler_args={'test': True, })
    var1410 = arg749.patch('aiohttp.web.Server')
    var2128.make_handler(loop=arg765)
    var1410.assert_called_with(var2128._handle, request_factory=var2128._make_request, loop=arg765, debug=mock.ANY, test=True)

@asyncio.coroutine
def function1456():
    var3737 = web.Application()
    var2808 = mock.Mock()
    var4043 = mock.Mock()
    var3737.on_cleanup.append(var2808)
    var3737.on_cleanup.append(var4043)
    yield from var3737.cleanup()
    var2808.assert_called_once_with(var3737)
    var4043.assert_called_once_with(var3737)

@asyncio.coroutine
def function766(arg1004):
    var1046 = web.Application()
    var3547 = helpers.create_future(arg1004)

    @asyncio.coroutine
    def function395(var1046):
        yield from asyncio.sleep(0.001, loop=arg1004)
        var3547.set_result(123)
    var1046.on_cleanup.append(function395)
    yield from var1046.cleanup()
    assert var3547.done()
    assert (123 == var3547.result())

def function1741():
    var2616 = mock.Mock(spec=AbstractRouter)
    var4285 = web.Application(router=var2616)
    assert (var2616 is var4285.var2616)

def function571():
    var3086 = mock.Mock()
    var3011 = web.Application()
    var3011.logger = var3086
    assert (var3011.var3086 is var3086)

@asyncio.coroutine
def function2233():
    var2873 = web.Application()
    var748 = False

    @asyncio.coroutine
    def function1330(arg1768):
        nonlocal called
        assert (var2873 is arg1768)
        var748 = True
    var2873.function1330.append(function1330)
    yield from var2873.shutdown()
    assert called

@asyncio.coroutine
def function649(arg536):
    var1356 = web.Application()
    var1356._set_loop(arg536)
    var2581 = False
    var2641 = False
    var793 = False
    var1008 = False

    def function2624(arg172):
        nonlocal blocking_called
        assert (var1356 is arg172)
        var2581 = True

    @asyncio.coroutine
    def function552(arg1875):
        nonlocal long_running1_called
        assert (var1356 is arg1875)
        var2641 = True

    @asyncio.coroutine
    def function1116(arg434):
        nonlocal long_running2_called
        assert (var1356 is arg434)
        var793 = True

    @asyncio.coroutine
    def function1906(arg1990):
        nonlocal all_long_running_called
        assert (var1356 is arg1990)
        var1008 = True
        return yield from asyncio.gather(function552(arg1990), function1116(arg1990), loop=arg1990.arg536)
    var1356.on_startup.append(function2624)
    var1356.on_startup.append(function1906)
    yield from var1356.startup()
    assert blocking_called
    assert long_running1_called
    assert long_running2_called
    assert all_long_running_called

def function722():
    var2541 = web.Application()
    var2541['key'] = 'value'
    assert (len(var2541) == 1)
    del var2541['key']
    assert (len(var2541) == 0)

def function172():
    var4040 = web.Application()
    var23 = mock.Mock()
    var4040._subapps.append(var23)
    var4040.freeze()
    assert var23.freeze.called
    var4040.freeze()
    assert (len(var23.freeze.call_args_list) == 1)

def function2719():
    var4527 = web.Application()
    assert (var4527._secure_proxy_ssl_header is None)

def function2104(arg1211):
    var1569 = web.Application()
    var4513 = ('X-Forwarded-Proto', 'https')
    var1569.make_handler(secure_proxy_ssl_header=var4513, loop=arg1211)
    assert (var1569._secure_proxy_ssl_header is var4513)

def function1897(arg1848):
    var180 = ('X-Forwarded-Proto', 'https')
    var4032 = web.Application(secure_proxy_ssl_header=var180)
    assert (var4032._secure_proxy_ssl_header is var180)
    var4032.make_handler(loop=arg1848)
    assert (var4032._secure_proxy_ssl_header is var180)

def function2067():
    var640 = web.Application()
    var1435 = web.Application()
    assert (var640 == var640)
    assert (var640 != var1435)