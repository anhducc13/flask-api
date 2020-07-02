import os
from flask import request
from flask_restplus import Namespace, Resource
from flask_accepts import responds
from main.helpers.decorators import accepts, accept_authorization, accept_permissions
from ..schemas.base import IdOnlySchema
from main.helpers.utils.authorization import AuthorizationUtils
from main.models.enums.provider import LoginProvider
from main.extensions.api_codes import APICode
from main.models.enums.action import Actions
from main.models.enums.resource import Resources
from main.helpers.utils.string import PERMISSION

api = Namespace('Admin/Role')


@api.route('/', methods=['GET', 'POST'])
class Roles(Resource):
    @accepts(
        authorization=True,
        permissions=[PERMISSION(Resources.role, Actions.read)]
    )
    def get(self):
        pass

    @accepts(
        authorization=True,
        permissions=[PERMISSION(Resources.role, Actions.create)]
    )
    @responds(IdOnlySchema)
    def post(self):
        pass


@api.route('/<int:role_id>', methods=['GET', 'PATCH', 'DELETE'])
class Role(Resource):
    @accepts(
        authorization=True,
        permissions=[PERMISSION(Resources.role, Actions.read)]
    )
    def get(self):
        pass

    @accepts(
        authorization=True,
        permissions=[PERMISSION(Resources.role, Actions.update)]
    )
    def patch(self):
        pass

    @accepts(
        authorization=True,
        permissions=[PERMISSION(Resources.role, Actions.delete)]
    )
    def delete(self):
        pass


@api.route('/<int:role_id>/permissions/bulk-create', methods=['POST'])
class RolePermissionCreate(Resource):
    @accepts(
        authorization=True,
        permissions=[PERMISSION(Resources.role_permission, Actions.create)]
    )
    def post(self):
        pass


@api.route('/<int:role_id>/permissions/get-all', methods=['GET'])
class RolePermissionGetAll(Resource):
    @accepts(
        authorization=True,
        permissions=[PERMISSION(Resources.role_permission, Actions.read)]
    )
    def get(self):
        pass


@api.route('/<int:role_id>/permissions/available', methods=['GET'])
class RolePermissionGetAvailable(Resource):
    @accepts(
        authorization=True,
        permissions=[PERMISSION(Resources.role_permission, Actions.read)]
    )
    def get(self):
        pass


@api.route('/<int:role_id>/permissions/<int:permission_id>', methods=['DELETE'])
class RolePermissionDelete(Resource):
    @accepts(
        authorization=True,
        permissions=[PERMISSION(Resources.role_permission, Actions.delete)]
    )
    def delete(self):
        pass
