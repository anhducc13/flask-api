from marshmallow import Schema, post_load, EXCLUDE
from marshmallow.fields import Nested, List, Integer, String, Date, Boolean, DateTime

from main.helpers.utils.string import StringUtils
from main.helpers.validators import ValidateLength, ValidateNumbersOnly, \
    ValidateNumbersAndLettersOnly, ValidateAcceptableDate, ValidateEmail
from main.helpers.validators.validate import ValidateEnum, ValidateList
from ...schemas.base import BaseResponseSchema, BaseRequestSchema


class RoleSchema(Schema):
    id = Integer(required=True)
    code = String(required=True)
    name = String(required=True)
    isActive = Boolean(required=True, attribute='is_active')
    createdAt = DateTime(attribute='created_at')
    updatedAt = DateTime(attribute='updated_at')
    hasAllPermissions = Boolean(required=True, attribute='has_all_permissions')
