'''This is where main app is running and we are importing all
the modules and packages that we need to run the app'''
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():

    return {'db': db, 'User': User, 'Posr': Post}
