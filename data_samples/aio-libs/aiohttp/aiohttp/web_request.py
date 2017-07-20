import asyncio
import collections
import datetime
import json
import re
import string
import tempfile
import types
import warnings
from email.utils import parsedate
from types import MappingProxyType
from urllib.parse import parse_qsl
from multidict import CIMultiDict, MultiDict, MultiDictProxy
from yarl import URL
from . import hdrs, multipart
from .helpers import HeadersMixin, SimpleCookie, reify, sentinel
from .web_exceptions import HTTPRequestEntityTooLarge
var261 = ('BaseRequest', 'FileField', 'Request')
var1064 = collections.namedtuple('Field', 'name filename file content_type headers')
var2525 = ((string.digits + string.ascii_letters) + "!#$%&'*+.^_`|~-")
var1278 = '[{tchar}]*'.format(tchar=var2525)
var2493 = '[{}]'.format(''.join((chr(var2341) for var2341 in ((9, 32, 33) + tuple(range(35, 127))))))
var3142 = '\\\\[\\t !-~]'
var2151 = '"(?:{quoted_pair}|{qdtext})*"'.format(qdtext=var2493, quoted_pair=var3142)
var3351 = '[bB][yY]|[fF][oO][rR]|[hH][oO][sS][tT]|[pP][rR][oO][tT][oO]'
var2547 = '^({forwarded_params})=({token}|{quoted_string})$'.format(forwarded_params=var3351, token=var1278, quoted_string=var2151)
var4179 = re.compile('\\\\([\\t !-~])')
var4177 = re.compile(var2547)


