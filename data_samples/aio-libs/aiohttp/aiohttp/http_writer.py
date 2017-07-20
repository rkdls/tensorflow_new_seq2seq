'Http related parsers and protocol.'
import asyncio
import collections
import socket
import zlib
from urllib.parse import SplitResult
import yarl
from .abc import AbstractPayloadWriter
from .helpers import create_future, noop
var863 = ('PayloadWriter', 'HttpVersion', 'HttpVersion10', 'HttpVersion11', 'StreamWriter')
var55 = collections.namedtuple('HttpVersion', ['major', 'minor'])
var2830 = var55(1, 0)
var2619 = var55(1, 1)
if hasattr(socket, 'TCP_CORK'):
    var4008 = socket.TCP_CORK
elif hasattr(socket, 'TCP_NOPUSH'):
    var4008 = socket.TCP_NOPUSH
else:
    var4008 = None


class Class436:

    def __init__(self, arg1199, arg1966, arg502):
        self.attribute1038 = arg1199
        self.attribute1480 = arg502
        self.attribute1068 = False
        self.attribute665 = False
        self.attribute1961 = arg1966.get_extra_info('socket')
        self.attribute2238 = []
        self.attribute651 = True
        self.attribute1396 = arg1966

    def function1285(self, arg64):
        if self.attribute651:
            self.attribute651 = False
            arg64.set_transport(self.attribute1396)
        else:
            self.attribute2238.append(arg64)

    def function106(self):
        if self.attribute2238:
            self.attribute651 = False
            var153 = self.attribute2238.pop(0)
            var153.set_transport(self.attribute1396)
        else:
            self.attribute651 = True

    def function373(self, arg1268, arg1683):
        try:
            var2206 = self.attribute2238.index(arg1268)
            arg1268 = arg1683(self, self.attribute1480, False)
            self.attribute2238[var2206] = arg1268
            return arg1268
        except ValueError:
            self.attribute651 = True
            return arg1683(self, self.attribute1480)

    @property
    def function2081(self):
        return self.attribute1068

    def function627(self, arg1058):
        arg1058 = bool(arg1058)
        if (self.attribute1068 == arg1058):
            return
        if (self.attribute1961 is None):
            return
        if (self.attribute1961.family not in (socket.AF_INET, socket.AF_INET6)):
            return
        try:
            if self.attribute665:
                if (var4008 is not None):
                    self.attribute1961.setsockopt(socket.IPPROTO_TCP, var4008, False)
                    self.attribute665 = False
            self.attribute1961.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, arg1058)
            self.attribute1068 = arg1058
        except OSError:
            pass

    @property
    def function1098(self):
        return self.attribute665

    def function2576(self, arg1058):
        arg1058 = bool(arg1058)
        if (self.attribute665 == arg1058):
            return
        if (self.attribute1961 is None):
            return
        if (self.attribute1961.family not in (socket.AF_INET, socket.AF_INET6)):
            return
        try:
            if self.attribute1068:
                self.attribute1961.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, False)
                self.attribute1068 = False
            if (var4008 is not None):
                self.attribute1961.setsockopt(socket.IPPROTO_TCP, var4008, arg1058)
                self.attribute665 = arg1058
        except OSError:
            pass

    @asyncio.coroutine
    def function782(self):
        'Flush the write buffer.\n\n        The intended use is to write\n\n          w.write(data)\n          yield from w.drain()\n        '
        if (self.attribute1038.transport is not None):
            yield from self.attribute1038._drain_helper()


