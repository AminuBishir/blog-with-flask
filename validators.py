import re

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