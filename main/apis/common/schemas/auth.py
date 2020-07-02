from marshmallow import Schema, post_load, EXCLUDE
from marshmallow.fields import Nested, List, Integer, String, Date, Boolean

from main.helpers.utils.string import StringUtils
from main.helpers.validators import ValidateLength, ValidateNumbersOnly, \
    ValidateNumbersAndLettersOnly, ValidateAcceptableDate, ValidateEmail
from main.helpers.validators.validate import ValidateEnum, ValidateList
from ...schemas.base import BaseResponseSchema, BaseRequestSchema
from main.models.enums.provider import LoginProvider


class LoginRequestSchema(BaseRequestSchema):
    usernameOrEmail = String(required=True, attribute='username_or_email', validate=[
        ValidateLength(min=1, max=255)
    ])
    password = String(required=True, validate=[
        ValidateLength(min=1, max=255)
    ])


class LoginResponseSchema(BaseResponseSchema):
    accessToken = String(required=True, attribute='access_token')
    refreshToken = String(required=True, attribute='refresh_token')
    expiredRefreshToken = Integer(required=True, attribute='expired_refresh_token')


class LoginSocialRequestSchema(BaseRequestSchema):
    token = String(required=True, validate=[
        ValidateLength(min=1)
    ])
    provider = String(required=True, validate=[
        ValidateEnum(LoginProvider)
    ])


class RefreshRequestSchema(BaseRequestSchema):
    refreshToken = String(required=True, attribute='refresh_token', validate=[
        ValidateLength(min=1)
    ])


class RefreshResponseSchema(BaseRequestSchema):
    newAccessToken = String(required=True, attribute='new_access_token')


class RegisterRequestSchema(BaseRequestSchema):
    username = String(required=True, validate=[
        ValidateLength(min=6, max=255),
        ValidateNumbersAndLettersOnly()
    ])
    email = String(required=True, validate=[
        ValidateEmail()
    ])
    password = String(required=True, validate=[
        ValidateLength(min=6, max=255),
        ValidateNumbersAndLettersOnly()
    ])


class User(Schema):
    id = Integer(required=True)
    username = String(required=True)
    email = String(required=True)
    isActive = Boolean(required=True, attribute='is_active')


class Role (Schema):
    id = Integer(required=True)
    code = String(required=True)
    name = String(required=True)


class UserWithRoleAndPermissions(User):
    role = Nested(Role)
    permissions = List(String())


class AccountResponseSchema(BaseResponseSchema):
    user = Nested(UserWithRoleAndPermissions, many=True)


