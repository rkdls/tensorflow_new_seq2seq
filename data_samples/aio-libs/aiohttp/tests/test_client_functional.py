'HTTP client functional tests against aiohttp.web server'
import asyncio
import http.cookies
import io
import json
import pathlib
import ssl
from unittest import mock
import pytest
from multidict import MultiDict
import aiohttp
from aiohttp import hdrs, web
from aiohttp.client import ServerFingerprintMismatch
from aiohttp.multipart import MultipartWriter

@pytest.fixture
def function713():
    return pathlib.Path(__file__).parent

@pytest.fixture
def function2460(function713):
    function2460 = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    function2460.load_cert_chain(str((function713 / 'sample.crt')), str((function713 / 'sample.key')))
    return function2460

@pytest.fixture
def function1107(function713):
    return (function713 / 'sample.key')

def function2432(arg50):
    return arg50

@asyncio.coroutine
def function2055(arg1474, arg1727):

    @asyncio.coroutine
    def function1233(arg1709):
        var847 = yield from arg1709.read()
        assert (b'' == var847)
        return web.Response(body=b'OK')
    var293 = web.Application()
    var293.router.add_route('GET', '/', function1233)
    var1411 = aiohttp.TCPConnector(loop=arg1474, limit=1)
    var1549 = yield from arg1727(var293, connector=var1411)
    var1837 = yield from var1549.get('/')
    yield from var1837.read()
    var4521 = yield from var1549.get('/')
    yield from var4521.read()
    assert (1 == len(var1549._session.var1411._conns))

@asyncio.coroutine
def function1317(arg2012, arg585):

    @asyncio.coroutine
    def function1233(arg948):
        var487 = yield from arg948.read()
        assert (b'' == var487)
        return web.Response(body=b'OK')
    var1579 = web.Application()
    var1579.router.add_route('GET', '/', function1233)
    var2945 = aiohttp.TCPConnector(loop=arg2012, limit=1)
    var250 = yield from arg585(var1579, connector=var2945)
    var1683 = yield from var250.get('/')
    var1683.release()
    var3466 = yield from var250.get('/')
    var3466.release()
    assert (1 == len(var250._session.var2945._conns))

@asyncio.coroutine
def function1380(arg2167, arg933):

    @asyncio.coroutine
    def function1233(arg980):
        var2625 = yield from arg980.read()
        assert (b'' == var2625)
        var1344 = web.Response(body=b'OK')
        var1344.force_close()
        return var1344
    var3889 = web.Application()
    var3889.router.add_route('GET', '/', function1233)
    var2658 = aiohttp.TCPConnector(loop=arg2167, limit=1)
    var2732 = yield from arg933(var3889, connector=var2658)
    var4621 = yield from var2732.get('/')
    var4621.close()
    var4730 = yield from var2732.get('/')
    var4730.close()
    assert (0 == len(var2732._session.var2658._conns))

@asyncio.coroutine
def function1590(arg1331, arg877):

    @asyncio.coroutine
    def function1233(arg975):
        yield from arg975.read()
        return web.Response(body=b'OK')
    var186 = web.Application()
    var186.router.add_route('GET', '/', function1233)
    var1962 = yield from arg877(var186)
    var3405 = yield from var1962.get('/')
    assert var3405.closed
    assert (1 == len(var1962._session.connector._conns))

@asyncio.coroutine
def function72(arg529, arg161):

    @asyncio.coroutine
    def function1233(arg1813):
        var2066 = yield from arg1813.read()
        assert (b'' == var2066)
        return web.Response(status=304)
    var3750 = web.Application()
    var3750.router.add_route('GET', '/', function1233)
    var1450 = yield from arg161(var3750)
    var2896 = yield from var1450.get('/')
    assert (var2896.status == 304)
    var2855 = yield from var2896.read()
    assert (var2855 == b'')

@asyncio.coroutine
def function1163(arg1848, arg2082):

    @asyncio.coroutine
    def function1233(arg570):
        var339 = yield from arg570.read()
        assert (b'' == var339)
        return web.Response(body=b'test', status=304)
    var1570 = web.Application()
    var1570.router.add_route('GET', '/', function1233)
    var3621 = yield from arg2082(var1570)
    var1827 = yield from var3621.get('/')
    assert (var1827.status == 304)
    var419 = yield from var1827.read()
    assert (var419 == b'')

@asyncio.coroutine
def function2423(arg886, arg2310):

    @asyncio.coroutine
    def function1233(arg228):
        assert ('aiohttp' in arg228.headers['user-agent'])
        return web.Response()
    var715 = web.Application()
    var715.router.add_route('GET', '/', function1233)
    var4426 = yield from arg2310(var715)
    var4042 = yield from var4426.get('/')
    assert 200, var4042.status

@asyncio.coroutine
def function301(arg2118, arg540):

    @asyncio.coroutine
    def function1233(arg1477):
        assert (hdrs.USER_AGENT not in arg1477.headers)
        return web.Response()
    var3932 = web.Application()
    var3932.router.add_route('GET', '/', function1233)
    var270 = yield from arg540(var3932)
    var4505 = yield from var270.get('/', skip_auto_headers=['user-agent'])
    assert (200 == var4505.status)

@asyncio.coroutine
def function1942(arg1736, arg1579):

    @asyncio.coroutine
    def function1233(arg2321):
        assert (hdrs.USER_AGENT not in arg2321.headers)
        return web.Response()
    var4529 = web.Application()
    var4529.router.add_route('GET', '/', function1233)
    var2143 = yield from arg1579(var4529, skip_auto_headers=['user-agent'])
    var4267 = yield from var2143.get('/')
    assert (200 == var4267.status)

@asyncio.coroutine
def function1965(arg600, arg1257):

    @asyncio.coroutine
    def function1233(arg225):
        assert (hdrs.CONTENT_TYPE not in arg225.headers)
        return web.Response()
    var735 = web.Application()
    var735.router.add_route('GET', '/', function1233)
    var7 = yield from arg1257(var735)
    var4260 = yield from var7.get('/', skip_auto_headers=['content-type'])
    assert (200 == var4260.status)

@asyncio.coroutine
def function1955(arg381, arg1738):
    var4535 = b'some buffer'

    @asyncio.coroutine
    def function1233(arg2136):
        assert (len(var4535) == arg2136.content_length)
        var1877 = yield from arg2136.read()
        assert (var4535 == var1877)
        return web.Response()
    var4592 = web.Application()
    var4592.router.add_route('POST', '/', function1233)
    var1436 = yield from arg1738(var4592)
    var3268 = yield from var1436.post('/', data=io.BytesIO(var4535))
    assert (200 == var3268.status)

@asyncio.coroutine
def function1921(arg1651, arg1421):
    var1007 = b'some buffer'

    @asyncio.coroutine
    def function1233(arg1970):
        var508 = yield from arg1970.post()
        assert (['file'] == list(var508.keys()))
        assert (var1007 == var508['file'].file.read())
        return web.Response()
    var4502 = web.Application()
    var4502.router.add_route('POST', '/', function1233)
    var1651 = yield from arg1421(var4502)
    var4295 = yield from var1651.post('/', data={'file': io.BytesIO(var1007), })
    assert (200 == var4295.status)

@asyncio.coroutine
def function2819(arg2089, arg2369):
    var82 = 'some buffer'

    @asyncio.coroutine
    def function1233(arg402):
        assert (len(var82) == arg402.content_length)
        assert (arg402.headers['CONTENT-TYPE'] == 'text/plain; charset=utf-8')
        var2497 = yield from arg402.text()
        assert (var82 == var2497)
        return web.Response()
    var1290 = web.Application()
    var1290.router.add_route('POST', '/', function1233)
    var3475 = yield from arg2369(var1290)
    var74 = yield from var3475.post('/', data=io.StringIO(var82))
    assert (200 == var74.status)

