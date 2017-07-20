'HTTP client functional tests.'
import asyncio
import binascii
import cgi
import contextlib
import email.parser
import gc
import http.server
import io
import json
import logging
import os
import os.path
import re
import ssl
import sys
import threading
import traceback
import unittest
import urllib.parse
from unittest import mock
from multidict import MultiDict
import aiohttp
import aiohttp.http
from aiohttp import client, helpers, test_utils, web
from aiohttp.multipart import MultipartWriter
from aiohttp.test_utils import run_briefly, unused_port

@contextlib.contextmanager
def function147(arg1231, *, listen_addr=('127.0.0.1', 0), use_ssl=False, router=None):
    var1639 = {}
    var653 = []


    class Class139:

        def __init__(self, arg88):
            (var1357, var3785) = arg88
            self.attribute905 = var1357
            self.attribute1856 = var3785
            self.attribute1280 = arg88
            self.attribute552 = '{}://{}:{}'.format(('https' if use_ssl else 'http'), var1357, var3785)

        def __getitem__(self, arg2074):
            return var1639[arg2074]

        def __setitem__(self, arg1993, arg443):
            var1639[arg1993] = arg443

        def function1322(self, *suffix):
            return urllib.parse.urljoin(self.attribute552, '/'.join((str(var3924) for var3924 in suffix)))

    @asyncio.coroutine
    def function1639(arg108):
        if var1639.get('close', False):
            return
        for (var1247, var3938) in arg108.message.headers.items():
            if ((var1247.upper() == 'EXPECT') and (var3938 == '100-continue')):
                arg108.writer.write(b'HTTP/1.0 100 Continue\r\n\r\n')
                break
        var3614 = router(var1639, arg108)
        return yield from var3614.dispatch()


    class Class224(web.RequestHandler):

        def function2267(self, arg1901):
            var653.append(arg1901)
            super().function2267(arg1901)
    if use_ssl:
        var4402 = os.path.join(os.path.dirname(__file__), '..', 'tests')
        var1323 = os.path.join(var4402, 'sample.key')
        var4383 = os.path.join(var4402, 'sample.crt')
        var3674 = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        var3674.load_cert_chain(var4383, var1323)
    else:
        var3674 = None

    def function1665(arg1231, arg132):
        var3476 = asyncio.new_event_loop()
        asyncio.set_event_loop(var3476)
        (var4510, var57) = listen_addr
        var2451 = var3476.create_server((lambda : Class224(web.Server(function1639, loop=var3476), keepalive_timeout=0.5)), var4510, var57, ssl=var3674)
        var1618 = var3476.run_until_complete(var2451)
        var954 = helpers.create_future(var3476)
        arg1231.call_soon_threadsafe(arg132.set_result, (var3476, var954, var1618.sockets[0].getsockname()))
        try:
            var3476.run_until_complete(var954)
        finally:
            run_briefly(var3476)
            for var3651 in var653:
                var3651.close()
            run_briefly(var3476)
            var1618.close()
            var3476.stop()
            var3476.close()
            gc.collect()
    var4399 = helpers.create_future(arg1231)
    var3410 = threading.Thread(target=function1665, args=(arg1231, var4399))
    var3410.start()
    (var370, var1486, var4177) = arg1231.run_until_complete(var4399)
    try:
        yield Class139(var4177)
    finally:
        var370.call_soon_threadsafe(var1486.set_result, None)
        var3410.join()


