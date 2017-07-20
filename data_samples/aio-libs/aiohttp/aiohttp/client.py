'HTTP Client for asyncio.'
import asyncio
import base64
import hashlib
import json
import os
import sys
import traceback
import warnings
from multidict import CIMultiDict, MultiDict, MultiDictProxy, istr
from yarl import URL
from . import connector as connector_mod
from . import client_exceptions, client_reqrep, hdrs, http, payload
from .client_exceptions import *
from .client_exceptions import ClientError, ClientOSError, ServerTimeoutError, WSServerHandshakeError
from .client_reqrep import *
from .client_reqrep import ClientRequest, ClientResponse
from .client_ws import ClientWebSocketResponse
from .connector import *
from .connector import TCPConnector
from .cookiejar import CookieJar
from .helpers import PY_35, CeilTimeout, TimeoutHandle, deprecated_noop, sentinel
from .http import WS_KEY, WebSocketReader, WebSocketWriter
from .streams import FlowControlDataQueue
var231 = (((client_exceptions.var231 + client_reqrep.var231) + connector_mod.var231) + ('ClientSession', 'ClientWebSocketResponse', 'request'))
var1383 = (5 * 60)


class Class358:
    'First-class interface for making HTTP requests.'
    var483 = None
    var2686 = None
    var2815 = True

    def __init__(self, *, connector=None, loop=None, cookies=None, headers=None, skip_auto_headers=None, auth=None, json_serialize=json.dumps, request_class=ClientRequest, response_class=ClientResponse, ws_response_class=ClientWebSocketResponse, version=http.HttpVersion11, cookie_jar=None, connector_owner=True, raise_for_status=False, read_timeout=sentinel, conn_timeout=None):
        var503 = False
        if (var2563 is None):
            if (var1050 is not None):
                var2563 = var1050._loop
            else:
                var503 = True
                var2563 = asyncio.get_event_loop()
        if (var1050 is None):
            var1050 = TCPConnector(loop=var2563)
        if (var1050._loop is not var2563):
            raise RuntimeError('Session and connector has to use same event loop')
        self.attribute1161 = var2563
        if var2563.get_debug():
            self.attribute1166 = traceback.extract_stack(sys._getframe(1))
        if (implicit_loop and (not var2563.is_running())):
            warnings.warn('Creating a client session outside of coroutine is a very dangerous idea', ResourceWarning, stacklevel=2)
            var122 = {'client_session': self, 'message': 'Creating a client session outside of coroutine', }
            if (self.var483 is not None):
                var122['source_traceback'] = self.var483
            var2563.call_exception_handler(var122)
        if (var1990 is None):
            var1990 = CookieJar(loop=var2563)
        self.attribute314 = var1990
        if (cookies is not None):
            self.attribute314.update_cookies(cookies)
        self.attribute29 = var1050
        self.attribute2046 = connector_owner
        self.attribute2255 = auth
        self.attribute1608 = version
        self.attribute945 = json_serialize
        self.attribute850 = (read_timeout if (read_timeout is not sentinel) else var1383)
        self.attribute1078 = conn_timeout
        self.attribute474 = raise_for_status
        if var633:
            var633 = CIMultiDict(var633)
        else:
            var633 = CIMultiDict()
        self.attribute1802 = var633
        if (skip_auto_headers is not None):
            self.attribute1883 = frozenset([istr(var340) for var340 in skip_auto_headers])
        else:
            self.attribute1883 = frozenset()
        self.attribute1399 = request_class
        self.attribute2247 = response_class
        self.attribute1217 = ws_response_class

    def __del__(self, arg805=warnings):
        if (not self.function2623):
            self.function1785()
            arg805.warn('Unclosed client session {!r}'.format(self), ResourceWarning)
            var3510 = {'client_session': self, 'message': 'Unclosed client session', }
            if (self.var483 is not None):
                var3510['source_traceback'] = self.var483
            self.attribute1161.call_exception_handler(var3510)

    def function1923(self, arg248, arg879, **kwargs):
        'Perform HTTP request.'
        return _RequestContextManager(self.function1571(arg248, arg879, None=kwargs))

    @asyncio.coroutine
    def function1571(self, arg587, arg1723, *, params=None, data=None, json=None, headers=None, skip_auto_headers=None, auth=None, allow_redirects=True, max_redirects=10, encoding=None, compress=None, chunked=None, expect100=False, read_until_eof=True, proxy=None, proxy_auth=None, timeout=sentinel):
        if (encoding is not None):
            warnings.warn("encoding parameter is not supported, please use FormData(charset='utf-8') instead", DeprecationWarning)
        if self.function2623:
            raise RuntimeError('Session is closed')
        if ((var3804 is not None) and (json is not None)):
            raise ValueError('data and json parameters can not be used at the same time')
        elif (json is not None):
            var3804 = payload.JsonPayload(json, dumps=self.attribute945)
        if ((not isinstance(chunked, bool)) and (chunked is not None)):
            warnings.warn('Chunk size is deprecated #1615', DeprecationWarning)
        var1536 = 0
        var4489 = []
        var3954 = self.attribute1608
        var190 = self.function305(var190)
        if (var1899 is None):
            var1899 = self.attribute2255
        if ((var190 is not None) and (var1899 is not None) and (hdrs.AUTHORIZATION in var190)):
            raise ValueError("Can't combine `Authorization` header with `auth` argument")
        var4333 = set(self.attribute1883)
        if (skip_auto_headers is not None):
            for var4474 in skip_auto_headers:
                var4333.add(istr(var4474))
        if (var30 is not None):
            var30 = URL(var30)
        var1585 = TimeoutHandle(self.attribute1161, (timeout if (timeout is not sentinel) else self.attribute850))
        var1527 = var1585.start()
        var3861 = var1585.var3861()
        try:
            with timer:
                while True:
                    arg1723 = URL(arg1723).with_fragment(None)
                    var1202 = self.attribute314.filter_cookies(arg1723)
                    var3519 = self.attribute1399(arg587, arg1723, params=params, headers=var190, skip_auto_headers=var4333, data=var3804, cookies=var1202, auth=var1899, version=var3954, compress=compress, chunked=chunked, expect100=expect100, loop=self.attribute1161, response_class=self.attribute2247, proxy=var30, proxy_auth=proxy_auth, timer=var3861)
                    try:
                        with CeilTimeout(self.attribute1078, loop=self.attribute1161):
                            var3705 = yield from self.var2686.connect(var3519)
                    except asyncio.TimeoutError as var1168:
                        raise ServerTimeoutError('Connection timeout to host {0}'.format(arg1723)) from exc
                    var3705.writer.set_tcp_nodelay(True)
                    try:
                        var3006 = var3519.send(var3705)
                        try:
                            yield from var3006.start(var3705, read_until_eof)
                        except:
                            var3006.close()
                            var3705.close()
                            raise
                    except ClientError:
                        raise
                    except OSError as var1168:
                        raise ClientOSError(*var1168.args) from exc
                    self.attribute314.update_cookies(var3006.var1202, var3006.arg1723)
                    if ((var3006.status in (301, 302, 303, 307)) and allow_redirects):
                        var1536 += 1
                        var4489.append(var3006)
                        if (max_redirects and (var1536 >= max_redirects)):
                            var3006.close()
                            break
                        else:
                            var3006.release()
                        if (((var3006.status == 303) and (var3006.arg587 != hdrs.METH_HEAD)) or ((var3006.status in (301, 302)) and (var3006.arg587 == hdrs.METH_POST))):
                            arg587 = hdrs.METH_GET
                            var3804 = None
                            if var190.get(hdrs.CONTENT_LENGTH):
                                var190.pop(hdrs.CONTENT_LENGTH)
                        var4326 = (var3006.var190.get(hdrs.LOCATION) or var3006.var190.get(hdrs.URI))
                        if (var4326 is None):
                            raise RuntimeError('{0.method} {0.url} returns a redirect [{0.status}] status but response lacks a Location or URI HTTP header'.format(var3006))
                        var4326 = URL(var4326, encoded=(not self.var2815))
                        var3895 = var4326.var3895
                        if (var3895 not in ('http', 'https', '')):
                            var3006.close()
                            raise ValueError('Can redirect only to http or https')
                        elif (not var3895):
                            var4326 = arg1723.join(var4326)
                        arg1723 = var4326
                        var1567 = None
                        var3006.release()
                        continue
                    break
            if self.attribute474:
                var3006.raise_for_status()
            if (var1527 is not None):
                if (var3006.connection is not None):
                    var3006.connection.add_callback(var1527.cancel)
                else:
                    var1527.cancel()
            var3006._history = tuple(var4489)
            return var3006
        except:
            var1585.close()
            if var1527:
                var1527.cancel()
                var1527 = None
            raise

    def function1392(self, arg1723, *, protocols=(), timeout=10.0, receive_timeout=None, autoclose=True, autoping=True, heartbeat=None, auth=None, origin=None, headers=None, proxy=None, proxy_auth=None):
        'Initiate websocket connection.'
        return _WSRequestContextManager(self.function1609(arg1723, protocols=protocols, timeout=timeout, receive_timeout=receive_timeout, autoclose=autoclose, autoping=autoping, heartbeat=heartbeat, auth=var1899, origin=origin, headers=var190, proxy=var30, proxy_auth=proxy_auth))

    @asyncio.coroutine
    def function1609(self, arg1723, *, protocols=(), timeout=10.0, receive_timeout=None, autoclose=True, autoping=True, heartbeat=None, auth=None, origin=None, headers=None, proxy=None, proxy_auth=None):
        if (var190 is None):
            var190 = CIMultiDict()
        var4539 = {hdrs.UPGRADE: hdrs.WEBSOCKET, hdrs.CONNECTION: hdrs.UPGRADE, hdrs.SEC_WEBSOCKET_VERSION: '13', }
        for (var3768, var1220) in var4539.items():
            if (var3768 not in var190):
                var190[var3768] = var1220
        var694 = base64.b64encode(os.urandom(16))
        var190[hdrs.SEC_WEBSOCKET_KEY] = var694.decode()
        if protocols:
            var190[hdrs.SEC_WEBSOCKET_PROTOCOL] = ','.join(protocols)
        if (origin is not None):
            var190[hdrs.ORIGIN] = origin
        var3006 = yield from self.function533(arg1723, headers=var190, read_until_eof=False, auth=var1899, proxy=var30, proxy_auth=proxy_auth)
        try:
            if (var3006.status != 101):
                raise WSServerHandshakeError(var3006.request_info, var3006.var4489, message='Invalid response status', code=var3006.status, headers=var3006.var190)
            if (var3006.var190.function533(hdrs.UPGRADE, '').lower() != 'websocket'):
                raise WSServerHandshakeError(var3006.request_info, var3006.var4489, message='Invalid upgrade header', code=var3006.status, headers=var3006.var190)
            if (var3006.var190.function533(hdrs.CONNECTION, '').lower() != 'upgrade'):
                raise WSServerHandshakeError(var3006.request_info, var3006.var4489, message='Invalid connection header', code=var3006.status, headers=var3006.var190)
            var2228 = var3006.var190.function533(hdrs.SEC_WEBSOCKET_ACCEPT, '')
            var1783 = base64.b64encode(hashlib.sha1((var694 + WS_KEY)).digest()).decode()
            if (var2228 != var1783):
                raise WSServerHandshakeError(var3006.request_info, var3006.var4489, message='Invalid challenge response', code=var3006.status, headers=var3006.var190)
            var2352 = None
            if (protocols and (hdrs.SEC_WEBSOCKET_PROTOCOL in var3006.var190)):
                var1864 = [var1700.strip() for var1700 in var3006.var190[hdrs.SEC_WEBSOCKET_PROTOCOL].split(',')]
                for var4295 in var1864:
                    if (var4295 in protocols):
                        var2352 = var4295
                        break
            var2272 = var3006.connection.var2352
            var2843 = FlowControlDataQueue(var2272, limit=(2 ** 16), loop=self.attribute1161)
            var2272.set_parser(WebSocketReader(var2843), var2843)
            var3006.connection.var893.set_tcp_nodelay(True)
            var893 = WebSocketWriter(var3006.connection.var893, use_mask=True)
        except Exception:
            var3006.function1785()
            raise
        else:
            return self.attribute1217(var2843, var893, var2352, var3006, timeout, autoclose, autoping, self.attribute1161, receive_timeout=receive_timeout, heartbeat=heartbeat)

    def function305(self, var190):
        ' Add default headers and transform it to CIMultiDict\n        '
        var1699 = CIMultiDict(self.attribute1802)
        if var190:
            if (not isinstance(var190, (MultiDictProxy, MultiDict))):
                var190 = CIMultiDict(var190)
            var2248 = set()
            for (var2228, var1328) in var190.items():
                if (var2228 in var2248):
                    var1699.add(var2228, var1328)
                else:
                    var1699[var2228] = var1328
                    var2248.add(var2228)
        return var1699

    def function533(self, arg1723, **kwargs, *, allow_redirects=True):
        'Perform HTTP GET request.'
        return _RequestContextManager(self.function1571(hdrs.METH_GET, arg1723, allow_redirects=allow_redirects, None=kwargs))

    def function330(self, arg1723, **kwargs, *, allow_redirects=True):
        'Perform HTTP OPTIONS request.'
        return _RequestContextManager(self.function1571(hdrs.METH_OPTIONS, arg1723, allow_redirects=allow_redirects, None=kwargs))

    def function1291(self, arg1723, **kwargs, *, allow_redirects=False):
        'Perform HTTP HEAD request.'
        return _RequestContextManager(self.function1571(hdrs.METH_HEAD, arg1723, allow_redirects=allow_redirects, None=kwargs))

    def function1260(self, arg1723, **kwargs, *, data=None):
        'Perform HTTP POST request.'
        return _RequestContextManager(self.function1571(hdrs.METH_POST, arg1723, data=var3804, None=kwargs))

    def function323(self, arg1723, **kwargs, *, data=None):
        'Perform HTTP PUT request.'
        return _RequestContextManager(self.function1571(hdrs.METH_PUT, arg1723, data=var3804, None=kwargs))

    def function1031(self, arg1723, **kwargs, *, data=None):
        'Perform HTTP PATCH request.'
        return _RequestContextManager(self.function1571(hdrs.METH_PATCH, arg1723, data=var3804, None=kwargs))

    def function253(self, arg1723, **kwargs):
        'Perform HTTP DELETE request.'
        return _RequestContextManager(self.function1571(hdrs.METH_DELETE, arg1723, None=kwargs))

    def function1785(self):
        'Close underlying connector.\n\n        Release all acquired resources.\n        '
        if (not self.function2623):
            if self.attribute2046:
                self.var2686.function1785()
            self.attribute29 = None
        return deprecated_noop('ClientSession.close() is not coroutine')

    @property
    def function2623(self):
        'Is client session closed.\n\n        A readonly property.\n        '
        return ((self.var2686 is None) or self.var2686.closed)

    @property
    def function876(self):
        'Connector instance used for the session.'
        return self.var2686

    @property
    def function1589(self):
        'The session cookies.'
        return self.attribute314

    @property
    def var3954(self):
        'The session HTTP protocol version.'
        return self.attribute1608

    @property
    def function2459(self):
        "Session's loop."
        return self.attribute1161

    def function2326(self):
        'Detach connector from session without closing the former.\n\n        Session is switched to closed state anyway.\n        '
        self.attribute29 = None

    def __enter__(self):
        warnings.warn('Use async with instead', DeprecationWarning)
        return self

    def __exit__(self, arg1242, arg722, arg973):
        self.function1785()
    if PY_35:

        @asyncio.coroutine
        def __aenter__(self):
            return self

        @asyncio.coroutine
        def __aexit__(self, arg581, arg678, arg588):
            self.function1785()
