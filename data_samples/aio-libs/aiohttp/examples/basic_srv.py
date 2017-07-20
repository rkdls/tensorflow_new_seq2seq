'Basic HTTP server with minimal setup'
import asyncio
from urllib.parse import parse_qsl, urlparse
import aiohttp
import aiohttp.server
from aiohttp import MultiDict


class Class328(aiohttp.server.ServerHttpProtocol):

    @asyncio.coroutine
    def function2245(self, arg2114, arg284):
        var2033 = aiohttp.Response(self.writer, 200, http_version=arg2114.version)
        var1109 = MultiDict(parse_qsl(urlparse(arg2114.path).query))
        if (arg2114.method == 'POST'):
            var1549 = yield from arg284.read()
        else:
            var1549 = None
        var2428 = '<h1>It Works!</h1>'
        if var1109:
            var2428 += (('<h2>Get params</h2><p>' + str(var1109)) + '</p>')
        if var1549:
            var2428 += (('<h2>Post params</h2><p>' + str(var1549)) + '</p>')
        var4666 = var2428.encode('utf-8')
        var2033.add_header('Content-Type', 'text/html; charset=UTF-8')
        var2033.add_header('Content-Length', str(len(var4666)))
        var2033.send_headers()
        var2033.write(var4666)
        yield from var2033.write_eof()
if (__name__ == '__main__'):
    var3939 = asyncio.get_event_loop()
    var4247 = var3939.create_server((lambda : Class328(debug=True, keep_alive=75)), '0.0.0.0', 8080)
    var1877 = var3939.run_until_complete(var4247)
    print('serving on', var1877.sockets[0].getsockname())
    try:
        var3939.run_forever()
    except KeyboardInterrupt:
        pass