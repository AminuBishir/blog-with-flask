import os
class Config(object):
	DEBUG = False
	TESTING = False
	
	SECRET_KEY = os.environ.get("SECRET_KEY","")
	UPLOAD_FOLDER = 'D:/AMINU BISHIR/AMINU BISHIR/PROGRAMMING/Full Stack Web/fullstack-nanodegree-vm/vagrant/sadarwa-blog/image'
	
	SESSION_COOKIE_SECURE = True
	
class ProductionConfig(Config):
	pass
	
class DevelopmentConfig(Config):
	DB_NAME = 'development-db'
	DB_USERNAME = 'vagrant'
	DB_PASSWORD = '8754'
	DEBUG = True
	SESSION_COOKIE_SECURE = False
	
class TestingConfig(Config):
	DB_NAME = 'development-db'
	DB_USERNAME = 'vagrant'
	DB_PASSWORD = '8754'
	TESTING = True
	SESSION_COOKIE_SECURE = False
