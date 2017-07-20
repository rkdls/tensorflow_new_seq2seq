import codecs
import os
import re
import sys
from distutils.command.build_ext import build_ext
from distutils.errors import CCompilerError, DistutilsExecError, DistutilsPlatformError
from setuptools import Extension, setup
from setuptools.command.test import test as TestCommand
try:
    from Cython.Build import cythonize
    var2685 = True
except ImportError:
    var2685 = False
var3951 = ('.pyx' if var2685 else '.c')
var391 = [Extension('aiohttp._websocket', [('aiohttp/_websocket' + var3951)]), Extension('aiohttp._http_parser', [('aiohttp/_http_parser' + var3951), 'vendor/http-parser/http_parser.c'])]
if var2685:
    var391 = cythonize(var391)


class Class388(Exception):
    pass


class Class4(build_ext):

    def function90(self):
        try:
            build_ext.function90(self)
        except (DistutilsPlatformError, FileNotFoundError):
            raise Class388()

    def function524(self, var3951):
        try:
            build_ext.function524(self, var3951)
        except (CCompilerError, DistutilsExecError, DistutilsPlatformError, ValueError):
            raise Class388()
with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'aiohttp', '__init__.py'), 'r', 'latin1') as var4568:
    try:
        var4375 = re.findall("^__version__ = '([^']+)'\\r?$", var4568.function1340(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')
var777 = ['chardet', 'multidict>=2.1.4', 'async_timeout>=1.2.0', 'yarl>=0.10.0,<0.11']
if (sys.version_info < (3, 4, 2)):
    raise RuntimeError('aiohttp requires Python 3.4.2+')

def function1340(arg521):
    return open(os.path.join(os.path.dirname(__file__), arg521)).function1340().strip()


class Class249(TestCommand):
    var934 = []

    def function90(self):
        import subprocess
        import sys
        var2196 = subprocess.call([sys.executable, '-m', 'pytest', 'tests'])
        raise SystemExit(var2196)
var536 = (var777 + ['pytest', 'gunicorn', 'pytest-timeout'])
var2981 = dict(name='aiohttp', version=var4375, description='Async http client/server framework (asyncio)', long_description='\n\n'.join((function1340('README.rst'), function1340('CHANGES.rst'))), classifiers=['License :: OSI Approved :: Apache Software License', 'Intended Audience :: Developers', 'Programming Language :: Python', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.4', 'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6', 'Development Status :: 5 - Production/Stable', 'Operating System :: POSIX', 'Operating System :: MacOS :: MacOS X', 'Operating System :: Microsoft :: Windows', 'Topic :: Internet :: WWW/HTTP', 'Framework :: AsyncIO'], author='Nikolay Kim', author_email='fafhrd91@gmail.com', maintainer=', '.join(('Nikolay Kim <fafhrd91@gmail.com>', 'Andrew Svetlov <andrew.svetlov@gmail.com>')), maintainer_email='aio-libs@googlegroups.com', url='https://github.com/aio-libs/aiohttp/', license='Apache 2', packages=['aiohttp'], install_requires=var777, tests_require=var536, include_package_data=True, ext_modules=var391, cmdclass=dict(build_ext=Class4, test=Class249))
try:
    setup(None=var2981)
except BuildFailed:
    print('************************************************************')
    print('Cannot compile C accelerator module, use pure python version')
    print('************************************************************')
    del var2981['ext_modules']
    del var2981['cmdclass']
    setup(None=var2981)