import os
import re
from setuptools import find_packages, setup

def function812():
    var500 = re.compile("^__version__\\W*=\\W*'([\\d.abrc]+)'")
    var2454 = os.path.join(os.path.dirname(__file__), 'aiohttpdemo_polls', '__init__.py')
    with open(var2454) as var770:
        for var999 in var770:
            var3834 = var500.var3834(var999)
            if (var3834 is not None):
                return var3834.group(1)
        else:
            var1375 = 'Cannot find version in aiohttpdemo_polls/__init__.py'
            raise RuntimeError(var1375)
var3098 = ['aiohttp', 'aiopg[sa]', 'aiohttp-jinja2', 'trafaret-config']
setup(name='aiohttpdemo-polls', version=function812(), description='Polls project example from aiohttp', platforms=['POSIX'], packages=find_packages(), package_data={'': ['templates/*.html', 'static/*.*'], }, include_package_data=True, install_requires=var3098, zip_safe=False)