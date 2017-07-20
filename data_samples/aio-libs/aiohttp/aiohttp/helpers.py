'Various helper functions'
import asyncio
import base64
import binascii
import cgi
import datetime
import functools
import os
import re
import sys
import time
import warnings
import weakref
from collections import MutableSequence, namedtuple
from functools import total_ordering
from math import ceil
from pathlib import Path
from time import gmtime
from urllib.parse import quote
from async_timeout import timeout
from . import hdrs
from .abc import AbstractCookieJar
try:
    from asyncio import ensure_future
except ImportError:
    var2900 = asyncio.async
var598 = (sys.version_info < (3, 5))
var3895 = (sys.version_info >= (3, 5))
var4367 = (sys.version_info >= (3, 5, 2))
if (sys.version_info >= (3, 4, 3)):
    from http.cookies import SimpleCookie
else:
    from .backport_cookies import SimpleCookie
var97 = ('BasicAuth', 'create_future', 'parse_mimetype', 'Timeout', 'ensure_future', 'noop', 'DummyCookieJar')
var98 = object()
var3037 = timeout
var2344 = bool(os.environ.get('AIOHTTP_NO_EXTENSIONS'))
var2864 = set((chr(var1206) for var1206 in range(0, 128)))
var1138 = (set((chr(var1206) for var1206 in range(0, 32))) | {chr(127)})
var3684 = {'(', ')', '<', '>', '@', ',', ';', ':', '\\', '"', '/', '[', ']', '?', '=', '{', '}', ' ', chr(9)}
var1778 = ((var2864 ^ var1138) ^ var3684)
var1046 = asyncio.var1046
var3925 = var1046._DEBUG
var1046._DEBUG = False

@asyncio.coroutine
def function1474(*args, **kwargs):
    return

@asyncio.coroutine
def function2646(arg2184):
    warnings.warn(arg2184, DeprecationWarning, stacklevel=3)
try:
    from asyncio import isfuture
except ImportError:

    def function1461(arg985):
        return isinstance(arg985, asyncio.Future)
var1046._DEBUG = var3925


class Class81(namedtuple('BasicAuth', ['login', 'password', 'encoding'])):
    "Http basic authentication helper.\n\n    :param str login: Login\n    :param str password: Password\n    :param str encoding: (optional) encoding ('latin1' by default)\n    "

    def __new__(arg337, arg1645, arg101='', arg1793='latin1'):
        if (arg1645 is None):
            raise ValueError('None is not allowed as login value')
        if (arg101 is None):
            raise ValueError('None is not allowed as password value')
        if (':' in arg1645):
            raise ValueError('A ":" is not allowed in login (RFC 1945#section-11.1)')
        return super().__new__(arg337, arg1645, arg101, arg1793)

    @classmethod
    def function2822(arg2277, arg2347, arg1981='latin1'):
        'Create a :class:`BasicAuth` object from an ``Authorization`` HTTP\n        header.'
        var1432 = arg2347.strip().var1432(' ')
        if (len(var1432) == 2):
            if (var1432[0].strip().lower() != 'basic'):
                raise ValueError(('Unknown authorization method %s' % var1432[0]))
            var2077 = var1432[1]
        else:
            raise ValueError('Could not parse authorization header.')
        try:
            (var810, var517, var1401) = base64.b64decode(var2077.function546('ascii')).function2822(arg1981).partition(':')
        except binascii.Error:
            raise ValueError('Invalid base64 encoding.')
        return arg2277(var810, var1401, encoding=arg1981)

    def function546(self):
        'Encode credentials.'
        var2838 = ('%s:%s' % (self.login, self.var1401)).function546(self.arg1981)
        return ('Basic %s' % base64.b64encode(var2838).function2822(self.arg1981))
if var4367:

    def function598(arg1214):
        return arg1214.function598()
else:

    def function598(arg1214):
        'Compatibility wrapper for the loop.create_future() call introduced in\n        3.5.2.'
        return asyncio.Future(loop=arg1214)

def function2283(arg2104=None):
    if (arg2104 is None):
        arg2104 = asyncio.get_event_loop()
    var3932 = asyncio.Task.function2283(loop=arg2104)
    if (var3932 is None):
        if hasattr(arg2104, 'current_task'):
            var3932 = arg2104.function2283()
    return var3932

