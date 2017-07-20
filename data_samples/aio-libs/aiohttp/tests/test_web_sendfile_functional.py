import asyncio
import os
import pathlib
import pytest
import aiohttp
from aiohttp import web
try:
    import ssl
except:
    var3190 = False

@pytest.fixture(params=['sendfile', 'fallback'], ids=['sendfile', 'fallback'])
def function1684(arg881):

    def function2859(*args, **kwargs):
        var1595 = web.FileResponse(*args, None=kwargs)
        if (arg881.param == 'fallback'):
            var1595._sendfile = var1595._sendfile_fallback
        return var1595
    return function2859

@asyncio.coroutine
def function2429(arg1653, arg384, function1684):
    var1568 = (pathlib.Path(__file__).parent / 'data.unknown_mime_type')

    @asyncio.coroutine
    def function632(arg1771):
        return function1684(var1568)
    var1225 = web.Application()
    var1225.router.add_get('/', function632)
    var353 = yield from arg384((lambda arg1653: app))
    var2516 = yield from var353.get('/')
    assert (var2516.status == 200)
    var4602 = yield from var2516.text()
    assert ('file content' == var4602.rstrip())
    assert ('application/octet-stream' == var2516.headers['Content-Type'])
    assert (var2516.headers.get('Content-Encoding') is None)
    yield from var2516.release()

@asyncio.coroutine
def function100(arg2086, arg2152, function1684):
    var1537 = (pathlib.Path(__file__).parent / 'data.unknown_mime_type')

    @asyncio.coroutine
    def function632(arg240):
        return function1684(str(var1537))
    var3710 = web.Application()
    var3710.router.add_get('/', function632)
    var1161 = yield from arg2152((lambda arg2086: app))
    var771 = yield from var1161.get('/')
    assert (var771.status == 200)
    var4156 = yield from var771.text()
    assert ('file content' == var4156.rstrip())
    assert ('application/octet-stream' == var771.headers['Content-Type'])
    assert (var771.headers.get('Content-Encoding') is None)
    yield from var771.release()

@asyncio.coroutine
def function651(arg2060, arg652):
    var3471 = web.Application()
    var4485 = yield from arg652((lambda arg2060: app))
    var1374 = yield from var4485.get('/fake')
    assert (var1374.status == 404)
    yield from var1374.release()

@asyncio.coroutine
def function2138(arg747, arg1494):
    var2944 = web.Application()
    var3659 = yield from arg1494((lambda arg747: app))
    var1572 = yield from var3659.get('/x*500')
    assert (var1572.status == 404)
    yield from var1572.release()

@asyncio.coroutine
def function488(arg1266, arg526):
    var4708 = web.Application()
    var3100 = yield from arg526((lambda arg1266: app))
    var3656 = yield from var3100.get('/../../')
    assert (var3656.status == 404)
    yield from var3656.release()

@asyncio.coroutine
def function581(arg340, arg2170, function1684):
    var720 = (pathlib.Path(__file__).parent / 'aiohttp.jpg')

    @asyncio.coroutine
    def function632(arg738):
        return function1684(var720, chunk_size=16)
    var2646 = web.Application()
    var2646.router.add_get('/', function632)
    var1970 = yield from arg2170((lambda arg340: app))
    var2662 = yield from var1970.get('/')
    assert (var2662.status == 200)
    var366 = yield from var2662.read()
    with var720.open('rb') as var2675:
        var1927 = var2675.read()
        assert (var1927 == var366)
    assert (var2662.headers['Content-Type'] == 'image/jpeg')
    assert (var2662.headers.get('Content-Encoding') is None)
    var2662.close()

