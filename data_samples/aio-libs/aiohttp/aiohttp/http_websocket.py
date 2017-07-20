'WebSocket protocol versions 13 and 8.'
import base64
import binascii
import collections
import hashlib
import json
import random
import sys
from enum import IntEnum
from struct import Struct
from . import hdrs
from .helpers import NO_EXTENSIONS, noop
from .http_exceptions import HttpBadRequest, HttpProcessingError
from .log import ws_logger
var2263 = ('WS_CLOSED_MESSAGE', 'WS_CLOSING_MESSAGE', 'WS_KEY', 'WebSocketReader', 'WebSocketWriter', 'do_handshake', 'WSMessage', 'WebSocketError', 'WSMsgType', 'WSCloseCode')


class Class195(IntEnum):
    var1517 = 1000
    var1514 = 1001
    var680 = 1002
    var2707 = 1003
    var4744 = 1007
    var3823 = 1008
    var2907 = 1009
    var2063 = 1010
    var2135 = 1011
    var1715 = 1012
    var4224 = 1013
var2320 = {int(var1157) for var1157 in Class195}


class Class140(IntEnum):
    var2612 = 0
    var2621 = 1
    var1336 = 2
    var4218 = 9
    var3940 = 10
    var3203 = 8
    var1616 = 256
    var12 = 257
    var492 = 258
    var3444 = var2621
    var3063 = var1336
    var748 = var4218
    var3599 = var3940
    var4286 = var3203
    var1043 = var1616
    var2072 = var12
    var1757 = var492
var2620 = b'258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
var2069 = Struct('!H').unpack_from
var1620 = Struct('!Q').unpack_from
var1298 = Struct('!H').unpack
var632 = Struct('!BB').pack
var1390 = Struct('!BBH').pack
var2006 = Struct('!BBQ').pack
var698 = Struct('!H').pack
var2167 = (2 ** 14)
var2740 = (2 ** 16)
var43 = collections.namedtuple('_WSMessageBase', ['type', 'data', 'extra'])


class Class228(_WSMessageBase):

    def function2859(self, *, loads=function2859.loads):
        'Return parsed JSON data.\n\n        .. versionadded:: 0.22\n        '
        return loads(self.data)

    @property
    def function1508(self):
        return self.type
var1649 = Class228(Class140.CLOSED, None, None)
var1548 = Class228(Class140.CLOSING, None, None)


class Class161(Exception):
    'WebSocket protocol parser error.'

    def __init__(self, arg487, arg1893):
        self.attribute769 = arg487
        super().__init__(arg1893)
var4113 = sys.byteorder
var877 = [bytes(((var1709 ^ var4481) for var1709 in range(256))) for var4481 in range(256)]

def function1265(arg881, arg976):
    'Websocket masking function.\n\n    `mask` is a `bytes` object of length 4; `data` is a `bytearray`\n    object of any length. The contents of `data` are masked with `mask`,\n    as specified in section 5.3 of RFC 6455.\n\n    Note that this function mutates the `data` argument.\n\n    This pure-python implementation may be replaced by an optimized\n    version when available.\n\n    '
    assert isinstance(arg976, bytearray), data
    assert (len(arg881) == 4), mask
    if arg976:
        (var537, var4648, var4244, var122) = (var877[var2577] for var2577 in arg881)
        arg976[::4] = arg976[::4].translate(var537)
        arg976[1::4] = arg976[1::4].translate(var4648)
        arg976[2::4] = arg976[2::4].translate(var4244)
        arg976[3::4] = arg976[3::4].translate(var122)
if NO_EXTENSIONS:
    var1539 = function1265
else:
    try:
        from ._websocket import _websocket_mask_cython
        var1539 = _websocket_mask_cython
    except ImportError:
        var1539 = function1265


class Class75(IntEnum):
    var3914 = 1
    var2122 = 2
    var1630 = 3
    var195 = 4


