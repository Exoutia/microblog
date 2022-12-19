from flask import Flask

app = Flask(__name__) # Create an instance of the Flask class using '__name__' as the name of the application

from app import routes # Import the routes module from app
