from dbhelper import Blog, Comment,User
from pytest import fixture
from hashlib import sha256
#fixture for new user
@fixture(scope='module')
def new_blog(user_name,create_date,post_id):
	user = Blog(subject='blog-name',content='this is a test blog post',author=user_name,created=create_date,img_src='',p_id=post_id)
	return user
	
'''GIVEN: Blog model
	WHEN: new user is created
	THEN: check that all values are assigned'''
def test_blog_post(new_blog,user_name,create_date):
	assert new_blog.subject == 'blog-name'
	assert new_blog.content == 'this is a test blog post'
	assert new_blog.author == user_name
	assert new_blog.created == create_date
	assert new_blog.img_src == ''

'''GIVEN: Comment model
	WHEN: new comment is added
	THEN: check the comment, the commentor and the post id'''
def test_comment(post_id,user_name):
	comment = Comment(id=1,p_id=post_id,comment="Hello there is this is a new comment",commentor=user_name)
	
	assert comment.comment == "Hello there is this is a new comment"
	assert comment.p_id == '3'
	assert comment.commentor == 'sadarwa'
	assert comment.serialize == {'id':1,'p_id':post_id,'commentor':user_name,'comment':"Hello there is this is a new comment"}
	
'''GIVEN: User model
	WHEN: new user is created
	THEN: check the email,firstname,lastname,password, role as well as get_id and get_role funcions'''
def test_new_user(email,user_name,password):
	new_user = User(email=email,f_name=user_name,s_name='A. '+user_name,password=sha256((email+password).encode('utf-8')).hexdigest(),role='admin')
	
	assert new_user.email == email
	assert new_user.f_name == user_name
	assert new_user.s_name == 'A. '+user_name
	assert new_user.password == sha256((email+password).encode('utf-8')).hexdigest()
	assert new_user.role == 'admin'
	assert new_user.get_id == email
	assert new_user.get_role == 'admin'