class Class393:
    var290 = '1.1'
    var4659 = http.server.BaseHTTPRequestHandler.responses

    def __init__(self, arg0, arg877):
        self.attribute407 = http.client.HTTPMessage()
        for (var685, var3529) in arg877.message.headers.items():
            self.attribute407.add_header(var685, var3529)
        self.attribute871 = arg0
        self.attribute2395 = arg877
        self.attribute793 = arg877.message.method
        self.attribute426 = arg877.message.path
        self.attribute1978 = arg877.message.version
        self.attribute925 = arg877.message.compression
        self.attribute781 = arg877.content
        var1869 = urllib.parse.urlsplit(self.attribute426)
        self.attribute2289 = var1869.path
        self.attribute1394 = var1869.query

    @staticmethod
    def function2747(arg1999):

        def function485(arg1740):
            var2923 = sys._getframe(1).var2923
            var1487 = var2923.setdefault('_mapping', [])
            var1487.append((re.compile(arg1999), arg1740.__name__))
            return arg1740
        return function485

    def function1128(self):
        for (var2196, var1335) in self._mapping:
            var2552 = var2196.var2552(self.attribute2289)
            if (var2552 is not None):
                try:
                    return yield from getattr(self, var1335)(var2552)
                except Exception:
                    var2195 = io.StringIO()
                    traceback.print_exc(file=var2195)
                    return yield from self.function2092(500, var2195.getvalue())
                return ()
        return yield from self.function2092(self.function1477(404))

    def function1477(self, arg1804):
        return web.Response(status=arg1804)

    @asyncio.coroutine
    def function2092(self, arg1398, arg574=None, arg146=None, arg1269=False, arg1329=None):
        var2547 = {}
        for (var2894, var3201) in self.attribute407.items():
            var2894 = '-'.join((var4513.capitalize() for var4513 in var2894.split('-')))
            var2547[var2894] = var3201
        var4025 = self.attribute407.get('content-encoding', '').lower()
        if ('gzip' in var4025):
            var133 = 'gzip'
        elif ('deflate' in var4025):
            var133 = 'deflate'
        else:
            var133 = ''
        var1163 = {'method': self.attribute793, 'version': ('%s.%s' % self.attribute1978), 'path': self.attribute426, 'headers': r_headers, 'origin': self.attribute2395.transport.get_extra_info('addr', ' ')[0], 'query': self.attribute1394, 'form': {}, 'compression': cmod, 'multipart-data': [], }
        if arg574:
            var1163['content'] = arg574
        else:
            var1163['content'] = yield from self.attribute2395.read().decode('utf-8', 'ignore')
        var231 = self.attribute407.get('content-type', '').lower()
        if (var231 == 'application/x-www-form-urlencoded'):
            var1163['form'] = urllib.parse.parse_qs(self.attribute781.decode('latin1'))
        elif var231.startswith('multipart/form-data'):
            var4168 = io.BytesIO()
            for (var2894, var3201) in self.attribute407.items():
                var4168.write(bytes('{}: {}\r\n'.format(var2894, var3201), 'latin1'))
            var751 = yield from self.attribute2395.read()
            var4168.write(b'\r\n')
            var4168.write(var751)
            var4168.write(b'\r\n')
            var4168.seek(0)
            var171 = email.parser.BytesParser().parse(var4168)
            if var171.is_multipart():
                for var2189 in var171.get_payload():
                    if var2189.is_multipart():
                        logging.warning('multipart msg is not expected')
                    else:
                        (var2894, var3735) = cgi.parse_header(var2189.get('content-disposition', ''))
                        var3735['data'] = var2189.get_payload()
                        var3735['content-type'] = var2189.get_content_type()
                        var2674 = var2189.get('content-transfer-encoding')
                        if (var2674 is not None):
                            var1163['content-transfer-encoding'] = var2674
                        var1163['multipart-data'].append(var3735)
        arg574 = json.dumps(var1163, indent=4, sort_keys=True)
        var4562 = [('Connection', 'close'), ('Content-Type', 'application/json')]
        if arg1269:
            var4562.append(('Transfer-Encoding', 'chunked'))
        else:
            var4562.append(('Content-Length', str(len(arg574))))
        if arg146:
            var4562.extend(arg146.items())
        for (var2894, var3201) in var4562:
            arg1398.arg146[var2894] = var3201
        if arg1269:
            self.attribute2395.writer.enable_chunking()
        yield from arg1398.prepare(self.attribute2395)
        if arg1329:
            try:
                arg1329(arg1398, arg574)
            except:
                return
        else:
            arg1398.write(arg574.encode('utf8'))
        return arg1398