@asyncio.coroutine
def function1362(arg1344, arg55):
    var4111 = 'текст'

    @asyncio.coroutine
    def function1233(arg1593):
        assert (arg1593.headers['CONTENT-TYPE'] == 'text/plain; charset=koi8-r')
        var1266 = yield from arg1593.text()
        assert (var4111 == var1266)
        return web.Response()
    var1668 = web.Application()
    var1668.router.add_route('POST', '/', function1233)
    var3780 = yield from arg55(var1668)
    var635 = aiohttp.TextIOPayload(io.StringIO(var4111), encoding='koi8-r')
    var856 = yield from var3780.post('/', data=var635)
    assert (200 == var856.status)

@asyncio.coroutine
def function2068(arg1646, function2460, arg1479, arg353):
    var1313 = aiohttp.TCPConnector(verify_ssl=False, loop=arg1646)

    @asyncio.coroutine
    def function1233(arg113):
        return web.HTTPOk(text='Test message')
    var4116 = web.Application()
    var4116.router.add_route('GET', '/', function1233)
    var1320 = yield from arg1479(var4116, ssl=function2460)
    var991 = yield from arg353(var1320, connector=var1313)
    var1880 = yield from var991.get('/')
    assert (200 == var1880.status)
    var277 = yield from var1880.text()
    assert (var277 == 'Test message')

@pytest.mark.parametrize('fingerprint', [b'\xa2\x06G\xad\xaa\xf5\xd8\\J\x99^by;\x06=', b's\x93\xfd:\xed\x08\x1do\xa9\xaeq9\x1a\xe3\xc5\x7f\x89\xe7l\xf9', b"0\x9a\xc9D\x83\xdc\x91'\x88\x91\x11\xa1d\x97\xfd\xcb~7U\x14D@L\x11\xab\x99\xa8\xae\xb7\x14\xee\x8b"], ids=['md5', 'sha1', 'sha256'])
@asyncio.coroutine
def function2249(arg408, arg109, arg1256, function2460, arg2337):

    @asyncio.coroutine
    def function1233(arg879):
        return web.HTTPOk(text='Test message')
    if ((len(arg2337) == 16) or (len(arg2337) == 20)):
        with pytest.warns(DeprecationWarning) as var3351:
            var2961 = aiohttp.TCPConnector(loop=arg1256, verify_ssl=False, fingerprint=arg2337)
        assert ('Use sha256.' in str(var3351[0].message))
    else:
        var2961 = aiohttp.TCPConnector(loop=arg1256, verify_ssl=False, fingerprint=arg2337)
    var3482 = web.Application()
    var3482.router.add_route('GET', '/', function1233)
    var3784 = yield from arg408(var3482, ssl=function2460)
    var4686 = yield from arg109(var3784, connector=var2961)
    var9 = yield from var4686.get('/')
    assert (var9.status == 200)
    var9.close()

@pytest.mark.parametrize('fingerprint', [b'\xa2\x06G\xad\xaa\xf5\xd8\\J\x99^by;\x06=', b's\x93\xfd:\xed\x08\x1do\xa9\xaeq9\x1a\xe3\xc5\x7f\x89\xe7l\xf9', b"0\x9a\xc9D\x83\xdc\x91'\x88\x91\x11\xa1d\x97\xfd\xcb~7U\x14D@L\x11\xab\x99\xa8\xae\xb7\x14\xee\x8b"], ids=['md5', 'sha1', 'sha256'])
@asyncio.coroutine
def function711(arg848, arg1131, arg289, function2460, arg468):

    @asyncio.coroutine
    def function1233(arg2145):
        return web.HTTPOk(text='Test message')
    var3087 = (b'\x00' * len(arg468))
    var2110 = aiohttp.TCPConnector(loop=arg289, verify_ssl=False, fingerprint=var3087)
    var2235 = web.Application()
    var2235.router.add_route('GET', '/', function1233)
    var4062 = yield from arg848(var2235, ssl=function2460)
    var1167 = yield from arg1131(var4062, connector=var2110)
    with pytest.raises(ServerFingerprintMismatch) as var1291:
        yield from var1167.get('/')
    var703 = var1291.value
    assert (var703.expected == var3087)
    assert (var703.got == arg468)

@asyncio.coroutine
def function1186(arg558, arg1194):

    @asyncio.coroutine
    def function1233(arg617):
        return web.Response(body=b'OK')
    var1175 = web.Application()
    var1175.router.add_route('GET', '/', function1233)
    var2054 = yield from arg558(var1175)
    var2955 = aiohttp.ClientSession(loop=arg1194)
    var701 = arg1194.create_task(var2955.get(var2054.make_url('/')))
    assert '{}'.format(var701).startswith('<Task pending')
    var756 = yield from task
    var756.close()
    var2955.close()

@asyncio.coroutine
def function2397(arg1176, arg1977):

    @asyncio.coroutine
    def function1233(arg663):
        assert ('q=t est' in arg663.rel_url.query_string)
        return web.Response()
    var3321 = web.Application()
    var3321.router.add_route('GET', '/', function1233)
    var568 = yield from arg1977(var3321)
    var525 = yield from var568.get('/', params='q=t+est')
    assert (200 == var525.status)

@asyncio.coroutine
def function853(arg2347, arg1378):

    @asyncio.coroutine
    def function43(arg2054):
        return web.Response(status=301, headers={'Location': '/ok?a=redirect', })

    @asyncio.coroutine
    def function1436(arg2300):
        assert (arg2300.rel_url.query_string == 'a=redirect')
        return web.Response(status=200)
    var2367 = web.Application()
    var2367.router.add_route('GET', '/ok', function1436)
    var2367.router.add_route('GET', '/redirect', function43)
    var4229 = yield from arg1378(var2367)
    var3898 = yield from var4229.get('/redirect', params={'a': 'initial', })
    assert (var3898.status == 200)

@asyncio.coroutine
def function1623(arg638, arg368):

    @asyncio.coroutine
    def function43(arg329):
        return web.Response(status=301, headers={'Location': '/ok#fragment', })

    @asyncio.coroutine
    def function1436(arg2065):
        return web.Response(status=200)
    var4368 = web.Application()
    var4368.router.add_route('GET', '/ok', function1436)
    var4368.router.add_route('GET', '/redirect', function43)
    var1769 = yield from arg368(var4368)
    var4087 = yield from var1769.get('/redirect')
    assert (var4087.status == 200)
    assert (var4087.url.path == '/ok')

@asyncio.coroutine
def function1182(arg516, arg1267):

    @asyncio.coroutine
    def function1436(arg130):
        return web.Response(status=200)
    var4693 = web.Application()
    var4693.router.add_route('GET', '/ok', function1436)
    var2585 = yield from arg1267(var4693)
    var3814 = yield from var2585.get('/ok#fragment')
    assert (var3814.status == 200)
    assert (var3814.url.path == '/ok')

@asyncio.coroutine
def function1409(arg96, arg2228):

    @asyncio.coroutine
    def function43(arg48):
        return web.Response(status=301, headers={'Location': '/ok', })

    @asyncio.coroutine
    def function1436(arg2057):
        return web.Response(status=200)
    var3238 = web.Application()
    var3238.router.add_route('GET', '/ok', function1436)
    var3238.router.add_route('GET', '/redirect', function43)
    var1059 = yield from arg2228(var3238)
    var4581 = yield from var1059.get('/ok')
    assert (len(var4581.history) == 0)
    assert (var4581.status == 200)
    var4178 = yield from var1059.get('/redirect')
    assert (len(var4178.history) == 1)
    assert (var4178.history[0].status == 301)
    assert (var4178.status == 200)

@asyncio.coroutine
def function738(arg1281, arg1449):

    @asyncio.coroutine
    def function1233(arg1671):
        var3230 = yield from arg1671.read()
        assert (b'' == var3230)
        var2394 = web.Response(body=b'OK')
        var2394.force_close()
        return var2394
    var3227 = web.Application()
    var3227.router.add_route('GET', '/', function1233)
    var1572 = aiohttp.TCPConnector(loop=arg1281, limit=1)
    var2604 = yield from arg1449(var3227, connector=var1572)
    var3440 = yield from var2604.get('/')
    var2207 = yield from var3440.read()
    assert (var2207 == b'OK')
    var4698 = yield from var2604.get('/')
    var2494 = yield from var4698.read()
    assert (var2494 == b'OK')
    assert (0 == len(var2604._session.var1572._conns))

