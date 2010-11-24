# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'distlib.zip')

# -----------------------------------------------------------------------------
#  IMPORTS.
# -----------------------------------------------------------------------------

import re

from flask import Flask
from flask import redirect
from flask import request

# -----------------------------------------------------------------------------
#  CONFIGURATION.
# -----------------------------------------------------------------------------

app = Flask(__name__)

# set the secret key.  keep this really secret:

app.secret_key = 'the secret key'
app.debug = True

target = re.compile(r'ja')

# -----------------------------------------------------------------------------
#  METHODS.
# -----------------------------------------------------------------------------


@app.route('/')
def accept_lang():
    if target.match(str(request.accept_languages.best)):
        return redirect('/ja/')
    else:
        return redirect('/en/')


@app.route('/hello/')
def index():
    return 'Hello World!'

# -----------------------------------------------------------------------------
#  MAIN.
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    app.run()

