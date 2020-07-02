from marshmallow import Schema, validates_schema
from main.helpers.validators.user import UserValidator


class UserLogin(Schema):
    @validates_schema
    def login_info(self, payload, **kwargs):
        user = UserValidator.login_info_validator(
            username_or_email=payload.get('username_or_email'),
            password=payload.get('password')
        )
        payload['user'] = user


class UserRegister(Schema):
    @validates_schema
    def username(self, payload, **kwargs):
        UserValidator.validate_uniqueness(username=payload.get('username'))

    @validates_schema
    def email(self, payload, **kwargs):
        UserValidator.validate_uniqueness(email=payload.get('email'))
