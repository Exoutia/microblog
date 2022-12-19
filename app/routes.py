from app import app

@app.route('/') # Decorator that tells Flask what URL should trigger our function
@app.route('/index') # Decorator that tells Flask what URL should trigger our function
def index():
    user = {'username': 'Bibek'}
    return '''
    <html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
    </html>
    '''