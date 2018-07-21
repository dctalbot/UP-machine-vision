"""Error handlers live here."""

from website import app
from flask import render_template


@app.errorhandler(400)
def bad_Request(e):
    """400: bad request"""
    return render_template('/abort/400.html'), 400


@app.errorhandler(404)
def page_not_found(e):
    """404: page not found"""
    return render_template('/abort/404.html'), 404


@app.errorhandler(403)
def unauthorized(e):
    """403: unauthorized access"""
    return render_template('/abort/403.html'), 403


@app.errorhandler(500)
def unhandled_exception(e):
    """500: internal server error"""
    return render_template('/abort/500.html'), 500
