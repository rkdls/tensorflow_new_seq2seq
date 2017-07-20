'Tests for aiohttp/worker.py'
import asyncio
import pathlib
import socket
import ssl
from unittest import mock
import pytest
from aiohttp import helpers
from aiohttp.test_utils import make_mocked_coro
var2938 = pytest.importorskip('aiohttp.worker')
try:
    import uvloop
except ImportError:
    var2798 = None
var3763 = '%a "%{Referrer}i" %(h)s %(l)s %s'
var1739 = '%a "%{Referrer}i" %s'

def function2087(arg707):
    if (not hasattr(arg707, '__dict__')):
        pytest.skip('can not override loop attributes')


class Class2:

    def __init__(self):
        self.attribute229 = {}
        self.attribute1952 = 0
        self.attribute807 = mock.Mock()
        self.attribute807.graceful_timeout = 100
        try:
            self.attribute1410 = 'pid'
        except:
            pass


class Class394(Class2, var2938.GunicornWebWorker):
    pass
var1967 = [Class394]
if (var2798 is not None):


    class Class279(Class2, var2938.GunicornUVLoopWebWorker):
        pass
    var1967.append(Class279)

@pytest.fixture(params=var1967)
def function742(arg1630):
    var3284 = arg1630.param()
    var3284.notify = mock.Mock()
    return var3284

def function715(function742):
    with mock.patch('aiohttp.worker.asyncio') as var2336:
        try:
            function742.init_process()
        except TypeError:
            pass
        assert var2336.get_event_loop.return_value.close.called
        assert var2336.new_event_loop.called
        assert var2336.set_event_loop.called

def function1941(function742, arg916):
    function742.wsgi = mock.Mock()
    function742.loop = arg916
    function742._run = mock.Mock(wraps=asyncio.coroutine((lambda : None)))
    function742.wsgi.startup = make_mocked_coro(None)
    with pytest.raises(SystemExit):
        function742.run()
    assert function742._run.called
    function742.wsgi.startup.assert_called_once_with()
    assert arg916.is_closed()

def function2660(function742, arg822):
    function742.wsgi = (lambda arg2323, arg958: arg958())
    function742.loop = arg822
    function742._run = mock.Mock(wraps=asyncio.coroutine((lambda : None)))
    with pytest.raises(SystemExit):
        function742.run()
    assert function742._run.called
    assert arg822.is_closed()

def function400(function742):
    with mock.patch('aiohttp.worker.ensure_future') as var4603:
        function742.loop = mock.Mock()
        function742.handle_quit(object(), object())
        assert (not function742.alive)
        assert (function742.exit_code == 0)
        assert var4603.called
        function742.loop.call_later.asset_called_with(0.1, function742._notify_waiter_done)

def function749(function742):
    with mock.patch('aiohttp.worker.sys') as var3072:
        function742.handle_abort(object(), object())
        assert (not function742.alive)
        assert (function742.exit_code == 1)
        var3072.exit.assert_called_with(1)

def function945(function742):
    function742.loop = mock.Mock()
    function742._notify_waiter_done = mock.Mock()
    var319 = function742._wait_next_notify()
    assert (function742._notify_waiter == var319)
    function742.loop.call_later.assert_called_with(1.0, function742._notify_waiter_done)

def function2715(function742):
    function742._notify_waiter = None
    function742._notify_waiter_done()
    assert (function742._notify_waiter is None)
    var2226 = function742._notify_waiter = mock.Mock()
    function742._notify_waiter.done.return_value = False
    function742._notify_waiter_done()
    assert (function742._notify_waiter is None)
    var2226.set_result.assert_called_with(True)

def function2252(function742):
    function742.loop = mock.Mock()
    function742.init_signals()
    assert function742.loop.add_signal_handler.called

def function1669(function742, arg1750):
    function742.wsgi = mock.Mock()
    function742.loop = mock.Mock()
    function742.log = mock.Mock()
    function742.cfg = mock.Mock()
    function742.cfg.access_log_format = var1739
    arg1750.spy(function742, '_get_valid_log_format')
    var786 = function742.make_handler(function742.wsgi)
    assert (var786 is function742.wsgi.make_handler.return_value)
    assert function742._get_valid_log_format.called

def function2159(function742, arg2200):
    function742.wsgi = (lambda arg2132, arg2150: arg2150())
    function742.loop = mock.Mock()
    function742.loop.time.return_value = 1477797232
    function742.log = mock.Mock()
    function742.cfg = mock.Mock()
    function742.cfg.access_log_format = var1739
    arg2200.spy(function742, '_get_valid_log_format')
    with pytest.raises(RuntimeError):
        function742.make_handler(function742.wsgi)

