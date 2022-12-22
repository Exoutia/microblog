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
