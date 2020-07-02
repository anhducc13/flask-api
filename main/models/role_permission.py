import logging

from sqlalchemy.orm import backref

from . import db
from .mixins import TimestampMixin, IDMixin

logger = logging.getLogger('main')


class RolePermission(db.Model, TimestampMixin):
    __tablename__ = 'role_permissions'

    role_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'roles.id',
            ondelete='CASCADE',
            onupdate='CASCADE'
        ),
        primary_key=True
    )
    permission_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'permissions.id',
            ondelete='CASCADE',
            onupdate='CASCADE'
        ),
        primary_key=True
    )

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
