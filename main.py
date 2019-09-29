from flask import Flask,render_template, request, redirect, url_for,make_response,jsonify, session as login_session
import requests
import jinja2
import hmac
import hashlib
import string
import re
import os
import random
import psycopg2
import bleach
from dbhelper import *
from werkzeug.utils import secure_filename
from wtforms import Form,StringField,validators, TextAreaField,FileField,PasswordField
import flask_login



'''template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)
'''


UPLOAD_FOLDER = 'D:/AMINU BISHIR/AMINU BISHIR/PROGRAMMING/Full Stack Web/fullstack-nanodegree-vm/vagrant/sadarwa-blog/image'
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
loginManager = flask_login.LoginManager()
loginManager.init_app(app)

#secret key for creating values
secret_key = '0!`~|+=_(*%:?>,$@-19'

#letter to be used in creating salt
letters = string.ascii_letters
user_email =''
#convenience function for setting and validating values
def set_secure_val(val):
	return '%s|%s' %(val,(hmac.new(str.encode(secret_key),str.encode(val)).hexdigest()))

def check_secure_val(secure_val):
	val = secure_val.split('|')[0]
	return val and secure_val==set_secure_val(val)

def render(self,template,**kw):
	render_template(template,**kw)

#convenience functions for creating and verifying cookie
def make_secure_cookie(name,user_id):
	res = make_response(render_template('blog.html'))
	res.set_cookie(name,set_secure_val(user_id))
	global user_email
	user_email = user_id
	return res
def check_secure_cookie(name):
	secure_cookie = request.cookies.get(name)
	return secure_cookie and check_secure_val(secure_cookie)

#convenience functions for hashing password
def make_salt(length=5):
	return ''.join(random.choice(letters) for x in range(length))
def make_pw_hash(name,password, salt=None):
	if not salt:
		salt = make_salt()
	return '%s,%s' %(salt,hashlib.sha256((name + password + salt).encode('utf-8')).hexdigest())
def valid_pw(name,password,hash):
	salt = hash.split(',')[0]
	return salt and hash == make_pw_hash(name,password,salt)

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

@app.route('/')	
def main_get():
	return redirect(url_for('blog'))

def show_posts(comments=None):
	#query the available blogs
	blogs = get_posts()
	
	recent_post = get_recent_post()
	if recent_post:
		comments = get_comments(recent_post.p_id)
		cookie = request.cookies.get('user_id')
		if cookie:
			uid = cookie.split('|')[0]
			user = get_user(uid)
			return render_template('blog.html',r_post=recent_post,blog_posts=blogs, user=user.f_name, login=True,comments = comments)
		else:
			return render_template('blog.html',r_post=recent_post, blog_posts=blogs,comments = comments)
	else:
		return render_template('blog.html',blog_posts=blogs,comments = comments)
@app.route('/blog',methods=['GET','POST'])	
def blog():
	if request.method == 'GET':
		print("Inside GET method")
		return show_posts()
	else:
		print("Inside POST method")
		comment = request.form.get('comment')
		id_post = request.form.get('post_id')
		if comment:
			return make_comment(comment,id_post)
		else:
			return 'comment not submitted!'

#Posts a comment to db
def make_comment(comment,id_post):
	
	cookie = request.cookies.get('user_id')
	uid = cookie.split('|')[0]
	if id_post:
		print("Post_id isn't empty")
		if not(add_comment(id_post,uid,comment)):
			print("Commed NOT Added!")
		load_comments = get_comments(id_post)
		return show_posts(load_comments)
	else:
		print("Post_id is empty")
		return show_posts()
#for editing user comment
@app.route('/posts/<int:p_id>/comments/<int:id>',methods=['GET','POST'])
@flask_login.login_required
def edit_my_comment(p_id,id):
	form = CommentForm(request.form)
	if request.method =='GET':
		comment = get_single_comment(id)
		user = flask_login.current_user
		if comment.commentor == user.email:
			form.comment.data = comment.comment
			return render_template('edit_comment.html',form=form)
		else:
			return redirect(url_for('get_blog',post_id=p_id))
	else:
		comment = form.comment.data
		edit_comment(id,comment)
		return redirect(url_for('get_blog',post_id=p_id))
		

@app.route('/posts/<int:p_id>/comments/<int:id>/delete',methods=['GET','POST'])
@flask_login.login_required
def delete_my_comment(p_id,id):
	form = CommentForm(request.form)
	if request.method =='GET':
		comment = get_single_comment(id)
		user = flask_login.current_user
		if comment.commentor == user.email:
			
			return render_template('confirm_delete.html',type="Comment",content=comment.comment)
		else:
			return redirect(url_for('get_blog',post_id=p_id))
	else:
		comment = get_single_comment(id)
		user = flask_login.current_user
		if comment.commentor == user.email:
			delete_single_comment(id)
			return redirect(url_for('get_blog',post_id=p_id))
		else:
			return redirect(url_for('get_blog',post_id=p_id))
		

