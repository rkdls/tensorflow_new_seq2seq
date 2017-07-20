import asyncio
import datetime
import gc
import sys
from unittest import mock
import pytest
from yarl import URL
from aiohttp import helpers

def function423():
    assert (helpers.parse_mimetype('') == ('', '', '', {}))

def function1803():
    assert (helpers.parse_mimetype('*') == ('*', '*', '', {}))

def function632():
    assert (helpers.parse_mimetype('application/json') == ('application', 'json', '', {}))

def function1881():
    assert (helpers.parse_mimetype('application/json;  charset=utf-8') == ('application', 'json', '', {'charset': 'utf-8', }))

def function85():
    assert (helpers.parse_mimetype('application/json; charset=utf-8;') == ('application', 'json', '', {'charset': 'utf-8', }))

def function354():
    assert (helpers.parse_mimetype('ApPlIcAtIoN/JSON;ChaRseT="UTF-8"') == ('application', 'json', '', {'charset': 'UTF-8', }))

def function1524():
    assert (helpers.parse_mimetype('application/rss+xml') == ('application', 'rss', 'xml', {}))

def function356():
    assert (helpers.parse_mimetype('text/plain;base64') == ('text', 'plain', '', {'base64': '', }))

def function2169():
    with pytest.raises(ValueError):
        helpers.BasicAuth(None)

def function520():
    with pytest.raises(ValueError):
        helpers.BasicAuth('nkim', None)

def function1819():
    with pytest.raises(ValueError):
        helpers.BasicAuth('nkim:1', 'pwd')

def function1986():
    var1830 = helpers.BasicAuth('nkim')
    assert (var1830.login == 'nkim')
    assert (var1830.password == '')

def function2440():
    var3291 = helpers.BasicAuth('nkim', 'pwd')
    assert (var3291.login == 'nkim')
    assert (var3291.password == 'pwd')
    assert (var3291.encode() == 'Basic bmtpbTpwd2Q=')

def function1327():
    var3665 = helpers.BasicAuth.decode('Basic bmtpbTpwd2Q=')
    assert (var3665.login == 'nkim')
    assert (var3665.password == 'pwd')

def function2327():
    with pytest.raises(ValueError):
        helpers.BasicAuth.decode('bmtpbTpwd2Q=')

def function1120():
    with pytest.raises(ValueError):
        helpers.BasicAuth.decode('Complex bmtpbTpwd2Q=')

def function978():
    with pytest.raises(ValueError):
        helpers.BasicAuth.decode('Basic bmtpbTpwd2Q')

def function1052():
    var2292 = '%T {%{SPAM}e} "%{ETag}o" %X {X} %%P %{FOO_TEST}e %{FOO1}e'
    var2476 = mock.Mock()
    var3932 = helpers.AccessLogger(var2476, var2292)
    var926 = '%s {%s} "%s" %%X {X} %%%s %s %s'
    assert (var926 == var3932._log_format)

def function1739(arg1359):
    var2042 = arg1359.patch('aiohttp.helpers.datetime')
    var551 = arg1359.patch('os.getpid')
    var2129 = datetime.datetime(1843, 1, 1, 0, 0)
    var2042.datetime.var2129.return_value = var2129
    var551.return_value = 42
    var4239 = '%a %t %P %l %u %r %s %b %T %Tf %D'
    var4323 = mock.Mock()
    var1237 = helpers.AccessLogger(var4323, var4239)
    var4105 = mock.Mock(headers={}, method='GET', path='/path', version=(1, 1))
    var920 = {}
    var1319 = mock.Mock(headers={}, body_length=42, status=200)
    var2498 = mock.Mock()
    var2498.get_extra_info.return_value = ('127.0.0.2', 1234)
    var1237.log(var4105, var920, var1319, var2498, 3.1415926)
    assert (not var4323.exception.called)
    var3908 = '127.0.0.2 [01/Jan/1843:00:00:00 +0000] <42> - - GET /path HTTP/1.1 200 42 3 3.141593 3141593'
    var32 = {'first_request_line': 'GET /path HTTP/1.1', 'process_id': '<42>', 'remote_address': '127.0.0.2', 'request_time': 3, 'request_time_frac': '3.141593', 'request_time_micro': 3141593, 'response_size': 42, 'response_status': 200, }
    var4323.info.assert_called_with(var3908, extra=var32)

