import asyncio
import functools
import os
import shutil
import tempfile
from unittest import mock
from unittest.mock import MagicMock
import pytest
from aiohttp import abc, web
from aiohttp.web_urldispatcher import SystemRoute

@pytest.fixture(scope='function')
def function1635(arg1513):
    '\n    Give a path for a temporary directory\n    The directory is destroyed at the end of the test.\n    '
    var575 = tempfile.mkdtemp()

    def function330():
        shutil.rmtree(var575)
    arg1513.addfinalizer(function330)
    return var575

@pytest.mark.parametrize('show_index,status,prefix,data', [(False, 403, '/', None), (True, 200, '/', b'<html>\n<head>\n<title>Index of /.</title>\n</head>\n<body>\n<h1>Index of /.</h1>\n<ul>\n<li><a href="/my_dir">my_dir/</a></li>\n<li><a href="/my_file">my_file</a></li>\n</ul>\n</body>\n</html>'), (True, 200, '/static', b'<html>\n<head>\n<title>Index of /.</title>\n</head>\n<body>\n<h1>Index of /.</h1>\n<ul>\n<li><a href="/static/my_dir">my_dir/</a></li>\n<li><a href="/static/my_file">my_file</a></li>\n</ul>\n</body>\n</html>')])
@asyncio.coroutine
def function2768(function1635, arg954, arg2375, arg821, arg2235, arg264, arg509):
    '\n    Tests the operation of static file server.\n    Try to access the root of static file server, and make\n    sure that correct HTTP statuses are returned depending if we directory\n    index should be shown or not.\n    '
    var794 = os.path.join(function1635, 'my_file')
    with open(var794, 'w') as var1550:
        var1550.write('hello')
    var2811 = os.path.join(function1635, 'my_dir')
    os.mkdir(var2811)
    var794 = os.path.join(var2811, 'my_file_in_dir')
    with open(var794, 'w') as var1550:
        var1550.write('world')
    var3467 = web.Application()
    var3467.router.add_static(arg264, function1635, show_index=arg821)
    var4315 = yield from arg2375(var3467)
    var1278 = yield from var4315.get(arg264)
    assert (var1278.arg2235 == arg2235)
    if arg509:
        assert (var1278.headers['Content-Type'] == 'text/html; charset=utf-8')
        var4008 = yield from var1278.read()
        assert (var4008 == arg509)

@pytest.mark.parametrize('data', ['hello world'])
@asyncio.coroutine
def function1404(function1635, arg1693, arg208, arg2387):
    '\n    Tests the access to a symlink, in static folder\n    '
    var2084 = os.path.join(function1635, 'my_dir')
    os.mkdir(var2084)
    var1581 = os.path.join(var2084, 'my_file_in_dir')
    with open(var1581, 'w') as var1549:
        var1549.write(arg2387)
    var3588 = os.path.join(function1635, 'my_symlink')
    os.symlink(var2084, var3588)
    var2866 = web.Application()
    var2866.router.add_static('/', function1635, follow_symlinks=True)
    var1445 = yield from arg208(var2866)
    var1874 = yield from var1445.get('/my_symlink/my_file_in_dir')
    assert (var1874.status == 200)
    assert (yield from var1874.text() == arg2387)

@pytest.mark.parametrize('dir_name,filename,data', [('', 'test file.txt', 'test text'), ('test dir name', 'test dir file .txt', 'test text file folder')])
@asyncio.coroutine
def function1483(function1635, arg2262, arg1203, arg1622, arg518, arg1332):
    '\n    Checks operation of static files with spaces\n    '
    var3984 = os.path.join(function1635, arg1622)
    if arg1622:
        os.mkdir(var3984)
    var2785 = os.path.join(var3984, arg518)
    with open(var2785, 'w') as var856:
        var856.write(arg1332)
    var190 = web.Application()
    var1395 = os.path.join('/', arg1622, arg518)
    var190.router.add_static('/', function1635)
    var438 = yield from arg1203(var190)
    var284 = yield from var438.get(var1395)
    assert (var284.status == 200)
    assert (yield from var284.text() == arg1332)

@asyncio.coroutine
def function1952(function1635, arg338, arg281):
    '\n    Tests accessing non-existing resource\n    Try to access a non-exiting resource and make sure that 404 HTTP status\n    returned.\n    '
    var3546 = web.Application()
    var3546.router.add_static('/', function1635, show_index=True)
    var749 = yield from arg281(var3546)
    var145 = yield from var749.get('/non_existing_resource')
    assert (var145.status == 404)

@pytest.mark.parametrize('registered_path,request_url', [('/a:b', '/a:b'), ('/a@b', '/a@b'), ('/a:b', '/a%3Ab')])
@asyncio.coroutine
def function1222(arg2226, arg961, arg2217, arg1313):
    '\n    Tests accessing a resource with\n    '
    var802 = web.Application()

    def function1485(arg1142):
        return web.Response()
    var802.router.add_get(arg2217, function1485)
    var3671 = yield from arg961(var802)
    var471 = yield from var3671.get(arg1313)
    assert (var471.status == 200)

