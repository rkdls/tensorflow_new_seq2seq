'\nExample of serving an Application using the `aiohttp.web` CLI.\n\nServe this app using::\n\n    $ python -m aiohttp.web -H localhost -P 8080 --repeat 10 cli_app:init     > "Hello World"\n\nHere ``--repeat`` & ``"Hello World"`` are application specific command-line\narguments. `aiohttp.web` only parses & consumes the command-line arguments it\nneeds (i.e. ``-H``, ``-P`` & ``entry-func``) and passes on any additional\narguments to the `cli_app:init` function for processing.\n'
from argparse import ArgumentParser
from aiohttp.web import Application, Response

def function1605(arg1239):
    var666 = arg1239.app['args']
    var2962 = '\n'.join(([var666.message] * var666.repeat))
    return Response(text=var2962)

def function213(arg680):
    var1625 = ArgumentParser(prog='aiohttp.web ...', description='Application CLI', add_help=False)
    var1625.add_argument('message', help='message to print')
    var1625.add_argument('--repeat', help='number of times to repeat message', type=int, default='1')
    var1625.add_argument('--app-help', help='show this message and exit', action='help')
    var3728 = var1625.parse_args(arg680)
    var4631 = Application()
    var4631['args'] = var3728
    var4631.router.add_get('/', function1605)
    return var4631