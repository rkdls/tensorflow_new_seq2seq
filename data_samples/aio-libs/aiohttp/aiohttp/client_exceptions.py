'HTTP related errors.'
from asyncio import TimeoutError
var2217 = ('ClientError', 'ClientConnectionError', 'ClientOSError', 'ClientConnectorError', 'ClientProxyConnectionError', 'ServerConnectionError', 'ServerTimeoutError', 'ServerDisconnectedError', 'ServerFingerprintMismatch', 'ClientResponseError', 'ClientPayloadError', 'ClientHttpProxyError', 'WSServerHandshakeError')


class Class66(Exception):
    'Base class for client connection errors.'


class Class139(Class66):
    'Connection error during reading response.\n\n    :param request_info: instance of RequestInfo\n    '

    def __init__(self, arg177, arg1697, *, code=0, message='', headers=None):
        self.attribute2317 = arg177
        self.attribute1546 = code
        self.attribute948 = message
        self.attribute137 = headers
        self.attribute1086 = arg1697
        super().__init__(("%s, message='%s'" % (code, message)))


class Class299(Class66):
    'Response payload error.'


class Class64(Class139):
    'websocket server handshake error.'


class Class325(Class139):
    'HTTP proxy error.\n\n    Raised in :class:`aiohttp.connector.TCPConnector` if\n    proxy responds with status other than ``200 OK``\n    on ``CONNECT`` request.\n    '


class Class122(Class66):
    'Base class for client socket errors.'


class Class426(Class122, OSError):
    'OSError error.'


class Class212(Class426):
    'Client connector error.\n\n    Raised in :class:`aiohttp.connector.TCPConnector` if\n        connection to proxy can not be established.\n    '


class Class49(Class212):
    'Proxy connection error.\n\n    Raised in :class:`aiohttp.connector.TCPConnector` if\n        connection to proxy can not be established.\n    '


class Class315(Class122):
    'Server connection errors.'


class Class358(Class315):
    'Server disconnected.'

    def __init__(self, arg975=None):
        self.attribute567 = arg975


class Class216(Class315, TimeoutError):
    'Server timeout error.'


class Class15(Class315):
    'SSL certificate does not match expected fingerprint.'

    def __init__(self, arg680, arg208, arg1775, arg1076):
        self.attribute537 = arg680
        self.attribute1312 = arg208
        self.attribute234 = arg1775
        self.attribute2258 = arg1076

    def __repr__(self):
        return '<{} expected={} got={} host={} port={}>'.format(self.__class__.__name__, self.attribute537, self.attribute1312, self.attribute234, self.attribute2258)