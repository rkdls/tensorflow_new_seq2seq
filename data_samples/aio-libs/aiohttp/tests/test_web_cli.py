import pytest
from aiohttp import web

def function293(arg1527):
    var673 = arg1527.patch('aiohttp.web.ArgumentParser.error', side_effect=SystemExit)
    var4097 = ['']
    with pytest.raises(SystemExit):
        web.main(var4097)
    var673.assert_called_with("'entry-func' not in 'module:function' syntax")

def function1319(arg2022):
    var1528 = ['test']
    var4705 = arg2022.patch('aiohttp.web.ArgumentParser.error', side_effect=SystemExit)
    with pytest.raises(SystemExit):
        web.main(var1528)
    var4705.assert_called_with("'entry-func' not in 'module:function' syntax")

def function2685(arg715):
    var3145 = [':test']
    var3604 = arg715.patch('aiohttp.web.ArgumentParser.error', side_effect=SystemExit)
    with pytest.raises(SystemExit):
        web.main(var3145)
    var3604.assert_called_with("'entry-func' not in 'module:function' syntax")

def function2150(arg308):
    var4296 = [':']
    var4420 = arg308.patch('aiohttp.web.ArgumentParser.error', side_effect=SystemExit)
    with pytest.raises(SystemExit):
        web.main(var4296)
    var4420.assert_called_with("'entry-func' not in 'module:function' syntax")

def function549(arg1274):
    var1960 = ['.a.b:c']
    var3510 = arg1274.patch('aiohttp.web.ArgumentParser.error', side_effect=SystemExit)
    with pytest.raises(SystemExit):
        web.main(var1960)
    var3510.assert_called_with('relative module names not supported')

def function2675(arg1922):
    var43 = ['alpha.beta:func']
    arg1922.patch('aiohttp.web.import_module', side_effect=ImportError('Test Error'))
    var3849 = arg1922.patch('aiohttp.web.ArgumentParser.error', side_effect=SystemExit)
    with pytest.raises(SystemExit):
        web.main(var43)
    var3849.assert_called_with('unable to import alpha.beta: Test Error')

def function929(arg1294):
    var2706 = ['alpha.beta:func']
    var4584 = arg1294.patch('aiohttp.web.import_module')
    var1603 = arg1294.patch('aiohttp.web.ArgumentParser.error', side_effect=SystemExit)
    var3005 = var4584('alpha.beta')
    del var3005.func
    with pytest.raises(SystemExit):
        web.main(var2706)
    var1603.assert_called_with(('module %r has no attribute %r' % ('alpha.beta', 'func')))

def function1834(arg1452, arg684):
    var3665 = '--path=test_path.sock alpha.beta:func'.split()
    arg1452.patch('aiohttp.web.import_module')
    arg684.delattr('socket.AF_UNIX', raising=False)
    var3957 = arg1452.patch('aiohttp.web.ArgumentParser.error', side_effect=SystemExit)
    with pytest.raises(SystemExit):
        web.main(var3665)
    var3957.assert_called_with('file system paths not supported by your operating environment')

def function979(arg880):
    arg880.patch('aiohttp.web.run_app')
    var293 = arg880.patch('aiohttp.web.import_module')
    var3718 = '-H testhost -P 6666 --extra-optional-eins alpha.beta:func --extra-optional-zwei extra positional args'.split()
    var280 = var293('alpha.beta')
    with pytest.raises(SystemExit):
        web.main(var3718)
    var280.func.assert_called_with('--extra-optional-eins --extra-optional-zwei extra positional args'.split())

def function2119(arg2013):
    var532 = arg2013.patch('aiohttp.web.run_app')
    var1134 = arg2013.patch('aiohttp.web.import_module')
    var2291 = arg2013.patch('aiohttp.web.ArgumentParser.exit', side_effect=SystemExit)
    var3769 = '-H testhost -P 6666 --extra-optional-eins alpha.beta:func --extra-optional-zwei extra positional args'.split()
    var3114 = var1134('alpha.beta')
    var2052 = var3114.func()
    with pytest.raises(SystemExit):
        web.main(var3769)
    var532.assert_called_with(var2052, host='testhost', port=6666, path=None)
    var2291.assert_called_with(message='Stopped\n')