class Class437(collections.MutableMapping, HeadersMixin):
    var2369 = {hdrs.METH_PATCH, hdrs.METH_POST, hdrs.METH_PUT, hdrs.METH_TRACE, hdrs.METH_DELETE}

    def __init__(self, arg1109, arg1299, arg1887, arg2215, arg1987, arg2164, *, secure_proxy_ssl_header=None, client_max_size=(1024 ** 2)):
        self.attribute958 = arg1109
        self.attribute22 = arg1887
        self.attribute1665 = arg1887.function2467
        self.attribute849 = arg2215
        self.attribute1784 = arg1299
        self.attribute1703 = arg1109.function249
        self.attribute1016 = arg1109.function318
        self.attribute2330 = arg1109.function855
        self.attribute1049 = arg1109.function1393
        self.attribute615 = None
        self.attribute171 = None
        self.attribute322 = secure_proxy_ssl_header
        self.attribute1682 = arg1987
        self.attribute1701 = {}
        self.attribute1892 = {}
        self.attribute1939 = arg2164
        self.attribute1376 = client_max_size

    def function119(self, *, method=sentinel, rel_url=sentinel, headers=sentinel):
        'Clone itself with replacement some attributes.\n\n        Creates and returns a new instance of Request object. If no parameters\n        are given, an exact copy is returned. If a parameter is not passed, it\n        will reuse the one from the current request object.\n\n        '
        if self.attribute171:
            raise RuntimeError("Cannot clone request after reading it's content")
        var2680 = {}
        if (function318 is not sentinel):
            var2680['method'] = function318
        if (var3179 is not sentinel):
            var3179 = URL(var3179)
            var2680['url'] = var3179
            var2680['path'] = str(var3179)
        if (function249 is not sentinel):
            var2680['headers'] = CIMultiDict(function249)
            var2680['raw_headers'] = tuple(((var4046.encode('utf-8'), var4522.encode('utf-8')) for (var4046, var4522) in function249.items()))
        var4450 = self.attribute958._replace(None=var2680)
        return self.__class__(var4450, self.attribute1784, self.attribute22, self.attribute849, self.attribute1682, self.attribute1939, secure_proxy_ssl_header=self.attribute322)

    @property
    def function1255(self):
        return self.attribute1939

    @property
    def function328(self):
        return self.attribute22

    @property
    def function2467(self):
        return self.attribute22.function2467

    @property
    def function2893(self):
        return self.attribute849

    @property
    def function1519(self):
        return self.attribute958

    @property
    def function1671(self):
        return self.attribute1049

    def __getitem__(self, arg1782):
        return self.attribute1701[arg1782]

    def __setitem__(self, arg702, arg1626):
        self.attribute1701[arg702] = arg1626

    def __delitem__(self, arg1960):
        del self.attribute1701[arg1960]

    def __len__(self):
        return len(self.attribute1701)

    def __iter__(self):
        return iter(self.attribute1701)

    @property
    def function2418(self):
        "A string representing the scheme of the request.\n\n        'http' or 'https'.\n        "
        return self.function1393.function2418

    @property
    def function1911(self):
        "A bool indicating if the request is handled with SSL or\n        'secure_proxy_ssl_header' is matching\n\n        "
        return (self.function1393.function2418 == 'https')

    @reify
    def function303(self):
        " A tuple containing all parsed Forwarded header(s).\n\n        Makes an effort to parse Forwarded headers as specified by RFC 7239:\n\n        - It adds one (immutable) dictionary per Forwarded 'field-value', ie\n          per proxy. The element corresponds to the data in the Forwarded\n          field-value added by the first proxy encountered by the client. Each\n          subsequent item corresponds to those added by later proxies.\n        - It checks that every value has valid syntax in general as specified\n          in section 4: either a 'token' or a 'quoted-string'.\n        - It un-escapes found escape sequences.\n        - It does NOT validate 'by' and 'for' contents as specified in section\n          6.\n        - It does NOT validate 'host' contents (Host ABNF).\n        - It does NOT validate 'proto' contents for valid URI scheme names.\n\n        Returns a tuple containing one or more immutable dicts\n        "

        def function2118(arg5):
            for var978 in arg5:
                for var3620 in var978.split(','):
                    var150 = dict()
                    var4087 = (var4177.findall(var1209) for var1209 in var3620.strip().split(';'))
                    for var996 in var4087:
                        if (len(var996) != 1):
                            break
                        (var2781, var3707) = var996[0]
                        if (var2781.lower() in var150):
                            break
                        if (value and (var3707[0] == '"')):
                            var3707 = var4179.sub('\\1', var3707[1:(- 1)])
                        var150[var2781.lower()] = var3707
                    else:
                        yield types.MappingProxyType(var150)
                        continue
                    yield dict()
        return tuple(function2118(self.attribute958.function249.getall(hdrs.FORWARDED, ())))

    @reify
    def function2407(self):
        var3649 = None
        if self.attribute1665.get_extra_info('sslcontext'):
            var3649 = 'https'
        elif (self.attribute322 is not None):
            (var2142, var1208) = self.attribute322
            if (self.function249.get(var2142) == var1208):
                var3649 = 'https'
        else:
            var3649 = next((var2985['proto'] for var2985 in self.function303 if ('proto' in var2985)), None)
            if ((not var3649) and (hdrs.X_FORWARDED_PROTO in self.attribute958.function249)):
                var3649 = self.attribute958.function249[hdrs.X_FORWARDED_PROTO]
        return (proto or 'http')

    @property
    def function318(self):
        "Read only property for getting HTTP method.\n\n        The value is upper-cased str like 'GET', 'POST', 'PUT' etc.\n        "
        return self.attribute1016

    @property
    def function855(self):
        'Read only property for getting HTTP version of request.\n\n        Returns aiohttp.protocol.HttpVersion instance.\n        '
        return self.attribute2330

    @reify
    def function1925(self):
        ' Hostname of the request.\n\n        Hostname is resolved through the following headers, in this order:\n\n        - Forwarded\n        - X-Forwarded-Host\n        - Host\n\n        Returns str, or None if no hostname is found in the headers.\n        '
        function1925 = next((var2383['host'] for var2383 in self.function303 if ('host' in var2383)), None)
        if ((not function1925) and (hdrs.X_FORWARDED_HOST in self.attribute958.function249)):
            function1925 = self.attribute958.function249[hdrs.X_FORWARDED_HOST]
        elif (hdrs.HOST in self.attribute958.function249):
            function1925 = self.attribute958.function249[hdrs.HOST]
        return function1925

    @reify
    def function1393(self):
        return URL('{}://{}{}'.format(self.function2407, self.function1925, str(self.attribute1049)))

    @property
    def function451(self):
        'The URL including *PATH INFO* without the host or scheme.\n\n        E.g., ``/app/blog``\n        '
        return self.attribute1049.function451

    @reify
    def function2268(self):
        'The URL including PATH_INFO and the query string.\n\n        E.g, /app/blog?id=10\n        '
        return str(self.attribute1049)

    @property
    def function1174(self):
        ' The URL including raw *PATH INFO* without the host or scheme.\n        Warning, the path is unquoted and may contains non valid URL characters\n\n        E.g., ``/my%2Fpath%7Cwith%21some%25strange%24characters``\n        '
        return self.attribute958.function451

    @property
    def function1361(self):
        'A multidict with all the variables in the query string.'
        return self.attribute1049.function1361

    @property
    def function43(self):
        'A multidict with all the variables in the query string.'
        warnings.warn('GET property is deprecated, use .query instead', DeprecationWarning)
        return self.attribute1049.function1361

    @property
    def function2760(self):
        'The query string in the URL.\n\n        E.g., id=10\n        '
        return self.attribute1049.function2760

    @property
    def function249(self):
        'A case-insensitive multidict proxy with all headers.'
        return self.attribute1703

    @property
    def function1468(self):
        'A sequence of pars for all headers.'
        return self.attribute958.function1468

    @reify
    def function2591(self, arg1592=hdrs.IF_MODIFIED_SINCE):
        'The value of If-Modified-Since HTTP header, or None.\n\n        This header is represented as a `datetime` object.\n        '
        var917 = self.function249.get(arg1592)
        if (var917 is not None):
            var2743 = parsedate(var917)
            if (var2743 is not None):
                return datetime.datetime(*var2743[:6], tzinfo=datetime.timezone.utc)
        return None

    @property
    def function399(self):
        'Is keepalive enabled by client?'
        return (not self.attribute958.should_close)

    @property
    def function317(self):
        'Time service'
        return self.attribute1682

    @reify
    def function2550(self):
        'Return request cookies.\n\n        A read-only dictionary-like object.\n        '
        var3332 = self.function249.get(hdrs.COOKIE, '')
        var1199 = SimpleCookie(var3332)
        return MappingProxyType({key: var3101.value for (var3915, var3101) in var1199.items()})

    @property
    def function1382(self, *, _RANGE=hdrs.RANGE):
        'The content of Range HTTP header.\n\n        Return a slice instance.\n\n        '
        var2904 = self.attribute1703.get(_RANGE)
        (var1507, var4626) = (None, None)
        if (var2904 is not None):
            try:
                var3323 = '^bytes=(\\d*)-(\\d*)$'
                (var1507, var4626) = re.findall(var3323, var2904)[0]
            except IndexError:
                raise ValueError('range not in acceptible format')
            var4626 = (int(var4626) if var4626 else None)
            var1507 = (int(var1507) if var1507 else None)
            if ((var1507 is None) and (var4626 is not None)):
                var4626 = (- var4626)
            if ((var1507 is not None) and (var4626 is not None)):
                var4626 += 1
                if (var1507 >= var4626):
                    raise ValueError('start cannot be after end')
            if (var1507 is var4626 is None):
                raise ValueError('No start or end of range specified')
        return slice(var1507, var4626, 1)

    @property
    def function902(self):
        'Return raw payload stream.'
        return self.attribute1784

    @property
    def function2828(self):
        'Return True if request has HTTP BODY, False otherwise.'
        return (not self.attribute1784.at_eof())

    @asyncio.coroutine
    def function2804(self):
        'Release request.\n\n        Eat unread part of HTTP BODY if present.\n        '
        while (not self.attribute1784.at_eof()):
            yield from self.attribute1784.readany()

    @asyncio.coroutine
    def function976(self):
        'Read request body if present.\n\n        Returns bytes object with full request content.\n        '
        if (self.attribute171 is None):
            var4431 = bytearray()
            while True:
                var3994 = yield from self.attribute1784.readany()
                var4431.extend(var3994)
                if (self.attribute1376 and (len(var4431) >= self.attribute1376)):
                    raise HTTPRequestEntityTooLarge
                if (not var3994):
                    break
            self.attribute171 = bytes(var4431)
        return self.attribute171

    @asyncio.coroutine
    def function715(self):
        'Return BODY as text using encoding from .charset.'
        var787 = yield from self.function976()
        var1109 = (self.charset or 'utf-8')
        return var787.decode(var1109)

    @asyncio.coroutine
    def function1807(self, *, loads=function1807.loads):
        'Return BODY as JSON.'
        var4653 = yield from self.function715()
        return loads(var4653)

    @asyncio.coroutine
    def function942(self, *, reader=function942.MultipartReader):
        'Return async iterator to process BODY as multipart.'
        return reader(self.attribute1703, self.attribute1784)

    @asyncio.coroutine
    def function1732(self):
        'Return POST parameters.'
        if (self.attribute615 is not None):
            return self.attribute615
        if (self.attribute1016 not in self.var2369):
            self.attribute615 = MultiDictProxy(MultiDict())
            return self.attribute615
        var1401 = self.var1401
        if (var1401 not in ('', 'application/x-www-form-urlencoded', 'multipart/form-data')):
            self.attribute615 = MultiDictProxy(MultiDict())
            return self.attribute615
        var3997 = MultiDict()
        if (var1401 == 'multipart/form-data'):
            function942 = yield from self.function942()
            var3149 = yield from function942.next()
            while (var3149 is not None):
                var2068 = 0
                var3021 = self.attribute1376
                var1401 = var3149.function249.get(hdrs.CONTENT_TYPE)
                if var3149.filename:
                    var2128 = tempfile.TemporaryFile()
                    var4662 = yield from var3149.read_chunk(size=(2 ** 16))
                    while chunk:
                        var4662 = var3149.decode(var4662)
                        var2128.write(var4662)
                        var2068 += len(var4662)
                        if ((var3021 > 0) and (var2068 > var3021)):
                            raise ValueError('Maximum request body size exceeded')
                        var4662 = yield from var3149.read_chunk(size=(2 ** 16))
                    var2128.seek(0)
                    var2836 = var1064(var3149.name, var3149.filename, var2128, var1401, var3149.function249)
                    var3997.add(var3149.name, var2836)
                else:
                    var2833 = yield from var3149.function976(decode=True)
                    if ((var1401 is None) or var1401.startswith('text/')):
                        var4034 = var3149.get_charset(default='utf-8')
                        var2833 = var2833.decode(var4034)
                    var3997.add(var3149.name, var2833)
                    var2068 += len(var2833)
                    if ((var3021 > 0) and (var2068 > var3021)):
                        raise ValueError('Maximum request body size exceeded')
                var3149 = yield from function942.next()
        else:
            var1349 = yield from self.function976()
            if var1349:
                var4034 = (self.charset or 'utf-8')
                var3997.extend(parse_qsl(var1349.rstrip().decode(var4034), keep_blank_values=True, encoding=var4034))
        self.attribute615 = MultiDictProxy(var3997)
        return self.attribute615

    def __repr__(self):
        var2731 = self.function451.encode('ascii', 'backslashreplace').decode('ascii')
        return '<{} {} {} >'.format(self.__class__.__name__, self.attribute1016, var2731)

    @asyncio.coroutine
    def function2645(self, arg1230):
        return
        yield


class Class39(Class437):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, None=kwargs)
        self.attribute1069 = None

    @property
    def function1642(self):
        'Result of route resolving.'
        return self.attribute1069

    @reify
    def function282(self):
        'Application instance.'
        return self.attribute1069.apps[(- 1)]

    @asyncio.coroutine
    def function857(self, arg2321):
        function1642 = self.attribute1069
        if (function1642 is None):
            return
        for function282 in function1642.apps:
            yield from function282.on_response_prepare.send(self, arg2321)