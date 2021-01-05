import os


class BaseConfig:
    """
        Base Configuration
    """
    TESTING = False 
    JSONIFY_PRETTYPRINT_REGULAR = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'birth_is_death'


class DevelopmentConfig(BaseConfig):
    """
        Development Configuration   
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
    """
        Testing Configuration
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
    """
        Production Configuration
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
