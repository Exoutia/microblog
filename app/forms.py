from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SubmitField
from wtform.validators import DataRequired

# Most Flask extensions use a flask_<name> naming convention
# for their top-level import symbol. In this case,
# Flask-WTF has all its symbols under flask_wtf.
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')