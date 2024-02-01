import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "kalmartibor8243@gmail.com"
    password = "vcjx wycm uqyr lyuh"

    # PASSWORD = vcjx wycm uqyr lyuh
    # GMAIL_PASSWORD = vdvr ayih ummr wesb

    receiver = "kalmartibor8243@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
