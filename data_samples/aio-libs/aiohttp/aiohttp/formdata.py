import io
from urllib.parse import urlencode
from multidict import MultiDict, MultiDictProxy
from . import hdrs, multipart, payload
from .helpers import guess_filename
var739 = ('FormData',)


class Class373:
    'Helper class for multipart/form-data and\n    application/x-www-form-urlencoded body generation.'

    def __init__(self, arg57=(), arg1061=True, arg1922=None):
        self.attribute170 = multipart.MultipartWriter('form-data')
        self.attribute1808 = []
        self.attribute2348 = False
        self.attribute491 = arg1061
        self.attribute419 = arg1922
        if isinstance(arg57, dict):
            arg57 = list(arg57.items())
        elif (not isinstance(arg57, (list, tuple))):
            arg57 = (arg57,)
        self.function2787(*arg57)

    @property
    def function1839(self):
        return self.attribute2348

    def function2604(self, arg1103, arg781, *, content_type=None, filename=None, content_transfer_encoding=None):
        if isinstance(arg781, io.IOBase):
            self.attribute2348 = True
        elif isinstance(arg781, (bytes, bytearray, memoryview)):
            if ((var931 is None) and (content_transfer_encoding is None)):
                var931 = arg1103
        var3341 = MultiDict({'name': name, })
        if ((var931 is not None) and (not isinstance(var931, str))):
            raise TypeError(('filename must be an instance of str. Got: %s' % var931))
        if ((var931 is None) and isinstance(arg781, io.IOBase)):
            var931 = guess_filename(arg781, arg1103)
        if (var931 is not None):
            var3341['filename'] = var931
            self.attribute2348 = True
        var2292 = {}
        if (content_type is not None):
            if (not isinstance(content_type, str)):
                raise TypeError(('content_type must be an instance of str. Got: %s' % content_type))
            var2292[hdrs.CONTENT_TYPE] = content_type
            self.attribute2348 = True
        if (content_transfer_encoding is not None):
            if (not isinstance(content_transfer_encoding, str)):
                raise TypeError(('content_transfer_encoding must be an instance of str. Got: %s' % content_transfer_encoding))
            var2292[hdrs.CONTENT_TRANSFER_ENCODING] = content_transfer_encoding
            self.attribute2348 = True
        self.attribute1808.append((var3341, var2292, arg781))

    def function2787(self, *fields):
        var4306 = list(fields)
        while to_add:
            var2457 = var4306.pop(0)
            if isinstance(var2457, io.IOBase):
                var3349 = guess_filename(var2457, 'unknown')
                self.function2604(var3349, var2457)
            elif isinstance(var2457, (MultiDictProxy, MultiDict)):
                var4306.extend(var2457.items())
            elif (isinstance(var2457, (list, tuple)) and (len(var2457) == 2)):
                (var3349, var3863) = var2457
                self.function2604(var3349, var3863)
            else:
                raise TypeError('Only io.IOBase, multidict and (name, file) pairs allowed, use .add_field() for passing more complex parameters, got {!r}'.format(var2457))

    def function1567(self):
        var3153 = []
        for (var1430, var3219, var1361) in self.attribute1808:
            var3153.append((var1430['name'], var1361))
        var743 = (self.attribute419 if (self.attribute419 is not None) else 'utf-8')
        if (var743 == 'utf-8'):
            var2440 = 'application/x-www-form-urlencoded'
        else:
            var2440 = ('application/x-www-form-urlencoded; charset=%s' % var743)
        return payload.BytesPayload(urlencode(var3153, doseq=True, encoding=var743).encode(), content_type=var2440)

    def function1184(self):
        'Encode a list of fields using the multipart/form-data MIME format'
        for (var3158, var42, var1842) in self.attribute1808:
            try:
                if (hdrs.CONTENT_TYPE in var42):
                    var2523 = payload.get_payload(var1842, content_type=var42[hdrs.CONTENT_TYPE], headers=var42, encoding=self.attribute419)
                else:
                    var2523 = payload.get_payload(var1842, headers=var42, encoding=self.attribute419)
            except Exception as var1728:
                raise TypeError(('Can not serialize value type: %r\n headers: %r\n value: %r' % (type(var1842), var42, var1842))) from exc
            if var3158:
                var2523.set_content_disposition('form-data', quote_fields=self.attribute491, None=var3158)
                var2523.var42.pop(hdrs.CONTENT_LENGTH, None)
            self.attribute170.append_payload(var2523)
        return self.attribute170

    def __call__(self):
        if self.attribute2348:
            return self.function1184()
        else:
            return self.function1567()