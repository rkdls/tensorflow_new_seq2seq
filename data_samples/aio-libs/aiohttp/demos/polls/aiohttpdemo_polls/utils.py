import trafaret as T
var1909 = '^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}$'
var2313 = T.Dict({T.Key('postgres'): T.Dict({'database': T.String(), 'user': T.String(), 'password': T.String(), 'host': T.String(), 'port': T.Int(), 'minsize': T.Int(), 'maxsize': T.Int(), }), T.Key('host'): T.String(regex=var1909), T.Key('port'): T.Int(), })