@app.route('/signup', methods=['GET','POST'])
def signup():
	if request.method=='GET':
		
		return render_template('signup.html')

	else:	
		#get params from request
		
		username = request.form.get("username")
		s_name = request.form.get("s_name")
		password = request.form.get("userpass")
		confirm = request.form.get("confirm")
		email = bleach.clean(request.form.get("email"))
		
		#query db for existing user
		#user = db.GqlQuery('SELECT * FROM User WHERE name= :1',username)
		user = get_user(email)
		
		if not user:
			#validate the params
			user_empty = check_empty(username)
			sname_empty = check_empty(s_name)
			user_err = check_username(username)
			sname_err = check_username(s_name)
			empty_pass = check_empty(password)
			empty_confirm = check_empty(confirm)
			confirm_err = confirmPass(password,confirm)
			email_err = validate_email(email)
			
			if (user_empty or sname_empty or empty_pass or empty_confirm):
				return render_template('signup.html',user_err=user_empty,confirm_err=empty_confirm,email_err="")
			else:
				if (user_err or sname_err or confirm_err or email_err):
					return render_template('signup.html',user_err=user_err,sname_err =sname_err,confirm_err=confirm_err,email_err=email_err)
				else:
					#self.response.headers.add_header('Set-Cookie','username='+str(username)+',path=/')
					
					#user = User(parent=user_key(),name=username, email=email,password=self.make_pw_hash(username,password))
					#user.put()
					
					add_user(email,username,s_name,make_pw_hash(email,password),role='admin')
					res = make_response(redirect(url_for('blog')))
					res.set_cookie('user_id',set_secure_val(email),httponly=True)
					return res
					#return redirect(url_for('blog'))
		else:
			user_err="User with this email already exists!"
			return render_template('signup.html',user_err=user_err,confirm_err="",email_err="")

@app.route('/user_signup',methods=['GET','POST'])
def user_signup():
	form = UserForm(request.form)
	if request.method == 'POST' and form.validate():
		fname = form.firstname.data
		sname = form.surname.data
		email = form.email.data
		password = form.password.data
		
		user = get_user(email)
		if not user:
			add_user(email,fname,sname,make_pw_hash(email,password),role='user')
			n_user = get_user(email)
			flask_login.login_user(n_user)
			
			res = make_response(redirect(url_for('blog')))
			res.set_cookie('user_id',set_secure_val(email),httponly=True)
			return res

	else:
		if form.errors:
			for e in form.errors:
				print(form.errors.get(e))
		return render_template('user_signup.html',form=form,err=form.errors)
@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'GET':
		login_session['token'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(20))
		return render_template('login.html',error='', token=login_session['token'])
	else:
	
		email = request.form.get('email')
		password = request.form.get('password')
		
		user = get_user(email)
		if user:
			if (valid_pw(email,password,user.password)):
				cookie = make_secure_cookie('user_id',user.email)
				recent_post = get_recent_post()
				res = make_response(render_template('blog.html',r_post=recent_post, blog_posts = get_posts(),user=user.f_name, login=True))
				res.set_cookie('user_id',set_secure_val(user.email),httponly=True)
				
				logged = flask_login.login_user(user)
				
				return res
			else:
				return render_template('login.html',error='Invalid Password!')
		else:
			return render_template('login.html',error='User does not exist!')

		
@app.route('/logout', methods=['GET'])
def logout():
	#self.response.headers.add_header('Set-Cookie','user_id =; path=/')
	res = make_response(redirect(url_for('blog')))
	flask_login.logout_user()
	res.set_cookie('user_id','')
	return res

	
def new_post(subject="",content="",error=""):
	if check_secure_cookie('user_id'):
		return render_template("new_post.html",subject=subject,content=content,error=error)
	else:
		global user_email
		user_email =''
		
		return render_template('login.html',error='Please login to continue')

@app.route('/new_post', methods=['GET'])
def new_post_get():
	if check_secure_cookie('user_id'):
	
		return new_post()
	else:
		global user_email
		user_email=''
		return render_template('login.html',error='Please login to continue')

