class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigTest(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///../test.db"
    SECRET_KEY = "TESTKEY1234"
