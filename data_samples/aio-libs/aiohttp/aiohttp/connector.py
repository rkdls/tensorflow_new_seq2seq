import asyncio
import functools
import ssl
import sys
import traceback
import warnings
from collections import defaultdict
from hashlib import md5, sha1, sha256
from itertools import cycle, islice
from time import monotonic
from types import MappingProxyType
from . import hdrs, helpers
from .client_exceptions import ClientConnectorError, ClientHttpProxyError, ClientProxyConnectionError, ServerFingerprintMismatch
from .client_proto import ResponseHandler
from .client_reqrep import ClientRequest
from .helpers import SimpleCookie, is_ip_address, noop, sentinel
from .resolver import DefaultResolver
var2903 = ('BaseConnector', 'TCPConnector', 'UnixConnector')
var163 = {16: md5, 20: sha1, 32: sha256, }


class Class239:
    var4283 = None
    var3735 = None

    def __init__(self, arg405, arg1094, arg1234, arg2056):
        self.attribute1836 = arg1094
        self.attribute1977 = arg405
        self.attribute1774 = arg2056
        self.attribute58 = arg1234
        self.attribute964 = []
        if arg2056.get_debug():
            self.attribute1738 = traceback.extract_stack(sys._getframe(1))

    def __repr__(self):
        return 'Connection<{}>'.format(self.attribute1836)

    def __del__(self, arg964=warnings):
        if (self.attribute58 is not None):
            arg964.warn('Unclosed connection {!r}'.format(self), ResourceWarning)
            if self.attribute1774.is_closed():
                return
            self.attribute1977._release(self.attribute1836, self.attribute58, should_close=True)
            var1004 = {'client_connection': self, 'message': 'Unclosed connection', }
            if (self.var4283 is not None):
                var1004['source_traceback'] = self.var4283
            self.attribute1774.call_exception_handler(var1004)

    @property
    def function1106(self):
        return self.attribute1774

    @property
    def function2607(self):
        return self.attribute58.function2607

    @property
    def function2559(self):
        return self.attribute58

    @property
    def function446(self):
        return self.attribute58.function446

    def function2852(self, arg2303):
        if (arg2303 is not None):
            self.attribute964.append(arg2303)

    def function143(self):
        (var2696, self.attribute964) = (self.attribute964[:], [])
        for var1670 in var2696:
            try:
                var1670()
            except:
                pass

    def function1412(self):
        self.function143()
        if (self.attribute58 is not None):
            self.attribute1977._release(self.attribute1836, self.attribute58, should_close=True)
            self.attribute58 = None

    def function754(self):
        self.function143()
        if (self.attribute58 is not None):
            self.attribute1977._release(self.attribute1836, self.attribute58, should_close=self.attribute58.should_close)
            self.attribute58 = None

    def function1992(self):
        self.function143()
        if (self.attribute58 is not None):
            self.attribute1977._release_acquired(self.attribute58)
        self.attribute58 = None

    @property
    def function12(self):
        return ((self.attribute58 is None) or (not self.attribute58.is_connected()))


class Class262:
    ' placeholder for BaseConnector.connect function '

    def function307(self):
        pass


