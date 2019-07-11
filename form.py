from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField('username', validators=[DataRequired()], render_kw={"placeholder" : "username"})
	password = PasswordField('password', validators=[DataRequired()], render_kw={"placeholder" : "password"})
	submit = SubmitField('Log in')