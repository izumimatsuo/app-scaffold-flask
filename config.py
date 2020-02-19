import os


class BaseConfig(object):
    DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://user01:user01@rdb/production')
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
