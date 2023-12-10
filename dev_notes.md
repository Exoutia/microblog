# Microblog
This is a simple flask web app made with python flask framework. This is made to practice and record my creating this app

# Learning Notes
Here I will write daily insights I have learned that day. It will be like some diary.

## 19-12-2022
- I have to get know about the flask about how it works.
- To use it we need to install the flask.
- I am using pipenv to create the env for running the my project to maintain the integrety of project throughout the development of project and not break something even if module we are using got updates that breaks our code.
- I learned about jangi2 and its some of the feature which I get know today is:
     - 1. if-else system ` {% if condition %}{% else %} {% end if %} `
     - 2. 'for key word' `{% for post in posts %} {% endfor %}`
     - 3.  template inheritamce using base.html

## 20-12-2022
### Web Forms
- Today I am learning about the flask-WTF which is a thin wrapper around WTForms in python

- WTForms is simple form framework which is used to make forms for you webapp it is helpfull to make the form for the webapp which can also be customize by the html. This helps us to keep presentation and code seprate. This is csrf(Cross-Site Request Forgery) proof.

- We also learn about config(app.config) this is us telling the framework our decisions as a list of configuration variables.
     - `app.config['SECRET_KEY'] = 'you-will-never-guess'` this is stored as the same for dictionary.
     - we can also use a config.py and create our variable as object of Config class. Like this:
     - ```py
          import os

          class Config(object):
          SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'```

     - we also get to know about that environment variable we use to store secret key for development.

- We are creating the form and its base using wtf_form

- some things to remember is to add the view and route for the new page we create

- form.hidden_tag generate a hidden feild that includes a token that is used to protect the form against csrf attacks.

- When the action string is empty in html form tag we submit the form into the url which user will be currently in.

- The method attribute specifies the HTTP request method that should be used when submitting the form to the server.

- The default is to send it with a GET request, but in almost all cases, using a POST request makes for a better user experience because requests of this type can submit the form data in the body of the request, while GET requests add the form fields to the URL, cluttering the browser address bar.

- when we are using the browser we are usualy use get method which send data to client(browser) and its default but when we want to collect data we use post method which we need to specify or teh method not found error will be shown

- now we creating the url_for functions which make the code more consistent and easy to use.

### Database
- Flask does not support database natively. so we can choose whichever data base we want

- Relational Database is better for application that have structured data such as list of users, blog posts, etc. and NoSQL database is better for the data has less defined structure.

- As we are making the microblog we will use relaional database.

- Flask-SQLAlchemy is a flask friendly wrapper to the popular SQLAlchemy package, which is an Object Relational Mapper or ORM.
     - ORMs allow applications to manage a database using high-level entities such as classes, objects and methods instead of tables and SQL.
     - The job of ORM is to translate the high-level operations into database commands.

- The nice thing about SQLAlchemy is that it is an ORM not for one, but for many relational databases. SQLAlchemy supports a long list of database engines, including the popular MySQL, PostgreSQL and SQLite.
     - This is extremely powerful, because you can do your development using a simple SQLite database that does not require a server, and then when the time comes to deploy the application on a production server you can choose a more robust MySQL or PostgreSQL server, without having to change your application.
- database can be designed in 'www sql designer'

- Flask-sqlalchemy need to be initiated in config ad init.py.

- when we want to change database we need to create whole databse from scratch but if we use flask-migrate which is based in `Alembic` which maintains the migration repository which is used to make the db by running the commands sequently and creating the repository.

- An unfortunate inconsistency that in some instances such as in a db.relationship() call, the model is referenced by the model class, which typically starts with an uppercase character, while in other cases such as this db.ForeignKey() declaration, a model is given by its database table name, for which SQLAlchemy automatically uses lowercase characters and, for multi-word model names, snake case.

- For one-to-many relationship field is normally defined on the 'one' side, and is used as convenient way to get access to the 'many'.
     - So for example, if I have a user stored in u, the expression u.posts will run a database query that returns all the posts written by that user
     - here we use the `db.relationship()` to connect the tables using primary and foreign key relationship.

- we are using the `flask shell` and config it using the microblog.py so we dont need to enter the import statements all the time.

## 21-12-2022
### User logins system
- Passowrd hassing can be implemented by the werkzeg library with some function predefined in it.

- we will make the function in model.py in the user class to set password and check it with username and password

- now we are going to use extenstion called flask-login.
     - This extension manages the user logged-in state, so that for example users can log in to the application and then navigate to different pages while the application "remembers" that the user is logged in. It also provides the "remember me" functionality that allows users to remain logged in even after closing the browser window.

- As with other extenstions, Flask-Login needs to be created and initialized right after the application instance in `app/.__init__.py`.
     ```py
     # ...
     from flask_login import LoginManager

     app = Flask(__name__)
     # ...
     login = LoginManager(app)

     # ...
     ```

