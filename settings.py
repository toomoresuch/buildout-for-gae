# -*- coding: utf-8 -*-

# APP_NAME = 'kay_main'
# DEFAULT_TIMEZONE = 'Asia/Tokyo'

"""
A sample of kay settings.

:Copyright: (c) 2009 Accense Technology, Inc. 
                     Takashi Matsuo <tmatsuo@candit.jp>,
                     All rights reserved.
:license: BSD, see LICENSE for more details.
"""

DEBUG = True

# PROFILE = False
# PRINNT_CALLERS_ON_PROFILING = False
# PRINNT_CALLEES_ON_PROFILING = False

SECRET_KEY = 'ReplaceItWithSecretString'

# SESSION_PREFIX = 'gaesess:'

COOKIE_AGE = 86400  # 1day
COOKIE_NAME = 'KAY_SESSION'

# SESSION_MEMCACHE_AGE = 360

SESSION_STORE = kay.sessions.sessionstore.SecureCookieSessionStore

# kay.sessions.sessionstore.GAESessionStore

# LANG_COOKIE_AGE = COOKIE_AGE
# LANG_COOKIE_NAME = hl
# FLASH_COOKIE_NAME = 'KAY_FLASH'

CACHE_MIDDLEWARE_SECONDS = 60

# CACHE_MIDDLEWARE_NAMESPACE = CACHE_MIDDLEWARE
# CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

ADD_APP_PREFIX_TO_KIND = True

# FORMS_USE_XHTML = False
# ROOT_URL_MODULE = urls

MEDIA_URL = '/statics'

# INTERNAL_MEDIA_URL = /_media

ADMINS = ('hoge', 'fuga@example.com')

# NOTIFY_ERRORS_TO_GAE_ADMINS = True
# TEMPLATE_DIRS = ()
# USE_I18N = True
# DEFAULT_LANG = 'en'

INSTALLED_APPS = ()

APP_MOUNT_POINTS = {}

# You can remove following settings if unnecessary.

CONTEXT_PROCESSORS = ('kay.context_processors.request',
                      'kay.context_processors.url_functions',
                      'kay.context_processors.media_url')

# JINJA2_FILTERS = {}
# JINJA2_ENVIRONMENT_KWARGS = {'autoescape': True,}
# JINJA2_EXTENSIONS = ('jinja2.ext.i18n',)
# SUBMOUNT_APPS = ()
# MIDDLEWARE_CLASSES = ()
# AUTH_USER_BACKEND = kay.auth.backends.googleaccount.GoogleBackend
# AUTH_USER_MODEL = kay.auth.models.GoogleUser

USE_DB_HOOK = False

DEFAULT_MAIL_FROM = 'fuga@example.com'

# PER_DOMAIN_SETTINGS = {
#   'foo.example.com': 'foo_settings', 'bar.example.com': 'bar_settings',
# }

