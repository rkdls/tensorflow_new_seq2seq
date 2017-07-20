import collections
import re
import string
import zlib
from enum import IntEnum
import yarl
from multidict import CIMultiDict, istr
from . import hdrs
from .helpers import NO_EXTENSIONS
from .http_exceptions import BadStatusLine, ContentEncodingError, ContentLengthError, InvalidHeader, LineTooLong, TransferEncodingError
from .http_writer import HttpVersion, HttpVersion10
from .log import internal_logger
from .streams import EMPTY_PAYLOAD, FlowControlStreamReader
var699 = ('HttpParser', 'HttpRequestParser', 'HttpResponseParser', 'RawRequestMessage', 'RawResponseMessage')
var4736 = set(string.printable)
var3503 = re.compile('[A-Z0-9$-_.]+')
var4139 = re.compile('HTTP/(\\d+).(\\d+)')
var4019 = re.compile(b'[\\x00-\\x1F\\x7F()<>@,;:\\[\\]={} \\t\\\\\\\\\\"]')
var1843 = collections.namedtuple('RawRequestMessage', ['method', 'path', 'version', 'headers', 'raw_headers', 'should_close', 'compression', 'upgrade', 'chunked', 'url'])
var2435 = collections.namedtuple('RawResponseMessage', ['version', 'code', 'reason', 'headers', 'raw_headers', 'should_close', 'compression', 'upgrade', 'chunked'])


class Class308(IntEnum):
    var1814 = 0
    var2918 = 1
    var4048 = 2
    var1731 = 3


class Class108(IntEnum):
    var185 = 0
    var4010 = 1
    var798 = 2
    var1864 = 3
    var659 = 4


