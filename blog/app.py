from flask import Flask

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
