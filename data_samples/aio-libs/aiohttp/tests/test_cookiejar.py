import asyncio
import datetime
import os
import tempfile
import unittest
from unittest import mock
import pytest
from yarl import URL
from aiohttp import CookieJar
from aiohttp.helpers import SimpleCookie

@pytest.fixture
def function674():
    return SimpleCookie('shared-cookie=first; domain-cookie=second; Domain=example.com; subdomain1-cookie=third; Domain=test1.example.com; subdomain2-cookie=fourth; Domain=test2.example.com; dotted-domain-cookie=fifth; Domain=.example.com; different-domain-cookie=sixth; Domain=different.org; secure-cookie=seventh; Domain=secure.com; Secure; no-path-cookie=eighth; Domain=pathtest.com; path1-cookie=nineth; Domain=pathtest.com; Path=/; path2-cookie=tenth; Domain=pathtest.com; Path=/one; path3-cookie=eleventh; Domain=pathtest.com; Path=/one/two; path4-cookie=twelfth; Domain=pathtest.com; Path=/one/two/; expires-cookie=thirteenth; Domain=expirestest.com; Path=/; Expires=Tue, 1 Jan 1980 12:00:00 GMT; max-age-cookie=fourteenth; Domain=maxagetest.com; Path=/; Max-Age=60; invalid-max-age-cookie=fifteenth; Domain=invalid-values.com;  Max-Age=string; invalid-expires-cookie=sixteenth; Domain=invalid-values.com;  Expires=string;')

@pytest.fixture
def function1086():
    return SimpleCookie('unconstrained-cookie=first; Path=/; domain-cookie=second; Domain=example.com; Path=/; subdomain1-cookie=third; Domain=test1.example.com; Path=/; subdomain2-cookie=fourth; Domain=test2.example.com; Path=/; dotted-domain-cookie=fifth; Domain=.example.com; Path=/; different-domain-cookie=sixth; Domain=different.org; Path=/; no-path-cookie=seventh; Domain=pathtest.com; path-cookie=eighth; Domain=pathtest.com; Path=/somepath; wrong-path-cookie=nineth; Domain=pathtest.com; Path=somepath;')

def function1240():
    var19 = CookieJar._parse_date
    var2737 = datetime.timezone.var2737
    assert (var19('') is None)
    assert (var19('Tue, 1 Jan 70 00:00:00 GMT') == datetime.datetime(1970, 1, 1, tzinfo=var2737))
    assert (var19('Tue, 1 Jan 10 00:00:00 GMT') == datetime.datetime(2010, 1, 1, tzinfo=var2737))
    assert (var19('1 Jan 1970 00:00:00 GMT') == datetime.datetime(1970, 1, 1, tzinfo=var2737))
    assert (var19('Tue, 1 Jan 1970 00:00:00') == datetime.datetime(1970, 1, 1, tzinfo=var2737))
    assert (var19('Tue, 1 Jan 00:00:00 GMT') is None)
    assert (var19('Tue, 1 1970 00:00:00 GMT') is None)
    assert (var19('Tue, Jan 1970 00:00:00 GMT') is None)
    assert (var19('Tue, 1 Jan 1970 GMT') is None)
    assert (var19('Tue, 0 Jan 1970 00:00:00 GMT') is None)
    assert (var19('Tue, 1 Jan 1500 00:00:00 GMT') is None)
    assert (var19('Tue, 1 Jan 1970 77:88:99 GMT') is None)

def function152():
    var4678 = CookieJar._is_domain_match
    assert var4678('test.com', 'test.com')
    assert var4678('test.com', 'sub.test.com')
    assert (not var4678('test.com', ''))
    assert (not var4678('test.com', 'test.org'))
    assert (not var4678('diff-test.com', 'test.com'))
    assert (not var4678('test.com', 'diff-test.com'))
    assert (not var4678('test.com', '127.0.0.1'))

def function1717():
    var172 = CookieJar._is_path_match
    assert var172('/', '')
    assert var172('', '/')
    assert var172('/file', '')
    assert var172('/folder/file', '')
    assert var172('/', '/')
    assert var172('/file', '/')
    assert var172('/file', '/file')
    assert var172('/folder/', '/folder/')
    assert var172('/folder/', '/')
    assert var172('/folder/file', '/')
    assert (not var172('/', '/file'))
    assert (not var172('/', '/folder/'))
    assert (not var172('/file', '/folder/file'))
    assert (not var172('/folder/', '/folder/file'))
    assert (not var172('/different-file', '/file'))
    assert (not var172('/different-folder/', '/folder/'))