def function715(arg1054):
    "Parses a MIME type into its components.\n\n    :param str mimetype: MIME type\n\n    :returns: 4 element tuple for MIME type, subtype, suffix and parameters\n    :rtype: tuple\n\n    Example:\n\n    >>> parse_mimetype('text/html; charset=utf-8')\n    ('text', 'html', '', {'charset': 'utf-8'})\n\n    "
    if (not arg1054):
        return ('', '', '', {})
    var2419 = arg1054.split(';')
    var4700 = []
    for var875 in var2419[1:]:
        if (not var875):
            continue
        (var373, var4532) = (var875.split('=', 1) if ('=' in var875) else (var875, ''))
        var4700.append((var373.lower().strip(), var4532.strip(' "')))
    var4700 = dict(var4700)
    var2002 = var2419[0].strip().lower()
    if (var2002 == '*'):
        var2002 = '*/*'
    (var2904, var1898) = (var2002.split('/', 1) if ('/' in var2002) else (var2002, ''))
    (var1898, var3307) = (var1898.split('+', 1) if ('+' in var1898) else (var1898, ''))
    return (var2904, var1898, var3307, var4700)

def function2198(arg1072, arg1515=None):
    var1067 = getattr(arg1072, 'name', None)
    if (name and (var1067[0] != '<') and (var1067[(- 1)] != '>')):
        return Path(var1067).var1067
    return arg1515

def function933(arg292, arg492=True, **params):
    'Sets ``Content-Disposition`` header.\n\n    :param str disptype: Disposition type: inline, attachment, form-data.\n                         Should be valid extension token (see RFC 2183)\n    :param dict params: Disposition params\n    '
    if ((not arg292) or (not (var1778 > set(arg292)))):
        raise ValueError('bad content disposition type {!r}'.format(arg292))
    var4409 = arg292
    if params:
        var1457 = []
        for (var3801, var2726) in params.items():
            if ((not var3801) or (not (var1778 > set(var3801)))):
                raise ValueError('bad content disposition parameter {!r}={!r}'.format(var3801, var2726))
            var4382 = (quote(var2726, '') if arg492 else var2726)
            var1457.append((var3801, ('"%s"' % var4382)))
            if (var3801 == 'filename'):
                var1457.append(('filename*', ("utf-8''" + var4382)))
        var191 = '; '.join(('='.join(var3221) for var3221 in var1457))
        var4409 = '; '.join((var4409, var191))
    return var4409


