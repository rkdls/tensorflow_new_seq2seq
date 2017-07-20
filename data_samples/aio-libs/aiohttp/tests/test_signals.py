import asyncio
from unittest import mock
import pytest
from multidict import CIMultiDict
from aiohttp.signals import Signal
from aiohttp.test_utils import make_mocked_request
from aiohttp.web import Application, Response

@pytest.fixture
def function1121():
    return Application()

@pytest.fixture
def function2688():
    return Application(debug=True)

def function1846(function1121, arg465, arg1502, arg1821=CIMultiDict()):
    return make_mocked_request(arg465, arg1502, arg1821, app=function1121)

@asyncio.coroutine
def function666(function1121):
    var2024 = True
    function1121.on_response_prepare.append(var2024)
    with pytest.raises(TypeError):
        yield from function1121.on_response_prepare(None, None)

@asyncio.coroutine
def function105(function1121):
    var3164 = Signal(function1121)
    var96 = {'foo': 1, 'bar': 2, }
    var2570 = mock.Mock()

    @asyncio.coroutine
    def function382(**kwargs):
        var2570(None=var96)
    var3164.append(function382)
    yield from var3164.send(None=var96)
    var2570.assert_called_once_with(None=var96)

@asyncio.coroutine
def function590(function1121):
    var906 = Signal(function1121)
    var730 = {'a', 'b'}
    var1090 = {'foo': 1, 'bar': 2, }
    var852 = mock.Mock()

    @asyncio.coroutine
    def function382(*args, **kwargs):
        var852(*var730, None=var1090)
    var906.append(function382)
    yield from var906.send(*var730, None=var1090)
    var852.assert_called_once_with(*var730, None=var1090)

@asyncio.coroutine
def function1158(function1121):
    function382 = mock.Mock()

    @asyncio.coroutine
    def function2829(*args, **kwargs):
        function382(*args, None=kwargs)
    function1121.on_response_prepare.append(function2829)
    var732 = function1846(function1121, 'GET', '/')
    var3974 = Response(body=b'')
    yield from var3974.prepare(var732)
    function382.assert_called_once_with(var732, var3974)

@asyncio.coroutine
def function1362(function1121):
    var676 = Signal(function1121)
    var2961 = {'foo': 1, 'bar': 2, }
    function382 = mock.Mock()
    var676.append(function382)
    yield from var676.send(None=var2961)
    function382.assert_called_once_with(None=var2961)

@asyncio.coroutine
def function1281(function2688):
    assert function2688.debug, 'Should be True'
    var3888 = Signal(function2688)
    function382 = mock.Mock()
    var3839 = mock.Mock()
    var835 = mock.Mock()
    var3888.append(function382)
    function2688.on_pre_signal.append(var3839)
    function2688.on_post_signal.append(var835)
    yield from var3888.send(1, a=2)
    function382.assert_called_once_with(1, a=2)
    var3839.assert_called_once_with(1, 'aiohttp.signals:Signal', 1, a=2)
    var835.assert_called_once_with(1, 'aiohttp.signals:Signal', 1, a=2)

def function1396(function1121):
    var3642 = Signal(function1121)
    var1856 = mock.Mock()
    var3642.append(var1856)
    assert (var3642[0] is var1856)
    var259 = mock.Mock()
    var3642[0] = var259
    assert (var3642[0] is var259)

def function2805(function1121):
    var1658 = Signal(function1121)
    var921 = mock.Mock()
    var1658.append(var921)
    assert (len(var1658) == 1)
    del var1658[0]
    assert (len(var1658) == 0)

def function2183(function1121):
    var4737 = Signal(function1121)
    var805 = mock.Mock()
    var3494 = mock.Mock()
    var4737.append(var805)
    var4737.freeze()
    with pytest.raises(RuntimeError):
        var4737.append(var3494)
    assert (list(var4737) == [var805])

def function2559(function1121):
    var98 = Signal(function1121)
    var2142 = mock.Mock()
    var516 = mock.Mock()
    var98.append(var2142)
    var98.freeze()
    with pytest.raises(RuntimeError):
        var98[0] = var516
    assert (list(var98) == [var2142])

def function2296(function1121):
    var2457 = Signal(function1121)
    var2367 = mock.Mock()
    var2457.append(var2367)
    var2457.freeze()
    with pytest.raises(RuntimeError):
        del var2457[0]
    assert (list(var2457) == [var2367])