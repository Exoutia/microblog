'''Thid is the file where config variables are stored'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """This is the configuration class for the app which is used
    for the different setting or decision we need to take for flask.
    I am using it to provide different things to app as objects.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL') or
                                'sqlite:///' + os.path.join(basedir, 'app.db'))

    # This is just here to suppress a warning from
    # SQLAlchemy as it will soon be removed
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # to get the error through the email to my account if some error occured during the production.
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']

    # to get the post per page
    POSTS_PER_PAGE = 3