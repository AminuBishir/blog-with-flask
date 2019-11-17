import sys
from sqlalchemy import Column,Table, ForeignKey,String,Integer,desc,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy import create_engine
import datetime
import bleach
from flask_login import UserMixin
from flask import jsonify


Base = declarative_base()

class Blog(Base):
	__tablename__ ='blog'
	subject = Column(String(250),nullable=False)
	content = Column(String(),nullable=False)
	author = Column(String(100),nullable=False)
	created = Column(DateTime(),default=datetime.datetime.utcnow)
	img_src = Column(String(100),nullable=True)
	p_id = Column(Integer,nullable=False, primary_key=True)
	

class Comment(Base):
	__tablename__ = 'comment'
	id = Column(Integer,nullable=False,primary_key=True)
	p_id = Column(Integer,ForeignKey('blog.p_id'))
	commentor = Column(String(100),nullable=False)
	comment = Column(String(),nullable=False)
	
	#create relationship between this table and blogs table
	blog = relationship(Blog)

	#creating api endpoint
	@property
	def serialize(self):
		#return the object data in an easily serializable format
		return {
		'id':self.id,
		'p_id':self.p_id,
		'commentor':self.commentor,
		'comment':self.comment
		}
		
		
		
class User(UserMixin,Base):
	__tablename__ = 'users'
	email=Column(String(100),nullable=False,primary_key=True)
	f_name = Column(String(100),nullable=False)
	s_name = Column(String(100),nullable=False)
	password = Column(String(100),nullable=False)
	role = Column(String(50),nullable=True)
	
	def get_id(self):
		return self.email
	def get_role(self):
		return self.role
	

class Likes(Base):
	__tablename__ = 'likes'
	id = Column(Integer,nullable=False,primary_key=True)
	p_id = Column(Integer,nullable=False)
	liker = Column(Integer,nullable=False)


#function to handle session creation
def create_session():
	engine = create_engine('postgresql://vagrant:8754@localhost/sadarwa')
	Base.metadata.bind = engine
	DBSession = sessionmaker(bind =engine)
	session = DBSession()
	return session

def add_user(email, f_name,s_name,password,role):
	
	session = create_session()
	nuser = User(email=email,f_name=f_name,s_name=s_name,password=password,role=role)
	session.add(nuser)
	session.commit()
	
def get_user(user_email):
	
	session = create_session()
	user = session.query(User).filter_by(email=bleach.clean(user_email)).first()
	return user
	
def add_post(subject,content,author,img_path):
	session = create_session()
	n_post = Blog(subject=subject,content=content,author=author,img_src=img_path)
	session.add(n_post)
	session.commit()
	
def get_post(p_id):
	
	session = create_session()
	post = session.query(Blog).filter_by(p_id=p_id).first()
	return post
def update_post(id,subject,content):
	session = create_session()
	post = session.query(Blog).filter_by(p_id=id).first()
	post.subject = subject
	post.content = content
	session.commit()

def delete_post(id):
	session = create_session()
	post = session.query(Blog).filter_by(p_id=id).first()
	#get all the comments related to the post
	related_comments = session.query(Comment).filter_by(p_id=id).all()
	
	#delete the comments one after the other
	for comment in related_comments:
		session.delete(comment)
		
	session.delete(post)
	session.commit()

def delete_single_comment(c_id):
	session = create_session()
	comment = session.query(Comment).filter_by(id=c_id).first()
	session.delete(comment)
	session.commit()
	

def get_recent_post():
	
	session = create_session()
	r_post = session.query(Blog).order_by(Blog.created.desc()).first()
	return r_post
def get_posts():
	
	session = create_session()
	all_posts = session.query(Blog).all()
	return all_posts

def add_comment(p_id,commentor,comment):
	session = create_session()
	n_comment = Comment(p_id=p_id,commentor=commentor,comment=comment)
	session.add(n_comment)
	return session.commit()


def get_comments(p_id):
	
	session = create_session()
	comments = session.query(Comment).filter_by(p_id=p_id).all()
	return comments
def get_single_comment(id):
	session = create_session()
	comment = session.query(Comment).filter_by(id=id).first()
	return comment
def edit_comment(id,new_comment):
	session = create_session()
	comment = session.query(Comment).filter_by(id=id).first()
	comment.comment = new_comment
	session.add(comment)
	session.commit()

def get_user_comments_api(user_id):
	session = create_session()
	user_comments = session.query(Comment).filter_by(commentor=user_id).all()
	return user_comments
	
#Below is the implementation using raw sql queries instead of orm
'''
DB_NAME = "sadarwa"
def add_user(email, f_name,s_name,password):
	
	db = psycopg2.connect(database = DB_NAME)
	c = db.cursor()
	c.execute("insert into users(email,f_name,s_name,password)values(%s,%s,%s,%s)",(bleach.clean(email),bleach.clean(f_name),bleach.clean(s_name),bleach.clean(s_name),bleach.clean(password)))
	db.commit()
	db.close

def get_user(email):
	
	db = psycopg2.connect(database = DB_NAME)
	c = db.cursor()
	c.execute("select * from users where email='email'")
	return c.fetchall()
	db.close()
	
def add_post(subject,content,author):
	db = psycopg2.connect(database = DB_NAME)
	c = db.cursor()
	c.execute("insert into blog(subject,content,author)values(%s,%s,%s)",(bleach.clean(subject),bleach.clean(content),bleach.clean(author)))
	db.commit()
	db.close

def get_post(p_id):
	
	db = psycopg2.connect(database = DB_NAME)
	c = db.cursor()
	c.execute("select * from blog where p_id=%",(p_id))
	return c.fetchall()
	db.close()
def get_recent_post():
	
	db = psycopg2.connect(database = DB_NAME)
	c = db.cursor()
	c.execute("select * from blog order by created desc limit 1")
	return c.fetchall()
	db.close()
def get_posts():
	
	db = psycopg2.connect(database = DB_NAME)
	c = db.cursor()
	c.execute("select * from blog order by created desc")
	return c.fetchall()
	db.close()

def add_comment(p_id,commentor,comment):
	db = psycopg2.connect(database = DB_NAME)
	c = db.cursor()
	c.execute("insert into comment(p_id,commentor,comment)values(%s,%s,%s)",(bleach.clean(p_id),bleach.clean(commentor),bleach.clean(comment)))
	db.commit()
	db.close
def get_comments(p_id):
	
	db = psycopg2.connect(database = DB_NAME)
	c = db.cursor()
	c.execute("select * from comment where p_id=%s order by created desc limit 12",(p_id))
	return c.fetchall()
	db.close()
	'''