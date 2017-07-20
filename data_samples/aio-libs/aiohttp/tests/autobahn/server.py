import asyncio
import logging
from aiohttp import web

@asyncio.coroutine
def function2571(arg119):
    var3601 = web.WebSocketResponse(autoclose=False)
    (var1544, var1511) = var3601.can_start(arg119)
    if (not var1544):
        return web.HTTPBadRequest()
    yield from var3601.prepare(arg119)
    while True:
        var188 = yield from var3601.receive()
        if (var188.type == web.WSMsgType.text):
            var3601.send_str(var188.data)
        elif (var188.type == web.WSMsgType.binary):
            var3601.send_bytes(var188.data)
        elif (var188.type == web.WSMsgType.close):
            yield from var3601.close()
            break
        else:
            break
    return var3601

@asyncio.coroutine
def function1191(arg1043):
    var4513 = web.Application()
    var4513.router.add_route('GET', '/', function2571)
    var927 = var4513.make_handler()
    var700 = yield from arg1043.create_server(var927, '127.0.0.1', 9001)
    print('Server started at http://127.0.0.1:9001')
    return (var4513, var700, var927)

@asyncio.coroutine
def function663(arg1578, arg1648, arg472):
    arg1648.close()
    yield from arg472.finish_connections()
    yield from arg1648.wait_closed()
if (__name__ == '__main__'):
    var3709 = asyncio.get_event_loop()
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
    var3709 = asyncio.get_event_loop()
    (var4328, var775, var1082) = var3709.run_until_complete(function1191(var3709))
    try:
        var3709.run_forever()
    except KeyboardInterrupt:
        var3709.run_until_complete(function663(var4328, var775, var1082))