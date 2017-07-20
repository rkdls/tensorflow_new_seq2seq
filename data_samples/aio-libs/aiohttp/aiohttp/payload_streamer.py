" Payload implemenation for coroutines as data provider.\n\nAs a simple case, you can upload data from file::\n\n   @aiohttp.streamer\n   def file_sender(writer, file_name=None):\n      with open(file_name, 'rb') as f:\n          chunk = f.read(2**16)\n          while chunk:\n              yield from writer.write(chunk)\n\n              chunk = f.read(2**16)\n\nThen you can use `file_sender` like this:\n\n    async with session.post('http://httpbin.org/post',\n                            data=file_sender(file_name='huge_file')) as resp:\n        print(await resp.text())\n\n..note:: Coroutine must accept `writer` as first argument\n\n"
import asyncio
from .payload import Payload, payload_type
var1000 = ('streamer',)


class Class24:

    def __init__(self, arg1311, arg2397, arg1350):
        self.attribute975 = asyncio.coroutine(arg1311)
        self.attribute2173 = arg2397
        self.attribute1217 = arg1350

    @asyncio.coroutine
    def __call__(self, arg0):
        yield from self.attribute975(arg0, *self.attribute2173, None=self.attribute1217)


class Class101:

    def __init__(self, arg1509):
        self.attribute1380 = arg1509

    def __call__(self, *args, **kwargs):
        return Class24(self.attribute1380, args, kwargs)


@payload_type(Class24)
class Class127(Payload):

    @asyncio.coroutine
    def function941(self, arg1795):
        yield from self._value(arg1795)


@payload_type(Class101)
class Class16(Class127):

    def __init__(self, arg2235, *args, **kwargs):
        super().__init__(arg2235(), *args, None=kwargs)

    @asyncio.coroutine
    def function1921(self, arg1197):
        yield from self._value(arg1197)