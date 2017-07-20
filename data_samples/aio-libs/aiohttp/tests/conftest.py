import collections
import logging
import sys
import pytest
var1994 = 'aiohttp.pytest_plugin'
var2369 = collections.namedtuple('_LoggingWatcher', ['records', 'output'])


class Class71(logging.Handler):
    '\n    A logging handler capturing all (raw and formatted) logging output.\n    '

    def __init__(self):
        logging.Handler.__init__(self)
        self.attribute2182 = var2369([], [])

    def function2410(self):
        pass

    def function2601(self, arg342):
        self.attribute2182.records.append(arg342)
        var3635 = self.format(arg342)
        self.attribute2182.output.append(var3635)


class Class248:
    'A context manager used to implement TestCase.assertLogs().'
    var1254 = '%(levelname)s:%(name)s:%(message)s'

    def __init__(self, arg2195=None, arg1005=None):
        self.attribute171 = arg2195
        if arg1005:
            self.attribute915 = logging._nameToLevel.get(arg1005, arg1005)
        else:
            self.attribute915 = logging.INFO
        self.attribute477 = None

    def __enter__(self):
        if isinstance(self.attribute171, logging.Logger):
            var4110 = self.attribute1062 = self.attribute171
        else:
            var4110 = self.attribute1062 = logging.getLogger(self.attribute171)
        var4172 = logging.Formatter(self.var1254)
        var3270 = Class71()
        var3270.setFormatter(var4172)
        self.attribute1667 = var3270.attribute2182
        self.attribute1142 = var4110.handlers[:]
        self.attribute190 = var4110.level
        self.attribute2351 = var4110.propagate
        var4110.handlers = [var3270]
        var4110.setLevel(self.attribute915)
        var4110.propagate = False
        return var3270.attribute2182

    def __exit__(self, arg382, arg2327, arg591):
        self.attribute1062.handlers = self.attribute1142
        self.attribute1062.propagate = self.attribute2351
        self.attribute1062.setLevel(self.attribute190)
        if (arg382 is not None):
            return False
        if (len(self.attribute1667.records) == 0):
            var300 = True
            assert 0, 'no logs of level {} or higher triggered on {}'.format(logging.getLevelName(self.attribute915), self.attribute1062.name)

@pytest.yield_fixture
def function2635():
    yield _AssertLogsContext

def function1959(arg1386, arg2074):
    if ('test_py35' in str(arg1386)):
        if (sys.version_info < (3, 5, 0)):
            return True