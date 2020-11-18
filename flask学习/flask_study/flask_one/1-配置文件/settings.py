class BaseConfig:
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'gsdagsdf'
    DATABASE_URL = 'splite://memory'


# 生产环境
class ProductionConfig(BaseConfig):
    pass


# 开发环境
class DevelopmentConfig(BaseConfig):
    pass


# 测试环境
class TestingConfig(BaseConfig):
    pass
