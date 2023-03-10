import os
class Config:
    SECRET_KEY=os.urandom(32)
    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(Config):
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"


class ProductionConfig(Config):
    DEBUG= False
    SQLALCHEMY_DATABASE_URI = "postgresql://kemo:12345@localhost:5432/project3"



projectConfig= {
    'dev': DevelopmentConfig,
    'prd': ProductionConfig
}
