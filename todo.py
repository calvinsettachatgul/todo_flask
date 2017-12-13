# Todo Flask App

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from pprint import pprint

import json 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/todo_flask'
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120) )
    description = db.Column(db.String(120))
    priority = db.Column(db.String(120))
    status = db.Column(db.String(120))
    date = db.Column(db.String(120))

    def __init__(self, title, description, priority, status, date):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.date = date

    def __repr__(self):
        return '<E-mail %r>' % self.email

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

