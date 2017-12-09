# Todo Flask App

from flask import Flask
from flask import render_template
from pprint import pprint

app = Flask(__name__)

all_todos = [
                "Python",   
                "Ruby", 
                "Javasript"
            ]

def get_todos():
    return  all_todos

@app.route('/')
def index():
    todos = get_todos()
    print(todos)
    return 'All Todos'

@app.route("/welcome")
def welcome(name="Calvin"):
    return render_template('welcome.html', name=name)

