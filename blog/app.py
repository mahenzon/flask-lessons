import os
from flask import Flask, render_template
from flask_migrate import Migrate

from blog.views.auth import login_manager, auth_app
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db

cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"

app = Flask(__name__)
app.config.from_object(f"blog.configs.{cfg_name}")

# views
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")

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

    admin = User(username="admin", is_staff=True)

    db.session.add(admin)
    db.session.commit()

    print("created admin:", admin)
