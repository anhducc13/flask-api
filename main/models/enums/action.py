# coding=utf-8
from .base import BaseEnumModel


class Actions(BaseEnumModel):
    read_ui = 'read:ui'
    read = 'read'
    create = 'create'
    update = 'update'
    delete = 'delete'