def function364(arg532, function674, function1086):
    var1201 = CookieJar(loop=arg532)
    var1201.update_cookies(function674)
    var3419 = SimpleCookie()
    for var3474 in var1201:
        dict.__setitem__(var3419, var3474.key, var3474)
    var3194 = function674
    assert (var3419 == var3194)
    assert (var1201._loop is arg532)

def function244(arg1826, function674, function1086):
    var2077 = (tempfile.mkdtemp() + '/aiohttp.test.cookie')
    var769 = CookieJar(loop=arg1826)
    var769.update_cookies(function1086)
    var769.save(file_path=var2077)
    var856 = CookieJar(loop=arg1826)
    var856.load(file_path=var2077)
    var2054 = SimpleCookie()
    for var3909 in var856:
        var2054[var3909.key] = var3909
    os.unlink(var2077)
    assert (var2054 == function1086)

def function1438(arg2129):
    var2175 = ('idna-domain-first=first; Domain=xn--9caa.com; Path=/;', 'idna-domain-second=second; Domain=xn--9caa.com; Path=/;')
    var1870 = CookieJar(loop=arg2129)
    var1870.update_cookies(SimpleCookie(var2175[0]), URL('http://éé.com/'))
    var1870.update_cookies(SimpleCookie(var2175[1]), URL('http://xn--9caa.com/'))
    var3895 = SimpleCookie()
    for var3162 in var1870:
        var3895[var3162.key] = var3162
    assert (var3895 == SimpleCookie(' '.join(var2175)))

def function1288(arg118):
    var1555 = CookieJar(loop=arg118)
    var1555.update_cookies(SimpleCookie('idna-domain-first=first; Domain=xn--9caa.com; Path=/; '))
    assert (len(var1555.filter_cookies(URL('http://éé.com'))) == 1)
    assert (len(var1555.filter_cookies(URL('http://xn--9caa.com'))) == 1)

def function1560(arg1174):
    asyncio.set_event_loop(arg1174)
    var311 = CookieJar()
    assert (var311._loop is arg1174)

def function761(arg2357):
    var1898 = CookieJar(loop=arg2357)
    var1347 = SimpleCookie('shared-cookie=first; domain-cookie=second; Domain=example.com; subdomain1-cookie=third; Domain=test1.example.com; subdomain2-cookie=fourth; Domain=test2.example.com; dotted-domain-cookie=fifth; Domain=.example.com; different-domain-cookie=sixth; Domain=different.org; secure-cookie=seventh; Domain=secure.com; Secure; no-path-cookie=eighth; Domain=pathtest.com; path1-cookie=nineth; Domain=pathtest.com; Path=/; path2-cookie=tenth; Domain=pathtest.com; Path=/one; path3-cookie=eleventh; Domain=pathtest.com; Path=/one/two; path4-cookie=twelfth; Domain=pathtest.com; Path=/one/two/; expires-cookie=thirteenth; Domain=expirestest.com; Path=/; Expires=Tue, 1 Jan 1980 12:00:00 GMT; max-age-cookie=fourteenth; Domain=maxagetest.com; Path=/; Max-Age=60; invalid-max-age-cookie=fifteenth; Domain=invalid-values.com;  Max-Age=string; invalid-expires-cookie=sixteenth; Domain=invalid-values.com;  Expires=string;')
    var1898.update_cookies(var1347)
    var25 = var1898.filter_cookies(URL('http://1.2.3.4/')).output(header='Cookie:')
    assert (var25 == 'Cookie: shared-cookie=first')

def function1435(arg924, function1086):
    var516 = CookieJar(loop=arg924)
    var516.update_cookies(function1086, URL('http://1.2.3.4/'))
    assert (len(var516) == 0)

def function895(arg1205):
    var807 = CookieJar(loop=arg1205, unsafe=True)
    var807.update_cookies(SimpleCookie('shared-cookie=first; ip-cookie=second; Domain=127.0.0.1;'))
    var1203 = var807.filter_cookies(URL('http://127.0.0.1/')).output(header='Cookie:')
    assert (var1203 == 'Cookie: ip-cookie=second\r\nCookie: shared-cookie=first')

def function2368(arg2126):
    var1128 = CookieJar(loop=arg2126, unsafe=True)
    var1128.update_cookies(SimpleCookie('ip-cookie="second"; Domain=127.0.0.1;'))
    var3020 = var1128.filter_cookies(URL('http://127.0.0.1/')).output(header='Cookie:')
    assert (var3020 == 'Cookie: ip-cookie="second"')

