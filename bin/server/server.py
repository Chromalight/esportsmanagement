import requests
import operations
import json
from flask import Flask
import os

# After CLI/HTTP request based functions are all-working, the website will become the development focus.

app = Flask(__name__)

@app.route('/')
def home():
    return 'This website is not intended to be opened in a browser.'
    

