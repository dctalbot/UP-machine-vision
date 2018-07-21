from website import app
from wsgi_basic_auth import BasicAuth

# Enable outrageously complete request dumping.
# app.wsgi_app = ExtremeRequestLogging(app.wsgi_app)

# If being proxied, plumb environment to pick up remote user, addr, etc.
# application.wsgi_app = SmiProxyPlumbing(application.wsgi_app)

# app = BasicAuth(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
