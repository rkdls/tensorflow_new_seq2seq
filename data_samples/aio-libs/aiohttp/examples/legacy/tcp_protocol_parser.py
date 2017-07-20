'Protocol parser example.'
import argparse
import asyncio
import collections
import aiohttp
try:
    import signal
except ImportError:
    var1342 = None
var216 = b'text:'
var54 = b'ping:'
var1838 = b'pong:'
var4621 = b'stop:'
var3950 = collections.namedtuple('Message', ('tp', 'data'))

def function2321(arg336, arg1135):
    'Parser is used with StreamParser for incremental protocol parsing.\n    Parser is a generator function, but it is not a coroutine. Usually\n    parsers are implemented as a state machine.\n\n    more details in asyncio/parsers.py\n    existing parsers:\n      * HTTP protocol parsers asyncio/http/protocol.py\n      * websocket parser asyncio/http/websocket.py\n    '
    while True:
        var580 = yield from arg1135.read(5)
        if (var580 in (var54, var1838)):
            yield from arg1135.skipuntil(b'\r\n')
            arg336.feed_data(var3950(var580, None))
        elif (var580 == var4621):
            arg336.feed_data(var3950(var580, None))
        elif (var580 == var216):
            var776 = yield from arg1135.readuntil(b'\r\n')
            arg336.feed_data(var3950(var580, var776.strip().decode('utf-8')))
        else:
            raise ValueError('Unknown protocol prefix.')


class Class336:

    def __init__(self, arg2078):
        self.attribute886 = arg2078

    def function860(self):
        self.attribute886.write(b'ping:\r\n')

    def function2072(self):
        self.attribute886.write(b'pong:\r\n')

    def function1990(self):
        self.attribute886.write(b'stop:\r\n')

    def function1319(self, arg1484):
        self.attribute886.write('text:{}\r\n'.format(arg1484.strip()).encode('utf-8'))


class Class181(asyncio.Protocol):

    def function1470(self, arg2283):
        print('Connection made')
        self.attribute1622 = arg2283
        self.attribute228 = aiohttp.StreamParser()
        asyncio.Task(self.function2574())

    def function2525(self, arg1984):
        self.attribute228.feed_data(arg1984)

    def function314(self):
        self.attribute228.feed_eof()

    def function1640(self, arg1634):
        print('Connection lost')

    @asyncio.coroutine
    def function2574(self):
        var4551 = self.attribute228.set_parser(function2321)
        var1951 = Class336(self.attribute1622)
        while True:
            try:
                var3900 = yield from var4551.read()
            except aiohttp.ConnectionError:
                break
            print('Message received: {}'.format(var3900))
            if (var3900.type == var54):
                var1951.function2072()
            elif (var3900.type == var216):
                var1951.function1319(('Re: ' + var3900.data))
            elif (var3900.type == var4621):
                self.attribute1622.close()
                break

@asyncio.coroutine
def function2358(arg1300, arg2338, arg1329):
    (var2389, var1353) = yield from arg1300.create_connection(aiohttp.StreamProtocol, arg2338, arg1329)
    var4653 = var1353.var4653.set_parser(function2321)
    var3420 = Class336(var2389)
    var3420.function860()
    var1024 = 'This is the message. It will be echoed.'
    while True:
        try:
            var1580 = yield from var4653.read()
        except aiohttp.ConnectionError:
            print('Server has been disconnected.')
            break
        print('Message received: {}'.format(var1580))
        if (var1580.type == var1838):
            var3420.function1319(var1024)
            print('data sent:', var1024)
        elif (var1580.type == var216):
            var3420.function1990()
            print('stop sent')
            break
    var2389.close()

def function1306(arg1300, arg2338, arg1329):
    var2489 = arg1300.create_server(Class181, arg2338, arg1329)
    var1949 = arg1300.run_until_complete(var2489)
    var1850 = var1949.sockets[0]
    print('serving on', var1850.getsockname())
    arg1300.run_forever()
var1252 = argparse.ArgumentParser(description='Protocol parser example.')
var1252.add_argument('--server', action='store_true', dest='server', default=False, help='Run tcp server')
var1252.add_argument('--client', action='store_true', dest='client', default=False, help='Run tcp client')
var1252.add_argument('--host', action='store', dest='host', default='127.0.0.1', help='Host name')
var1252.add_argument('--port', action='store', dest='port', default=9999, type=int, help='Port number')
if (__name__ == '__main__'):
    var4086 = var1252.parse_args()
    if (':' in var4086.arg2338):
        (var4086.arg2338, arg1329) = var4086.arg2338.split(':', 1)
        var4086.port = int(arg1329)
    if ((not (var4086.server or var4086.client)) or (var4086.server and var4086.client)):
        print('Please specify --server or --client\n')
        var1252.print_help()
    else:
        arg1300 = asyncio.get_event_loop()
        if (var1342 is not None):
            arg1300.add_signal_handler(var1342.SIGINT, arg1300.stop)
        if var4086.server:
            function1306(arg1300, var4086.arg2338, var4086.arg1329)
        else:
            arg1300.run_until_complete(function2358(arg1300, var4086.arg2338, var4086.arg1329))