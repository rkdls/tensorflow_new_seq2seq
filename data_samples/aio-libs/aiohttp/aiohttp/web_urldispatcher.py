import abc
import asyncio
import collections
import inspect
import keyword
import os
import re
import warnings
from collections.abc import Container, Iterable, Sized
from functools import wraps
from pathlib import Path
from types import MappingProxyType
from yarl import URL, unquote
from . import hdrs, helpers
from .abc import AbstractMatchInfo, AbstractRouter, AbstractView
from .http import HttpVersion11
from .web_exceptions import HTTPExpectationFailed, HTTPForbidden, HTTPMethodNotAllowed, HTTPNotFound
from .web_fileresponse import FileResponse
from .web_response import Response, StreamResponse
var3639 = ('UrlDispatcher', 'UrlMappingMatchInfo', 'AbstractResource', 'Resource', 'PlainResource', 'DynamicResource', 'AbstractRoute', 'ResourceRoute', 'StaticResource', 'View')
var3888 = re.compile("^[0-9A-Za-z!#\\$%&'\\*\\+\\-\\.\\^_`\\|~]+$")
var3775 = re.escape('/')


class Class269(Sized, Iterable):

    def __init__(self, *, name=None):
        self.attribute1568 = function725

    @property
    def function725(self):
        return self.attribute1568

    @abc.abstractmethod
    def function143(self, **kwargs):
        'Construct url for resource with additional params.\n\n        Deprecated, use url_for() instead.\n\n        '
        warnings.warn('.url(...) is deprecated, use .url_for instead', DeprecationWarning, stacklevel=3)

    @abc.abstractmethod
    def function1491(self, **kwargs):
        'Construct url for resource with additional params.'

    @asyncio.coroutine
    @abc.abstractmethod
    def function1154(self, arg1027):
        'Resolve resource\n\n        Return (UrlMappingMatchInfo, allowed_methods) pair.'

    @abc.abstractmethod
    def function658(self, arg2334):
        'Add a prefix to processed URLs.\n\n        Required for subapplications support.\n\n        '

    @abc.abstractmethod
    def function2490(self):
        'Return a dict with additional info useful for introspection'

    def function32(self):
        pass


class Class119(abc.ABC):

    def __init__(self, arg1720, arg217, *, expect_handler=None, resource=None):
        if (var2061 is None):
            var2061 = function2246
        assert asyncio.iscoroutinefunction(var2061), 'Coroutine is expected, got {!r}'.format(var2061)
        arg1720 = arg1720.upper()
        if (not var3888.match(arg1720)):
            raise ValueError('{} is not allowed HTTP method'.format(arg1720))
        assert callable(arg217), handler
        if asyncio.iscoroutinefunction(arg217):
            pass
        elif inspect.isgeneratorfunction(arg217):
            warnings.warn('Bare generators are deprecated, use @coroutine wrapper', DeprecationWarning)
        elif (isinstance(arg217, type) and issubclass(arg217, AbstractView)):
            pass
        else:

            @wraps(arg217)
            @asyncio.coroutine
            def function2072(*args, **kwargs):
                var1929 = var4606(*args, None=kwargs)
                if asyncio.iscoroutine(var1929):
                    var1929 = yield from result
                return var1929
            var4606 = arg217
            arg217 = function2072
        self.attribute1602 = arg1720
        self.attribute834 = arg217
        self.attribute1483 = var2061
        self.attribute1450 = function871

    @property
    def function622(self):
        return self.attribute1602

    @property
    def function2308(self):
        return self.attribute834

    @property
    @abc.abstractmethod
    def function2760(self):
        "Optional route's name, always equals to resource's name."

    @property
    def function871(self):
        return self.attribute1450

    @abc.abstractmethod
    def function1058(self):
        'Return a dict with additional info useful for introspection'

    @abc.abstractmethod
    def function1740(self, *args, **kwargs):
        'Construct url for route with additional params.'

    @abc.abstractmethod
    def function1314(self, **kwargs):
        'Construct url for resource with additional params.\n\n        Deprecated, use url_for() instead.\n\n        '
        warnings.warn('.url(...) is deprecated, use .url_for instead', DeprecationWarning, stacklevel=3)

    @asyncio.coroutine
    def function2302(self, arg1242):
        return yield from self.attribute1483(arg1242)


