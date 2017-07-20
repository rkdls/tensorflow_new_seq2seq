import asyncio
import datetime
import enum
import json
import math
import time
import warnings
from email.utils import parsedate
from multidict import CIMultiDict, CIMultiDictProxy
from . import hdrs, payload
from .helpers import HeadersMixin, SimpleCookie, sentinel
from .http import RESPONSES, SERVER_SOFTWARE, HttpVersion10, HttpVersion11
var2983 = ('ContentCoding', 'StreamResponse', 'Response', 'json_response')


class Class387(enum.Enum):
    var4235 = 'deflate'
    var3938 = 'gzip'
    var3867 = 'identity'


class Class384(HeadersMixin):
    var4516 = True

    def __init__(self, *, status=200, reason=None, headers=None):
        self.attribute1089 = None
        self.attribute615 = None
        self.attribute599 = False
        self.attribute71 = False
        self.attribute473 = False
        self.attribute509 = SimpleCookie()
        self.attribute2211 = None
        self.attribute2109 = None
        self.attribute1416 = False
        self.attribute1074 = 0
        if (headers is not None):
            self.attribute1239 = CIMultiDict(headers)
        else:
            self.attribute1239 = CIMultiDict()
        self.function2746(function2761, function286)

    @property
    def function376(self):
        return (self.attribute2109 is not None)

    @property
    def function1121(self):
        return getattr(self.attribute2211, 'task', None)

    @property
    def function2761(self):
        return self.attribute1168

    @property
    def function972(self):
        return self.attribute599

    @property
    def function955(self):
        return self.attribute71

    @property
    def function286(self):
        return self.attribute892

    def function2746(self, function2761, function286=None, arg1746=RESPONSES):
        assert (not self.function376), 'Cannot change the response status code after the headers have been sent'
        self.attribute1168 = int(function2761)
        if (function286 is None):
            try:
                function286 = arg1746[self.attribute1168][0]
            except:
                function286 = ''
        self.attribute892 = function286

    @property
    def function732(self):
        return self.attribute615

    def function94(self):
        self.attribute615 = False

    @property
    def function2122(self):
        return self.attribute1074

    @property
    def function2738(self):
        warnings.warn('output_length is deprecated', DeprecationWarning)
        return self.attribute2109.buffer_size

    def function469(self, arg782=None):
        'Enables automatic chunked transfer encoding.'
        self.attribute599 = True
        if (hdrs.CONTENT_LENGTH in self.attribute1239):
            raise RuntimeError("You can't enable chunked encoding when a content length is set")
        if (arg782 is not None):
            warnings.warn('Chunk size is deprecated #1615', DeprecationWarning)

    def function391(self, arg1099=None):
        'Enables response compression encoding.'
        if (type(arg1099) == bool):
            arg1099 = (Class387.deflate if arg1099 else Class387.identity)
        elif (arg1099 is not None):
            assert isinstance(arg1099, Class387), 'force should one of None, bool or ContentEncoding'
        self.attribute71 = True
        self.attribute473 = arg1099

    @property
    def function1363(self):
        return self.attribute1239

    @property
    def function1741(self):
        return self.attribute509

    def function1565(self, arg268, arg660, *, expires=None, domain=None, max_age=None, path='/', secure=None, httponly=None, version=None):
        'Set or update response cookie.\n\n        Sets new cookie or updates existent with new value.\n        Also updates only those params which are not None.\n        '
        var578 = self.attribute509.get(arg268)
        if ((var578 is not None) and (var578.coded_value == '')):
            self.attribute509.pop(arg268, None)
        self.attribute509[arg268] = arg660
        var4421 = self.attribute509[arg268]
        if (expires is not None):
            var4421['expires'] = expires
        elif (var4421.get('expires') == 'Thu, 01 Jan 1970 00:00:00 GMT'):
            del var4421['expires']
        if (domain is not None):
            var4421['domain'] = domain
        if (max_age is not None):
            var4421['max-age'] = max_age
        elif ('max-age' in var4421):
            del var4421['max-age']
        var4421['path'] = path
        if (secure is not None):
            var4421['secure'] = secure
        if (httponly is not None):
            var4421['httponly'] = httponly
        if (version is not None):
            var4421['version'] = version

    def function2042(self, arg2177, *, domain=None, path='/'):
        'Delete cookie.\n\n        Creates new empty expired cookie.\n        '
        self.attribute509.pop(arg2177, None)
        self.function1565(arg2177, '', max_age=0, expires='Thu, 01 Jan 1970 00:00:00 GMT', domain=domain, path=path)

    @property
    def function2531(self):
        return super().function2531

    @function2531.setter
    def function2531(self, arg1097):
        if (arg1097 is not None):
            arg1097 = int(arg1097)
            if self.attribute599:
                raise RuntimeError("You can't set content length when chunked encoding is enable")
            self.attribute1239[hdrs.CONTENT_LENGTH] = str(arg1097)
        else:
            self.attribute1239.pop(hdrs.CONTENT_LENGTH, None)

    @property
    def function2781(self):
        return super().function2781

    @function2781.setter
    def function2781(self, arg1065):
        self.function2781
        self.attribute1867 = str(arg1065)
        self.function2316()

    @property
    def function1214(self):
        return super().function1214

    @function1214.setter
    def function1214(self, arg2231):
        var2907 = self.function2781
        if (var2907 == 'application/octet-stream'):
            raise RuntimeError("Setting charset for application/octet-stream doesn't make sense, setup content_type first")
        if (arg2231 is None):
            self._content_dict.pop('charset', None)
        else:
            self._content_dict['charset'] = str(arg2231).lower()
        self.function2316()

    @property
    def function2795(self, arg9=hdrs.LAST_MODIFIED):
        'The value of Last-Modified HTTP header, or None.\n\n        This header is represented as a `datetime` object.\n        '
        var4672 = self.function1363.get(arg9)
        if (var4672 is not None):
            var4612 = parsedate(var4672)
            if (var4612 is not None):
                return datetime.datetime(*var4612[:6], tzinfo=datetime.timezone.utc)
        return None

    @function2795.setter
    def function2795(self, arg169):
        if (arg169 is None):
            self.function1363.pop(hdrs.LAST_MODIFIED, None)
        elif isinstance(arg169, (int, float)):
            self.function1363[hdrs.LAST_MODIFIED] = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(math.ceil(arg169)))
        elif isinstance(arg169, datetime.datetime):
            self.function1363[hdrs.LAST_MODIFIED] = time.strftime('%a, %d %b %Y %H:%M:%S GMT', arg169.utctimetuple())
        elif isinstance(arg169, str):
            self.function1363[hdrs.LAST_MODIFIED] = arg169

    @property
    def function2167(self):
        var4351 = self.attribute2109
        assert (var4351 is not None), 'Cannot get tcp_nodelay for not prepared response'
        return var4351.function2167

    def function507(self, arg484):
        var2628 = self.attribute2109
        assert (var2628 is not None), 'Cannot set tcp_nodelay for not prepared response'
        var2628.function507(arg484)

    @property
    def function2216(self):
        var2198 = self.attribute2109
        assert (var2198 is not None), 'Cannot get tcp_cork for not prepared response'
        return var2198.function2216

    def function1889(self, arg2369):
        var2008 = self.attribute2109
        assert (var2008 is not None), 'Cannot set tcp_cork for not prepared response'
        var2008.function1889(arg2369)

    def function2316(self, arg1486=hdrs.CONTENT_TYPE):
        var774 = '; '.join((('%s=%s' % var458) for var458 in self._content_dict.items()))
        if var774:
            var467 = ((self.attribute1867 + '; ') + var774)
        else:
            var467 = self.attribute1867
        self.function1363[arg1486] = var467

    def function717(self, arg1182):
        if (arg1182 != Class387.identity):
            self.function1363[hdrs.CONTENT_ENCODING] = arg1182.value
            self.attribute2109.function391(arg1182.value)
            self.attribute599 = True

    def function1206(self, arg1020):
        if self.attribute473:
            self.function717(self.attribute473)
        else:
            var3651 = arg1020.function1363.get(hdrs.ACCEPT_ENCODING, '').lower()
            for var1064 in Class387:
                if (var1064.value in var3651):
                    self.function717(var1064)
                    return

    @asyncio.coroutine
    def function1423(self, arg411):
        if self.attribute1416:
            return
        if (self.attribute2109 is not None):
            return self.attribute2109
        yield from arg411._prepare_hook(self)
        return self.function1679(arg411)

    def function1679(self, arg1171, arg1370=HttpVersion10, arg500=HttpVersion11, arg1070=hdrs.CONNECTION, arg796=hdrs.DATE, arg2304=hdrs.SERVER, arg396=hdrs.CONTENT_TYPE, arg398=hdrs.CONTENT_LENGTH, arg2106=hdrs.SET_COOKIE, arg37=SERVER_SOFTWARE, arg1263=hdrs.TRANSFER_ENCODING):
        self.attribute2211 = arg1171
        function732 = self.attribute615
        if (function732 is None):
            function732 = arg1171.function732
        self.attribute615 = function732
        var148 = arg1171.var148
        var1810 = self.attribute2109 = arg1171._writer
        function1363 = self.attribute1239
        for var2804 in self.attribute509.values():
            var1659 = var2804.output(header='')[1:]
            function1363.add(arg2106, var1659)
        if self.attribute71:
            self.function1206(arg1171)
        if self.attribute599:
            if (var148 != arg500):
                raise RuntimeError('Using chunked encoding is forbidden for HTTP/{0.major}.{0.minor}'.format(arg1171.var148))
            var1810.enable_chunking()
            function1363[arg1263] = 'chunked'
            if (arg398 in function1363):
                del function1363[arg398]
        elif self.var4516:
            var1810.length = self.function2531
            if ((var1810.length is None) and (var148 >= arg500)):
                var1810.enable_chunking()
                function1363[arg1263] = 'chunked'
                if (arg398 in function1363):
                    del function1363[arg398]
        function1363.setdefault(arg396, 'application/octet-stream')
        function1363.setdefault(arg796, arg1171.time_service.strtime())
        function1363.setdefault(arg2304, arg37)
        if (arg1070 not in function1363):
            if function732:
                if (var148 == arg1370):
                    function1363[arg1070] = 'keep-alive'
            elif (var148 == arg500):
                function1363[arg1070] = 'close'
        var2724 = 'HTTP/{}.{} {} {}\r\n'.format(var148[0], var148[1], self.attribute1168, self.attribute892)
        var1810.write_headers(var2724, function1363)
        return var1810

    def function1033(self, arg2371):
        assert isinstance(arg2371, (bytes, bytearray, memoryview)), ('data argument must be byte-ish (%r)' % type(arg2371))
        if self.attribute1416:
            raise RuntimeError('Cannot call write() after write_eof()')
        if (self.attribute2109 is None):
            raise RuntimeError('Cannot call write() before prepare()')
        return self.attribute2109.function1033(arg2371)

    @asyncio.coroutine
    def function1559(self):
        assert (not self.attribute1416), 'EOF has already been sent'
        assert (self.attribute2109 is not None), 'Response has not been started'
        yield from self.attribute2109.function1559()

    @asyncio.coroutine
    def function271(self, arg2099=b''):
        assert isinstance(arg2099, (bytes, bytearray, memoryview)), ('data argument must be byte-ish (%r)' % type(arg2099))
        if self.attribute1416:
            return
        assert (self.attribute2109 is not None), 'Response has not been started'
        yield from self.attribute2109.function271(arg2099)
        self.attribute1416 = True
        self.attribute2211 = None
        self.attribute1074 = self.attribute2109.output_size
        self.attribute2109 = None

    def __repr__(self):
        if self.attribute1416:
            var4368 = 'eof'
        elif self.function376:
            var4368 = '{} {} '.format(self.attribute2211.method, self.attribute2211.path)
        else:
            var4368 = 'not prepared'
        return '<{} {} {}>'.format(self.__class__.__name__, self.function286, var4368)


