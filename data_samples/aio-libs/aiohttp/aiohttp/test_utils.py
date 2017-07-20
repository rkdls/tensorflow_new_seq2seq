'Utilities shared by tests.'
import asyncio
import contextlib
import functools
import gc
import socket
import unittest
from abc import ABC, abstractmethod
from contextlib import contextmanager
from unittest import mock
from multidict import CIMultiDict
from yarl import URL
import aiohttp
from aiohttp.client import _RequestContextManager
from . import ClientSession, hdrs
from .helpers import PY_35, noop, sentinel
from .http import HttpVersion, RawRequestMessage
from .signals import Signal
from .web import Application, Request, Server, UrlMappingMatchInfo

def function1627(arg854):

    @asyncio.coroutine
    def function293():
        pass
    var3920 = asyncio.Task(function293(), loop=arg854)
    arg854.run_until_complete(var3920)

def function1872():
    'Return a port that is unused on the current host.'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as var3477:
        var3477.bind(('127.0.0.1', 0))
        return var3477.getsockname()[1]


class Class300(ABC):

    def __init__(self, **kwargs, *, scheme=sentinel, loop=None, host='127.0.0.1', skip_url_asserts=False):
        self.attribute1227 = loop
        self.attribute1000 = None
        self.attribute689 = None
        self.attribute992 = None
        self.attribute921 = None
        self.attribute1429 = host
        self.attribute1293 = False
        self.attribute1836 = scheme
        self.attribute1827 = skip_url_asserts

    @asyncio.coroutine
    def function1586(self, arg1837=None, **kwargs):
        if self.attribute689:
            return
        self.attribute1227 = arg1837
        self.attribute841 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.attribute841.bind((self.attribute1429, 0))
        self.attribute1000 = self.attribute841.getsockname()[1]
        self.attribute2083 = kwargs.pop('ssl', None)
        if (self.var4015 is sentinel):
            if self.attribute2083:
                var4015 = 'https'
            else:
                var4015 = 'http'
            self.attribute1836 = var4015
        self.attribute921 = URL('{}://{}:{}'.format(self.var4015, self.attribute1429, self.attribute1000))
        var3425 = yield from self.function1647(None=kwargs)
        self.attribute689 = yield from self.attribute1227.create_server(var3425, ssl=self.attribute2083, sock=self.attribute841)

    @abstractmethod
    @asyncio.coroutine
    def function1647(self, **kwargs):
        pass

    def function153(self, arg12):
        var2396 = URL(arg12)
        if (not self.attribute1827):
            assert (not var2396.is_absolute())
            return self.attribute921.join(var2396)
        else:
            return URL((str(self.attribute921) + arg12))

    @property
    def function2705(self):
        return (self.attribute689 is not None)

    @property
    def function926(self):
        return self.attribute1293

    @asyncio.coroutine
    def function192(self):
        'Close all fixtures created by the test client.\n\n        After that point, the TestClient is no longer usable.\n\n        This is an idempotent function: running close multiple times\n        will not have any additional effects.\n\n        close is also run when the object is garbage collected, and on\n        exit when used as a context manager.\n\n        '
        if (self.function2705 and (not self.function926)):
            self.attribute689.function192()
            yield from self.attribute689.wait_closed()
            self.attribute921 = None
            self.attribute1000 = None
            yield from self.function1501()
            self.attribute1293 = True

    @abstractmethod
    @asyncio.coroutine
    def function1501(self):
        pass

    def __enter__(self):
        self.attribute1227.run_until_complete(self.function1586(loop=self.attribute1227))
        return self

    def __exit__(self, arg755, arg191, arg491):
        self.attribute1227.run_until_complete(self.function192())
    if PY_35:

        @asyncio.coroutine
        def __aenter__(self):
            yield from self.function1586(loop=self.attribute1227)
            return self

        @asyncio.coroutine
        def __aexit__(self, arg2396, arg505, arg1474):
            yield from self.function192()


