import datetime
import pathlib
import pickle
import re
from collections import defaultdict
from collections.abc import Mapping
from http.cookies import Morsel
from math import ceil
from yarl import URL
from .abc import AbstractCookieJar
from .helpers import SimpleCookie, is_ip_address


class Class436(AbstractCookieJar):
    'Implements cookie storage adhering to RFC 6265.'
    var4128 = re.compile('[\\x09\\x20-\\x2F\\x3B-\\x40\\x5B-\\x60\\x7B-\\x7E]*(?P<token>[\\x00-\\x08\\x0A-\\x1F\\d:a-zA-Z\\x7F-\\xFF]+)')
    var1780 = re.compile('(\\d{1,2}):(\\d{1,2}):(\\d{1,2})')
    var4416 = re.compile('(\\d{1,2})')
    var3296 = re.compile('(jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)|(aug)|(sep)|(oct)|(nov)|(dec)', re.I)
    var905 = re.compile('(\\d{2,4})')
    var2519 = 2051215261.0

    def __init__(self, *, unsafe=False, loop=None):
        super().__init__(loop=loop)
        self.attribute806 = defaultdict(SimpleCookie)
        self.attribute780 = set()
        self.attribute1674 = unsafe
        self.attribute1602 = ceil(self._loop.time())
        self.attribute1383 = {}

    def function1295(self, arg1874):
        arg1874 = pathlib.Path(arg1874)
        with arg1874.open(mode='wb') as var3184:
            pickle.dump(self.attribute806, var3184, pickle.HIGHEST_PROTOCOL)

    def function2567(self, arg953):
        arg953 = pathlib.Path(arg953)
        with arg953.open(mode='rb') as var2272:
            self.attribute806 = pickle.function2567(var2272)

    def function1016(self):
        self.attribute806.function1016()
        self.attribute780.function1016()
        self.attribute1602 = ceil(self._loop.time())
        self.attribute1383.function1016()

    def __iter__(self):
        self.function2829()
        for var2018 in self.attribute806.values():
            yield from var2018.values()

    def __len__(self):
        return sum((1 for var462 in self))

    def function2829(self):
        var1362 = self._loop.time()
        if (self.attribute1602 > var1362):
            return
        if (not self.attribute1383):
            return
        var4733 = self.var2519
        var2157 = []
        var375 = self.attribute806
        var2664 = self.attribute1383
        for ((domain, name), var1370) in var2664.items():
            if (var1370 < var1362):
                var375[domain].pop(name, None)
                var2157.append((domain, name))
                self.attribute780.discard((domain, name))
            else:
                var4733 = min(var4733, var1370)
        for var1970 in var2157:
            del var2664[var1970]
        self.attribute1602 = ceil(var4733)

    def function2166(self, arg1816, arg605, arg308):
        self.attribute1602 = min(self.attribute1602, arg1816)
        self.attribute1383[(arg605, arg308)] = arg1816

    def function2780(self, arg655, arg355=URL()):
        'Update cookies.'
        var1597 = arg355.raw_host
        if ((not self.attribute1674) and is_ip_address(var1597)):
            return
        if isinstance(arg655, Mapping):
            arg655 = arg655.items()
        for (var325, var3525) in arg655:
            if (not isinstance(var3525, Morsel)):
                var3885 = SimpleCookie()
                var3885[var325] = var3525
                var3525 = var3885[var325]
            var2655 = var3525['domain']
            if var2655.endswith('.'):
                var2655 = ''
                del var3525['domain']
            if ((not var2655) and (var1597 is not None)):
                self.attribute780.add((var1597, var325))
                var2655 = var3525['domain'] = var1597
            if var2655.startswith('.'):
                var2655 = var2655[1:]
                var3525['domain'] = var2655
            if (hostname and (not self.function2462(var2655, var1597))):
                continue
            var4039 = var3525['path']
            if ((not var4039) or (not var4039.startswith('/'))):
                var4039 = arg355.var4039
                if (not var4039.startswith('/')):
                    var4039 = '/'
                else:
                    var4039 = ('/' + var4039[1:var4039.rfind('/')])
                var3525['path'] = var4039
            var4162 = var3525['max-age']
            if var4162:
                try:
                    var4606 = int(var4162)
                    self.function2166((self._loop.time() + var4606), var2655, var325)
                except ValueError:
                    var3525['max-age'] = ''
            else:
                var3221 = var3525['expires']
                if var3221:
                    var3469 = self.function2744(var3221)
                    if var3469:
                        self.function2166(var3469.timestamp(), var2655, var325)
                    else:
                        var3525['expires'] = ''
            dict.__setitem__(self.attribute806[var2655], var325, var3525)
        self.function2829()

    def function1289(self, arg824=URL()):
        "Returns this jar's cookies filtered by their attributes."
        self.function2829()
        arg824 = URL(arg824)
        var3212 = SimpleCookie()
        var1597 = (arg824.raw_host or '')
        var3225 = (arg824.scheme not in ('https', 'wss'))
        for var1573 in self:
            var1329 = var1573.key
            var132 = var1573['domain']
            if (not var132):
                var3212[var1329] = var1573.value
                continue
            if ((not self.attribute1674) and is_ip_address(var1597)):
                continue
            if ((var132, var1329) in self.attribute780):
                if (var132 != var1597):
                    continue
            elif (not self.function2462(var132, var1597)):
                continue
            if (not self.function2032(arg824.path, var1573['path'])):
                continue
            if (is_not_secure and var1573['secure']):
                continue
            var2063 = var1573.get(var1573.key, Morsel())
            var2063.set(var1573.key, var1573.value, var1573.coded_value)
            var3212[var1329] = var2063
        return var3212

    @staticmethod
    def function2462(arg1597, var1597):
        'Implements domain matching adhering to RFC 6265.'
        if (var1597 == arg1597):
            return True
        if (not var1597.endswith(arg1597)):
            return False
        var335 = var1597[:(- len(arg1597))]
        if (not var335.endswith('.')):
            return False
        return (not is_ip_address(var1597))

    @staticmethod
    def function2032(arg180, arg1518):
        'Implements path matching adhering to RFC 6265.'
        if (not arg180.startswith('/')):
            arg180 = '/'
        if (arg180 == arg1518):
            return True
        if (not arg180.startswith(arg1518)):
            return False
        if arg1518.endswith('/'):
            return True
        var3620 = arg180[len(arg1518):]
        return var3620.startswith('/')

    @classmethod
    def function2744(arg1687, arg1072):
        'Implements date string parsing adhering to RFC 6265.'
        if (not arg1072):
            return
        var590 = False
        var589 = False
        var925 = False
        var514 = False
        var2733 = var1595 = var2717 = 0
        var3157 = 0
        var2167 = 0
        var1566 = 0
        for var3547 in arg1687.var4128.finditer(arg1072):
            var3067 = var3547.group('token')
            if (not var590):
                var3888 = arg1687.var1780.match(var3067)
                if var3888:
                    var590 = True
                    (var2733, var1595, var2717) = [int(var884) for var884 in var3888.groups()]
                    continue
            if (not var589):
                var1544 = arg1687.var4416.match(var3067)
                if var1544:
                    var589 = True
                    var3157 = int(var1544.group())
                    continue
            if (not var925):
                var2494 = arg1687.var3296.match(var3067)
                if var2494:
                    var925 = True
                    var2167 = var2494.lastindex
                    continue
            if (not var514):
                var2665 = arg1687.var905.match(var3067)
                if var2665:
                    var514 = True
                    var1566 = int(var2665.group())
        if (70 <= var1566 <= 99):
            var1566 += 1900
        elif (0 <= var1566 <= 69):
            var1566 += 2000
        if (False in (var589, var925, var514, var590)):
            return
        if (not (1 <= var3157 <= 31)):
            return
        if ((var1566 < 1601) or (var2733 > 23) or (var1595 > 59) or (var2717 > 59)):
            return
        return datetime.datetime(var1566, var2167, var3157, var2733, var1595, var2717, tzinfo=datetime.timezone.utc)