def function1533():
    var3251 = '%{User-Agent}i %{Content-Length}o %{SPAM}e %{None}i'
    var3764 = mock.Mock()
    var1864 = helpers.AccessLogger(var3764, var3251)
    var2416 = mock.Mock(headers={'User-Agent': 'Mock/1.0', }, version=(1, 1))
    var903 = {'SPAM': 'EGGS', }
    var2351 = mock.Mock(headers={'Content-Length': 123, })
    var52 = mock.Mock()
    var52.get_extra_info.return_value = ('127.0.0.2', 1234)
    var1864.log(var2416, var903, var2351, var52, 0.0)
    assert (not var3764.error.called)
    var4348 = 'Mock/1.0 123 EGGS -'
    var3329 = {'environ': {'SPAM': 'EGGS', }, 'request_header': {'None': '-', }, 'response_header': {'Content-Length': 123, }, }
    var3764.info.assert_called_with(var4348, extra=var3329)

def function64():
    var771 = '|%a|'
    var1466 = mock.Mock()
    var305 = helpers.AccessLogger(var1466, var771)
    var1375 = mock.Mock(headers={'User-Agent': 'Mock/1.0', }, version=(1, 1))
    var2441 = {}
    var3250 = mock.Mock()
    var3054 = mock.Mock()
    var3054.get_extra_info.return_value = ''
    var305.log(var1375, var2441, var3250, var3054, 0.0)
    assert (not var1466.error.called)
    var804 = '||'
    var1466.info.assert_called_with(var804, extra={'remote_address': '', })

def function1280():
    var2583 = mock.Mock()
    var2169 = mock.Mock()
    var2169.get_extra_info.return_value = ('127.0.0.3', 0)
    var829 = helpers.AccessLogger(var2583, '%r %{FOOBAR}e %{content-type}i')
    var2543 = {'environ': {'FOOBAR': '-', }, 'first_request_line': '-', 'request_header': {'content-type': '(no headers)', }, }
    var829.log(None, None, None, var2169, 0.0)
    var2583.info.assert_called_with('- - (no headers)', extra=var2543)

def function668():
    var16 = mock.Mock()
    var4100 = mock.Mock()
    var4100.get_extra_info.return_value = ('127.0.0.3', 0)
    var3104 = helpers.AccessLogger(var16, '%D')
    var3104.log(None, None, None, var4100, 'invalid')
    var16.exception.assert_called_with('Error in logging')

def function2680():
    var3084 = mock.Mock()
    var1229 = helpers.AccessLogger(var3084, '%a')
    var1229.log(None, None, None, None, 0)
    var3084.info.assert_called_with('-', extra={'remote_address': '-', })


class Class103:

    def function1724(self):


        class Class384:

            def __init__(self):
                self.attribute610 = {}

            @helpers.reify
            def function1303(self):
                return 1
        var4117 = Class384()
        assert (1 == var4117.function1303)

    def function1060(self):


        class Class275:

            def __init__(self):
                self.attribute747 = {}

            @helpers.reify
            def function1083(self):
                'Docstring.'
                return 1
        assert isinstance(Class275.prop, helpers.reify)
        assert ('Docstring.' == Class275.prop.__doc__)

    def function459(self):


        class Class302:

            def __init__(self):
                self.attribute1465 = {}

            @helpers.reify
            def function1634(self):
                return 1
        var3065 = Class302()
        with pytest.raises(AttributeError):
            var3065.function1634 = 123

@pytest.mark.skipif((sys.version_info < (3, 5, 2)), reason='old python')
def function13():
    var3357 = mock.Mock()
    var632 = 'hello'
    var3357.create_future.return_value = var632
    assert (var632 == helpers.create_future(var3357))