class Class46(Class300):

    def __init__(self, arg1796, **kwargs, *, scheme=sentinel, host='127.0.0.1'):
        self.attribute469 = arg1796
        super().__init__(scheme=scheme, host=host, None=kwargs)

    @asyncio.coroutine
    def function1911(self, **kwargs):
        self.attribute309 = self.attribute469.make_handler(loop=self.attribute1227, None=kwargs)
        yield from self.attribute469.startup()
        return self.attribute309

    @asyncio.coroutine
    def function236(self):
        yield from self.attribute469.shutdown()
        yield from self.attribute309.shutdown()
        yield from self.attribute469.cleanup()


class Class408(Class300):

    def __init__(self, arg2223, **kwargs, *, scheme=sentinel, host='127.0.0.1'):
        self.attribute1859 = arg2223
        super().__init__(scheme=scheme, host=host, None=kwargs)

    @asyncio.coroutine
    def function81(self, arg332=True, **kwargs):
        self.attribute480 = Server(self.attribute1859, loop=self.attribute1227, debug=True, None=kwargs)
        return self.attribute480

    @asyncio.coroutine
    def function1800(self):
        return


class Class40:
    '\n    A test client implementation.\n\n    To write functional tests for aiohttp based servers.\n\n    '

    def __init__(self, arg1180, **kwargs, *, scheme=sentinel, host=sentinel, cookie_jar=None, server_kwargs=None, loop=None):
        if isinstance(arg1180, Class300):
            if ((var1712 is not sentinel) or (var4109 is not sentinel)):
                raise ValueError('scheme and host are mutable exclusive with TestServer parameter')
            self.attribute2237 = arg1180
        elif isinstance(arg1180, Application):
            var1712 = ('http' if (var1712 is sentinel) else var1712)
            var4109 = ('127.0.0.1' if (var4109 is sentinel) else var4109)
            var3659 = (server_kwargs or {})
            self.attribute2237 = Class46(arg1180, scheme=var1712, host=var4109, None=var3659)
        else:
            raise TypeError('app_or_server should be either web.Application or TestServer instance')
        self.attribute177 = loop
        if (var2280 is None):
            var2280 = aiohttp.CookieJar(unsafe=True, loop=loop)
        self.attribute135 = ClientSession(loop=loop, cookie_jar=var2280, None=kwargs)
        self.attribute55 = False
        self.attribute2151 = []
        self.attribute192 = []

    @asyncio.coroutine
    def function491(self):
        yield from self.attribute2237.function491(loop=self.attribute177)

    @property
    def function2731(self):
        return self.attribute2237.function2731

    @property
    def function1435(self):
        return self.attribute2237.function1435

    @property
    def function1085(self):
        return self.attribute2237

    @property
    def function1719(self):
        'An internal aiohttp.ClientSession.\n\n        Unlike the methods on the TestClient, client session requests\n        do not automatically include the host in the url queried, and\n        will require an absolute path to the resource.\n\n        '
        return self.attribute135

    def function2283(self, arg2247):
        return self.attribute2237.function2283(arg2247)

    @asyncio.coroutine
    def function1071(self, arg1789, arg762, *args, **kwargs):
        'Routes a request to tested http server.\n\n        The interface is identical to asyncio.ClientSession.request,\n        except the loop kwarg is overridden by the instance used by the\n        test server.\n\n        '
        var715 = yield from self.attribute135.function1071(arg1789, self.function2283(arg762), *args, None=kwargs)
        self.attribute2151.append(var715)
        return var715

    def function2309(self, arg1798, *args, **kwargs):
        'Perform an HTTP GET request.'
        return _RequestContextManager(self.function1071(hdrs.METH_GET, arg1798, *args, None=kwargs))

    def function660(self, arg2216, *args, **kwargs):
        'Perform an HTTP POST request.'
        return _RequestContextManager(self.function1071(hdrs.METH_POST, arg2216, *args, None=kwargs))

    def function1346(self, arg1152, *args, **kwargs):
        'Perform an HTTP OPTIONS request.'
        return _RequestContextManager(self.function1071(hdrs.METH_OPTIONS, arg1152, *args, None=kwargs))

    def function634(self, arg1786, *args, **kwargs):
        'Perform an HTTP HEAD request.'
        return _RequestContextManager(self.function1071(hdrs.METH_HEAD, arg1786, *args, None=kwargs))

    def function1631(self, arg1105, *args, **kwargs):
        'Perform an HTTP PUT request.'
        return _RequestContextManager(self.function1071(hdrs.METH_PUT, arg1105, *args, None=kwargs))

    def function629(self, arg1071, *args, **kwargs):
        'Perform an HTTP PATCH request.'
        return _RequestContextManager(self.function1071(hdrs.METH_PATCH, arg1071, *args, None=kwargs))

    def function2794(self, arg1589, *args, **kwargs):
        'Perform an HTTP PATCH request.'
        return _RequestContextManager(self.function1071(hdrs.METH_DELETE, arg1589, *args, None=kwargs))

    @asyncio.coroutine
    def function2400(self, arg1208, *args, **kwargs):
        'Initiate websocket connection.\n\n        The api corresponds to aiohttp.ClientSession.ws_connect.\n\n        '
        var1367 = yield from self.attribute135.function2400(self.function2283(arg1208), *args, None=kwargs)
        self.attribute192.append(var1367)
        return var1367

    @asyncio.coroutine
    def function657(self):
        'Close all fixtures created by the test client.\n\n        After that point, the TestClient is no longer usable.\n\n        This is an idempotent function: running close multiple times\n        will not have any additional effects.\n\n        close is also run on exit when used as a(n) (asynchronous)\n        context manager.\n\n        '
        if (not self.attribute55):
            for var2770 in self.attribute2151:
                var2770.function657()
            for var2921 in self.attribute192:
                yield from var2921.function657()
            self.attribute135.function657()
            yield from self.attribute2237.function657()
            self.attribute55 = True

    def __enter__(self):
        self.attribute177.run_until_complete(self.function491())
        return self

    def __exit__(self, arg1989, arg1445, arg1459):
        self.attribute177.run_until_complete(self.function657())
    if PY_35:

        @asyncio.coroutine
        def __aenter__(self):
            yield from self.function491()
            return self

        @asyncio.coroutine
        def __aexit__(self, arg1653, arg420, arg1372):
            yield from self.function657()