@pytest.mark.parametrize('source,result', [(var1739, var1739), (Class394.DEFAULT_GUNICORN_LOG_FORMAT, Class394.DEFAULT_AIOHTTP_LOG_FORMAT)])
def function702(function742, arg1445, arg946):
    assert (arg946 == function742._get_valid_log_format(arg1445))

def function1928(function742):
    with pytest.raises(ValueError) as var2892:
        function742._get_valid_log_format(var3763)
    assert ('%(name)s' in str(var2892))

@asyncio.coroutine
def function2160(function742, arg909):
    function2087(arg909)
    function742.ppid = 1
    function742.alive = True
    function742.servers = {}
    var3061 = mock.Mock()
    var3061.cfg_addr = ('localhost', 8080)
    function742.sockets = [var3061]
    function742.wsgi = mock.Mock()
    function742.close = make_mocked_coro(None)
    function742.log = mock.Mock()
    function742.loop = arg909
    arg909.create_server = make_mocked_coro(var3061)
    function742.wsgi.make_handler.return_value.requests_count = 1
    function742.cfg.max_requests = 100
    function742.cfg.is_ssl = True
    function742.cfg.access_log_format = var1739
    var2287 = mock.Mock()
    with mock.patch('ssl.SSLContext', return_value=var2287):
        with mock.patch('aiohttp.worker.asyncio') as var2336:
            var2336.sleep = mock.Mock(wraps=asyncio.coroutine((lambda *a, **kw: None)))
            yield from function742._run()
    function742.notify.assert_called_with()
    function742.log.info.assert_called_with('Parent changed, shutting down: %s', function742)
    (var1003, var1719) = arg909.create_server.call_args
    assert ('ssl' in var1719)
    var1046 = var1719['ssl']
    assert (var1046 is var2287)

@pytest.mark.skipif((not hasattr(socket, 'AF_UNIX')), reason='UNIX sockets are not supported')
@asyncio.coroutine
def function15(function742, arg2079):
    function2087(arg2079)
    function742.ppid = 1
    function742.alive = True
    function742.servers = {}
    var2769 = mock.Mock()
    var2769.cfg_addr = '/path/to'
    var2769.family = socket.AF_UNIX
    function742.sockets = [var2769]
    function742.wsgi = mock.Mock()
    function742.close = make_mocked_coro(None)
    function742.log = mock.Mock()
    function742.loop = arg2079
    arg2079.create_unix_server = make_mocked_coro(var2769)
    function742.wsgi.make_handler.return_value.requests_count = 1
    function742.cfg.max_requests = 100
    function742.cfg.is_ssl = True
    function742.cfg.access_log_format = var1739
    var1449 = mock.Mock()
    with mock.patch('ssl.SSLContext', return_value=var1449):
        with mock.patch('aiohttp.worker.asyncio') as var2336:
            var2336.sleep = mock.Mock(wraps=asyncio.coroutine((lambda *a, **kw: None)))
            yield from function742._run()
    function742.notify.assert_called_with()
    function742.log.info.assert_called_with('Parent changed, shutting down: %s', function742)
    (var1674, var4497) = arg2079.create_unix_server.call_args
    assert ('ssl' in var4497)
    var258 = var4497['ssl']
    assert (var258 is var1449)

@asyncio.coroutine
def function519(function742, arg1005):
    with mock.patch('aiohttp.worker.os') as var2294:
        var2294.getpid.return_value = 1
        var2294.getppid.return_value = 1
        var3203 = mock.Mock()
        var3203.requests_count = 0
        function742.servers = {mock.Mock(): handler, }
        function742._wait_next_notify = mock.Mock()
        function742.ppid = 1
        function742.alive = True
        function742.sockets = []
        function742.log = mock.Mock()
        function742.loop = arg1005
        function742.cfg.is_ssl = False
        function742.cfg.max_redirects = 0
        function742.cfg.max_requests = 100
        with mock.patch('aiohttp.worker.asyncio.sleep') as var4629:
            var3668 = helpers.create_future(arg1005)
            var3668.set_exception(KeyboardInterrupt)
            var4629.return_value = var3668
            function742.close = make_mocked_coro(None)
            yield from function742._run()
        assert function742._wait_next_notify.called
        function742.close.assert_called_with()

