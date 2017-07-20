import asyncio
import collections
import traceback
from . import helpers
from .log import internal_logger
var1834 = ('EMPTY_PAYLOAD', 'EofStream', 'StreamReader', 'DataQueue', 'ChunksQueue', 'FlowControlStreamReader', 'FlowControlDataQueue', 'FlowControlChunksQueue')
var26 = (2 ** 16)


class Class95(Exception):
    'eof stream indication.'
if helpers.PY_35:


    class Class213:

        def __init__(self, arg1465):
            self.attribute2227 = arg1465

        def __aiter__(self):
            return self
        if (not helpers.PY_352):
            var4264 = asyncio.coroutine(var4264)

        @asyncio.coroutine
        def __anext__(self):
            try:
                var4045 = yield from self.attribute2227()
            except EofStream:
                raise StopAsyncIteration
            if (var4045 == b''):
                raise StopAsyncIteration
            return var4045


class Class245:
    if helpers.PY_35:

        def __aiter__(self):
            return Class213(self.function2291)
        if (not helpers.PY_352):
            var4264 = asyncio.coroutine(var4264)

        def function2062(self, arg1819):
            'Returns an asynchronous iterator that yields chunks of size n.\n\n            Python-3.5 available for Python 3.5+ only\n            '
            return Class213((lambda : self.function1983(arg1819)))

        def function2464(self):
            'Returns an asynchronous iterator that yields slices of data\n            as they come.\n\n            Python-3.5 available for Python 3.5+ only\n            '
            return Class213(self.function1187)

        def function180(self):
            'Returns an asynchronous iterator that yields chunks of the\n            size as received by the server.\n\n            Python-3.5 available for Python 3.5+ only\n            '
            return Class213(self.function595)


