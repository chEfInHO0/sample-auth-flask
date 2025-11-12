from os import environ


class Config:
    SECRET_KEY = environ.get('SECRET_KEY', 'default_secret')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_HTTPONLY = environ.get('SESSION_COOKIE_HTTPONLY', True)
    SESSION_COOKIE_SECURE = environ.get('SESSION_COOKIE_SECURE', False)
    SESSION_COOKIE_SAMESITE = environ.get('SESSION_COOKIE_SAMESITE', 'Lax')
