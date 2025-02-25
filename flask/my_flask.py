# -*- coding: utf-8 -*-
"""Flask.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zw5fREPh2amEFZo2ZUj03t2xPgoxMTgU
"""
'''
/ importig the flask class
'''

from flask import Flask

'''
instannce
'''

app = Flask(__name__)

'''
Our home page
'''
@app.route('/')


def hello_world():
    return ' <h1>Hello, World!</h1>'


'''
When you run a Flask application, 
it automatically handles the web server 
setup and starts serving your application without 
needing the explicit app.run() call if the script is 
run as the main program. When you run the Flask application 
using the flask run command, Flask will internally handle the server setup.


The @app.route('/') decorator tells Flask that the 
hello_world function should be called when a request is made
 to the root URL ('/'). The function returns the HTML response 
 <h1>Hello, World!</h1>.

'''


