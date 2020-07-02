# coding=utf-8
from .base import BaseEnumModel


class LoginProvider(BaseEnumModel):
    google = 'google'
    facebook = 'facebook'
