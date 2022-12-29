from flask_mail import Message
from app import mail


def send_email(subject, sender, recipients, text_body, htnl_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = htnl_body
    mail.send(msg)
