# Todo Flask App

from flask import Flask
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
def welcome():
    return "Welcome to Todo Flask!"
