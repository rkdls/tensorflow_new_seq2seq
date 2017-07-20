import asyncio
import io
import json
import pathlib
import zlib
from unittest import mock
import pytest
from multidict import MultiDict
from yarl import URL
import aiohttp
from aiohttp import FormData, HttpVersion10, HttpVersion11, multipart, web
try:
    import ssl
except:
    var213 = False

@pytest.fixture
def function820():
    return pathlib.Path(__file__).parent

@pytest.fixture
def function614(function820):
    return (function820 / 'sample.key')

@asyncio.coroutine
def function283(arg212, arg332):

    @asyncio.coroutine
    def function146(arg1944):
        var4132 = yield from arg1944.read()
        assert (b'' == var4132)
        return web.Response(body=b'OK')
    var2423 = web.Application()
    var2423.router.add_get('/', function146)
    var543 = yield from arg332(var2423)
    var1804 = yield from var543.get('/')
    assert (200 == var1804.status)
    var3741 = yield from var1804.text()
    assert ('OK' == var3741)

@asyncio.coroutine
def function245(arg1164, arg2113):

    @asyncio.coroutine
    def function146(arg1325):
        var3393 = yield from arg1325.read()
        assert (b'' == var3393)
        return web.Response(text='OK', headers={'content-type': 'text/plain', })
    var4102 = web.Application()
    var4102.router.add_get('/', function146)
    var3403 = yield from arg2113(var4102)
    var3377 = yield from var3403.get('/')
    assert (200 == var3377.status)
    var547 = yield from var3377.text()
    assert ('OK' == var547)

@asyncio.coroutine
def function687(arg2027, arg2260, arg1996):
    var2987 = mock.Mock()

    @asyncio.coroutine
    def function146(arg449):
        return 'abc'
    var2414 = web.Application()
    var2414.router.add_get('/', function146)
    var2822 = yield from arg2260(var2414, logger=var2987)
    var1962 = yield from arg1996(var2822)
    var3786 = yield from var1962.get('/')
    assert (500 == var3786.status)
    assert var2987.exception.called

@asyncio.coroutine
def function155(arg1386, arg2273):

    @asyncio.coroutine
    def function146(arg1591):
        return web.Response(body=b'test')
    var170 = web.Application()
    var170.router.add_head('/', function146)
    var1881 = yield from arg2273(var170, version=HttpVersion11)
    var2259 = yield from var1881.head('/')
    assert (200 == var2259.status)
    var3570 = yield from var2259.text()
    assert ('' == var3570)

@asyncio.coroutine
def function1424(arg1139, arg558):

    @asyncio.coroutine
    def function146(arg522):
        return web.Response(body=b'OK')
    var3849 = web.Application()
    var3849.router.add_post('/', function146)
    var592 = yield from arg558(var3849)
    var1446 = ((b'0' * 1024) * 1024)
    var2098 = yield from var592.post('/', data=var1446)
    assert (200 == var2098.status)
    var4296 = yield from var2098.var4296()
    assert ('OK' == var4296)

@asyncio.coroutine
def function1570(arg80, arg1410):

    @asyncio.coroutine
    def function146(arg1870):
        var1586 = yield from arg1870.post()
        assert ({'a': '1', 'b': '2', 'c': '', } == var1586)
        return web.Response(body=b'OK')
    var3836 = web.Application()
    var3836.router.add_post('/', function146)
    var3713 = yield from arg1410(var3836)
    var151 = yield from var3713.post('/', data={'a': 1, 'b': 2, 'c': '', })
    assert (200 == var151.status)
    var2644 = yield from var151.text()
    assert ('OK' == var2644)

@asyncio.coroutine
def function1917(arg637, arg1465):

    @asyncio.coroutine
    def function146(arg2003):
        var1690 = yield from arg2003.text()
        assert ('русский' == var1690)
        var3749 = yield from arg2003.text()
        assert (var1690 == var3749)
        return web.Response(text=var1690)
    var1418 = web.Application()
    var1418.router.add_post('/', function146)
    var1079 = yield from arg1465(var1418)
    var937 = yield from var1079.post('/', data='русский')
    assert (200 == var937.status)
    var2814 = yield from var937.text()
    assert ('русский' == var2814)

@asyncio.coroutine
def function2538(arg2161, arg755):
    var3303 = {'key': 'текст', }

    @asyncio.coroutine
    def function146(arg51):
        var526 = yield from arg51.json()
        assert (var3303 == var526)
        var4463 = yield from arg51.json(loads=json.loads)
        assert (var526 == var4463)
        var4150 = web.Response()
        var4150.content_type = 'application/json'
        var4150.body = json.dumps(var526).encode('utf8')
        return var4150
    var4385 = web.Application()
    var4385.router.add_post('/', function146)
    var284 = yield from arg755(var4385)
    var3316 = {'Content-Type': 'application/json', }
    var34 = yield from var284.post('/', data=json.dumps(var3303), headers=var3316)
    assert (200 == var34.status)
    var1292 = yield from var34.json()
    assert (var3303 == var1292)

@asyncio.coroutine
def function2636(arg1060, arg1623):
    with multipart.MultipartWriter() as var1241:
        var1241.append('test')
        var1241.append_json({'passed': True, })

    @asyncio.coroutine
    def function146(arg571):
        var2178 = yield from arg571.multipart()
        assert isinstance(var2178, multipart.MultipartReader)
        var2237 = yield from var2178.next()
        assert isinstance(var2237, multipart.BodyPartReader)
        var1748 = yield from var2237.text()
        assert (var1748 == 'test')
        var2237 = yield from var2178.next()
        assert isinstance(var2237, multipart.BodyPartReader)
        assert (var2237.headers['Content-Type'] == 'application/json')
        var1748 = yield from var2237.json()
        assert (var1748 == {'passed': True, })
        var3938 = web.Response()
        var3938.content_type = 'application/json'
        var3938.body = b''
        return var3938
    var1429 = web.Application()
    var1429.router.add_post('/', function146)
    var1114 = yield from arg1623(var1429)
    var2785 = yield from var1114.post('/', data=var1241, headers=var1241.headers)
    assert (200 == var2785.status)
    yield from var2785.release()

