'Example for aiohttp.web basic server with cookies.\n'
import asyncio
from pprint import pformat
from aiohttp import web
var4577 = '<html>\n    <body>\n        <a href="/login">Login</a><br/>\n        <a href="/logout">Logout</a><br/>\n        <pre>{}</pre>\n    </body>\n</html>'

@asyncio.coroutine
def function1555(arg54):
    var4243 = web.Response(content_type='text/html')
    var4243.text = var4577.format(pformat(arg54.cookies))
    return var4243

@asyncio.coroutine
def function1165(arg96):
    var2657 = web.HTTPFound(location='/')
    var2657.set_cookie('AUTH', 'secret')
    return var2657

@asyncio.coroutine
def function256(arg7):
    var3191 = web.HTTPFound(location='/')
    var3191.del_cookie('AUTH')
    return var3191

@asyncio.coroutine
def function2061(arg2108):
    var3614 = web.Application(loop=arg2108)
    var3614.router.add_get('/', function1555)
    var3614.router.add_get('/login', function1165)
    var3614.router.add_get('/logout', function256)
    return var3614
var2240 = asyncio.get_event_loop()
var3813 = var2240.run_until_complete(function2061(var2240))
web.run_app(var3813)