import asyncio
import socket
from .abc import AbstractResolver
var402 = ('ThreadedResolver', 'AsyncResolver', 'DefaultResolver')
try:
    import aiodns
except ImportError:
    var2746 = None
var3703 = False


class Class125(AbstractResolver):
    'Use Executor for synchronous getaddrinfo() calls, which defaults to\n    concurrent.futures.ThreadPoolExecutor.\n    '

    def __init__(self, arg1572=None):
        if (arg1572 is None):
            arg1572 = asyncio.get_event_loop()
        self.attribute2353 = arg1572

    @asyncio.coroutine
    def function740(self, arg274, arg469=0, arg85=socket.AF_INET):
        var4486 = yield from self.attribute2353.getaddrinfo(arg274, arg469, type=socket.SOCK_STREAM, family=arg85)
        var3233 = []
        for (arg85, var3567, var2751, var3567, var735) in var4486:
            var3233.append({'hostname': host, 'host': var735[0], 'port': var735[1], 'family': family, 'proto': proto, 'flags': socket.AI_NUMERICHOST, })
        return var3233

    @asyncio.coroutine
    def function1217(self):
        pass


class Class17(AbstractResolver):
    'Use the `aiodns` package to make asynchronous DNS lookups'

    def __init__(self, arg1136=None, *args, **kwargs):
        if (arg1136 is None):
            arg1136 = asyncio.get_event_loop()
        if (var2746 is None):
            raise RuntimeError('Resolver requires aiodns library')
        self.attribute579 = arg1136
        self.attribute1418 = var2746.DNSResolver(*args, loop=arg1136, None=kwargs)
        if (not hasattr(self.attribute1418, 'gethostbyname')):
            self.attribute598 = self.function1321

    @asyncio.coroutine
    def function2466(self, arg177, arg150=0, arg410=socket.AF_INET):
        var4663 = []
        var859 = yield from self.attribute1418.gethostbyname(arg177, arg410)
        for var1502 in var859.addresses:
            var4663.append({'hostname': host, 'host': address, 'port': port, 'family': family, 'proto': 0, 'flags': socket.AI_NUMERICHOST, })
        return var4663

    @asyncio.coroutine
    def function1321(self, arg1817, arg780=0, arg785=socket.AF_INET):
        if (arg785 == socket.AF_INET6):
            var1561 = 'AAAA'
        else:
            var1561 = 'A'
        var2374 = []
        var2390 = yield from self.attribute1418.query(arg1817, var1561)
        for var309 in var2390:
            var2374.append({'hostname': host, 'host': var309.host, 'port': port, 'family': family, 'proto': 0, 'flags': socket.AI_NUMERICHOST, })
        return var2374

    @asyncio.coroutine
    def function149(self):
        return self.attribute1418.cancel()
var2730 = (Class17 if var3703 else Class125)