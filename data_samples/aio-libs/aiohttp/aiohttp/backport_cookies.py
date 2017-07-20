import re
import string
from http.cookies import CookieError, Morsel
var1085 = ['CookieError', 'BaseCookie', 'SimpleCookie']
var865 = ''.join
var254 = '; '.join
var4111 = ' '.join
var1536 = ((string.ascii_letters + string.digits) + "!#$%&'*+-.^_`|~:")
var3653 = {'\x00': '\\000', '\x01': '\\001', '\x02': '\\002', '\x03': '\\003', '\x04': '\\004', '\x05': '\\005', '\x06': '\\006', '\x07': '\\007', '\x08': '\\010', '\t': '\\011', '\n': '\\012', '\x0b': '\\013', '\x0c': '\\014', '\r': '\\015', '\x0e': '\\016', '\x0f': '\\017', '\x10': '\\020', '\x11': '\\021', '\x12': '\\022', '\x13': '\\023', '\x14': '\\024', '\x15': '\\025', '\x16': '\\026', '\x17': '\\027', '\x18': '\\030', '\x19': '\\031', '\x1a': '\\032', '\x1b': '\\033', '\x1c': '\\034', '\x1d': '\\035', '\x1e': '\\036', '\x1f': '\\037', ',': '\\054', ';': '\\073', '"': '\\"', '\\': '\\\\', '\x7f': '\\177', '\x80': '\\200', '\x81': '\\201', '\x82': '\\202', '\x83': '\\203', '\x84': '\\204', '\x85': '\\205', '\x86': '\\206', '\x87': '\\207', '\x88': '\\210', '\x89': '\\211', '\x8a': '\\212', '\x8b': '\\213', '\x8c': '\\214', '\x8d': '\\215', '\x8e': '\\216', '\x8f': '\\217', '\x90': '\\220', '\x91': '\\221', '\x92': '\\222', '\x93': '\\223', '\x94': '\\224', '\x95': '\\225', '\x96': '\\226', '\x97': '\\227', '\x98': '\\230', '\x99': '\\231', '\x9a': '\\232', '\x9b': '\\233', '\x9c': '\\234', '\x9d': '\\235', '\x9e': '\\236', '\x9f': '\\237', '\xa0': '\\240', '¡': '\\241', '¢': '\\242', '£': '\\243', '¤': '\\244', '¥': '\\245', '¦': '\\246', '§': '\\247', '¨': '\\250', '©': '\\251', 'ª': '\\252', '«': '\\253', '¬': '\\254', '\xad': '\\255', '®': '\\256', '¯': '\\257', '°': '\\260', '±': '\\261', '²': '\\262', '³': '\\263', '´': '\\264', 'µ': '\\265', '¶': '\\266', '·': '\\267', '¸': '\\270', '¹': '\\271', 'º': '\\272', '»': '\\273', '¼': '\\274', '½': '\\275', '¾': '\\276', '¿': '\\277', 'À': '\\300', 'Á': '\\301', 'Â': '\\302', 'Ã': '\\303', 'Ä': '\\304', 'Å': '\\305', 'Æ': '\\306', 'Ç': '\\307', 'È': '\\310', 'É': '\\311', 'Ê': '\\312', 'Ë': '\\313', 'Ì': '\\314', 'Í': '\\315', 'Î': '\\316', 'Ï': '\\317', 'Ð': '\\320', 'Ñ': '\\321', 'Ò': '\\322', 'Ó': '\\323', 'Ô': '\\324', 'Õ': '\\325', 'Ö': '\\326', '×': '\\327', 'Ø': '\\330', 'Ù': '\\331', 'Ú': '\\332', 'Û': '\\333', 'Ü': '\\334', 'Ý': '\\335', 'Þ': '\\336', 'ß': '\\337', 'à': '\\340', 'á': '\\341', 'â': '\\342', 'ã': '\\343', 'ä': '\\344', 'å': '\\345', 'æ': '\\346', 'ç': '\\347', 'è': '\\350', 'é': '\\351', 'ê': '\\352', 'ë': '\\353', 'ì': '\\354', 'í': '\\355', 'î': '\\356', 'ï': '\\357', 'ð': '\\360', 'ñ': '\\361', 'ò': '\\362', 'ó': '\\363', 'ô': '\\364', 'õ': '\\365', 'ö': '\\366', '÷': '\\367', 'ø': '\\370', 'ù': '\\371', 'ú': '\\372', 'û': '\\373', 'ü': '\\374', 'ý': '\\375', 'þ': '\\376', 'ÿ': '\\377', }