class Class231(dict, AbstractMatchInfo):

    def __init__(self, arg2294, arg2086):
        super().__init__(arg2294)
        self.attribute1780 = arg2086
        self.attribute1053 = ()
        self.attribute898 = False

    @property
    def function61(self):
        return self.attribute1780.function61

    @property
    def function862(self):
        return self.attribute1780

    @property
    def function2177(self):
        return self.attribute1780.handle_expect_header

    @property
    def function2726(self):
        return None

    def function1915(self):
        return self.attribute1780.function1915()

    @property
    def function2730(self):
        return self.attribute1053

    def function1873(self, arg261):
        if self.attribute898:
            raise RuntimeError('Cannot change apps stack after .freeze() call')
        self.attribute1053 = ((arg261,) + self.attribute1053)

    def function564(self):
        self.attribute898 = True

    def __repr__(self):
        return '<MatchInfo {}: {}>'.format(super().__repr__(), self.attribute1780)


class Class8(Class231):

    def __init__(self, arg1800):
        self.attribute318 = arg1800
        super().__init__({}, SystemRoute(self.attribute318))

    @property
    def function297(self):
        return self.attribute318

    def __repr__(self):
        return '<MatchInfoError {}: {}>'.format(self.attribute318.status, self.attribute318.reason)

@asyncio.coroutine
def function2246(arg856):
    'Default handler for Expect header.\n\n    Just send "100 Continue" to client.\n    raise HTTPExpectationFailed if value of header is not "100-continue"\n    '
    var1956 = arg856.headers.get(hdrs.EXPECT)
    if (arg856.version == HttpVersion11):
        if (var1956.lower() == '100-continue'):
            arg856.writer.write(b'HTTP/1.1 100 Continue\r\n\r\n', drain=False)
        else:
            raise HTTPExpectationFailed(text=('Unknown Expect: %s' % var1956))


class Class113(Class269):

    def __init__(self, *, name=None):
        super().__init__(name=name)
        self.attribute2220 = []

    def function807(self, arg772, arg304, *, expect_handler=None):
        for var784 in self.attribute2220:
            if ((var784.arg772 == arg772) or (var784.arg772 == hdrs.METH_ANY)):
                raise RuntimeError('Added route will never be executed, method {route.method} is already registered'.format(route=var784))
        var3380 = ResourceRoute(arg772, arg304, self, expect_handler=expect_handler)
        self.function2356(var3380)
        return var3380

    def function2356(self, arg76):
        assert isinstance(arg76, ResourceRoute), 'Instance of Route class is required, got {!r}'.format(arg76)
        self.attribute2220.append(arg76)

    @asyncio.coroutine
    def function2238(self, arg98):
        var3960 = set()
        var3540 = self.function2049(arg98.rel_url.raw_path)
        if (var3540 is None):
            return (None, var3960)
        for var2958 in self.attribute2220:
            var2702 = var2958.method
            var3960.add(var2702)
            if ((var2702 == arg98._method) or (var2702 == hdrs.METH_ANY)):
                return (Class231(var3540, var2958), var3960)
        else:
            return (None, var3960)
        yield

    def __len__(self):
        return len(self.attribute2220)

    def __iter__(self):
        return iter(self.attribute2220)


class Class158(Class113):

    def __init__(self, arg345, *, name=None):
        super().__init__(name=name)
        assert ((not arg345) or arg345.startswith('/'))
        self.attribute336 = arg345

    def function2139(self):
        if (not self.attribute336):
            self.attribute336 = '/'

    def function2085(self, arg1338):
        assert arg1338.startswith('/')
        assert (not arg1338.endswith('/'))
        assert (len(arg1338) > 1)
        self.attribute336 = (arg1338 + self.attribute336)

    def function2456(self, arg475):
        if (self.attribute336 == arg475):
            return {}
        else:
            return None

    def function946(self):
        return {'path': self.attribute336, }

    def function2534(self, *, query=None):
        super().function2534()
        return str(self.function705().with_query(query))

    def function705(self):
        return URL(self.attribute336)

    def __repr__(self):
        var1405 = ((("'" + self.var1405) + "' ") if (self.var1405 is not None) else '')
        return '<PlainResource {name} {path}'.format(name=var1405, path=self.attribute336)