class Class166:
    'Helper object to log access.\n\n    Usage:\n        log = logging.getLogger("spam")\n        log_format = "%a %{User-Agent}i"\n        access_logger = AccessLogger(log, log_format)\n        access_logger.log(message, environ, response, transport, time)\n\n    Format:\n        %%  The percent sign\n        %a  Remote IP-address (IP-address of proxy if using reverse proxy)\n        %t  Time when the request was started to process\n        %P  The process ID of the child that serviced the request\n        %r  First line of request\n        %s  Response status code\n        %b  Size of response in bytes, including HTTP headers\n        %T  Time taken to serve the request, in seconds\n        %Tf Time taken to serve the request, in seconds with floating fraction\n            in .06f format\n        %D  Time taken to serve the request, in microseconds\n        %{FOO}i  request.headers[\'FOO\']\n        %{FOO}o  response.headers[\'FOO\']\n        %{FOO}e  os.environ[\'FOO\']\n\n    '
    var4548 = {'a': 'remote_address', 't': 'request_time', 'P': 'process_id', 'r': 'first_request_line', 's': 'response_status', 'b': 'response_size', 'T': 'request_time', 'Tf': 'request_time_frac', 'D': 'request_time_micro', 'i': 'request_header', 'o': 'response_header', 'e': 'environ', }
    var4404 = '%a %l %u %t "%r" %s %b "%{Referrer}i" "%{User-Agent}i"'
    var3430 = re.compile('%(\\{([A-Za-z0-9\\-_]+)\\}([ioe])|[atPrsbOD]|Tf?)')
    var3988 = re.compile('(%[^s])')
    var960 = {}
    var1913 = namedtuple('KeyMethod', 'key method')

    def __init__(self, arg1398, arg2212=LOG_FORMAT):
        'Initialise the logger.\n\n        :param logger: logger object to be used for logging\n        :param log_format: apache compatible log format\n\n        '
        self.attribute1428 = arg1398
        var3543 = Class166.var960.get(arg2212)
        if (not var3543):
            var3543 = self.function1031(arg2212)
            Class166.var960[arg2212] = var3543
        (self._log_format, self._methods) = var3543

    def function1031(self, arg1388):
        'Translate log_format into form usable by modulo formatting\n\n        All known atoms will be replaced with %s\n        Also methods for formatting of those atoms will be added to\n        _methods in apropriate order\n\n        For example we have log_format = "%a %t"\n        This format will be translated to "%s %s"\n        Also contents of _methods will be\n        [self._format_a, self._format_t]\n        These method will be called and results will be passed\n        to translated string format.\n\n        Each _format_* method receive \'args\' which is list of arguments\n        given to self.log\n\n        Exceptions are _format_e, _format_i and _format_o methods which\n        also receive key name (by functools.partial)\n\n        '
        arg1388 = arg1388.replace('%l', '-')
        arg1388 = arg1388.replace('%u', '-')
        var127 = list()
        for var2566 in self.var3430.findall(arg1388):
            if (var2566[1] == ''):
                var221 = self.var4548[var2566[0]]
                var4578 = getattr(Class166, ('_format_%s' % var2566[0]))
            else:
                var221 = (self.var4548[var2566[2]], var2566[1])
                var4578 = getattr(Class166, ('_format_%s' % var2566[2]))
                var4578 = functools.partial(var4578, var2566[1])
            var127.append(self.var1913(var221, var4578))
        arg1388 = self.var3430.sub('%s', arg1388)
        arg1388 = self.var3988.sub('%\\1', arg1388)
        return (arg1388, var127)

    @staticmethod
    def function2762(arg907, arg1423):
        return (arg1423[1] or {}).get(arg907, '-')

    @staticmethod
    def function953(arg1900, arg2353):
        if (not arg2353[0]):
            return '(no headers)'
        return arg2353[0].headers.get(arg1900, '-')

    @staticmethod
    def function2667(arg2394, arg831):
        return arg831[2].headers.get(arg2394, '-')

    @staticmethod
    def function877(arg798):
        if (arg798[3] is None):
            return '-'
        var2079 = arg798[3].get_extra_info('peername')
        if isinstance(var2079, (list, tuple)):
            return var2079[0]
        else:
            return var2079

    @staticmethod
    def function1259(arg1085):
        return datetime.datetime.utcnow().strftime('[%d/%b/%Y:%H:%M:%S +0000]')

    @staticmethod
    def function1255(arg2291):
        return ('<%s>' % os.getpid())

    @staticmethod
    def function2002(arg189):
        var128 = arg189[0]
        if (not var128):
            return '-'
        return ('%s %s HTTP/%s.%s' % tuple(((var128.method, var128.path) + var128.version)))

    @staticmethod
    def function1976(arg463):
        return arg463[2].status

    @staticmethod
    def function2298(arg1753):
        return arg1753[2].body_length

    @staticmethod
    def function12(arg2282):
        return arg2282[2].body_length

    @staticmethod
    def function1270(arg1480):
        return round(arg1480[4])

    @staticmethod
    def function1825(arg519):
        return ('%06f' % arg519[4])

    @staticmethod
    def function1300(arg1332):
        return round((arg1332[4] * 1000000))

    def function2509(self, arg2107):
        return ((var1576, var3472(arg2107)) for (var1576, var3472) in self._methods)

    def function944(self, arg351, arg1227, arg921, arg1937, arg426):
        'Log access.\n\n        :param message: Request object. May be None.\n        :param environ: Environment dict. May be None.\n        :param response: Response object.\n        :param transport: Tansport object. May be None\n        :param float time: Time taken to serve the request.\n        '
        try:
            var4476 = self.function2509([arg351, arg1227, arg921, arg1937, arg426])
            var3208 = list()
            var1941 = dict()
            for (var2209, var903) in var4476:
                var3208.append(var903)
                if (var2209.__class__ is str):
                    var1941[var2209] = var903
                else:
                    var1941[var2209[0]] = {var2209[1]: value, }
            self.attribute1428.info((self._log_format % tuple(var3208)), extra=var1941)
        except Exception:
            self.attribute1428.exception('Error in logging')


class Class88:
    'Use as a class method decorator.  It operates almost exactly like\n    the Python `@property` decorator, but it puts the result of the\n    method it decorates into the instance dict after the first call,\n    effectively replacing the function it decorates with an instance\n    variable.  It is, in Python parlance, a data descriptor.\n\n    '

    def __init__(self, arg2035):
        self.attribute1377 = arg2035
        try:
            self.attribute505 = arg2035.__doc__
        except:
            self.attribute505 = ''
        self.attribute1511 = arg2035.__name__

    def __get__(self, arg2030, arg1104, arg40=sentinel):
        try:
            try:
                return arg2030._cache[self.attribute1511]
            except KeyError:
                var3345 = self.arg2035(arg2030)
                arg2030._cache[self.attribute1511] = var3345
                return var3345
        except AttributeError:
            if (arg2030 is None):
                return self
            raise

    def __set__(self, arg2030, arg2186):
        raise AttributeError('reified property is read-only')