class Class366:

    def __init__(self, arg334):
        self.attribute784 = arg334
        self.attribute2206 = None
        self.attribute1251 = []
        self.attribute175 = Class75.READ_HEADER
        self.attribute696 = None
        self.attribute1619 = False
        self.attribute1975 = None
        self.attribute1503 = bytearray()
        self.attribute944 = b''
        self.attribute332 = False
        self.attribute1498 = None
        self.attribute2314 = 0
        self.attribute809 = 0

    def function985(self):
        self.attribute784.function985()

    def function1367(self, arg267):
        if self.attribute2206:
            return (True, arg267)
        try:
            return self.function2560(arg267)
        except Exception as var2617:
            self.attribute2206 = var2617
            self.attribute784.set_exception(var2617)
            return (True, b'')

    def function2560(self, arg267):
        for (var2473, var3862, var1961) in self.function2754(arg267):
            if (var3862 == Class140.CLOSE):
                if (len(var1961) >= 2):
                    var1158 = var1298(var1961[:2])[0]
                    if ((var1158 < 3000) and (var1158 not in var2320)):
                        raise Class161(Class195.PROTOCOL_ERROR, 'Invalid close code: {}'.format(var1158))
                    try:
                        var729 = var1961[2:].decode('utf-8')
                    except UnicodeDecodeError as var1077:
                        raise Class161(Class195.INVALID_TEXT, 'Invalid UTF-8 text message') from exc
                    var4729 = Class228(Class140.CLOSE, var1158, var729)
                elif var1961:
                    raise Class161(Class195.PROTOCOL_ERROR, 'Invalid close frame: {} {} {!r}'.format(var2473, var3862, var1961))
                else:
                    var4729 = Class228(Class140.CLOSE, 0, '')
                self.attribute784.function1367(var4729, 0)
            elif (var3862 == Class140.PING):
                self.attribute784.function1367(Class228(Class140.PING, var1961, ''), len(var1961))
            elif (var3862 == Class140.PONG):
                self.attribute784.function1367(Class228(Class140.PONG, var1961, ''), len(var1961))
            elif ((var3862 not in (Class140.TEXT, Class140.BINARY)) and (self.attribute696 is None)):
                raise Class161(Class195.PROTOCOL_ERROR, 'Unexpected opcode={!r}'.format(var3862))
            elif (not var2473):
                if (var3862 != Class140.CONTINUATION):
                    self.attribute696 = var3862
                self.attribute1251.append(var1961)
            else:
                if self.attribute1251:
                    if (var3862 != Class140.CONTINUATION):
                        raise Class161(Class195.PROTOCOL_ERROR, 'The opcode in non-fin frame is expected to be zero, got {!r}'.format(var3862))
                if (var3862 == Class140.CONTINUATION):
                    var3862 = self.attribute696
                    self.attribute696 = None
                var1888 = (b''.join(self.attribute1251) + var1961)
                self.attribute1251.clear()
                if (var3862 == Class140.TEXT):
                    try:
                        var4582 = var1888.decode('utf-8')
                        self.attribute784.function1367(Class228(Class140.TEXT, var4582, ''), len(var4582))
                    except UnicodeDecodeError as var1077:
                        raise Class161(Class195.INVALID_TEXT, 'Invalid UTF-8 text message') from exc
                else:
                    self.attribute784.function1367(Class228(Class140.BINARY, var1888, ''), len(var1888))
        return (False, b'')

    def function2754(self, arg1967):
        'Return the next frame from the socket.'
        var2960 = []
        if self.attribute944:
            (arg1967, self.attribute944) = ((self.attribute944 + arg1967), b'')
        var3452 = 0
        var757 = len(arg1967)
        while True:
            if (self.attribute175 == Class75.READ_HEADER):
                if ((var757 - var3452) >= 2):
                    arg267 = arg1967[var3452:(var3452 + 2)]
                    var3452 += 2
                    (var3630, var4110) = arg267
                    var2473 = ((var3630 >> 7) & 1)
                    var3175 = ((var3630 >> 6) & 1)
                    var438 = ((var3630 >> 5) & 1)
                    var4239 = ((var3630 >> 4) & 1)
                    var3862 = (var3630 & 15)
                    if (rsv1 or rsv2 or rsv3):
                        raise Class161(Class195.PROTOCOL_ERROR, 'Received frame with non-zero reserved bits')
                    if ((var3862 > 7) and (var2473 == 0)):
                        raise Class161(Class195.PROTOCOL_ERROR, 'Received fragmented control frame')
                    var4148 = ((var4110 >> 7) & 1)
                    var4728 = (var4110 & 127)
                    if ((var3862 > 7) and (var4728 > 125)):
                        raise Class161(Class195.PROTOCOL_ERROR, 'Control frame payload cannot be larger than 125 bytes')
                    self.attribute1619 = var2473
                    self.attribute1975 = var3862
                    self.attribute332 = var4148
                    self.attribute809 = var4728
                    self.attribute175 = Class75.READ_PAYLOAD_LENGTH
                else:
                    break
            if (self.attribute175 == Class75.READ_PAYLOAD_LENGTH):
                var4728 = self.attribute809
                if (var4728 == 126):
                    if ((var757 - var3452) >= 2):
                        arg267 = arg1967[var3452:(var3452 + 2)]
                        var3452 += 2
                        var4728 = var2069(arg267)[0]
                        self.attribute2314 = var4728
                        self.attribute175 = (Class75.READ_PAYLOAD_MASK if self.attribute332 else Class75.READ_PAYLOAD)
                    else:
                        break
                elif (var4728 > 126):
                    if ((var757 - var3452) >= 8):
                        arg267 = arg1967[var3452:(var3452 + 8)]
                        var3452 += 8
                        var4728 = var1620(arg267)[0]
                        self.attribute2314 = var4728
                        self.attribute175 = (Class75.READ_PAYLOAD_MASK if self.attribute332 else Class75.READ_PAYLOAD)
                    else:
                        break
                else:
                    self.attribute2314 = var4728
                    self.attribute175 = (Class75.READ_PAYLOAD_MASK if self.attribute332 else Class75.READ_PAYLOAD)
            if (self.attribute175 == Class75.READ_PAYLOAD_MASK):
                if ((var757 - var3452) >= 4):
                    self.attribute1498 = arg1967[var3452:(var3452 + 4)]
                    var3452 += 4
                    self.attribute175 = Class75.READ_PAYLOAD
                else:
                    break
            if (self.attribute175 == Class75.READ_PAYLOAD):
                var4728 = self.attribute2314
                var1961 = self.attribute1503
                var3143 = (var757 - var3452)
                if (var4728 >= var3143):
                    self.attribute2314 = (var4728 - var3143)
                    var1961.extend(arg1967[var3452:])
                    var3452 = var757
                else:
                    self.attribute2314 = 0
                    var1961.extend(arg1967[var3452:(var3452 + var4728)])
                    var3452 = (var3452 + var4728)
                if (self.attribute2314 == 0):
                    if self.attribute332:
                        var1539(self.attribute1498, var1961)
                    var2960.append((self.attribute1619, self.attribute1975, var1961))
                    self.attribute1503 = bytearray()
                    self.attribute175 = Class75.READ_HEADER
                else:
                    break
        self.attribute944 = arg1967[var3452:]
        return var2960