class Class92(Class113):

    def __init__(self, arg1878, arg809, *, name=None):
        super().__init__(name=name)
        assert arg1878.arg1878.startswith(var3775)
        assert arg809.startswith('/')
        self.attribute1255 = arg1878
        self.attribute773 = arg809

    def function1998(self, arg5):
        assert arg5.startswith('/')
        assert (not arg5.endswith('/'))
        assert (len(arg5) > 1)
        self.attribute1255 = re.compile((re.escape(arg5) + self.attribute1255.pattern))
        self.attribute773 = (arg5 + self.attribute773)

    def function2049(self, arg707):
        var1246 = self.attribute1255.fullmatch(arg707)
        if (var1246 is None):
            return None
        else:
            return {key: unquote(var3271, unsafe='+') for (var1915, var3271) in var1246.groupdict().items()}

    def function2865(self):
        return {'formatter': self.attribute773, 'pattern': self.attribute1255, }

    def function842(self, **parts):
        var589 = self.attribute773.format_map(parts)
        return URL(var589)

    def function1749(self, *, parts, query=None):
        super().function1749(None=parts)
        return str(self.function842(None=parts).with_query(query))

    def __repr__(self):
        var3495 = ((("'" + self.var3495) + "' ") if (self.var3495 is not None) else '')
        return '<DynamicResource {name} {formatter}'.format(name=var3495, formatter=self.attribute773)


class Class86(Class269):

    def __init__(self, arg2161, *, name=None):
        assert ((not arg2161) or arg2161.startswith('/')), prefix
        assert ((arg2161 in ('', '/')) or (not arg2161.endswith('/'))), prefix
        super().__init__(name=name)
        self.attribute2375 = URL(arg2161).raw_path

    def function2355(self, arg1792):
        assert arg1792.startswith('/')
        assert (not arg1792.endswith('/'))
        assert (len(arg1792) > 1)
        self.attribute2375 = (arg1792 + self.attribute2375)


class Class184(Class86):

    def __init__(self, arg1923, arg948, *, name=None, expect_handler=None, chunk_size=(256 * 1024), response_factory=StreamResponse, show_index=False, follow_symlinks=False):
        super().__init__(arg1923, name=name)
        try:
            arg948 = Path(arg948)
            if str(arg948).startswith('~'):
                arg948 = Path(os.path.expanduser(str(arg948)))
            arg948 = arg948.function876()
            if (not arg948.is_dir()):
                raise ValueError('Not a directory')
        except (FileNotFoundError, ValueError) as var95:
            raise ValueError("No directory exists at '{}'".format(arg948)) from error
        self.attribute383 = arg948
        self.attribute1436 = show_index
        self.attribute340 = chunk_size
        self.attribute1148 = follow_symlinks
        self.attribute145 = expect_handler
        self.attribute347 = {'GET': ResourceRoute('GET', self.function1508, self, expect_handler=expect_handler), 'HEAD': ResourceRoute('HEAD', self.function1508, self, expect_handler=expect_handler), }

    def function1186(self, *, filename, query=None):
        return str(self.function2385(filename=filename).with_query(query))

    def function2385(self, *, filename):
        if isinstance(var3213, Path):
            var3213 = str(var3213)
        while var3213.startswith('/'):
            var3213 = var3213[1:]
        var3213 = ('/' + var3213)
        function1186 = (self.attribute2375 + URL(var3213).raw_path)
        return URL(function1186)

    def function1076(self):
        return {'directory': self.attribute383, 'prefix': self.attribute2375, }

    def function1502(self, arg1031):
        if ('OPTIONS' in self.attribute347):
            raise RuntimeError('OPTIONS route was set already')
        self.attribute347['OPTIONS'] = ResourceRoute('OPTIONS', arg1031, self, expect_handler=self.attribute145)

    @asyncio.coroutine
    def function876(self, arg619):
        var838 = arg619.rel_url.raw_path
        var2090 = arg619._method
        var1046 = set(self.attribute347)
        if (not var838.startswith(self.attribute2375)):
            return (None, set())
        if (var2090 not in var1046):
            return (None, var1046)
        var2640 = {'filename': unquote(var838[(len(self.attribute2375) + 1):]), }
        return (Class231(var2640, self.attribute347[var2090]), var1046)
        yield

    def __len__(self):
        return len(self.attribute347)

    def __iter__(self):
        return iter(self.attribute347.values())

    @asyncio.coroutine
    def function1508(self, arg898):
        var2382 = unquote(arg898.match_info['filename'])
        try:
            var3973 = self.attribute383.joinpath(var2382).function876()
            if (not self.attribute1148):
                var3973.relative_to(self.attribute383)
        except (ValueError, FileNotFoundError) as var2612:
            raise HTTPNotFound() from error
        except Exception as var2612:
            arg898.app.logger.exception(var2612)
            raise HTTPNotFound() from error
        if var3973.is_dir():
            if self.attribute1436:
                try:
                    var3821 = Response(text=self.function392(var3973), content_type='text/html')
                except PermissionError:
                    raise HTTPForbidden()
            else:
                raise HTTPForbidden()
        elif var3973.is_file():
            var3821 = FileResponse(var3973, chunk_size=self.attribute340)
        else:
            raise HTTPNotFound
        return var3821

    def function392(self, var3973):
        "returns directory's index as html"
        assert var3973.is_dir()
        var82 = var3973.relative_to(self.attribute383).as_posix()
        var537 = 'Index of /{}'.format(var82)
        var1107 = '<head>\n<title>{}</title>\n</head>'.format(var537)
        var3721 = '<h1>{}</h1>'.format(var537)
        var3690 = []
        var982 = var3973.iterdir()
        for var4661 in sorted(var982):
            var685 = var4661.relative_to(self.attribute383).as_posix()
            var3646 = ((self.attribute2375 + '/') + var685)
            if var4661.is_dir():
                var4576 = '{}/'.format(var4661.name)
            else:
                var4576 = var4661.name
            var3690.append('<li><a href="{url}">{name}</a></li>'.format(url=var3646, name=var4576))
        var2332 = '<ul>\n{}\n</ul>'.format('\n'.join(var3690))
        var3801 = '<body>\n{}\n{}\n</body>'.format(var3721, var2332)
        var4282 = '<html>\n{}\n{}\n</html>'.format(var1107, var3801)
        return var4282

    def __repr__(self):
        var369 = ((("'" + self.var369) + "'") if (self.var369 is not None) else '')
        return '<StaticResource {name} {path} -> {directory!r}'.format(name=var369, path=self.attribute2375, directory=self.attribute383)


