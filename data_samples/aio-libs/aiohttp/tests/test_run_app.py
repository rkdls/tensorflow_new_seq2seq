import asyncio
import contextlib
import os
import platform
import signal
import socket
import ssl
import subprocess
import sys
from io import StringIO
from unittest import mock
from uuid import uuid4
import pytest
from aiohttp import web
from aiohttp.test_utils import loop_context
var2719 = hasattr(socket, 'AF_UNIX')
if var2719:
    var60 = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        var60.bind((b'\x00' + uuid4().hex.encode('ascii')))
    except FileNotFoundError:
        var857 = True
    finally:
        var60.close()
        del _abstract_path_sock
    else:
        var857 = False
else:
    var857 = True
var2119 = pytest.mark.skipif(var857, reason='Linux-style abstract paths are not supported.')
var949 = pytest.mark.skipif((not var2719), reason='Unix domain sockets are not supported')
del _has_unix_domain_socks, _abstract_path_failed

def function514(arg1439):
    if (not hasattr(arg1439, '__dict__')):
        pytest.skip('can not override loop attributes')

def function2198():
    if (platform.system() == 'Windows'):
        pytest.skip('the test is not valid for Windows')

def function1627(arg610, arg1803):
    function514(arg610)
    arg1803.spy(arg610, 'create_server')
    arg610.call_later(0.05, arg610.stop)
    var1547 = web.Application()
    arg1803.spy(var1547, 'startup')
    web.run_app(var1547, loop=arg610, print=(lambda *args: None))
    assert (not arg610.is_closed())
    arg610.create_server.assert_called_with(mock.ANY, '0.0.0.0', 8080, ssl=None, backlog=128)
    var1547.startup.assert_called_once_with()

def function2419(arg1719, arg316):
    function514(arg1719)
    arg316.spy(arg1719, 'create_server')
    arg1719.call_later(0.05, arg1719.stop)
    asyncio.set_event_loop(arg1719)
    var2203 = web.Application()
    arg316.spy(var2203, 'startup')
    web.run_app(var2203, print=(lambda *args: None))
    assert arg1719.is_closed()
    arg1719.create_server.assert_called_with(mock.ANY, '0.0.0.0', 8080, ssl=None, backlog=128)
    var2203.startup.assert_called_once_with()
    asyncio.set_event_loop(None)
var3420 = [mock.call(mock.ANY, '/tmp/testsock1.sock', ssl=None, backlog=128)]
var3078 = [mock.call(mock.ANY, '/tmp/testsock1.sock', ssl=None, backlog=128), mock.call(mock.ANY, '/tmp/testsock2.sock', ssl=None, backlog=128)]
var89 = [mock.call(mock.ANY, '127.0.0.1', 8080, ssl=None, backlog=128)]
var4357 = [mock.call(mock.ANY, ('127.0.0.1', '192.168.1.1'), 8080, ssl=None, backlog=128)]
var4373 = [mock.call(mock.ANY, '0.0.0.0', 8989, ssl=None, backlog=128)]
var3177 = mock.Mock(getsockname=(lambda : ('mock-socket', 123)))
var1758 = (('Nothing Specified', {}, [mock.call(mock.ANY, '0.0.0.0', 8080, ssl=None, backlog=128)], []), ('Port Only', {'port': 8989, }, var4373, []), ('Multiple Hosts', {'host': ('127.0.0.1', '192.168.1.1'), }, var4357, []), ('Multiple Paths', {'path': ('/tmp/testsock1.sock', '/tmp/testsock2.sock'), }, [], var3078), ('Multiple Paths, Port', {'path': ('/tmp/testsock1.sock', '/tmp/testsock2.sock'), 'port': 8989, }, var4373, var3078), ('Multiple Paths, Single Host', {'path': ('/tmp/testsock1.sock', '/tmp/testsock2.sock'), 'host': '127.0.0.1', }, var89, var3078), ('Single Path, Single Host', {'path': '/tmp/testsock1.sock', 'host': '127.0.0.1', }, var89, var3420), ('Single Path, Multiple Hosts', {'path': '/tmp/testsock1.sock', 'host': ('127.0.0.1', '192.168.1.1'), }, var4357, var3420), ('Single Path, Port', {'path': '/tmp/testsock1.sock', 'port': 8989, }, var4373, var3420), ('Multiple Paths, Multiple Hosts, Port', {'path': ('/tmp/testsock1.sock', '/tmp/testsock2.sock'), 'host': ('127.0.0.1', '192.168.1.1'), 'port': 8000, }, [mock.call(mock.ANY, ('127.0.0.1', '192.168.1.1'), 8000, ssl=None, backlog=128)], var3078), ('Only socket', {'sock': [mock_socket], }, [mock.call(mock.ANY, ssl=None, sock=var3177, backlog=128)], []), ('Socket, port', {'sock': [mock_socket], 'port': 8765, }, [mock.call(mock.ANY, '0.0.0.0', 8765, ssl=None, backlog=128), mock.call(mock.ANY, sock=var3177, ssl=None, backlog=128)], []), ('Socket, Host, No port', {'sock': [mock_socket], 'host': 'localhost', }, [mock.call(mock.ANY, 'localhost', 8080, ssl=None, backlog=128), mock.call(mock.ANY, sock=var3177, ssl=None, backlog=128)], []))
var3606 = [var1959[0] for var1959 in var1758]
var1468 = [var1959[1:] for var1959 in var1758]

