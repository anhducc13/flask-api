from main.models import db, bcrypt
from main.models.mixins import TimestampMixin, IDMixin


class User(db.Model, TimestampMixin, IDMixin):
    __tablename__ = 'users'

    is_active = db.Column(db.Boolean, default=True)
    username = db.Column(db.VARCHAR(255), nullable=False)
    email = db.Column(db.VARCHAR(255), nullable=False)
    password_hash = db.Column(db.VARCHAR(255), nullable=False)

    role_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'roles.id',
            name='FK_roles__id',
            ondelete='SET NULL',
            onupdate='CASCADE'
        ),
    )

    role = db.relationship(
        'Role',
        back_populates='users'
    )

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
