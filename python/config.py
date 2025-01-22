DATABASE_CONFIG = {
    'user': 'root',
    'password': 'root',
    'host': 'mysql',
    'port': '3306',
    'database': 'db'
}

class Config:
    DEBUG = True
    TESTING = False
    DATABASE_CONFIG = DATABASE_CONFIG

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True