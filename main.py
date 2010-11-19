# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, './distlib.zip')

from itty import *


@get('/')
def index(request):
    return 'Hello World!'

run_itty(server='appengine')

