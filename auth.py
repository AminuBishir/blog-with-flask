import hmac
import hashlib
import string
import random
#from views import *


#secret key for creating values
secret_key = '0!`~|+=_(*%:?>,$@-19'
#letter to be used in creating salt
letters = string.ascii_letters
user_email =''
#convenience function for setting and validating values
def set_secure_val(val):
	return '%s|%s' %(val,(hmac.new(str.encode(secret_key),str.encode(val),hashlib.sha256).hexdigest()))

def check_secure_val(secure_val):
	val = secure_val.split('|')[0]
	return val and secure_val==set_secure_val(val)

def render(self,template,**kw):
	render_template(template,**kw)

	
	
#convenience functions for creating and verifying cookie
def make_secure_cookie(name,user_id):
	res = get_response('blog.html')
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
