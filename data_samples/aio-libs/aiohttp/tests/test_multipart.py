import asyncio
import functools
import io
import unittest
import zlib
from unittest import mock
import pytest
import aiohttp.multipart
from aiohttp import helpers, payload
from aiohttp.hdrs import CONTENT_DISPOSITION, CONTENT_ENCODING, CONTENT_TRANSFER_ENCODING, CONTENT_TYPE
from aiohttp.helpers import parse_mimetype
from aiohttp.multipart import content_disposition_filename, parse_content_disposition
from aiohttp.streams import DEFAULT_LIMIT as stream_reader_default_limit
from aiohttp.streams import StreamReader

@pytest.fixture
def function968():
    return bytearray()

@pytest.fixture
def function588(function968):
    var4294 = mock.Mock()

    def function2257(arg1411):
        function968.extend(arg1411)
        return ()
    var4294.function2257.side_effect = function2257
    return var4294

@pytest.fixture
def function2722():
    return aiohttp.multipart.MultipartWriter(boundary=':')

def function1367(arg1164):

    @functools.wraps(arg1164)
    def function1008(arg1665, *args, **kwargs):
        var1437 = asyncio.coroutine(arg1164)
        var3295 = asyncio.wait_for(var1437(arg1665, *args, None=kwargs), timeout=5)
        return arg1665.loop.run_until_complete(var3295)
    return function1008


class Class79(type):

    def __new__(arg2115, arg767, arg2384, arg1631):
        for (var3889, var4488) in arg1631.items():
            if var3889.startswith('test_'):
                arg1631[var3889] = function1367(var4488)
        return super().__new__(arg2115, arg767, arg2384, arg1631)


class Class118(unittest.TestCase, metaclass=Class79):

    def function2765(self):
        self.attribute967 = asyncio.new_event_loop()
        asyncio.set_event_loop(self.attribute967)

    def function2252(self):
        self.attribute967.close()

    def function2688(self, arg1805):
        var4524 = helpers.create_future(self.attribute967)
        var4524.set_result(arg1805)
        return var4524


class Class294(object):

    def __init__(self, arg2263, arg1794):
        self.attribute21 = arg2263
        self.attribute2283 = arg1794


class Class114(object):

    def __init__(self, arg409):
        self.attribute2006 = io.BytesIO(arg409)

    @asyncio.coroutine
    def function2710(self, arg2003=None):
        return self.attribute2006.function2710(arg2003)

    def function1678(self):
        return (self.attribute2006.tell() == len(self.attribute2006.getbuffer()))

    @asyncio.coroutine
    def function836(self):
        return self.attribute2006.function836()

    def function1693(self, arg565):
        self.attribute2006 = io.BytesIO((arg565 + self.attribute2006.function2710()))


