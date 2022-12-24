from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__) # Create an instance of the Flask class using '__name__' as the name of the application
app.config.from_object(Config) # Load the configuration from the Config class
db = SQLAlchemy(app) # Create an instance of the SQLAlchemy class using the app instance
migrate = Migrate(app, db) # Create an instance of the Migrate class using the app and db instances
login = LoginManager(app) # Create an instance of the LoginManager class using the app instance
login.login_view = 'login' # this is to use to protect the user to see some pages anonymous

from app import routes, models, errors
