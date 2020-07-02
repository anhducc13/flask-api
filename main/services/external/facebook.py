from main.models import User
from main.repositories.user import UserRepository
from main.extensions.exceptions.authorization import ErrorLoginSocialException
from main.extensions.exceptions.user import InactiveUserException
from main.helpers.utils.password import PasswordUtils
import requests

API_FACEBOOK = 'https://graph.facebook.com/me'
FIELDS = ['email', 'name', 'picture']


class FacebookService:
    @staticmethod
    def login_facebook(access_token) -> User:
        params = {
            'fields': ",".join(FIELDS),
            'access_token': access_token
        }
        result = requests.get(url=API_FACEBOOK, params=params)
        if result.status_code == 200:
            user_data = result.json()
            email = user_data.get('email')
            if email:
                user = UserRepository.get_by(email=email)
                if user:
                    if not user.is_active:
                        raise InactiveUserException
                    else:
                        return user
                else:
                    user_info = {
                        'email': email,
                        'username': email,
                        'password': PasswordUtils.generate_password()
                    }
                    user = UserRepository.create(user_info)
                    return user

        else:
            raise ErrorLoginSocialException

