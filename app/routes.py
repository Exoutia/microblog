from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse


@app.route('/') # Decorator that tells Flask what URL should trigger our function
@app.route('/index') # Decorator that tells Flask what URL should trigger our function
@login_required
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
    return render_template('index.html', title='Home', posts=posts)

# We are now adding the routes for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Chehck if the user is already logged in or not
    if current_user.is_authenticated():
        # return them to the index if user is already logged in
        return redirect(url_for('index'))

    form = LoginForm()

    # If the form is validated then we will check the username and password
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        # if the user is not found or the password is wrong then we will flash the message
        if user is None or not user.check_password(form.password.data):

            flash('Invalid username or password')
            return redirect(url_for('login'))

        # If the user is found and the password is correct then we will login the user
        login_user(user, remember=form.remember_me.data)

        # this is used toredirect to the page the user is trying
        # to get in when it gor here to first login and then go there

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for(next_page))


    return render_template('login.html', title='Sign In', form=form)


# this is function to logout the user
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))