def function698(arg2131, arg1860=_LegalChars):
    'Quote a string for use in a cookie header.\n\n    If the string does not need to be double-quoted, then just return the\n    string.  Otherwise, surround the string in doublequotes and quote\n    (with a \\) special characters.\n    '
    if all(((var127 in arg1860) for var127 in arg2131)):
        return arg2131
    else:
        return (('"' + var865((var3653.get(var2812, var2812) for var2812 in arg2131))) + '"')
var1320 = re.compile('\\\\[0-3][0-7][0-7]')
var2183 = re.compile('[\\\\].')

def function1025(arg2022):
    if (len(arg2022) < 2):
        return arg2022
    if ((arg2022[0] != '"') or (arg2022[(- 1)] != '"')):
        return arg2022
    arg2022 = arg2022[1:(- 1)]
    var1744 = 0
    var3427 = len(arg2022)
    var3946 = []
    while (0 <= var1744 < var3427):
        var1977 = var1320.search(arg2022, var1744)
        var2272 = var2183.search(arg2022, var1744)
        if ((not var1977) and (not var2272)):
            var3946.append(arg2022[var1744:])
            break
        var888 = var3065 = (- 1)
        if var1977:
            var888 = var1977.start(0)
        if var2272:
            var3065 = var2272.start(0)
        if (q_match and ((not var1977) or (var3065 < var888))):
            var3946.append(arg2022[var1744:var3065])
            var3946.append(arg2022[(var3065 + 1)])
            var1744 = (var3065 + 2)
        else:
            var3946.append(arg2022[var1744:var888])
            var3946.append(chr(int(arg2022[(var888 + 1):(var888 + 4)], 8)))
            var1744 = (var888 + 4)
    return var865(var3946)