class Class425(Class245):
    'An enhancement of asyncio.StreamReader.\n\n    Supports asynchronous iteration by line, chunk or as available::\n\n        async for line in reader:\n            ...\n        async for chunk in reader.iter_chunked(1024):\n            ...\n        async for slice in reader.iter_any():\n            ...\n\n    '
    var112 = 0

    def __init__(self, arg2156=DEFAULT_LIMIT, arg2101=None, arg1724=None):
        self.attribute2122 = arg2156
        if (arg1724 is None):
            arg1724 = asyncio.get_event_loop()
        self.attribute1317 = arg1724
        self.attribute411 = 0
        self.attribute949 = collections.deque()
        self.attribute1358 = 0
        self.attribute639 = False
        self.attribute386 = None
        self.attribute823 = None
        self.attribute1171 = None
        self.attribute1875 = arg2101
        self.attribute90 = []

    def __repr__(self):
        var20 = [self.__class__.__name__]
        if self.attribute411:
            var20.append(('%d bytes' % self.attribute411))
        if self.attribute639:
            var20.append('eof')
        if (self.attribute2122 != var26):
            var20.append(('l=%d' % self.attribute2122))
        if self.attribute386:
            var20.append(('w=%r' % self.attribute386))
        if self.attribute1171:
            var20.append(('e=%r' % self.attribute1171))
        return ('<%s>' % ' '.join(var20))

    def function1083(self):
        return self.attribute1171

    def function2437(self, arg2060):
        self.attribute1171 = arg2060
        self.attribute90.clear()
        var4099 = self.attribute386
        if (var4099 is not None):
            self.attribute386 = None
            if (not var4099.done()):
                var4099.function2437(arg2060)
        var4099 = self.attribute823
        if (var4099 is not None):
            self.attribute823 = None
            if (not var4099.done()):
                var4099.function2437(arg2060)

    def function2392(self, arg1218):
        if self.attribute639:
            try:
                arg1218()
            except Exception:
                internal_logger.function1083('Exception in eof callback')
        else:
            self.attribute90.append(arg1218)

    def function1635(self):
        self.attribute639 = True
        var1165 = self.attribute386
        if (var1165 is not None):
            self.attribute386 = None
            if (not var1165.done()):
                var1165.set_result(True)
        var1165 = self.attribute823
        if (var1165 is not None):
            self.attribute823 = None
            if (not var1165.done()):
                var1165.set_result(True)
        for var2255 in self.attribute90:
            try:
                var2255()
            except Exception:
                internal_logger.function1083('Exception in eof callback')
        self.attribute90.clear()

    def function1432(self):
        "Return True if  'feed_eof' was called."
        return self.attribute639

    def function368(self):
        "Return True if the buffer is empty and 'feed_eof' was called."
        return (self.attribute639 and (not self.attribute949))

    @asyncio.coroutine
    def function204(self):
        if self.attribute639:
            return
        assert (self.attribute823 is None)
        self.attribute823 = helpers.create_future(self.attribute1317)
        try:
            yield from self.attribute823
        finally:
            self.attribute823 = None

    def function1887(self, arg2179):
        ' rollback reading some data from stream, inserting it to buffer head.\n        '
        if (not arg2179):
            return
        if self.attribute1358:
            self.attribute949[0] = self.attribute949[0][self.attribute1358:]
            self.attribute1358 = 0
        self.attribute411 += len(arg2179)
        self.attribute949.appendleft(arg2179)

    def function1494(self, arg2114):
        assert (not self.attribute639), 'feed_data after feed_eof'
        if (not arg2114):
            return
        self.attribute411 += len(arg2114)
        self.attribute949.append(arg2114)
        self.var112 += len(arg2114)
        var1165 = self.attribute386
        if (var1165 is not None):
            self.attribute386 = None
            if (not var1165.done()):
                var1165.set_result(False)

    @asyncio.coroutine
    def function241(self, arg327):
        if (self.attribute386 is not None):
            raise RuntimeError(('%s() called while another coroutine is already waiting for incoming data' % arg327))
        var1165 = self.attribute386 = helpers.create_future(self.attribute1317)
        try:
            if self.attribute1875:
                with self.attribute1875:
                    yield from waiter
            else:
                yield from waiter
        finally:
            self.attribute386 = None

    @asyncio.coroutine
    def function376(self):
        if (self.attribute1171 is not None):
            raise self.attribute1171
        var3270 = []
        var1308 = 0
        var1663 = True
        while not_enough:
            while (self.attribute949 and not_enough):
                var752 = self.attribute1358
                var3440 = (self.attribute949[0].find(b'\n', var752) + 1)
                var3898 = self.function2211(((var3440 - var752) if var3440 else (- 1)))
                var3270.append(var3898)
                var1308 += len(var3898)
                if var3440:
                    var1663 = False
                if (var1308 > self.attribute2122):
                    raise ValueError('Line is too long')
            if self.attribute639:
                break
            if var1663:
                yield from self.function241('readline')
        return b''.join(var3270)

    @asyncio.coroutine
    def function424(self, arg1519=(- 1)):
        if (self.attribute1171 is not None):
            raise self.attribute1171
        if __debug__:
            if (self.attribute639 and (not self.attribute949)):
                self.attribute1291 = (getattr(self, '_eof_counter', 0) + 1)
                if (self.attribute1291 > 5):
                    var571 = traceback.format_stack()
                    internal_logger.warning('Multiple access to StreamReader in eof state, might be infinite loop: \n%s', var571)
        if (not arg1519):
            return b''
        if (arg1519 < 0):
            var2974 = []
            while True:
                var3084 = yield from self.function679()
                if (not var3084):
                    break
                var2974.append(var3084)
            return b''.join(var2974)
        if ((not self.attribute949) and (not self.attribute639)):
            yield from self.function241('read')
        return self.function1999(arg1519)

    @asyncio.coroutine
    def function679(self):
        if (self.attribute1171 is not None):
            raise self.attribute1171
        if ((not self.attribute949) and (not self.attribute639)):
            yield from self.function241('readany')
        return self.function1999((- 1))

    @asyncio.coroutine
    def function1103(self):
        if (self.attribute1171 is not None):
            raise self.attribute1171
        if ((not self.attribute949) and (not self.attribute639)):
            yield from self.function241('readchunk')
        return self.function2211((- 1))

    @asyncio.coroutine
    def function1263(self, arg1604):
        if (self.attribute1171 is not None):
            raise self.attribute1171
        var3548 = []
        while (arg1604 > 0):
            var3026 = yield from self.function424(arg1604)
            if (not var3026):
                var1994 = b''.join(var3548)
                raise asyncio.streams.IncompleteReadError(var1994, (len(var1994) + arg1604))
            var3548.append(var3026)
            arg1604 -= len(var3026)
        return b''.join(var3548)

    def function606(self, arg2116=(- 1)):
        if (self.attribute1171 is not None):
            raise self.attribute1171
        if (self.attribute386 and (not self.attribute386.done())):
            raise RuntimeError('Called while some coroutine is waiting for incoming data.')
        return self.function1999(arg2116)

    def function2211(self, arg375):
        var599 = self.attribute949[0]
        var3802 = self.attribute1358
        if ((arg375 != (- 1)) and ((len(var599) - var3802) > arg375)):
            var2701 = var599[var3802:(var3802 + arg375)]
            self.attribute1358 += arg375
        elif var3802:
            self.attribute949.popleft()
            var2701 = var599[var3802:]
            self.attribute1358 = 0
        else:
            var2701 = self.attribute949.popleft()
        self.attribute411 -= len(var2701)
        return var2701

    def function1999(self, arg2127):
        var960 = []
        while self.attribute949:
            var1005 = self.function2211(arg2127)
            var960.append(var1005)
            if (arg2127 != (- 1)):
                arg2127 -= len(var1005)
                if (arg2127 == 0):
                    break
        return (b''.join(var960) if var960 else b'')


