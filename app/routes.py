from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/') # Decorator that tells Flask what URL should trigger our function
@app.route('/index') # Decorator that tells Flask what URL should trigger our function
def index():
    # This is here we are making a dummy user for our app this is just tes should be deleted after some points
    user = {'username': 'Bibek'}
    posts = [
        {
            'author': {'username': 'Jhon'},
            'body': 'Beautiful day in India!'
        },
        {
            'author': {'username': 'Alice'},
            'body': 'Boy we are demons who control the fate'
        },
        {
            'author': {'username': 'Gummy_Bear_of_legends'},
            'body': 'You sucker of sugar I am the one who will control the universe'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

# We are now adding the routes for login
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)