@asyncio.coroutine
def function385(arg2392, arg1496):
    'For issue #1168'
    with multipart.MultipartWriter() as var3062:
        var3062.append((b'\x00' * 10), headers={'Content-Transfer-Encoding': 'binary', })

    @asyncio.coroutine
    def function146(arg2239):
        var518 = yield from arg2239.multipart()
        assert isinstance(var518, multipart.MultipartReader)
        var728 = yield from var518.next()
        assert isinstance(var728, multipart.BodyPartReader)
        assert (var728.headers['Content-Transfer-Encoding'] == 'binary')
        var4346 = yield from var728.read()
        assert (var4346 == (b'\x00' * 10))
        var2520 = web.Response()
        var2520.content_type = 'application/json'
        var2520.body = b''
        return var2520
    var1874 = web.Application()
    var1874.router.add_post('/', function146)
    var2834 = yield from arg1496(var1874)
    var2808 = yield from var2834.post('/', data=var3062, headers=var3062.headers)
    assert (200 == var2808.status)
    yield from var2808.release()

@asyncio.coroutine
def function1410(arg1339, arg508):

    @asyncio.coroutine
    def function146(arg1145):
        raise web.HTTPMovedPermanently(location='/path')
    var2304 = web.Application()
    var2304.router.add_get('/', function146)
    var4001 = yield from arg508(var2304)
    var3039 = yield from var4001.get('/', allow_redirects=False)
    assert (301 == var3039.status)
    var4032 = yield from var3039.text()
    assert ('301: Moved Permanently' == var4032)
    assert ('/path' == var3039.headers['location'])

@asyncio.coroutine
def function1789(arg987, arg391):
    function820 = pathlib.Path(__file__).parent

    def function388(arg642):
        var4289 = (function820 / arg642.filename)
        with var4289.open() as var411:
            var3714 = var411.read().encode()
            var2234 = arg642.file.read()
            assert (var3714 == var2234)

    @asyncio.coroutine
    def function146(arg612):
        var536 = yield from arg612.post()
        assert (['sample.crt'] == list(var536.keys()))
        for var1457 in var536.values():
            function388(var1457)
            var1457.file.close()
        var1119 = web.Response(body=b'OK')
        return var1119
    var2184 = web.Application()
    var2184.router.add_post('/', function146)
    var2088 = yield from arg391(var2184)
    function614 = (function820 / 'sample.crt')
    var3510 = yield from var2088.post('/', data=[function614.open()])
    assert (200 == var3510.status)

@asyncio.coroutine
def function1457(arg86, arg858):

    @asyncio.coroutine
    def function146(arg817):
        var646 = yield from arg817.post()
        var2363 = var646.getall('file')
        var1835 = set()
        for var421 in var2363:
            assert (not var421.file.closed)
            if (var421.filename == 'test1.jpeg'):
                assert (var421.file.read() == b'binary data 1')
            if (var421.filename == 'test2.jpeg'):
                assert (var421.file.read() == b'binary data 2')
            var1835.add(var421.filename)
        assert (len(var2363) == 2)
        assert (var1835 == {'test1.jpeg', 'test2.jpeg'})
        var3965 = web.Response(body=b'OK')
        return var3965
    var63 = web.Application()
    var63.router.add_post('/', function146)
    var2059 = yield from arg858(var63)
    var4541 = FormData()
    var4541.add_field('file', b'binary data 1', content_type='image/jpeg', filename='test1.jpeg')
    var4541.add_field('file', b'binary data 2', content_type='image/jpeg', filename='test2.jpeg')
    var3474 = yield from var2059.post('/', data=var4541)
    assert (200 == var3474.status)

@asyncio.coroutine
def function55(arg1313, arg1957):
    function820 = pathlib.Path(__file__).parent

    def function388(arg155):
        var901 = (function820 / arg155.filename)
        with var901.open() as var3391:
            var836 = var3391.read().encode()
            var2824 = arg155.file.read()
            assert (var836 == var2824)

    @asyncio.coroutine
    def function146(arg537):
        var140 = yield from arg537.post()
        assert (['sample.crt', 'sample.key'] == list(var140.keys()))
        for var1539 in var140.values():
            function388(var1539)
            var1539.file.close()
        var2623 = web.Response(body=b'OK')
        return var2623
    var4732 = web.Application()
    var4732.router.add_post('/', function146)
    var2981 = yield from arg1957(var4732)
    with (function820 / 'sample.crt').open() as var1763:
        with (function820 / 'sample.key').open() as var3523:
            var113 = yield from var2981.post('/', data=[var1763, var3523])
            assert (200 == var113.status)

@asyncio.coroutine
def function2469(arg270, arg1982):

    @asyncio.coroutine
    def function146(arg2227):
        yield from arg2227.release()
        var4501 = yield from arg2227.content.readany()
        assert (var4501 == b'')
        return web.Response()
    var1913 = web.Application()
    var1913.router.add_post('/', function146)
    var3146 = yield from arg1982(var1913)
    var3383 = yield from var3146.post('/', data='post text')
    assert (200 == var3383.status)

