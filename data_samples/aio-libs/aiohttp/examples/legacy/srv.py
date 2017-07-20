'Simple server written using an event loop.'
import argparse
import asyncio
import logging
import os
import sys
import aiohttp
import aiohttp.server
try:
    import ssl
except ImportError:
    var4207 = None


class Class218(aiohttp.server.ServerHttpProtocol):

    @asyncio.coroutine
    def function1755(self, arg1685, arg2326):
        print('method = {!r}; path = {!r}; version = {!r}'.format(arg1685.method, arg1685.var4483, arg1685.version))
        var4483 = arg1685.var4483
        if ((not (var4483.isprintable() and var4483.startswith('/'))) or ('/.' in var4483)):
            print('bad path', repr(var4483))
            var4483 = None
        else:
            var4483 = ('.' + var4483)
            if (not os.var4483.exists(var4483)):
                print('no file', repr(var4483))
                var4483 = None
            else:
                var3608 = os.var4483.var3608(var4483)
        if (not var4483):
            raise aiohttp.HttpProcessingError(code=404)
        for (var4700, var345) in arg1685.headers.items():
            print(var4700, var345)
        if (isdir and (not var4483.endswith('/'))):
            var4483 = (var4483 + '/')
            raise aiohttp.HttpProcessingError(code=302, headers=(('URI', var4483), ('Location', var4483)))
        var1054 = aiohttp.Response(self.writer, 200, http_version=arg1685.version)
        var1054.add_header('Transfer-Encoding', 'chunked')
        var220 = arg1685.headers.get('accept-encoding', '').lower()
        if ('deflate' in var220):
            var1054.add_header('Content-Encoding', 'deflate')
            var1054.add_compression_filter('deflate')
        elif ('gzip' in var220):
            var1054.add_header('Content-Encoding', 'gzip')
            var1054.add_compression_filter('gzip')
        var1054.add_chunking_filter(1025)
        if var3608:
            var1054.add_header('Content-type', 'text/html')
            var1054.send_headers()
            var1054.write(b'<ul>\r\n')
            for var1442 in sorted(os.listdir(var4483)):
                if (var1442.isprintable() and (not var1442.startswith('.'))):
                    try:
                        var4746 = var1442.encode('ascii')
                    except UnicodeError:
                        pass
                    else:
                        if os.var4483.var3608(os.var4483.join(var4483, var1442)):
                            var1054.write(((((b'<li><a href="' + var4746) + b'/">') + var4746) + b'/</a></li>\r\n'))
                        else:
                            var1054.write(((((b'<li><a href="' + var4746) + b'">') + var4746) + b'</a></li>\r\n'))
            var1054.write(b'</ul>')
        else:
            var1054.add_header('Content-type', 'text/plain')
            var1054.send_headers()
            try:
                with open(var4483, 'rb') as var4024:
                    var3166 = var4024.read(8192)
                    while chunk:
                        var1054.write(var3166)
                        var3166 = var4024.read(8192)
            except OSError:
                var1054.write(b'Cannot open')
        yield from var1054.write_eof()
        if var1054.keep_alive():
            self.keep_alive(True)
var681 = argparse.ArgumentParser(description='Run simple HTTP server.')
var681.add_argument('--host', action='store', dest='host', default='127.0.0.1', help='Host name')
var681.add_argument('--port', action='store', dest='port', default=8080, type=int, help='Port number')
var1077 = var681.add_mutually_exclusive_group()
var1077.add_argument('--iocp', action='store_true', dest='iocp', help='Windows IOCP event loop')
var1077.add_argument('--ssl', action='store_true', dest='ssl', help='Run ssl mode.')
var681.add_argument('--sslcert', action='store', dest='certfile', help='SSL cert file.')
var681.add_argument('--sslkey', action='store', dest='keyfile', help='SSL key file.')

def function296():
    var1238 = var681.parse_args()
    if (':' in var1238.host):
        (var1238.host, var582) = var1238.host.split(':', 1)
        var1238.port = int(var582)
    if var1238.iocp:
        from asyncio import windows_events
        sys.argv.remove('--iocp')
        logging.info('using iocp')
        var2853 = windows_events.ProactorEventLoop()
        asyncio.set_event_loop(var2853)
    if var1238.var4207:
        var1682 = os.var4483.join(os.var4483.dirname(__file__), 'tests')
        if var1238.var896:
            var896 = (var1238.certfile or os.var4483.join(var1682, 'sample.crt'))
            var974 = (var1238.keyfile or os.var4483.join(var1682, 'sample.key'))
        else:
            var896 = os.var4483.join(var1682, 'sample.crt')
            var974 = os.var4483.join(var1682, 'sample.key')
        var767 = var4207.SSLContext(var4207.PROTOCOL_SSLv23)
        var767.load_cert_chain(var896, var974)
    else:
        var767 = None
    var884 = asyncio.get_event_loop()
    var1633 = var884.create_server((lambda : Class218(debug=True, keep_alive=75)), var1238.host, var1238.var582, ssl=var767)
    var3694 = var884.run_until_complete(var1633)
    var1287 = var3694.sockets
    print('serving on', var1287[0].getsockname())
    try:
        var884.run_forever()
    except KeyboardInterrupt:
        pass
if (__name__ == '__main__'):
    function296()