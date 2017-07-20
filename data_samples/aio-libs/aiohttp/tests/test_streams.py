'Tests for streams.py'
import asyncio
import unittest
from unittest import mock
from aiohttp import helpers, streams, test_utils


class Class330(unittest.TestCase):
    var3826 = b'line1\nline2\nline3\n'

    def function417(self):
        self.attribute1794 = None
        self.attribute1361 = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def function902(self):
        self.attribute1361.close()

    def function1833(self, *args, **kwargs):
        if ('timeout' in kwargs):
            self.attribute1794 = helpers.TimeService(self.attribute1361, interval=0.01)
            self.addCleanup(self.attribute1794.close)
            kwargs['timer'] = self.attribute1794.timeout(kwargs.pop('timeout'))
        return streams.StreamReader(*args, loop=self.attribute1361, None=kwargs)

    def function258(self):
        var479 = self.function1833()
        var479._waiter = helpers.create_future(self.attribute1361)
        with self.assertRaises(RuntimeError):
            self.attribute1361.run_until_complete(var479._wait('test'))

    @mock.patch('aiohttp.streams.asyncio')
    def function2088(self, arg883):
        var4155 = streams.StreamReader()
        self.assertIs(var4155._loop, arg883.get_event_loop.return_value)

    def function335(self):
        var2048 = self.function1833()
        self.assertFalse(var2048.at_eof())
        var2048.feed_data(b'some data\n')
        self.assertFalse(var2048.at_eof())
        self.attribute1361.run_until_complete(var2048.readline())
        self.assertFalse(var2048.at_eof())
        var2048.feed_data(b'some data\n')
        var2048.feed_eof()
        self.attribute1361.run_until_complete(var2048.readline())
        self.assertTrue(var2048.at_eof())

    def function1798(self):
        var4254 = self.function1833()
        var778 = asyncio.Task(var4254.wait_eof(), loop=self.attribute1361)

        def function1417():
            yield from asyncio.sleep(0.1, loop=self.attribute1361)
            var4254.feed_eof()
        asyncio.Task(function1417(), loop=self.attribute1361)
        self.attribute1361.run_until_complete(var778)
        self.assertTrue(var4254.is_eof())
        self.assertIsNone(var4254._eof_waiter)

    def function2558(self):
        var3636 = self.function1833()
        var3636.feed_eof()
        var295 = asyncio.Task(var3636.wait_eof(), loop=self.attribute1361)
        self.attribute1361.run_until_complete(var295)
        self.assertTrue(var3636.is_eof())

    def function2591(self):
        var1946 = self.function1833()
        var1946.feed_data(b'')
        var1946.feed_eof()
        var3502 = self.attribute1361.run_until_complete(var1946.read())
        self.assertEqual(b'', var3502)

    def function2662(self):
        var623 = self.function1833()
        var623.feed_data(self.var3826)
        var623.feed_eof()
        var1212 = self.attribute1361.run_until_complete(var623.read())
        self.assertEqual(self.var3826, var1212)

    def function961(self):
        var2147 = self.function1833()
        var2147.feed_data(self.var3826)
        var4169 = self.attribute1361.run_until_complete(var2147.read(0))
        self.assertEqual(b'', var4169)
        var2147.feed_eof()
        var4169 = self.attribute1361.run_until_complete(var2147.read())
        self.assertEqual(self.var3826, var4169)

    def function1802(self):
        var4540 = self.function1833()
        var4626 = asyncio.Task(var4540.read(30), loop=self.attribute1361)

        def function2538():
            var4540.feed_data(self.var3826)
        self.attribute1361.call_soon(function2538)
        var3597 = self.attribute1361.run_until_complete(var4626)
        self.assertEqual(self.var3826, var3597)
        var4540.feed_eof()
        var3597 = self.attribute1361.run_until_complete(var4540.read())
        self.assertEqual(b'', var3597)

    def function2879(self):
        var2068 = self.function1833()
        var2068.feed_data(b'line1')
        var2068.feed_data(b'line2')
        var2910 = self.attribute1361.run_until_complete(var2068.read(5))
        self.assertEqual(b'line1', var2910)
        var2910 = self.attribute1361.run_until_complete(var2068.read(5))
        self.assertEqual(b'line2', var2910)

    def function1967(self):
        var2264 = self.function1833()
        var2264.feed_data(b'line1')
        var2264.feed_data(b'line2')
        var2264.feed_eof()
        var1773 = self.attribute1361.run_until_complete(var2264.read())
        self.assertEqual(b'line1line2', var1773)

    def function2122(self):
        var1493 = self.function1833()
        var1493.feed_data(b'line1')
        var1493.feed_data(b'line2')
        var2290 = self.attribute1361.run_until_complete(var1493.read(8))
        self.assertEqual(b'line1lin', var2290)
        var2290 = self.attribute1361.run_until_complete(var1493.read(8))
        self.assertEqual(b'e2', var2290)

    def function2274(self):
        var1759 = self.function1833()
        var59 = asyncio.Task(var1759.read(1024), loop=self.attribute1361)

        def function686():
            var1759.feed_eof()
        self.attribute1361.call_soon(function686)
        var2975 = self.attribute1361.run_until_complete(var59)
        self.assertEqual(b'', var2975)
        var2975 = self.attribute1361.run_until_complete(var1759.read())
        self.assertEqual(var2975, b'')

    @mock.patch('aiohttp.streams.internal_logger')
    def function684(self, arg2278):
        var989 = self.function1833()
        var989.feed_eof()
        self.attribute1361.run_until_complete(var989.read())
        self.attribute1361.run_until_complete(var989.read())
        self.attribute1361.run_until_complete(var989.read())
        self.attribute1361.run_until_complete(var989.read())
        self.attribute1361.run_until_complete(var989.read())
        self.attribute1361.run_until_complete(var989.read())
        self.assertTrue(arg2278.warning.called)

    def function140(self):
        var2945 = self.function1833()
        var718 = asyncio.Task(var2945.read((- 1)), loop=self.attribute1361)

        def function2509():
            var2945.feed_data(b'chunk1\n')
            var2945.feed_data(b'chunk2')
            var2945.feed_eof()
        self.attribute1361.call_soon(function2509)
        var1984 = self.attribute1361.run_until_complete(var718)
        self.assertEqual(b'chunk1\nchunk2', var1984)
        var1984 = self.attribute1361.run_until_complete(var2945.read())
        self.assertEqual(b'', var1984)

    def function2871(self):
        var4700 = self.function1833()
        var4700.feed_data(b'line\n')
        var3589 = self.attribute1361.run_until_complete(var4700.read(2))
        self.assertEqual(b'li', var3589)
        var4700.set_exception(ValueError())
        self.assertRaises(ValueError, self.attribute1361.run_until_complete, var4700.read(2))

    def function243(self):
        var3544 = self.function1833()
        var3544.feed_data(b'chunk1 ')
        var3461 = asyncio.Task(var3544.readline(), loop=self.attribute1361)

        def function2617():
            var3544.feed_data(b'chunk2 ')
            var3544.feed_data(b'chunk3 ')
            var3544.feed_data(b'\n chunk4')
        self.attribute1361.call_soon(function2617)
        var1478 = self.attribute1361.run_until_complete(var3461)
        self.assertEqual(b'chunk1 chunk2 chunk3 \n', var1478)
        var3544.feed_eof()
        var0 = self.attribute1361.run_until_complete(var3544.read())
        self.assertEqual(b' chunk4', var0)

    def function2392(self):
        var1317 = self.function1833(limit=3)
        var1317.feed_data(b'li')
        var1317.feed_data(b'ne1\nline2\n')
        self.assertRaises(ValueError, self.attribute1361.run_until_complete, var1317.readline())
        var1317.feed_eof()
        var2241 = self.attribute1361.run_until_complete(var1317.read())
        self.assertEqual(b'line2\n', var2241)

    def function915(self):
        var3495 = self.function1833(limit=7)

        def function2578():
            var3495.feed_data(b'chunk1')
            var3495.feed_data(b'chunk2')
            var3495.feed_data(b'chunk3\n')
            var3495.feed_eof()
        self.attribute1361.call_soon(function2578)
        self.assertRaises(ValueError, self.attribute1361.run_until_complete, var3495.readline())
        var3495 = self.function1833(limit=7)

        def function2578():
            var3495.feed_data(b'chunk1')
            var3495.feed_data(b'chunk2\n')
            var3495.feed_data(b'chunk3\n')
            var3495.feed_eof()
        self.attribute1361.call_soon(function2578)
        self.assertRaises(ValueError, self.attribute1361.run_until_complete, var3495.readline())
        var2597 = self.attribute1361.run_until_complete(var3495.read())
        self.assertEqual(b'chunk3\n', var2597)

    def function623(self):
        var4647 = self.function1833()
        var4647.feed_data(self.var3826[:6])
        var4647.feed_data(self.var3826[6:])
        var3954 = self.attribute1361.run_until_complete(var4647.readline())
        self.assertEqual(b'line1\n', var3954)
        var4647.feed_eof()
        var4170 = self.attribute1361.run_until_complete(var4647.read())
        self.assertEqual(b'line2\nline3\n', var4170)

    def function1093(self):
        var3521 = self.function1833()
        var3521.feed_data(b'some data')
        var3521.feed_eof()
        var2388 = self.attribute1361.run_until_complete(var3521.readline())
        self.assertEqual(b'some data', var2388)

    def function602(self):
        var3623 = self.function1833()
        var3623.feed_eof()
        var2351 = self.attribute1361.run_until_complete(var3623.readline())
        self.assertEqual(b'', var2351)

    def function2627(self):
        var4714 = self.function1833()
        var4714.feed_data(self.var3826)
        self.attribute1361.run_until_complete(var4714.readline())
        var779 = self.attribute1361.run_until_complete(var4714.read(7))
        self.assertEqual(b'line2\nl', var779)
        var4714.feed_eof()
        var779 = self.attribute1361.run_until_complete(var4714.read())
        self.assertEqual(b'ine3\n', var779)

    def function2118(self):
        var878 = self.function1833()
        var878.feed_data(b'line\n')
        var4348 = self.attribute1361.run_until_complete(var878.readline())
        self.assertEqual(b'line\n', var4348)
        var878.set_exception(ValueError())
        self.assertRaises(ValueError, self.attribute1361.run_until_complete, var878.readline())

    def function2256(self):
        var2628 = self.function1833()
        var2628.feed_data(self.var3826)
        var1628 = self.attribute1361.run_until_complete(var2628.readexactly(0))
        self.assertEqual(b'', var1628)
        var2628.feed_eof()
        var1628 = self.attribute1361.run_until_complete(var2628.read())
        self.assertEqual(self.var3826, var1628)
        var2628 = self.function1833()
        var2628.feed_data(self.var3826)
        var1628 = self.attribute1361.run_until_complete(var2628.readexactly((- 1)))
        self.assertEqual(b'', var1628)
        var2628.feed_eof()
        var1628 = self.attribute1361.run_until_complete(var2628.read())
        self.assertEqual(self.var3826, var1628)

    def function617(self):
        var690 = self.function1833()
        var2968 = (2 * len(self.var3826))
        var4124 = asyncio.Task(var690.readexactly(var2968), loop=self.attribute1361)

        def function1471():
            var690.feed_data(self.var3826)
            var690.feed_data(self.var3826)
            var690.feed_data(self.var3826)
        self.attribute1361.call_soon(function1471)
        var3288 = self.attribute1361.run_until_complete(var4124)
        self.assertEqual((self.var3826 + self.var3826), var3288)
        var690.feed_eof()
        var3288 = self.attribute1361.run_until_complete(var690.read())
        self.assertEqual(self.var3826, var3288)

    def function1814(self):
        var2307 = self.function1833()
        var3608 = (2 * len(self.var3826))
        var2197 = asyncio.Task(var2307.readexactly(var3608), loop=self.attribute1361)

        def function911():
            var2307.feed_data(self.var3826)
            var2307.feed_eof()
        self.attribute1361.call_soon(function911)
        with self.assertRaises(asyncio.IncompleteReadError) as var3842:
            self.attribute1361.run_until_complete(var2197)
        self.assertEqual(var3842.exception.partial, self.var3826)
        self.assertEqual(var3842.exception.expected, var3608)
        self.assertEqual(str(var3842.exception), '18 bytes read on a total of 36 expected bytes')
        var3401 = self.attribute1361.run_until_complete(var2307.read())
        self.assertEqual(b'', var3401)

    def function562(self):
        var4736 = self.function1833()
        var4736.feed_data(b'line\n')
        var4135 = self.attribute1361.run_until_complete(var4736.readexactly(2))
        self.assertEqual(b'li', var4135)
        var4736.set_exception(ValueError())
        self.assertRaises(ValueError, self.attribute1361.run_until_complete, var4736.readexactly(2))

    def function1379(self):
        var3714 = self.function1833()
        var3714.feed_data(b'line1')
        var3714.feed_data(b'line2')
        var3714.feed_data(b'onemoreline')
        var2681 = self.attribute1361.run_until_complete(var3714.read(5))
        self.assertEqual(b'line1', var2681)
        var3714.unread_data(var2681)
        var2681 = self.attribute1361.run_until_complete(var3714.read(5))
        self.assertEqual(b'line1', var2681)
        var2681 = self.attribute1361.run_until_complete(var3714.read(4))
        self.assertEqual(b'line', var2681)
        var3714.unread_data(b'line1line')
        var2681 = b''
        while (len(var2681) < 10):
            var2681 += self.attribute1361.run_until_complete(var3714.read(10))
        self.assertEqual(b'line1line2', var2681)
        var2681 = self.attribute1361.run_until_complete(var3714.read(7))
        self.assertEqual(b'onemore', var2681)
        var3714.unread_data(var2681)
        var2681 = b''
        while (len(var2681) < 11):
            var2681 += self.attribute1361.run_until_complete(var3714.read(11))
        self.assertEqual(b'onemoreline', var2681)
        var3714.unread_data(b'line')
        var2681 = self.attribute1361.run_until_complete(var3714.read(4))
        self.assertEqual(b'line', var2681)
        var3714.feed_eof()
        var3714.unread_data(b'at_eof')
        var2681 = self.attribute1361.run_until_complete(var3714.read(6))
        self.assertEqual(b'at_eof', var2681)

    def function2515(self):
        var2370 = self.function1833()
        self.assertIsNone(var2370.exception())
        var3234 = ValueError()
        var2370.set_exception(var3234)
        self.assertIs(var2370.exception(), var3234)

    def function128(self):
        var749 = self.function1833()

        @asyncio.coroutine
        def function429():
            var749.set_exception(ValueError())
        var758 = asyncio.Task(var749.readline(), loop=self.attribute1361)
        var3966 = asyncio.Task(function429(), loop=self.attribute1361)
        self.attribute1361.run_until_complete(asyncio.wait([var758, var3966], loop=self.attribute1361))
        self.assertRaises(ValueError, var758.result)

    def function261(self):
        var398 = self.function1833()

        @asyncio.coroutine
        def function2165():
            yield from var398.readline()
        var1888 = asyncio.Task(function2165(), loop=self.attribute1361)
        test_utils.run_briefly(self.attribute1361)
        var1888.cancel()
        test_utils.run_briefly(self.attribute1361)
        var398.set_exception(RuntimeError('message'))
        test_utils.run_briefly(self.attribute1361)
        self.assertIs(var398._waiter, None)

    def function1714(self):
        var1513 = self.function1833()
        var2412 = asyncio.Task(var1513.readany(), loop=self.attribute1361)
        self.attribute1361.call_soon(var1513.feed_data, b'chunk1\n')
        var3150 = self.attribute1361.run_until_complete(var2412)
        self.assertEqual(b'chunk1\n', var3150)
        var1513.feed_eof()
        var3150 = self.attribute1361.run_until_complete(var1513.read())
        self.assertEqual(b'', var3150)

    def function1812(self):
        var270 = self.function1833()
        var270.feed_eof()
        var3375 = asyncio.Task(var270.readany(), loop=self.attribute1361)
        var2132 = self.attribute1361.run_until_complete(var3375)
        self.assertEqual(b'', var2132)

    def function1644(self):
        var2331 = self.function1833()
        var2331.feed_data(b'line\n')
        var2859 = self.attribute1361.run_until_complete(var2331.readany())
        self.assertEqual(b'line\n', var2859)
        var2331.set_exception(ValueError())
        self.assertRaises(ValueError, self.attribute1361.run_until_complete, var2331.readany())

    def function559(self):
        var3923 = self.function1833()
        var3923.feed_data(b'line1\nline2\n')
        self.assertEqual(var3923.read_nowait(), b'line1\nline2\n')
        self.assertEqual(var3923.read_nowait(), b'')
        var3923.feed_eof()
        var4403 = self.attribute1361.run_until_complete(var3923.read())
        self.assertEqual(b'', var4403)

    def function1972(self):
        var3036 = self.function1833()
        var3036.feed_data(b'line1\nline2\n')
        self.assertEqual(var3036.read_nowait(4), b'line')
        self.assertEqual(var3036.read_nowait(), b'1\nline2\n')
        self.assertEqual(var3036.read_nowait(), b'')
        var3036.feed_eof()
        var1541 = self.attribute1361.run_until_complete(var3036.read())
        self.assertEqual(b'', var1541)

    def function1083(self):
        var3562 = self.function1833()
        var3562.feed_data(b'line\n')
        var3562.set_exception(ValueError())
        self.assertRaises(ValueError, var3562.read_nowait)

    def function2421(self):
        var938 = self.function1833()
        var938.feed_data(b'line\n')
        var938._waiter = helpers.create_future(self.attribute1361)
        self.assertRaises(RuntimeError, var938.read_nowait)

    def function2709(self):
        var189 = self.function1833()

        def function2225():
            var189.feed_data(b'chunk1')
            var189.feed_data(b'chunk2')
            var189.feed_eof()
        self.attribute1361.call_soon(function2225)
        var154 = self.attribute1361.run_until_complete(var189.readchunk())
        self.assertEqual(b'chunk1', var154)
        var154 = self.attribute1361.run_until_complete(var189.readchunk())
        self.assertEqual(b'chunk2', var154)
        var154 = self.attribute1361.run_until_complete(var189.read())
        self.assertEqual(b'', var154)

    def function1601(self):
        var2754 = self.function1833()
        self.assertEqual('<StreamReader>', repr(var2754))

    def function2875(self):
        var1491 = self.function1833(limit=123)
        self.assertEqual('<StreamReader l=123>', repr(var1491))

    def function1034(self):
        var571 = self.function1833()
        var571.feed_eof()
        self.assertEqual('<StreamReader eof>', repr(var571))

    def function1427(self):
        var3255 = self.function1833()
        var3255.feed_data(b'data')
        self.assertEqual('<StreamReader 4 bytes>', repr(var3255))

    def function2659(self):
        var2100 = self.function1833()
        var2125 = RuntimeError()
        var2100.set_exception(var2125)
        self.assertEqual('<StreamReader e=RuntimeError()>', repr(var2100))

    def function933(self):
        var1613 = self.function1833()
        var1613._waiter = helpers.create_future(self.attribute1361)
        self.assertRegex(repr(var1613), '<StreamReader w=<Future pending[\\S ]*>>')
        var1613._waiter.set_result(None)
        self.attribute1361.run_until_complete(var1613._waiter)
        var1613._waiter = None
        self.assertEqual('<StreamReader>', repr(var1613))

    def function2519(self):
        var2590 = self.function1833()
        var2590.feed_data(b'line1')
        var2590.feed_eof()
        var2590.unread_data(b'')
        var194 = self.attribute1361.run_until_complete(var2590.read(5))
        self.assertEqual(b'line1', var194)
        self.assertTrue(var2590.at_eof())


