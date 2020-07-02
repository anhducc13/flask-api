import os
from flask import request
from flask_restplus import Namespace, Resource
from flask_accepts import responds
from main.helpers.decorators import accepts, accept_authorization
from ..schemas.base import IdOnlySchema
from main.helpers.utils.authorization import AuthorizationUtils
from main.models.enums.provider import LoginProvider
from main.extensions.api_codes import APICode

api = Namespace('Admin/Permission')


@api.route('/', methods=['GET', 'POST'])
class Permissions(Resource):
    @accept_authorization()
    def get(self):
        pass

    @accept_authorization()
    def post(self):
        pass


@api.route('/<int:permission_id>', methods=['GET', 'PATCH', 'DELETE'])
class Permission(Resource):
    @accept_authorization()
    def get(self):
        pass

    @accept_authorization()
    def patch(self):
        pass

    @accept_authorization()
    def delete(self):
        pass

