import asyncio
import re
from aiohttp.web_exceptions import HTTPMovedPermanently
from aiohttp.web_urldispatcher import SystemRoute
var3209 = ('normalize_path_middleware',)

@asyncio.coroutine
def function1582(arg2352, arg707):
    var1038 = arg2352.clone(rel_url=arg707)
    var4160 = yield from arg2352.app.router.resolve(var1038)
    var1038._match_info = var4160
    if (not isinstance(var4160.route, SystemRoute)):
        return (True, var1038)
    return (False, arg2352)

def function2428(*, append_slash=True, merge_slashes=True, redirect_class=HTTPMovedPermanently):
    '\n    Middleware that normalizes the path of a request. By normalizing\n    it means:\n\n        - Add a trailing slash to the path.\n        - Double slashes are replaced by one.\n\n    The middleware returns as soon as it finds a path that resolves\n    correctly. The order if all enable is 1) merge_slashes, 2) append_slash\n    and 3) both merge_slashes and append_slash. If the path resolves with\n    at least one of those conditions, it will redirect to the new path.\n\n    If append_slash is True append slash when needed. If a resource is\n    defined with trailing slash and the request comes without it, it will\n    append it automatically.\n\n    If merge_slashes is True, merge multiple consecutive slashes in the\n    path into one.\n    '

    @asyncio.coroutine
    def function1901(arg572, arg1475):

        @asyncio.coroutine
        def function2817(arg834):
            if isinstance(arg834.match_info.route, SystemRoute):
                var90 = []
                var1445 = arg834.raw_path
                if merge_slashes:
                    var90.append(re.sub('//+', '/', var1445))
                if (append_slash and (not arg834.var1445.endswith('/'))):
                    var90.append((var1445 + '/'))
                if (merge_slashes and append_slash):
                    var90.append(re.sub('//+', '/', (var1445 + '/')))
                for var1445 in var90:
                    (var4005, arg834) = yield from function1582(arg834, var1445)
                    if var4005:
                        return redirect_class(arg834.var1445)
            return yield from arg1475(arg834)
        return function2817
    return function1901