import asyncio
import collections
import re
from unittest import mock
import pytest
from aiohttp import helpers, signals, web
from aiohttp.test_utils import make_mocked_request

@pytest.fixture
def function376():
    return bytearray()

@pytest.fixture
def function972(function376):
    var2637 = 'GET'
    var2672 = '/'
    var2203 = mock.Mock()
    var2203.drain.return_value = ()

    def function2620(arg1868=b''):
        function376.extend(arg1868)
        return helpers.noop()

    def function1322(arg1246, arg769):
        arg769 = (arg1246 + ''.join([(((var790 + ': ') + var3149) + '\r\n') for (var790, var3149) in arg769.items()]))
        arg769 = (arg769.encode('utf-8') + b'\r\n')
        function376.extend(arg769)
    var2203.buffer_data.side_effect = function2620
    var2203.write.side_effect = function2620
    var2203.write_eof.side_effect = function2620
    var2203.function1322.side_effect = function1322
    var3808 = mock.Mock()
    var3808._debug = False
    var3808.on_response_prepare = signals.Signal(var3808)
    var3580 = make_mocked_request(var2637, var2672, app=var3808, payload_writer=var2203)
    return var3580

def function367():
    assert ('HTTPException' in web.__all__)
    for var2090 in dir(web):
        if var2090.startswith('_'):
            continue
        var2768 = getattr(web, var2090)
        if (isinstance(var2768, type) and issubclass(var2768, web.HTTPException)):
            assert (var2090 in web.__all__)

@asyncio.coroutine
def function2312(function376, function972):
    var2320 = web.HTTPOk()
    yield from var2320.prepare(function972)
    yield from var2320.write_eof()
    var1261 = function376.decode('utf8')
    assert re.match('HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\nContent-Length: 7\r\nDate: .+\r\nServer: .+\r\n\r\n200: OK', var1261)

def function2201():
    var1573 = set()
    for var4224 in dir(web):
        var1445 = getattr(web, var4224)
        if (isinstance(var1445, type) and issubclass(var1445, web.HTTPException)):
            var1573.add(var1445)
    var1622 = frozenset(var1573)
    for var321 in var1622:
        for var690 in var1622:
            if (var321 in var690.__bases__):
                var1573.discard(var321)
    for var4206 in var1573:
        assert (var4206.status_code is not None)
    var4707 = collections.Counter((var2681.status_code for var2681 in var1573))
    assert (None not in var4707)
    assert (1 == var4707.most_common(1)[0][1])

@asyncio.coroutine
def function2245(function376, function972):
    var1892 = web.HTTPFound(location='/redirect')
    assert ('/redirect' == var1892.location)
    assert ('/redirect' == var1892.headers['location'])
    yield from var1892.prepare(function972)
    yield from var1892.write_eof()
    var1056 = function376.decode('utf8')
    assert re.match('HTTP/1.1 302 Found\r\nContent-Type: text/plain; charset=utf-8\r\nLocation: /redirect\r\nContent-Length: 10\r\nDate: .+\r\nServer: .+\r\n\r\n302: Found', var1056)

def function825():
    with pytest.raises(ValueError):
        web.HTTPFound(location='')
    with pytest.raises(ValueError):
        web.HTTPFound(location=None)

@asyncio.coroutine
def function715(function376, function972):
    var1791 = web.HTTPMethodNotAllowed('get', ['POST', 'PUT'])
    assert ('GET' == var1791.method)
    assert (['POST', 'PUT'] == var1791.allowed_methods)
    assert ('POST,PUT' == var1791.headers['allow'])
    yield from var1791.prepare(function972)
    yield from var1791.write_eof()
    var172 = function376.decode('utf8')
    assert re.match('HTTP/1.1 405 Method Not Allowed\r\nContent-Type: text/plain; charset=utf-8\r\nAllow: POST,PUT\r\nContent-Length: 23\r\nDate: .+\r\nServer: .+\r\n\r\n405: Method Not Allowed', var172)

def function233():
    var4139 = web.HTTPNotFound(text='Page not found')
    assert (404 == var4139.status)
    assert ('Page not found'.encode('utf-8') == var4139.body)
    assert ('Page not found' == var4139.text)
    assert ('text/plain' == var4139.content_type)
    assert ('utf-8' == var4139.charset)

def function501():
    var2174 = '<html><body>Page not found</body></html>'
    var4329 = web.HTTPNotFound(body=var2174.encode('utf-8'), content_type='text/html')
    assert (404 == var4329.status)
    assert (var2174.encode('utf-8') == var4329.body)
    assert (var2174 == var4329.text)
    assert ('text/html' == var4329.content_type)
    assert (var4329.charset is None)

def function873():
    var1312 = web.HTTPOk()
    assert (b'200: OK' == var1312.body)

def function789():
    var724 = web.HTTPNoContent()
    assert (var724.body is None)

def function286():
    var2531 = web.HTTPNoContent()
    assert (var2531.body is None)

def function2613():
    var2188 = web.HTTPNoContent()
    (var2188.body is None)

def function950(function376, function972):
    var3658 = web.HTTPUnavailableForLegalReasons(link='http://warning.or.kr/')
    assert ('http://warning.or.kr/' == var3658.link)
    assert ('<http://warning.or.kr/>; rel="blocked-by"' == var3658.headers['Link'])