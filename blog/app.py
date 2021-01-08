from time import time
from flask import Flask, request, g

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello web!"


@app.route("/greet/<name>/")
def greet_name(name: str):
    """
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules

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


@app.route("/status/", methods=["GET", "POST"])
def custom_status_code():
    """
    # https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

    # GET
    >  curl --request GET --url http://127.0.0.1:5000/status/
    - To get response with custom status code
      send request using POST method
      and pass `code` in JSON body / FormData

    # POST (empty body)
    > curl --request POST --url http://127.0.0.1:5000/status/
    < HTTP/1.0 204 NO CONTENT

    # POST (multipart/form-data)
    > curl --request POST --url http://127.0.0.1:5000/status/ \
      --header 'Content-Type: multipart/form-data' \
      --form code=202
    < HTTP/1.0 202
    - code from form

    # POST (json)
    > curl --request POST --url http://127.0.0.1:5000/status/ \
      --header 'Content-Type: application/json' \
      --data '{"code": 205}'
    < HTTP/1.0 205 RESET CONTENT
    - code from json

    :return:
    """
    if request.method == "GET":
        return """\
        To get response with custom status code 
        send request using POST method 
        and pass `code` in JSON body / FormData
        """

    print("raw bytes data:", request.data)

    if request.form and "code" in request.form:
        return "code from form", request.form["code"]

    if request.json and "code" in request.json:
        return "code from json", request.json["code"]

    return "", 204


@app.before_request
def process_before_request():
    """
    Sets start_time to `g` object

    :return:
    """
    g.start_time = time()


@app.after_request
def process_after_request(response):
    """
    adds process time in headers

    Example: visit http://127.0.0.1:5000/greet/GitHub/
    headers will contain:
    < process-time: 0.0001270771026611328

    :param response:
    :return:
    """
    if hasattr(g, "start_time"):
        response.headers["process-time"] = time() - g.start_time

    return response
