import asyncio
import asyncio.streams
import http.server
import socket
import traceback
import warnings
from collections import deque
from contextlib import suppress
from html import escape as html_escape
from . import helpers, http
from .helpers import CeilTimeout, create_future, ensure_future
from .http import HttpProcessingError, HttpRequestParser, PayloadWriter, StreamWriter
from .log import access_logger, server_logger
from .streams import EMPTY_PAYLOAD
from .web_exceptions import HTTPException
from .web_request import BaseRequest
from .web_response import Response
var851 = ('RequestHandler', 'RequestPayloadError')
var3087 = http.RawRequestMessage('UNKNOWN', '/', http.HttpVersion10, {}, {}, True, False, False, False, http.URL('/'))
if hasattr(socket, 'SO_KEEPALIVE'):

    def function1343(arg9, arg673):
        var1362 = arg673.get_extra_info('socket')
        if (var1362 is not None):
            var1362.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
else:

    def function1343(arg9, arg673):
        pass


class Class223(Exception):
    'Payload parsing error.'


class Class417(asyncio.streams.FlowControlMixin, asyncio.Protocol):
    'HTTP protocol implementation.\n\n    RequestHandler handles incoming HTTP request. It reads request line,\n    request headers and request payload and calls handle_request() method.\n    By default it always returns with 404 response.\n\n    RequestHandler handles errors in incoming request, like bad\n    status line, bad headers or incomplete payload. If any error occurs,\n    connection gets closed.\n\n    :param time_service: Low resolution time service\n\n    :param keepalive_timeout: number of seconds before closing\n                              keep-alive connection\n    :type keepalive_timeout: int or None\n\n    :param bool tcp_keepalive: TCP keep-alive is on, default is on\n\n    :param bool debug: enable debug mode\n\n    :param logger: custom logger object\n    :type logger: aiohttp.log.server_logger\n\n    :param access_log: custom logging object\n    :type access_log: aiohttp.log.server_logger\n\n    :param str access_log_format: access log format string\n\n    :param loop: Optional event loop\n\n    :param int max_line_size: Optional maximum header line size\n\n    :param int max_field_size: Optional maximum header field size\n\n    :param int max_headers: Optional maximum header size\n\n    '
    var2119 = 0
    var4410 = False

    def __init__(self, arg1789, **kwargs, *, loop=None, keepalive_timeout=75, tcp_keepalive=True, slow_request_timeout=None, logger=server_logger, access_log=access_logger, access_log_format=helpers.AccessLogger.LOG_FORMAT, debug=False, max_line_size=8190, max_headers=32768, max_field_size=8190, lingering_time=10.0, max_concurrent_handlers=1):
        var3018 = kwargs.get('logger', var3018)
        if (slow_request_timeout is not None):
            warnings.warn('slow_request_timeout is deprecated', DeprecationWarning)
        super().__init__(loop=loop)
        self.attribute153 = (loop if (loop is not None) else asyncio.get_event_loop())
        self.attribute88 = arg1789
        self.attribute659 = arg1789.function1523
        self.attribute656 = arg1789.request_handler
        self.attribute341 = arg1789.request_factory
        self.attribute94 = function1343
        self.attribute807 = None
        self.attribute1259 = None
        self.attribute935 = function2423
        self.attribute1987 = float(lingering_time)
        self.attribute1007 = deque()
        self.attribute2391 = b''
        self.attribute2317 = deque()
        self.attribute1245 = None
        self.attribute1980 = []
        self.attribute1558 = max_concurrent_handlers
        self.attribute1939 = False
        self.attribute1517 = None
        self.attribute1010 = HttpRequestParser(self, loop, max_line_size=max_line_size, max_field_size=max_field_size, max_headers=max_headers, payload_exception=Class223)
        self.attribute933 = None
        self.attribute706 = False
        self.attribute316 = var3018
        self.attribute1438 = debug
        self.attribute2160 = access_log
        if access_log:
            self.attribute557 = helpers.AccessLogger(access_log, access_log_format)
        else:
            self.attribute557 = None
        self.attribute1548 = False
        self.attribute1238 = False

    def __repr__(self):
        self.attribute1959 = None
        if (self.attribute1959 is None):
            var3982 = 'none'
            var3883 = 'none'
        else:
            var3982 = 'none'
            var3883 = 'none'
        return '<{} {}:{} {}>'.format(self.__class__.__name__, var3982, var3883, ('connected' if (self.attribute933 is not None) else 'disconnected'))

    @property
    def function1523(self):
        return self.attribute659

    @property
    def function2423(self):
        return self.attribute935

    @asyncio.coroutine
    def function1380(self, arg1975=15.0):
        'Worker process is about to exit, we need cleanup everything and\n        stop accepting requests. It is especially important for keep-alive\n        connections.'
        self.attribute1238 = True
        if (self.attribute1259 is not None):
            self.attribute1259.cancel()
        for var239 in self.attribute2317:
            if (not var239.done()):
                var239.cancel()
        with suppress(asyncio.CancelledError, asyncio.TimeoutError):
            with CeilTimeout(arg1975, loop=self.attribute153):
                if (self.attribute1245 and (not self.attribute1245.done())):
                    yield from self.attribute1245
                while True:
                    var616 = None
                    for var4380 in self.attribute1980:
                        if (not var4380.done()):
                            var616 = var4380
                            break
                    if var616:
                        yield from h
                    else:
                        break
        for var4380 in self.attribute1980:
            if (not var4380.done()):
                var4380.cancel()
        if (self.attribute933 is not None):
            self.attribute933.close()
            self.attribute933 = None
        if self.attribute1980:
            self.attribute1980.clear()

    def function420(self, arg280):
        super().function420(arg280)
        self.attribute933 = arg280
        self.attribute1787 = StreamWriter(self, arg280, self.attribute153)
        if self.attribute94:
            function1343(self, arg280)
        self.attribute1787.set_tcp_nodelay(True)
        self.attribute88.function420(self, arg280)

    def function603(self, arg940):
        self.attribute88.function603(self, arg940)
        super().function603(arg940)
        self.attribute88 = None
        self.attribute1238 = True
        self.attribute341 = None
        self.attribute656 = None
        self.attribute1010 = None
        self.attribute933 = self.attribute1787 = None
        if (self.attribute1259 is not None):
            self.attribute1259.cancel()
        for var3536 in self.attribute1980:
            if (not var3536.done()):
                var3536.cancel()
        if (self.attribute1245 is not None):
            if (not self.attribute1245.done()):
                self.attribute1245.cancel()
        self.attribute1980 = ()
        if (self.attribute1517 is not None):
            self.attribute1517.feed_eof()
            self.attribute1517 = None

    def function2718(self, arg794):
        assert (self.attribute1517 is None)
        self.attribute1517 = arg794
        if self.attribute2391:
            self.attribute1517.feed_data(self.attribute2391)
            self.attribute2391 = b''

    def function1894(self):
        pass

    def function345(self, arg2072):
        if (self.attribute1238 or self.attribute1548):
            return
        if ((self.attribute1517 is None) and (not self.attribute1939)):
            try:
                (var1414, var2433, var4431) = self.attribute1010.feed_data(arg2072)
            except HttpProcessingError as var2954:
                self.function1601()
                self.attribute1245 = ensure_future(self.function1135(PayloadWriter(self.attribute1787, self.attribute153), 400, var2954, var2954.message), loop=self.attribute153)
            except Exception as var2954:
                self.function1601()
                self.attribute1245 = ensure_future(self.function1135(PayloadWriter(self.attribute1787, self.attribute153), 500, var2954), loop=self.attribute153)
            else:
                for (var630, var541) in var1414:
                    self.var2119 += 1
                    if self.attribute2317:
                        var4244 = self.attribute2317.popleft()
                        var4244.set_result((var630, var541))
                    elif self.attribute1558:
                        self.attribute1558 -= 1
                        arg2072 = []
                        var4716 = ensure_future(self.function246(var630, var541, arg2072), loop=self.attribute153)
                        arg2072.append(var4716)
                        self.attribute1980.append(var4716)
                    else:
                        self.attribute1007.append((var630, var541))
                self.attribute2207 = var2433
                if (upgraded and tail):
                    self.attribute2391 = var4431
        elif ((self.attribute1517 is None) and self.attribute1939 and data):
            self.attribute2391 += arg2072
        elif arg2072:
            (var921, var4431) = self.attribute1517.feed_data(arg2072)
            if var921:
                self.function1601()

    def function1765(self, arg2257):
        'Set keep-alive connection mode.\n\n        :param bool val: new state.\n        '
        self.attribute1679 = arg2257

    def function1601(self):
        'Stop accepting new pipelinig messages and close\n        connection when handlers done processing messages'
        self.attribute1548 = True
        for var3458 in self.attribute2317:
            if (not var3458.done()):
                var3458.cancel()

    def function2899(self, arg547=False):
        'Force close connection'
        self.attribute1238 = True
        for var931 in self.attribute2317:
            if (not var931.done()):
                var931.cancel()
        if (self.attribute933 is not None):
            if arg547:
                self.attribute933.write(b'\r\n')
            self.attribute933.function1601()
            self.attribute933 = None

    def function398(self, arg1315, arg882, arg2305, arg1910):
        if self.attribute557:
            self.attribute557.log(arg1315, arg882, arg2305, self.attribute933, arg1910)

    def function1693(self, *args, **kw):
        if self.attribute1438:
            self.attribute316.debug(*args, None=kw)

    def function2720(self, *args, **kw):
        self.attribute316.exception(*args, None=kw)

    def function100(self):
        if self.attribute1238:
            return
        var1988 = (self.attribute807 + self.attribute935)
        if (len(self.attribute1980) == len(self.attribute2317)):
            var4312 = self.attribute659.loop_time
            if ((var4312 + 1.0) > var1988):
                self.function2899(send_last_heartbeat=True)
                return
        self.attribute1259 = self.attribute153.call_at(var1988, self.function100)

    def function1559(self):
        if (not self.attribute706):
            try:
                self.attribute933.function1559()
            except (AttributeError, NotImplementedError, RuntimeError):
                pass
            self.attribute706 = True

    def function1843(self):
        if self.attribute706:
            try:
                self.attribute933.function1843()
            except (AttributeError, NotImplementedError, RuntimeError):
                pass
            self.attribute706 = False

    @asyncio.coroutine
    def function246(self, arg1776, arg2350, arg1330):
        'Start processing of incoming requests.\n\n        It reads request line, request headers and request payload, then\n        calls handle_request() method. Subclass has to override\n        handle_request(). start() handles various exceptions in request\n        or response handling. Connection is being closed always unless\n        keep_alive(True) specified.\n        '
        var2463 = self.attribute153
        arg1330 = arg1330[0]
        var338 = self.attribute88
        function2423 = self.attribute935
        while (not self.attribute1238):
            if self.attribute2160:
                var4375 = var2463.time()
            var338.requests_count += 1
            var3439 = PayloadWriter(self.var3439, var2463)
            var3580 = self.attribute341(arg1776, arg2350, self, var3439, arg1330)
            try:
                try:
                    var4407 = yield from self.attribute656(var3580)
                except HTTPException as var2954:
                    var4407 = var2954
                except asyncio.CancelledError:
                    self.function1693('Ignored premature client disconnection')
                    break
                except asyncio.TimeoutError:
                    self.function1693('Request handler timed out.')
                    var4407 = self.function1014(var3580, 504)
                except Exception as var2954:
                    var4407 = self.function1014(var3580, 500, var2954)
                yield from var4407.prepare(var3580)
                yield from var4407.write_eof()
                self.attribute1679 = var4407.function1765
                var3439.set_tcp_cork(False)
                var3439.set_tcp_nodelay(True)
                if self.attribute2160:
                    self.function398(arg1776, None, var4407, (var2463.time() - var4375))
                if (not arg2350.is_eof()):
                    var4298 = self.attribute1987
                    if ((not self.attribute1238) and lingering_time):
                        self.function1693('Start lingering close timer for %s sec.', var4298)
                        var4375 = var2463.time()
                        var1364 = (var4375 + var4298)
                        with suppress(asyncio.TimeoutError, asyncio.CancelledError):
                            while ((not arg2350.is_eof()) and (var4375 < var1364)):
                                var4018 = min((var1364 - var4375), var4298)
                                with CeilTimeout(var4018, loop=var2463):
                                    yield from arg2350.readany()
                                var4375 = var2463.time()
                    if ((not arg2350.is_eof()) and (not self.attribute1238)):
                        self.function1693('Uncompleted request.')
                        self.function1601()
            except RuntimeError as var2954:
                if self.attribute1438:
                    self.function2720('Unhandled runtime exception', exc_info=var2954)
                self.function2899()
            except Exception as var2954:
                self.function2720('Unhandled exception', exc_info=var2954)
                self.function2899()
            finally:
                if (self.attribute933 is None):
                    self.function1693('Ignored premature client disconnection.')
                elif (not self.attribute1238):
                    if self.attribute1007:
                        (arg1776, arg2350) = self.attribute1007.popleft()
                    elif (self.attribute1679 and (not self.attribute1548)):
                        if (function2423 is not None):
                            var4375 = self.attribute659.loop_time
                            self.attribute807 = var4375
                            if (self.attribute1259 is None):
                                self.attribute1259 = var2463.call_at((var4375 + function2423), self.function100)
                        var4122 = create_future(var2463)
                        self.attribute2317.append(var4122)
                        try:
                            (arg1776, arg2350) = yield from waiter
                        except asyncio.CancelledError:
                            break
                    else:
                        break
        if (not self.attribute1238):
            self.attribute1980.remove(arg1330)
            if (not self.attribute1980):
                if (self.attribute933 is not None):
                    self.attribute933.function1601()

    def function1014(self, var3580, arg1667=500, var2954=None, arg1776=None):
        'Handle errors.\n\n        Returns HTTP response with specific status code. Logs additional\n        information. It always closes current connection.'
        self.function2720('Error handling request', exc_info=var2954)
        if (arg1667 == 500):
            var1259 = '<h1>500 Internal Server Error</h1>'
            if self.attribute1438:
                try:
                    var3687 = traceback.format_exc()
                    var3687 = html_escape(var3687)
                    var1259 += '<br><h2>Traceback:</h2>\n<pre>'
                    var1259 += var3687
                    var1259 += '</pre>'
                except:
                    pass
            else:
                var1259 += 'Server got itself in trouble'
                var1259 = (('<html><head><title>500 Internal Server Error</title></head><body>' + var1259) + '</body></html>')
        else:
            var1259 = arg1776
        var4407 = Response(status=arg1667, text=var1259, content_type='text/html')
        var4407.function2899()
        if ((var3580.var3439.output_size > 0) or (self.attribute933 is None)):
            self.function2899()
        return var4407

    @asyncio.coroutine
    def function1135(self, var3439, arg1667, var2954=None, arg1776=None):
        var3580 = BaseRequest(var3087, EMPTY_PAYLOAD, self, var3439, self.attribute659, None)
        var4407 = self.function1014(var3580, arg1667, var2954, arg1776)
        yield from var4407.prepare(var3580)
        yield from var4407.write_eof()
        self.var3439.set_tcp_cork(False)
        self.var3439.set_tcp_nodelay(True)