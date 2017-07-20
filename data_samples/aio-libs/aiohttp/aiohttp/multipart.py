import asyncio
import base64
import binascii
import json
import re
import uuid
import warnings
import zlib
from collections import Mapping, Sequence, deque
from urllib.parse import parse_qsl, unquote, urlencode
from multidict import CIMultiDict
from .hdrs import CONTENT_DISPOSITION, CONTENT_ENCODING, CONTENT_LENGTH, CONTENT_TRANSFER_ENCODING, CONTENT_TYPE
from .helpers import CHAR, PY_35, PY_352, TOKEN, parse_mimetype, reify
from .http import HttpParser
from .payload import BytesPayload, LookupError, Payload, StringPayload, get_payload, payload_type
var1485 = ('MultipartReader', 'MultipartWriter', 'BodyPartReader', 'BadContentDispositionHeader', 'BadContentDispositionParam', 'parse_content_disposition', 'content_disposition_filename')


class Class46(RuntimeWarning):
    pass


class Class55(RuntimeWarning):
    pass

def function733(arg2365):

    def function2510(arg1984):
        return (string and (TOKEN >= set(arg1984)))

    def function1018(arg2237):
        return (arg2237[0] == arg2237[(- 1)] == '"')

    def function1096(arg888):
        return (function2510(arg888) and (arg888.count("'") == 2))

    def function437(arg237):
        return arg237.endswith('*')

    def function1803(arg1681):
        var631 = (arg1681.find('*') + 1)
        if (not var631):
            return False
        var357 = (arg1681[var631:(- 1)] if arg1681.endswith('*') else arg1681[var631:])
        return var357.isdigit()

    def function1015(arg995, *, chars=''.join(map(re.escape, CHAR))):
        return re.sub('\\\\([{}])'.format(chars), '\\1', arg995)
    if (not arg2365):
        return (None, {})
    (var151, *parts) = arg2365.split(';')
    if (not function2510(var151)):
        warnings.warn(Class46(arg2365))
        return (None, {})
    var2803 = {}
    while parts:
        var4232 = parts.pop(0)
        if ('=' not in var4232):
            warnings.warn(Class46(arg2365))
            return (None, {})
        (var3613, var1742) = var4232.split('=', 1)
        var3613 = var3613.lower().strip()
        var1742 = var1742.lstrip()
        if (var3613 in var2803):
            warnings.warn(Class46(arg2365))
            return (None, {})
        if (not function2510(var3613)):
            warnings.warn(Class55(var4232))
            continue
        elif function1803(var3613):
            if function1018(var1742):
                var1742 = function1015(var1742[1:(- 1)])
            elif (not function2510(var1742)):
                warnings.warn(Class55(var4232))
                continue
        elif function437(var3613):
            if function1096(var1742):
                (var549, var785, var1742) = var1742.split("'", 2)
                var549 = (encoding or 'utf-8')
            else:
                warnings.warn(Class55(var4232))
                continue
            try:
                var1742 = unquote(var1742, var549, 'strict')
            except UnicodeDecodeError:
                warnings.warn(Class55(var4232))
                continue
        else:
            var841 = True
            if function1018(var1742):
                var841 = False
                var1742 = function1015(var1742[1:(- 1)].lstrip('\\/'))
            elif function2510(var1742):
                var841 = False
            elif parts:
                var733 = ('%s;%s' % (var1742, parts[0]))
                if function1018(var733):
                    parts.pop(0)
                    var1742 = function1015(var733[1:(- 1)].lstrip('\\/'))
                    var841 = False
            if var841:
                warnings.warn(Class46(arg2365))
                return (None, {})
        var2803[var3613] = var1742
    return (var151.lower(), var2803)

