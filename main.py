# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, './distlib.zip')

import re
from itty import *

target = re.compile(r'ja')


@get('/')
def accept_lang(request):
    ja = str(request._environ.get('HTTP_ACCEPT_LANGUAGE'))

    if target.match(ja):
        raise Redirect('/ja/')
    else:
        raise Redirect('/en/')


def index(request):
    return 'Hello World!'


run_itty(server='appengine')

