import os
from flask import request
from flask_restplus import Namespace, Resource
from flask_accepts import responds
from main.helpers.decorators import accepts
from ..schemas.base import IdOnlySchema
from main.helpers.utils.authorization import AuthorizationUtils
from main.models.enums.provider import LoginProvider
from main.extensions.api_codes import APICode
from .schemas.user import (
    UserCreateRequestSchema,
    UserWithRoleResponseSchema,
    UsersGetRequestSchema,
    UsersGetResponseSchema,
)
from main.models.enums.action import Actions
from main.models.enums.resource import Resources
from main.helpers.utils.string import PERMISSION

api = Namespace('Admin/User')


@api.route('/', methods=['GET', 'POST'])
class Users(Resource):
    @accepts(
        schema=UsersGetRequestSchema,
        has_request_params=True,
        authorization=True,
        permissions=[PERMISSION(Resources.user, Actions.read)]
    )
    @responds(schema=UsersGetResponseSchema, api=api)
    def get(self):
        pass

    @accepts(
        schema=UserCreateRequestSchema,
        api=api,
        authorization=True,
        permissions=[PERMISSION(Resources.user, Actions.create)]
    )
    @responds(schema=IdOnlySchema, api=api)
    def post(self):
        pass


@api.route('/<int:user_id>', methods=['GET', 'PATCH', 'DELETE'])
class User(Resource):
    @accepts(
        authorization=True,
        permissions=[PERMISSION(Resources.user, Actions.read)]
    )
    @responds(schema=UserWithRoleResponseSchema, api=api)
    def get(self):
        pass

    @accepts(
        authorization=True,
        permissions=[PERMISSION(Resources.user, Actions.update)]
    )
    @responds(schema=IdOnlySchema, api=api)
    def patch(self):
        pass

    @accepts(
        authorization=True,
        permissions=[PERMISSION(Resources.user, Actions.delete)]
    )
    @responds(schema=IdOnlySchema, api=api)
    def delete(self):
        pass