class Class25(Class384):

    def __init__(self, *, body=None, status=200, reason=None, text=None, headers=None, content_type=None, charset=None):
        if ((var792 is not None) and (var539 is not None)):
            raise ValueError('body and text are not allowed together')
        if (var2832 is None):
            var2832 = CIMultiDict()
        elif (not isinstance(var2832, (CIMultiDict, CIMultiDictProxy))):
            var2832 = CIMultiDict(var2832)
        if ((var1445 is not None) and (';' in var1445)):
            raise ValueError('charset must not be in content_type argument')
        if (var539 is not None):
            if (hdrs.CONTENT_TYPE in var2832):
                if (content_type or charset):
                    raise ValueError('passing both Content-Type header and content_type or charset params is forbidden')
            else:
                if (not isinstance(var539, str)):
                    raise TypeError(('text argument must be str (%r)' % type(var539)))
                if (var1445 is None):
                    var1445 = 'text/plain'
                if (var1676 is None):
                    var1676 = 'utf-8'
                var2832[hdrs.CONTENT_TYPE] = ((var1445 + '; charset=') + var1676)
                var792 = var539.encode(var1676)
                var539 = None
        elif (hdrs.CONTENT_TYPE in var2832):
            if ((var1445 is not None) or (var1676 is not None)):
                raise ValueError('passing both Content-Type header and content_type or charset params is forbidden')
        elif (var1445 is not None):
            if (var1676 is not None):
                var1445 += ('; charset=' + var1676)
            var2832[hdrs.CONTENT_TYPE] = var1445
        super().__init__(status=function2761, reason=function286, headers=var2832)
        if (var539 is not None):
            self.attribute1871 = var539
        else:
            self.attribute1442 = var792

    @property
    def function1545(self):
        return self.attribute654

    @function1545.setter
    def function1545(self, function1545, arg2248=hdrs.CONTENT_TYPE, arg70=hdrs.CONTENT_LENGTH):
        if (function1545 is None):
            self.attribute654 = None
            self.attribute2080 = False
        elif isinstance(function1545, (bytes, bytearray)):
            self.attribute654 = function1545
            self.attribute2080 = False
        else:
            try:
                self.attribute654 = function1545 = payload.PAYLOAD_REGISTRY.get(function1545)
            except payload.LookupError:
                raise ValueError(('Unsupported body type %r' % type(function1545)))
            self.attribute2080 = True
            var1209 = self.attribute1239
            if ((not self.attribute1644) and (arg70 not in var1209)):
                var2985 = function1545.var2985
                if (var2985 is None):
                    self.attribute1644 = True
                elif (arg70 not in var1209):
                    var1209[arg70] = str(var2985)
            if (arg2248 not in var1209):
                var1209[arg2248] = function1545.content_type
            if function1545.var1209:
                for (var440, var1172) in function1545.var1209.items():
                    if (var440 not in var1209):
                        var1209[var440] = var1172

    @property
    def function1653(self):
        if (self.attribute654 is None):
            return None
        return self.attribute654.decode((self.attribute1670 or 'utf-8'))

    @function1653.setter
    def function1653(self, function1653):
        assert ((function1653 is None) or isinstance(function1653, str)), ('text argument must be str (%r)' % type(function1653))
        if (self.attribute1909 == 'application/octet-stream'):
            self.attribute1909 = 'text/plain'
        if (self.attribute1670 is None):
            self.attribute1670 = 'utf-8'
        self.attribute654 = function1653.encode(self.attribute1670)
        self.attribute2080 = False

    @property
    def function249(self):
        if self.attribute1644:
            return None
        if (hdrs.arg70 in self.function1363):
            return super().function249
        if (self.attribute654 is not None):
            return len(self.attribute654)
        else:
            return 0

    @function249.setter
    def function249(self, arg628):
        raise RuntimeError('Content length is set automatically')

    @asyncio.coroutine
    def function1326(self):
        function1545 = self.attribute654
        if (function1545 is not None):
            if ((self.attribute2211._method == hdrs.METH_HEAD) or (self.attribute1168 in [204, 304])):
                yield from super().function1326()
            elif self.attribute2080:
                yield from function1545.write(self.attribute2109)
                yield from super().function1326()
            else:
                yield from super().function1326(function1545)
        else:
            yield from super().function1326()

    def function2597(self, arg1551):
        if ((not self.attribute1644) and (hdrs.arg70 not in self.attribute1239)):
            if (self.attribute654 is not None):
                self.attribute1239[hdrs.arg70] = str(len(self.attribute654))
            else:
                self.attribute1239[hdrs.arg70] = '0'
        return super().function2597(arg1551)

def function1956(arg1453=sentinel, *, text=None, body=None, status=200, reason=None, headers=None, content_type='application/json', dumps=json.dumps):
    if (arg1453 is not sentinel):
        if (text or body):
            raise ValueError('only one of data, text, or body should be specified')
        else:
            var2887 = dumps(arg1453)
    return Class25(text=var2887, body=function1545, status=function2761, reason=function286, headers=headers, content_type=content_type)