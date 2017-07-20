import asyncio
import collections
import io
import json
import sys
import traceback
import warnings
from http.cookies import CookieError, Morsel
from urllib.request import getproxies
from multidict import CIMultiDict, CIMultiDictProxy, MultiDict, MultiDictProxy
from yarl import URL
from . import hdrs, helpers, http, payload
from .client_exceptions import ClientConnectionError, ClientOSError, ClientResponseError
from .formdata import FormData
from .helpers import PY_35, HeadersMixin, SimpleCookie, TimerNoop, noop
from .http import SERVER_SOFTWARE, HttpVersion10, HttpVersion11, PayloadWriter
from .log import client_logger
from .streams import FlowControlStreamReader
try:
    import cchardet as chardet
except ImportError:
    import chardet
var2468 = ('ClientRequest', 'ClientResponse')
var1191 = collections.namedtuple('RequestInfo', ('url', 'method', 'headers'))


class Class150:
    var3318 = {hdrs.METH_GET, hdrs.METH_HEAD, hdrs.METH_OPTIONS}
    var2166 = {hdrs.METH_PATCH, hdrs.METH_POST, hdrs.METH_PUT}
    var3357 = var3318.union(var2166).union({hdrs.METH_DELETE, hdrs.METH_TRACE})
    var3979 = {hdrs.ACCEPT: '*/*', hdrs.ACCEPT_ENCODING: 'gzip, deflate', }
    var1407 = b''
    var450 = None
    var3271 = None
    var3118 = None
    var3221 = None
    var4430 = None

    def __init__(self, arg1092, arg1935, *, params=None, headers=None, skip_auto_headers=frozenset(), data=None, cookies=None, auth=None, version=http.HttpVersion11, compress=None, chunked=None, expect100=False, loop=None, response_class=None, proxy=None, proxy_auth=None, proxy_from_env=False, timer=None):
        if (var1693 is None):
            var1693 = asyncio.get_event_loop()
        assert isinstance(arg1935, URL), url
        assert isinstance(proxy, (URL, type(None))), proxy
        if params:
            var1877 = MultiDict(arg1935.query)
            var330 = arg1935.with_query(params)
            var1877.extend(var330.query)
            arg1935 = arg1935.with_query(var1877)
        self.attribute1914 = arg1935.with_fragment(None)
        self.attribute683 = arg1935
        self.attribute669 = arg1092.upper()
        self.attribute126 = chunked
        self.attribute1089 = compress
        self.attribute1757 = var1693
        self.attribute1138 = None
        self.attribute333 = (response_class or ClientResponse)
        self.attribute2226 = (timer if (timer is not None) else TimerNoop())
        if var1693.get_debug():
            self.attribute2397 = traceback.extract_stack(sys._getframe(1))
        self.function2543(version)
        self.function2715(arg1935)
        self.function229(headers)
        self.function1475(skip_auto_headers)
        self.function355(cookies)
        self.function964(data)
        self.function2129(var450)
        self.function150(proxy, proxy_auth, proxy_from_env)
        self.function71(data, skip_auto_headers)
        self.function1156()
        self.function2358(expect100)

    @property
    def function1365(self):
        return self.attribute1914.function1365

    @property
    def function251(self):
        return self.attribute1914.function251

    @property
    def function1813(self):
        return var1191(self.attribute1914, self.attribute669, self.attribute1936)

    def function2715(self, arg1829):
        'Update destination host, port and connection type (ssl).'
        if (not arg1829.function1365):
            raise ValueError("Could not parse hostname from URL '{}'".format(arg1829))
        (var4435, var1335) = (arg1829.user, arg1829.var1335)
        if var4435:
            self.attribute1591 = helpers.BasicAuth(var4435, (password or ''))
        var2716 = arg1829.var2716
        self.attribute720 = (var2716 in ('https', 'wss'))

    def function2543(self, arg2302):
        "Convert request version to two elements tuple.\n\n        parser HTTP version '1.1' => (1, 1)\n        "
        if isinstance(arg2302, str):
            var4344 = [var1609.strip() for var1609 in arg2302.split('.', 1)]
            try:
                arg2302 = (int(var4344[0]), int(var4344[1]))
            except ValueError:
                raise ValueError('Can not parse http version number: {}'.format(arg2302)) from None
        self.attribute2303 = arg2302

    def function229(self, arg2260):
        'Update request headers.'
        self.attribute1936 = CIMultiDict()
        if arg2260:
            if isinstance(arg2260, (dict, MultiDictProxy, MultiDict)):
                arg2260 = arg2260.items()
            for (var3643, var1822) in arg2260:
                self.arg2260.add(var3643, var1822)

    def function1475(self, arg1591):
        self.attribute1742 = arg1591
        var547 = (set(self.attribute1936) | arg1591)
        for (var679, var1771) in self.var3979.items():
            if (var679 not in var547):
                self.attribute1936.add(var679, var1771)
        if (hdrs.HOST not in var547):
            var986 = self.attribute1914.raw_host
            if (not self.attribute1914.is_default_port()):
                var986 += (':' + str(self.attribute1914.function251))
            self.attribute1936[hdrs.HOST] = var986
        if (hdrs.USER_AGENT not in var547):
            self.attribute1936[hdrs.USER_AGENT] = SERVER_SOFTWARE

    def function355(self, arg709):
        'Update request cookies header.'
        if (not arg709):
            return
        var557 = SimpleCookie()
        if (hdrs.COOKIE in self.attribute1936):
            var557.load(self.attribute1936.get(hdrs.COOKIE, ''))
            del self.attribute1936[hdrs.COOKIE]
        for (var4295, var2855) in arg709.items():
            if isinstance(var2855, Morsel):
                var519 = var2855.get(var2855.key, Morsel())
                var519.set(var2855.key, var2855.var2855, var2855.coded_value)
                var557[var4295] = var519
            else:
                var557[var4295] = var2855
        self.attribute1936[hdrs.COOKIE] = var557.output(header='', sep=';').strip()

    def function964(self, arg152):
        'Set request content encoding.'
        if (not arg152):
            return
        var3819 = self.attribute1936.get(hdrs.CONTENT_ENCODING, '').lower()
        if var3819:
            if self.attribute1089:
                raise ValueError('compress can not be set if Content-Encoding header is set')
        elif self.attribute1089:
            if (not isinstance(self.attribute1089, str)):
                self.attribute1089 = 'deflate'
            self.attribute1936[hdrs.CONTENT_ENCODING] = self.attribute1089
            self.attribute126 = True

    def function1156(self):
        'Analyze transfer-encoding header.'
        var1594 = self.attribute1936.get(hdrs.TRANSFER_ENCODING, '').lower()
        if ('chunked' in var1594):
            if self.attribute126:
                raise ValueError('chunked can not be set if "Transfer-Encoding: chunked" header is set')
        elif self.attribute126:
            if (hdrs.CONTENT_LENGTH in self.attribute1936):
                raise ValueError('chunked can not be set if Content-Length header is set')
            self.attribute1936[hdrs.TRANSFER_ENCODING] = 'chunked'
        elif (hdrs.CONTENT_LENGTH not in self.attribute1936):
            self.attribute1936[hdrs.CONTENT_LENGTH] = str(len(self.var1407))

    def function2129(self, var450):
        'Set basic auth.'
        if (var450 is None):
            var450 = self.var450
        if (var450 is None):
            return
        if (not isinstance(var450, helpers.BasicAuth)):
            raise TypeError('BasicAuth() tuple is required instead')
        self.attribute1936[hdrs.AUTHORIZATION] = var450.encode()

    def function71(self, var1407, arg2305):
        if (not var1407):
            return
        if isinstance(var1407, FormData):
            var1407 = var1407()
        try:
            var1407 = payload.PAYLOAD_REGISTRY.get(var1407, disposition=None)
        except payload.LookupError:
            var1407 = FormData(var1407)()
        self.attribute25 = var1407
        if (not self.attribute126):
            if (hdrs.CONTENT_LENGTH not in self.attribute1936):
                var2818 = var1407.var2818
                if (var2818 is None):
                    self.attribute126 = True
                elif (hdrs.CONTENT_LENGTH not in self.attribute1936):
                    self.attribute1936[hdrs.CONTENT_LENGTH] = str(var2818)
        if ((hdrs.CONTENT_TYPE not in self.attribute1936) and (hdrs.CONTENT_TYPE not in arg2305)):
            self.attribute1936[hdrs.CONTENT_TYPE] = var1407.content_type
        if var1407.headers:
            for (var4636, var3781) in var1407.headers.items():
                if (var4636 not in self.attribute1936):
                    self.attribute1936[var4636] = var3781

    def function2358(self, arg144=False):
        if arg144:
            self.attribute1936[hdrs.EXPECT] = '100-continue'
        elif (self.attribute1936.get(hdrs.EXPECT, '').lower() == '100-continue'):
            arg144 = True
        if arg144:
            self.attribute143 = helpers.create_future(self.attribute1757)

    def function150(self, arg2369, arg455, arg1310):
        if (proxy_from_env and (not arg2369)):
            var3723 = getproxies().get(self.attribute683.scheme)
            arg2369 = (URL(var3723) if var3723 else None)
        if (proxy and (not (arg2369.scheme == 'http'))):
            raise ValueError('Only http proxies are supported')
        if (proxy_auth and (not isinstance(arg455, helpers.BasicAuth))):
            raise ValueError('proxy_auth must be None or BasicAuth() tuple')
        self.attribute1478 = arg2369
        self.attribute563 = arg455

    def function707(self):
        if (self.arg2302 < HttpVersion10):
            return False
        if (self.arg2302 == HttpVersion10):
            if (self.attribute1936.get(hdrs.CONNECTION) == 'keep-alive'):
                return True
            else:
                return False
        elif (self.attribute1936.get(hdrs.CONNECTION) == 'close'):
            return False
        return True

    @asyncio.coroutine
    def function189(self, arg1083, arg270):
        'Support coroutines that yields bytes objects.'
        if (self.var4430 is not None):
            yield from arg1083.drain()
            yield from self.attribute143
        try:
            if isinstance(self.var1407, payload.Payload):
                yield from self.var1407.write(arg1083)
            else:
                if isinstance(self.var1407, (bytes, bytearray)):
                    self.attribute25 = (self.var1407,)
                for var3335 in self.var1407:
                    arg1083.write(var3335)
            yield from arg1083.write_eof()
        except OSError as var3753:
            var520 = ClientOSError(var3753.errno, ('Can not write request body for %s' % self.attribute1914))
            var520.__context__ = var3753
            var520.__cause__ = var3753
            arg270.protocol.set_exception(var520)
        except Exception as var3753:
            arg270.protocol.set_exception(var3753)
        finally:
            self.attribute1667 = None

    def function516(self, arg270):
        if (self.attribute669 == hdrs.METH_CONNECT):
            var3263 = '{}:{}'.format(self.attribute1914.raw_host, self.attribute1914.function251)
        elif (self.attribute1478 and (not self.attribute720)):
            var3263 = str(self.attribute1914)
        else:
            var3263 = self.attribute1914.raw_path
            if self.attribute1914.raw_query_string:
                var3263 += ('?' + self.attribute1914.raw_query_string)
        arg1083 = PayloadWriter(arg270.arg1083, self.attribute1757)
        if self.attribute1089:
            arg1083.enable_compression(self.attribute1089)
        if (self.attribute126 is not None):
            arg1083.enable_chunking()
        if ((self.attribute669 in self.var2166) and (hdrs.CONTENT_TYPE not in self.arg2305) and (hdrs.CONTENT_TYPE not in self.attribute1936)):
            self.attribute1936[hdrs.CONTENT_TYPE] = 'application/octet-stream'
        var648 = self.attribute1936.get(hdrs.CONNECTION)
        if (not var648):
            if self.function707():
                if (self.arg2302 == HttpVersion10):
                    var648 = 'keep-alive'
            elif (self.arg2302 == HttpVersion11):
                var648 = 'close'
        if (var648 is not None):
            self.attribute1936[hdrs.CONNECTION] = var648
        var1203 = '{0} {1} HTTP/{2[0]}.{2[1]}\r\n'.format(self.attribute669, var3263, self.arg2302)
        arg1083.write_headers(var1203, self.attribute1936)
        self.attribute1667 = helpers.ensure_future(self.function189(arg1083, arg270), loop=self.attribute1757)
        self.attribute596 = self.var3118(self.attribute669, self.attribute683, writer=self.var3221, continue100=self.var4430, timer=self.attribute2226, request_info=self.function1813)
        self.var3271._post_init(self.attribute1757)
        return self.var3271

    @asyncio.coroutine
    def function1516(self):
        if (self.var3221 is not None):
            try:
                yield from self.attribute1667
            finally:
                self.attribute1667 = None

    def function1574(self):
        if (self.var3221 is not None):
            if (not self.attribute1757.is_closed()):
                self.var3221.cancel()
            self.attribute1667 = None