class Class62(unittest.TestCase):

    def function2443(self):
        self.attribute836 = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def function1907(self):
        self.attribute836.close()

    def function2520(self):
        var1588 = streams.EmptyStreamReader()
        self.assertIsNone(var1588.set_exception(ValueError()))
        self.assertIsNone(var1588.exception())
        self.assertIsNone(var1588.feed_eof())
        self.assertIsNone(var1588.feed_data(b'data'))
        self.assertTrue(var1588.at_eof())
        self.assertIsNone(self.attribute836.run_until_complete(var1588.wait_eof()))
        self.assertEqual(self.attribute836.run_until_complete(var1588.read()), b'')
        self.assertEqual(self.attribute836.run_until_complete(var1588.readline()), b'')
        self.assertEqual(self.attribute836.run_until_complete(var1588.readany()), b'')
        self.assertEqual(self.attribute836.run_until_complete(var1588.readchunk()), b'')
        self.assertRaises(asyncio.IncompleteReadError, self.attribute836.run_until_complete, var1588.readexactly(10))
        self.assertEqual(var1588.read_nowait(), b'')


class Class305:

    def function1333(self):
        self.assertFalse(self.attribute1580.is_eof())
        self.attribute1580.feed_eof()
        self.assertTrue(self.attribute1580.is_eof())

    def function1899(self):
        self.assertFalse(self.attribute1580.at_eof())
        self.attribute1580.feed_eof()
        self.assertTrue(self.attribute1580.at_eof())
        self.attribute1580._buffer.append(object())
        self.assertFalse(self.attribute1580.at_eof())

    def function313(self):
        var1164 = object()
        self.attribute1580.feed_data(var1164, 1)
        self.assertEqual([(var1164, 1)], list(self.attribute1580._buffer))

    def function698(self):
        self.attribute1580.feed_eof()
        self.assertTrue(self.attribute1580._eof)

    def function434(self):
        var1986 = object()
        var3215 = asyncio.Task(self.attribute1580.read(), loop=self.attribute1349)

        def function2795():
            self.attribute1580.feed_data(var1986, 1)
        self.attribute1349.call_soon(function2795)
        var3121 = self.attribute1349.run_until_complete(var3215)
        self.assertIs(var1986, var3121)

    def function2218(self):
        var3356 = asyncio.Task(self.attribute1580.read(), loop=self.attribute1349)

        def function806():
            self.attribute1580.feed_eof()
        self.attribute1349.call_soon(function806)
        self.assertRaises(streams.EofStream, self.attribute1349.run_until_complete, var3356)

    def function263(self):
        var1258 = asyncio.Task(self.attribute1580.read(), loop=self.attribute1349)
        test_utils.run_briefly(self.attribute1349)
        var4149 = self.attribute1580._waiter
        self.assertTrue(helpers.isfuture(var4149))
        var1258.cancel()
        self.assertRaises(asyncio.CancelledError, self.attribute1349.run_until_complete, var1258)
        self.assertTrue(var4149.cancelled())
        self.assertIsNone(self.attribute1580._waiter)
        self.attribute1580.feed_data(b'test', 4)
        self.assertIsNone(self.attribute1580._waiter)

    def function2026(self):
        var2729 = object()
        self.attribute1580.feed_data(var2729, 1)
        self.attribute1580.feed_eof()
        var1119 = self.attribute1349.run_until_complete(self.attribute1580.read())
        self.assertIs(var1119, var2729)
        self.assertRaises(streams.EofStream, self.attribute1349.run_until_complete, self.attribute1580.read())

    def function653(self):
        var849 = object()
        self.attribute1580.feed_data(var849)
        self.attribute1580.set_exception(ValueError)
        var4725 = asyncio.Task(self.attribute1580.read(), loop=self.attribute1349)
        var2696 = self.attribute1349.run_until_complete(var4725)
        self.assertIs(var849, var2696)
        self.assertRaises(ValueError, self.attribute1349.run_until_complete, self.attribute1580.read())

    def function1426(self):
        self.attribute1580.set_exception(ValueError())
        self.assertRaises(ValueError, self.attribute1349.run_until_complete, self.attribute1580.read())

    def function2700(self):
        var4452 = object()
        self.attribute1580.feed_data(var4452, 1)
        self.attribute1580.set_exception(ValueError())
        self.assertIs(var4452, self.attribute1349.run_until_complete(self.attribute1580.read()))
        self.assertRaises(ValueError, self.attribute1349.run_until_complete, self.attribute1580.read())

    def function1129(self):
        var1390 = asyncio.Task(self.attribute1580.read(), loop=self.attribute1349)
        test_utils.run_briefly(self.attribute1349)
        self.assertTrue(helpers.isfuture(self.attribute1580._waiter))
        self.attribute1580.feed_eof()
        self.attribute1580.set_exception(ValueError())
        self.assertRaises(ValueError, self.attribute1349.run_until_complete, var1390)

    def function1246(self):
        self.assertIsNone(self.attribute1580.exception())
        var1611 = ValueError()
        self.attribute1580.set_exception(var1611)
        self.assertIs(self.attribute1580.exception(), var1611)

    def function2476(self):

        @asyncio.coroutine
        def function480():
            self.attribute1580.set_exception(ValueError())
        var2076 = asyncio.Task(self.attribute1580.read(), loop=self.attribute1349)
        var3767 = asyncio.Task(function480(), loop=self.attribute1349)
        self.attribute1349.run_until_complete(asyncio.wait([var2076, var3767], loop=self.attribute1349))
        self.assertRaises(ValueError, var2076.result)