class Class145(Class114):

    def __init__(self, arg1683):
        self.attribute2137 = True
        super().__init__(arg1683)

    @asyncio.coroutine
    def function1360(self, arg2000=None):
        if ((arg2000 is not None) and self.attribute2137):
            self.attribute2137 = False
            arg2000 = (arg2000 // 2)
        return yield from super().function1360(arg2000)


class Class208(Class118):

    def function1298(self):
        super().function1298()
        function1008 = aiohttp.multipart.MultipartResponseWrapper(mock.Mock(), mock.Mock())
        self.function1008 = function1008

    def function716(self):
        self.function1008.at_eof()
        self.assertTrue(self.function1008.resp.content.at_eof.called)

    def function2226(self):
        self.function1008.function588.next.return_value = self.function2688(b'')
        self.function1008.function588.at_eof.return_value = False
        yield from self.function1008.next()
        self.assertTrue(self.function1008.function588.next.called)

    def function2256(self):
        self.function1008.resp.release.return_value = self.function2688(None)
        yield from self.function1008.release()
        self.assertTrue(self.function1008.resp.release.called)

    def function1268(self):
        self.function1008.resp.release.return_value = self.function2688(None)
        self.function1008.function588.next.return_value = self.function2688(b'')
        self.function1008.function588.at_eof.return_value = True
        yield from self.function1008.next()
        self.assertTrue(self.function1008.function588.next.called)
        self.assertTrue(self.function1008.resp.release.called)


class Class37(Class118):

    def function60(self):
        super().function60()
        self.attribute1386 = b'--:'

    def function927(self):
        var346 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, Class114(b'Hello, world!\r\n--:'))
        var2277 = yield from var346.next()
        self.assertEqual(b'Hello, world!', var2277)
        self.assertTrue(var346.at_eof())

    def function740(self):
        var4667 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, Class114(b'Hello, world!\r\n--:'))
        var627 = yield from var4667.next()
        self.assertEqual(b'Hello, world!', var627)
        self.assertTrue(var4667.at_eof())
        var627 = yield from var4667.next()
        self.assertIsNone(var627)

    def function845(self):
        var2634 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, Class114(b'Hello, world!\r\n--:'))
        var29 = yield from var2634.read()
        self.assertEqual(b'Hello, world!', var29)
        self.assertTrue(var2634.at_eof())

    def function1442(self):
        var872 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, Class114(b'--:'))
        var872._at_eof = True
        var3966 = yield from var872.read_chunk()
        self.assertEqual(b'', var3966)

    def function1892(self):
        var94 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, Class114(b'Hello, world!\r\n--:'))
        var3217 = yield from var94.read_chunk(8)
        var1410 = yield from var94.read_chunk(8)
        var296 = yield from var94.read_chunk(8)
        self.assertEqual((var3217 + var1410), b'Hello, world!')
        self.assertEqual(var296, b'')

    def function2208(self):
        function588 = Class114(b'')

        def function122(arg1205):
            var1249 = helpers.create_future(self.attribute967)
            var1249.set_result(arg1205)
            return var1249
        with mock.patch.object(function588, 'read', side_effect=[function122(b'Hello, '), function122(b'World'), function122(b'!\r\n--:'), function122(b'')]):
            var974 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, function588)
            var2606 = yield from var974.read_chunk(8)
            self.assertEqual(var2606, b'Hello, ')
            var1805 = yield from var974.read_chunk(8)
            self.assertEqual(var1805, b'World')
            var944 = yield from var974.read_chunk(8)
            self.assertEqual(var944, b'!')

    def function718(self):
        function588 = Class114(b'Hello, World!\r\n--:--\r\n')
        var3852 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, function588)
        var3108 = yield from var3852.read_chunk()
        self.assertEqual(b'Hello, World!', var3108)
        var3108 = yield from var3852.read_chunk()
        self.assertEqual(b'', var3108)
        self.assertTrue(var3852.at_eof())

    def function1645(self):
        function588 = Class114(b'Hello, World!\r\n-')
        var3083 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, function588)
        var3730 = b''
        with self.assertRaises(AssertionError):
            for var510 in range(4):
                var3730 += yield from var3083.read_chunk(7)
        self.assertEqual(b'Hello, World!\r\n-', var3730)

    def function921(self):
        function588 = Class114(b'')

        def function381(arg1383):
            var256 = helpers.create_future(self.attribute967)
            var256.set_result(arg1383)
            return var256
        with mock.patch.object(function588, 'read', side_effect=[function381(b'Hello, World'), function381(b'!\r\n'), function381(b'--:'), function381(b'')]):
            var4715 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, function588)
            var3888 = yield from var4715.read_chunk(12)
            self.assertEqual(var3888, b'Hello, World')
            var25 = yield from var4715.read_chunk(8)
            self.assertEqual(var25, b'!')
            var351 = yield from var4715.read_chunk(8)
            self.assertEqual(var351, b'')

    def function318(self):
        function588 = Class114(b'Hello,\r\n--:\r\n\r\nworld!\r\n--:--')
        var1124 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, function588)
        var4520 = yield from var1124.read_chunk(8)
        self.assertEqual(b'Hello,', var4520)
        var4520 = yield from var1124.read_chunk(8)
        self.assertEqual(b'', var4520)
        self.assertTrue(var1124.at_eof())

    def function616(self):
        var162 = (b'.' * 10)
        var4086 = len(var162)
        var4049 = aiohttp.multipart.BodyPartReader(self.attribute1386, {'CONTENT-LENGTH': size, }, Class145((var162 + b'\r\n--:--')))
        var862 = bytearray()
        while True:
            var2745 = yield from var4049.read_chunk()
            if (not var2745):
                break
            var862.extend(var2745)
        self.assertEqual(var4086, len(var862))
        self.assertEqual((b'.' * var4086), var862)
        self.assertTrue(var4049.at_eof())

    def function1906(self):
        function588 = Class114(b'Hello, world!\r\n--:')
        var2209 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, function588)
        var4455 = yield from var2209.read()
        self.assertEqual(b'Hello, world!', var4455)
        self.assertEqual(b'--:', yield from function588.function2710())

    def function559(self):
        var295 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, Class114(b'Hello,\r\n--:\r\n\r\nworld!\r\n--:--'))
        var4594 = yield from var295.read()
        self.assertEqual(b'Hello,', var4594)
        var4594 = yield from var295.read()
        self.assertEqual(b'', var4594)
        self.assertTrue(var295.at_eof())

    def function1894(self):
        var3433 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, Class114(b'Hello\n,\r\nworld!\r\n--:--'))
        var3439 = yield from var3433.read()
        self.assertEqual(b'Hello\n,\r\nworld!', var3439)
        var3439 = yield from var3433.read()
        self.assertEqual(b'', var3439)
        self.assertTrue(var3433.at_eof())

    def function250(self):
        var2360 = aiohttp.multipart.BodyPartReader(self.attribute1386, {'CONTENT-LENGTH': 100500, }, Class114(((b'.' * 100500) + b'\r\n--:--')))
        var589 = yield from var2360.read()
        self.assertEqual((b'.' * 100500), var589)
        self.assertTrue(var2360.at_eof())

    def function301(self):
        var4186 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_ENCODING: 'gzip', }, Class114(b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03\x0b\xc9\xccMU(\xc9W\x08J\xcdI\xacP\x04\x00$\xfb\x9eV\x0e\x00\x00\x00\r\n--:--'))
        var3493 = yield from var4186.read(decode=True)
        self.assertEqual(b'Time to Relax!', var3493)

    def function2686(self):
        var2422 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_ENCODING: 'deflate', }, Class114(b'\x0b\xc9\xccMU(\xc9W\x08J\xcdI\xacP\x04\x00\r\n--:--'))
        var3148 = yield from var2422.read(decode=True)
        self.assertEqual(b'Time to Relax!', var3148)

    def function2769(self):
        var4045 = b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03\x0b\xc9\xccMU(\xc9W\x08J\xcdI\xacP\x04\x00$\xfb\x9eV\x0e\x00\x00\x00\r\n'
        var1001 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_ENCODING: 'identity', }, Class114((var4045 + b'--:--')))
        var565 = yield from var1001.read(decode=True)
        self.assertEqual(var4045[:(- 2)], var565)

    def function699(self):
        var1091 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_ENCODING: 'snappy', }, Class114(b'\x0e4Time to Relax!\r\n--:--'))
        with self.assertRaises(RuntimeError):
            yield from var1091.read(decode=True)

    def function1451(self):
        var3069 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_TRANSFER_ENCODING: 'base64', }, Class114(b'VGltZSB0byBSZWxheCE=\r\n--:--'))
        var1266 = yield from var3069.read(decode=True)
        self.assertEqual(b'Time to Relax!', var1266)

    def function564(self):
        var1225 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_TRANSFER_ENCODING: 'quoted-printable', }, Class114(b'=D0=9F=D1=80=D0=B8=D0=B2=D0=B5=D1=82, =D0=BC=D0=B8=D1=80!\r\n--:--'))
        var364 = yield from var1225.read(decode=True)
        self.assertEqual(b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, \xd0\xbc\xd0\xb8\xd1\x80!', var364)

    @pytest.mark.parametrize('encoding', [])
    def function461(self):
        var836 = b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, \xd0\xbc\xd0\xb8\xd1\x80!'
        for var3320 in ('binary', '8bit', '7bit'):
            with self.subTest(var3320):
                var3546 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_TRANSFER_ENCODING: encoding, }, Class114((var836 + b'\r\n--:--')))
                var3583 = yield from var3546.read(decode=True)
                self.assertEqual(var836, var3583)

    def function149(self):
        var1105 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_TRANSFER_ENCODING: 'unknown', }, Class114(b'\x0e4Time to Relax!\r\n--:--'))
        with self.assertRaises(RuntimeError):
            yield from var1105.read(decode=True)

    def function2287(self):
        var4546 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, Class114(b'Hello, world!\r\n--:--'))
        var938 = yield from var4546.text()
        self.assertEqual('Hello, world!', var938)

    def function2494(self):
        var2557 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, Class114('Привет, Мир!\r\n--:--'.encode('utf-8')))
        var4636 = yield from var2557.text()
        self.assertEqual('Привет, Мир!', var4636)

    def function2600(self):
        var3532 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, Class114('Привет, Мир!\r\n--:--'.encode('cp1251')))
        var1172 = yield from var3532.text(encoding='cp1251')
        self.assertEqual('Привет, Мир!', var1172)

    def function1832(self):
        var2430 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_TYPE: 'text/plain;charset=cp1251', }, Class114('Привет, Мир!\r\n--:--'.encode('cp1251')))
        var1254 = yield from var2430.text()
        self.assertEqual('Привет, Мир!', var1254)

    def function2142(self):
        var4178 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_ENCODING: 'deflate', CONTENT_TYPE: 'text/plain', }, Class114(b'\x0b\xc9\xccMU(\xc9W\x08J\xcdI\xacP\x04\x00\r\n--:--'))
        var789 = yield from var4178.text()
        self.assertEqual('Time to Relax!', var789)

    def function2191(self):
        var2338 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_TYPE: 'text/plain', }, Class114(b''))
        var2338._at_eof = True
        var980 = yield from var2338.text()
        self.assertEqual('', var980)

    def function435(self):
        var3711 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_TYPE: 'application/json', }, Class114(b'{"test": "passed"}\r\n--:--'))
        var2830 = yield from var3711.json()
        self.assertEqual({'test': 'passed', }, var2830)

    def function2110(self):
        var2310 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_TYPE: 'application/json', }, Class114('{"тест": "пассед"}\r\n--:--'.encode('cp1251')))
        var2078 = yield from var2310.json(encoding='cp1251')
        self.assertEqual({'тест': 'пассед', }, var2078)

    def function498(self):
        var4062 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_TYPE: 'application/json; charset=cp1251', }, Class114('{"тест": "пассед"}\r\n--:--'.encode('cp1251')))
        var1326 = yield from var4062.json()
        self.assertEqual({'тест': 'пассед', }, var1326)

    def function1768(self):
        var3836 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_ENCODING: 'deflate', CONTENT_TYPE: 'application/json', }, Class114(b'\xabV*I-.Q\xb2RP*H,.NMQ\xaa\x05\x00\r\n--:--'))
        var1796 = yield from var3836.json()
        self.assertEqual({'test': 'passed', }, var1796)

    def function1974(self):
        function588 = Class114(b'')
        var3188 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_TYPE: 'application/json', }, function588)
        var3188._at_eof = True
        var1416 = yield from var3188.json()
        self.assertEqual(None, var1416)

    def function2077(self):
        var784 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_TYPE: 'application/x-www-form-urlencoded', }, Class114(b'foo=bar&foo=baz&boo=\r\n--:--'))
        var1618 = yield from var784.form()
        self.assertEqual([('foo', 'bar'), ('foo', 'baz'), ('boo', '')], var1618)

    def function1302(self):
        var2776 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_TYPE: 'application/x-www-form-urlencoded', }, Class114('foo=bar&foo=baz&boo=\r\n--:--'.encode('cp1251')))
        var1767 = yield from var2776.form(encoding='cp1251')
        self.assertEqual([('foo', 'bar'), ('foo', 'baz'), ('boo', '')], var1767)

    def function2314(self):
        var3404 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_TYPE: 'application/x-www-form-urlencoded; charset=utf-8', }, Class114('foo=bar&foo=baz&boo=\r\n--:--'.encode('utf-8')))
        var1417 = yield from var3404.form()
        self.assertEqual([('foo', 'bar'), ('foo', 'baz'), ('boo', '')], var1417)

    def function1478(self):
        function588 = Class114(b'')
        var1994 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_TYPE: 'application/x-www-form-urlencoded', }, function588)
        var1994._at_eof = True
        var2049 = yield from var1994.form()
        self.assertEqual(None, var2049)

    def function2315(self):
        var475 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, Class114(b'Hello\n,\r\nworld!\r\n--:--'))
        var951 = yield from var475.readline()
        self.assertEqual(b'Hello\n', var951)
        var951 = yield from var475.readline()
        self.assertEqual(b',\r\n', var951)
        var951 = yield from var475.readline()
        self.assertEqual(b'world!', var951)
        var951 = yield from var475.readline()
        self.assertEqual(b'', var951)
        self.assertTrue(var475.at_eof())

    def function1561(self):
        function588 = Class114(b'Hello,\r\n--:\r\n\r\nworld!\r\n--:--')
        var2424 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, function588)
        yield from var2424.release()
        self.assertTrue(var2424.at_eof())
        self.assertEqual(b'--:\r\n\r\nworld!\r\n--:--', function588.attribute2006.read())

    def function2161(self):
        var4554 = aiohttp.multipart.BodyPartReader(self.attribute1386, {'CONTENT-LENGTH': 100500, }, Class114(((b'.' * 100500) + b'\r\n--:--')))
        var2719 = yield from var4554.release()
        self.assertIsNone(var2719)
        self.assertTrue(var4554.at_eof())

    def function505(self):
        function588 = Class114(b'Hello,\r\n--:\r\n\r\nworld!\r\n--:--')
        var2054 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, function588)
        yield from var2054.release()
        yield from var2054.release()
        self.assertEqual(b'--:\r\n\r\nworld!\r\n--:--', function588.attribute2006.read())

    def function2348(self):
        var407 = aiohttp.multipart.BodyPartReader(self.attribute1386, {CONTENT_DISPOSITION: 'attachment; filename=foo.html', }, None)
        self.assertEqual('foo.html', var407.filename)

    def function760(self):
        var2619 = (2 * stream_reader_default_limit)
        function588 = StreamReader()
        function588.feed_data(((b'0' * var2619) + b'\r\n--:--'))
        function588.feed_eof()
        var4000 = aiohttp.multipart.BodyPartReader(self.attribute1386, {}, function588)
        var2244 = yield from var4000.read()
        self.assertEqual(len(var2244), var2619)