def function1583(var2803, arg1678='filename'):
    var1871 = ('%s*' % arg1678)
    if (not var2803):
        return None
    elif (var1871 in var2803):
        return var2803[var1871]
    elif (arg1678 in var2803):
        return var2803[arg1678]
    else:
        var3847 = []
        var2654 = sorted(((var3613, var1742) for (var3613, var1742) in var2803.items() if var3613.startswith(var1871)))
        for (var1913, (var3613, var1742)) in enumerate(var2654):
            (var785, var1486) = var3613.split('*', 1)
            if var1486.endswith('*'):
                var1486 = var1486[:(- 1)]
            if (var1486 == str(var1913)):
                var3847.append(var1742)
            else:
                break
        if (not var3847):
            return None
        var1742 = ''.join(var3847)
        if ("'" in var1742):
            (var549, var785, var1742) = var1742.split("'", 2)
            var549 = (encoding or 'utf-8')
            return unquote(var1742, var549, 'strict')
        return var1742


class Class151(object):
    'Wrapper around the :class:`MultipartBodyReader` to take care about\n    underlying connection and close it when it needs in.'

    def __init__(self, arg73, arg223):
        self.attribute1167 = arg73
        self.attribute999 = arg223
    if PY_35:

        def __aiter__(self):
            return self
        if (not PY_352):
            var731 = asyncio.coroutine(var731)

        @asyncio.coroutine
        def __anext__(self):
            var3999 = yield from self.function2827()
            if (var3999 is None):
                raise StopAsyncIteration
            return var3999

    def function611(self):
        'Returns ``True`` when all response data had been read.\n\n        :rtype: bool\n        '
        return self.attribute1167.content.function611()

    @asyncio.coroutine
    def function2827(self):
        'Emits next multipart reader object.'
        var4232 = yield from self.attribute999.function2827()
        if self.attribute999.function611():
            yield from self.function88()
        return var4232

    @asyncio.coroutine
    def function88(self):
        'Releases the connection gracefully, reading all the content\n        to the void.'
        yield from self.attribute1167.function88()


