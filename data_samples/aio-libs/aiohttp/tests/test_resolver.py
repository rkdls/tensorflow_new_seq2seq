import asyncio
import ipaddress
import socket
from unittest.mock import Mock, patch
import pytest
from aiohttp.resolver import AsyncResolver, DefaultResolver, ThreadedResolver
try:
    import aiodns
    var2612 = hasattr(aiodns.DNSResolver, 'gethostbyname')
except ImportError:
    var4634 = None
    var2612 = False


class Class129:

    def __init__(self, arg1221):
        self.attribute525 = arg1221


class Class168:

    def __init__(self, arg1772):
        self.attribute82 = arg1772

@asyncio.coroutine
def function2494(arg430):
    return Class129(addresses=tuple(arg430))

@asyncio.coroutine
def function903(arg596):
    return [Class168(host=var679) for var679 in arg596]

def function1518(arg2374):

    @asyncio.coroutine
    def function1120(*args, **kwargs):
        if (not arg2374):
            raise socket.gaierror
        return list([(None, None, None, None, [var3614, 0]) for var3614 in arg2374])
    return function1120

@pytest.mark.skipif((not var2612), reason='aiodns 1.1 required')
@asyncio.coroutine
def function2629(arg457):
    with patch('aiodns.DNSResolver') as var1179:
        var1179().var2612.return_value = function2494(['127.0.0.1'])
        var4035 = AsyncResolver(loop=arg457)
        var918 = yield from var4035.resolve('www.python.org')
        ipaddress.ip_address(var918[0]['host'])
        var1179().var2612.assert_called_with('www.python.org', socket.AF_INET)

@pytest.mark.skipif((var4634 is None), reason='aiodns required')
@asyncio.coroutine
def function2470(arg1399):
    with patch('aiodns.DNSResolver') as var1266:
        del var1266().gethostbyname
        var1266().query.return_value = function903(['127.0.0.1'])
        var4374 = AsyncResolver(loop=arg1399)
        var573 = yield from var4374.resolve('www.python.org')
        ipaddress.ip_address(var573[0]['host'])
        var1266().query.assert_called_with('www.python.org', 'A')

@pytest.mark.skipif((not var2612), reason='aiodns 1.1 required')
@asyncio.coroutine
def function2013(arg1248):
    with patch('aiodns.DNSResolver') as var4503:
        var389 = ['127.0.0.1', '127.0.0.2', '127.0.0.3', '127.0.0.4']
        var4503().var2612.return_value = function2494(var389)
        var725 = AsyncResolver(loop=arg1248)
        var4020 = yield from var725.resolve('www.google.com')
        var389 = [ipaddress.ip_address(var4312['host']) for var4312 in var4020]
        assert (len(var389) > 3), 'Expecting multiple addresses'

@pytest.mark.skipif((var4634 is None), reason='aiodns required')
@asyncio.coroutine
def function19(arg2037):
    with patch('aiodns.DNSResolver') as var4453:
        del var4453().gethostbyname
        var1402 = ['127.0.0.1', '127.0.0.2', '127.0.0.3', '127.0.0.4']
        var4453().query.return_value = function903(var1402)
        var752 = AsyncResolver(loop=arg2037)
        var4214 = yield from var752.resolve('www.google.com')
        var1402 = [ipaddress.ip_address(var177['host']) for var177 in var4214]

@pytest.mark.skipif((not var2612), reason='aiodns 1.1 required')
@asyncio.coroutine
def function2595(arg483):
    with patch('aiodns.DNSResolver') as var3150:
        var3150().var2612.side_effect = var4634.error.DNSError()
        var3357 = AsyncResolver(loop=arg483)
        with pytest.raises(var4634.error.DNSError):
            yield from var3357.resolve('doesnotexist.bla')

@pytest.mark.skipif((var4634 is None), reason='aiodns required')
@asyncio.coroutine
def function583(arg1707):
    with patch('aiodns.DNSResolver') as var167:
        del var167().gethostbyname
        var167().query.side_effect = var4634.error.DNSError()
        var4596 = AsyncResolver(loop=arg1707)
        with pytest.raises(var4634.error.DNSError):
            yield from var4596.resolve('doesnotexist.bla')

@asyncio.coroutine
def function1893():
    var3559 = Mock()
    var3559.getaddrinfo = function1518(['127.0.0.1'])
    var3401 = ThreadedResolver(loop=var3559)
    var3891 = yield from var3401.resolve('www.python.org')
    ipaddress.ip_address(var3891[0]['host'])

@asyncio.coroutine
def function2200():
    var4211 = Mock()
    var1632 = ['127.0.0.1', '127.0.0.2', '127.0.0.3', '127.0.0.4']
    var4211.getaddrinfo = function1518(var1632)
    var4037 = ThreadedResolver(loop=var4211)
    var911 = yield from var4037.resolve('www.google.com')
    var1632 = [ipaddress.ip_address(var1531['host']) for var1531 in var911]
    assert (len(var1632) > 3), 'Expecting multiple addresses'

@asyncio.coroutine
def function1287():
    var1031 = Mock()
    var2205 = []
    var1031.getaddrinfo = function1518(var2205)
    var2284 = ThreadedResolver(loop=var1031)
    with pytest.raises(socket.gaierror):
        yield from var2284.resolve('doesnotexist.bla')

@asyncio.coroutine
def function2896(arg1805):
    var4423 = ThreadedResolver(loop=arg1805)
    yield from var4423.close()

@pytest.mark.skipif((var4634 is None), reason='aiodns required')
@asyncio.coroutine
def function2308(arg557):
    var3841 = AsyncResolver(loop=arg557)
    yield from var3841.close()

def function1250(arg1517):
    asyncio.set_event_loop(arg1517)
    var3254 = ThreadedResolver()
    assert (var3254._loop is arg1517)

@pytest.mark.skipif((var4634 is None), reason='aiodns required')
def function2336(arg844):
    asyncio.set_event_loop(arg844)
    var3683 = AsyncResolver()
    assert (var3683._loop is arg844)

@pytest.mark.skipif((not var2612), reason='aiodns 1.1 required')
@asyncio.coroutine
def function497(arg1205):
    with patch('aiodns.DNSResolver') as var441:
        var441().var2612.return_value = function2494(['::1'])
        var1084 = AsyncResolver(loop=arg1205)
        var3908 = yield from var1084.resolve('www.python.org', family=socket.AF_INET6)
        ipaddress.ip_address(var3908[0]['host'])
        var441().var2612.assert_called_with('www.python.org', socket.AF_INET6)

@pytest.mark.skipif((var4634 is None), reason='aiodns required')
@asyncio.coroutine
def function298(arg2184):
    with patch('aiodns.DNSResolver') as var168:
        del var168().gethostbyname
        var168().query.return_value = function903(['::1'])
        var4169 = AsyncResolver(loop=arg2184)
        var4092 = yield from var4169.resolve('www.python.org', family=socket.AF_INET6)
        ipaddress.ip_address(var4092[0]['host'])
        var168().query.assert_called_with('www.python.org', 'AAAA')

def function1590(arg642, arg2322):
    arg2322.setattr('aiohttp.resolver.aiodns', None)
    with pytest.raises(RuntimeError):
        AsyncResolver(loop=arg642)

def function261():
    assert (DefaultResolver is ThreadedResolver)