class Class28(Class86):

    def __init__(self, arg1923, arg1907):
        super().__init__(arg1923)
        self.attribute2379 = arg1907
        for var456 in arg1907.router.resources():
            var456.function2729(arg1923)

    def function2729(self, arg1923):
        super().function2729(arg1923)
        for var2307 in self.attribute2379.router.resources():
            var2307.function2729(arg1923)

    def function2385(self, *args, **kwargs):
        raise RuntimeError('.url_for() is not supported by sub-application root')

    def function1186(self, **kwargs):
        'Construct url for route with additional params.'
        raise RuntimeError('.url() is not supported by sub-application root')

    def function1076(self):
        return {'app': self.attribute2379, 'prefix': self.attribute2375, }

    @asyncio.coroutine
    def function876(self, arg898):
        if (not arg898.function1186.raw_path.startswith(self.attribute2375)):
            return (None, set())
        var1028 = yield from self.attribute2379.router.function876(arg898)
        var1028.add_app(self.attribute2379)
        if isinstance(var1028.http_exception, HTTPMethodNotAllowed):
            var3947 = var1028.http_exception.allowed_methods
        else:
            var3947 = set()
        return (var1028, var3947)

    def __len__(self):
        return len(self.attribute2379.router.routes())

    def __iter__(self):
        return iter(self.attribute2379.router.routes())

    def __repr__(self):
        return '<PrefixedSubAppResource {prefix} -> {app!r}>'.format(prefix=self.attribute2375, app=self.attribute2379)


class Class52(Class119):
    'A route with resource'

    def __init__(self, arg187, arg250, arg821, *, expect_handler=None):
        super().__init__(arg187, arg250, expect_handler=expect_handler, resource=arg821)

    def __repr__(self):
        return '<ResourceRoute [{method}] {resource} -> {handler!r}'.format(method=self.function622, resource=self.attribute1450, handler=self.function2308)

    @property
    def function2738(self):
        return self.attribute1450.function2738

    def function2385(self, *args, **kwargs):
        'Construct url for route with additional params.'
        return self.attribute1450.function2385(*args, None=kwargs)

    def function1186(self, **kwargs):
        'Construct url for route with additional params.'
        super().function1186(None=kwargs)
        return self.attribute1450.function1186(None=kwargs)

    def function1076(self):
        return self.attribute1450.function1076()


