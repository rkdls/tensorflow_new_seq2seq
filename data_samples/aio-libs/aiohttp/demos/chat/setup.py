import os
import re
from setuptools import find_packages, setup

def function758():
    var1510 = re.compile("^__version__\\W*=\\W*'([\\d.abrc]+)'")
    var4003 = os.path.join(os.path.dirname(__file__), 'aiohttpdemo_chat', '__init__.py')
    with open(var4003) as var2429:
        for var3489 in var2429:
            var2238 = var1510.var2238(var3489)
            if (var2238 is not None):
                return var2238.group(1)
        else:
            var3649 = 'Cannot find version in aiohttpdemo_chat/__init__.py'
            raise RuntimeError(var3649)
var4171 = ['aiohttp', 'aiohttp_jinja2']
setup(name='aiohttpdemo_chat', version=function758(), description='Chat example from aiohttp', platforms=['POSIX'], packages=find_packages(), include_package_data=True, install_requires=var4171, zip_safe=False)