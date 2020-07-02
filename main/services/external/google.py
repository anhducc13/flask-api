import requests
from main.models import User
from main.repositories.user import UserRepository
from main.extensions.exceptions.authorization import ErrorLoginSocialException
from main.extensions.exceptions.user import InactiveUserException
from main.helpers.utils.password import PasswordUtils

API_GOOGLE = 'https://oauth2.googleapis.com/tokeninfo'


class GoogleService:
    @staticmethod
    def login_google(id_token) -> User:
        params = {
            'id_token': id_token
        }
        result = requests.get(url=API_GOOGLE, params=params)
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
        raise ErrorLoginSocialException

