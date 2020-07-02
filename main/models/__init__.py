import flask_migrate as _fm
import flask_sqlalchemy as _fs
import flask_bcrypt as _fb

db = _fs.SQLAlchemy()
migrate = _fm.Migrate(db=db)
bcrypt = _fb.Bcrypt()


def init_app(app, **kwargs):
    db.app = app
    migrate.init_app(app)
    db.init_app(app)


from .user import User
from .role import Role
from .role_permission import RolePermission
from .permission import Permission