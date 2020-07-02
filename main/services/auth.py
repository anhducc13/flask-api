from main.models import User
from main.repositories.user import UserRepository
from .schemas.auth import UserLogin, UserRegister
from main.helpers.decorators import accepts_logic


class AuthService:
    @staticmethod
    def login(payload) -> User:
        new_payload = accepts_logic(
            payload=payload,
            schema=UserLogin
        )
        return new_payload.get('user')

    @staticmethod
    def register(payload) -> User:
        payload = accepts_logic(payload=payload, schema=UserRegister)
        user = UserRepository.create(payload)
        return user

