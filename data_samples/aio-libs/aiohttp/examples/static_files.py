import pathlib
from aiohttp import web
var3761 = web.Application()
var3761.router.add_static('/', pathlib.Path(__file__).parent, show_index=True)
web.run_app(var3761)