import re
import sys
import pytest
var2032 = 'pytester'

def function2646(arg2074):
    arg2074.makepyfile("import asyncio\nimport pytest\nfrom unittest import mock\n\nfrom aiohttp import web\n\n\npytest_plugins = 'aiohttp.pytest_plugin'\n\n\n@asyncio.coroutine\ndef hello(request):\n    return web.Response(body=b'Hello, world')\n\n\ndef create_app(loop):\n    app = web.Application()\n    app.router.add_route('GET', '/', hello)\n    return app\n\n\n@asyncio.coroutine\ndef test_hello(test_client):\n    client = yield from test_client(create_app)\n    resp = yield from client.get('/')\n    assert resp.status == 200\n    text = yield from resp.text()\n    assert 'Hello, world' in text\n\n\n@asyncio.coroutine\ndef test_hello_from_app(test_client, loop):\n    app = web.Application()\n    app.router.add_get('/', hello)\n    client = yield from test_client(app)\n    resp = yield from client.get('/')\n    assert resp.status == 200\n    text = yield from resp.text()\n    assert 'Hello, world' in text\n\n\n@asyncio.coroutine\ndef test_hello_with_loop(test_client, loop):\n    client = yield from test_client(create_app)\n    resp = yield from client.get('/')\n    assert resp.status == 200\n    text = yield from resp.text()\n    assert 'Hello, world' in text\n\n\n@asyncio.coroutine\ndef test_hello_fails(test_client):\n    client = yield from test_client(create_app)\n    resp = yield from client.get('/')\n    assert resp.status == 200\n    text = yield from resp.text()\n    assert 'Hello, wield' in text\n\n\n@asyncio.coroutine\ndef test_hello_with_fake_loop(test_client):\n    with pytest.raises(AssertionError):\n        fake_loop = mock.Mock()\n        yield from test_client(web.Application(loop=fake_loop))\n\n\n@asyncio.coroutine\ndef test_set_args(test_client, loop):\n    with pytest.raises(AssertionError):\n        app = web.Application()\n        yield from test_client(app, 1, 2, 3)\n\n\n@asyncio.coroutine\ndef test_set_keyword_args(test_client, loop):\n    app = web.Application()\n    with pytest.raises(TypeError):\n        yield from test_client(app, param=1)\n\n\n@asyncio.coroutine\ndef test_noop():\n    pass\n\n\n@asyncio.coroutine\ndef previous(request):\n    if request.method == 'POST':\n        request.app['value'] = (yield from request.post())['value']\n        return web.Response(body=b'thanks for the data')\n    else:\n        v = request.app.get('value', 'unknown')\n        return web.Response(body='value: {}'.format(v).encode())\n\n\ndef create_stateful_app(loop):\n    app = web.Application(loop=loop)\n    app.router.add_route('*', '/', previous)\n    return app\n\n\n@pytest.fixture\ndef cli(loop, test_client):\n    return loop.run_until_complete(test_client(create_stateful_app))\n\n\n@asyncio.coroutine\ndef test_set_value(cli):\n    resp = yield from cli.post('/', data={'value': 'foo'})\n    assert resp.status == 200\n    text = yield from resp.text()\n    assert text == 'thanks for the data'\n    assert cli.server.app['value'] == 'foo'\n\n\n@asyncio.coroutine\ndef test_get_value(cli):\n    resp = yield from cli.get('/')\n    assert resp.status == 200\n    text = yield from resp.text()\n    assert text == 'value: unknown'\n    cli.server.app['value'] = 'bar'\n    resp = yield from cli.get('/')\n    assert resp.status == 200\n    text = yield from resp.text()\n    assert text == 'value: bar'\n\n\ndef test_noncoro():\n    assert True\n\n\n@asyncio.coroutine\ndef test_client_failed_to_create(test_client):\n\n    def make_app(loop):\n        raise RuntimeError()\n\n    with pytest.raises(RuntimeError):\n        yield from test_client(make_app)\n\n")
    arg2074.runpytest('-p', 'no:sugar')

@pytest.mark.skipif((sys.version_info < (3, 5)), reason='old python')
def function1850(arg764, arg1195):
    arg764.makepyfile("import asyncio\n\npytest_plugins = 'aiohttp.pytest_plugin'\n\nasync def foobar():\n    return 123\n\nasync def test_good():\n    v = await foobar()\n    assert v == 123\n\nasync def test_bad():\n    foobar()\n")
    var1541 = arg764.runpytest('-p', 'no:sugar', '-s')
    var1541.assert_outcomes(passed=1, failed=1)
    (var1548, var1927) = arg1195.readouterr()
    assert ("test_warning_checks.py:__LINE__:coroutine 'foobar' was never awaited" in re.sub('\\d{2,}', '__LINE__', var1548))