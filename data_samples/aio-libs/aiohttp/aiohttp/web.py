import asyncio
import os
import signal
import socket
import stat
import sys
import warnings
from argparse import ArgumentParser
from collections import Iterable, MutableMapping
from importlib import import_module
from yarl import URL
from . import hdrs, web_exceptions, web_fileresponse, web_middlewares, web_protocol, web_request, web_response, web_server, web_urldispatcher, web_ws
from .abc import AbstractMatchInfo, AbstractRouter
from .helpers import FrozenList
from .http import HttpVersion
from .log import access_logger, web_logger
from .signals import FuncSignal, PostSignal, PreSignal, Signal
from .web_exceptions import *
from .web_fileresponse import *
from .web_middlewares import *
from .web_protocol import *
from .web_request import *
from .web_response import *
from .web_server import Server
from .web_urldispatcher import *
from .web_urldispatcher import PrefixedSubAppResource
from .web_ws import *
var4493 = (((((((((web_protocol.var4493 + web_fileresponse.var4493) + web_request.var4493) + web_response.var4493) + web_exceptions.var4493) + web_urldispatcher.var4493) + web_ws.var4493) + web_server.var4493) + web_middlewares.var4493) + ('Application', 'HttpVersion', 'MsgType'))


class Class433(MutableMapping):

    def __init__(self, *, logger=web_logger, router=None, middlewares=(), handler_args=None, client_max_size=(1024 ** 2), secure_proxy_ssl_header=None, loop=None, debug=...):
        if (var197 is None):
            var197 = web_urldispatcher.UrlDispatcher()
        assert isinstance(var197, AbstractRouter), router
        if (function2792 is not None):
            warnings.warn('loop argument is deprecated', ResourceWarning)
        if (secure_proxy_ssl_header is not None):
            warnings.warn('secure_proxy_ssl_header is deprecated', ResourceWarning)
        self.attribute1478 = function2786
        self.attribute239 = var197
        self.attribute991 = secure_proxy_ssl_header
        self.attribute921 = function2792
        self.attribute946 = handler_args
        self.attribute22 = logger
        self.attribute1074 = FrozenList(function1121)
        self.attribute512 = {}
        self.attribute708 = False
        self.attribute1714 = []
        self.attribute348 = PreSignal()
        self.attribute1275 = PostSignal()
        self.attribute400 = FuncSignal(self)
        self.attribute1140 = Signal(self)
        self.attribute1680 = Signal(self)
        self.attribute2319 = Signal(self)
        self.attribute1899 = Signal(self)
        self.attribute1139 = client_max_size

    def __eq__(self, arg1588):
        return (self is arg1588)

    def __getitem__(self, arg291):
        return self.attribute512[arg291]

    def function313(self):
        if self.attribute708:
            warnings.warn('Changing state of started or joined application is deprecated', DeprecationWarning, stacklevel=3)

    def __setitem__(self, arg514, arg1437):
        self.function313()
        self.attribute512[arg514] = arg1437

    def __delitem__(self, arg1516):
        self.function313()
        del self.attribute512[arg1516]

    def __len__(self):
        return len(self.attribute512)

    def __iter__(self):
        return iter(self.attribute512)

    @property
    def function2792(self):
        return self.attribute921

    def function2598(self, function2792):
        if (function2792 is None):
            function2792 = asyncio.get_event_loop()
        if ((self.attribute921 is not None) and (self.attribute921 is not function2792)):
            raise RuntimeError('web.Application instance initialized with different loop')
        self.attribute921 = function2792
        self.attribute400.send(self)
        if (self.attribute1478 is ...):
            self.attribute1478 = function2792.get_debug()
        for var1653 in self.attribute1714:
            var1653.function2598(function2792)

    @property
    def function2273(self):
        return self.attribute708

    def function1006(self):
        if self.attribute708:
            return
        self.attribute708 = True
        self.attribute1074 = tuple(reversed(self.attribute1074))
        self.attribute239.function1006()
        self.attribute400.function1006()
        self.attribute348.function1006()
        self.attribute1275.function1006()
        self.attribute1140.function1006()
        self.attribute1680.function1006()
        self.attribute2319.function1006()
        self.attribute1899.function1006()
        for var2824 in self.attribute1714:
            var2824.function1006()

    @property
    def function2786(self):
        return self.attribute1478

    def function2672(self, arg1473):

        def function406(arg1135):
            var1793 = getattr(arg1473, arg1135)

            @asyncio.coroutine
            def function1130(arg358):
                yield from var1793.send(arg1473)
            var570 = getattr(self, arg1135)
            var570.append(function1130)
        function406('on_startup')
        function406('on_shutdown')
        function406('on_cleanup')

    def function2553(self, arg868, arg1460):
        if self.function2273:
            raise RuntimeError('Cannot add sub application to frozen application')
        if arg1460.function2273:
            raise RuntimeError('Cannot add frozen application')
        if arg868.endswith('/'):
            arg868 = arg868[:(- 1)]
        if (arg868 in ('', '/')):
            raise ValueError('Prefix cannot be empty')
        var3205 = PrefixedSubAppResource(arg868, arg1460)
        self.function2386.register_resource(var3205)
        self.function2672(arg1460)
        self.attribute1714.append(arg1460)
        if (self.attribute921 is not None):
            arg1460.function2598(self.attribute921)
        return var3205

    @property
    def function116(self):
        return self.attribute400

    @property
    def function1500(self):
        return self.attribute1140

    @property
    def function2427(self):
        return self.attribute348

    @property
    def function308(self):
        return self.attribute1275

    @property
    def function1919(self):
        return self.attribute1680

    @property
    def function76(self):
        return self.attribute2319

    @property
    def function42(self):
        return self.attribute1899

    @property
    def function2386(self):
        return self.attribute239

    @property
    def function1121(self):
        return self.attribute1074

    def function1514(self, **kwargs, *, loop=None, secure_proxy_ssl_header=None):
        self.function2598(function2792)
        self.function1006()
        kwargs['debug'] = self.function2786
        if self.attribute946:
            for (var796, var208) in self.attribute946.items():
                kwargs[var796] = var208
        if secure_proxy_ssl_header:
            self.attribute991 = secure_proxy_ssl_header
        return Server(self.function2335, request_factory=self.function847, loop=self.function2792, None=kwargs)

    @asyncio.coroutine
    def function1512(self):
        'Causes on_startup signal\n\n        Should be called in the event loop along with the request handler.\n        '
        yield from self.function1919.send(self)

    @asyncio.coroutine
    def function2615(self):
        'Causes on_shutdown signal\n\n        Should be called before cleanup()\n        '
        yield from self.function76.send(self)

    @asyncio.coroutine
    def function2330(self):
        'Causes on_cleanup signal\n\n        Should be called after shutdown()\n        '
        yield from self.function42.send(self)

    def function847(self, arg251, arg1255, arg1030, arg9, arg2034, arg881=web_request.Request):
        return arg881(arg251, arg1255, arg1030, arg9, arg1030._time_service, arg2034, secure_proxy_ssl_header=self.attribute991, client_max_size=self.attribute1139)

    @asyncio.coroutine
    def function2335(self, arg770):
        var633 = yield from self.attribute239.resolve(arg770)
        assert isinstance(var633, AbstractMatchInfo), match_info
        var633.add_app(self)
        if __debug__:
            var633.function1006()
        var4281 = None
        arg770._match_info = var633
        var66 = arg770.headers.get(hdrs.EXPECT)
        if var66:
            var4281 = yield from var633.expect_handler(arg770)
            yield from arg770.writer.drain()
        if (var4281 is None):
            var2234 = var633.var2234
            for var601 in var633.apps[::(- 1)]:
                for var2573 in var601._middlewares:
                    var2234 = yield from var2573(var601, var2234)
            var4281 = yield from var2234(arg770)
        assert isinstance(var4281, web_response.StreamResponse), 'Handler {!r} should return response instance, got {!r} [middlewares {!r}]'.format(var633.var2234, type(var4281), [var2949 for var2949 in var4401.function1121 for var4401 in var633.apps])
        return var4281

    def __call__(self):
        'gunicorn compatibility'
        return self

    def __repr__(self):
        return '<Application 0x{:x}>'.format(id(self))


