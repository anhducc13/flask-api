from sqlalchemy import func, or_
from main.models import User, db


class UserRepository:
    @staticmethod
    def get_by(**kwargs):
        key, value = next(iter(kwargs.items()))
        return User.query.filter(
            func.lower(getattr(User, key)) == str(value).lower()
        ).first()

    @staticmethod
    def get_by_username_or_email(text):
        return User.query.filter(
            or_(
                User.username == text,
                User.email == text
            )
        ).first()

    @staticmethod
    def create(user_params: dict) -> User:
        user = User(**user_params)
        db.session.add(user)
        db.session.commit()

        return user