class Class253(object):
    'Multipart reader for single body part.'
    var3200 = 8192

    def __init__(self, arg1279, arg1073, arg2219):
        self.attribute173 = arg1073
        self.attribute1474 = arg1279
        self.attribute1224 = arg2219
        self.attribute1409 = False
        var1814 = self.arg1073.get(CONTENT_LENGTH, None)
        self.attribute357 = (int(var1814) if (var1814 is not None) else None)
        self.attribute706 = 0
        self.attribute166 = deque()
        self.attribute358 = None
        self.attribute956 = 0
        self.attribute335 = {}
    if PY_35:

        def __aiter__(self):
            return self
        if (not PY_352):
            var2537 = asyncio.coroutine(var2537)

        @asyncio.coroutine
        def __anext__(self):
            var1303 = yield from self.function2287()
            if (var1303 is None):
                raise StopAsyncIteration
            return var1303

    @asyncio.coroutine
    def function2287(self):
        var4232 = yield from self.function107()
        if (not var4232):
            return None
        return var4232

    @asyncio.coroutine
    def function107(self, *, decode=False):
        'Reads body part data.\n\n        :param bool decode: Decodes data following by encoding\n                            method from `Content-Encoding` header. If it missed\n                            data remains untouched\n\n        :rtype: bytearray\n        '
        if self.attribute1409:
            return b''
        var3940 = bytearray()
        while (not self.attribute1409):
            var3940.extend(yield from self.function567(self.var3200))
        if function1612:
            return self.function1612(var3940)
        return var3940

    @asyncio.coroutine
    def function567(self, arg1433=chunk_size):
        'Reads body part content chunk of the specified size.\n\n        :param int size: chunk size\n\n        :rtype: bytearray\n        '
        if self.attribute1409:
            return b''
        if self.attribute357:
            var2596 = yield from self.function1141(arg1433)
        else:
            var2596 = yield from self.function2862(arg1433)
        self.attribute706 += len(var2596)
        if (self.attribute706 == self.attribute357):
            self.attribute1409 = True
        if self.attribute1409:
            assert (b'\r\n' == yield from self.attribute1224.function1034()), 'reader did not read all the data or it is malformed'
        return var2596

    @asyncio.coroutine
    def function1141(self, arg780):
        'Reads body part content chunk of the specified size.\n        The body part must has `Content-Length` header with proper value.\n\n        :param int size: chunk size\n\n        :rtype: bytearray\n        '
        assert (self.attribute357 is not None), 'Content-Length required for chunked read'
        var3200 = min(arg780, (self.attribute357 - self.attribute706))
        var3597 = yield from self.attribute1224.function107(var3200)
        return var3597

    @asyncio.coroutine
    def function2862(self, arg1172):
        'Reads content chunk of body part with unknown length.\n        The `Content-Length` header for body part is not necessary.\n\n        :param int size: chunk size\n\n        :rtype: bytearray\n        '
        assert (arg1172 >= (len(self.attribute1474) + 2)), 'Chunk size must be greater or equal than boundary length + 2'
        var1823 = (self.attribute358 is None)
        if var1823:
            self.attribute358 = yield from self.attribute1224.function107(arg1172)
        var4651 = yield from self.attribute1224.function107(arg1172)
        self.attribute956 += int(self.attribute1224.function522())
        assert (self.attribute956 < 3), 'Reading after EOF'
        var3788 = (self.attribute358 + var4651)
        var3960 = (b'\r\n' + self.attribute1474)
        if var1823:
            var3494 = var3788.find(var3960)
        else:
            var3494 = var3788.find(var3960, max(0, (len(self.attribute358) - len(var3960))))
        if (var3494 >= 0):
            self.attribute1224.unread_data(var3788[var3494:])
            if (arg1172 > var3494):
                self.attribute358 = self.attribute358[:var3494]
            var4651 = var3788[len(self.attribute358):var3494]
            if (not var4651):
                self.attribute1409 = True
        var416 = self.attribute358
        self.attribute358 = var4651
        return var416

    @asyncio.coroutine
    def function1034(self):
        'Reads body part by line by line.\n\n        :rtype: bytearray\n        '
        if self.attribute1409:
            return b''
        if self.attribute166:
            var929 = self.attribute166.popleft()
        else:
            var929 = yield from self.attribute1224.function1034()
        if var929.startswith(self.attribute1474):
            var2889 = var929.rstrip(b'\r\n')
            var1595 = self.attribute1474
            var2513 = (self.attribute1474 + b'--')
            if ((var2889 == var1595) or (var2889 == var2513)):
                self.attribute1409 = True
                self.attribute166.append(var929)
                return b''
        else:
            var4549 = yield from self.attribute1224.function1034()
            if var4549.startswith(self.attribute1474):
                var929 = var929[:(- 2)]
            self.attribute166.append(var4549)
        return var929

    @asyncio.coroutine
    def function1834(self):
        'Like :meth:`read`, but reads all the data to the void.\n\n        :rtype: None\n        '
        if self.attribute1409:
            return
        while (not self.attribute1409):
            yield from self.function567(self.var3200)

    @asyncio.coroutine
    def function577(self, *, encoding=None):
        'Like :meth:`read`, but assumes that body part contains text data.\n\n        :param str encoding: Custom text encoding. Overrides specified\n                             in charset param of `Content-Type` header\n\n        :rtype: str\n        '
        var2912 = yield from self.function107(decode=True)
        var549 = (encoding or self.function1288(default='utf-8'))
        return var2912.function1612(var549)

    @asyncio.coroutine
    def function615(self, *, encoding=None):
        'Like :meth:`read`, but assumes that body parts contains JSON data.\n\n        :param str encoding: Custom JSON encoding. Overrides specified\n                             in charset param of `Content-Type` header\n        '
        var3002 = yield from self.function107(decode=True)
        if (not var3002):
            return None
        var549 = (encoding or self.function1288(default='utf-8'))
        return function615.loads(var3002.function1612(var549))

    @asyncio.coroutine
    def function735(self, *, encoding=None):
        'Like :meth:`read`, but assumes that body parts contains form\n        urlencoded data.\n\n        :param str encoding: Custom form encoding. Overrides specified\n                             in charset param of `Content-Type` header\n        '
        var208 = yield from self.function107(decode=True)
        if (not var208):
            return None
        var549 = (encoding or self.function1288(default='utf-8'))
        return parse_qsl(var208.rstrip().function1612(var549), keep_blank_values=True, encoding=var549)

    def function522(self):
        'Returns ``True`` if the boundary was reached or\n        ``False`` otherwise.\n\n        :rtype: bool\n        '
        return self.attribute1409

    def function1612(self, arg1490):
        'Decodes data according the specified `Content-Encoding`\n        or `Content-Transfer-Encoding` headers value.\n\n        Supports ``gzip``, ``deflate`` and ``identity`` encodings for\n        `Content-Encoding` header.\n\n        Supports ``base64``, ``quoted-printable``, ``binary`` encodings for\n        `Content-Transfer-Encoding` header.\n\n        :param bytearray data: Data to decode.\n\n        :raises: :exc:`RuntimeError` - if encoding is unknown.\n\n        :rtype: bytes\n        '
        if (CONTENT_TRANSFER_ENCODING in self.attribute173):
            arg1490 = self.function953(arg1490)
        if (CONTENT_ENCODING in self.attribute173):
            return self.function1362(arg1490)
        return arg1490

    def function1362(self, arg355):
        var549 = self.attribute173[CONTENT_ENCODING].lower()
        if (var549 == 'deflate'):
            return zlib.decompress(arg355, (- zlib.MAX_WBITS))
        elif (var549 == 'gzip'):
            return zlib.decompress(arg355, (16 + zlib.MAX_WBITS))
        elif (var549 == 'identity'):
            return arg355
        else:
            raise RuntimeError('unknown content encoding: {}'.format(var549))

    def function953(self, arg1016):
        var549 = self.attribute173[CONTENT_TRANSFER_ENCODING].lower()
        if (var549 == 'base64'):
            return base64.b64decode(arg1016)
        elif (var549 == 'quoted-printable'):
            return binascii.a2b_qp(arg1016)
        elif (var549 in ('binary', '8bit', '7bit')):
            return arg1016
        else:
            raise RuntimeError('unknown content transfer encoding: {}'.format(var549))

    def function1288(self, arg2226=None):
        'Returns charset parameter from ``Content-Type`` header or default.\n        '
        var49 = self.attribute173.get(CONTENT_TYPE, '')
        (*var785, var2803) = parse_mimetype(var49)
        return var2803.get('charset', arg2226)

    @reify
    def function1777(self):
        'Returns filename specified in Content-Disposition header or ``None``\n        if missed or header is malformed.'
        (var785, var2803) = function733(self.attribute173.get(CONTENT_DISPOSITION))
        return function1583(var2803, 'name')

    @reify
    def function1007(self):
        'Returns filename specified in Content-Disposition header or ``None``\n        if missed or header is malformed.'
        (var785, var2803) = function733(self.attribute173.get(CONTENT_DISPOSITION))
        return function1583(var2803, 'filename')


