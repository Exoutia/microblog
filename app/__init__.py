from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__) # Create an instance of the Flask class using '__name__' as the name of the application
app.config.from_object(Config) # Load the configuration from the Config class
db = SQLAlchemy(app) # Create an instance of the SQLAlchemy class using the app instance
migrate = Migrate(app, db) # Create an instance of the Migrate class using the app and db instances

from app import routes, models
