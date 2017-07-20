import pathlib
import subprocess
import pytest
from aiohttpdemo_polls.main import init
var4666 = pathlib.Path(__file__).parent.parent

@pytest.fixture
def function2509():
    var1803 = ((var4666 / 'config') / 'polls.yaml')
    return var1803.as_posix()

@pytest.fixture
def function2214(arg327, arg792, function2509):
    var136 = init(arg327, ['-c', function2509])
    return arg327.run_until_complete(arg792(var136))

@pytest.fixture
def function320():
    subprocess.call([((var4666 / 'sql') / 'install.sh').as_posix()], shell=True, cwd=var4666.as_posix())