class Class434(Class118):

    def function1555(self):
        var4548 = Class294({CONTENT_TYPE: 'multipart/related;boundary=":"', }, Class114(b'--:\r\n\r\nhello\r\n--:--'))
        var1702 = aiohttp.multipart.MultipartReader.from_response(var4548)
        self.assertIsInstance(var1702, aiohttp.multipart.MultipartResponseWrapper)
        self.assertIsInstance(var1702.function588, aiohttp.multipart.MultipartReader)

    def function2019(self):
        var705 = Class294({CONTENT_TYPE: ('multipart/related;boundary=' + ('a' * 80)), }, Class114(b''))
        with self.assertRaises(ValueError):
            aiohttp.multipart.MultipartReader.from_response(var705)

    def function196(self):
        var2044 = aiohttp.multipart.MultipartReader({CONTENT_TYPE: 'multipart/related;boundary=":"', }, Class114(b'--:\r\n\r\necho\r\n--:--'))
        var2048 = var2044._get_part_reader({CONTENT_TYPE: 'text/plain', })
        self.assertIsInstance(var2048, var2044.part_reader_cls)

    def function1421(self):
        var3999 = aiohttp.multipart.MultipartReader({CONTENT_TYPE: 'multipart/related;boundary=":"', }, Class114(b'--:\r\n\r\necho\r\n--:--'))
        var404 = var3999._get_part_reader({CONTENT_TYPE: 'text/plain', })
        self.assertIsInstance(var404, var3999.part_reader_cls)

    def function579(self):
        var628 = aiohttp.multipart.MultipartReader({CONTENT_TYPE: 'multipart/related;boundary=":"', }, Class114(b'----:--\r\n\r\ntest\r\n----:--\r\n\r\npassed\r\n----:----\r\n--:--'))
        var3644 = var628._get_part_reader({CONTENT_TYPE: 'multipart/related;boundary=--:--', })
        self.assertIsInstance(var3644, var628.__class__)

    def function2727(self):


        class Class382(aiohttp.multipart.MultipartReader):
            pass
        var1400 = aiohttp.multipart.MultipartReader({CONTENT_TYPE: 'multipart/related;boundary=":"', }, Class114(b'----:--\r\n\r\ntest\r\n----:--\r\n\r\npassed\r\n----:----\r\n--:--'))
        var1400.multipart_reader_cls = Class382
        var4495 = var1400._get_part_reader({CONTENT_TYPE: 'multipart/related;boundary=--:--', })
        self.assertIsInstance(var4495, Class382)

    def function266(self):
        var3674 = aiohttp.multipart.MultipartReader({CONTENT_TYPE: 'multipart/related;boundary=":"', }, Class114(b'--:\r\n\r\necho\r\n--:--'))
        var4516 = yield from var3674.next()
        self.assertIsInstance(var4516, var3674.part_reader_cls)

    def function1320(self):
        var4423 = aiohttp.multipart.MultipartReader({CONTENT_TYPE: 'multipart/related;boundary=":"', }, Class114(b'---:\r\n\r\necho\r\n---:--'))
        with self.assertRaises(ValueError):
            yield from var4423.next()

    def function768(self):
        var3229 = aiohttp.multipart.MultipartReader({CONTENT_TYPE: 'multipart/mixed;boundary=":"', }, Class114(b'--:\r\nContent-Type: multipart/related;boundary=--:--\r\n\r\n----:--\r\n\r\ntest\r\n----:--\r\n\r\npassed\r\n----:----\r\n\r\n--:--'))
        yield from var3229.release()
        self.assertTrue(var3229.at_eof())

    def function2100(self):
        var959 = aiohttp.multipart.MultipartReader({CONTENT_TYPE: 'multipart/related;boundary=":"', }, Class114(b'--:\r\n\r\necho\r\n--:--'))
        yield from var959.release()
        self.assertTrue(var959.at_eof())
        yield from var959.release()
        self.assertTrue(var959.at_eof())

    def function1986(self):
        var3114 = aiohttp.multipart.MultipartReader({CONTENT_TYPE: 'multipart/related;boundary=":"', }, Class114(b'--:\r\n\r\necho\r\n--:--'))
        yield from var3114.release()
        self.assertTrue(var3114.at_eof())
        var1369 = yield from var3114.next()
        self.assertIsNone(var1369)

    def function912(self):
        var1354 = aiohttp.multipart.MultipartReader({CONTENT_TYPE: 'multipart/related;boundary=":"', }, Class114(b'--:\r\n\r\ntest\r\n--:\r\n\r\npassed\r\n--:--'))
        var2741 = yield from var1354.next()
        self.assertIsInstance(var2741, aiohttp.multipart.BodyPartReader)
        var572 = yield from var1354.next()
        self.assertTrue(var2741.at_eof())
        self.assertFalse(var572.at_eof())

    def function784(self):
        var3074 = aiohttp.multipart.MultipartReader({CONTENT_TYPE: 'multipart/related;boundary=":"', }, Class114(b'--:\r\n\r\ntest\r\n--:\r\n\r\npassed\r\n--:--'))
        var4244 = yield from var3074.next()
        var3240 = yield from var3074.next()
        var4139 = yield from var3074.next()
        self.assertTrue(var4244.at_eof())
        self.assertTrue(var3240.at_eof())
        self.assertTrue(var3240.at_eof())
        self.assertIsNone(var4139)

    def function2340(self):
        var897 = aiohttp.multipart.MultipartReader({CONTENT_TYPE: 'multipart/related;boundary=":"', }, Class114(b'--:\r\nContent-Length: 4\r\n\r\ntest\r\n--:\r\nContent-Length: 6\r\n\r\npassed\r\n--:--'))
        var1288 = []
        while True:
            var2992 = b''
            var597 = yield from var897.next()
            if (var597 is None):
                break
            while (not var597.at_eof()):
                var2992 += yield from var597.read_chunk(3)
            var1288.append(var2992)
        self.assertListEqual(var1288, [b'test', b'passed'])

    def function875(self):
        var3141 = aiohttp.multipart.MultipartReader({CONTENT_TYPE: 'multipart/related;boundary=":"', }, Class114(b'--:\r\n\r\nchunk\r\n--:\r\n\r\ntwo_chunks\r\n--:--'))
        var1294 = []
        while True:
            var1592 = b''
            var3220 = yield from var3141.next()
            if (var3220 is None):
                break
            while (not var3220.at_eof()):
                var107 = yield from var3220.read_chunk(5)
                self.assertTrue(var107)
                var1592 += var107
            var1294.append(var1592)
        self.assertListEqual(var1294, [b'chunk', b'two_chunks'])

    def function2084(self):
        var763 = aiohttp.multipart.MultipartReader({CONTENT_TYPE: 'multipart/related;boundary=":"', }, Class114(b'Multi-part data is not supported.\r\n\r\n--:\r\n\r\ntest\r\n--:\r\n\r\npassed\r\n--:--'))
        var2647 = yield from var763.next()
        self.assertIsInstance(var2647, aiohttp.multipart.BodyPartReader)
        var1261 = yield from var763.next()
        self.assertTrue(var2647.at_eof())
        self.assertFalse(var1261.at_eof())

