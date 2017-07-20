import socket
from unittest import mock
import pytest
from aiohttp.http_writer import CORK, PayloadWriter, StreamWriter
var1274 = socket.var1274
if var1274:
    try:
        socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    except OSError:
        var1274 = False

def function476(arg1207):
    var2460 = mock.Mock()
    var3648 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    var2460.get_extra_info.return_value = var3648
    var1556 = mock.Mock()
    var2691 = StreamWriter(var1556, var2460, arg1207)
    assert (not var2691.tcp_nodelay)
    assert (not var2691.tcp_cork)
    assert (not var3648.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY))

def function2650(arg1784):
    var967 = mock.Mock()
    var940 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    var967.get_extra_info.return_value = var940
    var436 = mock.Mock()
    var208 = StreamWriter(var436, var967, arg1784)
    var208.set_tcp_nodelay(False)
    assert (not var208.tcp_nodelay)
    assert (not var940.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY))

def function1001(arg89):
    var1487 = mock.Mock()
    var177 = mock.Mock()
    var177.setsockopt = mock.Mock()
    var177.family = socket.AF_INET
    var177.setsockopt.side_effect = OSError
    var1487.get_extra_info.return_value = var177
    var3624 = mock.Mock()
    var1925 = StreamWriter(var3624, var1487, arg89)
    var1925.set_tcp_nodelay(True)
    assert (not var1925.tcp_nodelay)

def function2497(arg1962):
    var4584 = mock.Mock()
    var4240 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    var4584.get_extra_info.return_value = var4240
    var4191 = mock.Mock()
    var3344 = StreamWriter(var4191, var4584, arg1962)
    var3344.set_tcp_nodelay(True)
    assert var3344.tcp_nodelay
    assert var4240.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY)

def function2211(arg1993):
    var3972 = mock.Mock()
    var1038 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    var3972.get_extra_info.return_value = var1038
    var2675 = mock.Mock()
    var2733 = StreamWriter(var2675, var3972, arg1993)
    var2733.set_tcp_nodelay(True)
    var2733.set_tcp_nodelay(False)
    assert (not var2733.tcp_nodelay)
    assert (not var1038.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY))

@pytest.mark.skipif((CORK is None), reason='TCP_CORK or TCP_NOPUSH required')
def function517(arg1847):
    var664 = mock.Mock()
    var488 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    var664.get_extra_info.return_value = var488
    var1265 = mock.Mock()
    var4339 = StreamWriter(var1265, var664, arg1847)
    var4339.set_tcp_cork(True)
    var4339.set_tcp_nodelay(True)
    assert var4339.tcp_nodelay
    assert (not var4339.tcp_cork)
    assert var488.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY)

@pytest.mark.skipif((not var1274), reason='IPv6 is not available')
def function556(arg1892):
    var91 = mock.Mock()
    var4496 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    var91.get_extra_info.return_value = var4496
    var3923 = mock.Mock()
    var4325 = StreamWriter(var3923, var91, arg1892)
    var4325.set_tcp_nodelay(True)
    assert var4325.tcp_nodelay
    assert var4496.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY)

@pytest.mark.skipif((not hasattr(socket, 'AF_UNIX')), reason='requires unix sockets')
def function1205(arg514):
    var4402 = mock.Mock()
    var2806 = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    var4402.get_extra_info.return_value = var2806
    var1160 = mock.Mock()
    var1164 = StreamWriter(var1160, var4402, arg514)
    var1164.set_tcp_nodelay(True)
    assert (not var1164.tcp_nodelay)

def function740(arg402):
    var4352 = mock.Mock()
    var4352.get_extra_info.return_value = None
    var705 = mock.Mock()
    var586 = StreamWriter(var705, var4352, arg402)
    var586.set_tcp_nodelay(True)
    assert (not var586.tcp_nodelay)
    assert (var586._socket is None)

@pytest.mark.skipif((CORK is None), reason='TCP_CORK or TCP_NOPUSH required')
def function416(arg389):
    var3115 = mock.Mock()
    var2954 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    var3115.get_extra_info.return_value = var2954
    var199 = mock.Mock()
    var4663 = StreamWriter(var199, var3115, arg389)
    assert (not var4663.tcp_cork)
    assert (not var2954.getsockopt(socket.IPPROTO_TCP, CORK))

@pytest.mark.skipif((CORK is None), reason='TCP_CORK or TCP_NOPUSH required')
def function1758(arg1183):
    var1257 = mock.Mock()
    var3827 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    var1257.get_extra_info.return_value = var3827
    var3905 = mock.Mock()
    var970 = StreamWriter(var3905, var1257, arg1183)
    var970.set_tcp_cork(False)
    assert (not var970.tcp_cork)
    assert (not var3827.getsockopt(socket.IPPROTO_TCP, CORK))

@pytest.mark.skipif((CORK is None), reason='TCP_CORK or TCP_NOPUSH required')
def function33(arg1379):
    var4302 = mock.Mock()
    var204 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    var4302.get_extra_info.return_value = var204
    var920 = mock.Mock()
    var1760 = StreamWriter(var920, var4302, arg1379)
    var1760.set_tcp_cork(True)
    assert var1760.tcp_cork
    assert var204.getsockopt(socket.IPPROTO_TCP, CORK)

