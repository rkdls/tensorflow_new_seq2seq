'websocket cmd client for wssrv.py example.'
import argparse
import asyncio
import signal
import sys
import aiohttp
try:
    import selectors
except ImportError:
    from asyncio import selectors

def function2101(arg2261, arg1955):
    var641 = input('Please enter your name: ')
    var4170 = yield from aiohttp.ws_connect(arg1955, autoclose=False, autoping=False)

    def function809():
        var2615 = sys.stdin.buffer.readline().decode('utf-8')
        if (not var2615):
            arg2261.stop()
        else:
            var4170.send_str(((var641 + ': ') + var2615))
    arg2261.add_reader(sys.stdin.fileno(), function809)

    @asyncio.coroutine
    def function2515():
        while True:
            var355 = yield from var4170.receive()
            if (var355.type == aiohttp.WSMsgType.TEXT):
                print('Text: ', var355.data.strip())
            elif (var355.type == aiohttp.WSMsgType.BINARY):
                print('Binary: ', var355.data)
            elif (var355.type == aiohttp.WSMsgType.PING):
                var4170.pong()
            elif (var355.type == aiohttp.WSMsgType.PONG):
                print('Pong received')
            else:
                if (var355.type == aiohttp.WSMsgType.CLOSE):
                    yield from var4170.close()
                elif (var355.type == aiohttp.WSMsgType.ERROR):
                    print(('Error during receive %s' % var4170.exception()))
                elif (var355.type == aiohttp.WSMsgType.CLOSED):
                    pass
                break
    yield from function2515()
var3322 = argparse.ArgumentParser(description='websocket console client for wssrv.py example.')
var3322.add_argument('--host', action='store', dest='host', default='127.0.0.1', help='Host name')
var3322.add_argument('--port', action='store', dest='port', default=8080, type=int, help='Port number')
if (__name__ == '__main__'):
    var2601 = var3322.parse_args()
    if (':' in var2601.host):
        (var2601.host, var461) = var2601.host.split(':', 1)
        var2601.port = int(var461)
    var2042 = 'http://{}:{}'.format(var2601.host, var2601.var461)
    var3984 = asyncio.SelectorEventLoop(selectors.SelectSelector())
    asyncio.set_event_loop(var3984)
    var3984.add_signal_handler(signal.SIGINT, var3984.stop)
    asyncio.Task(function2101(var3984, var2042))
    var3984.run_forever()