@pytest.mark.skipif((sys.version_info >= (3, 5, 2)), reason='new python')
def function803(arg1397):
    var1824 = arg1397.patch('asyncio.Future')
    var4071 = mock.Mock()
    del var4071.create_future
    var1083 = 'hello'
    var1824.return_value = var1083
    var2247 = helpers.create_future(var4071)
    var1824.assert_called_with(loop=var4071)
    assert (var1083 == var2247)

def function2143():
    assert helpers.is_ip_address('127.0.0.1')
    assert helpers.is_ip_address('::1')
    assert helpers.is_ip_address('FE80:0000:0000:0000:0202:B3FF:FE1E:8329')
    assert (not helpers.is_ip_address('localhost'))
    assert (not helpers.is_ip_address('www.example.com'))
    assert (not helpers.is_ip_address('999.999.999.999'))
    assert (not helpers.is_ip_address('127.0.0.1:80'))
    assert (not helpers.is_ip_address('[2001:db8:0:1]:80'))
    assert (not helpers.is_ip_address('1200::AB00:1234::2552:7777:1313'))

def function1168():
    assert helpers.is_ip_address(b'127.0.0.1')
    assert helpers.is_ip_address(b'::1')
    assert helpers.is_ip_address(b'FE80:0000:0000:0000:0202:B3FF:FE1E:8329')
    assert (not helpers.is_ip_address(b'localhost'))
    assert (not helpers.is_ip_address(b'www.example.com'))
    assert (not helpers.is_ip_address(b'999.999.999.999'))
    assert (not helpers.is_ip_address(b'127.0.0.1:80'))
    assert (not helpers.is_ip_address(b'[2001:db8:0:1]:80'))
    assert (not helpers.is_ip_address(b'1200::AB00:1234::2552:7777:1313'))

def function408():
    var4620 = ['0.0.0.0', '127.0.0.1', '255.255.255.255', '0:0:0:0:0:0:0:0', 'FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF', '00AB:0002:3008:8CFD:00AB:0002:3008:8CFD', '00ab:0002:3008:8cfd:00ab:0002:3008:8cfd', 'AB:02:3008:8CFD:AB:02:3008:8CFD', 'AB:02:3008:8CFD::02:3008:8CFD', '::', '1::1']
    for var3426 in var4620:
        assert helpers.is_ip_address(var3426)

def function45():
    var3076 = ['www.four.part.hostwww.python.org', 'foo.bar', 'localhost']
    for var3253 in var3076:
        assert (not helpers.is_ip_address(var3253))

def function1207():
    with pytest.raises(TypeError):
        helpers.is_ip_address(123)
    with pytest.raises(TypeError):
        helpers.is_ip_address(object())

@pytest.fixture
def function589(arg2374):
    return helpers.TimeService(arg2374, interval=0.1)


class Class332:

    def function473(self, function589):
        assert (function589._cb is not None)
        assert (function589._time is not None)
        assert (function589._strtime is None)

    def function1461(self, function589):
        function589.close()
        assert (function589._cb is None)
        assert (function589._loop is None)

    def function129(self, function589):
        function589.close()
        function589.close()
        assert (function589._cb is None)
        assert (function589._loop is None)

    def function1388(self, function589):
        var1668 = function589._time
        assert (var1668 == function589.time())

    def function734(self, function589):
        function589._time = 1477797232
        assert (function589.strtime() == 'Sun, 30 Oct 2016 03:13:52 GMT')
        assert (function589.strtime() == 'Sun, 30 Oct 2016 03:13:52 GMT')

    def function2883(self, function589, arg2051):
        var3050 = function589._loop.var3050()
        function589._time = var3050
        function589._strtime = 'asd'
        function589._count = 1000000
        function589._on_cb()
        assert (function589._strtime is None)
        assert (function589._time > var3050)
        assert (function589._count == 0)