@asyncio.coroutine
def function176(arg253, arg737, function1684):
    var189 = (pathlib.Path(__file__).parent / 'hello.txt.gz')

    @asyncio.coroutine
    def function632(arg826):
        return function1684(var189)
    var3355 = web.Application()
    var3355.router.add_get('/', function632)
    var3176 = yield from arg737((lambda arg253: app))
    var1509 = yield from var3176.get('/')
    assert (200 == var1509.status)
    var1243 = yield from var1509.read()
    assert (b'hello aiohttp\n' == var1243)
    var2549 = var1509.headers['CONTENT-TYPE']
    assert ('text/plain' == var2549)
    var3532 = var1509.headers['CONTENT-ENCODING']
    assert ('gzip' == var3532)
    var1509.close()

@asyncio.coroutine
def function2131(arg2036, arg1233, function1684):
    var3227 = 'data.unknown_mime_type'
    var3066 = (pathlib.Path(__file__).parent / var3227)

    @asyncio.coroutine
    def function632(arg1906):
        return function1684(var3066)
    var2071 = web.Application()
    var2071.router.add_get('/', function632)
    var3166 = yield from arg1233((lambda arg2036: app))
    var4422 = yield from var3166.get('/')
    assert (200 == var4422.status)
    var417 = var4422.headers.get('Last-Modified')
    assert (var417 is not None)
    var4422.close()
    var4422 = yield from var3166.get('/', headers={'If-Modified-Since': lastmod, })
    assert (304 == var4422.status)
    var4422.close()

@asyncio.coroutine
def function108(arg483, arg1194, function1684):
    var4033 = 'data.unknown_mime_type'
    var4372 = (pathlib.Path(__file__).parent / var4033)

    @asyncio.coroutine
    def function632(arg1607):
        return function1684(var4372)
    var1812 = web.Application()
    var1812.router.add_get('/', function632)
    var3445 = yield from arg1194((lambda arg483: app))
    var2182 = 'Mon, 1 Jan 1990 01:01:01 GMT'
    var4079 = yield from var3445.get('/', headers={'If-Modified-Since': lastmod, })
    assert (200 == var4079.status)
    var4079.close()

@asyncio.coroutine
def function271(arg1228, arg1164, function1684):
    var1742 = 'data.unknown_mime_type'
    var2380 = (pathlib.Path(__file__).parent / var1742)

    @asyncio.coroutine
    def function632(arg1422):
        return function1684(var2380)
    var4411 = web.Application()
    var4411.router.add_get('/', function632)
    var2697 = yield from arg1164((lambda arg1228: app))
    var1488 = 'not a valid HTTP-date'
    var2655 = yield from var2697.get('/', headers={'If-Modified-Since': lastmod, })
    assert (200 == var2655.status)
    var2655.close()

@asyncio.coroutine
def function893(arg1830, arg517, function1684):
    var2342 = 'data.unknown_mime_type'
    var4297 = (pathlib.Path(__file__).parent / var2342)

    @asyncio.coroutine
    def function632(arg1451):
        return function1684(var4297)
    var1625 = web.Application()
    var1625.router.add_get('/', function632)
    var1755 = yield from arg517((lambda arg1830: app))
    var2192 = 'Fri, 31 Dec 9999 23:59:59 GMT'
    var4124 = yield from var1755.get('/', headers={'If-Modified-Since': lastmod, })
    assert (304 == var4124.status)
    var4124.close()

@pytest.mark.skipif((not var3190), reason='ssl not supported')
@asyncio.coroutine
def function1718(arg1774, arg2073, arg1885):
    var4429 = os.path.var4429(__file__)
    var3767 = 'data.unknown_mime_type'
    var3012 = var3190.SSLContext(var3190.PROTOCOL_SSLv23)
    var3012.load_cert_chain(os.path.join(var4429, 'sample.crt'), os.path.join(var4429, 'sample.key'))
    var3071 = web.Application()
    var3071.router.add_static('/static', var4429)
    var2331 = yield from arg2073(var3071, ssl=var3012)
    var4452 = aiohttp.TCPConnector(verify_ssl=False, loop=arg1774)
    var650 = yield from arg1885(var2331, connector=var4452)
    var2952 = yield from var650.get(('/static/' + var3767))
    assert (200 == var2952.status)
    var4158 = yield from var2952.text()
    assert ('file content' == var4158.rstrip())
    var2314 = var2952.headers['CONTENT-TYPE']
    assert ('application/octet-stream' == var2314)
    assert (var2952.headers.get('CONTENT-ENCODING') is None)

