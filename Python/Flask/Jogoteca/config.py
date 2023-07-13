import os

SECRET_KEY = 'alura'

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:4093@127.0.0.1/jogoteca'