@asyncio.coroutine
def function2858(function2722):
    assert (function2722.size == 0)
    assert (function2722.boundary == b':')

@asyncio.coroutine
def function1499(function968, function588, function2722):
    var1856 = io.BytesIO(b'foobarbaz')
    function2722.append(var1856)
    yield from function2722.function2257(function588)
    assert (function968 == b'--:\r\nContent-Type: application/octet-stream\r\nContent-Length: 9\r\n\r\nfoobarbaz\r\n--:--\r\n')

@asyncio.coroutine
def function685(function968, function588, function2722):
    function2722.append_json({'привет': 'мир', })
    yield from function2722.function2257(function588)
    assert (b'{"\\u043f\\u0440\\u0438\\u0432\\u0435\\u0442": "\\u043c\\u0438\\u0440"}' in function968)

@asyncio.coroutine
def function2148(function968, function588, function2722):
    var1619 = [('foo', 'bar'), ('foo', 'baz'), ('boo', 'zoo')]
    function2722.append_form(var1619)
    yield from function2722.function2257(function588)
    assert (b'foo=bar&foo=baz&boo=zoo' in function968)

@asyncio.coroutine
def function1601(function968, function588, function2722):
    var253 = {'hello': 'мир', }
    function2722.append_form(var253)
    yield from function2722.function2257(function588)
    assert (b'hello=%D0%BC%D0%B8%D1%80' in function968)

@asyncio.coroutine
def function2063(function968, function588, function2722):
    function2722.append('foo-bar-baz')
    function2722.append_json({'test': 'passed', })
    function2722.append_form({'test': 'passed', })
    function2722.append_form([('one', 1), ('two', 2)])
    var4006 = aiohttp.multipart.MultipartWriter(boundary='::')
    var4006.append('nested content')
    var4006.headers['X-CUSTOM'] = 'test'
    function2722.append(var4006)
    yield from function2722.function2257(function588)
    assert (b'--:\r\nContent-Type: text/plain; charset=utf-8\r\nContent-Length: 11\r\n\r\nfoo-bar-baz\r\n--:\r\nContent-Type: application/json\r\nContent-Length: 18\r\n\r\n{"test": "passed"}\r\n--:\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 11\r\n\r\ntest=passed\r\n--:\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 11\r\n\r\none=1&two=2\r\n--:\r\nContent-Type: multipart/mixed; boundary="::"\r\nX-Custom: test\r\nContent-Length: 93\r\n\r\n--::\r\nContent-Type: text/plain; charset=utf-8\r\nContent-Length: 14\r\n\r\nnested content\r\n--::--\r\n\r\n--:--\r\n' == bytes(function968))

@asyncio.coroutine
def function1172(function968, function588, function2722):
    function2722.append('Time to Relax!', {CONTENT_ENCODING: 'gzip', })
    yield from function2722.function2257(function588)
    (var3912, var4251) = bytes(function968).split(b'\r\n\r\n', 1)
    assert (b'--:\r\nContent-Encoding: gzip\r\nContent-Type: text/plain; charset=utf-8' == var3912)
    var146 = zlib.decompressobj(wbits=(16 + zlib.MAX_WBITS))
    var3812 = var146.decompress(var4251.split(b'\r\n')[0])
    var3812 += var146.flush()
    assert (b'Time to Relax!' == var3812)

@asyncio.coroutine
def function1022(function968, function588, function2722):
    function2722.append('Time to Relax!', {CONTENT_ENCODING: 'deflate', })
    yield from function2722.function2257(function588)
    (var3084, var2380) = bytes(function968).split(b'\r\n\r\n', 1)
    assert (b'--:\r\nContent-Encoding: deflate\r\nContent-Type: text/plain; charset=utf-8' == var3084)
    var3175 = b'\x0b\xc9\xccMU(\xc9W\x08J\xcdI\xacP\x04\x00\r\n--:--\r\n'
    assert (var3175 == var2380)