@asyncio.coroutine
def function2686(arg680, arg192):
    var912 = os.path.var912(__file__)
    var4324 = '../README.rst'
    assert os.path.isfile(os.path.join(var912, var4324))
    var778 = web.Application()
    var778.router.add_static('/static', var912)
    var480 = yield from arg192(var778)
    var4539 = yield from var480.get(('/static/' + var4324))
    assert (404 == var4539.status)
    var646 = ('/static/dir/../' + var4324)
    var4539 = yield from var480.get(var646)
    assert (404 == var4539.status)
    var3844 = ('/static/' + os.path.abspath(os.path.join(var912, var4324)))
    var4539 = yield from var480.get(var3844)
    assert (404 == var4539.status)

def function1336():
    var1743 = os.path.dirname(__file__)
    web.StaticResource('/', var1743)
    var4516 = os.path.join(var1743, 'nonexistent-uPNiOEAg5d')
    with pytest.raises(ValueError):
        web.StaticResource('/', var4516)

@asyncio.coroutine
def function2282(arg283, arg1704, arg1485):
    var4465 = 'huge_data.unknown_mime_type'
    with arg1485.join(var4465).open('w') as var3816:
        for var3792 in range((1024 * 20)):
            var3816.write((chr(((var3792 % 64) + 32)) * 1024))
    var4234 = os.stat(str(arg1485.join(var4465)))
    var4592 = web.Application()
    var4592.router.add_static('/static', str(arg1485))
    var2012 = yield from arg1704(var4592)
    var3342 = yield from var2012.get(('/static/' + var4465))
    assert (200 == var3342.status)
    var160 = var3342.headers['CONTENT-TYPE']
    assert ('application/octet-stream' == var160)
    assert (var3342.headers.get('CONTENT-ENCODING') is None)
    assert (int(var3342.headers.get('CONTENT-LENGTH')) == var4234.st_size)
    var3816 = arg1485.join(var4465).open('rb')
    var4270 = 0
    var2107 = 0
    while (var4270 < var4234.st_size):
        var2184 = yield from var3342.content.readany()
        var4101 = var3816.read(len(var2184))
        assert (var2184 == var4101)
        var4270 += len(var2184)
        var2107 += 1
    var3816.close()

@asyncio.coroutine
def function780(arg1581, arg21, function1684):
    var4725 = (pathlib.Path(__file__).parent.parent / 'LICENSE.txt')

    @asyncio.coroutine
    def function632(arg461):
        return function1684(var4725, chunk_size=16)
    var3719 = web.Application()
    var3719.router.add_get('/', function632)
    var2856 = yield from arg21((lambda arg1581: app))
    with var4725.open('rb') as var733:
        var2755 = var733.read()
    var527 = yield from asyncio.gather(var2856.get('/', headers={'Range': 'bytes=0-999', }), var2856.get('/', headers={'Range': 'bytes=1000-1999', }), var2856.get('/', headers={'Range': 'bytes=2000-', }), loop=arg1581)
    assert (len(var527) == 3)
    assert (var527[0].status == 206), ("failed 'bytes=0-999': %s" % var527[0].reason)
    assert (var527[1].status == 206), ("failed 'bytes=1000-1999': %s" % var527[1].reason)
    assert (var527[2].status == 206), ("failed 'bytes=2000-': %s" % var527[2].reason)
    var1249 = yield from asyncio.gather(*(var2134.read() for var2134 in var527), loop=arg1581)
    assert (len(var1249[0]) == 1000), ("failed 'bytes=0-999', received %d bytes" % len(var1249[0]))
    assert (len(var1249[1]) == 1000), ("failed 'bytes=1000-1999', received %d bytes" % len(var1249[1]))
    var527[0].close()
    var527[1].close()
    var527[2].close()
    assert (var2755 == b''.join(var1249))