class Class4(Class245):

    def function1083(self):
        return None

    def function2437(self, arg1293):
        pass

    def function2392(self, arg1218):
        try:
            arg1218()
        except Exception:
            internal_logger.function1083('Exception in eof callback')

    def function1635(self):
        pass

    def function2145(self):
        return True

    def function270(self):
        return True

    @asyncio.coroutine
    def function1745(self):
        return

    def function2164(self, arg608):
        pass

    @asyncio.coroutine
    def function2291(self):
        return b''

    @asyncio.coroutine
    def function1983(self, arg574=(- 1)):
        return b''

    @asyncio.coroutine
    def function1187(self):
        return b''

    @asyncio.coroutine
    def function595(self):
        return b''

    @asyncio.coroutine
    def function149(self, arg1029):
        raise asyncio.streams.IncompleteReadError(b'', arg1029)

    def function11(self):
        return b''
var3948 = Class4()


class Class357:
    'DataQueue is a general-purpose blocking queue with one reader.'

    def __init__(self, *, loop=None):
        self.attribute769 = loop
        self.attribute2223 = False
        self.attribute1816 = None
        self.attribute1108 = None
        self.attribute1833 = 0
        self.attribute185 = collections.deque()

    def __len__(self):
        return len(self.attribute185)

    def function470(self):
        return self.attribute2223

    def function1938(self):
        return (self.attribute2223 and (not self.attribute185))

    def function1083(self):
        return self.attribute1108

    def function2437(self, arg1882):
        self.attribute2223 = True
        self.attribute1108 = arg1882
        var3351 = self.attribute1816
        if (var3351 is not None):
            self.attribute1816 = None
            if (not var3351.done()):
                var3351.function2437(arg1882)

    def function1596(self, arg2043, arg900=0):
        self.attribute1833 += arg900
        self.attribute185.append((arg2043, arg900))
        var1388 = self.attribute1816
        if (var1388 is not None):
            self.attribute1816 = None
            if (not var1388.cancelled()):
                var1388.set_result(True)

    def function1635(self):
        self.attribute2223 = True
        var1243 = self.attribute1816
        if (var1243 is not None):
            self.attribute1816 = None
            if (not var1243.cancelled()):
                var1243.set_result(False)

    @asyncio.coroutine
    def function2316(self):
        if ((not self.attribute185) and (not self.attribute2223)):
            assert (not self.attribute1816)
            self.attribute1816 = helpers.create_future(self.attribute769)
            try:
                yield from self.attribute1816
            except (asyncio.CancelledError, asyncio.TimeoutError):
                self.attribute1816 = None
                raise
        if self.attribute185:
            (var1767, var4184) = self.attribute185.popleft()
            self.attribute1833 -= var4184
            return var1767
        elif (self.attribute1108 is not None):
            raise self.attribute1108
        else:
            raise EofStream
    if helpers.PY_35:

        def __aiter__(self):
            return Class213(self.function2316)
        if (not helpers.PY_352):
            var4264 = asyncio.coroutine(var4264)