@pytest.mark.parametrize('run_app_kwargs, expected_server_calls, expected_unix_server_calls', var1468, ids=var3606)
def function1040(arg1185, arg742, arg1121, arg300):
    var3250 = arg1185.MagicMock()
    var3926 = arg1185.MagicMock()
    arg1185.patch('asyncio.gather')
    web.run_app(var3250, loop=var3926, print=(lambda *args: None), None=arg742)
    assert (var3926.create_unix_server.mock_calls == arg300)
    assert (var3926.create_server.mock_calls == arg1121)

def function1640(arg84, arg1449):
    function514(arg84)
    arg1449.spy(arg84, 'create_server')
    arg84.call_later(0.05, arg84.stop)
    var618 = web.Application()
    arg1449.spy(var618, 'startup')
    web.run_app(var618, loop=arg84, print=(lambda *args: None), access_log_format='%a')
    assert (not arg84.is_closed())
    var4503 = arg84.create_server
    var4503.assert_called_with(mock.ANY, '0.0.0.0', 8080, ssl=None, backlog=128)
    assert (var4503.call_args[0][0]._kwargs['access_log_format'] == '%a')
    var618.startup.assert_called_once_with()

def function2611(arg707, arg1145):
    function514(arg707)
    arg1145.spy(arg707, 'create_server')
    arg707.call_later(0.05, arg707.stop)
    var4689 = web.Application()
    arg1145.spy(var4689, 'startup')
    var4216 = ssl.create_default_context()
    web.run_app(var4689, loop=arg707, ssl_context=var4216, print=(lambda *args: None))
    assert (not arg707.is_closed())
    arg707.create_server.assert_called_with(mock.ANY, '0.0.0.0', 8443, ssl=var4216, backlog=128)
    var4689.startup.assert_called_once_with()

def function163(arg1694, arg1825, arg693):
    function514(arg1694)
    var2537 = arg1825()
    var1017 = 'localhost'
    arg693.spy(arg1694, 'create_server')
    arg1694.call_later(0.05, arg1694.stop)
    var3223 = web.Application()
    arg693.spy(var3223, 'startup')
    web.run_app(var3223, loop=arg1694, host=var1017, port=var2537, print=(lambda *args: None))
    assert (not arg1694.is_closed())
    arg1694.create_server.assert_called_with(mock.ANY, var1017, var2537, ssl=None, backlog=128)
    var3223.startup.assert_called_once_with()

