from sqlalchemy.orm import backref
from main.models import db
from main.models.mixins import TimestampMixin, IDMixin


class Role(db.Model, TimestampMixin, IDMixin):
    __tablename__ = 'roles'

    is_active = db.Column(db.Boolean, default=True)
    name = db.Column(db.VARCHAR(255), nullable=False)
    code = db.Column(db.VARCHAR(20), nullable=False)
    has_all_permissions = db.Column(db.Boolean, default=False)

    users = db.relationship(
        'User',
        back_populates='role'
    )

    permissions = db.relationship('Permission', secondary='role_permissions')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
