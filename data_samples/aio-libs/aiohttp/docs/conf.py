import sys
import os
import codecs
import re
var1061 = os.path.dirname(__file__)
var1783 = os.path.abspath(os.path.join(var1061, '..', 'aiohttp', '__init__.py'))
with codecs.open(var1783, 'r', 'latin1') as var3460:
    try:
        var4638 = re.search("^__version__ = '(?P<major>\\d+)\\.(?P<minor>\\d+)\\.(?P<patch>\\d+)(?P<tag>.*)?'$", var3460.read(), re.M).groupdict()
    except IndexError:
        raise RuntimeError('Unable to determine version.')
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))
var4208 = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.intersphinx', 'alabaster', 'sphinxcontrib.asyncio', 'sphinxcontrib.newsfeed']
try:
    import sphinxcontrib.spelling
    var4208.append('sphinxcontrib.spelling')
except ImportError:
    pass
var1618 = {'python': ('http://docs.python.org/3', None), 'multidict': ('https://multidict.readthedocs.io/en/stable/', None), 'yarl': ('https://yarl.readthedocs.io/en/stable/', None), 'aiohttpjinja2': ('https://aiohttp-jinja2.readthedocs.io/en/stable/', None), 'aiohttpsession': ('https://aiohttp-session.readthedocs.io/en/stable/', None), }
var4225 = ['_templates']
var4134 = '.rst'
var1952 = 'index'
var3496 = 'aiohttp'
var295 = '2013-2017, Aiohttp contributors'
var1134 = '{major}.{minor}'.format(None=var4638)
var2426 = '{major}.{minor}.{patch}-{tag}'.format(None=var4638)
var1431 = ['_build']
var4195 = 'sphinx'
var2500 = 'python3'
var403 = 'alabaster'
var3849 = {'logo': 'aiohttp-icon-128x128.png', 'description': 'http client/server for asyncio', 'github_user': 'aio-libs', 'github_repo': 'aiohttp', 'github_button': True, 'github_type': 'star', 'github_banner': True, 'travis_button': True, 'codecov_button': True, 'pre_bg': '#FFF6E5', 'note_bg': '#E5ECD1', 'note_border': '#BFCF8C', 'body_text': '#482C0A', 'sidebar_text': '#49443E', 'sidebar_header': '#4B4032', }
var2734 = 'aiohttp-icon.ico'
var68 = ['_static']
var1540 = {'**': ['about.html', 'navigation.html', 'searchbox.html'], }
var2686 = 'aiohttpdoc'
var2592 = {}
var1446 = [('index', 'aiohttp.tex', 'aiohttp Documentation', 'aiohttp contributors', 'manual')]
var2318 = [('index', 'aiohttp', 'aiohttp Documentation', ['aiohttp'], 1)]
var127 = [('index', 'aiohttp', 'aiohttp Documentation', 'Aiohttp contributors', 'aiohttp', 'One line description of project.', 'Miscellaneous')]
var3373 = 'aiohttp'