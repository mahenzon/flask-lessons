from flask import Blueprint, render_template

users_app = Blueprint("users_app", __name__)


USERS = {
    1: "James",
    2: "Brian",
    3: "Peter",
}


@users_app.route("/")
def users_list():
    return render_template("users/list.html", users=USERS)
