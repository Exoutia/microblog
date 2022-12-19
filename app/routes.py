from flask import render_template
from app import app

@app.route('/') # Decorator that tells Flask what URL should trigger our function
@app.route('/index') # Decorator that tells Flask what URL should trigger our function
def index():
    user = {'username': 'Bibek'}
    return render_template('index.html', title='Home', user=user)