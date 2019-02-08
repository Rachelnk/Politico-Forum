import os
#Parent configuration class
class Config():
    DEBUG = False
    SECRET = os.getenv('SECRET')

#Configurations for Development
class DevelopmentConfig(Config):
    DEBUG= True

#configurations for the testing
class TestingConfig(Config):
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
