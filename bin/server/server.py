import requests
import operations
import json
from flask import Flask
import os
from flask import request 

# After CLI/HTTP request based functions are all-working, the website will become the development focus.

app = Flask(__name__)

@app.route('/')
def home():
    return 'This website is not intended to be opened in a browser.'
    
@app.route('/login', methods=['POST'])
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    operations.loginUser(email, password)
    # Session system will be implemented in the future.

@app.route('/logout')
def logout():
    return # Reserved for post-session system development.


@app.route('/manageteam')
def manageteam():
    return # Reserved for future usage.