@asyncio.coroutine
def function2349(arg188, arg1199):

    @asyncio.coroutine
    def function1233(arg240):
        return web.Response(body=b'OK')
    var4540 = web.Application()
    var4540.router.add_route('GET', '/', function1233)
    var1183 = yield from arg1199(var4540)
    var4316 = yield from asyncio.wait_for(var1183.get('/'), 10, loop=arg188)
    assert (var4316.status == 200)
    var2613 = yield from var4316.text()
    assert (var2613 == 'OK')

@asyncio.coroutine
def function2076(arg295, arg433):

    @asyncio.coroutine
    def function1233(arg1032):
        return web.Response()
    var1224 = web.Application()
    var1224.router.add_route('GET', '/', function1233)
    var132 = yield from arg433(var1224)
    var675 = yield from var132.get('/')
    assert (var675.status == 200)
    var2353 = tuple(((bytes(var2304), bytes(var1757)) for (var2304, var1757) in var675.var2353))
    assert (var2353 == ((b'Content-Length', b'0'), (b'Content-Type', b'application/octet-stream'), (b'Date', mock.ANY), (b'Server', mock.ANY)))
    var675.close()

@asyncio.coroutine
def function73(arg2095, arg934):

    @asyncio.coroutine
    def function1233(arg2341):
        var3631 = web.StreamResponse(status=204)
        var3631.content_length = 0
        var3631.content_type = 'application/json'
        var3631.headers['Content-Encoding'] = 'gzip'
        yield from var3631.prepare(arg2341)
        return var3631
    var3418 = web.Application()
    var3418.router.add_route('DELETE', '/', function1233)
    var3982 = yield from arg934(var3418)
    var4197 = yield from var3982.delete('/')
    assert (var4197.status == 204)
    assert var4197.closed

@asyncio.coroutine
def function1252(arg264, arg138, arg567):
    arg567.patch('aiohttp.helpers.ceil').side_effect = function2432

    @asyncio.coroutine
    def function1233(arg846):
        var1742 = web.StreamResponse()
        yield from asyncio.sleep(0.1, loop=arg264)
        yield from var1742.prepare(arg846)
        return var1742
    var3481 = web.Application()
    var3481.router.add_route('GET', '/', function1233)
    var2997 = yield from arg138(var3481)
    with pytest.raises(asyncio.TimeoutError):
        yield from var2997.get('/', timeout=0.01)

@asyncio.coroutine
def function973(arg1776, arg72, arg1607):
    arg1607.patch('aiohttp.helpers.ceil').side_effect = function2432

    @asyncio.coroutine
    def function1233(arg137):
        var456 = web.StreamResponse()
        yield from asyncio.sleep(0.1, loop=arg1776)
        yield from var456.prepare(arg137)
        return var456
    var1730 = web.Application()
    var1730.router.add_route('GET', '/', function1233)
    var2326 = aiohttp.TCPConnector(loop=arg1776)
    var912 = yield from arg72(var1730, connector=var2326)
    with pytest.raises(asyncio.TimeoutError):
        yield from var912.get('/', timeout=0.01)

@asyncio.coroutine
def function2373(arg1975, arg1116, arg2260):
    arg2260.patch('aiohttp.helpers.ceil').side_effect = function2432

    @asyncio.coroutine
    def function1233(arg1134):
        var3445 = web.StreamResponse()
        yield from asyncio.sleep(0.1, loop=arg1975)
        yield from var3445.prepare(arg1134)
        return var3445
    var3537 = web.Application()
    var3537.router.add_route('GET', '/', function1233)
    var2852 = aiohttp.TCPConnector(loop=arg1975)
    var627 = yield from arg1116(var3537, connector=var2852, read_timeout=0.01)
    with pytest.raises(asyncio.TimeoutError):
        yield from var627.get('/')

@asyncio.coroutine
def function2619(arg983, arg2073, arg714):
    arg714.patch('aiohttp.helpers.ceil').side_effect = function2432

    @asyncio.coroutine
    def function1233(arg1459):
        var4317 = web.StreamResponse(headers={'content-length': '100', })
        yield from var4317.prepare(arg1459)
        yield from var4317.drain()
        yield from asyncio.sleep(0.2, loop=arg983)
        return var4317
    var4261 = web.Application()
    var4261.router.add_route('GET', '/', function1233)
    var2992 = yield from arg2073(var4261)
    var2706 = yield from var2992.get('/', timeout=0.05)
    with pytest.raises(asyncio.TimeoutError):
        yield from var2706.read()

@asyncio.coroutine
def function2486(arg1754, arg1286, arg480):
    arg480.patch('aiohttp.helpers.ceil').side_effect = function2432

    @asyncio.coroutine
    def function1233(arg1016):
        var2191 = web.StreamResponse()
        yield from var2191.prepare(arg1016)
        return var2191
    var1861 = web.Application()
    var1861.router.add_route('GET', '/', function1233)
    var4074 = yield from arg1286(var1861)
    var4031 = yield from var4074.get('/', timeout=None)
    assert (var4031.status == 200)

@asyncio.coroutine
def function2561(arg816, arg887):

    @asyncio.coroutine
    def function1233(arg1822):
        var3798 = web.StreamResponse()
        yield from var3798.prepare(arg1822)
        with pytest.raises(aiohttp.ServerDisconnectedError):
            for var3353 in range(10):
                var3798.write(b'data\n')
                yield from var3798.drain()
                yield from asyncio.sleep(0.5, loop=arg816)
            return var3798
    var1603 = web.Application()
    var1603.router.add_route('GET', '/', function1233)
    var1939 = yield from arg887(var1603)
    with aiohttp.ClientSession(loop=arg816) as var4666:
        var2712 = False
        (var1798, var2798) = (var1939.make_url('/'), {'Connection': 'Keep-alive', })
        var3841 = yield from var4666.get(var1798, headers=var2798)
        with pytest.raises(aiohttp.ClientConnectionError):
            while True:
                var1354 = yield from var3841.content.readline()
                var1354 = var1354.strip()
                if (not var1354):
                    break
                assert (var1354 == b'data')
                if (not var2712):

                    def function1852():
                        arg816.create_task(var3841.release())
                    arg816.call_later(1.0, function1852)
                    var2712 = True

@asyncio.coroutine
def function219(arg964, arg2380):

    @asyncio.coroutine
    def function1233(arg86):
        var534 = web.StreamResponse()
        yield from var534.prepare(arg86)
        var534.write(b'data\n')
        yield from var534.drain()
        yield from asyncio.sleep(0.5, loop=arg964)
        return var534
    var1356 = web.Application()
    var1356.router.add_route('GET', '/', function1233)
    var655 = yield from arg2380(var1356)
    with aiohttp.ClientSession(loop=arg964) as var1447:
        (var2129, var4691) = (var655.make_url('/'), {'Connection': 'Keep-alive', })
        var4052 = yield from var1447.get(var2129, headers=var4691)
        while True:
            var3755 = yield from var4052.content.readline()
            var3755 = var3755.strip()
            if (not var3755):
                break
            assert (var3755 == b'data')
        assert (var4052.content.exception() is None)

@asyncio.coroutine
def function2785(arg1293, arg641):

    @asyncio.coroutine
    def function1233(arg546):
        var4506 = web.StreamResponse()
        yield from var4506.prepare(arg546)
        return var4506
    var1351 = web.Application()
    var1351.router.add_route('GET', '/', function1233)
    var555 = yield from arg641(var1351)
    with aiohttp.ClientSession(loop=arg1293) as var955:
        (var2046, var3866) = (var555.make_url('/'), {'Connection': 'Keep-alive', })
        var1153 = yield from var955.get(var2046, headers=var3866)
        var1153.content.set_exception(ValueError())
    assert isinstance(var1153.content.exception(), ValueError)