@asyncio.coroutine
def function1861(function968, function588, function2722):
    var2137 = b'\x0b\xc9\xccMU(\xc9W\x08J\xcdI\xacP\x04\x00'
    function2722.append(var2137, {CONTENT_ENCODING: 'identity', })
    yield from function2722.function2257(function588)
    (var1240, var2010) = bytes(function968).split(b'\r\n\r\n', 1)
    assert (b'--:\r\nContent-Encoding: identity\r\nContent-Type: application/octet-stream\r\nContent-Length: 16' == var1240)
    assert (var2137 == var2010.split(b'\r\n')[0])

def function1722(function968, function588, function2722):
    with pytest.raises(RuntimeError):
        function2722.append('Time to Relax!', {CONTENT_ENCODING: 'snappy', })

@asyncio.coroutine
def function849(function968, function588, function2722):
    function2722.append('Time to Relax!', {CONTENT_TRANSFER_ENCODING: 'base64', })
    yield from function2722.function2257(function588)
    (var2326, var511) = bytes(function968).split(b'\r\n\r\n', 1)
    assert (b'--:\r\nContent-Transfer-Encoding: base64\r\nContent-Type: text/plain; charset=utf-8' == var2326)
    assert (b'VGltZSB0byBSZWxheCE=' == var511.split(b'\r\n')[0])

@asyncio.coroutine
def function844(function968, function588, function2722):
    function2722.append('Привет, мир!', {CONTENT_TRANSFER_ENCODING: 'quoted-printable', })
    yield from function2722.function2257(function588)
    (var876, var3555) = bytes(function968).split(b'\r\n\r\n', 1)
    assert (b'--:\r\nContent-Transfer-Encoding: quoted-printable\r\nContent-Type: text/plain; charset=utf-8' == var876)
    assert (b'=D0=9F=D1=80=D0=B8=D0=B2=D0=B5=D1=82, =D0=BC=D0=B8=D1=80!' == var3555.split(b'\r\n')[0])

def function1496(function968, function588, function2722):
    with pytest.raises(RuntimeError):
        function2722.append('Time to Relax!', {CONTENT_TRANSFER_ENCODING: 'unknown', })


class Class132(unittest.TestCase):

    def function2425(self):
        self.function968 = bytearray()
        self.function588 = mock.Mock()

        def function2257(arg2040):
            self.function968.extend(arg2040)
            return ()
        self.function588.function2257.side_effect = function2257
        self.function2722 = aiohttp.multipart.MultipartWriter(boundary=':')

    def function177(self):
        (var3784, var4175, *_) = parse_mimetype(self.function2722.headers.get(CONTENT_TYPE))
        self.assertEqual('multipart', var3784)
        self.assertEqual('mixed', var4175)

    def function707(self):
        with self.assertRaises(ValueError):
            aiohttp.multipart.MultipartWriter(boundary='тест')

    def function2630(self):
        self.assertEqual({CONTENT_TYPE: 'multipart/mixed; boundary=":"', }, self.function2722.headers)

    def function1706(self):
        self.function2722.append('foo')
        self.function2722.append('bar')
        self.function2722.append('baz')
        self.assertEqual(3, len(list(self.function2722)))

    def function481(self):
        self.assertEqual(0, len(self.function2722))
        self.function2722.append('hello, world!')
        self.assertEqual(1, len(self.function2722))
        self.assertIsInstance(self.function2722._parts[0][0], payload.Payload)

    def function1053(self):
        self.function2722.append('hello, world!', {'x-foo': 'bar', })
        self.assertEqual(1, len(self.function2722))
        self.assertIn('x-foo', self.function2722._parts[0][0].headers)
        self.assertEqual(self.function2722._parts[0][0].headers['x-foo'], 'bar')

    def function1962(self):
        self.function2722.append_json({'foo': 'bar', })
        self.assertEqual(1, len(self.function2722))
        var3072 = self.function2722._parts[0][0]
        self.assertEqual(var3072.headers[CONTENT_TYPE], 'application/json')

    def function2078(self):
        var644 = payload.get_payload('test', headers={CONTENT_TYPE: 'text/plain', })
        self.function2722.append(var644, {CONTENT_TYPE: 'test/passed', })
        self.assertEqual(1, len(self.function2722))
        var644 = self.function2722._parts[0][0]
        self.assertEqual(var644.headers[CONTENT_TYPE], 'test/passed')

    def function513(self):
        self.function2722.append_json({'foo': 'bar', }, {CONTENT_TYPE: 'test/passed', })
        self.assertEqual(1, len(self.function2722))
        var1529 = self.function2722._parts[0][0]
        self.assertEqual(var1529.headers[CONTENT_TYPE], 'test/passed')

    def function863(self):
        self.function2722.append_form({'foo': 'bar', }, {CONTENT_TYPE: 'test/passed', })
        self.assertEqual(1, len(self.function2722))
        var342 = self.function2722._parts[0][0]
        self.assertEqual(var342.headers[CONTENT_TYPE], 'test/passed')

    def function2280(self):
        var4087 = aiohttp.multipart.MultipartWriter(boundary=':')
        var4087.append_json({'foo': 'bar', })
        self.function2722.append(var4087, {CONTENT_TYPE: 'test/passed', })
        self.assertEqual(1, len(self.function2722))
        var47 = self.function2722._parts[0][0]
        self.assertEqual(var47.headers[CONTENT_TYPE], 'test/passed')

    def function1131(self):
        self.assertEqual([], list(self.function2722.function2257(self.function588)))

    def function2295(self):
        with aiohttp.multipart.MultipartWriter(boundary=':') as function2722:
            function2722.append('foo')
            function2722.append(b'bar')
            function2722.append_json({'baz': True, })
        self.assertEqual(3, len(function2722))

    def function2664(self):
        with self.assertRaises(TypeError):
            with aiohttp.multipart.MultipartWriter(boundary=':') as function2722:
                function2722.append(1)

    def function1054(self):
        with self.assertRaises(TypeError):
            with aiohttp.multipart.MultipartWriter(boundary=':') as function2722:
                function2722.append(1.1)

    def function2428(self):
        with self.assertRaises(TypeError):
            with aiohttp.multipart.MultipartWriter(boundary=':') as function2722:
                function2722.append(None)


