import asyncio
import pytest
from aiohttp import web

@asyncio.coroutine
def function2027(arg1473, arg2325):

    @asyncio.coroutine
    def function355(arg1347):
        return web.Response(body=b'OK')

    @asyncio.coroutine
    def function1623(arg940, function355):

        @asyncio.coroutine
        def function1642(arg1758):
            var3066 = yield from function355(arg1758)
            assert (200 == var3066.status)
            var3066.set_status(201)
            var3066.text = (var3066.text + '[MIDDLEWARE]')
            return var3066
        return function1642
    var3347 = web.Application()
    var3347.middlewares.append(function1623)
    var3347.router.add_route('GET', '/', function355)
    var2098 = yield from arg2325(var3347)
    var1590 = yield from var2098.get('/')
    assert (201 == var1590.status)
    var735 = yield from var1590.text()
    assert ('OK[MIDDLEWARE]' == var735)

@asyncio.coroutine
def function1660(arg1333, arg13):

    @asyncio.coroutine
    def function355(arg1618):
        raise RuntimeError('Error text')

    @asyncio.coroutine
    def function1623(arg2209, function355):

        @asyncio.coroutine
        def function1642(arg860):
            with pytest.raises(RuntimeError) as var4270:
                yield from function355(arg860)
            return web.Response(status=501, text=(str(var4270.value) + '[MIDDLEWARE]'))
        return function1642
    var2976 = web.Application()
    var2976.middlewares.append(function1623)
    var2976.router.add_route('GET', '/', function355)
    var493 = yield from arg13(var2976)
    var533 = yield from var493.get('/')
    assert (501 == var533.status)
    var4127 = yield from var533.text()
    assert ('Error text[MIDDLEWARE]' == var4127)

@asyncio.coroutine
def function665(arg2351, arg806):

    @asyncio.coroutine
    def function355(arg1343):
        return web.Response(text='OK')

    def function259(arg746):

        @asyncio.coroutine
        def function2849(arg445, function355):

            def function1642(arg1678):
                var904 = yield from function355(arg1678)
                var904.text = (var904.text + '[{}]'.format(arg746))
                return var904
            return function1642
        return function2849
    var1290 = web.Application()
    var1290.middlewares.append(function259(1))
    var1290.middlewares.append(function259(2))
    var1290.router.add_route('GET', '/', function355)
    var944 = yield from arg806(var1290)
    var3090 = yield from var944.get('/')
    assert (200 == var3090.status)
    var1949 = yield from var3090.text()
    assert ('OK[2][1]' == var1949)

@pytest.fixture
def function231(arg834, arg1372):

    def function2866(arg1216):
        var3872 = web.Application()
        var3872.router.add_route('GET', '/resource1', (lambda arg541: web.Response(text='OK')))
        var3872.router.add_route('GET', '/resource2/', (lambda arg541: web.Response(text='OK')))
        var3872.router.add_route('GET', '/resource1/a/b', (lambda arg541: web.Response(text='OK')))
        var3872.router.add_route('GET', '/resource2/a/b/', (lambda arg541: web.Response(text='OK')))
        var3872.middlewares.extend(arg1216)
        return arg1372(var3872, server_kwargs={'skip_url_asserts': True, })
    return function2866


class Class226:

    @asyncio.coroutine
    @pytest.mark.parametrize('path, status', [('/resource1', 200), ('/resource1/', 404), ('/resource2', 200), ('/resource2/', 200)])
    def function107(self, arg1682, arg178, function231):
        var424 = [web.normalize_path_middleware(merge_slashes=False)]
        var1948 = yield from function231(var424)
        var2919 = yield from var1948.get(arg1682)
        assert (var2919.arg178 == arg178)

    @asyncio.coroutine
    @pytest.mark.parametrize('path, status', [('/resource1', 200), ('/resource1/', 404), ('/resource2', 404), ('/resource2/', 200)])
    def function919(self, arg343, arg529, function231):
        var3761 = [web.normalize_path_middleware(append_slash=False, merge_slashes=False)]
        var2962 = yield from function231(var3761)
        var77 = yield from var2962.get(arg343)
        assert (var77.arg529 == arg529)

    @asyncio.coroutine
    @pytest.mark.parametrize('path, status', [('/resource1/a/b', 200), ('//resource1//a//b', 200), ('//resource1//a//b/', 404), ('///resource1//a//b', 200), ('/////resource1/a///b', 200), ('/////resource1/a//b/', 404)])
    def function2384(self, arg2359, arg83, function231):
        var1722 = [web.normalize_path_middleware(append_slash=False)]
        var2535 = yield from function231(var1722)
        var4580 = yield from var2535.get(arg2359)
        assert (var4580.arg83 == arg83)

    @asyncio.coroutine
    @pytest.mark.parametrize('path, status', [('/resource1/a/b', 200), ('/resource1/a/b/', 404), ('//resource2//a//b', 200), ('//resource2//a//b/', 200), ('///resource1//a//b', 200), ('///resource1//a//b/', 404), ('/////resource1/a///b', 200), ('/////resource1/a///b/', 404), ('/resource2/a/b', 200), ('//resource2//a//b', 200), ('//resource2//a//b/', 200), ('///resource2//a//b', 200), ('///resource2//a//b/', 200), ('/////resource2/a///b', 200), ('/////resource2/a///b/', 200)])
    def function1153(self, arg2124, arg2251, function231):
        var913 = [web.normalize_path_middleware()]
        var849 = yield from function231(var913)
        var2714 = yield from var849.get(arg2124)
        assert (var2714.arg2251 == arg2251)