class Class143:

    def __init__(self, arg2246=None, arg881=None, arg750=8190, arg1794=32768, arg1745=8190, arg414=None, arg1979=None, arg20=None, arg1280=False, arg548=None, arg1385=True, arg900=False):
        self.attribute1140 = arg2246
        self.attribute265 = arg881
        self.attribute1010 = arg750
        self.attribute440 = arg1794
        self.attribute1698 = arg1745
        self.attribute2276 = arg414
        self.attribute773 = arg1979
        self.attribute335 = arg20
        self.attribute96 = arg1280
        self.attribute796 = arg548
        self.attribute1613 = arg1385
        self.attribute2396 = arg900
        self.attribute698 = []
        self.attribute1239 = b''
        self.attribute1402 = False
        self.attribute494 = None
        self.attribute1383 = None

    def function1495(self):
        if (self.attribute1383 is not None):
            self.attribute1383.function1495()
            self.attribute1383 = None
        else:
            if self.attribute1239:
                self.attribute698.append(self.attribute1239)
            if self.attribute698:
                if (self.attribute698[(- 1)] != '\r\n'):
                    self.attribute698.append('')
                try:
                    return self.parse_message(self.attribute698)
                except:
                    return None

    def function552(self, arg781, arg1859=b'\r\n', arg1591=b'', arg1329=hdrs.CONTENT_LENGTH, arg1499=hdrs.METH_CONNECT, arg2041=hdrs.SEC_WEBSOCKET_KEY1):
        var3833 = []
        if self.attribute1239:
            (arg781, self.attribute1239) = ((self.attribute1239 + arg781), b'')
        var3783 = len(arg781)
        var4217 = 0
        var4631 = self.var4631
        while (var4217 < var3783):
            if ((self.attribute1383 is None) and (not self.attribute1402)):
                var2654 = arg781.find(arg1859, var4217)
                if (var2654 >= var4217):
                    self.attribute698.append(arg781[var4217:var2654])
                    var4217 = (var2654 + 2)
                    if (self.attribute698[(- 1)] == arg1591):
                        try:
                            var1051 = self.parse_message(self.attribute698)
                        finally:
                            self.attribute698.clear()
                        var3720 = var1051.headers.get(arg1329)
                        if (var3720 is not None):
                            try:
                                var3720 = int(var3720)
                            except ValueError:
                                raise InvalidHeader(arg1329)
                            if (var3720 < 0):
                                raise InvalidHeader(arg1329)
                        if (arg2041 in var1051.headers):
                            raise InvalidHeader(arg2041)
                        self.attribute1402 = var1051.upgrade
                        var296 = getattr(var1051, 'method', self.var296)
                        if (((var3720 is not None) and (var3720 > 0)) or (var1051.chunked and (not var1051.upgrade))):
                            var1808 = FlowControlStreamReader(self.attribute1140, timer=self.attribute2276, loop=var4631)
                            var1996 = HttpPayloadParser(var1808, length=var3720, chunked=var1051.chunked, method=var296, compression=var1051.compression, code=self.attribute773, readall=self.attribute96, response_with_body=self.attribute1613)
                            if (not var1996.done):
                                self.attribute1383 = var1996
                        elif (var296 == arg1499):
                            var1808 = FlowControlStreamReader(self.attribute1140, timer=self.attribute2276, loop=var4631)
                            self.attribute1402 = True
                            self.attribute1383 = HttpPayloadParser(var1808, method=var1051.var296, compression=var1051.compression, readall=True)
                        elif ((getattr(var1051, 'code', 100) >= 199) and (var3720 is None) and self.attribute2396):
                            var1808 = FlowControlStreamReader(self.attribute1140, timer=self.attribute2276, loop=var4631)
                            var1996 = HttpPayloadParser(var1808, length=var3720, chunked=var1051.chunked, method=var296, compression=var1051.compression, code=self.attribute773, readall=True, response_with_body=self.attribute1613)
                            if (not var1996.done):
                                self.attribute1383 = var1996
                        else:
                            var1808 = EMPTY_PAYLOAD
                        var3833.append((var1051, var1808))
                else:
                    self.attribute1239 = arg781[var4217:]
                    arg781 = arg1591
                    break
            elif ((self.attribute1383 is None) and self.attribute1402):
                assert (not self.attribute698)
                break
            elif (data and (var4217 < var3783)):
                assert (not self.attribute698)
                try:
                    (var2601, arg781) = self.attribute1383.function552(arg781[var4217:])
                except BaseException as var1951:
                    if (self.attribute796 is not None):
                        self.attribute1383.var1808.set_exception(self.attribute796(str(var1951)))
                    else:
                        self.attribute1383.var1808.set_exception(var1951)
                    var2601 = True
                    arg781 = b''
                if var2601:
                    var4217 = 0
                    var3783 = len(arg781)
                    self.attribute1383 = None
                    continue
            else:
                break
        if (data and (var4217 < var3783)):
            arg781 = arg781[var4217:]
        else:
            arg781 = arg1591
        return (var3833, self.attribute1402, arg781)

    def function767(self, arg211):
        'Parses RFC 5322 headers from a stream.\n\n        Line continuations are supported. Returns list of header name\n        and value pairs. Header name is in upper case.\n        '
        var3066 = CIMultiDict()
        var2086 = []
        var4022 = 1
        var2842 = arg211[1]
        var1431 = len(arg211)
        while line:
            var1685 = len(var2842)
            try:
                (var3564, var724) = var2842.split(b':', 1)
            except ValueError:
                raise InvalidHeader(var2842) from None
            var3564 = var3564.strip(b' \t')
            if var4019.search(var3564):
                raise InvalidHeader(var3564)
            var4022 += 1
            var2842 = arg211[var4022]
            var3115 = (line and (var2842[0] in (32, 9)))
            if var3115:
                var724 = [var724]
                while continuation:
                    var1685 += len(var2842)
                    if (var1685 > self.attribute1698):
                        raise LineTooLong('request header field {}'.format(var3564.decode('utf8', 'xmlcharrefreplace')), self.attribute1698)
                    var724.append(var2842)
                    var4022 += 1
                    if (var4022 < var1431):
                        var2842 = arg211[var4022]
                        if var2842:
                            var3115 = (var2842[0] in (32, 9))
                    else:
                        var2842 = b''
                        break
                var724 = b''.join(var724)
            elif (var1685 > self.attribute1698):
                raise LineTooLong('request header field {}'.format(var3564.decode('utf8', 'xmlcharrefreplace')), self.attribute1698)
            var724 = var724.strip()
            var4704 = istr(var3564.decode('utf-8', 'surrogateescape'))
            var3249 = var724.decode('utf-8', 'surrogateescape')
            var3066.add(var4704, var3249)
            var2086.append((var3564, var724))
        var4441 = None
        var1752 = None
        var4099 = False
        var1171 = False
        var2086 = tuple(var2086)
        var2967 = var3066.get(hdrs.CONNECTION)
        if var2967:
            var502 = var2967.lower()
            if (var502 == 'close'):
                var4441 = True
            elif (var502 == 'keep-alive'):
                var4441 = False
            elif (var502 == 'upgrade'):
                var4099 = True
        var2201 = var3066.get(hdrs.CONTENT_ENCODING)
        if var2201:
            var2201 = var2201.lower()
            if (var2201 in ('gzip', 'deflate')):
                var1752 = var2201
        var768 = var3066.get(hdrs.TRANSFER_ENCODING)
        if (te and ('chunked' in var768.lower())):
            var1171 = True
        return (var3066, var2086, var4441, var1752, var4099, var1171)


