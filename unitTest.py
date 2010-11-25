# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '../distlib.zip')

import gaeunit
import unittest
import main


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()

    def tearDown(self):
        pass

    def test(self):
        rv = self.app.get('/hello/')
        assert 'Hello World!' in rv.data


if __name__ == '__main__':
    unittest.main()