@asyncio.coroutine
def function1156(arg992, arg1373):

    @asyncio.coroutine
    def function1233(arg634):
        return web.Response(text=arg634.method)
    var2482 = web.Application()
    for var70 in ('get', 'post', 'put', 'delete', 'head', 'patch', 'options'):
        var2482.router.add_route(var70.upper(), '/', function1233)
    var3370 = yield from arg1373(var2482)
    for var70 in ('get', 'post', 'put', 'delete', 'head', 'patch', 'options'):
        var85 = yield from var3370.request(var70, '/')
        assert (var85.status == 200)
        assert (len(var85.history) == 0)
        var101 = yield from var85.read()
        var2270 = yield from var85.read()
        assert (var101 == var2270)
        var4399 = yield from var85.text()
        if (var70 == 'head'):
            assert (b'' == var101)
        else:
            assert (var70.upper() == var4399)

@asyncio.coroutine
def function531(arg882, arg1478):

    @asyncio.coroutine
    def function1233(arg2223):
        return web.Response(text=arg2223.method)
    var2288 = aiohttp.TCPConnector(resolve=True, loop=arg882)
    var2288.clear_dns_cache()
    var4133 = web.Application()
    for var1732 in ('get', 'post', 'put', 'delete', 'head'):
        var4133.router.add_route(var1732.upper(), '/', function1233)
    var2538 = yield from arg1478(var4133, connector=var2288, conn_timeout=0.2)
    for var1732 in ('get', 'post', 'put', 'delete', 'head'):
        var2972 = yield from var2538.request(var1732, '/')
        var3121 = yield from var2972.read()
        var4552 = yield from var2972.read()
        assert (var3121 == var4552)
        var2791 = yield from var2972.text()
        assert (var2972.status == 200)
        if (var1732 == 'head'):
            assert (b'' == var3121)
        else:
            assert (var1732.upper() == var2791)

@asyncio.coroutine
def function1357(arg1735, arg1354):

    @asyncio.coroutine
    def function1233(arg603):
        return web.Response(text=arg603.method)

    @asyncio.coroutine
    def function918(arg493):
        return web.HTTPFound(location='/')
    var4631 = web.Application()
    var4631.router.add_get('/', function1233)
    var4631.router.add_get('/redirect', function918)
    var429 = yield from arg1354(var4631)
    var3813 = yield from var429.get('/redirect')
    assert (200 == var3813.status)
    assert (1 == len(var3813.history))
    var3813.close()

@asyncio.coroutine
def function1564(arg2134, arg708):

    @asyncio.coroutine
    def function1233(arg1997):
        return web.Response(text=arg1997.method)

    @asyncio.coroutine
    def function918(arg296):
        return web.HTTPFound(location='/')
    var2574 = web.Application()
    var2574.router.add_get('/', function1233)
    var2574.router.add_get('/redirect', function918)
    var2574.router.add_head('/', function1233)
    var2574.router.add_head('/redirect', function918)
    var2231 = yield from arg708(var2574)
    var2328 = yield from var2231.request('head', '/redirect')
    assert (200 == var2328.status)
    assert (1 == len(var2328.history))
    assert (var2328.method == 'HEAD')
    var2328.close()

@asyncio.coroutine
def function2262(arg1427, arg720):

    @asyncio.coroutine
    def function918(arg1090):
        return web.HTTPFound(location='ftp://127.0.0.1/test/')
    var1632 = web.Application()
    var1632.router.add_get('/redirect', function918)
    var4162 = yield from arg720(var1632)
    with pytest.raises(ValueError):
        yield from var4162.get('/redirect')

@asyncio.coroutine
def function1687(arg68, arg168):

    @asyncio.coroutine
    def function1233(arg1963):
        return web.Response(text=arg1963.method)

    @asyncio.coroutine
    def function918(arg861):
        return web.HTTPFound(location='/')
    var3639 = web.Application()
    var3639.router.add_get('/', function1233)
    var3639.router.add_post('/redirect', function918)
    var301 = yield from arg168(var3639)
    var3214 = yield from var301.post('/redirect')
    assert (200 == var3214.status)
    assert (1 == len(var3214.history))
    var1388 = yield from var3214.text()
    assert (var1388 == 'GET')
    var3214.close()

@asyncio.coroutine
def function2824(arg1820, arg2031):

    @asyncio.coroutine
    def function1233(arg120):
        return web.Response(text=arg120.method)

    @asyncio.coroutine
    def function918(arg1692):
        yield from arg1692.read()
        return web.HTTPFound(location='/')
    var664 = json.function1375({'some': 'data', })
    var2192 = web.Application(debug=True)
    var2192.router.add_get('/', function1233)
    var2192.router.add_post('/redirect', function918)
    var2673 = yield from arg2031(var2192)
    var3667 = yield from var2673.post('/redirect', data=var664, headers={'Content-Length': str(len(var664)), })
    assert (200 == var3667.status)
    assert (1 == len(var3667.history))
    var4362 = yield from var3667.text()
    assert (var4362 == 'GET')
    var3667.close()

@asyncio.coroutine
def function153(arg36, arg615):

    @asyncio.coroutine
    def function1233(arg823):
        return web.Response(text=arg823.method)

    @asyncio.coroutine
    def function918(arg972):
        yield from arg972.read()
        return web.HTTPTemporaryRedirect(location='/')
    var2085 = web.Application()
    var2085.router.add_post('/', function1233)
    var2085.router.add_post('/redirect', function918)
    var2973 = yield from arg615(var2085)
    var1398 = yield from var2973.post('/redirect', data={'some': 'data', })
    assert (200 == var1398.status)
    assert (1 == len(var1398.history))
    var1661 = yield from var1398.text()
    assert (var1661 == 'POST')
    var1398.close()

@asyncio.coroutine
def function1882(arg741, arg2261):

    @asyncio.coroutine
    def function1233(arg1145):
        return web.Response(text=arg1145.method)

    @asyncio.coroutine
    def function918(arg557):
        var2065 = int(arg557.match_info['count'])
        if var2065:
            return web.HTTPFound(location='/redirect/{}'.format((var2065 - 1)))
        else:
            return web.HTTPFound(location='/')
    var4597 = web.Application()
    var4597.router.add_get('/', function1233)
    var4597.router.add_get('/redirect/{count:\\d+}', function918)
    var2011 = yield from arg2261(var4597)
    var4371 = yield from var2011.get('/redirect/5', max_redirects=2)
    assert (302 == var4371.status)
    assert (2 == len(var4371.history))
    var4371.close()

@asyncio.coroutine
def function2480(arg1036, arg1501):

    @asyncio.coroutine
    def function1233(arg1089):
        return web.Response(text='&'.join((((var2692 + '=') + var4048) for (var2692, var4048) in arg1089.query.items())))
    var2562 = web.Application()
    var2562.router.add_get('/', function1233)
    var44 = yield from arg1501(var2562)
    var596 = yield from var44.get('/', params={'q': 'test', })
    assert (200 == var596.status)
    var758 = yield from var596.text()
    assert (var758 == 'q=test')
    var596.close()

@asyncio.coroutine
def function1888(arg1311, arg1668):

    @asyncio.coroutine
    def function1233(arg901):
        return web.Response(text='&'.join((((var451 + '=') + var1519) for (var451, var1519) in arg901.query.items())))
    var326 = web.Application()
    var326.router.add_get('/', function1233)
    var3738 = yield from arg1668(var326)
    var396 = yield from var3738.get('/', params=MultiDict([('q', 'test'), ('q', 'test2')]))
    assert (200 == var396.status)
    var748 = yield from var396.text()
    assert (var748 == 'q=test&q=test2')
    var396.close()

@asyncio.coroutine
def function687(arg623, arg443):

    @asyncio.coroutine
    def function1233(arg1621):
        return web.Response(text='&'.join((((var446 + '=') + var593) for (var446, var593) in arg1621.query.items())))
    var2617 = web.Application()
    var2617.router.add_get('/', function1233)
    var3023 = yield from arg443(var2617)
    var2280 = yield from var3023.get('/?test=true', params={'q': 'test', })
    assert (200 == var2280.status)
    var2689 = yield from var2280.text()
    assert (var2689 == 'test=true&q=test')
    var2280.close()

