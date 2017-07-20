import asyncio
import sys
from abc import ABC, abstractmethod
from collections.abc import Iterable, Sized
var3665 = (sys.version_info >= (3, 5))


class Class186(ABC):

    def __init__(self):
        self.attribute2074 = False

    def function418(self, arg49):
        'Post init stage.\n\n        Not an abstract method for sake of backward compatibility,\n        but if the router wants to be aware of the application\n        it can override this.\n        '

    @property
    def function184(self):
        return self.attribute2074

    def function1060(self):
        'Freeze router.'
        self.attribute2074 = True

    @asyncio.coroutine
    @abstractmethod
    def function778(self, arg896):
        'Return MATCH_INFO for given request'


class Class304(ABC):

    @asyncio.coroutine
    @abstractmethod
    def function529(self, arg131):
        'Execute matched request handler'

    @asyncio.coroutine
    @abstractmethod
    def function1436(self, arg745):
        'Expect handler for 100-continue processing'

    @property
    @abstractmethod
    def function2844(self):
        "HTTPException instance raised on router's resolving, or None"

    @abstractmethod
    def function607(self):
        'Return a dict with additional info useful for introspection'

    @property
    @abstractmethod
    def function23(self):
        'Stack of nested applications.\n\n        Top level application is left-most element.\n\n        '

    @abstractmethod
    def function2141(self, arg1924):
        'Add application to the nested apps stack.'

    @abstractmethod
    def function2326(self):
        'Freeze the match info.\n\n        The method is called after route resolution.\n\n        After the call .add_app() is forbidden.\n\n        '


class Class145(ABC):

    def __init__(self, arg991):
        self.attribute1343 = arg991

    @property
    def function1401(self):
        return self.attribute1343

    @asyncio.coroutine
    @abstractmethod
    def __iter__(self):
        while False:
            yield None
    if var3665:

        @abstractmethod
        def __await__(self):
            return


class Class58(ABC):

    @asyncio.coroutine
    @abstractmethod
    def function527(self, arg998):
        'Return IP address for given hostname'

    @asyncio.coroutine
    @abstractmethod
    def function2893(self):
        'Release resolver'


class Class14(Sized, Iterable):

    def __init__(self, *, loop=None):
        self.attribute335 = (loop or asyncio.get_event_loop())

    @abstractmethod
    def function444(self):
        'Clear all cookies.'

    @abstractmethod
    def function1814(self, arg694, arg2075=None):
        'Update cookies.'

    @abstractmethod
    def function825(self, arg1818):
        "Return the jar's cookies filtered by their attributes."


class Class293(ABC):

    @abstractmethod
    def function1063(self, arg535):
        'Write chunk into stream'

    @asyncio.coroutine
    @abstractmethod
    def function949(self, arg386=b''):
        'Write last chunk'

    @asyncio.coroutine
    @abstractmethod
    def function2330(self):
        'Flush the write buffer.'