@asyncio.coroutine
def function1447(arg122, arg867):

    @asyncio.coroutine
    def function146(arg1593):
        var4207 = yield from arg1593.post()
        assert (b'123' == var4207['name'])
        return web.Response()
    var1911 = web.Application()
    var1911.router.add_post('/', function146)
    var2008 = yield from arg867(var1911)
    var3214 = FormData()
    var3214.add_field('name', b'123', content_transfer_encoding='base64')
    var72 = yield from var2008.post('/', data=var3214)
    assert (200 == var72.status)

@asyncio.coroutine
def function1092(arg1355, arg262):

    @asyncio.coroutine
    def function146(arg1873):
        var2207 = yield from arg1873.post()
        var697 = list(var2207.items())
        assert ([('a', '1'), ('a', '2')] == var697)
        return web.Response()
    var2239 = web.Application()
    var2239.router.add_post('/', function146)
    var867 = yield from arg262(var2239)
    var3337 = yield from var867.post('/', data=MultiDict([('a', 1), ('a', 2)]))
    assert (200 == var3337.status)

def function986(arg2039):
    var3048 = web.Application()
    assert ('<Application 0x{:x}>'.format(id(var3048)) == repr(var3048))

@asyncio.coroutine
def function1084(arg751, arg691):
    'Test default Expect handler for unknown Expect value.\n\n    A server that does not understand or is unable to comply with any of\n    the expectation values in the Expect field of a request MUST respond\n    with appropriate error status. The server MUST respond with a 417\n    (Expectation Failed) status if any of the expectations cannot be met\n    or, if there are other problems with the request, some other 4xx\n    status.\n\n    http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.20\n    '

    @asyncio.coroutine
    def function146(arg971):
        yield from arg971.post()
        pytest.xfail('Handler should not proceed to this point in case of unknown Expect header')
    var4676 = web.Application()
    var4676.router.add_post('/', function146)
    var2878 = yield from arg691(var4676)
    var946 = yield from var2878.post('/', headers={'Expect': 'SPAM', })
    assert (417 == var946.status)

@asyncio.coroutine
def function2462(arg836, arg50):

    @asyncio.coroutine
    def function146(arg1393):
        var1247 = yield from arg1393.post()
        assert (b'123' == var1247['name'])
        return web.Response()
    var1086 = FormData()
    var1086.add_field('name', b'123', content_transfer_encoding='base64')
    var2777 = web.Application()
    var2777.router.add_post('/', function146)
    var3529 = yield from arg50(var2777)
    var174 = yield from var3529.post('/', data=var1086, expect100=True)
    assert (200 == var174.status)

@asyncio.coroutine
def function663(arg1801, arg549):
    var1478 = False

    @asyncio.coroutine
    def function146(arg675):
        var2387 = yield from arg675.post()
        assert (b'123' == var2387['name'])
        return web.Response()

    @asyncio.coroutine
    def function2702(arg602):
        nonlocal expect_received
        var1478 = True
        if (arg602.version == HttpVersion11):
            arg602.transport.write(b'HTTP/1.1 100 Continue\r\n\r\n')
    var3611 = FormData()
    var3611.add_field('name', b'123', content_transfer_encoding='base64')
    var992 = web.Application()
    var992.router.add_post('/', function146, expect_handler=function2702)
    var776 = yield from arg549(var992)
    var4637 = yield from var776.post('/', data=var3611, expect100=True)
    assert (200 == var4637.status)
    assert expect_received

@asyncio.coroutine
def function2814(arg264, arg187):

    @asyncio.coroutine
    def function146(arg1782):
        var2197 = yield from arg1782.post()
        assert b'123', var2197['name']
        return web.Response()

    @asyncio.coroutine
    def function2702(arg879):
        if (arg879.version == HttpVersion11):
            if var1702:
                return web.HTTPForbidden()
            arg879.writer.write(b'HTTP/1.1 100 Continue\r\n\r\n')
    var1353 = FormData()
    var1353.add_field('name', b'123', content_transfer_encoding='base64')
    var4658 = web.Application()
    var4658.router.add_post('/', function146, expect_handler=function2702)
    var4374 = yield from arg187(var4658)
    var1702 = False
    var1154 = yield from var4374.post('/', data=var1353, expect100=True)
    assert (200 == var1154.status)
    var1702 = True
    var1154 = yield from var4374.post('/', data=var1353, expect100=True)
    assert (403 == var1154.status)

@asyncio.coroutine
def function2564(arg1864, arg1709):
    var3687 = web.Application()
    var2723 = yield from arg1709(var3687)
    var1771 = yield from var2723.post('/not_found', data='data', expect100=True)
    assert (404 == var1771.status)

@asyncio.coroutine
def function1341(arg1752, arg2279):

    @asyncio.coroutine
    def function146(arg413):
        return web.Response()
    var3176 = web.Application()
    var3176.router.add_post('/', function146)
    var2608 = yield from arg2279(var3176)
    var1730 = yield from var2608.get('/', expect100=True)
    assert (405 == var1730.status)

@asyncio.coroutine
def function817(arg1331, arg545):

    @asyncio.coroutine
    def function146(arg498):
        return web.Response()
    var3769 = web.Application()
    var3769.router.add_get('/', function146)
    var1957 = yield from arg545(var3769, version=HttpVersion11)
    var4642 = yield from var1957.get('/')
    assert (200 == var4642.status)
    assert (var4642.version == HttpVersion11)
    assert ('Connection' not in var4642.headers)

@pytest.mark.xfail
@asyncio.coroutine
def function1753(arg70, arg1945):

    @asyncio.coroutine
    def function146(arg2331):
        return web.Response()
    var378 = web.Application()
    var378.router.add_get('/', function146)
    var3799 = yield from arg1945(var378, version=HttpVersion10)
    var1013 = yield from var3799.get('/')
    assert (200 == var1013.status)
    assert (var1013.version == HttpVersion10)
    assert (var1013.headers['Connection'] == 'keep-alive')

