from decouple import config


class Config():
    SECRET_KEY = config('SECRET_KEY', default='CorpTesla12_')


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}