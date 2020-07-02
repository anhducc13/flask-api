from http import HTTPStatus

from ..api_codes import APICode
from . import APIException


class ExpiredTokenException(APIException):
    code = APICode.TOKEN_EXPIRED
    http_status = HTTPStatus.UNAUTHORIZED

    def __init__(self, message=APICode.TOKEN_EXPIRED.description,
                 extra=None):
        super().__init__(
            code=APICode.TOKEN_EXPIRED,
            http_status=HTTPStatus.UNAUTHORIZED,
            message=message,
            extra=extra
        )

    def __str__(self):
        return "token expired"


class ErrorTokenException(APIException):
    code = APICode.TOKEN_ERROR
    http_status = HTTPStatus.FORBIDDEN

    def __init__(self, message=APICode.TOKEN_ERROR.description,
                 extra=None):
        super().__init__(
            code=APICode.TOKEN_ERROR,
            http_status=HTTPStatus.FORBIDDEN,
            message=message,
            extra=extra
        )

    def __str__(self):
        return 'token error'


class RequiredTokenException(APIException):
    code = APICode.TOKEN_REQUIRED
    http_status = HTTPStatus.BAD_REQUEST

    def __init__(self, message=APICode.TOKEN_REQUIRED.description,
                 extra=None):
        super().__init__(
            code=APICode.TOKEN_REQUIRED,
            http_status=HTTPStatus.BAD_REQUEST,
            message=message,
            extra=extra
        )

    def __str__(self):
        return 'token required'


class ErrorLoginSocialException(APIException):
    code = APICode.ERROR_LOGIN_SOCIAL
    http_status = HTTPStatus.FORBIDDEN

    def __init__(self, message=APICode.ERROR_LOGIN_SOCIAL.description,
                 extra=None):
        super().__init__(
            code=APICode.ERROR_LOGIN_SOCIAL,
            http_status=HTTPStatus.FORBIDDEN,
            message=message,
            extra=extra
        )

    def __str__(self):
        return 'token required'


class NotPermissionException(APIException):
    code = APICode.NOT_HAVE_PERMISSION
    http_status = HTTPStatus.FORBIDDEN

    def __init__(self, message=APICode.NOT_HAVE_PERMISSION.description,
                 extra=None):
        super().__init__(
            code=APICode.NOT_HAVE_PERMISSION,
            http_status=HTTPStatus.FORBIDDEN,
            message=message,
            extra=extra
        )

    def __str__(self):
        return 'not have permission'