@asyncio.coroutine
def function198(arg1738, arg1244):

    @asyncio.coroutine
    def function146(arg2127):
        yield from arg2127.read()
        return web.Response(body=b'OK')
    var3341 = web.Application()
    var3341.router.add_get('/', function146)
    var785 = yield from arg1244(var3341, version=HttpVersion10)
    var3729 = {'Connection': 'close', }
    var4098 = yield from var785.get('/', headers=var3729)
    assert (200 == var4098.status)
    assert (var4098.version == HttpVersion10)
    assert ('Connection' not in var4098.var3729)

@asyncio.coroutine
def function1347(arg1600, arg727):

    @asyncio.coroutine
    def function146(arg1104):
        yield from arg1104.read()
        return web.Response(body=b'OK')
    var5 = web.Application()
    var5.router.add_get('/', function146)
    var3344 = yield from arg727(var5, version=HttpVersion10)
    var270 = {'Connection': 'keep-alive', }
    var2829 = yield from var3344.get('/', headers=var270)
    assert (200 == var2829.status)
    assert (var2829.version == HttpVersion10)
    assert (var2829.var270['Connection'] == 'keep-alive')

@asyncio.coroutine
def function1805(arg1777, arg17):
    function820 = pathlib.Path(__file__).parent
    function614 = (function820 / 'aiohttp.png')
    with function614.open('rb') as var4426:
        var4746 = var4426.read()

    @asyncio.coroutine
    def function146(arg1867):
        var2780 = yield from arg1867.post()
        var2560 = var2780['file'].file.read()
        assert (var4746 == var2560)
        return web.Response()
    var800 = web.Application()
    var800.router.add_post('/', function146)
    var2449 = yield from arg17(var800)
    var4662 = yield from var2449.post('/', data={'file': data, })
    assert (200 == var4662.status)

@asyncio.coroutine
def function2333(arg1155, arg2126):
    function820 = pathlib.Path(__file__).parent
    function614 = (function820 / 'aiohttp.png')
    with function614.open('rb') as var1007:
        var613 = var1007.read()

    @asyncio.coroutine
    def function146(arg941):
        var3842 = yield from arg941.post()
        var1146 = var3842['file'].file.read()
        assert (var613 == var1146)
        return web.Response()
    var2320 = web.Application()
    var2320.router.add_post('/', function146)
    var4439 = yield from arg2126(var2320)
    with function614.open('rb') as var1007:
        var3855 = yield from var4439.post('/', data={'file': f, })
        assert (200 == var3855.status)

@asyncio.coroutine
def function2189(arg300, arg206):

    @asyncio.coroutine
    def function146(arg1670):
        assert (not arg1670.has_body)
        return web.Response()
    var3631 = web.Application()
    var3631.router.add_get('/', function146)
    var4599 = yield from arg206(var3631)
    var1731 = yield from var4599.get('/')
    assert (200 == var1731.status)

@asyncio.coroutine
def function848(arg21, arg220):

    @asyncio.coroutine
    def function146(arg1242):
        assert arg1242.has_body
        var512 = yield from arg1242.read()
        return web.Response(body=var512)
    var104 = web.Application()
    var104.router.add_post('/', function146)
    var413 = yield from arg220(var104)
    var3452 = yield from var413.post('/', data=b'data')
    assert (200 == var3452.status)

@asyncio.coroutine
def function731(arg1852, arg2021):

    @asyncio.coroutine
    def function146(arg1090):
        assert ('arg' in arg1090.query)
        assert ('' == arg1090.query['arg'])
        return web.Response()
    var2690 = web.Application()
    var2690.router.add_get('/', function146)
    var1185 = yield from arg2021(var2690)
    var483 = yield from var1185.get('/?arg')
    assert (200 == var483.status)

@asyncio.coroutine
def function1633(arg1271, arg1363):

    @asyncio.coroutine
    def function146(arg118):
        return web.Response()
    var744 = web.Application()
    var744.router.add_get('/', function146)
    var2546 = yield from arg1363(var744)
    var2343 = {'Long-Header': ('ab' * 8129), }
    var3450 = yield from var2546.get('/', headers=var2343)
    assert (400 == var3450.status)

@asyncio.coroutine
def function2134(arg192, arg401, arg26):

    @asyncio.coroutine
    def function146(arg2206):
        return web.Response()
    var4726 = web.Application()
    var4726.router.add_get('/', function146)
    var1654 = yield from arg26(var4726, max_field_size=81920)
    var1052 = yield from arg401(var1654)
    var4103 = {'Long-Header': ('ab' * 8129), }
    var2666 = yield from var1052.get('/', headers=var4103)
    assert (200 == var2666.status)

@asyncio.coroutine
def function2697(arg1278, arg1586):

    @asyncio.coroutine
    def function146(arg335):
        assert ('arg' in arg335.query)
        assert ('' == arg335.query['arg'])
        return web.Response()
    var3336 = web.Application()
    var3336.router.add_get('/', function146)
    var3996 = yield from arg1586(var3336)
    var1790 = yield from var3996.get('/?arg=')
    assert (200 == var1790.status)

@asyncio.coroutine
def function2025(arg1694, arg172, function614):
    with function614.open('rb') as var4450:
        var1038 = var4450.read()
    var1922 = len(var1038)

    @aiohttp.streamer
    def function1767(arg377, arg1895):
        with arg1895.open('rb') as var4450:
            var1038 = var4450.read(100)
            while data:
                yield from arg377.write(var1038)
                var1038 = var4450.read(100)

    @asyncio.coroutine
    def function146(arg873):
        var2963 = {'Content-Length': str(var1922), }
        return web.Response(body=function1767(function614), headers=var2963)
    var4286 = web.Application()
    var4286.router.add_get('/', function146)
    var1915 = yield from arg172(var4286)
    var1209 = yield from var1915.get('/')
    assert (200 == var1209.status)
    var1556 = yield from var1209.read()
    assert (var1556 == var1038)
    assert (var1209.headers.get('Content-Length') == str(len(var1556)))

