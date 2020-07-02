from marshmallow import ValidationError
from main.repositories.user import UserRepository
from main.extensions.exceptions.user import WrongLoginInfoException, InactiveUserException
from main.models import User
from .validate_error_code import ValidateErrorCode


class UserValidator:
    @staticmethod
    def login_info_validator(username_or_email, password) -> bool:
        user = UserRepository.get_by_username_or_email(username_or_email)
        if user and user.check_password(password):
            if not user.is_active:
                raise InactiveUserException
            return user
        else:
            raise WrongLoginInfoException

    @staticmethod
    def validate_uniqueness(field_name: str = None, **kwargs):
        user = UserRepository.get_by(**kwargs)
        if user is not None:
            key, value = next(iter(kwargs.items()))
            field_name = field_name if field_name else key
            raise ValidationError(field_name=field_name, message=ValidateErrorCode.IS_UNIQUE)
        return user
