"""Configure application variables."""
import os

basedir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# options
WTF_CSRF_ENABLED = True
SECRET_KEY = 'qoOOpYr3q89c'
EXPLAIN_TEMPLATE_LOADING = False


ALLOWED_EXTENSIONS = set(['jpg'])

# some friendly defaults for db connections
# MYSQLDB_HOST = os.environ.get('MYSQLDB_HOST', '127.0.0.1')
# MYSQLDB_USER = os.environ.get('MYSQLDB_USER', '<set.at.runtime>')
# MYSQLDB_PASS = os.environ.get('MYSQLDB_PASS', '<set.at.runtime>')
# MYSQLDB_NAME = os.environ.get('MYSQLDB_NAME', '<set.at.runtime>')

# SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://%s:%s@%s:3306/%s" %
#                            (MYSQLDB_USER, MYSQLDB_PASS, MYSQLDB_HOST, MYSQLDB_NAME))
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_POOL_RECYCLE = 300
# SQLALCHEMY_POOL_TIMEOUT = 10
# SQLALCHEMY_POOL_SIZE = 10
# SQLALCHEMY_MAX_OVERFLOW = 10


# folder paths
CSS_FOLDER = basedir + '/website/static/css/'
IMAGES_FOLDER = basedir + '/website/static/img/'
JS_FOLDER = basedir + '/website/static/dist/'
# UPLOADS_FOLDER = basedir + '/website/views/uploads/'

# template paths
ABORT_TEMPLATES = basedir + '/website/templates/abort/'
