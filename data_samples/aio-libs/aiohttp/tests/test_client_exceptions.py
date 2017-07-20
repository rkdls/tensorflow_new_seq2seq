'Tests for http_exceptions.py'
from aiohttp import client

def function1579():
    var4505 = client.ServerFingerprintMismatch('exp', 'got', 'host', 8888)
    var1598 = '<ServerFingerprintMismatch expected=exp got=got host=host port=8888>'
    assert (var1598 == repr(var4505))