def function12(arg1406, arg1335):
    function514(arg1406)
    arg1335.spy(arg1406, 'create_server')
    arg1406.call_later(0.05, arg1406.stop)
    var4456 = web.Application()
    arg1335.spy(var4456, 'startup')
    web.run_app(var4456, loop=arg1406, backlog=10, print=(lambda *args: None))
    assert (not arg1406.is_closed())
    arg1406.create_server.assert_called_with(mock.ANY, '0.0.0.0', 8080, ssl=None, backlog=10)
    var4456.startup.assert_called_once_with()

@skip_if_no_unix_socks
def function2220(arg640, arg663, arg2211):
    function514(arg640)
    arg663.spy(arg640, 'create_unix_server')
    arg640.call_later(0.05, arg640.stop)
    var840 = web.Application()
    arg663.spy(var840, 'startup')
    var1679 = str(arg2211.join('socket.sock'))
    var4394 = StringIO()
    web.run_app(var840, loop=arg640, path=var1679, print=var4394.write)
    assert (not arg640.is_closed())
    arg640.create_unix_server.assert_called_with(mock.ANY, var1679, ssl=None, backlog=128)
    var840.startup.assert_called_once_with()
    assert ('http://unix:{}:'.format(var1679) in var4394.getvalue())

@skip_if_no_unix_socks
def function1898(arg1508, arg1142, arg1251):
    function514(arg1508)
    arg1142.spy(arg1508, 'create_unix_server')
    arg1508.call_later(0.05, arg1508.stop)
    var3214 = web.Application()
    arg1142.spy(var3214, 'startup')
    var2178 = str(arg1251.join('socket.sock'))
    var2351 = StringIO()
    var388 = ssl.create_default_context()
    web.run_app(var3214, loop=arg1508, path=var2178, ssl_context=var388, print=var2351.write)
    assert (not arg1508.is_closed())
    arg1508.create_unix_server.assert_called_with(mock.ANY, var2178, ssl=var388, backlog=128)
    var3214.startup.assert_called_once_with()
    assert ('https://unix:{}:'.format(var2178) in var2351.getvalue())

@skip_if_no_unix_socks
def function1216(arg2304, arg1658, arg1416):
    'Older asyncio event loop implementations are known to halt server\n    creation when a socket path from a previous server bind still exists.\n    '
    function514(arg2304)
    arg2304.call_later(0.05, arg2304.stop)
    var3817 = web.Application()
    var3720 = arg1416.join('socket.sock')
    var1024 = str(var3720)
    web.run_app(var3817, loop=arg2304, path=var1024, print=(lambda *args: None))
    assert (not arg2304.is_closed())
    if var3720.check():
        with loop_context() as arg2304:
            arg1658.spy(arg2304, 'create_unix_server')
            arg2304.call_later(0.05, arg2304.stop)
            var3817 = web.Application()
            arg1658.spy(var3817, 'startup')
            arg1658.spy(os, 'remove')
            var2818 = StringIO()
            web.run_app(var3817, loop=arg2304, path=var1024, print=var2818.write)
            os.remove.assert_called_with(var1024)
            arg2304.create_unix_server.assert_called_with(mock.ANY, var1024, ssl=None, backlog=128)
            var3817.startup.assert_called_once_with()
            assert ('http://unix:{}:'.format(var3720) in var2818.getvalue())

@skip_if_no_unix_socks
@skip_if_no_abstract_paths
def function2519(arg66, arg1842):
    var4001 = (b'\x00' + uuid4().hex.encode('ascii'))
    arg66.call_later(0.05, arg66.stop)
    var1266 = web.Application()
    web.run_app(var1266, path=var4001.decode('ascii', 'ignore'), loop=arg66, print=(lambda *args: None))
    with loop_context() as arg66:
        arg1842.spy(arg66, 'create_unix_server')
        arg66.call_later(0.05, arg66.stop)
        var1266 = web.Application()
        arg1842.spy(var1266, 'startup')
        arg1842.spy(os, 'remove')
        var2309 = StringIO()
        web.run_app(var1266, path=var4001, print=var2309.write, loop=arg66)
        assert (mock.call([var4001]) not in os.remove.mock_calls)
        arg66.create_unix_server.assert_called_with(mock.ANY, var4001, ssl=None, backlog=128)
        var1266.startup.assert_called_once_with()

