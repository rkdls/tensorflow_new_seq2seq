import asyncio
import unittest
from unittest import mock
from aiohttp import streams


class Class1(unittest.TestCase):

    def function1686(self):
        self.attribute2260 = mock.Mock(_reading_paused=False)
        self.attribute1175 = self.attribute2260.transport
        self.attribute2182 = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def function2447(self):
        self.attribute2182.close()

    def function959(self, arg455=True, *args, **kwargs):
        var3944 = streams.FlowControlStreamReader(self.attribute2260, *args, buffer_limit=1, loop=self.attribute2182, None=kwargs)
        var3944._allow_pause = arg455
        return var3944

    def function639(self):
        var4693 = self.function959()
        var4693.feed_data(b'da', 2)
        var1540 = self.attribute2182.run_until_complete(var4693.read(1))
        self.assertEqual(var1540, b'd')
        self.assertFalse(var4693._protocol.resume_reading.called)

    def function289(self):
        var4319 = self.function959()
        var4319.feed_data(b'test', 4)
        var4319._protocol._reading_paused = True
        var3564 = self.attribute2182.run_until_complete(var4319.read(1))
        self.assertEqual(var3564, b't')
        self.assertTrue(var4319._protocol.pause_reading.called)

    def function281(self):
        var2549 = self.function959()
        var2549.feed_data(b'data\n', 5)
        var756 = self.attribute2182.run_until_complete(var2549.readline())
        self.assertEqual(var756, b'data\n')
        self.assertFalse(var2549._protocol.resume_reading.called)

    def function1710(self):
        var2031 = self.function959()
        var2031._protocol._reading_paused = True
        var2031.feed_data(b'data\n', 5)
        var195 = self.attribute2182.run_until_complete(var2031.readline())
        self.assertEqual(var195, b'data\n')
        self.assertTrue(var2031._protocol.resume_reading.called)

    def function573(self):
        var2043 = self.function959()
        var2043.feed_data(b'data', 4)
        var482 = self.attribute2182.run_until_complete(var2043.readany())
        self.assertEqual(var482, b'data')
        self.assertFalse(var2043._protocol.resume_reading.called)

    def function724(self):
        var726 = self.function959()
        var726._protocol._reading_paused = True
        var726.feed_data(b'data', 4)
        var51 = self.attribute2182.run_until_complete(var726.readany())
        self.assertEqual(var51, b'data')
        self.assertTrue(var726._protocol.resume_reading.called)

    def function938(self):
        var3877 = self.function959()
        var3877.feed_data(b'data', 4)
        var4562 = self.attribute2182.run_until_complete(var3877.readchunk())
        self.assertEqual(var4562, b'data')
        self.assertFalse(var3877._protocol.resume_reading.called)

    def function1835(self):
        var112 = self.function959()
        var112._protocol._reading_paused = True
        var112.feed_data(b'data', 4)
        var413 = self.attribute2182.run_until_complete(var112.readchunk())
        self.assertEqual(var413, b'data')
        self.assertTrue(var112._protocol.resume_reading.called)

    def function591(self):
        var3124 = self.function959()
        var3124.feed_data(b'data', 4)
        var2281 = self.attribute2182.run_until_complete(var3124.readexactly(3))
        self.assertEqual(var2281, b'dat')
        self.assertFalse(var3124._protocol.resume_reading.called)

    def function1477(self):
        var4683 = self.function959()
        var4683._protocol._reading_paused = True
        var4683.feed_data(b'data', 4)
        var2459 = self.attribute2182.run_until_complete(var4683.readexactly(3))
        self.assertEqual(var2459, b'dat')
        self.assertTrue(var4683._protocol.resume_reading.called)

    def function1225(self):
        var4514 = self.function959()
        var4514._protocol._reading_paused = False
        var4514.feed_data(b'datadata', 8)
        self.assertTrue(var4514._protocol.pause_reading.called)

    def function1175(self):
        var924 = self.function959()
        var924._protocol._reading_paused = True
        var924.feed_data(b'data1', 5)
        var924.feed_data(b'data2', 5)
        var924.feed_data(b'data3', 5)
        var4059 = self.attribute2182.run_until_complete(var924.read(5))
        self.assertTrue((var4059 == b'data1'))
        self.assertTrue((var924._protocol.resume_reading.call_count == 0))
        var4059 = var924.read_nowait(5)
        self.assertTrue((var4059 == b'data2'))
        self.assertTrue((var924._protocol.resume_reading.call_count == 0))
        var4059 = var924.read_nowait(5)
        self.assertTrue((var4059 == b'data3'))
        self.assertTrue((var924._protocol.resume_reading.call_count == 1))
        var924._protocol._reading_paused = False
        var4059 = var924.read_nowait(5)
        self.assertTrue((var4059 == b''))
        self.assertTrue((var924._protocol.resume_reading.call_count == 1))


class Class150:

    def function2510(self):
        var4128 = self.function79()
        var4128._protocol._reading_paused = False
        var4128.feed_data(object(), 100)
        self.assertTrue(var4128._protocol.pause_reading.called)

    def function642(self):
        var177 = self.function79()
        var177.feed_data(object(), 100)
        var177._protocol._reading_paused = True
        self.attribute1235.run_until_complete(var177.read())
        self.assertTrue(var177._protocol.resume_reading.called)


class Class357(unittest.TestCase, Class150):

    def function2769(self):
        self.attribute1808 = mock.Mock()
        self.attribute1376 = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def function2070(self):
        self.attribute1376.close()

    def function2883(self, *args, **kwargs):
        var4517 = streams.FlowControlDataQueue(self.attribute1808, *args, limit=1, loop=self.attribute1376, None=kwargs)
        var4517._allow_pause = True
        return var4517


class Class349(unittest.TestCase, Class150):

    def function2457(self):
        self.attribute1975 = mock.Mock()
        self.attribute1235 = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def function2549(self):
        self.attribute1235.close()

    def function79(self, *args, **kwargs):
        var4397 = streams.FlowControlChunksQueue(self.attribute1975, *args, limit=1, loop=self.attribute1235, None=kwargs)
        var4397._allow_pause = True
        return var4397

    def function796(self):
        var4237 = self.function79()
        var4203 = asyncio.Task(var4237.read(), loop=self.attribute1235)

        def function2330():
            var4237.feed_eof()
        self.attribute1235.call_soon(function2330)
        self.attribute1235.run_until_complete(var4203)
        self.assertTrue(var4237.at_eof())

    def function415(self):
        var1808 = object()
        var4575 = self.function79()
        var4575.feed_data(var1808, 1)
        var4575.feed_eof()
        var1366 = self.attribute1235.run_until_complete(var4575.read())
        self.assertIs(var1366, var1808)
        var3048 = self.attribute1235.run_until_complete(var4575.read())
        self.assertEqual(var3048, b'')
        self.assertTrue(var4575.at_eof())

    def function2773(self):
        var1656 = self.function79()
        self.assertIs(var1656.read.__func__, var1656.readany.__func__)