@asyncio.coroutine
def function2260(function742, arg841):
    var608 = mock.Mock()
    var608.wait_closed = make_mocked_coro(None)
    var3709 = mock.Mock()
    function742.servers = {srv: handler, }
    function742.log = mock.Mock()
    function742.loop = arg841
    var3538 = function742.wsgi = mock.Mock()
    var3538.cleanup = make_mocked_coro(None)
    var3709.connections = [object()]
    var3709.shutdown.return_value = helpers.create_future(arg841)
    var3709.shutdown.return_value.set_result(1)
    var3538.shutdown.return_value = helpers.create_future(arg841)
    var3538.shutdown.return_value.set_result(None)
    yield from function742.close()
    var3538.shutdown.assert_called_with()
    var3538.cleanup.assert_called_with()
    var3709.shutdown.assert_called_with(timeout=95.0)
    var608.close.assert_called_with()
    assert (function742.servers is None)
    yield from function742.close()

@asyncio.coroutine
def function112(function742, arg1816):
    var281 = mock.Mock()
    var281.wait_closed = make_mocked_coro(None)
    var4231 = mock.Mock()
    function742.servers = {srv: handler, }
    function742.log = mock.Mock()
    function742.loop = arg1816
    function742.wsgi = (lambda arg2173, arg1699: arg1699())
    var4231.connections = [object()]
    var4231.shutdown.return_value = helpers.create_future(arg1816)
    var4231.shutdown.return_value.set_result(1)
    yield from function742.close()
    var4231.shutdown.assert_called_with(timeout=95.0)
    var281.close.assert_called_with()
    assert (function742.servers is None)
    yield from function742.close()

@asyncio.coroutine
def function2216(function742, arg38):
    function2087(arg38)
    function742.ppid = 1
    function742.alive = True
    function742.servers = {}
    var3075 = mock.Mock()
    var3075.cfg_addr = ('localhost', 8080)
    function742.sockets = [var3075]
    function742.wsgi = mock.Mock()
    function742.close = make_mocked_coro(None)
    function742.log = mock.Mock()
    function742.loop = arg38
    arg38.create_server = make_mocked_coro(var3075)
    function742.wsgi.make_handler.return_value.requests_count = 1
    function742.cfg.access_log_format = var1739
    function742.cfg.max_requests = 0
    function742.cfg.is_ssl = True
    var978 = mock.Mock()
    with mock.patch('ssl.SSLContext', return_value=var978):
        with mock.patch('aiohttp.worker.asyncio') as var2336:
            var2336.sleep = mock.Mock(wraps=asyncio.coroutine((lambda *a, **kw: None)))
            yield from function742._run()
    function742.notify.assert_called_with()
    function742.log.info.assert_called_with('Parent changed, shutting down: %s', function742)
    (var3761, var2989) = arg38.create_server.call_args
    assert ('ssl' in var2989)
    var221 = var2989['ssl']
    assert (var221 is var978)

@asyncio.coroutine
def function2256(function742, arg1345):
    function2087(arg1345)
    function742.ppid = 1
    function742.alive = True
    function742.servers = {}
    var4447 = mock.Mock()
    var4447.cfg_addr = ('localhost', 8080)
    function742.sockets = [var4447]
    function742.wsgi = mock.Mock()
    function742.close = make_mocked_coro(None)
    function742.log = mock.Mock()
    function742.loop = arg1345
    arg1345.create_server = make_mocked_coro(var4447)
    function742.wsgi.make_handler.return_value.requests_count = 15
    function742.cfg.access_log_format = var1739
    function742.cfg.max_requests = 10
    function742.cfg.is_ssl = True
    var194 = mock.Mock()
    with mock.patch('ssl.SSLContext', return_value=var194):
        with mock.patch('aiohttp.worker.asyncio') as var2336:
            var2336.sleep = mock.Mock(wraps=asyncio.coroutine((lambda *a, **kw: None)))
            yield from function742._run()
    function742.notify.assert_called_with()
    function742.log.info.assert_called_with('Max requests, shutting down: %s', function742)
    (var3190, var70) = arg1345.create_server.call_args
    assert ('ssl' in var70)
    var2461 = var70['ssl']
    assert (var2461 is var194)

def function1752(function742):
    var282 = pathlib.Path(__file__).parent
    function742.cfg.ssl_version = ssl.PROTOCOL_SSLv23
    function742.cfg.cert_reqs = ssl.CERT_OPTIONAL
    function742.cfg.certfile = str((var282 / 'sample.crt'))
    function742.cfg.keyfile = str((var282 / 'sample.key'))
    function742.cfg.ca_certs = None
    function742.cfg.ciphers = None
    var3581 = function742._create_ssl_context(function742.cfg)
    assert isinstance(var3581, ssl.SSLContext)