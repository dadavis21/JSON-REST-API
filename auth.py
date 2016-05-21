from functools import wraps
from flask import request, Response
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.get_password
def get_pw(username):
    if username == 'admin':
        return 'secret'
    return "Incorrect username/password"
