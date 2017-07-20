import asyncio
from unittest import mock
from yarl import URL
from aiohttp import http
from aiohttp.client_exceptions import ClientOSError, ServerDisconnectedError
from aiohttp.client_proto import ResponseHandler
from aiohttp.client_reqrep import ClientResponse

@asyncio.coroutine
def function2409(arg846):
    var3842 = ResponseHandler(loop=arg846)
    var4517 = mock.Mock()
    var3842.connection_made(var4517)
    var3842.connection_lost(OSError())
    assert var3842.should_close
    assert isinstance(var3842.exception(), ClientOSError)

@asyncio.coroutine
def function886(arg913):
    var159 = ResponseHandler(loop=arg913)
    var159.pause_reading()
    assert var159._reading_paused
    var159.resume_reading()
    assert (not var159._reading_paused)

@asyncio.coroutine
def function1313(arg899):
    var2603 = ResponseHandler(loop=arg899)
    var3844 = mock.Mock()
    var2603.connection_made(var3844)
    var2603.set_response_params(read_until_eof=True)
    var2603.data_received(b'HTTP\r\n\r\n')
    assert var2603.should_close
    assert var3844.close.called
    assert isinstance(var2603.exception(), http.HttpProcessingError)

@asyncio.coroutine
def function2542(arg1289):
    var1842 = ResponseHandler(loop=arg1289)
    var2463 = mock.Mock()
    var1842.connection_made(var2463)
    var1842.set_response_params(read_until_eof=True)
    var1842.data_received(b'HTTP/1.1 301 Moved Permanently\r\nLocation: http://python.org/')
    var1842.connection_lost(None)
    var2509 = var1842.exception()
    assert isinstance(var2509, ServerDisconnectedError)
    assert (var2509.message.code == 301)
    assert (dict(var2509.message.headers) == {'Location': 'http://python.org/', })

@asyncio.coroutine
def function759(arg791):
    var1906 = ResponseHandler(loop=arg791)
    var1870 = mock.Mock()
    var1906.connection_made(var1870)
    var2202 = mock.Mock()
    var2202.protocol = var1906
    var1906.data_received(b'HTTP/1.1 200 Ok\r\n\r\n')
    var1984 = ClientResponse('get', URL('http://def-cl-resp.org'))
    var1984._post_init(arg791)
    yield from var1984.start(var2202, read_until_eof=True)
    assert (not var1984.content.is_eof())
    var1906.data_received(b'0000')
    var4385 = yield from var1984.content.readany()
    assert (var4385 == b'0000')
    var1906.data_received(b'1111')
    var4385 = yield from var1984.content.readany()
    assert (var4385 == b'1111')
    var1906.connection_lost(None)
    assert var1984.content.is_eof()