"""
Server code for loopgazer application
by @rowlindsay
"""

from flask import Flask
from flask import request
from urllib.parse import parse_qs
import sys

app = Flask(__name__)

global_uname = "rowan"
global_pwd = "password"

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/create-acct")
def create_user():
    creds = request.form
    usr = creds['username']
    pwd = creds['password']
    # TODO
    return "user create"

@app.route("/progress", methods=['GET', 'POST'])
def post_progress():

    print("progress request", file=sys.stderr)

    form = request.form
    usr = form['username']
    pwd = form['password']
    prog = form['progress']

    if ((usr == global_uname) & (pwd == global_pwd)): # TODO
        print(prog, file=sys.stderr)
        return 'Success!'
    else:
        return 'Failure'

@app.route("/change-acct")
def change_pwd():
    form = request.form
    usr = form['username']
    pwd = form['password']
    new_pwd = form['new_password']
    # TODO
    return "password change"


@app.route("/validate", methods=['GET', 'POST'])
def validate_usr():
    form = request.form
    usr = form['username']
    pwd = form['password']

    if ((usr == global_uname) & (pwd == global_pwd)): # TODO
        return 'True'
    else:
        return 'False'