class Class349(unittest.TestCase, Class305):

    def function2317(self):
        self.attribute2153 = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
        self.attribute1647 = streams.DataQueue(loop=self.attribute2153)

    def function1779(self):
        self.attribute2153.close()


class Class40(unittest.TestCase, Class305):

    def function618(self):
        self.attribute1349 = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
        self.attribute1580 = streams.ChunksQueue(loop=self.attribute1349)

    def function840(self):
        self.attribute1349.close()

    def function1084(self):
        var3313 = asyncio.Task(self.attribute1580.read(), loop=self.attribute1349)

        def function1338():
            self.attribute1580.feed_eof()
        self.attribute1349.call_soon(function1338)
        self.attribute1349.run_until_complete(var3313)
        self.assertTrue(self.attribute1580.at_eof())

    def function289(self):
        var3044 = object()
        self.attribute1580.feed_data(var3044, 1)
        self.attribute1580.feed_eof()
        var3902 = self.attribute1349.run_until_complete(self.attribute1580.read())
        self.assertIs(var3902, var3044)
        var641 = self.attribute1349.run_until_complete(self.attribute1580.read())
        self.assertEqual(var641, b'')
        self.assertTrue(self.attribute1580.at_eof())

    def function66(self):
        self.assertIs(self.attribute1580.read.__func__, self.attribute1580.readany.__func__)