class Class280:

    def __init__(self, arg2317, *, use_mask=False, limit=DEFAULT_LIMIT, random=random.Random()):
        self.attribute337 = arg2317
        self.attribute149 = arg2317.transport
        self.attribute439 = use_mask
        self.attribute1508 = random.randrange
        self.attribute2328 = False
        self.attribute373 = limit
        self.attribute2343 = 0

    def function602(self, arg2219, arg1848):
        'Send a frame over the websocket with message as its payload.'
        if self.attribute2328:
            ws_logger.warning('websocket connection is closing.')
        var3412 = len(arg2219)
        var3114 = self.var3114
        if var3114:
            var2172 = 128
        else:
            var2172 = 0
        if (var3412 < 126):
            var3512 = var632((128 | arg1848), (var3412 | var2172))
        elif (var3412 < (1 << 16)):
            var3512 = var1390((128 | arg1848), (126 | var2172), var3412)
        else:
            var3512 = var2006((128 | arg1848), (127 | var2172), var3412)
        if var3114:
            var4510 = self.attribute1508(0, 4294967295)
            var4510 = var4510.to_bytes(4, 'big')
            arg2219 = bytearray(arg2219)
            var1539(var4510, arg2219)
            self.attribute149.write(((var3512 + var4510) + arg2219))
            self.attribute2343 += ((len(var3512) + len(var4510)) + len(arg2219))
        else:
            if (len(arg2219) > var2167):
                self.attribute149.write(var3512)
                self.attribute149.write(arg2219)
            else:
                self.attribute149.write((var3512 + arg2219))
            self.attribute2343 += (len(var3512) + len(arg2219))
        if (self.attribute2343 > self.attribute373):
            self.attribute2343 = 0
            return self.attribute337.drain()
        return noop()

    def function75(self, arg1778=b''):
        'Send pong message.'
        if isinstance(arg1778, str):
            arg1778 = arg1778.encode('utf-8')
        return self.function602(arg1778, Class140.PONG)

    def function2621(self, arg415=b''):
        'Send ping message.'
        if isinstance(arg415, str):
            arg415 = arg415.encode('utf-8')
        return self.function602(arg415, Class140.PING)

    def function2304(self, arg2353, arg1598=False):
        'Send a frame over the websocket with message as its payload.'
        if isinstance(arg2353, str):
            arg2353 = arg2353.encode('utf-8')
        if arg1598:
            return self.function602(arg2353, Class140.BINARY)
        else:
            return self.function602(arg2353, Class140.TEXT)

    def function322(self, arg1027=1000, arg1413=b''):
        'Close the websocket, sending the specified code and message.'
        if isinstance(arg1413, str):
            arg1413 = arg1413.encode('utf-8')
        try:
            return self.function602((var698(arg1027) + arg1413), opcode=Class140.CLOSE)
        finally:
            self.attribute2328 = True

