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

- now we creating the url_for functions.