def function569(arg1357):
    var1577 = streams.StreamReader(loop=arg1357)
    var2495 = var1577._waiter = helpers.create_future(arg1357)
    var1147 = var1577._eof_waiter = helpers.create_future(arg1357)
    var1577.feed_data(b'1')
    assert (list(var1577._buffer) == [b'1'])
    assert (var1577._size == 1)
    assert (var1577.total_bytes == 1)
    assert var2495.done()
    assert (not var1147.done())
    assert (var1577._waiter is None)
    assert (var1577._eof_waiter is var1147)

def function1653(arg2258):
    var1775 = streams.StreamReader(loop=arg2258)
    var1128 = var1775._waiter = helpers.create_future(arg2258)
    var1128.set_result(1)
    var1775.feed_data(b'1')
    assert (var1775._waiter is None)

def function2024(arg1422):
    var2649 = streams.StreamReader(loop=arg1422)
    var311 = var2649._waiter = helpers.create_future(arg1422)
    var817 = var2649._eof_waiter = helpers.create_future(arg1422)
    var2649.feed_eof()
    assert var2649._eof
    assert var311.done()
    assert var817.done()
    assert (var2649._waiter is None)
    assert (var2649._eof_waiter is None)

def function12(arg2332):
    var3845 = streams.StreamReader(loop=arg2332)
    var390 = var3845._waiter = helpers.create_future(arg2332)
    var3097 = var3845._eof_waiter = helpers.create_future(arg2332)
    var390.set_result(1)
    var3097.set_result(1)
    var3845.feed_eof()
    assert var390.done()
    assert var3097.done()
    assert (var3845._waiter is None)
    assert (var3845._eof_waiter is None)