def function1467(arg1059, arg1545, arg2052, arg2057=(), arg451=DEFAULT_LIMIT):
    'Prepare WebSocket handshake.\n\n    It return HTTP response code, response headers, websocket parser,\n    websocket writer. It does not perform any IO.\n\n    `protocols` is a sequence of known protocols. On successful handshake,\n    the returned response headers contain the first protocol in this list\n    which the server also knows.\n\n    `write_buffer_size` max size of write buffer before `drain()` get called.\n    '
    if (arg1059.upper() != hdrs.METH_GET):
        raise HttpProcessingError(code=405, headers=((hdrs.ALLOW, hdrs.METH_GET),))
    if ('websocket' != arg1545.get(hdrs.UPGRADE, '').lower().strip()):
        raise HttpBadRequest(message='No WebSocket UPGRADE hdr: {}\n Can "Upgrade" only to "WebSocket".'.format(arg1545.get(hdrs.UPGRADE)))
    if ('upgrade' not in arg1545.get(hdrs.CONNECTION, '').lower()):
        raise HttpBadRequest(message='No CONNECTION upgrade hdr: {}'.format(arg1545.get(hdrs.CONNECTION)))
    var4 = None
    if (hdrs.SEC_WEBSOCKET_PROTOCOL in arg1545):
        var2576 = [str(var1813.strip()) for var1813 in arg1545[hdrs.SEC_WEBSOCKET_PROTOCOL].split(',')]
        for var4013 in var2576:
            if (var4013 in arg2057):
                var4 = var4013
                break
        else:
            ws_logger.warning('Client protocols %r don’t overlap server-known ones %r', var2576, arg2057)
    var4540 = arg1545.get(hdrs.SEC_WEBSOCKET_VERSION, '')
    if (var4540 not in ('13', '8', '7')):
        raise HttpBadRequest(message='Unsupported version: {}'.format(var4540), headers=((hdrs.SEC_WEBSOCKET_VERSION, '13'),))
    var4198 = arg1545.get(hdrs.SEC_WEBSOCKET_KEY)
    try:
        if ((not var4198) or (len(base64.b64decode(var4198)) != 16)):
            raise HttpBadRequest(message='Handshake error: {!r}'.format(var4198))
    except binascii.Error:
        raise HttpBadRequest(message='Handshake error: {!r}'.format(var4198)) from None
    var4288 = [(hdrs.UPGRADE, 'websocket'), (hdrs.CONNECTION, 'upgrade'), (hdrs.TRANSFER_ENCODING, 'chunked'), (hdrs.SEC_WEBSOCKET_ACCEPT, base64.b64encode(hashlib.sha1((var4198.encode() + var2620)).digest()).decode())]
    if var4:
        var4288.append((hdrs.SEC_WEBSOCKET_PROTOCOL, var4))
    return (101, var4288, None, Class280(arg2052, limit=arg451), var4)