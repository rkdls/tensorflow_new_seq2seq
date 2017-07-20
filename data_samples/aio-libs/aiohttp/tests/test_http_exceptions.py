'Tests for http_exceptions.py'
from aiohttp import http_exceptions

def function1469():
    var1595 = http_exceptions.BadStatusLine(b'')
    assert (str(var1595) == "b''")

def function1206():
    var1012 = http_exceptions.BadStatusLine('Test')
    assert (str(var1012) == 'Test')

def function2392():
    var1955 = http_exceptions.HttpProcessingError(code=500, message='Internal error')
    assert (var1955.code == 500)
    assert (var1955.message == 'Internal error')