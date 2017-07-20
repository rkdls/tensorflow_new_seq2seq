import asyncio
import mimetypes
import os
import pathlib
from . import hdrs
from .helpers import create_future
from .http_writer import PayloadWriter
from .log import server_logger
from .web_exceptions import HTTPNotModified, HTTPOk, HTTPPartialContent, HTTPRequestRangeNotSatisfiable
from .web_response import StreamResponse
var4127 = ('FileResponse',)
var1131 = bool(os.environ.get('AIOHTTP_NOSENDFILE'))


class Class219(PayloadWriter):

    def function851(self, arg462):
        self.attribute250 = arg462
        if (self.attribute205 is not None):
            (var33, self._drain_maiter) = (self._drain_maiter, None)
            if (not var33.done()):
                var33.set_result(None)

    def function508(self, arg2367):
        self.output_size += len(arg2367)
        self._buffer.append(arg2367)

    def function310(self, arg2195, arg1324, arg400, arg982, arg2241, arg502, arg1215):
        if arg1215:
            arg502.remove_writer(arg1324)
        if arg2195.cancelled():
            return
        try:
            var2551 = os.sendfile(arg1324, arg400, arg982, arg2241)
            if (var2551 == 0):
                var2551 = arg2241
        except (BlockingIOError, InterruptedError):
            var2551 = 0
        except Exception as var2481:
            arg2195.set_exception(var2481)
            return
        if (var2551 < arg2241):
            arg502.add_writer(arg1324, self.function310, arg2195, arg1324, arg400, (arg982 + var2551), (arg2241 - var2551), arg502, True)
        else:
            arg2195.set_result(None)

    @asyncio.coroutine
    def function2338(self, arg1291, arg2241):
        if (self.attribute250 is None):
            if (self.attribute205 is None):
                self.attribute205 = create_future(self.arg502)
            yield from self.attribute205
        var1030 = self.attribute250.get_extra_info('socket').dup()
        var1030.setblocking(False)
        arg1324 = var1030.fileno()
        arg400 = arg1291.fileno()
        arg982 = arg1291.tell()
        arg502 = self.arg502
        try:
            yield from arg502.sock_sendall(var1030, b''.join(self._buffer))
            arg2195 = create_future(arg502)
            self.function310(arg2195, arg1324, arg400, arg982, arg2241, arg502, False)
            yield from fut
        except:
            server_logger.debug('Socket error')
            self.attribute250.close()
        finally:
            var1030.close()
        self.output_size += arg2241
        self.attribute250 = None
        self._stream.release()

    @asyncio.coroutine
    def function807(self, arg2194=b''):
        pass


class Class136(StreamResponse):
    'A response object can be used to send files.'

    def __init__(self, arg10, arg1059=(256 * 1024), *args, **kwargs):
        super().__init__(*args, None=kwargs)
        if isinstance(arg10, str):
            arg10 = pathlib.Path(arg10)
        self.attribute1162 = arg10
        self.attribute345 = arg1059

    @asyncio.coroutine
    def function1413(self, arg628, arg1063, arg2241):
        var1538 = arg628.var1538
        if (var1538.get_extra_info('sslcontext') or (var1538.get_extra_info('socket') is None)):
            var1034 = yield from self.function512(arg628, arg1063, arg2241)
        else:
            var1034 = arg628._protocol.var1034.replace(arg628._writer, Class219)
            arg628._writer = var1034
            yield from super().function2721(arg628)
            yield from var1034.function2338(arg1063, arg2241)
        return var1034

    @asyncio.coroutine
    def function512(self, arg32, arg1356, arg2241):
        var3276 = yield from super().function2721(arg32)
        self.set_tcp_cork(True)
        try:
            var1258 = self.attribute345
            var76 = arg1356.read(var1258)
            while True:
                yield from var3276.write(var76)
                arg2241 = (arg2241 - var1258)
                if (arg2241 <= 0):
                    break
                var76 = arg1356.read(min(var1258, arg2241))
        finally:
            self.set_tcp_nodelay(True)
        yield from var3276.drain()
        return var3276
    if (hasattr(os, 'sendfile') and (not var1131)):
        var620 = function1413
    else:
        var620 = function512

    @asyncio.coroutine
    def function2721(self, arg296):
        var151 = self.attribute1162
        var4300 = False
        if ('gzip' in arg296.headers.get(hdrs.ACCEPT_ENCODING, '')):
            var530 = var151.with_name((var151.name + '.gz'))
            if var530.is_file():
                var151 = var530
                var4300 = True
        var2460 = var151.stat()
        var1186 = arg296.if_modified_since
        if ((var1186 is not None) and (var2460.st_mtime <= var1186.timestamp())):
            self.set_status(HTTPNotModified.status_code)
            return yield from super().function2721(arg296)
        (var4369, var4702) = mimetypes.guess_type(str(var151))
        if (not var4369):
            var4369 = 'application/octet-stream'
        var1746 = HTTPOk.status_code
        var2185 = var2460.st_size
        arg2241 = var2185
        try:
            var751 = arg296.http_range
            var2553 = var751.var2553
            var3528 = var751.stop
        except ValueError:
            self.set_status(HTTPRequestRangeNotSatisfiable.status_code)
            return yield from super().function2721(arg296)
        if ((var2553 is not None) or (var3528 is not None)):
            if ((var2553 is None) and (var3528 < 0)):
                var2553 = (var2185 + var3528)
                arg2241 = (- var3528)
            else:
                arg2241 = ((end or file_size) - var2553)
            if ((var2553 + arg2241) > var2185):
                arg2241 = (var2185 - var2553)
            if (var2553 >= var2185):
                arg2241 = 0
        if (arg2241 != var2185):
            var1746 = HTTPPartialContent.status_code
        self.set_status(var1746)
        self.attribute2112 = var4369
        if var4702:
            self.headers[hdrs.CONTENT_ENCODING] = var4702
        if var4300:
            self.headers[hdrs.VARY] = hdrs.ACCEPT_ENCODING
        self.attribute1592 = var2460.st_mtime
        self.attribute1894 = arg2241
        if arg2241:
            with var151.open('rb') as var919:
                if var2553:
                    var919.seek(var2553)
                return yield from self.var620(arg296, var919, arg2241)
        return yield from super().function2721(arg296)