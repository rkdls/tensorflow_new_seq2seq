import asyncio
from itertools import count
from aiohttp.helpers import FrozenList, isfuture


class Class214(FrozenList):
    var4339 = ()

    @asyncio.coroutine
    def function1621(self, *args, **kwargs):
        for var1935 in self._items:
            var3199 = var1935(*args, None=kwargs)
            if (asyncio.iscoroutine(var3199) or isfuture(var3199)):
                yield from res


class Class268(Class214):
    'Coroutine-based signal implementation.\n\n    To connect a callback to a signal, use any list method.\n\n    Signals are fired using the :meth:`send` coroutine, which takes named\n    arguments.\n    '
    var1766 = ('_app', '_name', '_pre', '_post')

    def __init__(self, arg999):
        super().__init__()
        self.attribute1316 = arg999
        var3924 = self.__class__
        self.attribute132 = ((var3924.__module__ + ':') + var3924.__qualname__)
        self.attribute2355 = arg999.on_pre_signal
        self.attribute1326 = arg999.on_post_signal

    @asyncio.coroutine
    def function356(self, *args, **kwargs):
        '\n        Sends data to all registered receivers.\n        '
        if self._items:
            var1073 = None
            var91 = self.attribute1316._debug
            if var91:
                var1073 = self.attribute2355.var1073()
                yield from self.attribute2355.function356(var1073, self.attribute132, *args, None=kwargs)
            yield from self.function1621(*args, None=kwargs)
            if var91:
                yield from self.attribute1326.function356(var1073, self.attribute132, *args, None=kwargs)


class Class330(Class214):
    'Callback-based signal implementation.\n\n    To connect a callback to a signal, use any list method.\n\n    Signals are fired using the :meth:`send` method, which takes named\n    arguments.\n    '
    var2056 = ()

    def function1859(self, *args, **kwargs):
        '\n        Sends data to all registered receivers.\n        '
        for var1039 in self._items:
            var1039(*args, None=kwargs)


class Class126(Class214):
    var4464 = ()

    @asyncio.coroutine
    def function77(self, arg1380, arg2039, *args, **kwargs):
        yield from self._send(arg1380, arg2039, *args, None=kwargs)


class Class411(Class126):
    var1979 = ('_counter',)

    def __init__(self):
        super().__init__()
        self.attribute146 = count(1)

    def function618(self):
        return next(self.attribute146)


class Class263(Class126):
    var2313 = ()