- The flask-login extenstion works with the application's user model and expects certain properties and methods to be implemented in it.
     - The Four required items are listed below:
          1. **is_authenticated**: a property that is True if the user has valid credentials or False otherwise.
          2. **is_active**: a property that is True if the user's account is active or False otherwise.
          3. **is_anonymous**: a property that is False for regular users, and True for a special, anonymous user.
          4. **get_id()**: a method that returns a unique identifier for the user as a string (unicode, if using Python 2).
     - Flask login has a mixin-class which is appropriate for most user model classes called UserMixin you can pass it to the user mode like this
          ```py
          #...
          from flask_login import UserMixin

          class User(UserMixin, db.Model):
          # ...
          ```


- flask-login keeps track of the looged in user by storing unique id in flask's user session, a storage space assigned to each user who connects to the application. This is done by connecting it to database to get the unique id of user. this is done by adding it into thee models.py
     ```py
     from app import login
     # ...

     @login.userr_loader
     def load_user(id):
          return User.query.get(int(id))
     ```

- We are implementing the logic to request the login to anonymous user to restrict them.

- we can do this by giving the logic for the next page or index page.

- An attacker could insert a URL to a malicious site in the next argument, so the application only redirects when the URL is relative, which ensures that the redirect stays within the same site as the application. To determine if the URL is relative or absolute, I parse it with Werkzeug's url_parse() function and then check if the netloc component is set or not.

## 22-12-2022
### user_profile and avatar
- `@app.route('/user/<username>')` here '<>' angle brackets surround the element to tell that its a dynamic component.

-  When a route has a dynamic component, Flask will accept any text in that portion of the URL, and will invoke the view function with the actual text as an argument. For example, if the client browser requests URL /user/susan, the view function is going to be called with the argument username set to 'susan'.

- `# nosec` can be used to tell the editor to stop getting fired up where we dont need to think about security. I learn about in during the use of `md5` hashing to use the hash to get the gravatar from the email of user.

- In jinga2 we can use sub-templates, and the conventions of sub-templates in my file is that sub-templates will start with the `./templates/_sub-templates.html`.

## 23-12-2022
- only some days left for christmas!!!
- yay I want to add some emoji to the md file but vs code is not showing which emoji is added and i dont know how to fix it guess a reload will fix it after install a extension of `emoji` in md.
- i am feeling lazy too.
- so :field_hockey_stick_and_ball:
- lets start anyways we need to make that user interface today at any cost.
### User-profile
- To use sub-template we need to add `include` statement in jinja2.

- We added a `@before_request` for recording the last seen of user which will run the function inside it before any view function for the user. This way we can have a idea about the time the user was active.


## 24-12-2022
- Just one day before christmas and my brother's birthday.
- today i need to atleast complete the work and learn some cloud compting concept.
- I also need to learn rust also so much work to do but I will do it all not in one day but everyday.
- I am not the smartest guy but i can be the consistent guy and can achieve all things with consistency.
- lets start
- one more thing i need to thought about how will the product will scale and security issues and different things about the product this will help be greatly in real world problems.

### Error Handling
- Error handling is one the most crucial thing one need to learn to work with real world application. lets learn how to fix them in flask.

- Error function of flask acts same as the routes or view of app. we are returning the contents of their respective templates.

- To get these error handlers registered with Flask, I need to import the new app/errors.py module after the application instance is created:
     ```py
     # ...
     from app import routes, models, errors
     ```

- During the process we can have the error send to our email address.

## 25-12-2022
- Merry Christmas everyone :tada:
- To day I am going to add some follower to my microblog and do some things with data base and learn more about it.
### Followers
- There are three types of relationship in Relational Database which is
     1. One-TO-Many
     2. One-TO-One
     3. Many-TO-Many

- To use many to many to realtion we use a auxilary table in which has both the keys of two tables.

- A relationship in which instances of a class are linked to other instances of the same class is called a self-referential relationship, and that is exactly what I have here. As the user follow user and user has many follower and user follow many users we just discussed it is self-referential relationship.

- ```py

     class User(UserMixin, db.Model):
     # ...
     followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
     ```
     - 'User' is the right side entity of the relationship (the left side entity is the parent class). Since this is a self-referential relationship, I have to use the same class on both sides.

     - secondary configures the association table that is used for this relationship, which I defined right above this class.

     - primaryjoin indicates the condition that links the left side entity (the follower user) with the association table. The join condition for the left side of the relationship is the user ID matching the follower_id field of the association table. The value of this argument is followers.c.follower_id, which qreferences the follower_id column of the association table.

     - secondaryjoin indicates the condition that links the right side entity (the followed user) with the association table. This condition is similar to the one for primaryjoin, with the only difference that now I'm using followed_id, which is the other foreign key in the association table.

     - backref defines how this relationship will be accessed from the right side entity. From the left side, the relationship is named followed, so from the right side I am going to use the name followers to represent all the left side users that are linked to the target user in the right side. The additional lazy argument indicates the execution mode for this query. A mode of dynamic sets up the query to not run until specifically requested, which is also how I set up the posts one-to-many relationship.

     - lazy is similar to the parameter of the same name in the backref, but this one applies to the left side query instead of the right side.