@asyncio.coroutine
def function2176(arg1785, arg2133):

    @asyncio.coroutine
    def function1233(arg1771):
        var4651 = yield from arg1771.post()
        return web.json_response(dict(var4651))
    var299 = web.Application()
    var299.router.add_post('/', function1233)
    var2931 = yield from arg2133(var299)
    var3086 = yield from var2931.post('/', data={'some': 'data', })
    assert (200 == var3086.status)
    var2946 = yield from var3086.json()
    assert (var2946 == {'some': 'data', })
    var3086.close()

@asyncio.coroutine
def function1242(arg1181, arg808):

    @asyncio.coroutine
    def function1233(arg89):
        var1314 = yield from arg89.post()
        return web.json_response(dict(var1314))
    var3292 = web.Application()
    var3292.router.add_post('/', function1233)
    var3938 = yield from arg808(var3292)
    var1758 = aiohttp.FormData()
    var1758.add_field('name', 'text')
    var3790 = yield from var3938.post('/', data=var1758)
    assert (200 == var3790.status)
    var4397 = yield from var3790.json()
    assert (var4397 == {'name': 'text', })
    var3790.close()

@asyncio.coroutine
def function2453(arg630, arg254):

    @asyncio.coroutine
    def function1233(arg1590):
        var4466 = yield from arg1590.multipart()
        var2763 = yield from var4466.next()
        var1196 = yield from var2763.var1196()
        return web.Response(text=var1196)
    var3647 = web.Application()
    var3647.router.add_post('/', function1233)
    var2960 = yield from arg254(var3647)
    var4424 = aiohttp.FormData()
    var4424.add_field('name', 'текст', content_type='text/plain; charset=koi8-r')
    var1256 = yield from var2960.post('/', data=var4424)
    assert (200 == var1256.status)
    var1444 = yield from var1256.text()
    assert (var1444 == 'текст')
    var1256.close()

@asyncio.coroutine
def function1366(arg935, arg756):

    @asyncio.coroutine
    def function1233(arg237):
        var4688 = yield from arg237.post()
        assert ('name' in var4688)
        return web.Response(text=var4688['name'])
    var1913 = web.Application()
    var1913.router.add_post('/', function1233)
    var2021 = yield from arg756(var1913)
    var1960 = aiohttp.FormData(charset='koi8-r')
    var1960.add_field('name', 'текст')
    var4636 = yield from var2021.post('/', data=var1960)
    assert (200 == var4636.status)
    var2632 = yield from var4636.text()
    assert (var2632 == 'текст')
    var4636.close()

@asyncio.coroutine
def function1414(arg1650, arg219):

    @asyncio.coroutine
    def function1233(arg12):
        var553 = yield from arg12.post()
        return web.Response(text=var553['name'])
    var3770 = web.Application()
    var3770.router.add_post('/', function1233)
    var549 = yield from arg219(var3770)
    var4309 = aiohttp.FormData()
    var4309.add_field('name', 'текст', content_type='text/plain; charset=koi8-r')
    var2044 = yield from var549.post('/', data=var4309)
    assert (200 == var2044.status)
    var2347 = yield from var2044.text()
    assert (var2347 == 'текст')
    var2044.close()

@asyncio.coroutine
def function584(arg87, arg1824):

    @asyncio.coroutine
    def function1233(arg2010):
        var112 = yield from arg2010.post()
        assert (var112['name'] == 'text')
        return web.Response(text=var112['name'])
    var4283 = web.Application()
    var4283.router.add_post('/', function1233)
    var1626 = yield from arg1824(var4283)
    var3878 = aiohttp.FormData()
    var3878.add_field('name', 'text', content_transfer_encoding='base64')
    var1924 = yield from var1626.post('/', data=var3878)
    assert (200 == var1924.status)
    var1130 = yield from var1924.text()
    assert (var1130 == 'text')
    var1924.close()

@asyncio.coroutine
def function1972(arg274, arg517):

    @asyncio.coroutine
    def function1233(arg1774):
        var3959 = yield from arg1774.post()
        assert (var3959['name'] == 'text')
        return web.Response(body=var3959['name'])
    var3597 = web.Application()
    var3597.router.add_post('/', function1233)
    var1229 = yield from arg517(var3597)
    var2551 = aiohttp.FormData()
    var2551.add_field('name', 'text', content_type='text/plain', content_transfer_encoding='base64')
    var360 = yield from var1229.post('/', data=var2551)
    assert (200 == var360.status)
    var1273 = yield from var360.text()
    assert (var1273 == 'text')
    var360.close()

@asyncio.coroutine
def function2411(arg1956, arg100):

    @asyncio.coroutine
    def function1233(arg486):
        var2420 = yield from arg486.post()
        assert (var2420 == MultiDict([('q', 'test1'), ('q', 'test2')]))
        return web.Response()
    var483 = web.Application()
    var483.router.add_post('/', function1233)
    var1697 = yield from arg100(var483)
    var1839 = yield from var1697.post('/', data=MultiDict([('q', 'test1'), ('q', 'test2')]))
    assert (200 == var1839.status)
    var1839.close()

@asyncio.coroutine
def function2430(arg592, arg2313):

    @asyncio.coroutine
    def function1233(arg553):
        var4544 = yield from arg553.post()
        return web.json_response(dict(var4544))
    var3275 = web.Application()
    var3275.router.add_post('/', function1233)
    var2951 = yield from arg2313(var3275)
    var760 = yield from var2951.post('/', data={'some': 'data', }, compress=True)
    assert (200 == var760.status)
    var2753 = yield from var760.json()
    assert (var2753 == {'some': 'data', })
    var760.close()

@asyncio.coroutine
def function815(arg304, arg1252, function1107):

    @asyncio.coroutine
    def function1233(arg1302):
        var3872 = yield from arg1302.post()
        assert (var3872['some'].filename == function1107.name)
        with function1107.open('rb') as var463:
            var1919 = var463.read()
        var1322 = var3872['some'].file.read()
        assert (var1919 == var1322)
        assert (var3872['test'].file.read() == b'data')
        return web.HTTPOk()
    var1420 = web.Application()
    var1420.router.add_post('/', function1233)
    var2590 = yield from arg1252(var1420)
    with function1107.open() as var2697:
        var3823 = yield from var2590.post('/', data={'some': f, 'test': b'data', }, chunked=True)
        assert (200 == var3823.status)
        var3823.close()

@asyncio.coroutine
def function2737(arg1528, arg1186, function1107):

    @asyncio.coroutine
    def function1233(arg1129):
        var2904 = yield from arg1129.post()
        assert (var2904['some'].filename == function1107.name)
        with function1107.open('rb') as var2100:
            var1615 = var2100.read()
        var2646 = var2904['some'].file.read()
        assert (var1615 == var2646)
        return web.HTTPOk()
    var3811 = web.Application()
    var3811.router.add_post('/', function1233)
    var3393 = yield from arg1186(var3811)
    with function1107.open() as var2210:
        var2370 = yield from var3393.post('/', data={'some': f, }, chunked=True, compress='deflate')
        assert (200 == var2370.status)
        var2370.close()

@asyncio.coroutine
def function296(arg1710, arg1518, function1107):

    @asyncio.coroutine
    def function1233(arg2124):
        var2243 = yield from arg2124.post()
        with function1107.open() as var3385:
            var914 = var3385.read()
        var2478 = var2243['some']
        assert (var914 == var2478)
        return web.HTTPOk()
    var672 = web.Application()
    var672.router.add_post('/', function1233)
    var2686 = yield from arg1518(var672)
    with function1107.open() as var829:
        var928 = yield from var2686.post('/', data={'some': var829.read(), })
        assert (200 == var928.status)
        var928.close()