class Class273(Class393):

    @Class393.function2747('/method/([A-Za-z]+)$')
    def function1030(self, arg49):
        return self.function2092(self.function1477(200))

    @Class393.function2747('/keepalive$')
    def function827(self, arg967):
        var1062 = self.attribute2395.var1062
        var1062._requests = (getattr(var1062, '_requests', 0) + 1)
        var2998 = self.function1477(200)
        if ('close=' in self.attribute1394):
            return self.function2092(var2998, 'requests={}'.format(var1062._requests))
        else:
            return self.function2092(var2998, 'requests={}'.format(var1062._requests), headers={'CONNECTION': 'keep-alive', })

    @Class393.function2747('/cookies$')
    def function777(self, arg1711):
        function777 = helpers.SimpleCookie()
        function777['c1'] = 'cookie1'
        function777['c2'] = 'cookie2'
        var1102 = self.function1477(200)
        for var907 in function777.output(header='').split('\n'):
            var1102.headers.extend({'Set-Cookie': var907.strip(), })
        var1102.headers.extend({'Set-Cookie': 'ISAWPLB{A7F52349-3531-4DA9-8776-F74BC6F4F1BB}={925EC0B8-CB17-4BEB-8A35-1033813B0523}; HttpOnly; Path=/', })
        return self.function2092(var1102)

    @Class393.function2747('/cookies_partial$')
    def function2788(self, arg1892):
        function777 = helpers.SimpleCookie()
        function777['c1'] = 'other_cookie1'
        var62 = self.function1477(200)
        for var646 in function777.output(header='').split('\n'):
            var62.add_header('Set-Cookie', var646.strip())
        return self.function2092(var62)

    @Class393.function2747('/broken$')
    def function628(self, arg2337):
        var4683 = self.function1477(200)

        def function1038(var4683, arg1727):
            self._transport.close()
            raise ValueError()
        return self.function2092(var4683, body=json.dumps({'t': (b'0' * 1024).decode('utf-8'), }), write_body=function1038)


