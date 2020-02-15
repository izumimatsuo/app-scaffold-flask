import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}/{database}'.format(
        **{
          'user': os.getenv('DB_USER', 'user01'),
          'password': os.getenv('DB_PASSWORD', 'user01'),
          'host': os.getenv('DB_HOST', 'rdb'),
          'database': os.getenv('DB_DATABASE', 'development'),
        })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