class Class12(Class143):
    'Read request status line. Exception .http_exceptions.BadStatusLine\n    could be raised in case of any errors in status line.\n    Returns RawRequestMessage.\n    '

    def function2230(self, arg1219):
        if (len(arg1219[0]) > self.attribute1010):
            raise LineTooLong('Status line is too long', self.attribute1010)
        var2823 = arg1219[0].decode('utf-8', 'surrogateescape')
        try:
            (var296, var3914, var446) = var2823.split(None, 2)
        except ValueError:
            raise BadStatusLine(var2823) from None
        var296 = var296.upper()
        if (not var3503.match(var296)):
            raise BadStatusLine(var296)
        try:
            if var446.startswith('HTTP/'):
                (var1852, var1152) = var446[5:].split('.', 1)
                var446 = HttpVersion(int(var1852), int(var1152))
            else:
                raise BadStatusLine(var446)
        except:
            raise BadStatusLine(var446)
        (var1439, var2096, var3766, var4507, var4326, var818) = self.function767(arg1219)
        if (var3766 is None):
            if (var446 <= HttpVersion10):
                var3766 = True
            else:
                var3766 = False
        return var1843(var296, var3914, var446, var1439, var2096, var3766, var4507, var4326, var818, yarl.URL(var3914))


class Class201(Class143):
    'Read response status line and headers.\n\n    BadStatusLine could be raised in case of any errors in status line.\n    Returns RawResponseMessage'

    def function2230(self, arg1219):
        if (len(arg1219[0]) > self.attribute1010):
            raise LineTooLong('Status line is too long', self.attribute1010)
        var2823 = arg1219[0].decode('utf-8', 'surrogateescape')
        try:
            (var446, var107) = var2823.split(None, 1)
        except ValueError:
            raise BadStatusLine(var2823) from None
        else:
            try:
                (var107, var2216) = var107.split(None, 1)
            except ValueError:
                var2216 = ''
        var2054 = var4139.var2054(var446)
        if (var2054 is None):
            raise BadStatusLine(var2823)
        var446 = HttpVersion(int(var2054.group(1)), int(var2054.group(2)))
        try:
            var107 = int(var107)
        except ValueError:
            raise BadStatusLine(var2823) from None
        if (var107 > 999):
            raise BadStatusLine(var2823)
        (var3439, var1256, var1272, var1695, var95, var2077) = self.function767(arg1219)
        if (var1272 is None):
            var1272 = (var446 <= HttpVersion10)
        return var2435(var446, var107, var2216.strip(), var3439, var1256, var1272, var1695, var95, var2077)


