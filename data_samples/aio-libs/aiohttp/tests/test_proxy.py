import asyncio
import gc
import os
import socket
import unittest
from unittest import mock
from urllib.request import getproxies
from yarl import URL
import aiohttp
from aiohttp.client_reqrep import ClientRequest, ClientResponse
from aiohttp.test_utils import make_mocked_coro


class Class221(unittest.TestCase):

    def function2723(self):
        self.attribute501 = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def function2335(self):
        self.attribute501.stop()
        self.attribute501.run_forever()
        self.attribute501.close()
        gc.collect()

    @mock.patch('aiohttp.connector.ClientRequest')
    def function1340(self, arg735):
        var2739 = ClientRequest('GET', URL('http://www.python.org'), proxy=URL('http://proxy.example.com'), loop=self.attribute501)
        self.assertEqual(str(var2739.proxy), 'http://proxy.example.com')
        var3234 = aiohttp.TCPConnector(loop=self.attribute501)
        var3234._resolve_host = make_mocked_coro([mock.MagicMock()])
        var4104 = mock.Mock()
        self.attribute501.create_connection = make_mocked_coro((var4104.transport, var4104))
        var1447 = self.attribute501.run_until_complete(var3234.connect(var2739))
        self.assertEqual(var2739.url, URL('http://www.python.org'))
        self.assertIs(var1447._protocol, var4104)
        self.assertIs(var1447.transport, var4104.transport)
        arg735.assert_called_with('GET', URL('http://proxy.example.com'), auth=None, headers={'Host': 'www.python.org', }, loop=self.attribute501)

    def function2784(self):
        with self.assertRaises(ValueError) as var1670:
            ClientRequest('GET', URL('http://python.org'), proxy=URL('http://proxy.example.com'), proxy_auth=('user', 'pass'), loop=mock.Mock())
        self.assertEqual(var1670.exception.args[0], 'proxy_auth must be None or BasicAuth() tuple')

    @mock.patch('aiohttp.client_reqrep.PayloadWriter')
    def function497(self, arg2127):
        var3269 = mock.Mock()
        var557 = ClientRequest('CONNECT', URL('http://éé.com/'), loop=var3269)
        var557.response_class = mock.Mock()
        var557.write_bytes = mock.Mock()
        var557.write_bytes.return_value = asyncio.Future(loop=var3269)
        var557.write_bytes.return_value.set_result(None)
        var557.send(mock.Mock())
        arg2127.assert_called_with(mock.ANY, mock.ANY, 'xn--9caa.com:80', mock.ANY, loop=var3269)

    def function2045(self):
        var1894 = aiohttp.TCPConnector(loop=self.attribute501)
        var1894._resolve_host = make_mocked_coro(raise_exception=OSError('dont take it serious'))
        var4452 = ClientRequest('GET', URL('http://www.python.org'), proxy=URL('http://proxy.example.com'), loop=self.attribute501)
        var1607 = dict(var4452.headers)
        with self.assertRaises(aiohttp.ClientConnectorError):
            self.attribute501.run_until_complete(var1894.connect(var4452))
        self.assertEqual(var4452.url.path, '/')
        self.assertEqual(dict(var4452.headers), var1607)

    @mock.patch('aiohttp.connector.ClientRequest')
    def function47(self, arg2203):
        var887 = ClientRequest('GET', URL('http://proxy.example.com'), auth=aiohttp.helpers.BasicAuth('user', 'pass'), loop=self.attribute501)
        arg2203.return_value = var887
        self.assertIn('AUTHORIZATION', var887.headers)
        self.assertNotIn('PROXY-AUTHORIZATION', var887.headers)
        var1227 = aiohttp.TCPConnector(loop=self.attribute501)
        var1227._resolve_host = make_mocked_coro([mock.MagicMock()])
        (var4096, var2735) = (mock.Mock(), mock.Mock())
        self.attribute501.create_connection = make_mocked_coro((var4096, var2735))
        var4220 = ClientRequest('GET', URL('http://www.python.org'), proxy=URL('http://proxy.example.com'), proxy_auth=aiohttp.helpers.BasicAuth('user', 'pass'), loop=self.attribute501)
        self.assertNotIn('AUTHORIZATION', var4220.headers)
        self.assertNotIn('PROXY-AUTHORIZATION', var4220.headers)
        var3715 = self.attribute501.run_until_complete(var1227.connect(var4220))
        self.assertEqual(var4220.url, URL('http://www.python.org'))
        self.assertNotIn('AUTHORIZATION', var4220.headers)
        self.assertIn('PROXY-AUTHORIZATION', var4220.headers)
        self.assertNotIn('AUTHORIZATION', var887.headers)
        self.assertNotIn('PROXY-AUTHORIZATION', var887.headers)
        arg2203.assert_called_with('GET', URL('http://proxy.example.com'), auth=aiohttp.helpers.BasicAuth('user', 'pass'), loop=mock.ANY, headers=mock.ANY)
        var3715.close()

    def function1992(self):
        var1596 = ClientRequest('GET', URL('http://proxy.example.com'), auth=aiohttp.helpers.BasicAuth('юзер', 'пасс', 'utf-8'), loop=self.attribute501)
        self.assertIn('AUTHORIZATION', var1596.headers)

    @mock.patch('aiohttp.connector.ClientRequest')
    def function1065(self, arg1934):
        var4056 = ClientRequest('GET', URL('http://user:pass@proxy.example.com'), loop=self.attribute501)
        arg1934.return_value = var4056
        self.assertIn('AUTHORIZATION', var4056.headers)
        self.assertNotIn('PROXY-AUTHORIZATION', var4056.headers)
        var1878 = aiohttp.TCPConnector(loop=self.attribute501)
        var1878._resolve_host = make_mocked_coro([mock.MagicMock()])
        (var469, var1171) = (mock.Mock(), mock.Mock())
        self.attribute501.create_connection = make_mocked_coro((var469, var1171))
        var433 = ClientRequest('GET', URL('http://www.python.org'), proxy=URL('http://user:pass@proxy.example.com'), loop=self.attribute501)
        self.assertNotIn('AUTHORIZATION', var433.headers)
        self.assertNotIn('PROXY-AUTHORIZATION', var433.headers)
        var2804 = self.attribute501.run_until_complete(var1878.connect(var433))
        self.assertEqual(var433.url, URL('http://www.python.org'))
        self.assertNotIn('AUTHORIZATION', var433.headers)
        self.assertIn('PROXY-AUTHORIZATION', var433.headers)
        self.assertNotIn('AUTHORIZATION', var4056.headers)
        self.assertNotIn('PROXY-AUTHORIZATION', var4056.headers)
        arg1934.assert_called_with('GET', URL('http://user:pass@proxy.example.com'), auth=None, loop=mock.ANY, headers=mock.ANY)
        var2804.close()

    @mock.patch('aiohttp.connector.ClientRequest')
    def function11(self, arg1567):
        var1091 = ClientRequest('GET', URL('http://user:pass@proxy.example.com'), loop=self.attribute501)
        arg1567.return_value = var1091
        var4651 = dict(var1091.headers)
        var271 = aiohttp.TCPConnector(loop=self.attribute501)
        var271._resolve_host = make_mocked_coro(raise_exception=OSError('nothing personal'))
        var35 = ClientRequest('GET', URL('http://www.python.org'), proxy=URL('http://user:pass@proxy.example.com'), loop=self.attribute501)
        var3649 = dict(var35.headers)
        with self.assertRaises(aiohttp.ClientConnectorError):
            self.attribute501.run_until_complete(var271.connect(var35))
        self.assertEqual(var35.headers, var3649)
        self.assertEqual(var35.url.path, '/')
        self.assertEqual(var1091.headers, var4651)

    @mock.patch('aiohttp.connector.ClientRequest')
    def function2319(self, arg2208):
        var4652 = ClientRequest('GET', URL('http://proxy.example.com'), loop=self.attribute501)
        arg2208.return_value = var4652
        var1046 = ClientResponse('get', URL('http://proxy.example.com'))
        var1046._loop = self.attribute501
        var4652.send = var1673 = mock.Mock()
        var1673.return_value = var1046
        var1046.start = make_mocked_coro(mock.Mock(status=200))
        var2388 = aiohttp.TCPConnector(loop=self.attribute501)
        var2388._resolve_host = make_mocked_coro([{'hostname': 'hostname', 'host': '127.0.0.1', 'port': 80, 'family': socket.AF_INET, 'proto': 0, 'flags': 0, }])
        (var4139, var1856) = (mock.Mock(), mock.Mock())
        self.attribute501.create_connection = make_mocked_coro((var4139, var1856))
        var1177 = ClientRequest('GET', URL('https://www.python.org'), proxy=URL('http://proxy.example.com'), loop=self.attribute501)
        self.attribute501.run_until_complete(var2388._create_connection(var1177))
        self.assertEqual(var1177.url.path, '/')
        self.assertEqual(var4652.method, 'CONNECT')
        self.assertEqual(var4652.url, URL('https://www.python.org'))
        var4139.close.assert_called_once_with()
        var4139.get_extra_info.assert_called_with('socket', default=None)
        self.attribute501.run_until_complete(var4652.close())
        var1046.close()
        self.attribute501.run_until_complete(var1177.close())

    @mock.patch('aiohttp.connector.ClientRequest')
    def function2858(self, arg1561):
        var2387 = ClientRequest('GET', URL('http://proxy.example.com'), loop=self.attribute501)
        arg1561.return_value = var2387
        var1860 = ClientResponse('get', URL('http://proxy.example.com'))
        var1860._loop = self.attribute501
        var2387.send = var3004 = mock.Mock()
        var3004.return_value = var1860
        var1860.start = make_mocked_coro(mock.Mock(status=200))
        var346 = aiohttp.TCPConnector(loop=self.attribute501)
        var346._resolve_host = make_mocked_coro([{'hostname': 'hostname', 'host': '127.0.0.1', 'port': 80, 'family': socket.AF_INET, 'proto': 0, 'flags': 0, }])
        (var56, var3675) = (mock.Mock(), mock.Mock())
        var56.get_extra_info.return_value = None
        self.attribute501.create_connection = make_mocked_coro((var56, var3675))
        var4332 = ClientRequest('GET', URL('https://www.python.org'), proxy=URL('http://proxy.example.com'), loop=self.attribute501)
        with self.assertRaisesRegex(RuntimeError, 'Transport does not expose socket instance'):
            self.attribute501.run_until_complete(var346._create_connection(var4332))
        self.attribute501.run_until_complete(var2387.close())
        var1860.close()
        self.attribute501.run_until_complete(var4332.close())

    @mock.patch('aiohttp.connector.ClientRequest')
    def function356(self, arg91):
        var1725 = ClientRequest('GET', URL('http://proxy.example.com'), loop=self.attribute501)
        arg91.return_value = var1725
        var3901 = ClientResponse('get', URL('http://proxy.example.com'))
        var3901._loop = self.attribute501
        var1725.send = var3048 = mock.Mock()
        var3048.return_value = var3901
        var3901.start = make_mocked_coro(mock.Mock(status=400, reason='bad request'))
        var3040 = aiohttp.TCPConnector(loop=self.attribute501)
        var3040._resolve_host = make_mocked_coro([{'hostname': 'hostname', 'host': '127.0.0.1', 'port': 80, 'family': socket.AF_INET, 'proto': 0, 'flags': 0, }])
        (var574, var1140) = (mock.Mock(), mock.Mock())
        var574.get_extra_info.return_value = None
        self.attribute501.create_connection = make_mocked_coro((var574, var1140))
        var3112 = ClientRequest('GET', URL('https://www.python.org'), proxy=URL('http://proxy.example.com'), loop=self.attribute501)
        with self.assertRaisesRegex(aiohttp.ClientHttpProxyError, "400, message='bad request'"):
            self.attribute501.run_until_complete(var3040._create_connection(var3112))
        self.attribute501.run_until_complete(var1725.close())
        var3901.close()
        self.attribute501.run_until_complete(var3112.close())

    @mock.patch('aiohttp.connector.ClientRequest')
    def function118(self, arg987):
        var4087 = ClientRequest('GET', URL('http://proxy.example.com'), loop=self.attribute501)
        arg987.return_value = var4087
        var4513 = ClientResponse('get', URL('http://proxy.example.com'))
        var4513._loop = self.attribute501
        var4087.send = var2059 = mock.Mock()
        var2059.return_value = var4513
        var4513.start = make_mocked_coro(raise_exception=OSError('error message'))
        var2951 = aiohttp.TCPConnector(loop=self.attribute501)
        var2951._resolve_host = make_mocked_coro([{'hostname': 'hostname', 'host': '127.0.0.1', 'port': 80, 'family': socket.AF_INET, 'proto': 0, 'flags': 0, }])
        (var1761, var460) = (mock.Mock(), mock.Mock())
        var1761.get_extra_info.return_value = None
        self.attribute501.create_connection = make_mocked_coro((var1761, var460))
        var2112 = ClientRequest('GET', URL('https://www.python.org'), proxy=URL('http://proxy.example.com'), loop=self.attribute501)
        with self.assertRaisesRegex(OSError, 'error message'):
            self.attribute501.run_until_complete(var2951._create_connection(var2112))

    @mock.patch('aiohttp.connector.ClientRequest')
    def function583(self, arg937):
        var1507 = ClientRequest('GET', URL('http://proxy.example.com'), loop=self.attribute501)
        arg937.return_value = var1507
        var4632 = aiohttp.TCPConnector(loop=self.attribute501)
        var4632._resolve_host = make_mocked_coro([{'hostname': 'hostname', 'host': '127.0.0.1', 'port': 80, 'family': socket.AF_INET, 'proto': 0, 'flags': 0, }])
        (var3527, var1854) = (mock.Mock(), mock.Mock())
        var3527.get_extra_info.return_value = None
        self.attribute501.create_connection = make_mocked_coro((var3527, var1854))
        var4232 = ClientRequest('GET', URL('http://localhost:1234/path'), proxy=URL('http://proxy.example.com'), loop=self.attribute501)
        self.attribute501.run_until_complete(var4632._create_connection(var4232))
        self.assertEqual(var4232.url, URL('http://localhost:1234/path'))

    def function2422(self):
        var2780 = aiohttp.ClientRequest('GET', URL('http://localhost:1234/path'), proxy=URL('http://proxy.example.com'), proxy_auth=aiohttp.helpers.BasicAuth('user', 'pass'), loop=self.attribute501)
        self.assertEqual(('user', 'pass', 'latin1'), var2780.proxy_auth)

    def function1525(self):
        var4726 = aiohttp.ClientRequest('GET', URL('http://localhost:1234/path'), proxy=URL('http://proxy.example.com'), loop=self.attribute501)
        self.assertIsNone(var4726.proxy_auth)

    @mock.patch('aiohttp.connector.ClientRequest')
    def function2112(self, arg746):
        var391 = ClientRequest('GET', URL('http://proxy.example.com'), loop=self.attribute501)
        arg746.return_value = var391
        var4145 = ClientResponse('get', URL('http://proxy.example.com'))
        var4145._loop = self.attribute501
        var391.send = var3083 = mock.Mock()
        var3083.return_value = var4145
        var4145.start = make_mocked_coro(mock.Mock(status=200))
        var3477 = aiohttp.TCPConnector(loop=self.attribute501)
        var3477._resolve_host = make_mocked_coro([{'hostname': 'hostname', 'host': '127.0.0.1', 'port': 80, 'family': socket.AF_INET, 'proto': 0, 'flags': 0, }])
        (var240, var333) = (mock.Mock(), mock.Mock())
        self.attribute501.create_connection = make_mocked_coro((var240, var333))
        var4717 = ClientRequest('GET', URL('https://www.python.org'), proxy=URL('http://proxy.example.com'), loop=self.attribute501)
        self.attribute501.run_until_complete(var3477._create_connection(var4717))
        self.attribute501.create_connection.assert_called_with(mock.ANY, ssl=var3477.ssl_context, sock=mock.ANY, server_hostname='www.python.org')
        self.assertEqual(var4717.url.path, '/')
        self.assertEqual(var391.method, 'CONNECT')
        self.assertEqual(var391.url, URL('https://www.python.org'))
        var240.close.assert_called_once_with()
        var240.get_extra_info.assert_called_with('socket', default=None)
        self.attribute501.run_until_complete(var391.close())
        var4145.close()
        self.attribute501.run_until_complete(var4717.close())

    @mock.patch('aiohttp.connector.ClientRequest')
    def function1482(self, arg730):
        var3149 = ClientRequest('GET', URL('http://proxy.example.com'), auth=aiohttp.helpers.BasicAuth('user', 'pass'), loop=self.attribute501)
        arg730.return_value = var3149
        var1630 = ClientResponse('get', URL('http://proxy.example.com'))
        var1630._loop = self.attribute501
        var3149.send = var2291 = mock.Mock()
        var2291.return_value = var1630
        var1630.start = make_mocked_coro(mock.Mock(status=200))
        var3229 = aiohttp.TCPConnector(loop=self.attribute501)
        var3229._resolve_host = make_mocked_coro([{'hostname': 'hostname', 'host': '127.0.0.1', 'port': 80, 'family': socket.AF_INET, 'proto': 0, 'flags': 0, }])
        (var3729, var3324) = (mock.Mock(), mock.Mock())
        self.attribute501.create_connection = make_mocked_coro((var3729, var3324))
        self.assertIn('AUTHORIZATION', var3149.headers)
        self.assertNotIn('PROXY-AUTHORIZATION', var3149.headers)
        var3369 = ClientRequest('GET', URL('https://www.python.org'), proxy=URL('http://proxy.example.com'), loop=self.attribute501)
        self.assertNotIn('AUTHORIZATION', var3369.headers)
        self.assertNotIn('PROXY-AUTHORIZATION', var3369.headers)
        self.attribute501.run_until_complete(var3229._create_connection(var3369))
        self.assertEqual(var3369.url.path, '/')
        self.assertNotIn('AUTHORIZATION', var3369.headers)
        self.assertNotIn('PROXY-AUTHORIZATION', var3369.headers)
        self.assertNotIn('AUTHORIZATION', var3149.headers)
        self.assertIn('PROXY-AUTHORIZATION', var3149.headers)
        var3229._resolve_host.assert_called_with('proxy.example.com', 80)
        self.attribute501.run_until_complete(var3149.close())
        var1630.close()
        self.attribute501.run_until_complete(var3369.close())

    @mock.patch.dict(os.environ, {'http_proxy': 'http://proxy.example.com', })
    @mock.patch('aiohttp.connector.ClientRequest')
    def function586(self, arg1234):
        var178 = ClientRequest('GET', URL('http://www.python.org'), loop=self.attribute501)
        self.assertIsNone(var178.proxy)
        var553 = aiohttp.TCPConnector(loop=self.attribute501)
        var553._resolve_host = make_mocked_coro([mock.MagicMock()])
        var4558 = mock.Mock()
        self.attribute501.create_connection = make_mocked_coro((var4558.transport, var4558))
        var2121 = self.attribute501.run_until_complete(var553.connect(var178))
        self.assertEqual(var178.url, URL('http://www.python.org'))
        self.assertIs(var2121._protocol, var4558)
        self.assertIs(var2121.transport, var4558.transport)
        arg1234.assert_not_called()
        self.assertIn('http', getproxies())

    @mock.patch.dict(os.environ, {'http_proxy': 'http://proxy.example.com', })
    @mock.patch('aiohttp.connector.ClientRequest')
    def function269(self, arg2216):
        var1052 = ClientRequest('GET', URL('http://www.python.org'), proxy_from_env=True, loop=self.attribute501)
        self.assertEqual(str(var1052.proxy), 'http://proxy.example.com')
        var3841 = aiohttp.TCPConnector(loop=self.attribute501)
        var3841._resolve_host = make_mocked_coro([mock.MagicMock()])
        var1147 = mock.Mock()
        self.attribute501.create_connection = make_mocked_coro((var1147.transport, var1147))
        var2883 = self.attribute501.run_until_complete(var3841.connect(var1052))
        self.assertEqual(var1052.url, URL('http://www.python.org'))
        self.assertIs(var2883._protocol, var1147)
        self.assertIs(var2883.transport, var1147.transport)
        arg2216.assert_called_with('GET', URL('http://proxy.example.com'), auth=None, headers={'Host': 'www.python.org', }, loop=self.attribute501)
        self.assertIn('http', getproxies())

    @mock.patch.dict(os.environ, {'https_proxy': 'http://proxy.example.com', })
    @mock.patch('aiohttp.connector.ClientRequest')
    def function954(self, arg491):
        var3389 = ClientRequest('GET', URL('http://www.python.org'), proxy_from_env=True, loop=self.attribute501)
        self.assertIsNone(var3389.proxy)
        var1289 = aiohttp.TCPConnector(loop=self.attribute501)
        var1289._resolve_host = make_mocked_coro([mock.MagicMock()])
        var412 = mock.Mock()
        self.attribute501.create_connection = make_mocked_coro((var412.transport, var412))
        var3662 = self.attribute501.run_until_complete(var1289.connect(var3389))
        self.assertEqual(var3389.url, URL('http://www.python.org'))
        self.assertIs(var3662._protocol, var412)
        self.assertIs(var3662.transport, var412.transport)
        arg491.assert_not_called()
        self.assertIn('https', getproxies())
        self.assertNotIn('http', getproxies())

    @mock.patch.dict(os.environ, {'https_proxy': 'http://proxy.example.com', })
    @mock.patch('aiohttp.connector.ClientRequest')
    def function1358(self, arg6):
        var742 = ClientRequest('GET', URL('http://proxy.example.com'), loop=self.attribute501)
        arg6.return_value = var742
        var607 = ClientResponse('get', URL('http://proxy.example.com'))
        var607._loop = self.attribute501
        var742.send = var2681 = mock.Mock()
        var2681.return_value = var607
        var607.start = make_mocked_coro(mock.Mock(status=200))
        var566 = aiohttp.TCPConnector(loop=self.attribute501)
        var566._resolve_host = make_mocked_coro([{'hostname': 'hostname', 'host': '127.0.0.1', 'port': 80, 'family': socket.AF_INET, 'proto': 0, 'flags': 0, }])
        (var1525, var1631) = (mock.Mock(), mock.Mock())
        self.attribute501.create_connection = make_mocked_coro((var1525, var1631))
        var2225 = ClientRequest('GET', URL('https://www.python.org'), proxy_from_env=True, loop=self.attribute501)
        self.attribute501.run_until_complete(var566._create_connection(var2225))
        self.assertEqual(var2225.url.path, '/')
        self.assertEqual(var742.method, 'CONNECT')
        self.assertEqual(var742.url, URL('https://www.python.org'))
        var1525.close.assert_called_once_with()
        var1525.get_extra_info.assert_called_with('socket', default=None)
        self.attribute501.run_until_complete(var742.close())
        var607.close()
        self.attribute501.run_until_complete(var2225.close())
        self.assertIn('https', getproxies())

    @mock.patch.dict(os.environ, {'http_proxy': 'http://proxy23.example.com', })
    @mock.patch('aiohttp.connector.ClientRequest')
    def function1908(self, arg1143):
        var442 = ClientRequest('GET', URL('http://www.python.org'), proxy_from_env=True, proxy=URL('http://proxy.example.com'), loop=self.attribute501)
        self.assertEqual(str(var442.proxy), 'http://proxy.example.com')
        var2676 = aiohttp.TCPConnector(loop=self.attribute501)
        var2676._resolve_host = make_mocked_coro([mock.MagicMock()])
        var4024 = mock.Mock()
        self.attribute501.create_connection = make_mocked_coro((var4024.transport, var4024))
        var3547 = self.attribute501.run_until_complete(var2676.connect(var442))
        self.assertEqual(var442.url, URL('http://www.python.org'))
        self.assertIs(var3547._protocol, var4024)
        self.assertIs(var3547.transport, var4024.transport)
        arg1143.assert_called_with('GET', URL('http://proxy.example.com'), auth=None, headers={'Host': 'www.python.org', }, loop=self.attribute501)
        self.assertIn('http', getproxies())