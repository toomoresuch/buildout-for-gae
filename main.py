# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, './distlib.zip')

from google.appengine.ext.webapp.util import run_wsgi_app
from application import app

run_wsgi_app(app)

