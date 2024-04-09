import os
from dotenv import load_dotenv

load_dotenv("../.env.database")

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_precious_secret_key')

    DATABASE_HOST = os.environ.get('DB_HOST', 'localhost')
    DATABASE_USER = os.environ.get('DB_USER', 'postgres')
    DATABASE_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
    
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False