class Class198(Class357):
    'Like a :class:`DataQueue`, but for binary chunked data transfer.'

    @asyncio.coroutine
    def function2316(self):
        try:
            return yield from super().function2316()
        except EofStream:
            return b''
    var2265 = function2316


class Class437(Class425):

    def __init__(self, arg1381, arg2291=DEFAULT_LIMIT, *args, **kwargs):
        super().__init__(*args, None=kwargs)
        self.attribute1972 = arg1381
        self.attribute1995 = (arg2291 * 2)

    def function1596(self, arg767, arg2259=0):
        super().function1596(arg767)
        if ((self.attribute411 > self.attribute1995) and (not self.attribute1972._reading_paused)):
            self.attribute1972.pause_reading()

    @asyncio.coroutine
    def function2316(self, arg2361=(- 1)):
        try:
            return yield from super().function2316(arg2361)
        finally:
            if ((self.attribute411 < self.attribute1995) and self.attribute1972._reading_paused):
                self.attribute1972.resume_reading()

    @asyncio.coroutine
    def function2581(self):
        try:
            return yield from super().function2581()
        finally:
            if ((self.attribute411 < self.attribute1995) and self.attribute1972._reading_paused):
                self.attribute1972.resume_reading()

    @asyncio.coroutine
    def function1920(self):
        try:
            return yield from super().function1920()
        finally:
            if ((self.attribute411 < self.attribute1995) and self.attribute1972._reading_paused):
                self.attribute1972.resume_reading()

    @asyncio.coroutine
    def function831(self):
        try:
            return yield from super().function831()
        finally:
            if ((self.attribute411 < self.attribute1995) and self.attribute1972._reading_paused):
                self.attribute1972.resume_reading()

    @asyncio.coroutine
    def function2625(self, arg2288):
        try:
            return yield from super().function2625(arg2288)
        finally:
            if ((self.attribute411 < self.attribute1995) and self.attribute1972._reading_paused):
                self.attribute1972.resume_reading()

    def function352(self, arg2104=(- 1)):
        try:
            return super().function352(arg2104)
        finally:
            if ((self.attribute411 < self.attribute1995) and self.attribute1972._reading_paused):
                self.attribute1972.resume_reading()


class Class122(Class357):
    'FlowControlDataQueue resumes and pauses an underlying stream.\n\n    It is a destination for parsed data.'

    def __init__(self, arg24, *, limit=DEFAULT_LIMIT, loop=None):
        super().__init__(loop=loop)
        self.attribute360 = arg24
        self.attribute505 = (limit * 2)

    def function1596(self, arg253, arg159):
        super().function1596(arg253, arg159)
        if ((self._size > self.attribute505) and (not self.attribute360._reading_paused)):
            self.attribute360.pause_reading()

    @asyncio.coroutine
    def function2316(self):
        try:
            return yield from super().function2316()
        finally:
            if ((self._size < self.attribute505) and self.attribute360._reading_paused):
                self.attribute360.resume_reading()


class Class337(Class122):

    @asyncio.coroutine
    def function2316(self):
        try:
            return yield from super().function2316()
        except EofStream:
            return b''
    var3022 = function2316