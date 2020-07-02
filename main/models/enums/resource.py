# coding=utf-8
from .base import BaseEnumModel


class Resources(BaseEnumModel):
    user = 'user'
    role = 'role'
    permission = 'permission'
    role_permission = 'role_permission'
