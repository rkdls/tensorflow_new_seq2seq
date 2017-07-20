import asyncio
from unittest import mock
import pytest
from aiohttp.formdata import FormData

@pytest.fixture
def function1105():
    return bytearray()

@pytest.fixture
def function604(function1105):
    function604 = mock.Mock()

    def function2007(arg2005):
        function1105.extend(arg2005)
        return ()
    function604.function2007.side_effect = function2007
    return function604

def function2016(function1105, function604):
    var3393 = FormData()
    assert (not var3393.is_multipart)
    var3393.add_field('test', b'test', filename='test.txt')
    assert var3393.is_multipart

def function617():
    var3234 = FormData()
    var3234.add_field('test', object(), filename='test.txt')
    with pytest.raises(TypeError):
        var3234()

def function1578():
    with pytest.raises(TypeError):
        FormData('asdasf')

def function2419():
    with pytest.raises(TypeError):
        FormData('as')

def function615():
    var1644 = FormData()
    var1564 = [0, 0.1, {}, [], b'foo']
    for var155 in var1564:
        with pytest.raises(TypeError):
            var1644.add_field('foo', 'bar', content_type=var155)

def function2237():
    var938 = FormData()
    var3721 = [0, 0.1, {}, [], b'foo']
    for var1022 in var3721:
        with pytest.raises(TypeError):
            var938.add_field('foo', 'bar', filename=var1022)

def function1541():
    var670 = FormData()
    var676 = [0, 0.1, {}, [], b'foo']
    for var103 in var676:
        with pytest.raises(TypeError):
            var670.add_field('foo', 'bar', content_transfer_encoding=var103)

@asyncio.coroutine
def function1429(function1105, function604):
    var4060 = FormData(charset='ascii')
    var4060.add_field('emails[]', 'xxx@x.co', content_type='multipart/form-data')
    var3464 = var4060()
    yield from var3464.function2007(function604)
    assert (b'name="emails%5B%5D"' in function1105)

@asyncio.coroutine
def function398(function1105, function604):
    var3042 = FormData(quote_fields=False, charset='ascii')
    var3042.add_field('emails[]', 'xxx@x.co', content_type='multipart/form-data')
    var4723 = var3042()
    yield from var4723.function2007(function604)
    assert (b'name="emails[]"' in function1105)