from typing import Union, Type, List
from main.helpers.utils.authorization import AuthorizationUtils
from marshmallow import Schema, ValidationError
from main.extensions.exceptions.authorization import (
    ErrorTokenException,
    NotPermissionException
)
from flask_accepts.utils import for_swagger, get_default_model_name
from flask_accepts import accepts
from flask_restplus import reqparse
from main.extensions.exceptions.physical_validation import PhysicalValidationException


def accept_authorization():
    def decorator(func):
        def inner(*args, **kwargs):
            from flask import request
            bearer_token = request.headers.get('Authorization')
            if bearer_token and len(bearer_token.split(' ')) == 2:
                token = bearer_token.split(' ')[1]
                user = AuthorizationUtils.get_user_info(token)
                request.user_extra = user
            else:
                raise ErrorTokenException
            return func(*args, **kwargs)
        return inner
    return decorator


def accept_permissions(pers):
    def decorator(func):
        def inner(*args, **kwargs):
            from flask import request
            user = request.user_extra
            if user and user.role and user.role.has_all_permissions:
                return func(*args, **kwargs)
            permissions = []
            if user and user.permissions:
                permissions = user.permissions
            accept = all([(item in permissions) for item in pers])
            if accept:
                return func(*args, **kwargs)
            raise NotPermissionException
        return inner
    return decorator


def accepts(
        *args,
        schema: Schema = None,
        many=False,
        has_request_params=False,
        api=None,
        use_swagger: bool = True,
        authorization: bool = False,
        permissions=None
):
    if permissions is None:
        permissions = []
    if schema:
        schema = _get_or_create_schema(schema, many=many)
    query_params = [arg for arg in args if isinstance(arg, dict)]
    if api:
        _parser = api.parser()
    else:
        _parser = reqparse.RequestParser(bundle_errors=True)

    def decorator(func):
        from functools import wraps

        @wraps(func)
        def inner(*args, **kwargs):
            from flask import request
            user = None
            if authorization:
                bearer_token = request.headers.get('Authorization')
                if bearer_token and len(bearer_token.split(' ')) == 2:
                    token = bearer_token.split(' ')[1]
                    user = AuthorizationUtils.get_user_info(token)
                    request.user_extra = user
                else:
                    raise ErrorTokenException

            if permissions is not None and isinstance(permissions, List):
                if user and user.role and user.role.has_all_permissions:
                    return func(*args, **kwargs)
                user_permissions = []
                if user and user.permissions:
                    user_permissions = user.permissions
                accept = all([(item in user_permissions) for item in permissions])
                if not accept:
                    raise NotPermissionException
            if schema:
                if has_request_params:
                    try:
                        obj = schema.load(request.args)
                        request.parse_args = obj
                    except ValidationError:
                        raise PhysicalValidationException(message='The query param is not valid')

                else:
                    try:
                        obj = schema.load(request.get_json())
                        request.parse_obj = obj
                    except ValidationError as err:
                        raise PhysicalValidationException(extra=err.messages)

            return func(*args, **kwargs)

        if api and use_swagger:
            if schema:
                inner = api.doc(
                    params={qp["name"]: qp for qp in query_params},
                    body=for_swagger(
                        schema=schema,
                        model_name=get_default_model_name(schema),
                        api=api,
                        operation="load",
                    ),
                )(inner)
            elif _parser:
                inner = api.expect(_parser)(inner)
        return inner
    return decorator


def _get_or_create_schema(
        schema: Union[Schema, Type[Schema]], many: bool = False
) -> Schema:
    if isinstance(schema, Schema):
        return schema
    return schema(many=many)