@app.route('/new_post', methods=['POST'])	
def new_post_post():
	cookie = request.cookies.get('user_id')
	if cookie:
		subject = request.form.get("subject")
		content = request.form.get("content")
		file = request.files['file']
		content = content.replace('/n','<br>')
		if subject and content and file:
			 user_email = get_user(cookie.split('|')[0])
			 filename = secure_filename(file.filename)
			 path = os.path.join('/static/image',filename)
			 file.save(os.path.join(os.getcwd()+'/static/image',filename))
			 print(path)
			 add_post(subject,content,cookie.split('|')[0],path)
			 blog = get_recent_post()
			 return redirect(url_for('blog'))
		else:
			error = "Sorry, no field can be left empty!"
			new_post(subject,content,error)
	return render_template('login.html',error='Please login to continue')


@app.route('/blog/<int:post_id>', methods=['GET','POST'])
def get_blog(post_id):
	if request.method =='GET':
		#key = db.Key.from_path('Blog',int(post_id),parent=blog_key())
		post = get_post(post_id)
		
		if not post:
			#request.error(404)
			return render_template('404.html')
		else:	
			comments = get_comments(post_id)
			
			return render_template('post.html',user_id=user_email,posts=post,comments=comments,login=True)
	else:
		print("Inside POST method")
		comment = request.form.get('comment')
		id_post = request.form.get('post_id')
		if comment:
			return make_comment(comment,id_post)
		else:
			return 'comment not submitted!'
@app.route('/wtf', methods=['GET','POST'])
def gen_form():
	form = userForm(request.form)
	if request.method == 'POST' and form.validate():
		return 'Success!'
	return render_template('wtf.html',form=form)
	
@app.route('/edit_post/<int:id>',methods=['GET','POST'])
@flask_login.login_required
def edit_post(id):
	form = post_form(request.form)
	if request.method == 'GET':
		post = get_post(id)
		form.subject.data = post.subject
		form.content.data = post.content
		return render_template('edit_post.html',form=form)
	elif request.method =='POST' and form.validate():
		subject = form.subject.data
		content = form.content.data
		update_post(id,subject,content)
		return redirect(url_for('get_blog',post_id=id))

@app.route('/delete_post/<int:id>', methods=['GET','POST'])
@flask_login.login_required
def delete_blog_post(id):
	if request.method =='POST':
		delete_post(id)
		return redirect(url_for('blog'))
	else:
		post = get_post(id)
		return render_template('confirm_delete.html',p_id=id,type='Blog Post',content=post.subject)


#returns the json format of the user commetns		
@app.route('/comments/<string:user_id>',methods=['GET','POST'])
@flask_login.login_required
def comments_api_json(user_id):
	comments = get_user_comments_api(user_id)
	return jsonify(Comment=[i.serialize for i in comments])

class post_form(Form):
	subject = StringField("Subject",[validators.Length(min=5, max=150),validators.required()])
	content = TextAreaField("Content", [validators.required()])
class UserForm(Form):
	firstname = StringField("First Name",[validators.Length(min=3,max=50), validators.required()])
	surname = StringField("Surname",[validators.Length(min=3,max=50),validators.required()])
	email = StringField('Email',[validators.required(), validators.Email()])
	password = PasswordField('Password',[validators.Length(min=3),validators.EqualTo('confirm', message="Passwords must match!")])
	confirm = PasswordField('Confirm Password',[validators.required('Please confirm Password!')])
class CommentForm(Form):
	comment = StringField('Comment',[validators.required(),validators.Length(min=3, message="This comment is too short!")])
'''
class PostPage(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Blog', int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return

        self.render("post.html", post = post)
	
'''
def check_empty(input):
	if not input:
		return "This field cannot be empty!"
	else:
		return ""
def confirmPass(pass1,pass2):
	if(pass1 == pass2): #006b08a801d82d0c9824dcfdfdfa3b3c
		return ""
	else:
		return "Passwords do not match!"
def check_username(input):
	if ((" " in input) or len(input)<3):
		return "Invalid First and/or Last name!"
	else:
		return ""
def validate_email(email):
	if re.match("^.+@(/[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) or not email:
		return ""
	else:
		return "Invalid email address!"
@loginManager.user_loader
def load_user(user_id):
	# since the user_id is just the primary key of our user table, use it in the query for the user
	return get_user(user_id)
'''app = webapp2.WSGIApplication([
   ('/', MainHandler),('/blog',BlogHandler),('/new_post',NewPost),('/blog/([0-9]+)',BlogPage),('/login',LoginHandler),('/signup',Signup),('/logout',Logout)
], debug=True)
'''
if __name__ == '__main__':
	app.debug = True
	app.secret_key = secret_key
	app.run(host='0.0.0.0',port=5000)
	
