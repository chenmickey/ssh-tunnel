class Config(object):
	PORT = 5555
	DEBUG = True
	TESTING = True
	SECRET_KEY = '...'
	SESSION_COOKIE_HTTPONLY = '...'
	SESSION_COOKIE_NAME = '...'


class ProductionConfig(Config):
	PORT = 5555
	DEBUG = True
	TESTING = True
	SECRET_KEY = '...'
	SESSION_COOKIE_HTTPONLY = '...'
	SESSION_COOKIE_NAME = '...'


class DevelopmentConfig(Config):
	PORT = 5555
	DEBUG = True
	TESTING = True
	SECRET_KEY = '...'
	SESSION_COOKIE_HTTPONLY = '...'
	SESSION_COOKIE_NAME = '...'


class TestingConfig(Config):
	PORT = 5555
	DEBUG = True
	TESTING = True
	SECRET_KEY = '...'
	SESSION_COOKIE_HTTPONLY = '...'
	SESSION_COOKIE_NAME = '...'
