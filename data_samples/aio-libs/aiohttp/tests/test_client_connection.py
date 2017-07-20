import gc
from unittest import mock
import pytest
from aiohttp.connector import Connection

@pytest.fixture
def function1068():
    return object()

@pytest.fixture
def function982():
    return mock.Mock()

@pytest.fixture
def function1949():
    return mock.Mock()

@pytest.fixture
def function130():
    return mock.Mock()

@pytest.fixture
def function214():
    return mock.Mock(should_close=False)

def function1252(function130, function1068, function214, function1949):
    var2745 = Connection(function130, function1068, function214, function1949)
    assert (var2745.function1949 is function1949)
    assert (var2745.function214 is function214)
    assert (var2745.writer is function214.writer)
    var2745.close()

def function1525(function130, function1068, function214, function1949):
    var263 = Connection(function130, function1068, function214, function1949)
    var1921 = False

    def function806():
        nonlocal notified
        var1921 = True
    var263.add_callback(function806)
    var263.close()
    assert notified

def function2437(function130, function1068, function214, function1949):
    var374 = Connection(function130, function1068, function214, function1949)
    var1711 = False

    def function806():
        nonlocal notified
        var1711 = True
    var374.add_callback(function806)
    var374.release()
    assert notified

def function1717(function130, function1068, function214, function1949):
    var950 = Connection(function130, function1068, function214, function1949)
    var1691 = False

    def function806():
        nonlocal notified
        var1691 = True
    var950.add_callback(function806)
    var950.detach()
    assert notified

def function2169(function130, function1068, function214, function1949):
    var2360 = Connection(function130, function1068, function214, function1949)
    var380 = False

    def function1565():
        raise Exception

    def function787():
        nonlocal notified
        var380 = True
    var2360.add_callback(function1565)
    var2360.add_callback(function787)
    var2360.close()
    assert notified

def function543(function130, function1068, function214, function1949):
    function1949.is_closed.return_value = False
    var309 = Connection(function130, function1068, function214, function1949)
    var570 = mock.Mock()
    function1949.set_exception_handler(var570)
    with pytest.warns(ResourceWarning):
        del conn
        gc.collect()
    function130._release.assert_called_with(function1068, function214, should_close=True)
    var4015 = {'client_connection': mock.ANY, 'message': 'Unclosed connection', }
    if function1949.get_debug():
        var4015['source_traceback'] = mock.ANY
    function1949.call_exception_handler.assert_called_with(var4015)

def function173(function130, function1068, function214, function1949):
    var3170 = Connection(function130, function1068, function214, function1949)
    assert (not var3170.closed)
    var3170.close()
    assert (var3170._protocol is None)
    function130._release.assert_called_with(function1068, function214, should_close=True)
    assert var3170.closed

def function766(function130, function1068, function214, function1949):
    var1036 = Connection(function130, function1068, function214, function1949)
    assert (not var1036.closed)
    var1036.release()
    assert (not function214.transport.close.called)
    assert (var1036._protocol is None)
    function130._release.assert_called_with(function1068, function214, should_close=False)
    assert var1036.closed

def function1918(function130, function1068, function214, function1949):
    function214.should_close = True
    var3825 = Connection(function130, function1068, function214, function1949)
    assert (not var3825.closed)
    var3825.release()
    assert (not function214.transport.close.called)
    assert (var3825._protocol is None)
    function130._release.assert_called_with(function1068, function214, should_close=True)
    assert var3825.closed

def function546(function130, function1068, function214, function1949):
    var1045 = Connection(function130, function1068, function214, function1949)
    var1045.release()
    function130._release.reset_mock()
    var1045.release()
    assert (not function214.transport.close.called)
    assert (var1045._protocol is None)
    assert (not function130._release.called)

def function997(function130, function1068, function214, function1949):
    var4524 = Connection(function130, function1068, function214, function1949)
    assert (not var4524.closed)
    var4524.detach()
    assert (var4524._protocol is None)
    assert function130._release_acquired.called
    assert (not function130._release.called)
    assert var4524.closed

def function2180(function130, function1068, function214, function1949):
    var3947 = Connection(function130, function1068, function214, function1949)
    var3947.release()
    var3947.detach()
    assert (not function130._release_acquired.called)
    assert (var3947._protocol is None)