class Class224(object):
    'Base connector class.\n\n    keepalive_timeout - (optional) Keep-alive timeout.\n    force_close - Set to True to force close and do reconnect\n        after each request (and between redirects).\n    limit - The total number of simultaneous connections.\n    limit_per_host - Number of simultaneous connections to one host.\n    disable_cleanup_closed - Disable clean-up closed ssl transports.\n    loop - Optional event loop.\n    '
    var792 = True
    var4283 = None
    var3846 = 2.0

    def __init__(self, *, keepalive_timeout=sentinel, force_close=False, limit=100, limit_per_host=0, enable_cleanup_closed=False, loop=None):
        if function1319:
            if ((var4595 is not None) and (var4595 is not sentinel)):
                raise ValueError('keepalive_timeout cannot be set if force_close is True')
        elif (var4595 is sentinel):
            var4595 = 15.0
        if (function1106 is None):
            function1106 = asyncio.get_event_loop()
        self.attribute350 = False
        if function1106.get_debug():
            self.attribute1810 = traceback.extract_stack(sys._getframe(1))
        self.attribute871 = {}
        self.attribute317 = function1950
        self.attribute751 = function2510
        self.attribute1372 = set()
        self.attribute762 = defaultdict(set)
        self.attribute2064 = var4595
        self.attribute1545 = function1319
        self.attribute878 = defaultdict(list)
        self.attribute18 = function1106
        self.attribute651 = functools.partial(ResponseHandler, loop=function1106)
        self.attribute2304 = SimpleCookie()
        self.attribute922 = None
        self.attribute1427 = None
        self.attribute1446 = (not enable_cleanup_closed)
        self.attribute1541 = []
        self.function2642()

    def __del__(self, arg2226=warnings):
        if self.var792:
            return
        if (not self.attribute871):
            return
        var2392 = [repr(var354) for var354 in self.attribute871.values()]
        self.function627()
        arg2226.warn('Unclosed connector {!r}'.format(self), ResourceWarning)
        var1499 = {'connector': self, 'connections': conns, 'message': 'Unclosed connector', }
        if (self.var4283 is not None):
            var1499['source_traceback'] = self.var4283
        self.attribute18.call_exception_handler(var1499)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.function627()

    @property
    def function1319(self):
        'Ultimately close connection on releasing if True.'
        return self.attribute1545

    @property
    def function1950(self):
        'The total number for simultaneous connections.\n\n        If limit is 0 the connector has no limit.\n        The default limit size is 100.\n        '
        return self.attribute317

    @property
    def function2510(self):
        'The limit_per_host for simultaneous connections\n        to the same endpoint.\n\n        Endpoints are the same if they are have equal\n        (host, port, is_ssl) triple.\n\n        '
        return self.attribute751

    def function1533(self):
        'Cleanup unused transports.'
        if self.attribute922:
            self.attribute922.cancel()
        var2159 = self.attribute18.time()
        var4712 = self.attribute2064
        if self.attribute871:
            var1386 = {}
            var4324 = (var2159 - var4712)
            for (var109, var3461) in self.attribute871.items():
                var507 = []
                for (var1956, var1684) in var3461:
                    if var1956.is_connected():
                        if ((var1684 - var4324) < 0):
                            function2607 = var1956.function627()
                            if (var109[(- 1)] and (not self.attribute1446)):
                                self.attribute1541.append(function2607)
                        else:
                            var507.append((var1956, var1684))
                if var507:
                    var1386[var109] = var507
            self.attribute871 = var1386
        if self.attribute871:
            self.attribute922 = helpers.weakref_handle(self, '_cleanup', var4712, self.attribute18)

    def function2642(self):
        'Double confirmation for transport close.\n        Some broken ssl servers may leave socket open without proper close.\n        '
        if self.attribute1427:
            self.attribute1427.cancel()
        for function2607 in self.attribute1541:
            if (function2607 is not None):
                function2607.abort()
        self.attribute1541 = []
        if (not self.attribute1446):
            self.attribute1427 = helpers.weakref_handle(self, '_cleanup_closed', self.var3846, self.attribute18)

    def function627(self):
        'Close all opened transports.'
        if self.var792:
            return
        self.attribute350 = True
        try:
            if self.attribute18.is_closed():
                return noop()
            if self.attribute922:
                self.attribute922.cancel()
            if self.attribute1427:
                self.attribute1427.cancel()
            for var3996 in self.attribute871.values():
                for (var2250, var3034) in var3996:
                    var2250.function627()
            for var701 in self.attribute1372:
                var701.function627()
            for function2607 in self.attribute1541:
                if (function2607 is not None):
                    function2607.abort()
        finally:
            self.attribute871.clear()
            self.attribute1372.clear()
            self.attribute878.clear()
            self.attribute922 = None
            self.attribute1541.clear()
            self.attribute1427 = None

    @property
    def function1473(self):
        'Is connector closed.\n\n        A readonly property.\n        '
        return self.var792

    @asyncio.coroutine
    def function1219(self, arg805):
        'Get from pool or create new connection.'
        var3619 = (arg805.host, arg805.port, arg805.ssl)
        if self.attribute317:
            var3311 = ((self.attribute317 - len(self.attribute878)) - len(self.attribute1372))
            if (self.attribute751 and (var3311 > 0) and (var3619 in self.attribute762)):
                var3311 = (self.attribute751 - len(self.attribute762.get(var3619)))
        elif (self.attribute751 and (var3619 in self.attribute762)):
            var3311 = (self.attribute751 - len(self.attribute762.get(var3619)))
        else:
            var3311 = 1
        if (var3311 <= 0):
            var2563 = helpers.create_future(self.attribute18)
            var928 = self.attribute878[var3619]
            var928.append(var2563)
            yield from fut
            var928.remove(var2563)
            if (not var928):
                del self.attribute878[var3619]
        var3486 = self.function745(var3619)
        if (var3486 is None):
            var1006 = Class262()
            self.attribute1372.add(var1006)
            self.attribute762[var3619].add(var1006)
            try:
                var3486 = yield from self.function546(arg805)
            except OSError as var3100:
                raise ClientConnectorError(var3100.errno, 'Cannot connect to host {0[0]}:{0[1]} ssl:{0[2]} [{1}]'.format(var3619, var3100.strerror)) from exc
            finally:
                self.attribute1372.remove(var1006)
                self.attribute762[var3619].remove(var1006)
        self.attribute1372.add(var3486)
        self.attribute762[var3619].add(var3486)
        return Class239(self, var3619, var3486, self.attribute18)

    def function745(self, var3619):
        try:
            var1313 = self.attribute871[var3619]
        except KeyError:
            return None
        var4215 = self.attribute18.time()
        while conns:
            (var3486, var2370) = var1313.pop()
            if var3486.is_connected():
                if ((var4215 - var2370) > self.attribute2064):
                    function2607 = var3486.function627()
                    if (var3619[(- 1)] and (not self.attribute1446)):
                        self.attribute1541.append(function2607)
                else:
                    if (not var1313):
                        del self.attribute871[var3619]
                    return var3486
        del self.attribute871[var3619]
        return None

    def function626(self):
        if self.attribute317:
            if ((self.attribute317 - len(self.attribute1372)) > 0):
                for (var3619, var928) in self.attribute878.items():
                    if var928:
                        if (not var928[0].done()):
                            var928[0].set_result(None)
                        break
        elif self.attribute751:
            for (var3619, var928) in self.attribute878.items():
                if var928:
                    if (not var928[0].done()):
                        var928[0].set_result(None)
                    break

    def function13(self, var3619, var3486):
        if self.var792:
            return
        try:
            self.attribute1372.remove(var3486)
            self.attribute762[var3619].remove(var3486)
            if (not self.attribute762[var3619]):
                del self.attribute762[var3619]
        except KeyError:
            pass
        else:
            self.function626()

    def function2678(self, var3619, function2559, *, should_close=False):
        if self.var792:
            return
        self.function13(var3619, function2559)
        if self.attribute1545:
            var813 = True
        if (should_close or function2559.should_close):
            function2607 = function2559.function627()
            if (var3619[(- 1)] and (not self.attribute1446)):
                self.attribute1541.append(function2607)
        else:
            var1313 = self.attribute871.get(var3619)
            if (var1313 is None):
                var1313 = self.attribute871[var3619] = []
            var1313.append((function2559, self.attribute18.time()))
            if (self.attribute922 is None):
                self.attribute922 = helpers.weakref_handle(self, '_cleanup', self.attribute2064, self.attribute18)

    @asyncio.coroutine
    def function546(self, arg805):
        raise NotImplementedError()