@asyncio.coroutine
def function1062(arg1976, arg1521, function1107):

    @asyncio.coroutine
    def function1233(arg1157):
        var2731 = yield from arg1157.read()
        with function1107.open('rb') as var1902:
            var1903 = var1902.read()
        assert (var1903 == var2731)
        return web.HTTPOk()
    var4376 = web.Application()
    var4376.router.add_post('/', function1233)
    var2278 = yield from arg1521(var4376)
    with function1107.open() as var1521:
        var657 = yield from var2278.post('/', data=var1521.read())
        assert (200 == var657.status)
        var657.close()

@asyncio.coroutine
def function898(arg1868, arg1887, function1107):

    @asyncio.coroutine
    def function1233(arg1075):
        var4015 = yield from arg1075.post()
        assert (function1107.name == var4015['some'].filename)
        with function1107.open('rb') as var3584:
            var4121 = var3584.read()
        assert (var4121 == var4015['some'].file.read())
        return web.HTTPOk()
    var418 = web.Application()
    var418.router.add_post('/', function1233)
    var702 = yield from arg1887(var418)
    with function1107.open() as var3786:
        var3036 = yield from var702.post('/', data=[('some', var3786)])
        assert (200 == var3036.status)
        var3036.close()

@asyncio.coroutine
def function834(arg174, arg958, function1107):

    @asyncio.coroutine
    def function1233(arg727):
        var2428 = yield from arg727.post()
        assert (function1107.name == var2428['some'].filename)
        assert ('text/plain' == var2428['some'].content_type)
        with function1107.open('rb') as var1999:
            var2238 = var1999.read()
        assert (var2238 == var2428['some'].file.read())
        return web.HTTPOk()
    var2498 = web.Application()
    var2498.router.add_post('/', function1233)
    var3008 = yield from arg958(var2498)
    with function1107.open() as var939:
        var4450 = aiohttp.FormData()
        var4450.add_field('some', var939, content_type='text/plain')
        var639 = yield from var3008.post('/', data=var4450)
        assert (200 == var639.status)
        var639.close()

@asyncio.coroutine
def function2759(arg1506, arg1998, function1107):

    @asyncio.coroutine
    def function1233(arg405):
        var2496 = yield from arg405.text()
        with function1107.open('r') as var1638:
            var3329 = var1638.read()
            assert (var3329 == var2496)
        assert (arg405.content_type in ['application/pgp-keys', 'text/plain', 'application/octet-stream'])
        assert ('content-disposition' not in arg405.headers)
        return web.HTTPOk()
    var500 = web.Application()
    var500.router.add_post('/', function1233)
    var2513 = yield from arg1998(var500)
    with function1107.open() as var3640:
        var289 = yield from var2513.post('/', data=var3640)
        assert (200 == var289.status)
        var289.close()

@asyncio.coroutine
def function2879(arg247, arg789, function1107):

    @asyncio.coroutine
    def function1233(arg1374):
        var337 = yield from arg1374.text()
        with function1107.open('r') as var1906:
            var4000 = var1906.read()
            assert (var4000 == var337)
        assert (arg1374.content_type in ['application/pgp-keys', 'text/plain', 'application/octet-stream'])
        assert (arg1374.headers['content-disposition'] == 'inline; filename="sample.key"; filename*=utf-8\'\'sample.key')
        return web.HTTPOk()
    var4206 = web.Application()
    var4206.router.add_post('/', function1233)
    var303 = yield from arg789(var4206)
    with function1107.open() as var46:
        var141 = yield from var303.post('/', data=aiohttp.get_payload(var46, disposition='inline'))
        assert (200 == var141.status)
        var141.close()

@asyncio.coroutine
def function421(arg2280, arg440, function1107):

    @asyncio.coroutine
    def function1233(arg728):
        var3442 = yield from arg728.read()
        with function1107.open('rb') as var2351:
            var3567 = var2351.read()
        assert (var3567 == var3442)
        assert (arg728.content_type in ['application/pgp-keys', 'text/plain', 'application/octet-stream'])
        return web.HTTPOk()
    var4196 = web.Application()
    var4196.router.add_post('/', function1233)
    var894 = yield from arg440(var4196)
    with function1107.open('rb') as var4195:
        var1242 = yield from var894.post('/', data=var4195)
        assert (200 == var1242.status)
        var1242.close()

@asyncio.coroutine
def function965(arg146, arg292):

    @asyncio.coroutine
    def function1233(arg2219):
        var4175 = yield from arg2219.post()
        assert (b'data' == var4175['unknown'].file.read())
        assert (var4175['unknown'].content_type == 'application/octet-stream')
        assert (var4175['unknown'].filename == 'unknown')
        return web.HTTPOk()
    var2477 = web.Application()
    var2477.router.add_post('/', function1233)
    var4465 = yield from arg292(var2477)
    var2219 = io.BytesIO(b'data')
    var1574 = yield from var4465.post('/', data=[var2219])
    assert (200 == var1574.status)
    var1574.close()

@pytest.mark.xfail
@asyncio.coroutine
def function1425(arg73, arg290):

    @asyncio.coroutine
    def function1233(arg250):
        var4141 = yield from arg250.post()
        var4145 = list(var4141.values())
        assert (3 == len(var4145))
        assert (var4145[0] == 'foo')
        assert (var4145[1] == {'bar': 'баз', })
        assert (b'data' == var4141['unknown'].file.read())
        assert (var4141['unknown'].content_type == 'application/octet-stream')
        assert (var4141['unknown'].filename == 'unknown')
        return web.HTTPOk()
    var512 = web.Application()
    var512.router.add_post('/', function1233)
    var536 = yield from arg290(var512)
    with MultipartWriter('form-data') as var2185:
        var2185.append('foo')
        var2185.append_json({'bar': 'баз', })
        var2185.append_form([('тест', '4'), ('сетс', '2')])
    var3441 = yield from var536.post('/', data=var2185)
    assert (200 == var3441.status)
    var3441.close()

@asyncio.coroutine
def function2410(arg1705, arg2036):

    @asyncio.coroutine
    def function1233(arg477):
        var1607 = yield from arg477.post()
        assert (var1607['test'] == 'true')
        assert (var1607['unknown'].content_type == 'application/octet-stream')
        assert (var1607['unknown'].filename == 'unknown')
        assert (var1607['unknown'].file.read() == b'data')
        assert (var1607.getall('q') == ['t1', 't2'])
        return web.HTTPOk()
    var3157 = web.Application()
    var3157.router.add_post('/', function1233)
    var4695 = yield from arg2036(var3157)
    var3453 = io.BytesIO(b'data')
    var4721 = yield from var4695.post('/', data=(('test', 'true'), MultiDict([('q', 't1'), ('q', 't2')]), var3453))
    assert (200 == var4721.status)
    var4721.close()

@asyncio.coroutine
def function2504(arg1847, arg967, function1107):

    @asyncio.coroutine
    def function1233(arg513):
        var960 = yield from arg513.post()
        assert (var960['test'] == 'true')
        assert (var960['some'].content_type in ['application/pgp-keys', 'text/plain; charset=utf-8', 'application/octet-stream'])
        assert (var960['some'].filename == function1107.name)
        with function1107.open('rb') as var2743:
            assert (var960['some'].file.read() == var2743.read())
        return web.HTTPOk()
    var1168 = web.Application()
    var1168.router.add_post('/', function1233)
    var170 = yield from arg967(var1168)
    with function1107.open() as var2165:
        var722 = yield from var170.post('/', data={'test': 'true', 'some': f, })
        assert (200 == var722.status)
        var722.close()