class Class14(unittest.TestCase):
    "A base class to allow for unittest web applications using\n    aiohttp.\n\n    Provides the following:\n\n    * self.client (aiohttp.test_utils.TestClient): an aiohttp test client.\n    * self.loop (asyncio.BaseEventLoop): the event loop in which the\n        application and server are running.\n    * self.app (aiohttp.web.Application): the application returned by\n        self.get_application()\n\n    Note that the TestClient's methods are asynchronous: you have to\n    execute function on the test client using asynchronous methods.\n    "

    @asyncio.coroutine
    def function165(self):
        '\n        This method should be overridden\n        to return the aiohttp.web.Application\n        object to test.\n\n        '
        return self.function2784()

    def function2784(self):
        'Obsolete method used to constructing web application.\n\n        Use .get_application() coroutine instead\n\n        '
        pass

    def function2307(self):
        self.attribute1684 = function1563()
        self.attribute1852 = self.attribute1684.run_until_complete(self.function165())
        self.attribute1850 = self.attribute1684.run_until_complete(self.function1829(self.attribute1852))
        self.attribute1684.run_until_complete(self.attribute1850.start_server())

    def function64(self):
        self.attribute1684.run_until_complete(self.attribute1850.close())
        function2050(self.attribute1684)

    @asyncio.coroutine
    def function1829(self, arg639):
        'Return a TestClient instance.'
        return Class40(self.arg639, loop=self.attribute1684)

def function2272(arg1742, *args, **kwargs):
    'A decorator dedicated to use with asynchronous methods of an\n    AioHTTPTestCase.\n\n    Handles executing an asynchronous function, using\n    the self.loop of the AioHTTPTestCase.\n    '

    @functools.wraps(arg1742, *args, None=kwargs)
    def function1142(self):
        return self.loop.run_until_complete(arg1742(self, *args, None=kwargs))
    return function1142