@asyncio.coroutine
def function299(arg1373, arg2066, function614):
    with function614.open('rb') as var2115:
        var1060 = var2115.read()
    var3537 = len(var1060)

    @aiohttp.streamer
    def function1767(arg1912):
        with function614.open('rb') as var2115:
            var1060 = var2115.read(100)
            while data:
                yield from arg1912.write(var1060)
                var1060 = var2115.read(100)

    @asyncio.coroutine
    def function146(arg961):
        var1047 = {'Content-Length': str(var3537), }
        return web.Response(body=function1767, headers=var1047)
    var788 = web.Application()
    var788.router.add_get('/', function146)
    var672 = yield from arg2066(var788)
    var1467 = yield from var672.get('/')
    assert (200 == var1467.status)
    var3282 = yield from var1467.read()
    assert (var3282 == var1060)
    assert (var1467.headers.get('Content-Length') == str(len(var3282)))

@asyncio.coroutine
def function2109(arg1751, arg1681, function614):
    with function614.open('rb') as var2275:
        var2295 = var2275.read()

    @asyncio.coroutine
    def function146(arg533):
        return web.Response(body=function614.open('rb'))
    var3822 = web.Application()
    var3822.router.add_get('/', function146)
    var887 = yield from arg1681(var3822)
    var3258 = yield from var887.get('/')
    assert (200 == var3258.status)
    var2802 = yield from var3258.read()
    assert (var2802 == var2295)
    assert (var3258.headers.get('Content-Type') in ('application/octet-stream', 'application/pgp-keys'))
    assert (var3258.headers.get('Content-Length') == str(len(var2802)))
    assert (var3258.headers.get('Content-Disposition') == 'attachment; filename="sample.key"; filename*=utf-8\'\'sample.key')

@asyncio.coroutine
def function1870(arg1479, arg356, function614):
    with function614.open('rb') as var1386:
        var724 = var1386.read()

    @asyncio.coroutine
    def function146(arg88):
        return web.Response(body=function614.open('rb'), headers={'content-type': 'text/binary', })
    var2696 = web.Application()
    var2696.router.add_get('/', function146)
    var2784 = yield from arg356(var2696)
    var4648 = yield from var2784.get('/')
    assert (200 == var4648.status)
    var2359 = yield from var4648.read()
    assert (var2359 == var724)
    assert (var4648.headers.get('Content-Type') == 'text/binary')
    assert (var4648.headers.get('Content-Length') == str(len(var2359)))
    assert (var4648.headers.get('Content-Disposition') == 'attachment; filename="sample.key"; filename*=utf-8\'\'sample.key')

@asyncio.coroutine
def function1724(arg184, arg965, function614):
    with function614.open('rb') as var2770:
        var3578 = var2770.read()

    @asyncio.coroutine
    def function146(arg1002):
        var251 = aiohttp.get_payload(function614.open('rb'))
        var251.set_content_disposition('inline', filename='test.txt')
        return web.Response(body=var251, headers={'content-type': 'text/binary', })
    var3613 = web.Application()
    var3613.router.add_get('/', function146)
    var3411 = yield from arg965(var3613)
    var181 = yield from var3411.get('/')
    assert (200 == var181.status)
    var527 = yield from var181.read()
    assert (var527 == var3578)
    assert (var181.headers.get('Content-Type') == 'text/binary')
    assert (var181.headers.get('Content-Length') == str(len(var527)))
    assert (var181.headers.get('Content-Disposition') == 'inline; filename="test.txt"; filename*=utf-8\'\'test.txt')

@asyncio.coroutine
def function977(arg749, arg2231, function614):

    @asyncio.coroutine
    def function146(arg1394):
        return web.Response(body=io.StringIO('test'))
    var1565 = web.Application()
    var1565.router.add_get('/', function146)
    var511 = yield from arg2231(var1565)
    var1892 = yield from var511.get('/')
    assert (200 == var1892.status)
    var3096 = yield from var1892.read()
    assert (var3096 == b'test')

@asyncio.coroutine
def function2515(arg581, arg770):

    @asyncio.coroutine
    def function146(arg101):
        var3617 = {'Content-Encoding': 'gzip', }
        var1667 = zlib.compressobj(wbits=(16 + zlib.MAX_WBITS))
        var812 = (var1667.compress(b'mydata') + var1667.flush())
        return web.Response(body=var812, headers=var3617)
    var1553 = web.Application()
    var1553.router.add_get('/', function146)
    var178 = yield from arg770(var1553)
    var2192 = yield from var178.get('/')
    assert (200 == var2192.status)
    var1574 = yield from var2192.read()
    assert (b'mydata' == var1574)
    assert (var2192.headers.get('Content-Encoding') == 'gzip')

@asyncio.coroutine
def function1609(arg620, arg414):

    @asyncio.coroutine
    def function146(arg599):
        var444 = {'Content-Encoding': 'deflate', }
        var4021 = zlib.compressobj(wbits=(- zlib.MAX_WBITS))
        var4366 = (var4021.compress(b'mydata') + var4021.flush())
        return web.Response(body=var4366, headers=var444)
    var1051 = web.Application()
    var1051.router.add_get('/', function146)
    var3161 = yield from arg414(var1051)
    var1454 = yield from var3161.get('/')
    assert (200 == var1454.status)
    var560 = yield from var1454.read()
    assert (b'mydata' == var560)
    assert (var1454.headers.get('Content-Encoding') == 'deflate')

