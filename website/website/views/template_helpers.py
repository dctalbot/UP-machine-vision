"""Helper methods used in jinja templates."""

from website import app
from website.config import IMAGES_FOLDER

from flask import send_from_directory


# ==============================
# =======      OTHER     =======
# ==============================

@app.route('/assets/images/<filename>')
def download_img(filename):
    """Download image from static/img folder."""
    return send_from_directory(IMAGES_FOLDER, filename)

# @app.route('/assets/images/<filename>')
# def download_from_uploads(filename):
#     """Download image from views/uploads folder."""
#     return send_from_directory(UPLOADS_FOLDER, filename)