def function573(arg2211):
    var3415 = CookieJar(loop=arg2211, unsafe=True)
    var3415.update_cookies(SimpleCookie('cookie=val; Domain=example.com.;'), URL('http://www.example.com'))
    var1963 = var3415.filter_cookies(URL('http://www.example.com/'))
    assert (var1963.output(header='Cookie:') == 'Cookie: cookie=val')
    var1963 = var3415.filter_cookies(URL('http://example.com/'))
    assert (var1963.output(header='Cookie:') == '')


class Class134(unittest.TestCase):

    def function1020(self):
        self.attribute702 = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
        self.attribute762 = CookieJar(loop=self.attribute702)

    def function249(self):
        self.attribute702.close()

    def function1281(self, arg284):
        self.attribute762.update_cookies(self.function674)
        var1595 = self.attribute762.filter_cookies(URL(arg284))
        self.attribute762.clear()
        self.attribute762.update_cookies(self.function1086, URL(arg284))
        var3164 = SimpleCookie()
        for var3580 in self.attribute762:
            dict.__setitem__(var3164, var3580.key, var3580)
        self.attribute762.clear()
        return (var1595, var3164)


class Class109(Class134):

    def function829(self):
        super().function829()
        self.function674 = SimpleCookie('shared-cookie=first; domain-cookie=second; Domain=example.com; subdomain1-cookie=third; Domain=test1.example.com; subdomain2-cookie=fourth; Domain=test2.example.com; dotted-domain-cookie=fifth; Domain=.example.com; different-domain-cookie=sixth; Domain=different.org; secure-cookie=seventh; Domain=secure.com; Secure; no-path-cookie=eighth; Domain=pathtest.com; path1-cookie=nineth; Domain=pathtest.com; Path=/; path2-cookie=tenth; Domain=pathtest.com; Path=/one; path3-cookie=eleventh; Domain=pathtest.com; Path=/one/two; path4-cookie=twelfth; Domain=pathtest.com; Path=/one/two/; expires-cookie=thirteenth; Domain=expirestest.com; Path=/; Expires=Tue, 1 Jan 1980 12:00:00 GMT; max-age-cookie=fourteenth; Domain=maxagetest.com; Path=/; Max-Age=60; invalid-max-age-cookie=fifteenth; Domain=invalid-values.com;  Max-Age=string; invalid-expires-cookie=sixteenth; Domain=invalid-values.com;  Expires=string;')
        self.function1086 = SimpleCookie('unconstrained-cookie=first; Path=/; domain-cookie=second; Domain=example.com; Path=/; subdomain1-cookie=third; Domain=test1.example.com; Path=/; subdomain2-cookie=fourth; Domain=test2.example.com; Path=/; dotted-domain-cookie=fifth; Domain=.example.com; Path=/; different-domain-cookie=sixth; Domain=different.org; Path=/; no-path-cookie=seventh; Domain=pathtest.com; path-cookie=eighth; Domain=pathtest.com; Path=/somepath; wrong-path-cookie=nineth; Domain=pathtest.com; Path=somepath;')
        self.attribute684 = CookieJar(loop=self.attribute702)

    def function2308(self, arg1432, arg554, arg2376):
        with mock.patch.object(self.attribute702, 'time', return_value=arg554):
            self.attribute684.update_cookies(self.function674)
        with mock.patch.object(self.attribute702, 'time', return_value=arg2376):
            var1016 = self.attribute684.filter_cookies(URL(arg1432))
        self.attribute684.clear()
        return var1016

    def function1079(self):
        (var2086, var746) = self.function1281('http://example.com/')
        self.assertEqual(set(var2086.keys()), {'shared-cookie', 'domain-cookie', 'dotted-domain-cookie'})
        self.assertEqual(set(var746.keys()), {'unconstrained-cookie', 'domain-cookie', 'dotted-domain-cookie'})

    def function1904(self):
        (var2722, var4440) = self.function1281('http://test1.example.com/')
        self.assertEqual(set(var2722.keys()), {'shared-cookie', 'domain-cookie', 'subdomain1-cookie', 'dotted-domain-cookie'})
        self.assertEqual(set(var4440.keys()), {'unconstrained-cookie', 'domain-cookie', 'subdomain1-cookie', 'dotted-domain-cookie'})

    def function1154(self):
        (var1758, var4586) = self.function1281('http://different.example.com/')
        self.assertEqual(set(var1758.keys()), {'shared-cookie', 'domain-cookie', 'dotted-domain-cookie'})
        self.assertEqual(set(var4586.keys()), {'unconstrained-cookie', 'domain-cookie', 'dotted-domain-cookie'})

    def function41(self):
        (var1751, var2799) = self.function1281('http://different.org/')
        self.assertEqual(set(var1751.keys()), {'shared-cookie', 'different-domain-cookie'})
        self.assertEqual(set(var2799.keys()), {'unconstrained-cookie', 'different-domain-cookie'})

    def function1701(self):
        self.attribute684.update_cookies(self.function1086, URL('http://example.com/'))
        var4242 = self.attribute684.filter_cookies(URL('http://example.com/'))
        self.assertIn('unconstrained-cookie', set(var4242.keys()))
        var4242 = self.attribute684.filter_cookies(URL('http://different.org/'))
        self.assertNotIn('unconstrained-cookie', set(var4242.keys()))

    def function40(self):
        (var594, var1244) = self.function1281('http://secure.com/')
        self.assertEqual(set(var594.keys()), {'shared-cookie'})
        (var594, var1244) = self.function1281('https://secure.com/')
        self.assertEqual(set(var594.keys()), {'shared-cookie', 'secure-cookie'})

    def function1512(self):
        (var3624, var3414) = self.function1281('http://pathtest.com/')
        self.assertEqual(set(var3624.keys()), {'shared-cookie', 'no-path-cookie', 'path1-cookie'})

    def function2599(self):
        (var4506, var3655) = self.function1281('http://pathtest.com/one/')
        self.assertEqual(set(var4506.keys()), {'shared-cookie', 'no-path-cookie', 'path1-cookie', 'path2-cookie'})

    def function2738(self):
        (var3435, var2363) = self.function1281('http://pathtest.com/one/two')
        self.assertEqual(set(var3435.keys()), {'shared-cookie', 'no-path-cookie', 'path1-cookie', 'path2-cookie', 'path3-cookie'})

    def function422(self):
        (var705, var3858) = self.function1281('http://pathtest.com/one/two/')
        self.assertEqual(set(var705.keys()), {'shared-cookie', 'no-path-cookie', 'path1-cookie', 'path2-cookie', 'path3-cookie', 'path4-cookie'})

    def function2737(self):
        (var1973, var47) = self.function1281('http://pathtest.com/one/two/three/')
        self.assertEqual(set(var1973.keys()), {'shared-cookie', 'no-path-cookie', 'path1-cookie', 'path2-cookie', 'path3-cookie', 'path4-cookie'})

    def function2630(self):
        (var2559, var4088) = self.function1281('http://pathtest.com/hundred/')
        self.assertEqual(set(var2559.keys()), {'shared-cookie', 'no-path-cookie', 'path1-cookie'})

    def function1078(self):
        (var1919, var1124) = self.function1281('http://pathtest.com/')
        self.assertEqual(set(var1124.keys()), {'unconstrained-cookie', 'no-path-cookie', 'path-cookie', 'wrong-path-cookie'})
        self.assertEqual(var1124['no-path-cookie']['path'], '/')
        self.assertEqual(var1124['path-cookie']['path'], '/somepath')
        self.assertEqual(var1124['wrong-path-cookie']['path'], '/')

    def function571(self):
        var1472 = datetime.datetime(1975, 1, 1, tzinfo=datetime.timezone.utc).timestamp()
        var4091 = datetime.datetime(2115, 1, 1, tzinfo=datetime.timezone.utc).timestamp()
        var2731 = self.function2308('http://expirestest.com/', var1472, var1472)
        self.assertEqual(set(var2731.keys()), {'shared-cookie', 'expires-cookie'})
        var2731 = self.function2308('http://expirestest.com/', var1472, var4091)
        self.assertEqual(set(var2731.keys()), {'shared-cookie'})

    def function1280(self):
        var2264 = self.function2308('http://maxagetest.com/', 1000, 1000)
        self.assertEqual(set(var2264.keys()), {'shared-cookie', 'max-age-cookie'})
        var2264 = self.function2308('http://maxagetest.com/', 1000, 2000)
        self.assertEqual(set(var2264.keys()), {'shared-cookie'})

    def function1453(self):
        (var3134, var2649) = self.function1281('http://invalid-values.com/')
        self.assertEqual(set(var3134.keys()), {'shared-cookie', 'invalid-max-age-cookie', 'invalid-expires-cookie'})
        var706 = var3134['invalid-max-age-cookie']
        self.assertEqual(var706['max-age'], '')
        var706 = var3134['invalid-expires-cookie']
        self.assertEqual(var706['expires'], '')