@contextlib.contextmanager
def function275(arg290=asyncio.new_event_loop, arg2090=False):
    'A contextmanager that creates an event_loop, for test purposes.\n\n    Handles the creation and cleanup of a test loop.\n    '
    var505 = function1563(arg290)
    yield loop
    function2050(var505, fast=arg2090)

def function1563(arg2001=asyncio.new_event_loop):
    'Create and return an asyncio.BaseEventLoop\n    instance.\n\n    The caller should also call teardown_test_loop,\n    once they are done with the loop.\n    '
    var3144 = arg2001()
    asyncio.set_event_loop(None)
    return var3144

def function2050(arg1644, arg529=False):
    'Teardown and cleanup an event_loop created\n    by setup_test_loop.\n\n    '
    var1046 = arg1644.is_closed()
    if (not var1046):
        arg1644.call_soon(arg1644.stop)
        arg1644.run_forever()
        arg1644.close()
    if (not arg529):
        gc.collect()
    asyncio.set_event_loop(None)

def function1762():
    var4365 = mock.Mock()
    var4365._debug = False
    var4365.on_response_prepare = Signal(var4365)
    return var4365

def function2311(arg299=None):
    var3102 = mock.Mock()

    def function1441(arg315):
        if (arg315 == 'sslcontext'):
            return arg299
        else:
            return None
    var3102.function1441.side_effect = function1441
    return var3102

def function1044(arg1240, arg1308, arg1088=None, *, version=HttpVersion(1, 1), closing=False, app=None, writer=sentinel, payload_writer=sentinel, protocol=sentinel, transport=sentinel, payload=sentinel, sslcontext=None, secure_proxy_ssl_header=None, client_max_size=(1024 ** 2)):
    'Creates mocked web.Request testing purposes.\n\n    Useful in unit tests, when spinning full web server is overkill or\n    specific conditions and errors are hard to trigger.\n\n    '
    var1332 = mock.Mock()
    var3409 = mock.Mock()
    var3409.create_future.return_value = ()
    if (version < HttpVersion(1, 1)):
        var4501 = True
    if arg1088:
        arg1088 = CIMultiDict(arg1088)
        var4475 = tuple(((var4335.encode('utf-8'), var3338.encode('utf-8')) for (var4335, var3338) in arg1088.items()))
    else:
        arg1088 = CIMultiDict()
        var4475 = ()
    var727 = ('chunked' in arg1088.get(hdrs.TRANSFER_ENCODING, '').lower())
    var4131 = RawRequestMessage(arg1240, arg1308, version, arg1088, var4475, var4501, False, False, var727, URL(arg1308))
    if (var245 is None):
        var245 = function1762()
    if (var3691 is sentinel):
        var3691 = mock.Mock()
    if (var1888 is sentinel):
        var1888 = function2311(sslcontext)
    if (var1322 is sentinel):
        var1322 = mock.Mock()
        var1322.transport = var1888
    if (var3259 is sentinel):
        var3259 = mock.Mock()
        var3259.write_eof.side_effect = noop
        var3259.drain.side_effect = noop
    var3691.transport = var1888
    var3691.writer = var1322
    if (var1771 is sentinel):
        var1771 = mock.Mock()
    var2816 = mock.Mock()
    var2816.time.return_value = 12345
    var2816.strtime.return_value = 'Tue, 15 Nov 1994 08:12:31 GMT'

    @contextmanager
    def function2256(*args, **kw):
        yield
    var2816.timeout = mock.Mock()
    var2816.function2256.side_effect = function2256
    var1836 = Request(var4131, var1771, var3691, var3259, var2816, var1332, secure_proxy_ssl_header=secure_proxy_ssl_header, client_max_size=client_max_size)
    var4206 = UrlMappingMatchInfo({}, mock.Mock())
    var4206.add_app(var245)
    var1836._match_info = var4206
    return var1836

def function2716(arg1364=sentinel, arg1894=sentinel):
    'Creates a coroutine mock.'

    @asyncio.coroutine
    def function385(*args, **kwargs):
        if (arg1894 is not sentinel):
            raise raise_exception
        return arg1364
    return mock.Mock(wraps=function385)