@asyncio.coroutine
def function1252(arg275, arg1887):

    @asyncio.coroutine
    def function146(arg31):
        assert (arg31.method == 'GET')
        with pytest.raises(aiohttp.web.RequestPayloadError):
            yield from arg31.content.read()
        return web.Response()
    var1770 = web.Application()
    var1770.router.add_get('/', function146)
    var1527 = yield from arg1887(var1770)
    var3614 = yield from var1527.get('/', data=b'test', headers={'content-encoding': 'gzip', })
    assert (200 == var3614.status)

@asyncio.coroutine
def function1452(arg1275, arg1680):

    @asyncio.coroutine
    def function146(arg2056):
        var1442 = web.StreamResponse()
        var1442.enable_chunked_encoding()
        yield from var1442.prepare(arg2056)
        var1442.write(b'x')
        var1442.write(b'y')
        var1442.write(b'z')
        return var1442
    var3262 = web.Application()
    var3262.router.add_get('/', function146)
    var46 = yield from arg1680(var3262)
    var443 = yield from var46.get('/')
    assert (200 == var443.status)
    var533 = yield from var443.read()
    assert (b'xyz' == var533)

@asyncio.coroutine
def function1576(arg1818, arg1098):
    var232 = web.Application()
    var3789 = yield from arg1098(var232)
    var4105 = yield from var3789.get('/')
    assert (404 == var4105.status)

@asyncio.coroutine
def function1831(arg2307, arg784):

    @asyncio.coroutine
    def function146(arg340):
        return web.Response()
    var2704 = web.Application()
    var2704.router.add_get('/', function146)
    var2861 = yield from arg784(var2704)
    assert (var2861.server.function146.requests_count == 0)
    var2961 = yield from var2861.get('/')
    assert (200 == var2961.status)
    assert (var2861.server.function146.requests_count == 1)
    var2961 = yield from var2861.get('/')
    assert (200 == var2961.status)
    assert (var2861.server.function146.requests_count == 2)
    var2961 = yield from var2861.get('/')
    assert (200 == var2961.status)
    assert (var2861.server.function146.requests_count == 3)

@asyncio.coroutine
def function1544(arg856, arg1780):

    @asyncio.coroutine
    def function2785(arg2087):
        raise web.HTTPFound(location=URL('/redirected'))

    @asyncio.coroutine
    def function1626(arg1802):
        return web.Response()
    var3326 = web.Application()
    var3326.router.add_get('/redirector', function2785)
    var3326.router.add_get('/redirected', function1626)
    var2946 = yield from arg1780(var3326)
    var3757 = yield from var2946.get('/redirector')
    assert (var3757.status == 200)

@asyncio.coroutine
def function910(arg2318, arg714):

    @asyncio.coroutine
    def function146(arg1890):
        return web.Response(text='OK')
    var3807 = web.Application()
    var4012 = web.Application()
    var4012.router.add_get('/to', function146)
    var3807.add_subapp('/path', var4012)
    var4215 = yield from arg714(var3807)
    var209 = yield from var4215.get('/path/to')
    assert (var209.status == 200)
    var473 = yield from var209.text()
    assert ('OK' == var473)

@asyncio.coroutine
def function7(arg1220, arg2394):

    @asyncio.coroutine
    def function146(arg319):
        return web.HTTPMovedPermanently(location=var2731.router['name'].url_for())

    @asyncio.coroutine
    def function925(arg1111):
        return web.Response(text='OK')
    var3712 = web.Application()
    var2731 = web.Application()
    var2731.router.add_get('/to', function146)
    var2731.router.add_get('/final', function925, name='name')
    var3712.add_subapp('/path', var2731)
    var2089 = yield from arg2394(var3712)
    var3824 = yield from var2089.get('/path/to')
    assert (var3824.status == 200)
    var4497 = yield from var3824.text()
    assert ('OK' == var4497)
    assert (var3824.url.path == '/path/final')

@asyncio.coroutine
def function2708(arg2222, arg2120):

    @asyncio.coroutine
    def function146(arg74):
        return web.HTTPMovedPermanently(location=var3835.router['name'].url_for(part='final'))

    @asyncio.coroutine
    def function925(arg1921):
        return web.Response(text='OK')
    var3129 = web.Application()
    var3835 = web.Application()
    var3835.router.add_get('/to', function146)
    var3835.router.add_get('/{part}', function925, name='name')
    var3129.add_subapp('/path', var3835)
    var1003 = yield from arg2120(var3129)
    var3760 = yield from var1003.get('/path/to')
    assert (var3760.status == 200)
    var2396 = yield from var3760.text()
    assert ('OK' == var2396)
    assert (var3760.url.path == '/path/final')

@asyncio.coroutine
def function424(arg46, arg2144):
    function614 = 'aiohttp.png'

    @asyncio.coroutine
    def function146(arg164):
        return web.HTTPMovedPermanently(location=var4536.router['name'].url_for(filename=function614))
    var2068 = web.Application()
    var4536 = web.Application()
    var4536.router.add_get('/to', function146)
    function820 = pathlib.Path(__file__).parent
    var4536.router.add_static('/static', function820, name='name')
    var2068.add_subapp('/path', var4536)
    var4478 = yield from arg2144(var2068)
    var3825 = yield from var4478.get('/path/to')
    assert (var3825.url.path == ('/path/static/' + function614))
    assert (var3825.status == 200)
    var2893 = yield from var3825.read()
    with (function820 / function614).open('rb') as var2741:
        assert (var2893 == var2741.read())

