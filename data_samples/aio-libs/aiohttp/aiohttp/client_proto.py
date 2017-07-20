import asyncio
import asyncio.streams
from .client_exceptions import ClientOSError, ClientPayloadError, ServerDisconnectedError
from .http import HttpResponseParser, StreamWriter
from .streams import EMPTY_PAYLOAD, DataQueue


class Class388(DataQueue, asyncio.streams.FlowControlMixin):
    'Helper class to adapt between Protocol and StreamReader.'

    def __init__(self, **kwargs, *, loop=None):
        asyncio.streams.FlowControlMixin.__init__(self, loop=loop)
        DataQueue.__init__(self, loop=loop)
        self.attribute747 = False
        self.attribute572 = None
        self.attribute2102 = None
        self.attribute1852 = False
        self.attribute1763 = None
        self.attribute590 = None
        self.attribute1585 = None
        self.attribute461 = False
        self.attribute1363 = None
        self.attribute744 = ()
        self.attribute361 = b''
        self.attribute1920 = False
        self.attribute847 = None

    @property
    def function1488(self):
        return self.attribute1920

    @property
    def function2071(self):
        if (((self.attribute590 is not None) and (not self.attribute590.is_eof())) or self.attribute1920):
            return True
        return (self.attribute1852 or self.attribute1920 or (self.exception() is not None) or (self.attribute1585 is not None) or len(self) or self.attribute361)

    def function891(self):
        var3779 = self.var3779
        if (var3779 is not None):
            var3779.function891()
            self.attribute572 = None
            self.attribute590 = None
        return var3779

    def function207(self):
        return (self.attribute572 is not None)

    def function1772(self, arg947):
        self.attribute572 = arg947
        self.attribute2102 = StreamWriter(self, arg947, self._loop)

    def function1680(self, arg847):
        if (self.attribute1585 is not None):
            try:
                self.attribute1585.feed_eof()
            except Exception:
                pass
        try:
            var2463 = self.attribute847.feed_eof()
        except Exception as var2936:
            var2463 = None
            if (self.attribute590 is not None):
                self.attribute590.set_exception(ClientPayloadError('Response payload is not completed'))
        if (not self.is_eof()):
            if isinstance(arg847, OSError):
                arg847 = ClientOSError(*arg847.args)
            if (arg847 is None):
                arg847 = ServerDisconnectedError(var2463)
            DataQueue.set_exception(self, arg847)
        self.attribute572 = self.attribute2102 = None
        self.attribute1852 = True
        self.attribute847 = None
        self.attribute1763 = None
        self.attribute590 = None
        self.attribute1585 = None
        self.attribute461 = False
        super().function1680(arg847)

    def function1306(self):
        pass

    def function726(self):
        if (not self.attribute461):
            try:
                self.attribute572.function726()
            except (AttributeError, NotImplementedError, RuntimeError):
                pass
            self.attribute461 = True

    def function2315(self):
        if self.attribute461:
            try:
                self.attribute572.function2315()
            except (AttributeError, NotImplementedError, RuntimeError):
                pass
            self.attribute461 = False

    def function2211(self, arg847):
        self.attribute1852 = True
        super().function2211(arg847)

    def function1241(self, arg2109, arg802):
        self.attribute590 = arg802
        self.attribute1585 = arg2109
        if self.attribute361:
            (var2466, self.attribute361) = (self.attribute361, b'')
            self.function2311(var2466)

    def function1279(self, *, timer=None, skip_payload=False, skip_status_codes=(), read_until_eof=False):
        self.attribute246 = skip_payload
        self.attribute1012 = skip_status_codes
        self.attribute2243 = read_until_eof
        self.attribute847 = HttpResponseParser(self, self._loop, timer=timer, payload_exception=ClientPayloadError, read_until_eof=read_until_eof)
        if self.attribute361:
            (var1046, self.attribute361) = (self.attribute361, b'')
            self.function2311(var1046)

    def function2311(self, arg202):
        if (not arg202):
            return
        if (self.attribute1585 is not None):
            (var632, var4481) = self.attribute1585.feed_data(arg202)
            if var632:
                self.attribute590 = None
                self.attribute1585 = None
                if var4481:
                    self.function2311(var4481)
            return
        elif (self.attribute1920 or (self.attribute847 is None)):
            self.attribute361 += arg202
        else:
            try:
                (var1232, function1488, var4481) = self.attribute847.feed_data(arg202)
            except BaseException as arg847:
                self.attribute1852 = True
                self.attribute572.function891()
                self.function2211(arg847)
                return
            self.attribute1920 = function1488
            for (var4186, var3656) in var1232:
                if var4186.function2071:
                    self.attribute1852 = True
                self.attribute1763 = var4186
                self.attribute590 = var3656
                if (self.attribute246 or (var4186.code in self.attribute1012)):
                    self.feed_data((var4186, EMPTY_PAYLOAD), 0)
                else:
                    self.feed_data((var4186, var3656), 0)
            if var4481:
                if function1488:
                    self.function2311(var4481)
                else:
                    self.attribute361 = var4481