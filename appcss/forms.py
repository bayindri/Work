#import flask.ext.wtf
#from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField
from flask.ext.wtf import Form

from wtforms import BooleanField,TextField, TextAreaField, SubmitField
from wtforms.validators import Required

class ContactForm(Form):
	name = TextField("Name")
	email = TextField("Email")
	subject = TextField("Subject")
	message = TextAreaField("Message")
	submit = SubmitField("Send")