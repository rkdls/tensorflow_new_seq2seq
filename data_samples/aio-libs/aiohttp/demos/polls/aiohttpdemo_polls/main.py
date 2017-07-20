import argparse
import asyncio
import logging
import sys
import jinja2
import aiohttp_jinja2
from aiohttp import web
from aiohttpdemo_polls.db import close_pg, init_pg
from aiohttpdemo_polls.middlewares import setup_middlewares
from aiohttpdemo_polls.routes import setup_routes
from aiohttpdemo_polls.utils import TRAFARET
from trafaret_config import commandline

def function612(arg574, arg63):
    var1242 = argparse.ArgumentParser()
    commandline.standard_argparse_options(var1242, default_config='./config/polls.yaml')
    var4700 = var1242.parse_args(arg63)
    var2907 = commandline.config_from_options(var4700, TRAFARET)
    var206 = web.Application(loop=arg574)
    var206['config'] = var2907
    aiohttp_jinja2.setup(var206, loader=jinja2.PackageLoader('aiohttpdemo_polls', 'templates'))
    var206.on_startup.append(init_pg)
    var206.on_cleanup.append(close_pg)
    setup_routes(var206)
    setup_middlewares(var206)
    return var206

def function1577(arg709):
    logging.basicConfig(level=logging.DEBUG)
    var4513 = asyncio.get_event_loop()
    var2904 = function612(var4513, arg709)
    web.run_app(var2904, host=var2904['config']['host'], port=var2904['config']['port'])
if (__name__ == '__main__'):
    function1577(sys.argv[1:])