class Class381(SystemExit):
    var377 = 1

def function213():
    raise Class381()

def function189(arg246, *, host=None, port=None, path=None, sock=None, shutdown_timeout=60.0, ssl_context=None, print=print, backlog=128, access_log_format=None, access_log=access_logger, handle_signals=True, loop=None):
    'Run an app locally'
    var2079 = (var2229 is not None)
    if (var2229 is None):
        var2229 = asyncio.get_event_loop()
    var3101 = dict()
    if (access_log_format is not None):
        var3101['access_log_format'] = access_log_format
    var379 = arg246.make_handler(loop=var2229, access_log=access_log, None=var3101)
    var2229.run_until_complete(arg246.startup())
    var3982 = ('https' if ssl_context else 'http')
    var2646 = URL('{}://localhost'.format(var3982)).with_port(var1439)
    if (path is None):
        var1316 = ()
    elif (isinstance(path, (str, bytes, bytearray, memoryview)) or (not isinstance(path, Iterable))):
        var1316 = (path,)
    else:
        var1316 = path
    if (sock is None):
        var3662 = ()
    elif (not isinstance(sock, Iterable)):
        var3662 = (sock,)
    else:
        var3662 = sock
    if (host is None):
        if ((paths or socks) and (not var1439)):
            var2903 = ()
        else:
            var2903 = ('0.0.0.0',)
    elif (isinstance(host, (str, bytes, bytearray, memoryview)) or (not isinstance(host, Iterable))):
        var2903 = (host,)
    else:
        var2903 = host
    if (hosts and (var1439 is None)):
        var1439 = (8443 if ssl_context else 8080)
    var4306 = []
    var1037 = [str(var2646.with_host(var3177)) for var3177 in var2903]
    if var2903:
        var4659 = (var2903[0] if (len(var2903) == 1) else var2903)
        var4306.append(var2229.create_server(var379, var4659, var1439, ssl=ssl_context, backlog=backlog))
    for var3159 in var1316:
        var4306.append(var2229.create_unix_server(var379, var3159, ssl=ssl_context, backlog=backlog))
        var1037.append('{}://unix:{}:'.format(var3982, var3159))
        if (var3159[0] not in (0, '\x00')):
            try:
                if stat.S_ISSOCK(os.stat(var3159).st_mode):
                    os.remove(var3159)
            except FileNotFoundError:
                pass
    for var374 in var3662:
        var4306.append(var2229.create_server(var379, sock=var374, ssl=ssl_context, backlog=backlog))
        if (hasattr(socket, 'AF_UNIX') and (var374.family == socket.AF_UNIX)):
            var1037.append('{}://unix:{}:'.format(var3982, var374.getsockname()))
        else:
            (var4534, var1439) = var374.getsockname()
            var1037.append(str(var2646.with_host(var4534).with_port(var1439)))
    var3431 = var2229.run_until_complete(asyncio.gather(*var4306, loop=var2229))
    if handle_signals:
        try:
            var2229.add_signal_handler(signal.SIGINT, function213)
            var2229.add_signal_handler(signal.SIGTERM, function213)
        except NotImplementedError:
            pass
    try:
        print('======== Running on {} ========\n(Press CTRL+C to quit)'.format(', '.join(var1037)))
        var2229.run_forever()
    except (Class381, KeyboardInterrupt):
        pass
    finally:
        var4050 = []
        for var1213 in var3431:
            var1213.close()
            var4050.append(var1213.wait_closed())
        var2229.run_until_complete(asyncio.gather(*var4050, loop=var2229))
        var2229.run_until_complete(arg246.shutdown())
        var2229.run_until_complete(var379.shutdown(shutdown_timeout))
        var2229.run_until_complete(arg246.cleanup())
    if (not var2079):
        var2229.close()

