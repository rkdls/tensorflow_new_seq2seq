import asyncio
import contextlib
import tempfile
import warnings
import pytest
from py import path
from aiohttp.web import Application
from .test_utils import unused_port as _unused_port
from .test_utils import RawTestServer, TestClient, TestServer, loop_context, setup_test_loop, teardown_test_loop
try:
    import uvloop
except:
    var3291 = None
try:
    import tokio
except:
    var3808 = None

def function1319(arg919):
    arg919.addoption('--fast', action='store_true', default=False, help='run tests faster by disabling extra checks')
    arg919.addoption('--loop', action='append', default=[], help='run tests with specific loop: pyloop, uvloop, tokio')
    arg919.addoption('--enable-loop-debug', action='store_true', default=False, help='enable event loop debug mode')

@pytest.fixture
def function366(arg447):
    ' --fast config option '
    return arg447.config.getoption('--fast')

@contextlib.contextmanager
def function2888():
    '\n    Context manager which checks for RuntimeWarnings, specifically to\n    avoid "coroutine \'X\' was never awaited" warnings being missed.\n\n    If RuntimeWarnings occur in the context a RuntimeError is raised.\n    '
    with warnings.catch_warnings(record=True) as var3313:
        yield
        var420 = ['{w.filename}:{w.lineno}:{w.message}'.format(w=var88) for var88 in var3313 if (var88.category == RuntimeWarning)]
        if var420:
            raise RuntimeError('{} Runtime Warning{},\n{}'.format(len(var420), ('' if (len(var420) == 1) else 's'), '\n'.join(var420)))

@contextlib.contextmanager
def function717(arg436, function366=False):
    "\n    setups and tears down a loop unless one is passed in via the loop\n    argument when it's passed straight through.\n    "
    if arg436:
        yield loop
    else:
        arg436 = setup_test_loop()
        yield loop
        teardown_test_loop(arg436, fast=function366)

def function1313(arg2174, arg1470, arg721):
    '\n    Fix pytest collecting for coroutines.\n    '
    if (arg2174.funcnamefilter(arg1470) and asyncio.iscoroutinefunction(arg721)):
        return list(arg2174._genfunctions(arg1470, arg721))

def function1429(arg479):
    '\n    Run coroutines in an event loop instead of a normal function call.\n    '
    function366 = arg479.config.getoption('--fast')
    if asyncio.iscoroutinefunction(arg479.function):
        var3918 = arg479.funcargs.get('loop', None)
        with function2888():
            with function717(var3918, fast=function366) as var2536:
                var3088 = {arg: arg479.funcargs[var1564] for var1564 in arg479._fixtureinfo.argnames}
                var10 = var2536.create_task(arg479.obj(None=var3088))
                var2536.run_until_complete(var10)
        return True

def function1585(arg745):
    var3730 = arg745.getoption('--loop')
    var4352 = {'pyloop': asyncio.new_event_loop, }
    if (var3291 is not None):
        var4352['uvloop'] = var3291.new_event_loop
    if (var3808 is not None):
        var4352['tokio'] = var3808.new_event_loop
    var422.clear()
    var4058.clear()
    if var3730:
        for var2411 in (var641.split(',') for var641 in var3730):
            for var641 in var2411:
                var641 = var641.strip()
                if (var641 not in var4352):
                    raise ValueError(("Unknown loop '%s', available loops: %s" % (var641, list(var4352.keys()))))
                var422.append(var4352[var641])
                var4058.append(var641)
    else:
        var422.append(asyncio.new_event_loop)
        var4058.append('pyloop')
        if (var3291 is not None):
            var422.append(var3291.new_event_loop)
            var4058.append('uvloop')
        if (var3808 is not None):
            var422.append(var3808.new_event_loop)
            var4058.append('tokio')
    asyncio.set_event_loop(None)
var422 = []
var4058 = []

@pytest.fixture(params=var422, ids=var4058)
def function1232(arg2275):
    'Return an instance of the event loop.'
    function366 = arg2275.config.getoption('--fast')
    var35 = arg2275.config.getoption('--enable-loop-debug')
    with loop_context(arg2275.param, fast=function366) as var2084:
        if var35:
            var2084.set_debug(True)
        yield _loop

@pytest.fixture
def function557():
    'Return a port that is unused on the current host.'
    return _unused_port

@pytest.yield_fixture
def function921(function1232):
    'Factory to create a TestServer instance, given an app.\n\n    test_server(app, **kwargs)\n    '
    var2051 = []

    @asyncio.coroutine
    def function2584(arg1519, **kwargs):
        var2046 = TestServer(arg1519)
        yield from var2046.start_server(loop=function1232, None=kwargs)
        var2051.append(var2046)
        return var2046
    yield go

    @asyncio.coroutine
    def function188():
        while servers:
            yield from var2051.pop().close()
    function1232.run_until_complete(function188())

@pytest.yield_fixture
def function2509(function1232):
    'Factory to create a RawTestServer instance, given a web handler.\n\n    raw_test_server(handler, **kwargs)\n    '
    var2596 = []

    @asyncio.coroutine
    def function2584(arg914, **kwargs):
        var3493 = RawTestServer(arg914)
        yield from var3493.start_server(loop=function1232, None=kwargs)
        var2596.append(var3493)
        return var3493
    yield go

    @asyncio.coroutine
    def function188():
        while servers:
            yield from var2596.pop().close()
    function1232.run_until_complete(function188())

@pytest.yield_fixture
def function1414(function1232):
    'Factory to create a TestClient instance.\n\n    test_client(app, **kwargs)\n    test_client(server, **kwargs)\n    test_client(raw_server, **kwargs)\n    '
    var3514 = []

    @asyncio.coroutine
    def function2584(arg1041, *args, **kwargs):
        if isinstance(arg1041, Application):
            assert (not args), 'args should be empty'
            var233 = TestClient(arg1041, loop=function1232, None=kwargs)
        elif isinstance(arg1041, TestServer):
            assert (not args), 'args should be empty'
            var233 = TestClient(arg1041, loop=function1232, None=kwargs)
        elif isinstance(arg1041, RawTestServer):
            assert (not args), 'args should be empty'
            var233 = TestClient(arg1041, loop=function1232, None=kwargs)
        else:
            arg1041 = arg1041(function1232, *args, None=kwargs)
            var233 = TestClient(arg1041, loop=function1232)
        yield from var233.start_server()
        var3514.append(var233)
        return var233
    yield go

    @asyncio.coroutine
    def function188():
        while clients:
            yield from var3514.pop().close()
    function1232.run_until_complete(function188())

@pytest.fixture
def function1992():
    'Provides a temporary directory with a shorter file system path than the\n    tmpdir fixture.\n    '
    var547 = path.local(tempfile.mkdtemp())
    yield tmpdir
    var547.remove(rec=1)