@asyncio.coroutine
def function384(arg24, arg1749):

    @asyncio.coroutine
    def function146(arg943):
        assert (arg943.var154 is var1943)
        return web.HTTPOk(text='OK')
    var154 = web.Application()
    var1943 = web.Application()
    var1943.router.add_get('/to', function146)
    var154.add_subapp('/path/', var1943)
    var2894 = yield from arg1749(var154)
    var1338 = yield from var2894.get('/path/to')
    assert (var1338.status == 200)
    var2012 = yield from var1338.text()
    assert ('OK' == var2012)

@asyncio.coroutine
def function734(arg1344, arg1805):

    @asyncio.coroutine
    def function146(arg1458):
        return web.HTTPOk(text='OK')
    var353 = web.Application()
    var696 = web.Application()
    var696.router.add_get('/to', function146)
    var353.add_subapp('/path/', var696)
    var4274 = yield from arg1805(var353)
    var2542 = yield from var4274.get('/path/other')
    assert (var2542.status == 404)

@asyncio.coroutine
def function383(arg451, arg2311):

    @asyncio.coroutine
    def function146(arg1702):
        return web.HTTPOk(text='OK')
    var4443 = web.Application()
    var576 = web.Application()
    var576.router.add_get('/to', function146)
    var4443.add_subapp('/path/', var576)
    var898 = yield from arg2311(var4443)
    var176 = yield from var898.get('/invalid/other')
    assert (var176.status == 404)

@asyncio.coroutine
def function2541(arg2214, arg3):

    @asyncio.coroutine
    def function146(arg1077):
        return web.HTTPOk(text='OK')
    var3169 = web.Application()
    var250 = web.Application()
    var250.router.add_get('/to', function146)
    var3169.add_subapp('/path/', var250)
    var956 = yield from arg3(var3169)
    var3809 = yield from var956.post('/path/to')
    assert (var3809.status == 405)
    assert (var3809.headers['Allow'] == 'GET,HEAD')

@asyncio.coroutine
def function2286(arg2109, arg1388):

    @asyncio.coroutine
    def function146(arg1659):
        arg1659.match_info.add_app(var451)
        return web.HTTPOk(text='OK')
    var451 = web.Application()
    var1076 = web.Application()
    var1076.router.add_get('/to', function146)
    var451.add_subapp('/path/', var1076)
    var591 = yield from arg1388(var451)
    var87 = yield from var591.get('/path/to')
    assert (var87.status == 500)

@asyncio.coroutine
def function320(arg1617, arg829):
    var2060 = []

    @asyncio.coroutine
    def function146(arg1613):
        return web.HTTPOk(text='OK')

    @asyncio.coroutine
    def function1829(arg1452, function146):

        @asyncio.coroutine
        def function2021(arg487):
            var2060.append((1, arg1452))
            var1861 = yield from function146(arg487)
            assert (200 == var1861.status)
            var2060.append((2, arg1452))
            return var1861
        return function2021
    var777 = web.Application(middlewares=[function1829])
    var824 = web.Application(middlewares=[function1829])
    var2716 = web.Application(middlewares=[function1829])
    var2716.router.add_get('/to', function146)
    var824.add_subapp('/b/', var2716)
    var777.add_subapp('/a/', var824)
    var782 = yield from arg829(var777)
    var980 = yield from var782.get('/a/b/to')
    assert (var980.status == 200)
    assert ([(1, var777), (1, var824), (1, var2716), (2, var2716), (2, var824), (2, var777)] == var2060)

@asyncio.coroutine
def function243(arg684, arg283):
    var3790 = []

    @asyncio.coroutine
    def function146(arg1948):
        return web.HTTPOk(text='OK')

    def function2209(arg274):

        @asyncio.coroutine
        def function1038(arg438, arg887):
            var3790.append(arg274)
        return function1038
    var749 = web.Application()
    var749.on_response_prepare.append(function2209(var749))
    var1850 = web.Application()
    var1850.on_response_prepare.append(function2209(var1850))
    var1729 = web.Application()
    var1729.on_response_prepare.append(function2209(var1729))
    var1729.router.add_get('/to', function146)
    var1850.add_subapp('/b/', var1729)
    var749.add_subapp('/a/', var1850)
    var4411 = yield from arg283(var749)
    var845 = yield from var4411.get('/a/b/to')
    assert (var845.status == 200)
    assert ([var749, var1850, var1729] == var3790)

@asyncio.coroutine
def function1714(arg234, arg325):
    var4600 = []

    @asyncio.coroutine
    def function2580(arg138):
        var4600.append(arg138)
    var3302 = web.Application()
    var3302.on_startup.append(function2580)
    var1174 = web.Application()
    var1174.on_startup.append(function2580)
    var3994 = web.Application()
    var3994.on_startup.append(function2580)
    var1174.add_subapp('/b/', var3994)
    var3302.add_subapp('/a/', var1174)
    yield from arg325(var3302)
    assert ([var3302, var1174, var3994] == var4600)

@asyncio.coroutine
def function1497(arg1238, arg964):
    var1391 = []

    def function2580(arg1071):
        var1391.append(arg1071)
    var3434 = web.Application()
    var3434.on_shutdown.append(function2580)
    var4741 = web.Application()
    var4741.on_shutdown.append(function2580)
    var2657 = web.Application()
    var2657.on_shutdown.append(function2580)
    var4741.add_subapp('/b/', var2657)
    var3434.add_subapp('/a/', var4741)
    var1789 = yield from arg964(var3434)
    yield from var1789.close()
    assert ([var3434, var4741, var2657] == var1391)

