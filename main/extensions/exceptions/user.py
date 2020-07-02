from http import HTTPStatus

from ..api_codes import APICode
from . import APIException


class WrongLoginInfoException(APIException):
    code = APICode.WRONG_LOGIN_INFO
    http_status = HTTPStatus.BAD_REQUEST

    def __init__(self, message=APICode.WRONG_LOGIN_INFO.description,
                 extra=None):
        super().__init__(
            code=APICode.WRONG_LOGIN_INFO,
            http_status=HTTPStatus.BAD_REQUEST,
            message=message,
            extra=extra
        )

    def __str__(self):
        return "login info wrong"


class InactiveUserException(APIException):
    code = APICode.USER_INACTIVE
    http_status = HTTPStatus.FORBIDDEN

    def __init__(self, message=APICode.USER_INACTIVE.description,
                 extra=None):
        super().__init__(
            code=APICode.USER_INACTIVE,
            http_status=HTTPStatus.FORBIDDEN,
            message=message,
            extra=extra
        )

    def __str__(self):
        return "user inactive"
