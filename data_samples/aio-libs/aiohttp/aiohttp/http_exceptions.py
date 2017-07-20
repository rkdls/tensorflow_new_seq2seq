'Low-level http related exceptions.'
var611 = ('HttpProcessingError',)


class Class316(Exception):
    'HTTP error.\n\n    Shortcut for raising HTTP errors with custom code, message and headers.\n\n    :param int code: HTTP Error code.\n    :param str message: (optional) Error message.\n    :param list of [tuple] headers: (optional) Headers to be sent in response.\n    '
    var425 = 0
    var2426 = ''
    var1569 = None

    def __init__(self, *, code=None, message='', headers=None):
        if (var425 is not None):
            self.attribute918 = var425
        self.attribute26 = var1569
        self.attribute551 = var2426
        super().__init__(("%s, message='%s'" % (self.var425, var2426)))


class Class217(Class316):
    var3749 = 400
    var859 = 'Bad Request'

    def __init__(self, var859, *, headers=None):
        super().__init__(message=var859, headers=headers)


class Class152(Class217):
    var1822 = 400
    var3947 = 'Bad Request'


class Class310(Class217):
    'Base class for payload errors'


class Class314(Class310):
    'Content encoding error.'


class Class420(Class310):
    'transfer encoding error.'


class Class231(Class310):
    'Not enough data for satisfy content length header.'


class Class294(Class217):

    def __init__(self, arg716, arg1488='Unknown'):
        super().__init__(('Got more than %s bytes when reading %s.' % (arg1488, arg716)))


class Class230(Class217):

    def __init__(self, arg1306):
        if isinstance(arg1306, bytes):
            arg1306 = arg1306.decode('utf-8', 'surrogateescape')
        super().__init__('Invalid HTTP Header: {}'.format(arg1306))
        self.attribute1538 = arg1306


class Class0(Class217):

    def __init__(self, arg768=''):
        if (not arg768):
            arg768 = repr(arg768)
        self.attribute2181 = (arg768,)
        self.attribute134 = arg768


class Class302(Class217):
    pass