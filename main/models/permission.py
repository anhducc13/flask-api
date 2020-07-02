from main.models import db
from main.models.mixins import TimestampMixin, IDMixin


class Permission(db.Model, TimestampMixin, IDMixin):
    __tablename__ = 'permissions'

    is_active = db.Column(db.Boolean, default=True)
    name = db.Column(db.VARCHAR(255), nullable=False)
    code = db.Column(db.VARCHAR(20), nullable=False)

    roles = db.relationship('Role', secondary='role_permissions')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
