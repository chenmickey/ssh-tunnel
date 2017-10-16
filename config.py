class Config(object):
	DEBUG = False
	TESTING = False
	DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
	DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
	DEBUG = True


class TestingConfig(Config):
	PORT = 5555
	DEBUG = True
	TESTING = True
	SECRET_KEY = '...'
	SESSION_COOKIE_HTTPONLY = '...'
	SESSION_COOKIE_NAME = '...'