@asyncio.coroutine
def function1916(arg993, arg310):
    var404 = []

    @asyncio.coroutine
    def function2580(arg592):
        var404.append(arg592)
    var397 = web.Application()
    var397.on_cleanup.append(function2580)
    var2844 = web.Application()
    var2844.on_cleanup.append(function2580)
    var1641 = web.Application()
    var1641.on_cleanup.append(function2580)
    var2844.add_subapp('/b/', var1641)
    var397.add_subapp('/a/', var2844)
    var3007 = yield from arg310(var397)
    yield from var3007.close()
    assert ([var397, var2844, var1641] == var404)

@asyncio.coroutine
def function1396(arg1673, arg1641):

    @asyncio.coroutine
    def function146(arg550):
        return web.Response(headers={'Date': 'Sun, 30 Oct 2016 03:13:52 GMT', })
    var44 = web.Application()
    var44.router.add_get('/', function146)
    var3911 = yield from arg1641(var44)
    var2336 = yield from var3911.get('/')
    assert (200 == var2336.status)
    assert (var2336.headers['Date'] == 'Sun, 30 Oct 2016 03:13:52 GMT')

@asyncio.coroutine
def function1814(arg769, arg734):

    @asyncio.coroutine
    def function146(arg579):
        var738 = arg579.clone()
        var1805 = web.StreamResponse()
        yield from var1805.prepare(var738)
        return var1805
    var2026 = web.Application()
    var2026.router.add_get('/', function146)
    var309 = yield from arg734(var2026)
    var2434 = yield from var309.get('/')
    assert (200 == var2434.status)

@asyncio.coroutine
def function1494(arg574, arg1937):

    @asyncio.coroutine
    def function146(arg457):
        yield from arg457.post()
        return web.Response(body=b'ok')
    var3773 = (1024 ** 2)
    var1369 = web.Application()
    var1369.router.add_post('/', function146)
    var1243 = yield from arg1937(var1369)
    var1517 = {'long_string': ((var3773 * 'x') + 'xxx'), }
    var2619 = yield from var1243.post('/', data=var1517)
    assert (413 == var2619.status)
    var2715 = yield from var2619.text()
    assert ('Request Entity Too Large' in var2715)

@asyncio.coroutine
def function1339(arg1472, arg1853):

    @asyncio.coroutine
    def function146(arg1260):
        yield from arg1260.post()
        return web.Response(body=b'ok')
    var4131 = (1024 ** 2)
    var1488 = (var4131 * 2)
    var2833 = web.Application(client_max_size=var1488)
    var2833.router.add_post('/', function146)
    var3276 = yield from arg1853(var2833)
    var2326 = {'long_string': ((var4131 * 'x') + 'xxx'), }
    var2633 = yield from var3276.post('/', data=var2326)
    assert (200 == var2633.status)
    var690 = yield from var2633.text()
    assert ('ok' == var690)
    var4027 = {'log_string': ((var1488 * 'x') + 'xxx'), }
    var2633 = yield from var3276.post('/', data=var4027)
    assert (413 == var2633.status)
    var690 = yield from var2633.text()
    assert ('Request Entity Too Large' in var690)

@asyncio.coroutine
def function2194(arg1440, arg833):

    @asyncio.coroutine
    def function146(arg316):
        yield from arg316.post()
        return web.Response(body=b'ok')
    var1648 = (1024 ** 2)
    var686 = None
    var2103 = web.Application(client_max_size=var686)
    var2103.router.add_post('/', function146)
    var450 = yield from arg833(var2103)
    var1497 = {'long_string': ((var1648 * 'x') + 'xxx'), }
    var422 = yield from var450.post('/', data=var1497)
    assert (200 == var422.status)
    var2931 = yield from var422.text()
    assert ('ok' == var2931)
    var1431 = {'log_string': ((var1648 * 2) * 'x'), }
    var422 = yield from var450.post('/', data=var1431)
    assert (200 == var422.status)
    var2931 = yield from var422.text()
    assert (var2931 == 'ok')

@asyncio.coroutine
def function2649(arg1358, arg2118):

    @asyncio.coroutine
    def function146(arg880):
        try:
            yield from arg880.post()
        except ValueError:
            return web.HTTPOk()
        return web.HTTPBadRequest()
    var2313 = web.Application(client_max_size=10)
    var2313.router.add_post('/', function146)
    var4166 = yield from arg2118(var2313)
    var958 = {'long_string': (1024 * 'x'), 'file': io.BytesIO(b'test'), }
    var4285 = yield from var4166.post('/', data=var958)
    assert (200 == var4285.status)

@asyncio.coroutine
def function1017(arg1358, arg2118):

    @asyncio.coroutine
    def function146(arg1849):
        try:
            yield from arg1849.post()
        except ValueError:
            return web.HTTPOk()
        return web.HTTPBadRequest()
    var1999 = web.Application(client_max_size=2)
    var1999.router.add_post('/', function146)
    var3784 = yield from arg2118(var1999)
    var1844 = {'file': io.BytesIO(b'test'), }
    var1583 = yield from var3784.post('/', data=var1844)
    assert (200 == var1583.status)

@asyncio.coroutine
def function268(arg1358, arg2118):

    @asyncio.coroutine
    def function146(arg2095):
        var1318 = yield from arg2095.multipart()
        var3589 = yield from var1318.next()
        return web.Response(body=var3589)
    var4234 = web.Application(client_max_size=2)
    var4234.router.add_post('/', function146)
    var4717 = yield from arg2118(var4234)
    var2516 = {'file': io.BytesIO(b'test'), }
    var1618 = yield from var4717.post('/', data=var2516)
    assert (200 == var1618.status)
    var3083 = yield from var1618.read()
    assert (var3083 == b'test')
    var1466 = multipart.parse_content_disposition(var1618.headers['content-disposition'])
    assert (var1466 == ('attachment', {'name': 'file', 'filename': 'file', 'filename*': 'file', }))