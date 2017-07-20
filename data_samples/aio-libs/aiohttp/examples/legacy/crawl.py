import asyncio
import logging
import re
import signal
import sys
import urllib.parse
import aiohttp


class Class257:

    def __init__(self, arg273, arg202, arg1946=100):
        self.attribute1390 = arg273
        self.attribute232 = arg202
        self.attribute2317 = set()
        self.attribute1224 = set()
        self.attribute2124 = {}
        self.attribute2337 = set()
        self.attribute1488 = asyncio.Semaphore(arg1946, loop=arg202)
        self.attribute1279 = aiohttp.ClientSession(loop=arg202)

    @asyncio.coroutine
    def function2883(self):
        var2797 = asyncio.ensure_future(self.function1672([(self.attribute1390, '')]), loop=self.attribute232)
        yield from asyncio.sleep(1, loop=self.attribute232)
        while self.attribute1224:
            yield from asyncio.sleep(1, loop=self.attribute232)
        yield from t
        yield from self.attribute1279.close()
        self.attribute232.stop()

    @asyncio.coroutine
    def function1672(self, arg214):
        for (var3076, var1687) in arg214:
            var3076 = urllib.parse.urljoin(var1687, var3076)
            (var3076, var4257) = urllib.parse.urldefrag(var3076)
            if (var3076.startswith(self.attribute1390) and (var3076 not in self.attribute1224) and (var3076 not in self.attribute2124) and (var3076 not in self.attribute2317)):
                self.attribute2317.add(var3076)
                yield from self.attribute1488.acquire()
                var672 = asyncio.ensure_future(self.function2555(var3076), loop=self.attribute232)
                var672.add_done_callback((lambda arg952: self.attribute1488.release()))
                var672.add_done_callback(self.attribute2337.remove)
                self.attribute2337.add(var672)

    @asyncio.coroutine
    def function2555(self, arg2097):
        print('processing:', arg2097)
        self.attribute2317.remove(arg2097)
        self.attribute1224.add(arg2097)
        try:
            var3833 = yield from self.attribute1279.get(arg2097)
        except Exception as var2309:
            print('...', arg2097, 'has error', repr(str(var2309)))
            self.attribute2124[arg2097] = False
        else:
            if ((var3833.status == 200) and ('text/html' in var3833.headers.get('content-type'))):
                var2501 = yield from var3833.read().decode('utf-8', 'replace')
                var2985 = re.findall('(?i)href=["\\\']?([^\\s"\\\'<>]+)', var2501)
                asyncio.Task(self.function1672([(var979, arg2097) for var979 in var2985]))
            var3833.close()
            self.attribute2124[arg2097] = True
        self.attribute1224.remove(arg2097)
        print(len(self.attribute2124), 'completed tasks,', len(self.attribute2337), 'still pending, todo', len(self.attribute2317))

def function1266():
    var2900 = asyncio.get_event_loop()
    var759 = Class257(sys.argv[1], var2900)
    asyncio.ensure_future(var759.function2883(), loop=var2900)
    try:
        var2900.add_signal_handler(signal.SIGINT, var2900.stop)
    except RuntimeError:
        pass
    var2900.run_forever()
    print('todo:', len(var759.attribute2317))
    print('busy:', len(var759.attribute1224))
    print('done:', len(var759.attribute2124), '; ok:', sum(var759.attribute2124.values()))
    print('tasks:', len(var759.attribute2337))
if (__name__ == '__main__'):
    if ('--iocp' in sys.argv):
        from asyncio import events, windows_events
        sys.argv.remove('--iocp')
        logging.info('using iocp')
        var3995 = windows_events.ProactorEventLoop()
        events.set_event_loop(var3995)
    function1266()