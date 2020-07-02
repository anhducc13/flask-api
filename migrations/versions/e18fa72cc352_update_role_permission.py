"""update_role_permission

Revision ID: e18fa72cc352
Revises: 090d55b2cb86
Create Date: 2020-06-30 15:51:36.840373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e18fa72cc352'
down_revision = '090d55b2cb86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('role_permissions_ibfk_2', 'role_permissions', type_='foreignkey')
    op.drop_constraint('role_permissions_ibfk_1', 'role_permissions', type_='foreignkey')
    op.create_foreign_key(None, 'role_permissions', 'permissions', ['permission_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'role_permissions', 'roles', ['role_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'role_permissions', type_='foreignkey')
    op.drop_constraint(None, 'role_permissions', type_='foreignkey')
    op.create_foreign_key('role_permissions_ibfk_1', 'role_permissions', 'permissions', ['permission_id'], ['id'])
    op.create_foreign_key('role_permissions_ibfk_2', 'role_permissions', 'roles', ['role_id'], ['id'])
    # ### end Alembic commands ###