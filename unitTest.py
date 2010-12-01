# -*- coding: utf-8 -*-

from google.appengine.ext import db
from kay.app import get_application
from kay.ext.testutils.gae_test_base import GAETestBase
from werkzeug import BaseResponse, Client, Request

import unittest


class TestCase(unittest.TestCase):

    # USE_PRODUCTION_STUBS = True
    # USE_REMOTE_STUBS = True

    CLEANUP_USED_KIND = True

    def setUp(self):

        app = get_application()
        self.client = Client(app, BaseResponse)

    def tearDown(self):
        pass

    def test(self):
        response = self.client.get('/')
        assert response.status_code is 200



