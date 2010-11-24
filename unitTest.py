# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '../distlib.zip')

import root
import gaeunit
import unittest


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = root.app.test_client()

    def tearDown(self):
        pass

    def test(self):
        rv = self.app.get('/hello/')
        assert 'Hello World!' in rv.data


if __name__ == '__main__':
    unittest.main()

