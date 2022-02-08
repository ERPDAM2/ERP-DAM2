class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigTest(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///../test.db?check_same_thread=False"
    SECRET_KEY = "TESTKEY1234"
