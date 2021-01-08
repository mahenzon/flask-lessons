from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required

from blog.models import User

login_manager = LoginManager()
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


def login():
    if request.method == "GET":
        return render_template("auth/login.html")

    username = request.form.get("username")
    if not username:
        return render_template("auth/login.html", error="username not passed")

    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return render_template("auth/login.html", error=f"no user {username!r} found")

    # TODO: require password and validate it

    login_user(user)
    return redirect(url_for("index"))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("login"))


@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@login_required
def secret_view():
    return "Super secret data"


def init_auth_views(app: Flask):
    app.add_url_rule("/login/", view_func=login, methods=["GET", "POST"])
    app.add_url_rule("/logout/", view_func=logout)
    app.add_url_rule("/secret/", view_func=secret_view)


__all__ = [
    "login_manager",
    "init_auth_views",
]
