from flask_restplus import Api

from .version import api as version_ns
from .common.auth import api as common_auth_ns

from .admin.user import api as user_auth_ns
from .admin.role import api as role_auth_ns
from .admin.permission import api as permission_auth_ns

authorizations = {

}

api = Api(title='Test API', version='0.0.1', authorizations=authorizations)

api.add_namespace(version_ns, path="/getversion")
api.add_namespace(common_auth_ns, path="/common/auth")

api.add_namespace(user_auth_ns, path="/admin/users")
api.add_namespace(role_auth_ns, path="/admin/roles")
api.add_namespace(permission_auth_ns, path="/admin/permissions")
