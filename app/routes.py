from flask import render_template
from app import app

@app.route('/') # Decorator that tells Flask what URL should trigger our function
@app.route('/index') # Decorator that tells Flask what URL should trigger our function
def index():
    # This is here we are making a dummy user for our app this is just tes should be deleted after some points
    user = {'username': 'Bibek'}
    return render_template('index.html', title='Home', user=user)