# coding=utf-8

from marshmallow import Schema, post_dump
from marshmallow.fields import Field, String, Integer, Date, List, Dict

from main.extensions.api_codes import APICode
from main.helpers.validators.validate_error_code import ValidateErrorCode
from main.helpers.validators.validate import ValidateRange


class BaseRequestSchema(Schema):
    Field.default_error_messages["required"] = ValidateErrorCode.IS_REQUIRED

    String.default_error_messages["invalid"] = ValidateErrorCode.INVALID_TYPE

    Integer.default_error_messages["invalid"] = ValidateErrorCode.INVALID_TYPE

    Date.default_error_messages["invalid"] = ValidateErrorCode.INVALID_FORMAT

    List.default_error_messages['invalid'] = ValidateErrorCode.INVALID_TYPE

    Schema._default_error_messages['unknown'] = ValidateErrorCode.UNKNOWN_FIELD

    Dict.default_error_messages['invalid'] = ValidateErrorCode.INVALID_TYPE


class BaseResponseSchema(Schema):
    # pylint: disable=unused-argument
    @post_dump(pass_original=True)
    def wrap(self, result, original, many, **kwargs):
        context = {}
        if isinstance(original, Schema):
            context = original.context
        return ResponseFormatter.format(result, context)


class ResponseFormatter:
    @staticmethod
    def format(result, context):
        response = {
            "code": APICode.DEFAULT,
            "message": APICode.DEFAULT.description,
            "result": result
        }

        if context.get('code'):
            response['code'] = context.get('code')

        if context.get('message'):
            response['message'] = context.get('message')

        if context.get('extra'):
            response['extra'] = context.get('extra')

        return response


class IdOnlySchema(BaseResponseSchema):
    # pylint: disable=invalid-name
    id = Integer(required=True)

    def __init__(self, **kwargs):
        super().__init__()
        self.id = kwargs.get('id')
        self.context = kwargs.get('context')


class ListRequestSchemaBasic(BaseRequestSchema):
    page = Integer(default=1, missing=1, validate=[
        ValidateRange(min=1)
    ])
    pageSize = Integer(attribute='page_size', default=10, missing=10, validate=[
        ValidateRange(min=1, max=200)
    ])
    query = String()


class ListResponseSchemaBasic(BaseResponseSchema):
    page = Integer(required=True)
    pageSize = Integer(attribute='page_size', required=True, validate=[
        ValidateRange(min=1, max=200)
    ])
    total = Integer(required=True)
