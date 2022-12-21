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