var1648 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
var725 = [None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def function631(arg989=0, arg2394=_weekdayname, arg1961=_monthname):
    from time import gmtime, time
    var3211 = time()
    (var913, var207, var1195, var3881, var891, var1788, var3434, var1727, var3241) = gmtime((var3211 + arg989))
    return ('%s, %02d %3s %4d %02d:%02d:%02d GMT' % (arg2394[var3434], var1195, arg1961[var207], var913, var3881, var891, var1788))
var1665 = "\\w\\d!#%&'~_`><@,:/\\$\\*\\+\\-\\.\\^\\|\\)\\(\\?\\}\\{\\="
var4227 = (var1665 + '\\[\\]')
var1595 = re.compile((((("\n    (?x)                           # This is a verbose pattern\n    \\s*                            # Optional whitespace at start of cookie\n    (?P<key>                       # Start of group 'key'\n    [" + var1665) + ']+?   # Any word of at least one letter\n    )                              # End of group \'key\'\n    (                              # Optional group: there may not be a value.\n    \\s*=\\s*                          # Equal Sign\n    (?P<val>                         # Start of group \'val\'\n    "(?:[^\\\\"]|\\\\.)*"                  # Any doublequoted string\n    |                                  # or\n    \\w{3},\\s[\\w\\d\\s-]{9,11}\\s[\\d:]{8}\\sGMT  # Special case for "expires" attr\n    |                                  # or\n    [') + var4227) + "]*      # Any word or empty string\n    )                                # End of group 'val'\n    )?                             # End of optional value group\n    \\s*                            # Any number of spaces.\n    (\\s+|;|$)                      # Ending either at space, semicolon, or EOS.\n    "), re.ASCII)


class Class82(dict):
    'A container class for a set of Morsels.'

    def function1613(self, arg1488):
        "real_value, coded_value = value_decode(STRING)\n        Called prior to setting a cookie's value from the network\n        representation.  The VALUE is the value read from HTTP\n        header.\n        Override this function to modify the behavior of cookies.\n        "
        return (arg1488, arg1488)

    def function671(self, arg426):
        "real_value, coded_value = value_encode(VALUE)\n        Called prior to setting a cookie's value from the dictionary\n        representation.  The VALUE is the value being assigned.\n        Override this function to modify the behavior of cookies.\n        "
        var2476 = str(arg426)
        return (var2476, var2476)

    def __init__(self, arg427=None):
        if arg427:
            self.function332(arg427)

    def __set(self, arg1316, arg2304, arg633):
        "Private method for setting a cookie's value"
        var2405 = self.get(arg1316, Morsel())
        var2405.set(arg1316, arg2304, arg633)
        dict.__setitem__(self, arg1316, var2405)

    def __setitem__(self, arg1238, arg226):
        'Dictionary style assignment.'
        if isinstance(arg226, Morsel):
            dict.__setitem__(self, arg1238, arg226)
        else:
            (var3253, var2279) = self.function671(arg226)
            self.__set(arg1238, var3253, var2279)

    def function679(self, arg1559=None, arg1578='Set-Cookie:', arg352='\r\n'):
        'Return a string suitable for HTTP.'
        var1293 = []
        var2486 = sorted(self.var2486())
        for (var2857, var4503) in var2486:
            var1293.append(var4503.function679(arg1559, arg1578))
        return arg352.join(var1293)
    var4427 = function679

    def __repr__(self):
        var1989 = []
        var2314 = sorted(self.var2314())
        for (var4577, var2825) in var2314:
            var1989.append(('%s=%s' % (var4577, repr(var2825.var2825))))
        return ('<%s: %s>' % (self.__class__.__name__, var4111(var1989)))

    def function1842(self, arg590=None):
        'Return a string suitable for JavaScript.'
        var1512 = []
        var4441 = sorted(self.var4441())
        for (var446, var1987) in var4441:
            var1512.append(var1987.function1842(arg590))
        return var865(var1512)

    def function332(self, arg702):
        "Load cookies from a string (presumably HTTP_COOKIE) or\n        from a dictionary.  Loading cookies from a dictionary 'd'\n        is equivalent to calling:\n            map(Cookie.__setitem__, d.keys(), d.values())\n        "
        if isinstance(arg702, str):
            self.__parse_string(arg702)
        else:
            for (var2416, var3964) in arg702.items():
                self[var2416] = var3964
        return

    def __parse_string(self, arg656, arg717=_CookiePattern):
        var137 = 0
        var3179 = len(arg656)
        var1058 = None
        while (0 <= var137 < var3179):
            var3700 = arg717.var3700(arg656, var137)
            if (not var3700):
                break
            (var3633, var1809) = (var3700.group('key'), var3700.group('val'))
            var137 = var3700.end(0)
            if (var3633[0] == '$'):
                if var1058:
                    var1058[var3633[1:]] = var1809
            elif (var3633.lower() in Morsel._reserved):
                if var1058:
                    if (var1809 is None):
                        if (var3633.lower() in Morsel._flags):
                            var1058[var3633] = True
                    else:
                        var1058[var3633] = function1025(var1809)
            elif (var1809 is not None):
                (var1822, var3829) = self.function1613(var1809)
                self.__set(var3633, var1822, var3829)
                var1058 = self[var3633]


class Class332(Class82):
    '\n    SimpleCookie supports strings as cookie values.  When setting\n    the value using the dictionary assignment notation, `SimpleCookie`\n    calls the builtin `str()` to convert the value to a string.  Values\n    received from HTTP are kept as strings.\n    '

    def function297(self, arg1177):
        return (function1025(arg1177), arg1177)

    def function6(self, arg1899):
        var53 = str(arg1899)
        return (var53, function698(var53))