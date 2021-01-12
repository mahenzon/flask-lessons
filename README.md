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
- Flask-Admin==1.5.7
- Flask-COMBO-JSONAPI==1.0.4
- ComboJSONAPI==1.0.5
- apispec==2.0.2


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

5. Flask-Bcrypt, WTForms. Allow users to register and login ([result](https://github.com/mahenzon/flask-lessons/tree/lesson-5))
    - install and configure Flask-Bcrypt
    - create password field for user, hash it
    - add first_name and last_name to User, mark email field as unique
    - install WTForms + email-validator and Flask-WTF
    - create template macro render_field
    - enable csrf protection
    - create RegistrationForm
    - create register template
    - create register view, register user
    - move existing 'login' view to 'login_as' (for admins)
    - create login view for users

6. Author and Article models. Relationships one-to-one and one-to-many ([result](https://github.com/mahenzon/flask-lessons/tree/lesson-6))
    - create Author and Article models, add relationships
    - create views for authors and articles
    - create view for creating an article

7. Tag model. Article-Tag association. Many-to-many relationship ([result](https://github.com/mahenzon/flask-lessons/tree/lesson-7))
    - create Tag model
    - create Article-Tag association table
    - configure relationships
    - add command for creating tags
    - update CreateArticleForm with SelectMultipleField for adding tags
    - set selected Tags to Article on create 
    - load tags for article using joinedload
    - show Article tags on article details view

8. Flask-Admin ([result](https://github.com/mahenzon/flask-lessons/tree/lesson-8))
    - install and configure Flask-Admin
    - create base CustomView, add models to admin
    - add string representations to models
    - customize Tag admin view to add features: `column_searchable_list`, `column_filters`, `can_export`
    - customize User admin view, demo `column_exclude_list`, `column_editable_list`, `can_create`, `can_edit`, `can_delete`
    - limit view access only for staff
    - limit admin index access only for staff too

9. JSON REST API. CRUD, swagger, marshmallow, flask-combo-jsonapi, combojsonapi ([result](https://github.com/mahenzon/flask-lessons/tree/lesson-9))
    - install Flask-COMBO-JSONAPI
    - create first marshmallow Schema
    - create first ResourceList and ResourceDetail
    - register first api views
    - install ComboJSONAPI and apispec + PyYAML
    - create and use api spec plugin
    - create schemas and views for the rest of models

10. flask-combo-jsonapi, combojsonapi: EventPlugin, PermissionPlugin ([result](https://github.com/mahenzon/flask-lessons/tree/lesson-10))
    - add EventPlugin
    - create ArticleListEvents: event_get_count
    - create AuthorDetailEvents: event_get_articles_count
    - create UserDetailEvents: event_update_avatar. Add YAML spec
    - setup PermissionPlugin
    - create UserPermission
    - add UserPermission for User views
    - create permission for PATCH user
