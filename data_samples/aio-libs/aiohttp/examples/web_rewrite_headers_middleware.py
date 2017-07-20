'\nExample for rewriting response headers by middleware.\n'
import asyncio
from aiohttp.web import Application, HTTPException, Response, run_app

@asyncio.coroutine
def function2374(arg2154):
    return Response(text='Everything is fine')

@asyncio.coroutine
def function1391(arg240, arg2010):

    @asyncio.coroutine
    def function1083(arg1429):
        try:
            var2561 = yield from arg2010(arg1429)
        except HTTPException as var2456:
            var2561 = var2456
        if (not var2561.prepared):
            var2561.headers['SERVER'] = 'Secured Server Software'
        return var2561
    return function1083

def function2272(arg1871):
    arg240 = Application(loop=arg1871, middlewares=[function1391])
    arg240.router.add_get('/', function2374)
    return arg240
var1371 = asyncio.get_event_loop()
arg240 = function2272(var1371)
run_app(arg240)