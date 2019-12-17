from flask import Flask,render_template, request, redirect, url_for,make_response,jsonify, session as login_session
import string
import os
import random
import psycopg2
import bleach
from werkzeug.utils import secure_filename
import flask_login



'''template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)
'''


def create_app():
#create app and register blueprints
	app = Flask("__main__")
	
	loginManager = flask_login.LoginManager()
	loginManager.login_view = 'views.login'
	loginManager.init_app(app)
	#import blueprints
	from views import bp as views_bp
	from validation import bp as validators_bp
	from auth import bp as auth_bp
	from forms import bp as forms_bp
	from models import bp as db_bp



	app.register_blueprint(views_bp)
	app.register_blueprint(validators_bp)
	app.register_blueprint(auth_bp)
	app.register_blueprint(forms_bp)
	app.register_blueprint(db_bp)
	return app







'''
def blog_key(name='default'):
	return db.Key.from_path('blogs',name)

#parent key for users
def user_key(name='user-parent'):
	return db.Key.from_path('users',name)
def comment_key(name='comment'):
	return db.Key.from_path('comment',name)


class User(db.Model):
	
	name = db.StringProperty(required = True)
	password = db.StringProperty(required = True)
	email = db.StringProperty(required = True)
	def by_id(self,uid):
		return self.get_by_id(uid)
class Blog(db.Model):
	
	id = db.IntegerProperty()
	subject = db.StringProperty(required=True)
	content = db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add = True)
	last_modified = db.DateTimeProperty(auto_now = True)
	author = db.StringProperty()
	
	def by_id(self,blog_id):
		return self.get_by_id(blog_id)
	
	
	def render(self):
		self._render_text = self.content.replace('/n','<br>')
		return render('post.htm', p=self)
class Comment(db.Model):
	post_id = db.StringProperty(required=True)
	commentor = db.ReferenceProperty(User)
	commentor_id = db.StringProperty(required = True)
	comment = db.TextProperty(required=True)
	date = db.DateTimeProperty(auto_now_add = True)
	
class Like(db.Model):
	post_id = db.StringProperty(required = True)
	liked_by_id = db.StringProperty(required = True)
	liked_by = db.ReferenceProperty(User)
	date_like = db.DateTimeProperty(auto_now_add = True)
'''	

#get single user from db



if __name__ == '__main__':
	app = create_app()
	if app.config["ENV"] == 'production':
		app.config.from_object("config.ProductionConfig")
	else:
		app.config.from_object("config.DevelopmentConfig")
	app.run(host='0.0.0.0',port=5000)
	