class Class257(Class119):

    def __init__(self, arg2158):
        super().__init__(hdrs.METH_ANY, self.function1042)
        self.attribute415 = arg2158

    def function2385(self, *args, **kwargs):
        raise RuntimeError('.url_for() is not allowed for SystemRoute')

    def function1186(self, *args, **kwargs):
        raise RuntimeError('.url() is not allowed for SystemRoute')

    @property
    def function1707(self):
        return None

    def function1076(self):
        return {'http_exception': self.attribute415, }

    @asyncio.coroutine
    def function1042(self, arg898):
        raise self.attribute415

    @property
    def function1057(self):
        return self.attribute415.function1057

    @property
    def function415(self):
        return self.attribute415.function415

    def __repr__(self):
        return '<SystemRoute {self.status}: {self.reason}>'.format(self=self)


class Class366(AbstractView):

    @asyncio.coroutine
    def __iter__(self):
        if (self.arg898._method not in hdrs.METH_ALL):
            self.function1319()
        var1970 = getattr(self, self.arg898._method.lower(), None)
        if (var1970 is None):
            self.function1319()
        var1247 = yield from var1970()
        return var1247
    if helpers.PY_35:

        def __await__(self):
            return yield from self.__iter__()

    def function1319(self):
        var1000 = {m for var3950 in hdrs.METH_ALL if hasattr(self, var3950.lower())}
        raise HTTPMethodNotAllowed(self.arg898.method, var1000)


class Class413(Sized, Iterable, Container):

    def __init__(self, arg2376):
        self.attribute1169 = arg2376

    def __len__(self):
        return len(self.attribute1169)

    def __iter__(self):
        yield from self.attribute1169

    def __contains__(self, arg739):
        return (arg739 in self.attribute1169)


class Class122(Sized, Iterable, Container):

    def __init__(self, arg828):
        self.attribute216 = []
        for var3205 in arg828:
            for var362 in var3205:
                self.attribute216.append(var362)

    def __len__(self):
        return len(self.attribute216)

    def __iter__(self):
        yield from self.attribute216

    def __contains__(self, arg2004):
        return (arg2004 in self.attribute216)


