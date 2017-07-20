import asyncio
import aiohttp

def function2505(arg2110, arg533, arg2385):
    var1538 = yield from aiohttp.ws_connect((arg533 + '/getCaseCount'))
    var2751 = int(yield from var1538.receive().data)
    print(('running %d cases' % var2751))
    yield from var1538.close()
    for var3246 in range(1, (var2751 + 1)):
        print('running test case:', var3246)
        var3727 = (arg533 + ('/runCase?case=%d&agent=%s' % (var3246, arg2385)))
        var1538 = yield from aiohttp.ws_connect(var3727)
        while True:
            var3651 = yield from var1538.receive()
            if (var3651.type == aiohttp.WSMsgType.text):
                yield from var1538.send_str(var3651.data)
            elif (var3651.type == aiohttp.WSMsgType.binary):
                yield from var1538.send_bytes(var3651.data)
            elif (var3651.type == aiohttp.WSMsgType.close):
                yield from var1538.close()
                break
            else:
                break
    arg533 = (arg533 + ('/updateReports?agent=%s' % arg2385))
    var1538 = yield from aiohttp.ws_connect(arg533)
    yield from var1538.close()

def function1218(arg2042, arg130, arg68):
    try:
        yield from function2505(arg2042, arg130, arg68)
    except:
        import traceback
        traceback.print_exc()
if (__name__ == '__main__'):
    arg2042 = asyncio.get_event_loop()
    try:
        arg2042.run_until_complete(function1218(arg2042, 'http://localhost:9001', 'aiohttp'))
    except KeyboardInterrupt:
        pass
    finally:
        arg2042.close()