@asyncio.coroutine
def function558(arg2191, arg2368, function1107):

    @asyncio.coroutine
    def function1233(arg1148):
        assert (arg1148.content_type == 'application/octet-stream')
        var4668 = yield from arg1148.read()
        with function1107.open('rb') as var2775:
            var4251 = var2775.read()
            assert (arg1148.content_length == len(var4251))
            assert (var4668 == var4251)
        return web.HTTPOk()
    var3491 = web.Application()
    var3491.router.add_post('/', function1233)
    var53 = yield from arg2368(var3491)
    with function1107.open('rb') as var4272:
        var4725 = len(var4272.read())

    @aiohttp.streamer
    def function617(arg1852, function1107):
        with function1107.open('rb') as var4272:
            var4276 = var4272.read(100)
            while data:
                yield from arg1852.write(var4276)
                var4276 = var4272.read(100)
    var2093 = yield from var53.post('/', data=function617(function1107), headers={'Content-Length': str(var4725), })
    assert (200 == var2093.status)
    var2093.close()

@asyncio.coroutine
def function2744(arg1910, arg904, function1107):

    @asyncio.coroutine
    def function1233(arg2263):
        assert (arg2263.content_type == 'application/octet-stream')
        var4410 = yield from arg2263.read()
        with function1107.open('rb') as var1064:
            var3732 = var1064.read()
            assert (arg2263.content_length == len(var3732))
            assert (var4410 == var3732)
        return web.HTTPOk()
    var1197 = web.Application()
    var1197.router.add_post('/', function1233)
    var2573 = yield from arg904(var1197)
    with function1107.open('rb') as var3267:
        var622 = len(var3267.read())

    @aiohttp.streamer
    def function617(arg1689):
        with function1107.open('rb') as var3267:
            var227 = var3267.read(100)
            while data:
                yield from arg1689.write(var227)
                var227 = var3267.read(100)
    var4602 = yield from var2573.post('/', data=function617, headers={'Content-Length': str(var622), })
    assert (200 == var4602.status)
    var4602.close()

@asyncio.coroutine
def function1512(function1107, arg613, arg1919):

    @asyncio.coroutine
    def function1233(arg397):
        assert (arg397.content_type == 'application/octet-stream')
        var4674 = yield from arg397.read()
        with function1107.open('rb') as var4381:
            var3124 = var4381.read()
        assert (arg397.content_length == len(var3124))
        assert (var4674 == var3124)
        return web.HTTPOk()
    var2452 = web.Application()
    var2452.router.add_post('/', function1233)
    var1657 = yield from arg1919(var2452)
    with function1107.open('rb') as var3686:
        var3476 = var3686.read()
    function617 = aiohttp.StreamReader(loop=arg613)
    function617.feed_data(var3476)
    function617.feed_eof()
    var636 = yield from var1657.post('/', data=function617, headers={'Content-Length': str(len(var3476)), })
    assert (200 == var636.status)
    var636.close()

@asyncio.coroutine
def function556(arg657, arg2214):

    @asyncio.coroutine
    def function1233(arg1874):
        assert (arg1874.content_type == 'application/json')
        var1526 = yield from arg1874.json()
        return web.Response(body=aiohttp.JsonPayload(var1526))
    var2462 = web.Application()
    var2462.router.add_post('/', function1233)
    var1218 = yield from arg2214(var2462)
    var2644 = yield from var1218.post('/', json={'some': 'data', })
    assert (200 == var2644.status)
    var4571 = yield from var2644.json()
    assert (var4571 == {'some': 'data', })
    var2644.close()
    with pytest.raises(ValueError):
        yield from var1218.post('/', data='some data', json={'some': 'data', })

@asyncio.coroutine
def function1735(arg2079, arg2177):

    @asyncio.coroutine
    def function1233(arg233):
        assert (arg233.content_type == 'application/json')
        var3641 = yield from arg233.json()
        return web.Response(body=aiohttp.JsonPayload(var3641))
    var1177 = False

    def function1375(arg1042):
        nonlocal used
        var1177 = True
        return json.function1375(arg1042)
    var1989 = web.Application()
    var1989.router.add_post('/', function1233)
    var3451 = yield from arg2177(var1989, json_serialize=function1375)
    var4593 = yield from var3451.post('/', json={'some': 'data', })
    assert (200 == var4593.status)
    assert used
    var3856 = yield from var4593.json()
    assert (var3856 == {'some': 'data', })
    var4593.close()
    with pytest.raises(ValueError):
        yield from var3451.post('/', data='some data', json={'some': 'data', })

@asyncio.coroutine
def function1226(arg421, arg1006):
    var3063 = False

    @asyncio.coroutine
    def function1233(arg580):
        var4035 = yield from arg580.post()
        assert (var4035 == {'some': 'data', })
        return web.HTTPOk()

    @asyncio.coroutine
    def function1605(arg79):
        nonlocal expect_called
        var4618 = arg79.headers.get(hdrs.EXPECT)
        if (var4618.lower() == '100-continue'):
            arg79.transport.write(b'HTTP/1.1 100 Continue\r\n\r\n')
            var3063 = True
    var1830 = web.Application()
    var1830.router.add_post('/', function1233, expect_handler=function1605)
    var3144 = yield from arg1006(var1830)
    var341 = yield from var3144.post('/', data={'some': 'data', }, expect100=True)
    assert (200 == var341.status)
    var341.close()
    assert expect_called

@asyncio.coroutine
def function692(arg814, arg1035):

    @asyncio.coroutine
    def function1233(arg1515):
        var1364 = web.Response(text='text')
        var1364.enable_chunked_encoding()
        var1364.enable_compression(web.ContentCoding.deflate)
        return var1364
    var3812 = web.Application()
    var3812.router.add_get('/', function1233)
    var486 = yield from arg1035(var3812)
    var3673 = yield from var486.get('/')
    assert (200 == var3673.status)
    var1525 = yield from var3673.text()
    assert (var1525 == 'text')
    var3673.close()

@asyncio.coroutine
def function2167(arg528, arg1828):

    @asyncio.coroutine
    def function1233(arg1567):
        var1942 = web.Response(text='text')
        var1942.enable_chunked_encoding()
        var1942.enable_compression(web.ContentCoding.gzip)
        return var1942
    var2949 = web.Application()
    var2949.router.add_get('/', function1233)
    var4153 = yield from arg1828(var2949)
    var2412 = yield from var4153.get('/')
    assert (200 == var2412.status)
    var3950 = yield from var2412.text()
    assert (var3950 == 'text')
    var2412.close()

@asyncio.coroutine
def function2637(arg1192, arg1435):

    @asyncio.coroutine
    def function1233(arg1324):
        var3840 = web.Response(text='text')
        var3840.headers['Content-Encoding'] = 'gzip'
        return var3840
    var3870 = web.Application()
    var3870.router.add_get('/', function1233)
    var3011 = yield from arg1435(var3870)
    var3397 = yield from var3011.get('/')
    assert (200 == var3397.status)
    with pytest.raises(aiohttp.ClientPayloadError):
        yield from var3397.read()
    var3397.close()

@asyncio.coroutine
def function1354(arg1991, arg2317):

    @asyncio.coroutine
    def function1233(arg2224):
        var4211 = web.StreamResponse()
        var4211.force_close()
        var4211._length_check = False
        var4211.headers['Transfer-Encoding'] = 'chunked'
        var2986 = yield from var4211.prepare(arg2224)
        var2986.write(b'9\r\n\r\n')
        yield from var2986.write_eof()
        return var4211
    var4613 = web.Application()
    var4613.router.add_get('/', function1233)
    var4384 = yield from arg2317(var4613)
    var1987 = yield from var4384.get('/')
    assert (200 == var1987.status)
    with pytest.raises(aiohttp.ClientPayloadError):
        yield from var1987.read()
    var1987.close()

@asyncio.coroutine
def function2086(arg746, arg1228):

    @asyncio.coroutine
    def function1233(arg249):
        var2801 = web.Response(text='text')
        var2801.headers['Content-Length'] = '10000'
        var2801.force_close()
        return var2801
    var292 = web.Application()
    var292.router.add_get('/', function1233)
    var999 = yield from arg1228(var292)
    var3155 = yield from var999.get('/')
    assert (200 == var3155.status)
    with pytest.raises(aiohttp.ClientPayloadError):
        yield from var3155.read()
    var3155.close()

