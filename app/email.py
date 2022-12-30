from flask_mail import Message
from app import mail, app
from flask import render_template
from threading import Thread # this is use for multipurpose

# this is use for the async mail sending
# as we know starting a background thread for email
# being sent is much less resource intensive than starting
# a brand new process, so I'm going to go with that approach
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, htnl_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = htnl_body
    # he send_async_email function now runs in a background thread,
    # invoked via the Thread class in the last line of send_email().
    # With this change, the sending of the email will run in the thread,
    # and when the process completes the thread will end and clean itself up.
    Thread(target=send_async_email, args=(app, msg)).start() # this will free send email function to use another place while email is sending.



def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset your password',
        sender=app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=('email/reset_password.txt', user=user, token=token),
        html_body=render_template('email/reset_password.html', user=user, token=token)
    )

