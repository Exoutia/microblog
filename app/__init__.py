from flask import Flask
from config import Config


app = Flask(__name__) # Create an instance of the Flask class using '__name__' as the name of the application
app.config.from_object(Config) # Load the configuration from the Config class

from app import routes # Import the routes module from app