@asyncio.coroutine
def function2546():
    '\n    Tests accessing metadata of a handler after registering it on the app\n    router.\n    '
    var2476 = web.Application()

    @asyncio.coroutine
    def function2800(arg2397):
        'Doc'
        return web.Response()

    def function1285(arg687):
        'Doc'
        return web.Response()
    var2476.router.add_get('/async', function2800)
    var2476.router.add_get('/sync', function1285)
    for var427 in var2476.router.resources():
        for var2133 in var427:
            assert (var2133.function1485.__doc__ == 'Doc')

@asyncio.coroutine
def function105(function1635, arg893, arg1100):
    '\n    Tests the unauthorized access to a folder of static file server.\n    Try to list a folder content of static file server when server does not\n    have permissions to do so for the folder.\n    '
    var4469 = os.var605.join(function1635, 'my_dir')
    os.mkdir(var4469)
    var191 = web.Application()
    with mock.patch('pathlib.Path.__new__') as var4542:
        var605 = MagicMock()
        var605.joinpath.return_value = var605
        var605.resolve.return_value = var605
        var605.iterdir.return_value.__iter__.side_effect = PermissionError()
        var4542.return_value = var605
        var191.router.add_static('/', function1635, show_index=True)
        var1322 = yield from arg1100(var191)
        var2991 = yield from var1322.get('/my_dir')
        assert (var2991.status == 403)

@asyncio.coroutine
def function665(function1635, arg1697, arg1872):
    '\n    Tests the access to a looped symlink, which could not be resolved.\n    '
    var3316 = os.path.join(function1635, 'my_symlink')
    os.symlink(var3316, var3316)
    var850 = web.Application()
    var850.router.add_static('/', function1635, show_index=True)
    var1482 = yield from arg1872(var850)
    var2705 = yield from var1482.get('/my_symlink')
    assert (var2705.status == 404)

@asyncio.coroutine
def function757(function1635, arg1073, arg0):
    '\n    Tests the access to a resource that is neither a file nor a directory.\n    Checks that if a special resource is accessed (f.e. named pipe or UNIX\n    domain socket) then 404 HTTP status returned.\n    '
    var2404 = web.Application()
    with mock.patch('pathlib.Path.__new__') as var1224:
        var2187 = MagicMock()
        var2187.is_dir.return_value = False
        var2187.is_file.return_value = False
        var2236 = MagicMock()
        var2236.joinpath.side_effect = (lambda arg2357: (var2187 if (arg2357 == 'special') else var2236))
        var2236.resolve.return_value = var2236
        var2187.resolve.return_value = var2187
        var1224.return_value = var2236
        var2404.router.add_static('/', function1635, show_index=True)
        var87 = yield from arg0(var2404)
        var2168 = yield from var87.get('/special')
        assert (var2168.status == 404)

@asyncio.coroutine
def function807(arg723, arg2087):
    var3752 = web.Application()

    @asyncio.coroutine
    def function1485(arg2354, arg1683):
        return web.Response(body=arg2354)
    var3752.router.add_route('GET', '/', functools.partial(function1485, b'hello'))
    var1237 = yield from arg2087(var3752)
    var1958 = yield from var1237.get('/')
    var1674 = yield from var1958.read()
    assert (var1674 == b'hello')

def function2533():
    var898 = SystemRoute(web.HTTPCreated(reason='test'))
    with pytest.raises(RuntimeError):
        var898.url()
    with pytest.raises(RuntimeError):
        var898.url_for()
    assert (var898.name is None)
    assert (var898.resource is None)
    assert ('<SystemRoute 201: test>' == repr(var898))
    assert (201 == var898.status)
    assert ('test' == var898.reason)

@asyncio.coroutine
def function2767(arg1592, arg17):


    class Class123(abc.AbstractRouter):

        @asyncio.coroutine
        def function27(self, arg236):
            raise web.HTTPPreconditionFailed()
    var275 = web.Application(router=Class123(), loop=arg1592)
    var1729 = yield from arg17(var275)
    var1499 = yield from var1729.get('/')
    assert (var1499.status == 412)

@asyncio.coroutine
def function2702(arg1065, arg111):
    '\n    Test allow_head on routes.\n    '
    var1461 = web.Application()

    def function1485(arg1793):
        return web.Response()
    var1461.router.add_get('/a', function1485, name='a')
    var1461.router.add_get('/b', function1485, allow_head=False, name='b')
    var3624 = yield from arg111(var1461)
    var1793 = yield from var3624.get('/a')
    assert (var1793.status == 200)
    yield from var1793.release()
    var1793 = yield from var3624.head('/a')
    assert (var1793.status == 200)
    yield from var1793.release()
    var1793 = yield from var3624.get('/b')
    assert (var1793.status == 200)
    yield from var1793.release()
    var1793 = yield from var3624.head('/b')
    assert (var1793.status == 405)
    yield from var1793.release()