class Class382(HeadersMixin):
    arg2302 = None
    var381 = None
    var1470 = None
    var4688 = None
    var784 = None
    var1163 = None
    var3935 = None
    var840 = FlowControlStreamReader
    var3398 = None
    var1515 = None
    var1216 = None
    var3200 = True

    def __init__(self, arg1589, arg693, *, writer=None, continue100=None, timer=None, request_info=None):
        assert isinstance(arg693, URL)
        self.attribute531 = arg1589
        self.attribute1193 = None
        self.attribute1868 = SimpleCookie()
        self.attribute1087 = arg693
        self.attribute1860 = None
        self.attribute1299 = arg1083
        self.attribute2037 = continue100
        self.attribute1010 = True
        self.attribute97 = ()
        self.attribute587 = function1813
        self.attribute779 = (timer if (timer is not None) else TimerNoop())

    @property
    def function1118(self):
        return self.attribute1087

    @property
    def function838(self):
        warnings.warn('Deprecated, use .url #1654', DeprecationWarning, stacklevel=2)
        return self.attribute1087

    @property
    def function1365(self):
        return self.attribute1087.function1365

    @property
    def function442(self):
        return self.var784

    @property
    def function1813(self):
        return self.attribute587

    def function2753(self, arg1284):
        self.attribute2182 = arg1284
        if arg1284.get_debug():
            self.attribute622 = traceback.extract_stack(sys._getframe(1))

    def __del__(self, arg1125=warnings):
        if (self.var1216 is None):
            return
        if self.var3200:
            return
        if (self.var3935 is not None):
            self.var3935.release()
            self.function2139()
            if __debug__:
                if self.var1216.get_debug():
                    arg1125.warn('Unclosed response {!r}'.format(self), ResourceWarning)
                    var2436 = {'client_response': self, 'message': 'Unclosed response', }
                    if self.var1515:
                        var2436['source_traceback'] = self.var1515
                    self.var1216.call_exception_handler(var2436)

    def __repr__(self):
        var2070 = io.StringIO()
        var1223 = str(self.function1118)
        if self.var1470:
            var1819 = self.var1470.encode('ascii', 'backslashreplace').decode('ascii')
        else:
            var1819 = self.var1470
        print('<ClientResponse({}) [{} {}]>'.format(var1223, self.var381, var1819), file=var2070)
        print(self.var784, file=var2070)
        return var2070.getvalue()

    @property
    def function2018(self):
        return self.var3935

    @property
    def function2402(self):
        'A sequence of of responses, if redirects occurred.'
        return self.attribute97

    @asyncio.coroutine
    def function2395(self, function2018, arg2064=False):
        'Start response processing.'
        self.attribute1010 = False
        self.attribute189 = function2018.protocol
        self.attribute1422 = function2018
        function2018.protocol.set_response_params(timer=self.attribute779, skip_payload=(self.attribute531.lower() == 'head'), skip_status_codes=(204, 304), read_until_eof=arg2064)
        with self.attribute779:
            while True:
                try:
                    (var3955, var4549) = yield from self.attribute189.read()
                except http.HttpProcessingError as var94:
                    raise ClientResponseError(self.function1813, self.function2402, code=var94.code, message=var94.var3955, headers=var94.var784) from exc
                if ((var3955.code < 100) or (var3955.code > 199) or (var3955.code == 101)):
                    break
                if ((self.var4430 is not None) and (not self.var4430.done())):
                    self.var4430.set_result(True)
                    self.attribute2037 = None
        var4549.on_eof(self.function125)
        self.attribute2300 = var3955.arg2302
        self.attribute1541 = var3955.code
        self.attribute2352 = var3955.var1470
        self.attribute1193 = CIMultiDictProxy(var3955.var784)
        self.attribute270 = tuple(var3955.var1163)
        self.attribute394 = var4549
        for var3514 in self.var784.getall(hdrs.SET_COOKIE, ()):
            try:
                self.attribute1868.load(var3514)
            except CookieError as var94:
                client_logger.warning('Can not load response cookies: %s', var94)
        return self

    def function125(self):
        if self.var3200:
            return
        if (self.var3935 is not None):
            if ((self.var3935.protocol is not None) and self.var3935.protocol.upgraded):
                return
            self.var3935.function1996()
            self.attribute1422 = None
        self.attribute1010 = True
        self.function2139()

    @property
    def function2100(self):
        return self.var3200

    def function2315(self):
        if self.var3200:
            return
        self.attribute1010 = True
        if ((self.var1216 is None) or self.var1216.is_closed()):
            return
        if (self.var3935 is not None):
            self.var3935.function2315()
            self.attribute1422 = None
        self.function2139()
        self.function2123()

    def function1996(self):
        if self.var3200:
            return noop()
        self.attribute1010 = True
        if (self.var3935 is not None):
            self.var3935.function1996()
            self.attribute1422 = None
        self.function2139()
        self.function2123()
        return noop()

    def function2437(self):
        if (400 <= self.var381):
            raise ClientResponseError(self.function1813, self.function2402, code=self.var381, message=self.var1470, headers=self.var784)

    def function2139(self):
        if ((self.var3221 is not None) and (not self.var3221.done())):
            self.var3221.cancel()
        self.attribute1299 = None

    def function2123(self):
        var4688 = self.var4688
        if (content and (var4688.exception() is None) and (not var4688.is_eof())):
            var4688.set_exception(ClientConnectionError('Connection closed'))

    @asyncio.coroutine
    def function677(self):
        if (self.var3221 is not None):
            try:
                yield from self.attribute1299
            finally:
                self.attribute1299 = None
        self.function1996()

    @asyncio.coroutine
    def function2855(self):
        'Read response payload.'
        if (self.attribute1860 is None):
            try:
                self.attribute1860 = yield from self.var4688.function2855()
            except:
                self.function2315()
                raise
        return self.attribute1860

    def function1907(self):
        var4179 = self.var784.get(hdrs.CONTENT_TYPE, '').lower()
        (var3295, var3292, var1197, var2553) = helpers.parse_mimetype(var4179)
        var3007 = var2553.get('charset')
        if (not var3007):
            if ((var3295 == 'application') and (var3292 == 'json')):
                var3007 = 'utf-8'
            else:
                var3007 = chardet.detect(self.attribute1860)['encoding']
        if (not var3007):
            var3007 = 'utf-8'
        return var3007

    @asyncio.coroutine
    def function1039(self, arg162=None, arg2308='strict'):
        'Read response payload and decode.'
        if (self.attribute1860 is None):
            yield from self.function2855()
        if (arg162 is None):
            arg162 = self.function1907()
        return self.attribute1860.decode(arg162, errors=arg2308)

    @asyncio.coroutine
    def function148(self, *, encoding=None, loads=function148.loads, content_type='application/json'):
        'Read and decodes JSON response.'
        if (self.attribute1860 is None):
            yield from self.function2855()
        if content_type:
            var1691 = self.var784.get(hdrs.CONTENT_TYPE, '').lower()
            if (content_type not in var1691):
                raise ClientResponseError(self.function1813, self.function2402, message=('Attempt to decode JSON with unexpected mimetype: %s' % var1691), headers=self.var784)
        var1908 = self.attribute1860.strip()
        if (not var1908):
            return None
        if (var3957 is None):
            var3957 = self.function1907()
        return loads(var1908.decode(var3957))
    if PY_35:

        @asyncio.coroutine
        def __aenter__(self):
            return self

        @asyncio.coroutine
        def __aexit__(self, arg655, arg677, arg1727):
            self.function1996()