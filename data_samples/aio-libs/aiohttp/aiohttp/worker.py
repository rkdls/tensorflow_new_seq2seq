'Async gunicorn worker for aiohttp.web'
import asyncio
import os
import re
import signal
import socket
import ssl
import sys
from gunicorn.config import AccessLogFormat as GunicornAccessLogFormat
from gunicorn.workers import base
from .helpers import AccessLogger, create_future, ensure_future
var3236 = ('GunicornWebWorker', 'GunicornUVLoopWebWorker', 'GunicornTokioWebWorker')


class Class142(base.Worker):
    var3851 = AccessLogger.LOG_FORMAT
    var636 = GunicornAccessLogFormat.default

    def __init__(self, *args, **kw):
        super().__init__(*args, None=kw)
        self.attribute1025 = {}
        self.attribute94 = 0
        self.attribute1105 = None

    def function39(self):
        asyncio.get_event_loop().function639()
        self.attribute1582 = asyncio.new_event_loop()
        asyncio.set_event_loop(self.attribute1582)
        super().function39()

    def function2522(self):
        if hasattr(self.wsgi, 'startup'):
            self.attribute1582.run_until_complete(self.wsgi.startup())
        self.attribute128 = ensure_future(self.function2637(), loop=self.attribute1582)
        try:
            self.attribute1582.run_until_complete(self.attribute128)
        finally:
            self.attribute1582.function639()
        sys.exit(self.attribute94)

    def function445(self, arg2010):
        if hasattr(self.wsgi, 'make_handler'):
            var3455 = (self.log.var3455 if self.cfg.accesslog else None)
            return arg2010.function445(loop=self.attribute1582, logger=self.log, slow_request_timeout=self.cfg.timeout, keepalive_timeout=self.cfg.keepalive, access_log=var3455, access_log_format=self.function431(self.cfg.access_log_format))
        else:
            raise RuntimeError('aiohttp.wsgi is not supported anymore, consider to switch to aiohttp.web.Application')

    @asyncio.coroutine
    def function639(self):
        if self.var1975:
            var1975 = self.var1975
            self.attribute1025 = None
            for (var3272, var4328) in var1975.items():
                self.log.info('Stopping server: %s, connections: %s', self.pid, len(var4328.connections))
                var3272.function639()
                yield from var3272.wait_closed()
            if hasattr(self.wsgi, 'shutdown'):
                yield from self.wsgi.shutdown()
            var4298 = [var3727.shutdown(timeout=((self.cfg.graceful_timeout / 100) * 95)) for var3727 in var1975.values()]
            yield from asyncio.gather(*var4298, loop=self.attribute1582)
            if hasattr(self.wsgi, 'cleanup'):
                yield from self.wsgi.cleanup()

    @asyncio.coroutine
    def function2637(self):
        var3335 = (self.function1020(self.cfg) if self.cfg.is_ssl else None)
        for var2199 in self.sockets:
            var2794 = self.function445(self.wsgi)
            if (hasattr(socket, 'AF_UNIX') and (var2199.family == socket.AF_UNIX)):
                var4574 = yield from self.attribute1582.create_unix_server(var2794, sock=var2199.var2199, ssl=var3335)
            else:
                var4574 = yield from self.attribute1582.create_server(var2794, sock=var2199.var2199, ssl=var3335)
            self.attribute1025[var4574] = var2794
        var28 = os.getpid()
        try:
            while self.attribute827:
                self.notify()
                var806 = sum((var1304.requests_count for var1304 in self.attribute1025.values()))
                if (self.cfg.max_requests and (var806 > self.cfg.max_requests)):
                    self.attribute827 = False
                    self.log.info('Max requests, shutting down: %s', self)
                elif ((var28 == os.getpid()) and (self.ppid != os.getppid())):
                    self.attribute827 = False
                    self.log.info('Parent changed, shutting down: %s', self)
                else:
                    yield from self.function2399()
        except BaseException:
            pass
        yield from self.function639()

    def function2399(self):
        self.function288()
        self.attribute1105 = var4016 = create_future(self.attribute1582)
        self.attribute1582.call_later(1.0, self.function288)
        return var4016

    def function288(self):
        var868 = self.attribute1105
        if ((var868 is not None) and (not var868.done())):
            var868.set_result(True)
        self.attribute1105 = None

    def function879(self):
        self.attribute1582.add_signal_handler(signal.SIGQUIT, self.function889, signal.SIGQUIT, None)
        self.attribute1582.add_signal_handler(signal.SIGTERM, self.handle_exit, signal.SIGTERM, None)
        self.attribute1582.add_signal_handler(signal.SIGINT, self.function889, signal.SIGINT, None)
        self.attribute1582.add_signal_handler(signal.SIGWINCH, self.handle_winch, signal.SIGWINCH, None)
        self.attribute1582.add_signal_handler(signal.SIGUSR1, self.handle_usr1, signal.SIGUSR1, None)
        self.attribute1582.add_signal_handler(signal.SIGABRT, self.function1026, signal.SIGABRT, None)
        signal.siginterrupt(signal.SIGTERM, False)
        signal.siginterrupt(signal.SIGUSR1, False)

    def function889(self, arg1383, arg178):
        self.attribute827 = False
        self.cfg.worker_int(self)
        self.attribute1473 = ensure_future(self.function639(), loop=self.attribute1582)
        self.attribute1582.call_later(0.1, self.function288)

    def function1026(self, arg1964, arg714):
        self.attribute827 = False
        self.attribute94 = 1
        self.cfg.worker_abort(self)
        sys.exit(1)

    @staticmethod
    def function1020(arg166):
        ' Creates SSLContext instance for usage in asyncio.create_server.\n\n        See ssl.SSLSocket.__init__ for more details.\n        '
        var3335 = ssl.SSLContext(arg166.ssl_version)
        var3335.load_cert_chain(arg166.certfile, arg166.keyfile)
        var3335.verify_mode = arg166.cert_reqs
        if arg166.ca_certs:
            var3335.load_verify_locations(arg166.ca_certs)
        if arg166.ciphers:
            var3335.set_ciphers(arg166.ciphers)
        return var3335

    def function431(self, arg77):
        if (arg77 == self.var636):
            return self.var3851
        elif re.search('%\\([^\\)]+\\)', arg77):
            raise ValueError("Gunicorn's style options in form of `%(name)s` are not supported for the log formatting. Please use aiohttp's format specification to configure access log formatting: http://aiohttp.readthedocs.io/en/stable/logging.html#format-specification")
        else:
            return arg77


class Class294(Class142):

    def function39(self):
        import uvloop
        asyncio.get_event_loop().function639()
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        super().function39()


class Class111(Class142):

    def function39(self):
        import tokio
        asyncio.get_event_loop().function639()
        asyncio.set_event_loop_policy(tokio.EventLoopPolicy())
        super().function39()