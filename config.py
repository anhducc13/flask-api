import os
from datetime import timedelta, datetime
from dotenv import load_dotenv

_DOT_ENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(_DOT_ENV_PATH)

ROOT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__)
))

MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'test_db')
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PORT = os.getenv('MYSQL_PORT', '3306')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '123456')

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4'.format(
    MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE
)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.getenv('SECRET_KEY', 'ductt')
SECRET_KEY_REFRESH = os.getenv('SECRET_KEY_REFRESH', 'ductt')
ACCESS_TOKEN_EXPIRED_TIME = os.getenv('ACCESS_TOKEN_EXPIRED_TIME', 15*60)
REFRESH_TOKEN_EXPIRED_TIME = os.getenv('REFRESH_TOKEN_EXPIRED_TIME', 7 * 24 * 60 * 60)
