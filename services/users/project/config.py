

class BaseConfig:
    """
        Base Configuration
    """

    TESTING = False 
    JSONIFY_PRETTYPRINT_REGULAR = False

class DevelopmentConfig(BaseConfig):
    """
        Development Configuration   
    """
    pass

class TestingConfig(BaseConfig):
    """
        Testing Configuration
    """
    TESTING = True

class ProductionConfig(BaseConfig):
    """
        Production Configuration
    """
    pass