@pytest.mark.skipif((CORK is None), reason='TCP_CORK or TCP_NOPUSH required')
def function108(arg1505):
    var3536 = mock.Mock()
    var3786 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    var3536.get_extra_info.return_value = var3786
    var2439 = mock.Mock()
    var3885 = StreamWriter(var2439, var3536, arg1505)
    var3885.set_tcp_cork(True)
    var3885.set_tcp_cork(False)
    assert (not var3885.tcp_cork)
    assert (not var3786.getsockopt(socket.IPPROTO_TCP, CORK))

@pytest.mark.skipif((not var1274), reason='IPv6 is not available')
@pytest.mark.skipif((CORK is None), reason='TCP_CORK or TCP_NOPUSH required')
def function72(arg2013):
    var3623 = mock.Mock()
    var3108 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    var3623.get_extra_info.return_value = var3108
    var4421 = mock.Mock()
    var2701 = StreamWriter(var4421, var3623, arg2013)
    var2701.set_tcp_cork(True)
    assert var2701.tcp_cork
    assert var3108.getsockopt(socket.IPPROTO_TCP, CORK)

@pytest.mark.skipif((not hasattr(socket, 'AF_UNIX')), reason='requires unix sockets')
@pytest.mark.skipif((CORK is None), reason='TCP_CORK or TCP_NOPUSH required')
def function512(arg348):
    var543 = mock.Mock()
    var4405 = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    var543.get_extra_info.return_value = var4405
    var2766 = mock.Mock()
    var3991 = StreamWriter(var2766, var543, arg348)
    var3991.set_tcp_cork(True)
    assert (not var3991.tcp_cork)

@pytest.mark.skipif((CORK is None), reason='TCP_CORK or TCP_NOPUSH required')
def function1322(arg1333):
    var541 = mock.Mock()
    var541.get_extra_info.return_value = None
    var2065 = mock.Mock()
    var250 = StreamWriter(var2065, var541, arg1333)
    var250.set_tcp_cork(True)
    assert (not var250.tcp_cork)
    assert (var250._socket is None)

def function2800(arg1864):
    var833 = mock.Mock()
    var3422 = mock.Mock()
    var3422.setsockopt = mock.Mock()
    var3422.family = socket.AF_INET
    var3422.setsockopt.side_effect = OSError
    var2775 = mock.Mock()
    var1102 = StreamWriter(var2775, var833, arg1864)
    var1102.set_tcp_cork(True)
    assert (not var1102.tcp_cork)

@pytest.mark.skipif((CORK is None), reason='TCP_CORK or TCP_NOPUSH required')
def function1821(arg1884):
    var2263 = mock.Mock()
    var2090 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    var2263.get_extra_info.return_value = var2090
    var2736 = mock.Mock()
    var1583 = StreamWriter(var2736, var2263, arg1884)
    var1583.set_tcp_nodelay(True)
    var1583.set_tcp_cork(True)
    assert (not var1583.tcp_nodelay)
    assert (not var2090.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY))
    assert var1583.tcp_cork
    assert var2090.getsockopt(socket.IPPROTO_TCP, CORK)

@pytest.mark.skipif((CORK is None), reason='TCP_CORK or TCP_NOPUSH required')
def function1198(arg1210):
    var1614 = mock.Mock()
    var1317 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    var1614.get_extra_info.return_value = var1317
    var1172 = mock.Mock()
    var2047 = StreamWriter(var1172, var1614, arg1210)
    var2047.set_tcp_cork(True)
    var2047.set_tcp_nodelay(True)
    assert var2047.tcp_nodelay
    assert var1317.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY)
    assert (not var2047.tcp_cork)
    assert (not var1317.getsockopt(socket.IPPROTO_TCP, CORK))

def function1364(arg181):
    var3656 = mock.Mock()
    var2000 = StreamWriter(mock.Mock(), var3656, arg181)
    assert var2000.available
    var2417 = PayloadWriter(var2000, arg181)
    assert (not var2000.available)
    assert (var2417._transport is var3656)
    var4677 = PayloadWriter(var2000, arg181)
    assert (var4677._transport is None)
    assert (var4677 in var2000._waiters)

def function522(arg325):
    var1425 = mock.Mock()
    var383 = StreamWriter(mock.Mock(), var1425, arg325)
    var1622 = PayloadWriter(var383, arg325)
    var383.release()
    assert var383.available
    var383.acquire(var1622)
    assert (not var383.available)
    assert (var1622._transport is var1425)

def function2667(arg185):
    var223 = mock.Mock()
    var1979 = StreamWriter(mock.Mock(), var223, arg185)
    var1979.available = False
    var4719 = mock.Mock()
    var1979.acquire(var4719)
    assert (not var1979.available)
    assert (not var4719.set_transport.called)
    var1979.release()
    assert (not var1979.available)
    var4719.set_transport.assert_called_with(var223)
    var1979.release()
    assert var1979.available

def function2166(arg634):
    var2824 = mock.Mock()
    var4275 = StreamWriter(mock.Mock(), var2824, arg634)
    var4275.available = False
    var4137 = PayloadWriter(var4275, arg634)
    assert (var4137._transport is None)
    assert (var4137 in var4275._waiters)
    var1377 = var4275.replace(var4137, PayloadWriter)
    assert (var1377._transport is None)
    assert (var1377 in var4275._waiters)
    assert (var4137 not in var4275._waiters)
    var4275.release()
    assert (var1377._transport is var2824)
    assert (not var4275._waiters)

def function1442(arg46):
    var266 = mock.Mock()
    var133 = StreamWriter(mock.Mock(), var266, arg46)
    var2133 = PayloadWriter(var133, arg46, False)
    var2805 = var133.replace(var2133, PayloadWriter)
    assert (var2805._transport is var266)
    assert (var2805 not in var133._waiters)