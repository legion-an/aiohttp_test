import pathlib

from gino.ext.aiohttp import Gino


BASE_DIR = pathlib.Path(__file__).parent.parent


SHARED_SECRET_KEY = 'dskaty3786219tgedusadnhjouid12-0hnduj-inq3123'


DEBUG = False

HOST = '127.0.0.1'
PORT = '8000'


DATABASE = {
    'drivername': 'postgresql',
    'user': '',
    'password': '',
    'host': '',
    'port': '',
    'database': '',
    'username': ''
}


DB = Gino()

try:
    from .settings_local import *
except ImportError:
    pass