var2959 = getattr(ssl, 'OP_NO_COMPRESSION', 0)


class Class273:

    def __init__(self, arg207=None):
        self.attribute910 = {}
        self.attribute538 = {}
        self.attribute955 = {}
        self.attribute551 = arg207

    def __contains__(self, arg111):
        return (arg111 in self.attribute910)

    @property
    def function2256(self):
        return self.attribute910

    def function2322(self, arg1023, function2256):
        self.attribute910[arg1023] = function2256
        self.attribute538[arg1023] = cycle(function2256)
        if self.attribute551:
            self.attribute955[arg1023] = monotonic()

    def function2509(self, arg153):
        self.attribute910.pop(arg153, None)
        self.attribute538.pop(arg153, None)
        if self.attribute551:
            self.attribute955.pop(arg153, None)

    def function2789(self):
        self.attribute910.function2789()
        self.attribute538.function2789()
        self.attribute955.function2789()

    def function1035(self, arg1280):
        return islice(self.attribute538[arg1280], len(self.attribute910[arg1280]))

    def function1349(self, arg1323):
        if (self.attribute551 is None):
            return False
        return ((self.attribute955[arg1323] + self.attribute551) < monotonic())


class Class144(Class224):
    'TCP connector.\n\n    verify_ssl - Set to True to check ssl certifications.\n    fingerprint - Pass the binary md5, sha1, or sha256\n        digest of the expected certificate in DER format to verify\n        that the certificate the server presents matches. See also\n        https://en.wikipedia.org/wiki/Transport_Layer_Security#Certificate_pinning\n    resolve - (Deprecated) Set to True to do DNS lookup for\n        host name.\n    resolver - Enable DNS lookups and use this\n        resolver\n    use_dns_cache - Use memory cache for DNS lookups.\n    ttl_dns_cache - Max seconds having cached a DNS entry, None forever.\n    family - socket address family\n    local_addr - local tuple of (host, port) to bind socket to\n\n    keepalive_timeout - (optional) Keep-alive timeout.\n    force_close - Set to True to force close and do reconnect\n        after each request (and between redirects).\n    limit - The total number of simultaneous connections.\n    limit_per_host - Number of simultaneous connections to one host.\n    loop - Optional event loop.\n    '

    def __init__(self, *, verify_ssl=True, fingerprint=None, resolve=sentinel, use_dns_cache=True, ttl_dns_cache=10, family=0, ssl_context=None, local_addr=None, resolver=None, keepalive_timeout=sentinel, force_close=False, limit=100, limit_per_host=0, enable_cleanup_closed=False, loop=None):
        super().__init__(keepalive_timeout=keepalive_timeout, force_close=function1319, limit=function1950, limit_per_host=function2510, enable_cleanup_closed=enable_cleanup_closed, loop=function1106)
        if ((not function439) and (function2204 is not None)):
            raise ValueError('Either disable ssl certificate validation by verify_ssl=False or specify ssl_context, not both.')
        self.attribute171 = function439
        if function342:
            var4476 = len(function342)
            var775 = var163.get(var4476)
            if (not var775):
                raise ValueError('fingerprint has invalid length')
            elif ((var775 is md5) or (var775 is sha1)):
                warnings.simplefilter('always')
                warnings.warn('md5 and sha1 are insecure and deprecated. Use sha256.', DeprecationWarning, stacklevel=2)
            self.attribute565 = var775
        self.attribute1049 = function342
        if (var151 is None):
            var151 = DefaultResolver(loop=self.attribute18)
        self.attribute577 = var151
        self.attribute604 = function2634
        self.attribute1474 = Class273(ttl=ttl_dns_cache)
        self.attribute17 = function2204
        self.attribute1559 = function732
        self.attribute1234 = local_addr

    @property
    def function439(self):
        'Do check for ssl certifications?'
        return self.attribute171

    @property
    def function342(self):
        'Expected ssl certificate fingerprint.'
        return self.attribute1049

    @property
    def function2204(self):
        'SSLContext instance for https requests.\n\n        Lazy property, creates context on demand.\n        '
        if (self.attribute17 is None):
            if (not self.attribute171):
                var4368 = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
                var4368.options |= ssl.OP_NO_SSLv2
                var4368.options |= ssl.OP_NO_SSLv3
                var4368.options |= var2959
                var4368.set_default_verify_paths()
            else:
                var4368 = ssl.create_default_context()
            self.attribute17 = var4368
        return self.attribute17

    @property
    def function732(self):
        'Socket family like AF_INET.'
        return self.attribute1559

    @property
    def function2634(self):
        'True if local DNS caching is enabled.'
        return self.attribute604

    @property
    def function1998(self):
        'Read-only dict of cached DNS record.'
        return MappingProxyType(self.attribute1474.addrs)

    def function797(self, arg857=None, arg1507=None):
        'Remove specified host/port or clear all dns local cache.'
        if ((arg857 is not None) and (arg1507 is not None)):
            self.attribute1474.remove((arg857, arg1507))
        elif ((arg857 is not None) or (arg1507 is not None)):
            raise ValueError('either both host and port or none of them are allowed')
        else:
            self.attribute1474.clear()

    @asyncio.coroutine
    def function1006(self, arg254, arg677):
        if is_ip_address(arg254):
            return [{'hostname': host, 'host': host, 'port': port, 'family': self.attribute1559, 'proto': 0, 'flags': 0, }]
        if self.attribute604:
            var3619 = (arg254, arg677)
            if ((var3619 not in self.attribute1474) or self.attribute1474.expired(var3619)):
                var2766 = yield from self.attribute577.resolve(arg254, arg677, family=self.attribute1559)
                self.attribute1474.add(var3619, var2766)
            return self.attribute1474.next_addrs(var3619)
        else:
            var1214 = yield from self.attribute577.resolve(arg254, arg677, family=self.attribute1559)
            return var1214

    @asyncio.coroutine
    def function1494(self, arg805):
        'Create connection.\n\n        Has same keyword arguments as BaseEventLoop.create_connection.\n        '
        if arg805.proxy:
            (var4345, var3486) = yield from self.function2147(arg805)
        else:
            (var4345, var3486) = yield from self.function2628(arg805)
        return var3486

    @asyncio.coroutine
    def function2628(self, arg805):
        if arg805.ssl:
            var3926 = self.function2204
        else:
            var3926 = None
        var4004 = yield from self.function1006(arg805.url.raw_host, arg805.port)
        var268 = None
        for var8 in var4004:
            try:
                var3215 = var8['host']
                var1442 = var8['port']
                (var4211, var3486) = yield from self.attribute18.create_connection(self.attribute651, var3215, var1442, ssl=var3926, family=var8['family'], proto=var8['proto'], flags=var8['flags'], server_hostname=(var8['hostname'] if var3926 else None), local_addr=self.attribute1234)
                var1806 = var4211.get_extra_info('sslcontext')
                if (has_cert and self.attribute1049):
                    var2208 = var4211.get_extra_info('socket')
                    if (not hasattr(var2208, 'getpeercert')):
                        var2208 = var4211._ssl_protocol._sslpipe.ssl_object
                    var2595 = var2208.getpeercert(binary_form=True)
                    assert cert
                    var871 = self.attribute565(var2595).digest()
                    var659 = self.attribute1049
                    if (var871 != var659):
                        var4211.function627()
                        if (not self.attribute1446):
                            self.attribute1541.append(var4211)
                        raise ServerFingerprintMismatch(var659, var871, var3215, var1442)
                return (var4211, var3486)
            except OSError as var639:
                var268 = var639
        else:
            raise ClientConnectorError(var268.errno, ('Can not connect to %s:%s [%s]' % (arg805.var3215, arg805.var1442, var268.strerror))) from exc

    @asyncio.coroutine
    def function2147(self, arg805):
        var1269 = ClientRequest(hdrs.METH_GET, arg805.proxy, headers={hdrs.HOST: arg805.headers[hdrs.HOST], }, auth=arg805.proxy_auth, loop=self.attribute18)
        try:
            (function2607, var3486) = yield from self.function2628(var1269)
        except OSError as var268:
            raise ClientProxyConnectionError(*var268.args) from exc
        if (hdrs.AUTHORIZATION in var1269.headers):
            var2715 = var1269.headers[hdrs.AUTHORIZATION]
            del var1269.headers[hdrs.AUTHORIZATION]
            if (not arg805.ssl):
                arg805.headers[hdrs.PROXY_AUTHORIZATION] = var2715
            else:
                var1269.headers[hdrs.PROXY_AUTHORIZATION] = var2715
        if arg805.ssl:
            var1269.method = hdrs.METH_CONNECT
            var1269.url = arg805.url
            var3619 = (arg805.host, arg805.port, arg805.ssl)
            var2995 = Class239(self, var3619, var3486, self.attribute18)
            var2350 = var1269.send(var2995)
            try:
                var2354 = yield from var2350.start(var2995, True)
            except:
                var2350.function627()
                var2995.function627()
                raise
            finally:
                var2350.function627()
            else:
                var2995.attribute58 = None
                var2995._transport = None
                try:
                    if (var2354.status != 200):
                        raise ClientHttpProxyError(var2350.request_info, var2354.history, code=var2354.status, message=var2354.reason, headers=var2354.headers)
                    var4504 = function2607.get_extra_info('socket', default=None)
                    if (var4504 is None):
                        raise RuntimeError('Transport does not expose socket instance')
                    var4504 = var4504.dup()
                finally:
                    function2607.function627()
                (function2607, var3486) = yield from self.attribute18.create_connection(self.attribute651, ssl=self.function2204, sock=var4504, server_hostname=arg805.host)
        return (function2607, var3486)


class Class395(Class224):
    "Unix socket connector.\n\n    path - Unix socket path.\n    keepalive_timeout - (optional) Keep-alive timeout.\n    force_close - Set to True to force close and do reconnect\n        after each request (and between redirects).\n    limit - The total number of simultaneous connections.\n    limit_per_host - Number of simultaneous connections to one host.\n    loop - Optional event loop.\n\n    Usage:\n\n    >>> conn = UnixConnector(path='/path/to/socket')\n    >>> session = ClientSession(connector=conn)\n    >>> resp = yield from session.get('http://python.org')\n\n    "

    def __init__(self, arg316, function1319=False, arg1629=sentinel, function1950=100, function2510=0, function1106=None):
        super().__init__(force_close=function1319, keepalive_timeout=arg1629, limit=function1950, limit_per_host=function2510, loop=function1106)
        self.attribute218 = arg316

    @property
    def function1210(self):
        'Path to unix socket.'
        return self.attribute218

    @asyncio.coroutine
    def function1494(self, arg805):
        (var2950, var3486) = yield from self.attribute18.create_unix_connection(self.attribute651, self.attribute218)
        return var3486