from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from datetime import datetime


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
    if current_user.is_authenticated:
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

        # this here we only return the url_for object and that does not have the url
        return redirect(next_page)


    return render_template('login.html', title='Sign In', form=form)


# this is function to logout the user
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, your registration is complete.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes has been saved. 😎')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)