import jwt
from datetime import datetime, timedelta
from config import (
    SECRET_KEY,
    SECRET_KEY_REFRESH,
    ACCESS_TOKEN_EXPIRED_TIME,
    REFRESH_TOKEN_EXPIRED_TIME
)
from jwt.exceptions import ExpiredSignatureError
from main.extensions.exceptions.authorization import (
    ErrorTokenException,
    ExpiredTokenException,
)
from main.repositories.user import UserRepository


class AuthorizationUtils:
    @staticmethod
    def get_user_info(token):
        try:
            info = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id = info.get('user_id')
            if user_id:
                user = UserRepository.get_by(id=user_id)
                if user:
                    if user.role and user.role.is_active:
                        user.role = user.role
                        user.permissions = [item.code for item in user.role.permissions if item.is_active]
                    return user
                else:
                    raise ErrorTokenException
            else:
                raise ErrorTokenException
        except ExpiredSignatureError:
            raise ExpiredTokenException
        except Exception:
            raise ErrorTokenException

    @staticmethod
    def gen_token_response(user):
        payload_access = {
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(seconds=ACCESS_TOKEN_EXPIRED_TIME)
        }
        payload_refresh = {
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(seconds=REFRESH_TOKEN_EXPIRED_TIME)
        }
        access_token = jwt.encode(payload_access, SECRET_KEY)
        refresh_token = jwt.encode(payload_refresh, SECRET_KEY_REFRESH)
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'expired_refresh_token': REFRESH_TOKEN_EXPIRED_TIME,
        }

    @staticmethod
    def gen_new_access_token(refresh_token):
        try:
            info = jwt.decode(refresh_token, SECRET_KEY_REFRESH, algorithms=['HS256'])
            user_id = info.get('user_id')
            if user_id:
                user = UserRepository.get_by(id=user_id)
                if user:
                    payload_access = {
                        'user_id': user.id,
                        'exp': datetime.utcnow() + timedelta(seconds=ACCESS_TOKEN_EXPIRED_TIME)
                    }
                    access_token = jwt.encode(payload_access, SECRET_KEY)
                    return {
                        'new_access_token': access_token,
                    }
                else:
                    raise ErrorTokenException
            else:
                raise ErrorTokenException
        except ExpiredSignatureError:
            raise ExpiredTokenException
        except Exception:
            raise ErrorTokenException


