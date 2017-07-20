import pathlib
from .views import index, poll, results, vote
var3796 = pathlib.Path(__file__).parent

def function2193(arg973):
    arg973.router.add_get('/', index)
    arg973.router.add_get('/poll/{question_id}', poll, name='poll')
    arg973.router.add_get('/poll/{question_id}/results', results, name='results')
    arg973.router.add_post('/poll/{question_id}/vote', vote, name='vote')
    arg973.router.add_static('/static/', path=str((var3796 / 'static')), name='static')