@payload_type(Class253)
class Class290(Payload):

    def __init__(self, var1742, *args, **kwargs):
        super().__init__(var1742, *args, None=kwargs)
        var2803 = {}
        if (var1742.name is not None):
            var2803['name'] = var1742.name
        if (var1742.filename is not None):
            var2803['filename'] = var1742.name
        if var2803:
            self.set_content_disposition('attachment', None=var2803)

    @asyncio.coroutine
    def function2252(self, arg899):
        var1029 = self._value
        var3208 = yield from var1029.read_chunk(size=(2 ** 16))
        while chunk:
            arg899.function2252(var1029.decode(var3208))
            var3208 = yield from var1029.read_chunk(size=(2 ** 16))


class Class172(object):
    'Multipart body reader.'
    var3097 = Class151
    var4456 = None
    var2604 = Class253

    def __init__(self, arg464, arg1286):
        self.attribute654 = arg464
        self.attribute954 = ('--' + self.function770()).encode()
        self.attribute1130 = arg1286
        self.attribute95 = None
        self.attribute884 = False
        self.attribute2384 = True
        self.attribute144 = []
    if PY_35:

        def __aiter__(self):
            return self
        if (not PY_352):
            var2698 = asyncio.coroutine(var2698)

        @asyncio.coroutine
        def __anext__(self):
            var2718 = yield from self.function605()
            if (var2718 is None):
                raise StopAsyncIteration
            return var2718

    @classmethod
    def function779(arg1829, arg2093):
        'Constructs reader instance from HTTP response.\n\n        :param response: :class:`~aiohttp.client.ClientResponse` instance\n        '
        var3472 = arg1829.var3097(arg2093, arg1829(arg2093.headers, arg2093.content))
        return var3472

    def function800(self):
        'Returns ``True`` if the final boundary was reached or\n        ``False`` otherwise.\n\n        :rtype: bool\n        '
        return self.attribute884

    @asyncio.coroutine
    def function605(self):
        'Emits the next multipart body part.'
        if self.attribute884:
            return
        yield from self.function1735()
        if self.attribute2384:
            yield from self.function315()
            self.attribute2384 = False
        else:
            yield from self.function701()
        if self.attribute884:
            return
        self.attribute95 = yield from self.function1462()
        return self.attribute95

    @asyncio.coroutine
    def function1880(self):
        'Reads all the body parts to the void till the final boundary.'
        while (not self.attribute884):
            var4232 = yield from self.function605()
            if (var4232 is None):
                break
            yield from var4232.function1880()

    @asyncio.coroutine
    def function1462(self):
        'Returns the next body part reader.'
        var4668 = yield from self.function839()
        return self.function2582(var4668)

    def function2582(self, arg251):
        'Dispatches the response by the `Content-Type` header, returning\n        suitable reader instance.\n\n        :param dict headers: Response headers\n        '
        var988 = arg251.get(CONTENT_TYPE, '')
        (var4372, *var785) = parse_mimetype(var988)
        if (var4372 == 'multipart'):
            if (self.var4456 is None):
                return type(self)(arg251, self.attribute1130)
            return self.var4456(arg251, self.attribute1130)
        else:
            return self.var2604(self.attribute954, arg251, self.attribute1130)

    def function770(self):
        (var1371, *var785, var2803) = parse_mimetype(self.attribute654[CONTENT_TYPE])
        assert (var1371 == 'multipart'), 'multipart/* content type expected'
        if ('boundary' not in var2803):
            raise ValueError(('boundary missed for Content-Type: %s' % self.attribute654[CONTENT_TYPE]))
        var2444 = var2803['boundary']
        if (len(var2444) > 70):
            raise ValueError(('boundary %r is too long (70 chars max)' % var2444))
        return var2444

    @asyncio.coroutine
    def function1546(self):
        if self.attribute144:
            return self.attribute144.pop()
        return yield from self.attribute1130.readline()

    @asyncio.coroutine
    def function315(self):
        while True:
            var3842 = yield from self.function1546()
            if (var3842 == b''):
                raise ValueError(('Could not find starting boundary %r' % self.attribute954))
            var3842 = var3842.rstrip()
            if (var3842 == self.attribute954):
                return
            elif (var3842 == (self.attribute954 + b'--')):
                self.attribute884 = True
                return

    @asyncio.coroutine
    def function701(self):
        var2891 = yield from self.function1546().rstrip()
        if (var2891 == self.attribute954):
            pass
        elif (var2891 == (self.attribute954 + b'--')):
            self.attribute884 = True
            var3895 = yield from self.function1546()
            var2722 = yield from self.function1546()
            if (var2722[:2] == b'--'):
                self.attribute144.append(var2722)
            else:
                self.attribute144.extend([var2722, var3895])
        else:
            raise ValueError(('Invalid boundary %r, expected %r' % (var2891, self.attribute954)))

    @asyncio.coroutine
    def function839(self):
        var2854 = [b'']
        while True:
            var3783 = yield from self.attribute1130.readline()
            var3783 = var3783.strip()
            var2854.append(var3783)
            if (not var3783):
                break
        var3682 = HttpParser()
        (var3749, *var785) = var3682.parse_headers(var2854)
        return var3749

    @asyncio.coroutine
    def function1735(self):
        'Ensures that the last read body part is read completely.'
        if (self.attribute95 is not None):
            if (not self.attribute95.function800()):
                yield from self.attribute95.function1880()
            self.attribute144.extend(self.attribute95._unread)
            self.attribute95 = None