class Class254(unittest.TestCase):

    def function498(self):
        self.attribute2267 = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def function2337(self):
        test_utils.run_briefly(self.attribute2267)
        self.attribute2267.close()
        gc.collect()

    def function648(self):
        with function147(self.attribute2267, router=Class273) as var3172:
            var246 = var3172.var246('method', 'post')
            var1811 = aiohttp.FormData()
            var1811.add_field('name', 'текст', content_type='text/plain; charset=koi8-r')
            var3654 = client.ClientSession(loop=self.attribute2267)
            var1781 = self.attribute2267.run_until_complete(var3654.request('post', var246, data=var1811))
            var4179 = self.attribute2267.run_until_complete(var1781.json())
            self.assertEqual(1, len(var4179['multipart-data']))
            var4731 = var4179['multipart-data'][0]
            self.assertEqual('name', var4731['name'])
            self.assertEqual('текст', var4731['data'])
            self.assertEqual(var1781.status, 200)
            var1781.close()
            var3654.close()

    def function2834(self):
        with function147(self.attribute2267, router=Class273) as var3594:
            var3682 = var3594.var3682('method', 'post')
            var1005 = aiohttp.FormData()
            var1005.add_field('name', 'текст', content_type='text/plain; charset=koi8-r')
            var2777 = self.attribute2267.run_until_complete(aiohttp.request('post', var3682, data=var1005, loop=self.attribute2267))
            var1300 = self.attribute2267.run_until_complete(var2777.json())
            self.assertEqual(1, len(var1300['multipart-data']))
            var2288 = var1300['multipart-data'][0]
            self.assertEqual('name', var2288['name'])
            self.assertEqual('текст', var2288['data'])
            self.assertEqual(var2777.status, 200)
            var2777.close()

    def function2629(self):
        with function147(self.attribute2267, router=Class273) as var759:
            var2773 = var759.var2773('method', 'post')
            var2392 = aiohttp.FormData()
            var2392.add_field('name', b'123', content_transfer_encoding='base64')
            var589 = client.ClientSession(loop=self.attribute2267)
            var2364 = self.attribute2267.run_until_complete(var589.request('post', var2773, data=var2392))
            var1070 = self.attribute2267.run_until_complete(var2364.json())
            self.assertEqual(1, len(var1070['multipart-data']))
            var898 = var1070['multipart-data'][0]
            self.assertEqual('name', var898['name'])
            self.assertEqual(b'123', binascii.a2b_base64(var898['data']))
            self.assertEqual(var2364.status, 200)
            var2364.close()
            var589.close()

    def function1236(self):
        with function147(self.attribute2267, router=Class273) as var4065:
            var2123 = var4065.var2123('method', 'post')
            with MultipartWriter('form-data') as var4608:
                var4608.append('foo')
                var4608.append_json({'bar': 'баз', })
                var4608.append_form([('тест', '4'), ('сетс', '2')])
            var101 = client.ClientSession(loop=self.attribute2267)
            var983 = self.attribute2267.run_until_complete(var101.request('post', var2123, data=var4608))
            var4642 = self.attribute2267.run_until_complete(var983.json())
            self.assertEqual(3, len(var4642['multipart-data']))
            self.assertEqual({'content-type': 'text/plain', 'data': 'foo', }, var4642['multipart-data'][0])
            self.assertEqual({'content-type': 'application/json', 'data': '{"bar": "\\u0431\\u0430\\u0437"}', }, var4642['multipart-data'][1])
            self.assertEqual({'content-type': 'application/x-www-form-urlencoded', 'data': '%D1%82%D0%B5%D1%81%D1%82=4&%D1%81%D0%B5%D1%82%D1%81=2', }, var4642['multipart-data'][2])
            self.assertEqual(var983.status, 200)
            var983.close()
            var101.close()

    def function78(self):
        with function147(self.attribute2267, router=Class273) as var3378:
            var3302 = var3378.var3302('method', 'post')
            var1996 = os.path.dirname(__file__)
            var4222 = os.path.join(var1996, 'sample.key')
            with open(var4222, 'rb') as var1661:
                var4344 = var1661.read()
            var2930 = helpers.create_future(self.attribute2267)

            @aiohttp.streamer
            def function2826(arg1131):
                yield from fut
                arg1131.write(var4344)
            self.attribute2267.call_later(0.01, var2930.set_result, True)
            var3796 = client.ClientSession(loop=self.attribute2267)
            var3190 = self.attribute2267.run_until_complete(var3796.request('post', var3302, data=function2826(), headers={'Content-Length': str(len(var4344)), }))
            var1778 = self.attribute2267.run_until_complete(var3190.json())
            var3190.close()
            var3796.close()
            self.assertEqual(str(len(var4344)), var1778['headers']['Content-Length'])
            self.assertEqual('application/octet-stream', var1778['headers']['Content-Type'])

    def function125(self):
        with function147(self.attribute2267, router=Class273) as var4426:
            var1019 = var4426.var1019('method', 'post')
            var1508 = os.path.dirname(__file__)
            var2235 = os.path.join(var1508, 'sample.key')
            with open(var2235, 'rb') as var122:
                var2880 = var122.read()
            var1769 = aiohttp.StreamReader(loop=self.attribute2267)
            var1769.feed_data(var2880)
            var1769.feed_eof()
            var610 = client.ClientSession(loop=self.attribute2267)
            var2959 = self.attribute2267.run_until_complete(var610.request('post', var1019, data=var1769, headers={'Content-Length': str(len(var2880)), }))
            var3252 = self.attribute2267.run_until_complete(var2959.json())
            var2959.close()
            var610.close()
            self.assertEqual(str(len(var2880)), var3252['headers']['Content-Length'])

    def function352(self):
        with function147(self.attribute2267, router=Class273) as var4292:
            var4405 = var4292.var4405('method', 'post')
            var4536 = os.path.dirname(__file__)
            var116 = os.path.join(var4536, 'sample.key')
            with open(var116, 'rb') as var3049:
                var3571 = var3049.read()
            var4736 = aiohttp.DataQueue(loop=self.attribute2267)
            var4736.feed_data(var3571[:100], 100)
            var4736.feed_data(var3571[100:], len(var3571[100:]))
            var4736.feed_eof()
            var457 = client.ClientSession(loop=self.attribute2267)
            var137 = self.attribute2267.run_until_complete(var457.request('post', var4405, data=var4736, headers={'Content-Length': str(len(var3571)), }))
            var2098 = self.attribute2267.run_until_complete(var137.json())
            var137.close()
            var457.close()
            self.assertEqual(str(len(var3571)), var2098['headers']['Content-Length'])

    def function2085(self):
        with function147(self.attribute2267, router=Class273) as var3959:
            var4309 = var3959.var4309('method', 'post')
            var1036 = os.path.dirname(__file__)
            var164 = os.path.join(var1036, 'sample.key')
            with open(var164, 'rb') as var1896:
                var2352 = var1896.read()
            var1990 = aiohttp.ChunksQueue(loop=self.attribute2267)
            var1990.feed_data(var2352[:100], 100)
            var212 = var2352[100:]
            var1990.feed_data(var212, len(var212))
            var1990.feed_eof()
            var645 = client.ClientSession(loop=self.attribute2267)
            var1358 = self.attribute2267.run_until_complete(var645.request('post', var4309, data=var1990, headers={'Content-Length': str(len(var2352)), }))
            var1410 = self.attribute2267.run_until_complete(var1358.json())
            var1358.close()
            var645.close()
            self.assertEqual(str(len(var2352)), var1410['headers']['Content-Length'])

    def function535(self):
        with function147(self.attribute2267, router=Class273) as var4474:
            var4474['close'] = True
            var3176 = client.ClientSession(loop=self.attribute2267)
            with self.assertRaises(aiohttp.ServerDisconnectedError):
                self.attribute2267.run_until_complete(var3176.request('get', var4474.url('method', 'get')))
            var3176.close()

    def function681(self):
        var934 = aiohttp.TCPConnector(loop=self.attribute2267)
        var3475 = client.ClientSession(loop=self.attribute2267, connector=var934)
        with function147(self.attribute2267, router=Class273) as var4622:
            var174 = self.attribute2267.run_until_complete(var3475.request('get', (var4622.url('keepalive') + '?close=1')))
            self.assertEqual(var174.status, 200)
            var2570 = self.attribute2267.run_until_complete(var174.json())
            self.assertEqual(var2570['content'], 'requests=1')
            var174.close()
            var174 = self.attribute2267.run_until_complete(var3475.request('get', var4622.url('keepalive')))
            self.assertEqual(var174.status, 200)
            var2570 = self.attribute2267.run_until_complete(var174.json())
            self.assertEqual(var2570['content'], 'requests=1')
            var174.close()
        var3475.close()
        var934.close()

    def function2388(self):
        var2908 = client.ClientSession(loop=self.attribute2267)
        with function147(self.attribute2267, router=Class273) as var4573:
            var445 = var4573.var445('method', 'post')
            var1077 = b'sample data'
            var600 = self.attribute2267.run_until_complete(var2908.request('post', var445, data=var1077, headers=MultiDict({'Content-Length': str(len(var1077)), })))
            var1221 = self.attribute2267.run_until_complete(var600.json())
            var600.close()
            self.assertEqual(str(len(var1077)), var1221['headers']['Content-Length'])
        var2908.close()

    def function1396(self):

        @asyncio.coroutine
        def function171(arg2232):
            var608 = aiohttp.TCPConnector(loop=self.attribute2267)
            var862 = client.ClientSession(loop=self.attribute2267, connector=var608)
            var3989 = yield from var862.request('GET', arg2232)
            yield from var3989.read()
            self.assertEqual(1, len(var608._conns))
            var608.close()
            var862.close()
        with function147(self.attribute2267, router=Class273) as var3613:
            var770 = var3613.var770('keepalive')
            self.attribute2267.run_until_complete(function171(var770))

    def function2578(self):


        class Class414(asyncio.Protocol):

            def function2211(self, arg1039):
                self.attribute132 = arg1039
                self.attribute353 = b''

            def function2686(self, arg2030):
                self.arg2030 += arg2030
                if arg2030.endswith(b'\r\n\r\n'):
                    self.attribute132.write(b'HTTP/1.1 200 OK\r\nCONTENT-LENGTH: 2\r\nCONNECTION: close\r\n\r\nok')
                    self.attribute132.close()

            def function280(self, arg1911):
                self.attribute132 = None

        @asyncio.coroutine
        def function1137():
            var173 = yield from self.attribute2267.create_server(Class414, '127.0.0.1', unused_port())
            var2911 = var173.sockets[0].getsockname()
            var1617 = aiohttp.TCPConnector(loop=self.attribute2267, limit=1)
            var1185 = client.ClientSession(loop=self.attribute2267, connector=var1617)
            var2170 = 'http://{}:{}/'.format(*var2911)
            for var3245 in range(2):
                var3249 = yield from var1185.request('GET', var2170)
                yield from var3249.read()
                self.assertEqual(0, len(var1617._conns))
            var1185.close()
            var1617.close()
            var173.close()
            yield from var173.wait_closed()
        self.attribute2267.run_until_complete(function1137())

    def function457(self):


        class Class64(asyncio.Protocol):

            def function806(self, arg2270):
                self.attribute1875 = arg2270
                self.attribute415 = b''

            def function790(self, arg2374):
                self.arg2374 += arg2374
                if arg2374.endswith(b'\r\n\r\n'):
                    self.attribute1875.write(b'HTTP/1.1 200 OK\r\nCONTENT-LENGTH: 2\r\n\r\nok')
                    self.attribute1875.close()

            def function598(self, arg1254):
                self.attribute1875 = None

        @asyncio.coroutine
        def function1766():
            var3752 = yield from self.attribute2267.create_server(Class64, '127.0.0.1', unused_port())
            var3589 = var3752.sockets[0].getsockname()
            var2284 = aiohttp.TCPConnector(loop=self.attribute2267, limit=1)
            var1480 = client.ClientSession(loop=self.attribute2267, connector=var2284)
            var2199 = 'http://{}:{}/'.format(*var3589)
            var4232 = yield from var1480.request('GET', var2199)
            yield from var4232.read()
            self.assertEqual(1, len(var2284._conns))
            with self.assertRaises(aiohttp.ServerDisconnectedError):
                yield from var1480.request('GET', var2199)
            self.assertEqual(0, len(var2284._conns))
            var1480.close()
            var2284.close()
            var3752.close()
            yield from var3752.wait_closed()
        self.attribute2267.run_until_complete(function1766())

    @mock.patch('aiohttp.client_reqrep.client_logger')
    def function1019(self, arg141):
        with function147(self.attribute2267, router=Class273) as var4359:
            var2716 = client.ClientSession(loop=self.attribute2267)
            var3031 = self.attribute2267.run_until_complete(var2716.request('get', var4359.url('cookies')))
            self.assertEqual(var3031.cookies['c1'].value, 'cookie1')
            self.assertEqual(var3031.cookies['c2'].value, 'cookie2')
            var3031.close()
            var2716.cookie_jar.update_cookies(var3031.cookies)
            var152 = self.attribute2267.run_until_complete(var2716.request('get', var4359.url('method', 'get')))
            self.assertEqual(var152.status, 200)
            var2327 = self.attribute2267.run_until_complete(var152.json())
            self.assertEqual(var2327['headers']['Cookie'], 'c1=cookie1; c2=cookie2')
            var152.close()
            var2716.close()

    def function2020(self):
        with function147(self.attribute2267, router=Class273) as var301:
            var1002 = client.ClientSession(loop=self.attribute2267, headers={'X-Real-IP': '192.168.0.1', })
            var1321 = self.attribute2267.run_until_complete(var1002.request('get', var301.url('method', 'get')))
            self.assertEqual(var1321.status, 200)
            var1602 = self.attribute2267.run_until_complete(var1321.json())
            self.assertIn('X-Real-Ip', var1602['headers'])
            self.assertEqual(var1602['headers']['X-Real-Ip'], '192.168.0.1')
            var1321.close()
            var1002.close()

    def function1248(self):
        with function147(self.attribute2267, router=Class273) as var2018:
            var812 = client.ClientSession(loop=self.attribute2267, headers=[('X-Real-IP', '192.168.0.1'), ('X-Sent-By', 'requests')])
            var4084 = self.attribute2267.run_until_complete(var812.request('get', var2018.url('method', 'get'), headers={'X-Sent-By': 'aiohttp', }))
            self.assertEqual(var4084.status, 200)
            var1073 = self.attribute2267.run_until_complete(var4084.json())
            self.assertIn('X-Real-Ip', var1073['headers'])
            self.assertIn('X-Sent-By', var1073['headers'])
            self.assertEqual(var1073['headers']['X-Real-Ip'], '192.168.0.1')
            self.assertEqual(var1073['headers']['X-Sent-By'], 'aiohttp')
            var4084.close()
            var812.close()

    def function659(self):
        with function147(self.attribute2267, router=Class273) as var3816:
            var1840 = client.ClientSession(loop=self.attribute2267, auth=helpers.BasicAuth('login', 'pass'))
            var2341 = self.attribute2267.run_until_complete(var1840.request('get', var3816.url('method', 'get')))
            self.assertEqual(var2341.status, 200)
            var4209 = self.attribute2267.run_until_complete(var2341.json())
            self.assertIn('Authorization', var4209['headers'])
            self.assertEqual(var4209['headers']['Authorization'], 'Basic bG9naW46cGFzcw==')
            var2341.close()
            var1840.close()

    def function248(self):
        with function147(self.attribute2267, router=Class273) as var1255:
            var4057 = client.ClientSession(loop=self.attribute2267, auth=helpers.BasicAuth('login', 'pass'))
            var2920 = self.attribute2267.run_until_complete(var4057.request('get', var1255.url('method', 'get'), auth=helpers.BasicAuth('other_login', 'pass')))
            self.assertEqual(var2920.status, 200)
            var4442 = self.attribute2267.run_until_complete(var2920.json())
            self.assertIn('Authorization', var4442['headers'])
            self.assertEqual(var4442['headers']['Authorization'], 'Basic b3RoZXJfbG9naW46cGFzcw==')
            var2920.close()
            var4057.close()

    def function588(self):
        with function147(self.attribute2267, router=Class273) as var4462:
            var1378 = client.ClientSession(loop=self.attribute2267, auth=helpers.BasicAuth('login', 'pass'))
            var3192 = {'Authorization': 'Basic b3RoZXJfbG9naW46cGFzcw==', }
            with self.assertRaises(ValueError):
                self.attribute2267.run_until_complete(var1378.request('get', var4462.url('method', 'get'), headers=var3192))
            var1378.close()