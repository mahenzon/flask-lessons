# Flask lessons

## tech:
- Python 3.9.1
- Flask 1.1.2
- Bootstrap v5.0.0-beta1


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
