'Low level HTTP server.'
import asyncio
from .helpers import TimeService
from .web_protocol import RequestHandler
from .web_request import BaseRequest
var949 = ('Server',)


class Class439:

    def __init__(self, arg524, **kwargs, *, request_factory=None, loop=None):
        if (var3539 is None):
            var3539 = asyncio.get_event_loop()
        self.attribute2022 = var3539
        self.attribute2145 = {}
        self.attribute2137 = kwargs
        self.attribute115 = TimeService(self.attribute2022)
        self.attribute560 = 0
        self.attribute1301 = arg524
        self.attribute1038 = (request_factory or self.function1216)

    @property
    def function2847(self):
        return list(self.attribute2145.keys())

    def function331(self, arg2169, arg1695):
        self.attribute2145[arg2169] = arg1695

    def function2864(self, arg1069, arg1607=None):
        if (arg1069 in self.attribute2145):
            del self.attribute2145[arg1069]

    def function1216(self, arg37, arg1419, arg1812, arg1792, arg904):
        return BaseRequest(arg37, arg1419, arg1812, arg1792, arg1812.time_service, arg904)

    @asyncio.coroutine
    def function268(self, arg1710=None):
        var794 = [var578.function268(arg1710) for var578 in self.attribute2145]
        yield from asyncio.gather(*var794, loop=self.attribute2022)
        self.attribute2145.clear()
        self.attribute115.close()
    var1064 = function268

    def __call__(self):
        return RequestHandler(self, loop=self.attribute2022, None=self.attribute2137)