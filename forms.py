from wtforms import Form,StringField,validators, TextAreaField,FileField,PasswordField


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