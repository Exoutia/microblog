from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User
from wtforms import TextAreaField
from wtforms.validators import Length

# Most Flask extensions use a flask_<name> naming convention
# for their top-level import symbol. In this case,
# Flask-WTF has all its symbols under flask_wtf.
class LoginForm(FlaskForm):
    """This is the form we login with and it has field of username
    functions are self explantory.

    Args:
        FlaskForm (class of flasl_login): use to make the form for flask website
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    """this is the form for registration purpose."""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    # The implementation is in a custom validation method, but there is an overloaded
    # constructor that accepts the original username as an argument. This username is saved as an
    # instance variable, and checked in the validate_username() method. If the username entered in
    # the form is the same as the original username, then there is no reason to check the database
    # for duplicates.

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_usernamer = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')