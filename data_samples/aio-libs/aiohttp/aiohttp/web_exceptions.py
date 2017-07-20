from .web_response import Response
var931 = ('HTTPException', 'HTTPError', 'HTTPRedirection', 'HTTPSuccessful', 'HTTPOk', 'HTTPCreated', 'HTTPAccepted', 'HTTPNonAuthoritativeInformation', 'HTTPNoContent', 'HTTPResetContent', 'HTTPPartialContent', 'HTTPMultipleChoices', 'HTTPMovedPermanently', 'HTTPFound', 'HTTPSeeOther', 'HTTPNotModified', 'HTTPUseProxy', 'HTTPTemporaryRedirect', 'HTTPPermanentRedirect', 'HTTPClientError', 'HTTPBadRequest', 'HTTPUnauthorized', 'HTTPPaymentRequired', 'HTTPForbidden', 'HTTPNotFound', 'HTTPMethodNotAllowed', 'HTTPNotAcceptable', 'HTTPProxyAuthenticationRequired', 'HTTPRequestTimeout', 'HTTPConflict', 'HTTPGone', 'HTTPLengthRequired', 'HTTPPreconditionFailed', 'HTTPRequestEntityTooLarge', 'HTTPRequestURITooLong', 'HTTPUnsupportedMediaType', 'HTTPRequestRangeNotSatisfiable', 'HTTPExpectationFailed', 'HTTPMisdirectedRequest', 'HTTPUnprocessableEntity', 'HTTPFailedDependency', 'HTTPUpgradeRequired', 'HTTPPreconditionRequired', 'HTTPTooManyRequests', 'HTTPRequestHeaderFieldsTooLarge', 'HTTPUnavailableForLegalReasons', 'HTTPServerError', 'HTTPInternalServerError', 'HTTPNotImplemented', 'HTTPBadGateway', 'HTTPServiceUnavailable', 'HTTPGatewayTimeout', 'HTTPVersionNotSupported', 'HTTPVariantAlsoNegotiates', 'HTTPInsufficientStorage', 'HTTPNotExtended', 'HTTPNetworkAuthenticationRequired')


class Class417(Response, Exception):
    var1342 = None
    var3882 = False

    def __init__(self, *, headers=None, reason=None, body=None, text=None, content_type=None):
        Response.__init__(self, status=self.var1342, headers=headers, reason=reason, body=body, text=text, content_type=content_type)
        Exception.__init__(self, self.reason)
        if ((self.body is None) and (not self.var3882)):
            self.attribute1716 = '{}: {}'.format(self.status, self.reason)


class Class238(Class417):
    'Base class for exceptions with status codes in the 400s and 500s.'


class Class437(Class417):
    'Base class for exceptions with status codes in the 300s.'


class Class145(Class417):
    'Base class for exceptions with status codes in the 200s.'


class Class323(Class145):
    var1735 = 200


class Class189(Class145):
    var3889 = 201


class Class42(Class145):
    var2332 = 202


class Class77(Class145):
    var3039 = 203


class Class278(Class145):
    var1746 = 204
    var190 = True


class Class53(Class145):
    var652 = 205
    var4692 = True


class Class27(Class145):
    var4126 = 206


class Class277(Class437):

    def __init__(self, arg436, *, headers=None, reason=None, body=None, text=None, content_type=None):
        if (not arg436):
            raise ValueError('HTTP redirects need a location to redirect to.')
        super().__init__(headers=headers, reason=reason, body=body, text=text, content_type=content_type)
        self.headers['Location'] = str(arg436)
        self.attribute647 = arg436


class Class180(Class277):
    var1538 = 300


class Class171(Class277):
    var3368 = 301


class Class62(Class277):
    var4363 = 302


class Class202(Class277):
    var3392 = 303


class Class438(Class437):
    var3706 = 304
    var209 = True


class Class159(Class277):
    var3729 = 305


class Class173(Class277):
    var2592 = 307


class Class31(Class277):
    var3045 = 308


class Class157(Class238):
    pass


class Class248(Class157):
    var3394 = 400


class Class347(Class157):
    var3598 = 401


class Class399(Class157):
    var213 = 402


class Class232(Class157):
    var2696 = 403


class Class102(Class157):
    var925 = 404


class Class413(Class157):
    var1710 = 405

    def __init__(self, arg685, arg1731, *, headers=None, reason=None, body=None, text=None, content_type=None):
        var2477 = ','.join(sorted(arg1731))
        super().__init__(headers=headers, reason=reason, body=body, text=text, content_type=content_type)
        self.headers['Allow'] = var2477
        self.attribute725 = arg1731
        self.attribute1307 = arg685.upper()


class Class260(Class157):
    var309 = 406


class Class108(Class157):
    var1161 = 407


class Class344(Class157):
    var4127 = 408


class Class357(Class157):
    var3399 = 409


class Class195(Class157):
    var2220 = 410


class Class100(Class157):
    var440 = 411


class Class46(Class157):
    var1636 = 412


class Class38(Class157):
    var2027 = 413


class Class93(Class157):
    var4258 = 414


class Class218(Class157):
    var4298 = 415


class Class25(Class157):
    var3103 = 416


class Class116(Class157):
    var3131 = 417


class Class227(Class157):
    var101 = 421


class Class87(Class157):
    var53 = 422


class Class11(Class157):
    var927 = 424


class Class259(Class157):
    var1717 = 426


class Class200(Class157):
    var4376 = 428


class Class214(Class157):
    var3988 = 429


class Class142(Class157):
    var2559 = 431


class Class40(Class157):
    var4701 = 451

    def __init__(self, arg2000, *, headers=None, reason=None, body=None, text=None, content_type=None):
        super().__init__(headers=headers, reason=reason, body=body, text=text, content_type=content_type)
        self.headers['Link'] = ('<%s>; rel="blocked-by"' % arg2000)
        self.attribute2101 = arg2000


class Class9(Class238):
    pass


class Class151(Class9):
    var2039 = 500


class Class134(Class9):
    var4064 = 501


class Class192(Class9):
    var3528 = 502


class Class101(Class9):
    var63 = 503


class Class352(Class9):
    var2240 = 504


class Class419(Class9):
    var2301 = 505


class Class205(Class9):
    var151 = 506


class Class251(Class9):
    var4349 = 507


class Class424(Class9):
    var4218 = 510


class Class281(Class9):
    var3117 = 511