class Class81(Payload):
    'Multipart body writer.'

    def __init__(self, arg1321='mixed', arg2276=None):
        arg2276 = (arg2276 if (arg2276 is not None) else uuid.uuid4().hex)
        try:
            self.attribute1559 = arg2276.encode('us-ascii')
        except UnicodeEncodeError:
            raise ValueError('boundary should contains ASCII only chars')
        var2765 = 'multipart/{}; boundary="{}"'.format(arg1321, arg2276)
        super().__init__(None, content_type=var2765)
        self.attribute1736 = []
        self.attribute1677 = CIMultiDict()
        self.attribute1677[CONTENT_TYPE] = self.content_type

    def __enter__(self):
        return self

    def __exit__(self, arg970, arg1090, arg2074):
        pass

    def __iter__(self):
        return iter(self.attribute1736)

    def __len__(self):
        return len(self.attribute1736)

    @property
    def arg2276(self):
        return self.attribute1559

    def function1601(self, arg1096, arg1514=None):
        if (arg1514 is None):
            arg1514 = CIMultiDict()
        if isinstance(arg1096, Payload):
            if (arg1096.arg1514 is not None):
                arg1096.arg1514.update(arg1514)
            else:
                arg1096._headers = arg1514
            self.function2463(arg1096)
        else:
            try:
                self.function2463(get_payload(arg1096, headers=arg1514))
            except LookupError:
                raise TypeError

    def function2463(self, arg1480):
        'Adds a new body part to multipart writer.'
        if (CONTENT_TYPE not in arg1480.arg1514):
            arg1480.arg1514[CONTENT_TYPE] = arg1480.content_type
        var549 = arg1480.arg1514.get(CONTENT_ENCODING, '').lower()
        if (encoding and (var549 not in ('deflate', 'gzip', 'identity'))):
            raise RuntimeError('unknown content encoding: {}'.format(var549))
        if (var549 == 'identity'):
            var549 = None
        var279 = arg1480.arg1514.get(CONTENT_TRANSFER_ENCODING, '').lower()
        if (var279 not in ('', 'base64', 'quoted-printable', 'binary')):
            raise RuntimeError('unknown content transfer encoding: {}'.format(var279))
        if (var279 == 'binary'):
            var279 = None
        var2719 = arg1480.var2719
        if ((var2719 is not None) and (not (encoding or te_encoding))):
            arg1480.arg1514[CONTENT_LENGTH] = str(var2719)
        arg1514 = (''.join([(((var4218 + ': ') + var3992) + '\r\n') for (var4218, var3992) in arg1480.arg1514.items()]).encode('utf-8') + b'\r\n')
        self.attribute1736.function1601((arg1480, arg1514, var549, var279))

    def function2872(self, arg1096, arg1514=None):
        'Helper to append JSON part.'
        if (arg1514 is None):
            arg1514 = CIMultiDict()
        var2874 = json.dumps(arg1096).encode('utf-8')
        self.function2463(BytesPayload(var2874, headers=arg1514, content_type='application/json'))

    def function399(self, arg1096, arg1514=None):
        'Helper to append form urlencoded part.'
        assert isinstance(arg1096, (Sequence, Mapping))
        if (arg1514 is None):
            arg1514 = CIMultiDict()
        if isinstance(arg1096, Mapping):
            arg1096 = list(arg1096.items())
        var939 = urlencode(arg1096, doseq=True)
        return self.function2463(StringPayload(var939, headers=arg1514, content_type='application/x-www-form-urlencoded'))

    @property
    def function186(self):
        'Size of the payload.'
        if (not self.attribute1736):
            return 0
        var2704 = 0
        for (var2587, arg1514, var549, var3873) in self.attribute1736:
            if (encoding or te_encoding or (var2587.function186 is None)):
                return None
            var2704 += (((((2 + len(self.attribute1559)) + 2) + var2587.function186) + len(arg1514)) + 2)
        var2704 += ((2 + len(self.attribute1559)) + 4)
        return var2704

    @asyncio.coroutine
    def function1333(self, arg2389):
        'Write body.'
        if (not self.attribute1736):
            return
        for (var3123, arg1514, var549, var1845) in self.attribute1736:
            yield from arg2389.function1333(((b'--' + self.attribute1559) + b'\r\n'))
            yield from arg2389.function1333(arg1514)
            if (encoding or te_encoding):
                var793 = Class326(arg2389)
                if var549:
                    var793.enable_compression(var549)
                if var1845:
                    var793.enable_encoding(var1845)
                yield from var3123.function1333(var793)
                yield from var793.write_eof()
            else:
                yield from var3123.function1333(arg2389)
            yield from arg2389.function1333(b'\r\n')
        yield from arg2389.function1333(((b'--' + self.attribute1559) + b'--\r\n'))