- indexing makes the data far more easily sorted in data base this is why use to sort the post and show it into the home page.

## 26-12-2022
- So we today we are going to do unit-test.

### Unit Tests
- Unit testing is important cause it ensure that program is running fine without someone keeping an eye on the product and its every feature.

- I have added four tests that exercise the password hashing, user avatar and followers functionality in the user model. The setUp() and tearDown() methods are special methods that the unit testing framework executes before and after each test respectively.

- I have implemented a little hack to prevent the unit tests from using the regular database that I use for development. By setting the DATABASE_URL environment variable to sqlite://, I change the application configuration to direct SQLAlchemy to use an in-memory SQLite database during the tests.

- The setUp() method then creates an application context and pushes it. This ensures that the Flask application instance, along with its configuration data is accessible to Flask extensions. Don't worry if this does not make a lot of sense at this point, as this will be covered in more detail later.

- The db.create_all() call creates all the database tables. This is a quick way to create a database from scratch that is useful for testing. For development and production use I have already shown you how to create database tables through database migrations.

- Because the follow and unfollow actions introduce changes in the application, I'm going to implement them as POST requests, which are triggered from the web browser as a result of submitting a web form. It would be easier to implement these routes as GET requests, but then they could be exploited in CSRF attacks. Because GET requests are harder to protect against CSRF, they should only be used on actions that do not introduce state changes. Implementing these as a result of a form submission is better because then a CSRF token can be added to the form.

- But how can a follow or unfollow action be triggered from a web form when the only thing the user needs to do is click on "Follow" or "Unfollow", without submitting any data? To make this work, the form is going to be empty. The only elements in the form are going to be the CSRF token, which is implemented as a hidden field and added automatically by Flask-WTF, and a submit button, which is going to be what the user needs to click to trigger the action. Since the two actions are almost identical I'm going to use the same form for both. I'm going to call this form EmptyForm.

## 27-12-2022
Today i am going to implicate the idea of adding posts in the social site by the user.

### Pagination

- we make the postform in form in forms section.

- Let's review the changes in this view function one by one:

     - I'm now importing the Post and PostForm classes
     - I accept POST requests in both routes associated with the index view function in addition to GET requests, since this view function will now receive form data.
     - The form processing logic inserts a new Post record into the database.
     - The template receives the form object as an additional argument, so that it can render the text field.

- Its standard practice to respond to a post request generated by a web form submission with a redirect. This is called the Post/Redirect/Get. It avoids inserting duplicate posts when a user inadvertently refreshes the page after submitting a web form.

- to show the limited number of posts in single page we can use paginate function of the sqlAlchemy.

<<<<<<< Updated upstream
## 31-12-2022
its not like i was away just giving an interview and next day i didn't bother to add any date. Today i am at last going to some designing part of the web at last.

### Facelift
- Basicaly its hard to write the pure css for the web page so we need to take the high way and use a css framework which we are going to use for our site that is bootstrap. tada

- sorry for the cliche presentation. :sweat_smile: i will focus on the work now no more jokes only work.

- As the flask-bootstrap has not been updated until now so we are going to use bootstrap-3 for the website.
- as we know that sending the mail make the system slow and it will take time to send the mail by function we are using so we need to make the email service async to make it available wehn its already running.
- What I really want is for the send_email() function to be asynchronous. What does that mean? It means that when this function is called, the task of sending the email is scheduled to happen in the background, freeing the send_email() to return immediately so that the application can continue running concurrently with the email being sent.

- Python has support for running asynchronous tasks, actually in more than one way. The threading and multiprocessing modules can both do this. Starting a background thread for email being sent is much less resource intensive than starting a brand new process, so I'm going to go with that approach
- as we know that sending the mail make the system slow and it will take time to send the mail by function we are using so we need to make the email service async to make it available wehn its already running.
- What I really want is for the send_email() function to be asynchronous. What does that mean? It means that when this function is called, the task of sending the email is scheduled to happen in the background, freeing the send_email() to return immediately so that the application can continue running concurrently with the email being sent.

- Python has support for running asynchronous tasks, actually in more than one way. The threading and multiprocessing modules can both do this. Starting a background thread for email being sent is much less resource intensive than starting a brand new process, so I'm going to go with that approach

### 10/12/2023

- From today I am going to make new frontend for the application and adding tailwindcss to it to make it good looking.
- I am thinking of adding 2fa also in the security purpose.
