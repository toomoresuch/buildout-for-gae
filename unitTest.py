# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '../distlib.zip')

import gaeunit
import unittest
from main import index


class Test(unittest.TestCase):

    def test(self):
        res = index({})
        self.assertEqual(res, 'Hello World!')


if __name__ == '__main__':

    # import sys;sys.argv = ['', 'Test.testName']

    unittest.main()

