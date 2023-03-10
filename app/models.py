from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from app import db, login
from hashlib import md5
from time import time
import jwt
from app import app


# This is a direct translation of the association
# table from my diagram above. Note that I am not
# declaring this table as a model, like I did for
# the users and posts tables. Since this is an
# auxiliary table that has no data other than the
# foreign keys, I created it without an associated model class.

followers = db.Table('followers',
        db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(150))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    # declare the many-to-many relationship in the users table
    #  I'm using the db.relationship function to define the relationship in the model
    # class. This relationship links User instanlazy is similar to the parameter of the same name in the backref, but this one applies to the left side query instead of the right side.ces to other User instances,
    # so as a convention let's say that for a pair of users linked by this
    # relationship, the left side user is following the right side user.

    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref = db.backref('followers', lazy='dynamic'),
        lazy='dynamic'
    )


    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest() # nosec
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id
        ).count() > 0

    # this fucntion get the posts from the followed by user to his/her homepage.
    # this is done by the query we do at the posts table to get the all followed users
    # we got both our and followed post from the use of posts and our followers table
    # and this is done to use them cause they are indexed and this makes the data far more easily sorted.
    def followed_posts(self):
        followed = Post.query.join(followers, (followers.c.followed_id == Post.user_id)).filter(followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    # to help with reset password to the user
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {"reset_password": self.id, 'exp': time()+expires_in},
            app.config['SECRET_KEY'], algorithm='HS256'
        )

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except:
            return
        return


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.body}>'



# as flask login knows nothing about database, it needs the
# application's help in loading a user for that reason
# the extension expects that the application will configure
# a user loader function, that can be called to load a user given the ID
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
