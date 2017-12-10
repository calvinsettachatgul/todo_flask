# Todo Flask App

from flask import Flask
from flask import render_template
from pprint import pprint
import json 

app = Flask(__name__)

def get_todos():
    todos = []
    with open('./data/todos.json') as json_data:
        d = json.load(json_data)
        json_data.close()
        todos = d["todos"]
    return  todos

@app.route('/')
def index():
    todos = get_todos()
    print(todos)
    return render_template('index.html', todos=todos)

@app.route("/welcome")
def welcome(name="Calvin"):
    return render_template('welcome.html', name=name)

