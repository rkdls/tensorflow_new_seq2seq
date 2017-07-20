from unittest import mock
from aiohttp import hdrs, helpers
from aiohttp.test_utils import make_mocked_coro, make_mocked_request
from aiohttp.web_fileresponse import FileResponse, SendfilePayloadWriter

def function2710(arg1730):
    var29 = mock.Mock()
    with mock.patch('aiohttp.web_fileresponse.os') as var1264:
        var3508 = 30
        var1552 = 31
        var3859 = helpers.create_future(arg1730)
        var1264.sendfile.return_value = 0
        var1063 = SendfilePayloadWriter(var29, mock.Mock())
        var1063._sendfile_cb(var3859, var3508, var1552, 0, 100, var29, False)
        var1264.sendfile.assert_called_with(var3508, var1552, 0, 100)
        assert var3859.done()
        assert (var3859.result() is None)
        assert (not var29.add_writer.called)
        assert (not var29.remove_writer.called)

def function491(arg185):
    var2469 = mock.Mock()
    with mock.patch('aiohttp.web_fileresponse.os') as var807:
        var3379 = 30
        var4557 = 31
        var660 = helpers.create_future(arg185)
        var807.sendfile.side_effect = BlockingIOError()
        var2728 = SendfilePayloadWriter(var2469, mock.Mock())
        var2728._sendfile_cb(var660, var3379, var4557, 0, 100, var2469, False)
        var807.sendfile.assert_called_with(var3379, var4557, 0, 100)
        assert (not var660.done())
        var2469.add_writer.assert_called_with(var3379, var2728._sendfile_cb, var660, var3379, var4557, 0, 100, var2469, True)
        assert (not var2469.remove_writer.called)

def function154(arg1246):
    var2722 = mock.Mock()
    with mock.patch('aiohttp.web_fileresponse.os') as var2445:
        var547 = 30
        var3676 = 31
        var3871 = helpers.create_future(arg1246)
        var4272 = OSError()
        var2445.sendfile.side_effect = var4272
        var264 = SendfilePayloadWriter(var2722, mock.Mock())
        var264._sendfile_cb(var3871, var547, var3676, 0, 100, var2722, False)
        var2445.sendfile.assert_called_with(var547, var3676, 0, 100)
        assert var3871.done()
        assert (var4272 is var3871.exception())
        assert (not var2722.add_writer.called)
        assert (not var2722.remove_writer.called)

def function1408(arg1300):
    var4179 = mock.Mock()
    with mock.patch('aiohttp.web_fileresponse.os') as var3760:
        var808 = 30
        var3847 = 31
        var453 = helpers.create_future(arg1300)
        var453.cancel()
        var3794 = SendfilePayloadWriter(var4179, mock.Mock())
        var3794._sendfile_cb(var453, var808, var3847, 0, 100, var4179, False)
        assert var453.done()
        assert (not var4179.add_writer.called)
        assert (not var4179.remove_writer.called)
        assert (not var3760.sendfile.called)

def function2349(arg1111):
    var2428 = make_mocked_request('GET', 'http://python.org/logo.png', headers={hdrs.ACCEPT_ENCODING: 'gzip', })
    var789 = mock.Mock()
    var789.open = mock.mock_open()
    var789.is_file.return_value = True
    var789.stat.return_value = mock.MagicMock()
    var789.stat.st_size = 1024
    var2300 = mock.Mock()
    var2300.name = 'logo.png'
    var2300.open = mock.mock_open()
    var2300.with_name.return_value = var789
    var3618 = FileResponse(var2300)
    var3618._sendfile = make_mocked_coro(None)
    arg1111.run_until_complete(var3618.prepare(var2428))
    assert (not var2300.open.called)
    assert var789.open.called

def function1075(arg449):
    var911 = make_mocked_request('GET', 'http://python.org/logo.png', headers={})
    var2505 = mock.Mock()
    var2505.open = mock.mock_open()
    var2505.is_file.return_value = True
    var2750 = mock.Mock()
    var2750.name = 'logo.png'
    var2750.open = mock.mock_open()
    var2750.with_name.return_value = var2505
    var2750.stat.return_value = mock.MagicMock()
    var2750.stat.st_size = 1024
    var2254 = FileResponse(var2750)
    var2254._sendfile = make_mocked_coro(None)
    arg449.run_until_complete(var2254.prepare(var911))
    assert var2750.open.called
    assert (not var2505.open.called)

def function2154(arg2122):
    var3452 = make_mocked_request('GET', 'http://python.org/logo.png', headers={})
    var4044 = mock.Mock()
    var4044.open = mock.mock_open()
    var4044.is_file.return_value = False
    var1683 = mock.Mock()
    var1683.name = 'logo.png'
    var1683.open = mock.mock_open()
    var1683.with_name.return_value = var4044
    var1683.stat.return_value = mock.MagicMock()
    var1683.stat.st_size = 1024
    var4675 = FileResponse(var1683)
    var4675._sendfile = make_mocked_coro(None)
    arg2122.run_until_complete(var4675.prepare(var3452))
    assert var1683.open.called
    assert (not var4044.open.called)

def function182(arg2286):
    var2392 = make_mocked_request('GET', 'http://python.org/logo.png', headers={hdrs.ACCEPT_ENCODING: 'gzip', })
    var4676 = mock.Mock()
    var4676.open = mock.mock_open()
    var4676.is_file.return_value = False
    var3011 = mock.Mock()
    var3011.name = 'logo.png'
    var3011.open = mock.mock_open()
    var3011.with_name.return_value = var4676
    var3011.stat.return_value = mock.MagicMock()
    var3011.stat.st_size = 1024
    var410 = FileResponse(var3011)
    var410._sendfile = make_mocked_coro(None)
    arg2286.run_until_complete(var410.prepare(var2392))
    assert var3011.open.called
    assert (not var4676.open.called)