from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello web!"


@app.route("/greet/<name>/")
def greet_name(name: str):
    """
    Visit http://127.0.0.1:5000/greet/GitHub/

    :param name:
    :return:
    """
    return f"Hello {name}!"


@app.route("/user/")
def read_user():
    """
    > http://127.0.0.1:5000/user/
    - `User [no name] [no surname]`

    > http://127.0.0.1:5000/user/?name=John&surname=Smith
    - User John Smith

    :return:
    """
    name = request.args.get("name")
    surname = request.args.get("surname")
    return f"User {name or '[no name]'} {surname or '[no surname]'}"