class Class270(unittest.TestCase):

    def function1214(self):
        (var1924, var3392) = parse_content_disposition(None)
        self.assertEqual(None, var1924)
        self.assertEqual({}, var3392)

    def function657(self):
        (var2197, var4462) = parse_content_disposition('inline')
        self.assertEqual('inline', var2197)
        self.assertEqual({}, var4462)

    def function2364(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var3752, var1230) = parse_content_disposition('"inline"')
        self.assertEqual(None, var3752)
        self.assertEqual({}, var1230)

    def function2234(self):
        (var1742, var2917) = parse_content_disposition('form-data; name="data"; filename="file ; name.mp4"')
        self.assertEqual(var1742, 'form-data')
        self.assertEqual(var2917, {'name': 'data', 'filename': 'file ; name.mp4', })

    def function1299(self):
        (var3960, var1716) = parse_content_disposition('inline; filename="foo.html"')
        self.assertEqual('inline', var3960)
        self.assertEqual({'filename': 'foo.html', }, var1716)

    def function1871(self):
        (var166, var4580) = parse_content_disposition('inline; filename="Not an attachment!"')
        self.assertEqual('inline', var166)
        self.assertEqual({'filename': 'Not an attachment!', }, var4580)

    def function2033(self):
        (var3755, var4413) = parse_content_disposition('attachment')
        self.assertEqual('attachment', var3755)
        self.assertEqual({}, var4413)

    def function2791(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var3243, var2122) = parse_content_disposition('"attachment"')
        self.assertEqual(None, var3243)
        self.assertEqual({}, var2122)

    def function1051(self):
        (var1945, var3393) = parse_content_disposition('ATTACHMENT')
        self.assertEqual('attachment', var1945)
        self.assertEqual({}, var3393)

    def function902(self):
        (var2759, var2766) = parse_content_disposition('attachment; filename="foo.html"')
        self.assertEqual('attachment', var2759)
        self.assertEqual({'filename': 'foo.html', }, var2766)

    def function2346(self):
        (var2169, var4349) = parse_content_disposition('attachment; filename="foo.pdf"')
        self.assertEqual('attachment', var2169)
        self.assertEqual({'filename': 'foo.pdf', }, var4349)

    def function2836(self):
        (var741, var129) = parse_content_disposition('attachment; filename="0000000000111111111122222"')
        self.assertEqual('attachment', var741)
        self.assertEqual({'filename': '0000000000111111111122222', }, var129)

    def function746(self):
        (var1246, var1468) = parse_content_disposition('attachment; filename="00000000001111111111222222222233333"')
        self.assertEqual('attachment', var1246)
        self.assertEqual({'filename': '00000000001111111111222222222233333', }, var1468)

    def function1183(self):
        (var689, var2341) = parse_content_disposition('attachment; filename="f\\oo.html"')
        self.assertEqual('attachment', var689)
        self.assertEqual({'filename': 'foo.html', }, var2341)

    def function2545(self):
        (var4278, var3865) = parse_content_disposition('attachment; filename=""quoting" tested.html"')
        self.assertEqual('attachment', var4278)
        self.assertEqual({'filename': '"quoting" tested.html', }, var3865)

    @unittest.skip('need more smart parser which respects quoted text')
    def function2470(self):
        (var686, var448) = parse_content_disposition('attachment; filename="Here\'s a semicolon;.html"')
        self.assertEqual('attachment', var686)
        self.assertEqual({'filename': "Here's a semicolon;.html", }, var448)

    def function757(self):
        (var2407, var2977) = parse_content_disposition('attachment; foo="bar"; filename="foo.html"')
        self.assertEqual('attachment', var2407)
        self.assertEqual({'filename': 'foo.html', 'foo': 'bar', }, var2977)

    def function46(self):
        (var793, var2372) = parse_content_disposition('attachment; foo=""\\";filename="foo.html"')
        self.assertEqual('attachment', var793)
        self.assertEqual({'filename': 'foo.html', 'foo': '"\\', }, var2372)

    def function1763(self):
        (var2708, var1015) = parse_content_disposition('attachment; FILENAME="foo.html"')
        self.assertEqual('attachment', var2708)
        self.assertEqual({'filename': 'foo.html', }, var1015)

    def function33(self):
        (var999, var4498) = parse_content_disposition('attachment; filename=foo.html')
        self.assertEqual('attachment', var999)
        self.assertEqual({'filename': 'foo.html', }, var4498)

    def function2074(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var4668, var2324) = parse_content_disposition('attachment; filename=foo,bar.html')
        self.assertEqual(None, var4668)
        self.assertEqual({}, var2324)

    def function330(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var4400, var387) = parse_content_disposition('attachment; filename=foo.html ;')
        self.assertEqual(None, var4400)
        self.assertEqual({}, var387)

    def function1541(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var563, var3897) = parse_content_disposition('attachment; ;filename=foo')
        self.assertEqual(None, var563)
        self.assertEqual({}, var3897)

    def function354(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var1029, var2594) = parse_content_disposition('attachment; filename=foo bar.html')
        self.assertEqual(None, var1029)
        self.assertEqual({}, var2594)

    def function405(self):
        (var2195, var500) = parse_content_disposition("attachment; filename='foo.html'")
        self.assertEqual('attachment', var2195)
        self.assertEqual({'filename': "'foo.html'", }, var500)

    def function2339(self):
        (var4399, var901) = parse_content_disposition('attachment; filename="foo-ä.html"')
        self.assertEqual('attachment', var4399)
        self.assertEqual({'filename': 'foo-ä.html', }, var901)

    def function2749(self):
        (var4688, var2270) = parse_content_disposition('attachment; filename="foo-Ã¤.html"')
        self.assertEqual('attachment', var4688)
        self.assertEqual({'filename': 'foo-Ã¤.html', }, var2270)

    def function2841(self):
        (var1420, var517) = parse_content_disposition('attachment; filename="foo-%41.html"')
        self.assertEqual('attachment', var1420)
        self.assertEqual({'filename': 'foo-%41.html', }, var517)

    def function1432(self):
        (var1143, var2256) = parse_content_disposition('attachment; filename="50%.html"')
        self.assertEqual('attachment', var1143)
        self.assertEqual({'filename': '50%.html', }, var2256)

    def function1758(self):
        (var4143, var2675) = parse_content_disposition('attachment; filename="foo-%\\41.html"')
        self.assertEqual('attachment', var4143)
        self.assertEqual({'filename': 'foo-%41.html', }, var2675)

    def function1625(self):
        (var4704, var1908) = parse_content_disposition('attachment; filename="foo-%41.html"')
        self.assertEqual('attachment', var4704)
        self.assertEqual({'filename': 'foo-%41.html', }, var1908)

    def function2493(self):
        (var1280, var4219) = parse_content_disposition('attachment; filename="ä-%41.html"')
        self.assertEqual('attachment', var1280)
        self.assertEqual({'filename': 'ä-%41.html', }, var4219)

    def function494(self):
        (var362, var2039) = parse_content_disposition('attachment; filename="foo-%c3%a4-%e2%82%ac.html"')
        self.assertEqual('attachment', var362)
        self.assertEqual({'filename': 'foo-%c3%a4-%e2%82%ac.html', }, var2039)

    def function1879(self):
        (var4343, var1953) = parse_content_disposition('attachment; filename ="foo.html"')
        self.assertEqual('attachment', var4343)
        self.assertEqual({'filename': 'foo.html', }, var1953)

    def function2236(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var870, var4280) = parse_content_disposition('attachment; filename="foo.html"; filename="bar.html"')
        self.assertEqual(None, var870)
        self.assertEqual({}, var4280)

    def function2880(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var700, var1576) = parse_content_disposition('attachment; filename=foo[1](2).html')
        self.assertEqual(None, var700)
        self.assertEqual({}, var1576)

    def function1536(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var3094, var1031) = parse_content_disposition('attachment; filename=foo-ä.html')
        self.assertEqual(None, var3094)
        self.assertEqual({}, var1031)

    def function142(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var4438, var2396) = parse_content_disposition('attachment; filename=foo-Ã¤.html')
        self.assertEqual(None, var4438)
        self.assertEqual({}, var2396)

    def function1273(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var2178, var4197) = parse_content_disposition('filename=foo.html')
        self.assertEqual(None, var2178)
        self.assertEqual({}, var4197)

    def function2125(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var918, var422) = parse_content_disposition('x=y; filename=foo.html')
        self.assertEqual(None, var918)
        self.assertEqual({}, var422)

    def function1839(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var4628, var2032) = parse_content_disposition('"foo; filename=bar;baz"; filename=qux')
        self.assertEqual(None, var4628)
        self.assertEqual({}, var2032)

    def function838(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var4442, var251) = parse_content_disposition('filename=foo.html, filename=bar.html')
        self.assertEqual(None, var4442)
        self.assertEqual({}, var251)

    def function1069(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var3800, var2933) = parse_content_disposition('; filename=foo.html')
        self.assertEqual(None, var3800)
        self.assertEqual({}, var2933)

    def function1684(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var562, var3538) = parse_content_disposition(': inline; attachment; filename=foo.html')
        self.assertEqual(None, var562)
        self.assertEqual({}, var3538)

    def function183(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var1978, var1655) = parse_content_disposition('inline; attachment; filename=foo.html')
        self.assertEqual(None, var1978)
        self.assertEqual({}, var1655)

    def function1047(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var1068, var1463) = parse_content_disposition('attachment; inline; filename=foo.html')
        self.assertEqual(None, var1068)
        self.assertEqual({}, var1463)

    def function1559(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var701, var10) = parse_content_disposition('attachment; filename="foo.html".txt')
        self.assertEqual(None, var701)
        self.assertEqual({}, var10)

    def function1175(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var843, var2737) = parse_content_disposition('attachment; filename="bar')
        self.assertEqual(None, var843)
        self.assertEqual({}, var2737)

    def function2390(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var3284, var3066) = parse_content_disposition('attachment; filename=foo"bar;baz"qux')
        self.assertEqual(None, var3284)
        self.assertEqual({}, var3066)

    def function462(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var3338, var2770) = parse_content_disposition('attachment; filename=foo.html, attachment; filename=bar.html')
        self.assertEqual(None, var3338)
        self.assertEqual({}, var2770)

    def function2505(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var2750, var2907) = parse_content_disposition('attachment; foo=foo filename=bar')
        self.assertEqual(None, var2750)
        self.assertEqual({}, var2907)

    def function2748(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var995, var393) = parse_content_disposition('attachment; filename=bar foo=foo')
        self.assertEqual(None, var995)
        self.assertEqual({}, var393)

    def function2536(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var3604, var1412) = parse_content_disposition('attachment filename=bar')
        self.assertEqual(None, var3604)
        self.assertEqual({}, var1412)

    def function1453(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var4076, var4263) = parse_content_disposition('filename=foo.html; attachment')
        self.assertEqual(None, var4076)
        self.assertEqual({}, var4263)

    def function964(self):
        (var4722, var1027) = parse_content_disposition('attachment; xfilename=foo.html')
        self.assertEqual('attachment', var4722)
        self.assertEqual({'xfilename': 'foo.html', }, var1027)

    def function1003(self):
        (var1534, var4550) = parse_content_disposition('attachment; filename="/foo.html"')
        self.assertEqual('attachment', var1534)
        self.assertEqual({'filename': 'foo.html', }, var4550)

    def function1497(self):
        (var2282, var1347) = parse_content_disposition('attachment; filename="\\foo.html"')
        self.assertEqual('attachment', var2282)
        self.assertEqual({'filename': 'foo.html', }, var1347)

    def function2116(self):
        (var1345, var359) = parse_content_disposition('attachment; creation-date="Wed, 12 Feb 1997 16:29:51 -0500"')
        self.assertEqual('attachment', var1345)
        self.assertEqual({'creation-date': 'Wed, 12 Feb 1997 16:29:51 -0500', }, var359)

    def function1145(self):
        (var2385, var3477) = parse_content_disposition('attachment; modification-date="Wed, 12 Feb 1997 16:29:51 -0500"')
        self.assertEqual('attachment', var2385)
        self.assertEqual({'modification-date': 'Wed, 12 Feb 1997 16:29:51 -0500', }, var3477)

    def function1874(self):
        (var2203, var1836) = parse_content_disposition('foobar')
        self.assertEqual('foobar', var2203)
        self.assertEqual({}, var1836)

    def function2784(self):
        (var2677, var144) = parse_content_disposition('attachment; example="filename=example.txt"')
        self.assertEqual('attachment', var2677)
        self.assertEqual({'example': 'filename=example.txt', }, var144)

    def function1942(self):
        (var1778, var3991) = parse_content_disposition("attachment; filename*=iso-8859-1''foo-%E4.html")
        self.assertEqual('attachment', var1778)
        self.assertEqual({'filename*': 'foo-ä.html', }, var3991)

    def function499(self):
        (var3506, var2850) = parse_content_disposition("attachment; filename*=UTF-8''foo-%c3%a4-%e2%82%ac.html")
        self.assertEqual('attachment', var3506)
        self.assertEqual({'filename*': 'foo-ä-€.html', }, var2850)

    def function185(self):
        (var3391, var1645) = parse_content_disposition("attachment; filename*=''foo-%c3%a4-%e2%82%ac.html")
        self.assertEqual('attachment', var3391)
        self.assertEqual({'filename*': 'foo-ä-€.html', }, var1645)

    def function1735(self):
        (var4565, var4602) = parse_content_disposition("attachment; filename*=UTF-8''foo-a%cc%88.html")
        self.assertEqual('attachment', var4565)
        self.assertEqual({'filename*': 'foo-ä.html', }, var4602)

    @unittest.skip('should raise decoding error: %82 is invalid for latin1')
    def function2717(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionParam):
            (var3355, var1204) = parse_content_disposition("attachment; filename*=iso-8859-1''foo-%c3%a4-%e2%82%ac.html")
        self.assertEqual('attachment', var3355)
        self.assertEqual({}, var1204)

    @unittest.skip('should raise decoding error: %E4 is invalid for utf-8')
    def function556(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionParam):
            (var2400, var1461) = parse_content_disposition("attachment; filename*=utf-8''foo-%E4.html")
        self.assertEqual('attachment', var2400)
        self.assertEqual({}, var1461)

    def function2817(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionParam):
            (var840, var2) = parse_content_disposition("attachment; filename *=UTF-8''foo-%c3%a4.html")
        self.assertEqual('attachment', var840)
        self.assertEqual({}, var2)

    def function352(self):
        (var3846, var771) = parse_content_disposition("attachment; filename*= UTF-8''foo-%c3%a4.html")
        self.assertEqual('attachment', var3846)
        self.assertEqual({'filename*': 'foo-ä.html', }, var771)

    def function681(self):
        (var3470, var2727) = parse_content_disposition("attachment; filename* =UTF-8''foo-%c3%a4.html")
        self.assertEqual('attachment', var3470)
        self.assertEqual({'filename*': 'foo-ä.html', }, var2727)

    def function1468(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionParam):
            (var4252, var1026) = parse_content_disposition('attachment; filename*="UTF-8\'\'foo-%c3%a4.html"')
        self.assertEqual('attachment', var4252)
        self.assertEqual({}, var1026)

    def function16(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionParam):
            (var2988, var3079) = parse_content_disposition('attachment; filename*="foo%20bar.html"')
        self.assertEqual('attachment', var2988)
        self.assertEqual({}, var3079)

    def function2447(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionParam):
            (var3874, var230) = parse_content_disposition("attachment; filename*=UTF-8'foo-%c3%a4.html")
        self.assertEqual('attachment', var3874)
        self.assertEqual({}, var230)

    @unittest.skip('urllib.parse.unquote is tolerate to standalone % chars')
    def function510(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionParam):
            (var1312, var1854) = parse_content_disposition("attachment; filename*=UTF-8''foo%")
        self.assertEqual('attachment', var1312)
        self.assertEqual({}, var1854)

    @unittest.skip('urllib.parse.unquote is tolerate to standalone % chars')
    def function55(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionParam):
            (var2589, var3290) = parse_content_disposition("attachment; filename*=UTF-8''f%oo.html")
        self.assertEqual('attachment', var2589)
        self.assertEqual({}, var3290)

    def function612(self):
        (var3776, var842) = parse_content_disposition("attachment; filename*=UTF-8''A-%2541.html")
        self.assertEqual('attachment', var3776)
        self.assertEqual({'filename*': 'A-%41.html', }, var842)

    def function422(self):
        (var626, var20) = parse_content_disposition("attachment; filename*=UTF-8''%5cfoo.html")
        self.assertEqual('attachment', var626)
        self.assertEqual({'filename*': '\\foo.html', }, var20)

    def function2212(self):
        (var4043, var3457) = parse_content_disposition('attachment; filename*0="foo."; filename*1="html"')
        self.assertEqual('attachment', var4043)
        self.assertEqual({'filename*0': 'foo.', 'filename*1': 'html', }, var3457)

    def function590(self):
        (var513, var3529) = parse_content_disposition('attachment; filename*0="foo"; filename*1="\\b\\a\\r.html"')
        self.assertEqual('attachment', var513)
        self.assertEqual({'filename*0': 'foo', 'filename*1': 'bar.html', }, var3529)

    def function109(self):
        (var2929, var1521) = parse_content_disposition('attachment; filename*0*=UTF-8foo-%c3%a4; filename*1=".html"')
        self.assertEqual('attachment', var2929)
        self.assertEqual({'filename*0*': 'UTF-8foo-%c3%a4', 'filename*1': '.html', }, var1521)

    def function2468(self):
        (var2114, var625) = parse_content_disposition('attachment; filename*0="foo"; filename*01="bar"')
        self.assertEqual('attachment', var2114)
        self.assertEqual({'filename*0': 'foo', 'filename*01': 'bar', }, var625)

    def function2389(self):
        (var2509, var1695) = parse_content_disposition('attachment; filename*0="foo"; filename*2="bar"')
        self.assertEqual('attachment', var2509)
        self.assertEqual({'filename*0': 'foo', 'filename*2': 'bar', }, var1695)

    def function493(self):
        (var2483, var4231) = parse_content_disposition('attachment; filename*0="foo."; filename*2="html"')
        self.assertEqual('attachment', var2483)
        self.assertEqual({'filename*0': 'foo.', 'filename*2': 'html', }, var4231)

    def function2477(self):
        (var2772, var4204) = parse_content_disposition('attachment; filename*1="bar"; filename*0="foo"')
        self.assertEqual('attachment', var2772)
        self.assertEqual({'filename*0': 'foo', 'filename*1': 'bar', }, var4204)

    def function1000(self):
        (var668, var1977) = parse_content_disposition('attachment; filename="foo-ae.html"; filename*=UTF-8\'\'foo-%c3%a4.html')
        self.assertEqual('attachment', var668)
        self.assertEqual({'filename': 'foo-ae.html', 'filename*': 'foo-ä.html', }, var1977)

    def function2281(self):
        (var2930, var1139) = parse_content_disposition('attachment; filename*=UTF-8\'\'foo-%c3%a4.html; filename="foo-ae.html"')
        self.assertEqual('attachment', var2930)
        self.assertEqual({'filename': 'foo-ae.html', 'filename*': 'foo-ä.html', }, var1139)

    def function2731(self):
        (var2540, var264) = parse_content_disposition("attachment; filename*0*=ISO-8859-15''euro-sign%3d%a4; filename*=ISO-8859-1''currency-sign%3d%a4")
        self.assertEqual('attachment', var2540)
        self.assertEqual({'filename*': 'currency-sign=¤', 'filename*0*': "ISO-8859-15''euro-sign%3d%a4", }, var264)

    def function2897(self):
        (var433, var66) = parse_content_disposition('attachment; foobar=x; filename="foo.html"')
        self.assertEqual('attachment', var433)
        self.assertEqual({'foobar': 'x', 'filename': 'foo.html', }, var66)

    def function1719(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionHeader):
            (var3993, var1518) = parse_content_disposition('attachment; filename==?ISO-8859-1?Q?foo-=E4.html?=')
        self.assertEqual(None, var3993)
        self.assertEqual({}, var1518)

    def function614(self):
        (var2890, var2266) = parse_content_disposition('attachment; filename="=?ISO-8859-1?Q?foo-=E4.html?="')
        self.assertEqual('attachment', var2890)
        self.assertEqual({'filename': '=?ISO-8859-1?Q?foo-=E4.html?=', }, var2266)

    def function1710(self):
        with self.assertWarns(aiohttp.multipart.BadContentDispositionParam):
            (var528, var2482) = parse_content_disposition('attachment; filename*0=foo bar')
        self.assertEqual('attachment', var528)
        self.assertEqual({}, var2482)