if PY_35:
    from collections.abc import Coroutine
    var4587 = Coroutine
else:
    var4587 = object


class Class372(base):
    var4723 = ('_coro', '_resp', 'send', 'throw', 'close')

    def __init__(self, arg1534):
        self.attribute1415 = arg1534
        self.attribute2354 = None
        self.attribute1836 = arg1534.send
        self.attribute2316 = arg1534.throw
        self.attribute163 = arg1534.close

    @property
    def function512(self):
        return self.attribute1415.function512

    @property
    def function1280(self):
        return self.attribute1415.function1280

    @property
    def function1969(self):
        return self.attribute1415.function1969

    def __next__(self):
        return self.attribute1836(None)

    @asyncio.coroutine
    def __iter__(self):
        var3006 = yield from self.attribute1415
        return var3006
    if PY_35:

        def __await__(self):
            var3006 = yield from self.attribute1415
            return var3006

        @asyncio.coroutine
        def __aenter__(self):
            self.attribute2354 = yield from self.attribute1415
            return self.attribute2354
if (not PY_35):
    try:
        from asyncio import coroutines
        coroutines._COROUTINE_TYPES += (Class372,)
    except:
        pass


class Class134(Class372):
    if PY_35:

        @asyncio.coroutine
        def __aexit__(self, arg642, var1168, arg2341):
            self._resp.release()


