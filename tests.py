import os
os.environ['DATABASE_URL'] = 'sqlite://'

from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_avatar(self):
        u = User(username='john', email='john@example.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
                                        'd4c74594d841139328695756648b6bd6'
                                         '?d=identicon&s=128'))

    def test_follow(self):
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@exapmle.com')

        db.session.add(u1)
        db.session.add(u2)
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u2.followed.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'susan')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'john')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0)


    def test_follow_posts(self):
        # create fout users
        u1 = User(username='user_1', email='user_1@example.com')
        u2 = User(username='user_2', email='user_2@example.com')
        u3 = User(username='user_3', email='user_3@example.com')
        u4 = User(username='user_4', email='user_4@example.com')

        db.session.add_all([u1, u2, u3, u4])

        # create four posts
        now = datetime.utcnow()
        p1 = Post(body='Hello from user_1', author=u1, timestamp=now + timedelta(seconds=1) )
        p2 = Post(body='Hello from user_2', author=u2, timestamp=now + timedelta(seconds=1) )
        p3 = Post(body='Hello from user_3', author=u3, timestamp=now + timedelta(seconds=1) )
        p4 = Post(body='Hello from user_4', author=u4, timestamp=now + timedelta(seconds=1) )
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # setup the followers
        u1.follow(u2)
        u1.follow(u4)
        u2.follow(u3)
        u3.follow(u4)
        db.session.commit()

        # check the followed posts of each user
        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        self.assertEqual(f1, [p1, p2, p4])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])

if __name__ == "__main__":
    unittest.main(verbosity=2)


# I have added four tests that exercise the password hashing,
# user avatar and followers functionality in the user model.
# The setUp() and tearDown() methods are special methods that
# the unit testing framework executes before and after each test
# respectively.

# I have implemented a little hack to prevent the unit tests
# from using the regular database that I use for development.
# By setting the DATABASE_URL environment variable to sqlite://,
# I change the application configuration to direct SQLAlchemy
# to use an in-memory SQLite database during the tests.

# The setUp() method then creates an application context and pushes it.
# This ensures that the Flask application instance, along with its
# configuration data is accessible to Flask extensions. Don't worry
# if this does not make a lot of sense at this point, as this will be
# covered in more detail later.

# The db.create_all() call creates all the database tables.
# This is a quick way to create a database from scratch that is
# useful for testing. For development and production use I have
# already shown you how to create database tables through database
# migrations.