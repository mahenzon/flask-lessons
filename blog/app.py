import os
from flask import Flask, render_template
from flask_migrate import Migrate

from blog.security import flask_bcrypt
from blog.admin import admin
from blog.views.auth import login_manager, auth_app
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.views.authors import authors_app
from blog.models.database import db
from blog.api import init_api

cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"

app = Flask(__name__)
app.config.from_object(f"blog.configs.{cfg_name}")

# security
flask_bcrypt.init_app(app)

# admin
admin.init_app(app)

# views
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(authors_app, url_prefix="/authors")

# api views
api = init_api(app)

# db
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

# auth
login_manager.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.cli.command("create-admin")
def create_admin():
    """
    Run in your terminal:
    ➜ flask create-admin
    > created admin: <User #1 'admin'>
    """
    from blog.models import User

    # # delete existing admin ?
    # User.query.filter_by(username="admin").delete(synchronize_session="fetch")

    # create new
    admin = User(username="admin", is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"

    db.session.add(admin)
    db.session.commit()

    print("created admin:", admin)


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)

    db.session.commit()
    print("created tags")
