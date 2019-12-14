from flask import Flask,render_template, request, redirect, url_for,make_response,jsonify, session as login_session
from flask import Flask,render_template, request, redirect, url_for,make_response,jsonify, session as login_session
import string
import os
import random
import psycopg2
import bleach
from werkzeug.utils import secure_filename
import flask_login
from views import bp
from models.dbhelper import *
from validation.validators import *
from auth.auth import *


loginManager = flask_login.LoginManager()

@bp.route('/')	
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
@bp.route('/blog',methods=['GET','POST'])	
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
@bp.route('/posts/<int:p_id>/comments/<int:id>',methods=['GET','POST'])
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
		

@bp.route('/posts/<int:p_id>/comments/<int:id>/delete',methods=['GET','POST'])
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
			return redirect(url_for('views.get_blog',post_id=p_id))
		else:
			return redirect(url_for('views.get_blog',post_id=p_id))
		

@bp.route('/signup', methods=['GET','POST'])
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
					res = make_response(redirect(url_for('iews.blog')))
					res.set_cookie('user_id',set_secure_val(email),httponly=True)
					return res
					#return redirect(url_for('iews.blog'))
		else:
			user_err="User with this email already exists!"
			return render_template('signup.html',user_err=user_err,confirm_err="",email_err="")

@bp.route('/user_signup',methods=['GET','POST'])
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
			
			res = make_response(redirect(url_for('views.blog')))
			res.set_cookie('user_id',set_secure_val(email),httponly=True)
			return res

	else:
		if form.errors:
			for e in form.errors:
				print(form.errors.get(e))
		return render_template('user_signup.html',form=form,err=form.errors)
@bp.route('/login', methods=['GET','POST'])
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
				
				#logged = flask_login.login_user(user)
				
				return res
			else:
				return render_template('login.html',error='Invalid Password!')
		else:
			return render_template('login.html',error='User does not exist!')

		
@bp.route('/logout', methods=['GET'])
def logout():
	#self.response.headers.add_header('Set-Cookie','user_id =; path=/')
	res = make_response(redirect(url_for('views.blog')))
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

@bp.route('/new_post', methods=['GET'])
def new_post_get():
	if check_secure_cookie('user_id'):
	
		return new_post()
	else:
		global user_email
		user_email=''
		return render_template('login.html',error='Please login to continue')

@bp.route('/new_post', methods=['POST'])	
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
			 return redirect(url_for('views.blog'))
		else:
			error = "Sorry, no field can be left empty!"
			new_post(subject,content,error)
	return render_template('login.html',error='Please login to continue')


@bp.route('/blog/<int:post_id>', methods=['GET','POST'])
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
@bp.route('/wtf', methods=['GET','POST'])
def gen_form():
	form = userForm(request.form)
	if request.method == 'POST' and form.validate():
		return 'Success!'
	return render_template('wtf.html',form=form)
	
@bp.route('/edit_post/<int:id>',methods=['GET','POST'])
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

@bp.route('/delete_post/<int:id>', methods=['GET','POST'])
@flask_login.login_required
def delete_blog_post(id):
	if request.method =='POST':
		delete_post(id)
		return redirect(url_for('blog'))
	else:
		post = get_post(id)
		return render_template('confirm_delete.html',p_id=id,type='Blog Post',content=post.subject)


#returns the json format of the user commetns		
@bp.route('/comments/<string:user_id>',methods=['GET','POST'])
@flask_login.login_required
def comments_api_json(user_id):
	comments = get_user_comments_api(user_id)
	return jsonify(Comment=[i.serialize for i in comments])


@loginManager.user_loader
def load_user(user_id):
	# since the user_id is just the primary key of our user table, use it in the query for the user
	return get_user(user_id)