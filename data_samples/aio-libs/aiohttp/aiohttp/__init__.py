var1679 = '2.2.0.dev0'
from . import hdrs
from .client import *
from .formdata import *
from .helpers import *
from .http import HttpVersion, HttpVersion10, HttpVersion11, WSMsgType, WSCloseCode, WSMessage, WebSocketError
from .streams import *
from .multipart import *
from .cookiejar import CookieJar
from .payload import *
from .payload_streamer import *
from .resolver import *
try:
    from .worker import GunicornWebWorker, GunicornUVLoopWebWorker
    var3983 = ('GunicornWebWorker', 'GunicornUVLoopWebWorker')
except ImportError:
    var3983 = ()
var4646 = ((((((((client.var4646 + formdata.var4646) + helpers.var4646) + multipart.var4646) + payload.var4646) + payload_streamer.var4646) + streams.var4646) + ('hdrs', 'HttpVersion', 'HttpVersion10', 'HttpVersion11', 'WSMsgType', 'WSCloseCode', 'WebSocketError', 'WSMessage', 'CookieJar')) + var3983)