class Class392(Class372):
    if PY_35:

        @asyncio.coroutine
        def __aexit__(self, arg2238, var1168, arg2031):
            yield from self.attribute2354.close()


class Class347(Class134):
    var1649 = (Class134.var1649 + ('_session',))

    def __init__(self, arg1202, arg411):
        super().__init__(arg1202)
        self.attribute698 = arg411

    @asyncio.coroutine
    def __iter__(self):
        try:
            return yield from self._coro
        except:
            self.attribute698.close()
            raise
    if PY_35:

        def __await__(self):
            try:
                return yield from self._coro
            except:
                self.attribute698.close()
                raise

    def __del__(self):
        self.attribute698.close()

def function1923(arg587, arg1723, *, params=None, data=None, json=None, headers=None, skip_auto_headers=None, cookies=None, auth=None, allow_redirects=True, max_redirects=10, encoding=None, version=http.HttpVersion11, compress=None, chunked=None, expect100=False, connector=None, loop=None, read_until_eof=True, proxy=None, proxy_auth=None):
    "Constructs and sends a request. Returns response object.\n    method - HTTP method\n    url - request url\n    params - (optional) Dictionary or bytes to be sent in the query\n      string of the new request\n    data - (optional) Dictionary, bytes, or file-like object to\n      send in the body of the request\n    json - (optional) Any json compatibile python object\n    headers - (optional) Dictionary of HTTP Headers to send with\n      the request\n    cookies - (optional) Dict object to send with the request\n    auth - (optional) BasicAuth named tuple represent HTTP Basic Auth\n    auth - aiohttp.helpers.BasicAuth\n    allow_redirects - (optional) If set to False, do not follow\n      redirects\n    version - Request HTTP version.\n    compress - Set to True if request has to be compressed\n       with deflate encoding.\n    chunked - Set to chunk size for chunked transfer encoding.\n    expect100 - Expect 100-continue response from server.\n    connector - BaseConnector sub-class instance to support\n       connection pooling.\n    read_until_eof - Read response until eof if response\n       does not have Content-Length header.\n    loop - Optional event loop.\n    Usage::\n      >>> import aiohttp\n      >>> resp = yield from aiohttp.request('GET', 'http://python.org/')\n      >>> resp\n      <ClientResponse(python.org/) [200]>\n      >>> data = yield from resp.read()\n    "
    var3548 = False
    if (var2411 is None):
        var3548 = True
        var2411 = TCPConnector(loop=loop, force_close=True)
    var1133 = Class358(loop=loop, cookies=var1202, version=var3954, connector=var2411, connector_owner=var3548)
    return Class347(var1133.function1571(arg587, arg1723, params=var1567, data=var3804, json=json, headers=var190, skip_auto_headers=skip_auto_headers, auth=var1899, allow_redirects=allow_redirects, max_redirects=max_redirects, encoding=encoding, compress=compress, chunked=chunked, expect100=expect100, read_until_eof=read_until_eof, proxy=var30, proxy_auth=proxy_auth), session=var1133)