class Class358(unittest.TestCase):

    def function790(self):
        self.assertIsNone(content_disposition_filename({}))
        self.assertIsNone(content_disposition_filename({'foo': 'bar', }))

    def function1951(self):
        var123 = {'filename': 'foo.html', }
        self.assertEqual('foo.html', content_disposition_filename(var123))

    def function2868(self):
        var3371 = {'filename*': 'файл.html', }
        self.assertEqual('файл.html', content_disposition_filename(var3371))

    def function962(self):
        var1597 = {'filename*0': 'foo.', 'filename*1': 'html', }
        self.assertEqual('foo.html', content_disposition_filename(var1597))

    def function712(self):
        var3884 = {'filename*0': 'foo', 'filename*1': 'bar.html', }
        self.assertEqual('foobar.html', content_disposition_filename(var3884))

    def function2712(self):
        var3068 = {'filename*0*': "UTF-8''foo-%c3%a4", 'filename*1': '.html', }
        self.assertEqual('foo-ä.html', content_disposition_filename(var3068))

    def function717(self):
        var3354 = {'filename*0': 'foo', 'filename*01': 'bar', }
        self.assertEqual('foo', content_disposition_filename(var3354))

    def function658(self):
        var190 = {'filename*0': 'foo', 'filename*2': 'bar', }
        self.assertEqual('foo', content_disposition_filename(var190))

    def function592(self):
        var2356 = {'filename*1': 'foo', 'filename*2': 'bar', }
        self.assertEqual(None, content_disposition_filename(var2356))

    def function978(self):
        var241 = {'filename': 'foo-ae.html', 'filename*': 'foo-ä.html', }
        self.assertEqual('foo-ä.html', content_disposition_filename(var241))

    def function1756(self):
        var1726 = {'filename*0*': "ISO-8859-15''euro-sign%3d%a4", 'filename*': 'currency-sign=¤', }
        self.assertEqual('currency-sign=¤', content_disposition_filename(var1726))

    def function1341(self):
        var2340 = {'filename': '=?ISO-8859-1?Q?foo-=E4.html?=', }
        self.assertEqual('=?ISO-8859-1?Q?foo-=E4.html?=', content_disposition_filename(var2340))