"""Initializes the Flask app."""

from sassutils.wsgi import SassMiddleware
from flask import Blueprint, Flask
from flask_cors import CORS


# from website.views.courses import courses
# from website.views.export import export
# from website.views.subjects import subjects

# app is a single object used by all the code modules in this package
app = Flask(__name__)
CORS(app)

# compile sass into /static/css
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'website': ('static/sass', 'static/css', '/static/css')
})

# Read settings from config module
app.config.from_object('website.config')

# blueprints
# app.register_blueprint(courses, url_prefix="/courses")
# app.register_blueprint(export, url_prefix="/export")
# app.register_blueprint(subjects, url_prefix="/subjects")


# bind the db to the app
# db.init_app(app)

# Tell our app about views and models.  This is dangerously close to a
# circular import, which is naughty, but Flask was designed that way.
# (Reference http://flask.pocoo.org/docs/0.12/patterns/packages/)
import website.views.index
import website.views.template_helpers
# import website.roles
# import website.views.error_handlers
