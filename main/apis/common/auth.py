import os
from flask import request
from flask_restplus import Namespace, Resource
from flask_accepts import responds
from main.helpers.decorators import accepts, accept_authorization
from .schemas.auth import (
    LoginRequestSchema,
    LoginSocialRequestSchema,
    RefreshRequestSchema,
    RefreshResponseSchema,
    LoginResponseSchema,
    AccountResponseSchema,
    RegisterRequestSchema
)
from ..schemas.base import IdOnlySchema
from main.services.auth import AuthService
from main.services.external.google import GoogleService
from main.services.external.facebook import FacebookService
from main.helpers.utils.authorization import AuthorizationUtils
from main.models.enums.provider import LoginProvider
from main.extensions.api_codes import APICode

api = Namespace('Common/Auth')


@api.route('/me', methods=['GET'])
class Account(Resource):
    @accepts(authorization=True)
    @responds(schema=AccountResponseSchema, api=api)
    def get(self):
        return {
            'user': request.user_extra,
        }


@api.route('/register', methods=['POST'])
class Register(Resource):
    @accepts(schema=RegisterRequestSchema, api=api)
    @responds(schema=IdOnlySchema, api=api)
    def post(self):
        params = request.parse_obj
        user = AuthService.register(params)
        return IdOnlySchema(
            id=user.id,
            context={
                'code': APICode.CREATE_SUCCESS,
                'message': APICode.CREATE_SUCCESS.description
            }
        )


@api.route('/login', methods=['POST'])
class Login(Resource):
    @accepts(schema=LoginRequestSchema, api=api)
    @responds(schema=LoginResponseSchema, api=api)
    def post(self):
        params = request.parse_obj
        user = AuthService.login(params)
        return AuthorizationUtils.gen_token_response(user)


@api.route('/login-social-network', methods=['POST'])
class LoginSocial(Resource):
    @accepts(schema=LoginSocialRequestSchema, api=api)
    @responds(schema=LoginResponseSchema, api=api)
    def post(self):
        params = request.parse_obj
        provider = params.get('provider')
        token = params.get('token')
        user = None
        if provider == LoginProvider.facebook:
            user = FacebookService.login_facebook(token)
        elif provider == LoginProvider.google:
            user = GoogleService.login_google(token)
        return AuthorizationUtils.gen_token_response(user)


@api.route('/refresh', methods=['POST'])
class TokenRefresh(Resource):
    @accepts(schema=RefreshRequestSchema, api=api)
    @responds(schema=RefreshResponseSchema, api=api)
    def post(self):
        params = request.parse_obj
        return AuthorizationUtils.gen_new_access_token(params.get('refresh_token'))
