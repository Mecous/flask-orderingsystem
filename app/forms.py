from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField("email",validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('remember me',default=False)

class RegisterForm(FlaskForm):
    email = StringField('email',validators=[DataRequired()])
    username = StringField("User Name",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    phonenum = StringField('Phonenum',validators=[DataRequired()])