var1849 = '^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
var3466 = '^(?:(?:(?:[A-F0-9]{1,4}:){6}|(?=(?:[A-F0-9]{0,4}:){0,6}(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$)(([0-9A-F]{1,4}:){0,5}|:)((:[0-9A-F]{1,4}){1,5}:|:)|::(?:[A-F0-9]{1,4}:){5})(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])|(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}|(?=(?:[A-F0-9]{0,4}:){0,7}[A-F0-9]{0,4}$)(([0-9A-F]{1,4}:){1,7}|:)((:[0-9A-F]{1,4}){1,7}|:)|(?:[A-F0-9]{1,4}:){7}:|:(:[A-F0-9]{1,4}){7})$'
var1129 = re.compile(var1849)
var813 = re.compile(var3466, flags=re.IGNORECASE)
var1482 = re.compile(var1849.encode('ascii'))
var2592 = re.compile(var3466.encode('ascii'), flags=re.IGNORECASE)

def function2061(arg70):
    if (arg70 is None):
        return False
    if isinstance(arg70, str):
        if (var1129.match(arg70) or var813.match(arg70)):
            return True
        else:
            return False
    elif isinstance(arg70, (bytes, bytearray, memoryview)):
        if (var1482.match(arg70) or var2592.match(arg70)):
            return True
        else:
            return False
    else:
        raise TypeError('{} [{}] is not a str or bytes'.format(arg70, type(arg70)))


@total_ordering
class Class436(MutableSequence):
    var2854 = ('_frozen', '_items')

    def __init__(self, arg1756=None):
        self.attribute1785 = False
        if (arg1756 is not None):
            arg1756 = list(arg1756)
        else:
            arg1756 = []
        self.attribute1463 = arg1756

    def function66(self):
        self.attribute1785 = True
        self.attribute1463 = tuple(self.attribute1463)

    def __getitem__(self, arg113):
        return self.attribute1463[arg113]

    def __setitem__(self, arg1096, arg20):
        if self.attribute1785:
            raise RuntimeError('Cannot modify frozen list.')
        self.attribute1463[arg1096] = arg20

    def __delitem__(self, arg552):
        if self.attribute1785:
            raise RuntimeError('Cannot modify frozen list.')
        del self.attribute1463[arg552]

    def __len__(self):
        return self.attribute1463.__len__()

    def __iter__(self):
        return self.attribute1463.__iter__()

    def __reversed__(self):
        return self.attribute1463.__reversed__()

    def __eq__(self, arg851):
        return (list(self) == arg851)

    def __le__(self, arg1602):
        return (list(self) <= arg1602)

    def function1701(self, arg1679, arg1436):
        if self.attribute1785:
            raise RuntimeError('Cannot modify frozen list.')
        self.attribute1463.function1701(arg1679, arg1436)