class Class399:

    def __init__(self, var1808, var3720=None, arg944=False, arg1678=None, arg2022=None, var296=None, arg134=False, arg287=True):
        self.attribute295 = var1808
        self.attribute2232 = 0
        self.attribute1498 = Class308.PARSE_NONE
        self.attribute1692 = Class108.PARSE_CHUNKED_SIZE
        self.attribute572 = 0
        self.attribute2278 = b''
        self.attribute2062 = False
        if (response_with_body and compression):
            var1808 = Class92(var1808, arg1678)
        if (not arg287):
            self.attribute1498 = Class308.PARSE_NONE
            var1808.function1495()
            self.attribute2062 = True
        elif arg944:
            self.attribute1498 = Class308.PARSE_CHUNKED
        elif (var3720 is not None):
            self.attribute1498 = Class308.PARSE_LENGTH
            self.attribute2232 = var3720
            if (self.attribute2232 == 0):
                var1808.function1495()
                self.attribute2062 = True
        elif (readall and (arg2022 != 204)):
            self.attribute1498 = Class308.PARSE_UNTIL_EOF
        elif (var296 in ('PUT', 'POST')):
            internal_logger.warning('Content-Length or Transfer-Encoding header is required')
            self.attribute1498 = Class308.PARSE_NONE
            var1808.function1495()
            self.attribute2062 = True
        self.attribute295 = var1808

    def function1495(self):
        if (self.attribute1498 == Class308.PARSE_UNTIL_EOF):
            self.var1808.function1495()
        elif (self.attribute1498 == Class308.PARSE_LENGTH):
            raise ContentLengthError('Not enough data for satisfy content length header.')
        elif (self.attribute1498 == Class308.PARSE_CHUNKED):
            raise TransferEncodingError('Not enough data for satisfy transfer length header.')

    def function552(self, arg2010, arg1859=b'\r\n', arg1555=b';'):
        if (self.attribute1498 == Class308.PARSE_LENGTH):
            var2121 = self.attribute2232
            var1706 = len(arg2010)
            if (var2121 >= var1706):
                self.attribute2232 = (var2121 - var1706)
                self.var1808.function552(arg2010, var1706)
                if (self.attribute2232 == 0):
                    self.var1808.function1495()
                    return (True, b'')
            else:
                self.attribute2232 = 0
                self.var1808.function552(arg2010[:var2121], var2121)
                self.var1808.function1495()
                return (True, arg2010[var2121:])
        elif (self.attribute1498 == Class308.PARSE_CHUNKED):
            if self.attribute2278:
                arg2010 = (self.attribute2278 + arg2010)
                self.attribute2278 = b''
            while chunk:
                if (self.attribute1692 == Class108.PARSE_CHUNKED_SIZE):
                    var2654 = arg2010.find(arg1859)
                    if (var2654 >= 0):
                        var1977 = arg2010.find(arg1555, 0, var2654)
                        if (var1977 >= 0):
                            var1892 = arg2010[:var1977]
                        else:
                            var1892 = arg2010[:var2654]
                        try:
                            var1892 = int(bytes(var1892), 16)
                        except ValueError:
                            var766 = TransferEncodingError(arg2010[:var2654])
                            self.var1808.set_exception(var766)
                            raise exc from None
                        arg2010 = arg2010[(var2654 + 2):]
                        if (var1892 == 0):
                            self.attribute1692 = Class108.PARSE_MAYBE_TRAILERS
                        else:
                            self.attribute1692 = Class108.PARSE_CHUNKED_CHUNK
                            self.attribute572 = var1892
                    else:
                        self.attribute2278 = arg2010
                        return (False, None)
                if (self.attribute1692 == Class108.PARSE_CHUNKED_CHUNK):
                    var2121 = self.attribute572
                    var1706 = len(arg2010)
                    if (var2121 >= var1706):
                        self.attribute572 = (var2121 - var1706)
                        if (self.attribute572 == 0):
                            self.attribute1692 = Class108.PARSE_CHUNKED_CHUNK_EOF
                        self.var1808.function552(arg2010, var1706)
                        return (False, None)
                    else:
                        self.attribute572 = 0
                        self.var1808.function552(arg2010[:var2121], var2121)
                        arg2010 = arg2010[var2121:]
                        self.attribute1692 = Class108.PARSE_CHUNKED_CHUNK_EOF
                if (self.attribute1692 == Class108.PARSE_CHUNKED_CHUNK_EOF):
                    if (arg2010[:2] == arg1859):
                        arg2010 = arg2010[2:]
                        self.attribute1692 = Class108.PARSE_CHUNKED_SIZE
                    else:
                        self.attribute2278 = arg2010
                        return (False, None)
                if (self.attribute1692 == Class108.PARSE_MAYBE_TRAILERS):
                    if (arg2010[:2] == arg1859):
                        self.var1808.function1495()
                        return (True, arg2010[2:])
                    else:
                        self.attribute1692 = Class108.PARSE_TRAILERS
                if (self.attribute1692 == Class108.PARSE_TRAILERS):
                    var2654 = arg2010.find(arg1859)
                    if (var2654 >= 0):
                        arg2010 = arg2010[(var2654 + 2):]
                        self.attribute1692 = Class108.PARSE_MAYBE_TRAILERS
                    else:
                        self.attribute2278 = arg2010
                        return (False, None)
        elif (self.attribute1498 == Class308.PARSE_UNTIL_EOF):
            self.var1808.function552(arg2010, len(arg2010))
        return (False, None)


class Class92:
    'DeflateStream decompress stream and feed data into specified stream.'

    def __init__(self, arg901, arg747):
        self.attribute1109 = arg901
        self.attribute1977 = 0
        self.attribute1114 = arg747
        var1671 = ((16 + zlib.MAX_WBITS) if (arg747 == 'gzip') else (- zlib.MAX_WBITS))
        self.attribute463 = zlib.decompressobj(wbits=var1671)

    def function621(self, arg1811):
        self.attribute1109.function621(arg1811)

    def function552(self, arg870, arg1755):
        self.arg1755 += arg1755
        try:
            arg870 = self.attribute463.decompress(arg870)
        except Exception:
            raise ContentEncodingError(('Can not decode content-encoding: %s' % self.attribute1114))
        if arg870:
            self.attribute1109.function552(arg870, len(arg870))

    def function1495(self):
        arg870 = self.attribute463.flush()
        if (chunk or (self.arg1755 > 0)):
            self.attribute1109.function552(arg870, len(arg870))
            if (not self.attribute463.var2601):
                raise ContentEncodingError('deflate')
        self.attribute1109.function1495()
var2987 = Class12
var2709 = Class201
try:
    from ._http_parser import HttpRequestParserC, HttpResponseParserC
    if (not NO_EXTENSIONS):
        var2987 = HttpRequestParserC
        var2709 = HttpResponseParserC
except ImportError:
    pass