def function2822(arg611):
    var2017 = ArgumentParser(description='aiohttp.web Application server', prog='aiohttp.web')
    var2017.add_argument('entry_func', help="Callable returning the `aiohttp.web.Application` instance to run. Should be specified in the 'module:function' syntax.", metavar='entry-func')
    var2017.add_argument('-H', '--hostname', help='TCP/IP hostname to serve on (default: %(default)r)', default='localhost')
    var2017.add_argument('-P', '--port', help='TCP/IP port to serve on (default: %(default)r)', type=int, default='8080')
    var2017.add_argument('-U', '--path', help='Unix file system path to serve on. Specifying a path will cause hostname and port arguments to be ignored.')
    (var3826, var4146) = var2017.parse_known_args(arg611)
    (var3730, var842, var1721) = var3826.entry_func.partition(':')
    if ((not var1721) or (not var3730)):
        var2017.error("'entry-func' not in 'module:function' syntax")
    if var3730.startswith('.'):
        var2017.error('relative module names not supported')
    try:
        var2621 = import_module(var3730)
    except ImportError as var3316:
        var2017.error(('unable to import %s: %s' % (var3730, var3316)))
    try:
        var4676 = getattr(var2621, var1721)
    except AttributeError:
        var2017.error(('module %r has no attribute %r' % (var3730, var1721)))
    if ((var3826.var3159 is not None) and (not hasattr(socket, 'AF_UNIX'))):
        var2017.error('file system paths not supported by your operating environment')
    arg246 = var4676(var4146)
    function189(arg246, host=var3826.hostname, port=var3826.var1439, path=var3826.var3159)
    var2017.exit(message='Stopped\n')
if (__name__ == '__main__'):
    function2822(sys.arg611[1:])