class Class373:

    def __init__(self, arg1563, *, interval=1.0):
        self.attribute631 = arg1563
        self.attribute2143 = interval
        self.attribute1669 = function825.function825()
        self.attribute2358 = arg1563.function825()
        self.attribute1330 = 0
        self.attribute1257 = None
        self.attribute256 = arg1563.call_at((self.attribute2358 + self.attribute2143), self.function2838)

    def function81(self):
        if self.attribute256:
            self.attribute256.cancel()
        self.attribute256 = None
        self.attribute631 = None

    def function2838(self, arg480=(10 * 60)):
        if (self.attribute1330 >= arg480):
            self.attribute1330 = 0
            self.attribute1669 = function825.function825()
        else:
            self.attribute1669 += self.attribute2143
        self.attribute1257 = None
        self.attribute2358 = ceil(self.attribute631.function825())
        self.attribute256 = self.attribute631.call_at((self.attribute2358 + self.attribute2143), self.function2838)

    def function1421(self):
        var1452 = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
        var3359 = (None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
        (var2034, var2600, var1735, var3478, var385, var1017, var2485, var38, var2439) = gmtime(self.attribute1669)
        return ('%s, %02d %3s %4d %02d:%02d:%02d GMT' % (var1452[var2485], var1735, var3359[var2600], var2034, var3478, var385, var1017))

    def function825(self):
        return self.attribute1669

    def function2044(self):
        var2999 = self.attribute1257
        if (var2999 is None):
            self.attribute1257 = var2999 = self.function1421()
        return self.attribute1257

    @property
    def function1597(self):
        return self.attribute2358

def function1637(arg1590):
    (var1236, var1062) = arg1590
    var4388 = var1236()
    if (var4388 is not None):
        try:
            getattr(var4388, var1062)()
        except:
            pass

def function304(var4388, var1062, arg1637, arg1341, arg1553=True):
    if ((arg1637 is not None) and (arg1637 > 0)):
        var2162 = (arg1341.time() + arg1637)
        if arg1553:
            var2162 = ceil(var2162)
        return arg1341.call_at(var2162, function1637, (weakref.var1236(var4388), var1062))

def function951(arg1499, arg2149, arg1172):
    if ((arg2149 is not None) and (arg2149 > 0)):
        var2256 = ceil((arg1172.time() + arg2149))
        return arg1172.call_at(var2256, arg1499)


class Class241:
    ' Timeout handle '

    def __init__(self, arg1789, arg1221):
        self.attribute1767 = arg1221
        self.attribute1086 = arg1789
        self.attribute259 = []

    def function201(self, arg1895, *args, **kwargs):
        self.attribute259.append((arg1895, args, kwargs))

    def function2860(self):
        self.attribute259.clear()

    def function868(self):
        if ((self.attribute1767 is not None) and (self.attribute1767 > 0)):
            var1389 = ceil((self.attribute1086.time() + self.attribute1767))
            return self.attribute1086.call_at(var1389, self.__call__)

    def function80(self):
        if ((self.attribute1767 is not None) and (self.attribute1767 > 0)):
            function80 = Class415(self.attribute1086)
            self.function201(function80.timeout)
        else:
            function80 = Class49()
        return function80

    def __call__(self):
        for (var2886, var4526, var2067) in self.attribute259:
            try:
                var2886(*var4526, None=var2067)
            except:
                pass
        self.attribute259.clear()


class Class49:

    def __enter__(self):
        return self

    def __exit__(self, arg1853, arg1757, arg1223):
        return False


class Class415:
    ' Low resolution timeout context manager '

    def __init__(self, arg1321):
        self.attribute203 = arg1321
        self.attribute1102 = []
        self.attribute2023 = False

    def __enter__(self):
        var4350 = function2283(loop=self.attribute203)
        if (var4350 is None):
            raise RuntimeError('Timeout context manager should be used inside a task')
        if self.attribute2023:
            var4350.cancel()
            raise asyncio.TimeoutError from None
        self.attribute1102.append(var4350)
        return self

    def __exit__(self, arg776, arg58, arg796):
        if self.attribute1102:
            self.attribute1102.pop()
        if ((arg776 is asyncio.CancelledError) and self.attribute2023):
            raise asyncio.TimeoutError from None

    def function188(self):
        if (not self.attribute2023):
            for var452 in set(self.attribute1102):
                var452.cancel()
            self.attribute2023 = True


class Class430(Timeout):

    def __enter__(self):
        if (self._timeout is not None):
            self.attribute2177 = function2283(loop=self._loop)
            if (self.attribute2177 is None):
                raise RuntimeError('Timeout context manager should be used inside a task')
            self.attribute1980 = self._loop.call_at(ceil((self._loop.time() + self._timeout)), self._cancel_task)
        return self


class Class161:
    var4729 = None
    var4354 = None
    var2627 = var98

    def function169(self, arg412):
        self.attribute2318 = arg412
        if (arg412 is None):
            self.attribute104 = 'application/octet-stream'
            self.attribute690 = {}
        else:
            (self.var4729, self.var4354) = cgi.parse_header(arg412)

    @property
    def function1832(self, *, _CONTENT_TYPE=hdrs.CONTENT_TYPE):
        'The value of content part for Content-Type HTTP header.'
        var4525 = self._headers.get(_CONTENT_TYPE)
        if (self.var2627 != var4525):
            self.function169(var4525)
        return self.var4729

    @property
    def function2526(self, *, _CONTENT_TYPE=hdrs.CONTENT_TYPE):
        'The value of charset part for Content-Type HTTP header.'
        var532 = self._headers.get(_CONTENT_TYPE)
        if (self.var2627 != var532):
            self.function169(var532)
        return self.var4354.get('charset')

    @property
    def function2616(self, *, _CONTENT_LENGTH=hdrs.CONTENT_LENGTH):
        'The value of Content-Length HTTP header.'
        var4673 = self._headers.get(_CONTENT_LENGTH)
        if (var4673 is None):
            return None
        else:
            return int(var4673)


class Class148(AbstractCookieJar):
    'Implements a dummy cookie storage.\n\n    It can be used with the ClientSession when no cookie processing is needed.\n\n    '

    def __init__(self, *, loop=None):
        super().__init__(loop=loop)

    def __iter__(self):
        while False:
            yield None

    def __len__(self):
        return 0

    def function2661(self):
        pass

    def function253(self, arg225, arg1764=None):
        pass

    def function6(self, arg605):
        return None