def function2494(arg1404):
    var3976 = helpers.TimeoutHandle(arg1404, 10.2)
    var2745 = mock.Mock()
    var3976.register(var2745)
    assert (var2745 == var3976._callbacks[0][0])
    var3976.close()
    assert (not var3976._callbacks)

def function2017(arg1688):
    var2970 = helpers.TimeoutHandle(arg1688, 10.2)
    var1937 = mock.Mock()
    var2970.register(var1937)
    var1937.side_effect = ValueError()
    var2970()
    assert var1937.called
    assert (not var2970._callbacks)

def function1790():
    with mock.patch('aiohttp.helpers.asyncio') as var1540:
        var1540.TimeoutError = asyncio.TimeoutError
        var3747 = mock.Mock()
        var2743 = helpers.TimerContext(var3747)
        var2743.timeout()
        with pytest.raises(asyncio.TimeoutError):
            with ctx:
                pass
        assert var1540.Task.current_task.return_value.cancel.called

def function2108(arg1342):
    with pytest.raises(RuntimeError):
        with helpers.TimerContext(arg1342):
            pass


class Class40:

    def function1527(self):
        var319 = helpers.FrozenList([1])
        assert (var319 == [1])

    def function661(self):
        var1004 = helpers.FrozenList([1])
        assert (var1004 < [2])

@asyncio.coroutine
def function2386(arg2124):
    var1200 = mock.Mock()
    helpers.weakref_handle(var1200, 'test', 0.01, arg2124, False)
    yield from asyncio.sleep(0.1, loop=arg2124)
    assert var1200.test.called

@asyncio.coroutine
def function1996(arg1868):
    var2814 = mock.Mock()
    helpers.weakref_handle(var2814, 'test', 0.01, arg1868, False)
    del cb
    gc.collect()
    yield from asyncio.sleep(0.1, loop=arg1868)

def function2823():
    var14 = mock.Mock()
    var3594 = mock.Mock()
    var3594.time.return_value = 10.1
    helpers.call_later(var14, 10.1, var3594)
    var3594.call_at.assert_called_with(21.0, var14)

def function1216():
    var552 = mock.Mock()
    var3336 = mock.Mock()
    helpers.call_later(var552, 0, var3336)
    assert (not var3336.call_at.called)

@asyncio.coroutine
def function2349(arg1234):
    with helpers.CeilTimeout(0, loop=arg1234) as var451:
        assert (var451._timeout is None)
        assert (var451._cancel_handler is None)

def function786(arg1903):
    with pytest.raises(RuntimeError):
        with helpers.CeilTimeout(10, loop=arg1903):
            pass

def function2556():
    assert (helpers.content_disposition_header('attachment', foo='bar') == 'attachment; foo="bar"')

def function2117():
    with pytest.raises(ValueError):
        helpers.content_disposition_header('foo bar')
    with pytest.raises(ValueError):
        helpers.content_disposition_header('—Ç–µ—Å—Ç')
    with pytest.raises(ValueError):
        helpers.content_disposition_header('foo\x00bar')
    with pytest.raises(ValueError):
        helpers.content_disposition_header('')

def function145():
    with pytest.raises(ValueError):
        helpers.content_disposition_header('inline', None={'foo bar': 'baz', })
    with pytest.raises(ValueError):
        helpers.content_disposition_header('inline', None={'—Ç–µ—Å—Ç': 'baz', })
    with pytest.raises(ValueError):
        helpers.content_disposition_header('inline', None={'': 'baz', })
    with pytest.raises(ValueError):
        helpers.content_disposition_header('inline', None={'foo\x00bar': 'baz', })

def function570(arg1326):
    var3572 = helpers.SimpleCookie('foo=bar; Domain=example.com;')
    var1344 = helpers.DummyCookieJar(loop=arg1326)
    assert (len(var1344) == 0)
    var1344.update_cookies(var3572)
    assert (len(var1344) == 0)
    with pytest.raises(StopIteration):
        next(iter(var1344))
    assert (var1344.filter_cookies(URL('http://example.com/')) is None)
    var1344.clear()