class Class50(AbstractPayloadWriter):

    def __init__(self, arg1548, arg376, function1285=True):
        self.attribute1482 = arg1548
        self.attribute710 = None
        self.attribute2227 = arg376
        self.attribute413 = None
        self.attribute1491 = False
        self.attribute411 = 0
        self.attribute2243 = 0
        self.attribute1906 = False
        self.attribute614 = []
        self.attribute1209 = None
        self.attribute1863 = None
        if self.attribute1482.available:
            self.attribute710 = self.attribute1482.transport
            self.attribute1482.available = False
        elif function1285:
            self.attribute1482.function1285(self)

    def function877(self, arg1411):
        self.attribute710 = arg1411
        var1870 = b''.join(self.attribute614)
        if var1870:
            arg1411.function207(var1870)
            self.attribute614.clear()
        if (self.attribute1863 is not None):
            (var3861, self.attribute1863) = (self.attribute1863, None)
            if (not var3861.done()):
                var3861.set_result(None)

    @property
    def function2081(self):
        return self.attribute1482.function2081

    def function627(self, arg1058):
        self.attribute1482.function627(arg1058)

    @property
    def function1098(self):
        return self.attribute1482.function1098

    def function2576(self, arg1058):
        self.attribute1482.function2576(arg1058)

    def function2364(self):
        self.attribute1491 = True

    def function2115(self, arg1692='deflate'):
        var1493 = ((16 + zlib.MAX_WBITS) if (arg1692 == 'gzip') else (- zlib.MAX_WBITS))
        self.attribute1209 = zlib.compressobj(wbits=var1493)

    def function2803(self, arg1179):
        if arg1179:
            var3374 = len(arg1179)
            self.attribute411 += var3374
            self.attribute2243 += var3374
            self.attribute614.append(arg1179)

    def function2126(self, arg2326):
        var1150 = len(arg2326)
        self.attribute411 += var1150
        self.attribute2243 += var1150
        if (self.attribute710 is not None):
            if self.attribute614:
                self.attribute614.append(arg2326)
                self.attribute710.function207(b''.join(self.attribute614))
                self.attribute614.clear()
            else:
                self.attribute710.function207(arg2326)
        else:
            self.attribute614.append(arg2326)

    def function207(self, arg129, *, drain=True, LIMIT=(64 * 1024)):
        "Writes chunk of data to a stream.\n\n        write_eof() indicates end of stream.\n        writer can't be used after write_eof() method being called.\n        write() return drain future.\n        "
        if (self.attribute1209 is not None):
            arg129 = self.attribute1209.compress(arg129)
            if (not arg129):
                return noop()
        if (self.attribute413 is not None):
            var3269 = len(arg129)
            if (self.attribute413 >= var3269):
                self.attribute413 = (self.attribute413 - var3269)
            else:
                arg129 = arg129[:self.attribute413]
                self.attribute413 = 0
                if (not arg129):
                    return noop()
        if arg129:
            if self.attribute1491:
                var3269 = ('%x\r\n' % len(arg129)).encode('ascii')
                arg129 = ((var3269 + arg129) + b'\r\n')
            self.function2126(arg129)
            if ((self.attribute411 > LIMIT) and drain):
                self.attribute411 = 0
                return self.function1461()
        return noop()

    def function1116(self, arg680, arg2114, arg1946=': ', arg847='\r\n'):
        'Write request/response status and headers.'
        arg2114 = (arg680 + ''.join([(((var2790 + arg1946) + var1456) + arg847) for (var2790, var1456) in arg2114.items()]))
        arg2114 = (arg2114.encode('utf-8') + b'\r\n')
        var612 = len(arg2114)
        self.attribute411 += var612
        self.attribute2243 += var612
        self.attribute614.append(arg2114)

    @asyncio.coroutine
    def function825(self, arg1925=b''):
        if self.attribute1906:
            return
        if self.attribute1209:
            if arg1925:
                arg1925 = self.attribute1209.compress(arg1925)
            arg1925 = (arg1925 + self.attribute1209.flush())
            if (chunk and self.attribute1491):
                var3116 = ('%x\r\n' % len(arg1925)).encode('ascii')
                arg1925 = ((var3116 + arg1925) + b'\r\n0\r\n\r\n')
        elif self.attribute1491:
            if arg1925:
                var3116 = ('%x\r\n' % len(arg1925)).encode('ascii')
                arg1925 = ((var3116 + arg1925) + b'\r\n0\r\n\r\n')
            else:
                arg1925 = b'0\r\n\r\n'
        if arg1925:
            self.function2803(arg1925)
        yield from self.function1461(True)
        self.attribute1906 = True
        self.attribute710 = None
        self.attribute1482.function106()

    @asyncio.coroutine
    def function1461(self, arg346=False):
        if (self.attribute710 is not None):
            if self.attribute614:
                self.attribute710.function207(b''.join(self.attribute614))
                if (not arg346):
                    self.attribute614.clear()
            yield from self.attribute1482.function1461()
        else:
            if (self.attribute1863 is None):
                self.attribute1863 = create_future(self.attribute2227)
            yield from self.attribute1863


class Class246(yarl.URL):

    def __init__(self, arg1051, arg1000, arg682, arg2280, arg192, arg1897, arg551):
        self.attribute1287 = False
        if arg682:
            arg1000 += ':{}'.format(arg682)
        if arg551:
            arg1000 = ((yarl.quote(arg551, safe='@:', protected=':', strict=False) + '@') + arg1000)
        if arg2280:
            arg2280 = yarl.quote(arg2280, safe='@:', protected='/', strict=False)
        if arg192:
            arg192 = yarl.quote(arg192, safe='=+&?/:@', protected=yarl.PROTECT_CHARS, qs=True, strict=False)
        if arg1897:
            arg1897 = yarl.quote(arg1897, safe='?/:@', strict=False)
        self.attribute914 = SplitResult((schema or ''), netloc=arg1000, path=arg2280, query=arg192, fragment=arg1897)
        self.attribute233 = {}