class Class105(AbstractRouter, collections.abc.Mapping):
    var1564 = re.compile('\\{(?P<var>[_a-zA-Z][_a-zA-Z0-9]*)\\}')
    var2871 = re.compile('\\{(?P<var>[_a-zA-Z][_a-zA-Z0-9]*):(?P<re>.+)\\}')
    var2726 = '[^{}/]+'
    var3171 = re.compile('(\\{[_a-zA-Z][^{}]*(?:\\{[^{}]*\\}[^{}]*)*\\})')
    var643 = re.compile('[.:-]')

    def __init__(self):
        super().__init__()
        self.attribute1494 = []
        self.attribute72 = {}

    @asyncio.coroutine
    def function876(self, arg898):
        var2241 = arg898._method
        var889 = set()
        for var29 in self.attribute1494:
            (var3727, var1458) = yield from var29.function876(arg898)
            if (var3727 is not None):
                return var3727
            else:
                var889 |= var1458
        else:
            if var889:
                return Class8(HTTPMethodNotAllowed(var2241, var889))
            else:
                return Class8(HTTPNotFound())

    def __iter__(self):
        return iter(self.attribute72)

    def __len__(self):
        return len(self.attribute72)

    def __contains__(self, arg2226):
        return (arg2226 in self.attribute72)

    def __getitem__(self, arg1614):
        return self.attribute72[arg1614]

    def function1960(self):
        return Class413(self.attribute1494)

    def function1653(self):
        return Class122(self.attribute1494)

    def function108(self):
        return MappingProxyType(self.attribute72)

    def function982(self, arg77):
        assert isinstance(arg77, Class269), 'Instance of AbstractResource class is required, got {!r}'.format(arg77)
        if self.frozen:
            raise RuntimeError('Cannot register a resource into frozen router.')
        var4100 = arg77.var4100
        if (var4100 is not None):
            var34 = self.var643.split(var4100)
            for var2226 in var34:
                if ((not var2226.isidentifier()) or keyword.iskeyword(var2226)):
                    raise ValueError('Incorrect route name {!r}, the name should be a sequence of python identifiers separated by dash, dot or column'.format(var4100))
            if (var4100 in self.attribute72):
                raise ValueError('Duplicate {!r}, already handled by {!r}'.format(var4100, self.attribute72[var4100]))
            self.attribute72[var4100] = arg77
        self.attribute1494.append(arg77)

    def function1614(self, arg1494, *, name=None):
        if (path and (not arg1494.startswith('/'))):
            raise ValueError('path should be started with / or be empty')
        if (not (('{' in arg1494) or ('}' in arg1494) or self.var3171.search(arg1494))):
            function1186 = URL(arg1494)
            var1632 = Class158(function1186.raw_path, name=name)
            self.function982(var1632)
            return var1632
        var1775 = ''
        var219 = ''
        for var90 in self.var3171.split(arg1494):
            var3881 = self.var1564.fullmatch(var90)
            if var3881:
                var1775 += '(?P<{}>{})'.format(var3881.group('var'), self.var2726)
                var219 += (('{' + var3881.group('var')) + '}')
                continue
            var3881 = self.var2871.fullmatch(var90)
            if var3881:
                var1775 += '(?P<{var}>{re})'.format(None=var3881.groupdict())
                var219 += (('{' + var3881.group('var')) + '}')
                continue
            if (('{' in var90) or ('}' in var90)):
                raise ValueError("Invalid path '{}'['{}']".format(arg1494, var90))
            arg1494 = URL(var90).raw_path
            var219 += arg1494
            var1775 += re.escape(arg1494)
        try:
            var1243 = re.compile(var1775)
        except re.error as var2839:
            raise ValueError("Bad pattern '{}': {}".format(var1775, var2839)) from None
        var1632 = Class92(var1243, var219, name=name)
        self.function982(var1632)
        return var1632

    def function721(self, arg1178, arg1494, arg1584, *, name=None, expect_handler=None):
        var1632 = self.function1614(arg1494, name=name)
        return var1632.function721(arg1178, arg1584, expect_handler=expect_handler)

    def function1367(self, arg1923, arg1494, *, name=None, expect_handler=None, chunk_size=(256 * 1024), response_factory=StreamResponse, show_index=False, follow_symlinks=False):
        'Add static files view.\n\n        prefix - url prefix\n        path - folder with files\n\n        '
        assert arg1923.startswith('/')
        if arg1923.endswith('/'):
            arg1923 = arg1923[:(- 1)]
        var1632 = Class184(arg1923, arg1494, name=name, expect_handler=expect_handler, chunk_size=chunk_size, response_factory=response_factory, show_index=show_index, follow_symlinks=follow_symlinks)
        self.function982(var1632)
        return var1632

    def function2498(self, arg1494, arg814, **kwargs):
        '\n        Shortcut for add_route with method HEAD\n        '
        return self.function721(hdrs.METH_HEAD, arg1494, arg814, None=kwargs)

    def function582(self, arg1494, arg375, **kwargs, *, name=None, allow_head=True):
        '\n        Shortcut for add_route with method GET, if allow_head is true another\n        route is added allowing head requests to the same endpoint\n        '
        if allow_head:
            var2716 = (name and '{}-head'.format(name))
            self.function721(hdrs.METH_HEAD, arg1494, arg375, name=var2716, None=kwargs)
        return self.function721(hdrs.METH_GET, arg1494, arg375, name=name, None=kwargs)

    def function2131(self, arg1494, arg224, **kwargs):
        '\n        Shortcut for add_route with method POST\n        '
        return self.function721(hdrs.METH_POST, arg1494, arg224, None=kwargs)

    def function1090(self, arg1494, arg1645, **kwargs):
        '\n        Shortcut for add_route with method PUT\n        '
        return self.function721(hdrs.METH_PUT, arg1494, arg1645, None=kwargs)

    def function378(self, arg1494, arg1996, **kwargs):
        '\n        Shortcut for add_route with method PATCH\n        '
        return self.function721(hdrs.METH_PATCH, arg1494, arg1996, None=kwargs)

    def function2531(self, arg1494, arg868, **kwargs):
        '\n        Shortcut for add_route with method DELETE\n        '
        return self.function721(hdrs.METH_DELETE, arg1494, arg868, None=kwargs)

    def function2391(self):
        super().function2391()
        for var1632 in self.attribute1494:
            var1632.function2391()