@asyncio.coroutine
def function178(arg1434, arg266, function1684):
    var3464 = (pathlib.Path(__file__).parent / 'aiohttp.png')

    @asyncio.coroutine
    def function632(arg975):
        return function1684(var3464, chunk_size=16)
    var2812 = web.Application()
    var2812.router.add_get('/', function632)
    var1416 = yield from arg266((lambda arg1434: app))
    with var3464.open('rb') as var1983:
        var1630 = var1983.read()
        var2111 = yield from var1416.get('/', headers={'Range': 'bytes=61000-62000', })
        assert (var2111.status == 206), ("failed 'bytes=61000-62000': %s" % var2111.reason)
        var1650 = yield from var2111.read()
        assert (len(var1650) == 108), ("failed 'bytes=0-999', received %d bytes" % len(var1650[0]))
        assert (var1630[61000:] == var1650)

@asyncio.coroutine
def function569(arg1971, arg1551, function1684):
    var3505 = (pathlib.Path(__file__).parent / 'aiohttp.png')

    @asyncio.coroutine
    def function632(arg23):
        return function1684(var3505, chunk_size=16)
    var3699 = web.Application()
    var3699.router.add_get('/', function632)
    var2878 = yield from arg1551((lambda arg1971: app))
    var370 = yield from var2878.get('/', headers={'Range': 'bytes=1000000-1200000', })
    assert (var370.status == 206), ("failed 'bytes=1000000-1200000': %s" % var370.reason)
    assert (var370.headers['content-length'] == '0')

@asyncio.coroutine
def function161(arg473, arg592, function1684):
    var2350 = (pathlib.Path(__file__).parent / 'aiohttp.png')

    @asyncio.coroutine
    def function632(arg1487):
        return function1684(var2350, chunk_size=16)
    var1307 = web.Application()
    var1307.router.add_get('/', function632)
    var697 = yield from arg592((lambda arg473: app))
    with var2350.open('rb') as var2722:
        var479 = var2722.read()
    var3251 = yield from var697.get('/', headers={'Range': 'bytes=-500', })
    assert (var3251.status == 206), var3251.reason
    var2218 = yield from var3251.read()
    var3251.close()
    assert (var479[(- 500):] == var2218)

@asyncio.coroutine
def function310(arg1468, arg401, function1684):
    var4187 = (pathlib.Path(__file__).parent / 'aiohttp.png')

    @asyncio.coroutine
    def function632(arg493):
        return function1684(var4187, chunk_size=16)
    var3504 = web.Application()
    var3504.router.add_get('/', function632)
    var157 = yield from arg401((lambda arg1468: app))
    var4356 = yield from var157.get('/', headers={'Range': 'blocks=0-10', })
    assert (var4356.status == 416), 'Range must be in bytes'
    var4356.close()
    var4356 = yield from var157.get('/', headers={'Range': 'bytes=100-0', })
    assert (var4356.status == 416), "Range start can't be greater than end"
    var4356.close()
    var4356 = yield from var157.get('/', headers={'Range': 'bytes=10-9', })
    assert (var4356.status == 416), "Range start can't be greater than end"
    var4356.close()
    var4356 = yield from var157.get('/', headers={'Range': 'bytes=a-f', })
    assert (var4356.status == 416), 'Range must be integers'
    var4356.close()
    var4356 = yield from var157.get('/', headers={'Range': 'bytes=0--10', })
    assert (var4356.status == 416), 'double dash in range'
    var4356.close()
    var4356 = yield from var157.get('/', headers={'Range': 'bytes=-', })
    assert (var4356.status == 416), 'no range given'
    var4356.close()