@asyncio.coroutine
def function1694(arg1155, arg6):

    @asyncio.coroutine
    def function1233(arg1744):
        var257 = web.Response(text='text')
        var257.enable_chunked_encoding()
        return var257
    var1046 = web.Application()
    var1046.router.add_get('/', function1233)
    var380 = yield from arg6(var1046)
    var1223 = yield from var380.get('/')
    assert (200 == var1223.status)
    assert (var1223.headers['Transfer-Encoding'] == 'chunked')
    var4209 = yield from var1223.text()
    assert (var4209 == 'text')
    var1223.close()

@asyncio.coroutine
def function1334(arg454, arg189):

    @asyncio.coroutine
    def function1233(arg1372):
        return web.Response(text=arg1372.method)
    var4069 = web.Application()
    for var2766 in ('get', 'post', 'put', 'delete', 'head', 'patch', 'options'):
        var4069.router.add_route(var2766.upper(), '/', function1233)
    var242 = yield from arg454((lambda arg189: app))
    for var2766 in ('get', 'post', 'put', 'delete', 'head', 'patch', 'options'):
        var4313 = getattr(var242.session, var2766)
        var2334 = yield from var4313(var242.make_url('/'))
        assert (var2334.status == 200)
        assert (len(var2334.history) == 0)
        var546 = yield from var2334.read()
        var3855 = yield from var2334.read()
        assert (var546 == var3855)
        var3202 = yield from var2334.text()
        if (var2766 == 'head'):
            assert (b'' == var546)
        else:
            assert (var2766.upper() == var3202)

@asyncio.coroutine
def function2173(arg683, arg1):

    @asyncio.coroutine
    def function1233(arg1266):
        assert (arg1266.cookies.keys() == {'test1', 'test3'})
        assert (arg1266.cookies['test1'] == '123')
        assert (arg1266.cookies['test3'] == '456')
        return web.Response()
    var4151 = http.cookies.Morsel()
    var4151.set('test3', '456', '456')
    var849 = web.Application()
    var849.router.add_get('/', function1233)
    var1124 = yield from arg683(var849, cookies={'test1': '123', 'test2': c, })
    var600 = yield from var1124.get('/')
    assert (200 == var600.status)
    var600.close()

@asyncio.coroutine
def function1644(arg2344, arg997):

    @asyncio.coroutine
    def function1233(arg2002):
        assert (arg2002.cookies.keys() == {'test3'})
        assert (arg2002.cookies['test3'] == '456')
        return web.Response()
    var3946 = http.cookies.Morsel()
    var3946.set('test3', '456', '456')
    var3946['httponly'] = True
    var3946['secure'] = True
    var3946['max-age'] = 1000
    var594 = web.Application()
    var594.router.add_get('/', function1233)
    var3930 = yield from arg2344(var594, cookies={'test2': c, })
    var3534 = yield from var3930.get('/')
    assert (200 == var3534.status)
    var3534.close()

@asyncio.coroutine
def function599(arg966, arg1496):

    @asyncio.coroutine
    def function1233(arg1424):
        var2850 = web.Response()
        var2850.set_cookie('c1', 'cookie1')
        var2850.set_cookie('c2', 'cookie2')
        var2850.headers.add('Set-Cookie', 'ISAWPLB{A7F52349-3531-4DA9-8776-F74BC6F4F1BB}={925EC0B8-CB17-4BEB-8A35-1033813B0523}; HttpOnly; Path=/')
        return var2850
    var4511 = web.Application()
    var4511.router.add_get('/', function1233)
    var2142 = yield from arg966((lambda arg1496: app))
    with mock.patch('aiohttp.client_reqrep.client_logger') as var2912:
        var3361 = yield from var2142.get('/')
        assert (200 == var3361.status)
        var1191 = {var3271.key for var3271 in var2142.session.cookie_jar}
        assert (var1191 == {'c1', 'c2'})
        var3361.close()
        var2912.warning.assert_called_with('Can not load response cookies: %s', mock.ANY)

@asyncio.coroutine
def function2667(arg45):
    var1335 = aiohttp.ClientSession(loop=arg45)
    with pytest.raises(aiohttp.ClientConnectionError):
        yield from var1335.get('http://0.0.0.0:1')
    var1335.close()

@pytest.mark.xfail
@asyncio.coroutine
def function2145(arg1262, arg1964):

    @asyncio.coroutine
    def function1233(arg2092):
        arg2092.transport.close()
        return web.Response(text=('answer' * 1000))
    var4373 = web.Application()
    var4373.router.add_get('/', function1233)
    var49 = yield from arg1964(var4373)
    with pytest.raises(aiohttp.ClientResponseError):
        yield from var49.get('/')

@asyncio.coroutine
def function836(arg149, arg628):

    @asyncio.coroutine
    def function1233(arg1857):
        var1639 = web.StreamResponse(headers={'content-length': '1000', })
        yield from var1639.prepare(arg1857)
        yield from var1639.drain()
        var1639.write(b'answer')
        yield from var1639.drain()
        arg1857.transport.close()
        return var1639
    var1021 = web.Application()
    var1021.router.add_get('/', function1233)
    var2249 = yield from arg628(var1021)
    var1842 = yield from var2249.get('/')
    with pytest.raises(aiohttp.ClientPayloadError):
        yield from var1842.read()
    var1842.close()

@asyncio.coroutine
def function2815(arg25, arg472):

    @asyncio.coroutine
    def function1233(arg1989):
        assert (arg1989.headers['x-api-key'] == 'foo')
        return web.Response()
    var4523 = web.Application()
    var4523.router.add_post('/', function1233)
    var2820 = yield from arg472((lambda arg25: app))
    var1147 = yield from var2820.post('/', headers={'Content-Type': 'application/json', 'x-api-key': 'foo', })
    assert (var1147.status == 200)

@asyncio.coroutine
def function1808(arg1601, arg2094):

    @asyncio.coroutine
    def function1233(arg2346):
        return web.Response(text=arg2346.method)

    @asyncio.coroutine
    def function918(arg1993):
        return web.HTTPFound(location=var3322.make_url('/'))
    var4415 = web.Application()
    var4415.router.add_get('/', function1233)
    var4415.router.add_get('/redirect', function918)
    var3322 = yield from arg2094(var4415)
    var1682 = yield from var3322.get('/redirect')
    assert (200 == var1682.status)
    var1682.close()

@asyncio.coroutine
def function2630(arg2099, arg1662):

    @asyncio.coroutine
    def function43(arg1158):
        return web.Response(status=301)
    var4228 = web.Application()
    var4228.router.add_route('GET', '/redirect', function43)
    var4400 = yield from arg1662(var4228)
    with pytest.raises(RuntimeError) as var4063:
        yield from var4400.get('/redirect')
    assert (str(var4063.value) == 'GET http://127.0.0.1:{}/redirect returns a redirect [301] status but response lacks a Location or URI HTTP header'.format(var4400.port))

@asyncio.coroutine
def function1491(arg1574, arg376):

    @asyncio.coroutine
    def function43(arg656):
        return web.Response(status=301)
    var4654 = web.Application()
    var4654.router.add_route('GET', '/redirect', function43)
    var4194 = yield from arg376(var4654)
    with pytest.warns(DeprecationWarning):
        yield from var4194.get('/', encoding='utf-8')

@asyncio.coroutine
def function1659(arg1001, arg1320):

    @asyncio.coroutine
    def function43(arg332):
        return web.Response(status=301)
    var3506 = web.Application()
    var3506.router.add_route('GET', '/redirect', function43)
    var1415 = yield from arg1320(var3506)
    with pytest.warns(DeprecationWarning):
        yield from var1415.get('/', chunked=1024)

@asyncio.coroutine
def function506(arg61, arg328):

    @asyncio.coroutine
    def function43(arg1576):
        return web.HTTPBadRequest()
    var922 = web.Application()
    var922.router.add_route('GET', '/', function43)
    var492 = yield from arg328(var922, raise_for_status=True)
    with pytest.raises(aiohttp.ClientResponseError):
        yield from var492.get('/')