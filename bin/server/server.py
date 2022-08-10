import requests
import operations
from flask import Flask, request
import os

# After CLI/HTTP request based functions are all-working, the website will become the development focus.

app = Flask(__name__)

@app.route('/')
def home():
    return 'This website is not intended to be opened in a browser.'
    
@app.route('/login', methods=['POST'])
def login():
    credentials = request.get_json()
    email = credentials['email']
    password = credentials['password']

    if operations.loginUser(email, password):
        return 'Logged in.'
        # Session system will be implemented in the future.

    else:
        return 'Login failed.'
@app.route('/logout')
def logout():
    return # Reserved for post-session system development.
    

@app.route('/manageteam')
def manageteam():
    return # Reserved for future usage.



