# Flask lessons

## tech:
- Python 3.9.1
- Flask 1.1.2
- Bootstrap v5.0.0-beta1
- SQLAlchemy==1.3.22
- Flask-SQLAlchemy==2.4.4
- Flask-Login==0.5.0
- alembic==1.4.3
- Flask-Migrate==2.5.3


### Lessons:
1. Getting started with werkzeug and Flask ([result](https://github.com/mahenzon/flask-lessons/tree/lesson-1))
    - install requirements
    - create app and run it
    - parse path (variable-rules)
    - use query params (request.args)
    - send custom http codes
    - read data from form and json body
    - `before_request` and `after_request`, `g` object, response headers
    - raise werkzeug exceptions (like `BadRequest`), use `app.logger`
    - process unhandled exceptions using `app.errorhandler`, use `app.logger.exception`

2. Templates: Jinja2 ([result](https://github.com/mahenzon/flask-lessons/tree/lesson-2))
    - create base template and index template
    - create users blueprint, list view and template
    - create user details view and template, handle user not found
    - create endpoints for users app, use `url_for` for links
    - add and connect bootstrap 5, use starter template
    - add navbar with links
    - create articles blueprint, list view and template, add to navbar

3. Flask-SQLAlchemy; Flask-Login ([result](https://github.com/mahenzon/flask-lessons/tree/lesson-3))
    - install and setup Flask-SQLAlchemy
    - create User model
    - create commands init-db and create-users
    - upgrade users list / details to use db (load users from db)
    - install Flask-Login, update User model with UserMixin
    - configure LoginManager, create login and logout views, update templates
    - use `login_required` to restrict access to views

4. Docker, docker-compose, Postgres. Schema migrations using Flask-Migrate + alembic ([result](https://github.com/mahenzon/flask-lessons/tree/lesson-4))
    - install psycopg2
    - create class-based configs, move configuration there
    - create Dockerfile for the app
    - create docker-compose for the project, connect Postgres
    - install and configure Flask-Migrate
    - create first migration: add user table
    - add email field to the User model
    - change command create-users to create-admin
    - set compare_type = True and demo column changes
