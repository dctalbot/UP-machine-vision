#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Launch Flask app with suitable environment."""

import logging
import sys

from website import app
from werkzeug.serving import WSGIRequestHandler
from wsgiref.simple_server import make_server


# Override the built-in werkzeug logging function to change log line format.
werkzeug_logger = logging.getLogger('werkzeug')
WSGIRequestHandler.log = lambda self, type, message, *args: \
        getattr(werkzeug_logger, type)(
            '%s - %s [%s] %s' %
            (self.environ.get("REMOTE_ADDR", "0.0.0.0"),
                self.environ.get("REMOTE_USER", "-"),
                self.log_date_time_string(),
                message % args)
        )

if __name__ == '__main__':
    # Default behavior is bind to 127.0.0.1 ONLY

    mode = 'local'
    if len(sys.argv) > 1:
        # Looking for 'share' guys
        mode = sys.argv[1]
    if mode == 'share':
        print(">>>>>> Sharing mode!  Listening on all interfaces.")
        # Bind to all interfaces, and suffer the consequences!
        # Wrapping flask in a trivial basic_auth configuration.
        # The user:pass is set in environent a la
        #   export WSGI_AUTH_CREDENTIALS=foo:bar
        #   from wsgi_basic_auth import BasicAuth
        #   app = BasicAuth(app)
        app = BasicAuth(app)
        httpd = make_server('', 8080, app)
        httpd.serve_forever()
    else:
        print('>>>>>> Local mode.  Only for you.')
        app.run(host='127.0.0.1', port=4000, debug=True)