class Class326:

    def __init__(self, arg788):
        self.attribute1595 = arg788
        self.attribute1374 = None
        self.attribute574 = None

    def function1848(self, var549):
        if (var549 == 'base64'):
            self.attribute1374 = var549
            self.attribute1311 = bytearray()
        elif (var549 == 'quoted-printable'):
            self.attribute1374 = 'quoted-printable'

    def function280(self, var549='deflate'):
        var3748 = ((16 + zlib.MAX_WBITS) if (var549 == 'gzip') else (- zlib.MAX_WBITS))
        self.attribute574 = zlib.compressobj(wbits=var3748)

    @asyncio.coroutine
    def function72(self):
        if (self.attribute574 is not None):
            var1388 = self.attribute574.flush()
            if var1388:
                self.attribute574 = None
                yield from self.function1089(var1388)
        if (self.attribute1374 == 'base64'):
            if self.attribute1311:
                yield from self.attribute1595.function1089(base64.b64encode(self.attribute1311))

    @asyncio.coroutine
    def function1089(self, arg2191):
        if (self.attribute574 is not None):
            if arg2191:
                arg2191 = self.attribute574.compress(arg2191)
                if (not arg2191):
                    return
        if (self.attribute1374 == 'base64'):
            self.attribute1311.extend(arg2191)
            if self.attribute1311:
                var1362 = self.attribute1311
                (var2413, var2126) = divmod(len(var1362), 3)
                (var1180, self.attribute1311) = (var1362[:(var2413 * 3)], var1362[(var2413 * 3):])
                if var1180:
                    var1180 = base64.b64encode(var1180)
                    yield from self.attribute1595.function1089(var1180)
        elif (self.attribute1374 == 'quoted-printable'):
            yield from self.attribute1595.function1089(binascii.b2a_qp(arg2191))
        else:
            yield from self.attribute1595.function1089(arg2191)