@skip_if_no_unix_socks
def function2460(arg33, arg1361, arg2175):
    var4726 = web.Application()
    var2526 = arg2175.join('socket.sock')
    var2526.ensure()
    var722 = str(var2526)
    arg1361.spy(os, 'remove')
    with pytest.raises(OSError):
        web.run_app(var4726, loop=arg33, path=var722, print=(lambda *args: None))
    assert (mock.call([var722]) not in os.remove.mock_calls)

def function1495(arg2252, arg865):
    function514(arg2252)
    arg865.spy(arg2252, 'create_server')
    arg2252.call_later(0.05, arg2252.stop)
    var4582 = web.Application()
    arg865.spy(var4582, 'startup')
    var772 = socket.socket()
    with contextlib.closing(var772):
        var772.bind(('0.0.0.0', 0))
        (var3280, var2582) = var772.getsockname()
        var4588 = StringIO()
        web.run_app(var4582, loop=arg2252, sock=var772, print=var4588.write)
        assert (not arg2252.is_closed())
        arg2252.create_server.assert_called_with(mock.ANY, sock=var772, backlog=128, ssl=None)
        var4582.startup.assert_called_once_with()
        assert ('http://0.0.0.0:{}'.format(var2582) in var4588.getvalue())

@skip_if_no_unix_socks
def function197(arg750, arg1410):
    function514(arg750)
    arg1410.spy(arg750, 'create_server')
    arg750.call_later(0.05, arg750.stop)
    var2929 = web.Application()
    arg1410.spy(var2929, 'startup')
    var2898 = '/tmp/test_preexisting_sock1'
    var4696 = socket.socket(socket.AF_UNIX)
    with contextlib.closing(var4696):
        var4696.bind(var2898)
        os.unlink(var2898)
        var1473 = StringIO()
        web.run_app(var2929, loop=arg750, sock=var4696, print=var1473.write)
        assert (not arg750.is_closed())
        arg750.create_server.assert_called_with(mock.ANY, sock=var4696, backlog=128, ssl=None)
        var2929.startup.assert_called_once_with()
        assert ('http://unix:{}:'.format(var2898) in var1473.getvalue())

def function1080(arg209, arg431):
    function514(arg209)
    arg431.spy(arg209, 'create_server')
    arg209.call_later(0.05, arg209.stop)
    var2823 = web.Application()
    arg431.spy(var2823, 'startup')
    var2925 = socket.socket()
    var555 = socket.socket()
    with contextlib.closing(var2925) , contextlib.closing(var555):
        var2925.bind(('0.0.0.0', 0))
        (var1555, var21) = var2925.getsockname()
        var555.bind(('0.0.0.0', 0))
        (var1555, var1550) = var555.getsockname()
        var3492 = StringIO()
        web.run_app(var2823, loop=arg209, sock=(var2925, var555), print=var3492.write)
        arg209.create_server.assert_has_calls([mock.call(mock.ANY, sock=var2925, backlog=128, ssl=None), mock.call(mock.ANY, sock=var555, backlog=128, ssl=None)])
        var2823.startup.assert_called_once_with()
        assert ('http://0.0.0.0:{}'.format(var21) in var3492.getvalue())
        assert ('http://0.0.0.0:{}'.format(var1550) in var3492.getvalue())
var1577 = '\nfrom aiohttp import web\n\napp = web.Application()\nweb.run_app(app, host=())\n'

def function814(arg1552, arg1535):
    function2198()
    var2667 = subprocess.Popen([sys.executable, '-u', '-c', var1577], stdout=subprocess.PIPE)
    for var2863 in var2667.stdout:
        if var2863.startswith(b'======== Running on'):
            break
    var2667.send_signal(signal.SIGINT)
    assert (var2667.wait() == 0)

def function2053(arg1113, arg535):
    function2198()
    var3228 = subprocess.Popen([sys.executable, '-u', '-c', var1577], stdout=subprocess.PIPE)
    for var1558 in var3228.stdout:
        if var1558.startswith(b'======== Running on'):
            break
    var3228.terminate()
    assert (var3228.wait() == 0)