def function716(arg2093):
    var1473 = streams.StreamReader(loop=arg2093)
    var3245 = mock.Mock()
    var1473.var3245(var3245)
    assert (not var3245.called)
    var1473.feed_eof()
    assert var3245.called

def function2864(arg2074):
    var2958 = streams.EmptyStreamReader()
    var506 = mock.Mock()
    var2958.var506(var506)
    assert var506.called

def function351(arg755):
    var1479 = streams.StreamReader(loop=arg755)
    var3761 = mock.Mock()
    var3761.side_effect = ValueError
    var1479.var3761(var3761)
    assert (not var3761.called)
    var1479.feed_eof()
    assert var3761.called
    assert (not var1479._eof_callbacks)

def function605(arg276):
    var3909 = streams.EmptyStreamReader()
    var2028 = mock.Mock()
    var2028.side_effect = ValueError
    var3909.var2028(var2028)
    assert var2028.called

def function983(arg800):
    var292 = streams.StreamReader(loop=arg800)
    var292.feed_eof()
    var4742 = mock.Mock()
    var292.var4742(var4742)
    assert var4742.called
    assert (not var292._eof_callbacks)

def function107(arg555):
    var4578 = streams.StreamReader(loop=arg555)
    var4578.feed_eof()
    var2516 = mock.Mock()
    var2516.side_effect = ValueError
    var4578.var2516(var2516)
    assert var2516.called
    assert (not var4578._eof_callbacks)

def function887(arg1438):
    var3801 = streams.StreamReader(loop=arg1438)
    var2954 = var3801._waiter = helpers.create_future(arg1438)
    var2415 = var3801._eof_waiter = helpers.create_future(arg1438)
    var2468 = ValueError()
    var3801.set_exception(var2468)
    assert (var2954.exception() is var2468)
    assert (var2415.exception() is var2468)
    assert (var3801._waiter is None)
    assert (var3801._eof_waiter is None)

def function2145(arg180):
    var1226 = streams.StreamReader(loop=arg180)
    var3512 = var1226._waiter = helpers.create_future(arg180)
    var1757 = var1226._eof_waiter = helpers.create_future(arg180)
    var3512.set_result(1)
    var1757.set_result(1)
    var2994 = ValueError()
    var1226.set_exception(var2994)
    assert (var3512.exception() is None)
    assert (var1757.exception() is None)
    assert (var1226._waiter is None)
    assert (var1226._eof_waiter is None)

def function1068(arg695):
    var1730 = streams.StreamReader(loop=arg695)
    var932 = mock.Mock()
    var1730.var932(var932)
    var1730.set_exception(ValueError())
    assert (not var932.called)
    assert (not var1730._eof_callbacks)