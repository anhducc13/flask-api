from marshmallow import Schema, post_load, EXCLUDE
from marshmallow.fields import Nested, List, Integer, String, Date, Boolean, DateTime

from main.helpers.utils.string import StringUtils
from main.helpers.validators import ValidateLength, ValidateNumbersOnly, \
    ValidateNumbersAndLettersOnly, ValidateAcceptableDate, ValidateEmail
from main.helpers.validators.validate import ValidateEnum, ValidateList, ValidateRange
from ...schemas.base import BaseResponseSchema, BaseRequestSchema, ListRequestSchemaBasic, ListResponseSchemaBasic
from main.models.enums.provider import LoginProvider
from .role import RoleSchema


class UserSchema(Schema):
    id = Integer(required=True)
    username = String(required=True)
    email = String(required=True)
    isActive = Boolean(required=True, attribute='is_active')
    createdAt = DateTime(attribute='created_at')
    updatedAt = DateTime(attribute='updated_at')


class UserCreateRequestSchema(BaseRequestSchema):
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
    isActive = Boolean(required=True, attribute='is_active')
    roleId = Integer(required=True, attribute='role_id')


class UserWithRoleSchema(UserSchema):
    role = Nested(RoleSchema)


class UserWithRoleResponseSchema(BaseResponseSchema):
    user = Nested(UserWithRoleSchema)


class UsersGetRequestSchema(ListRequestSchemaBasic):
    isActive = Integer(attribute='is_active', required=False, validate=[
        ValidateRange(min=0, max=1)
    ])


class UsersGetResponseSchema(ListResponseSchemaBasic):
    users = Nested(UserWithRoleSchema, many=True)





