#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_testrepo
----------------------------------

Tests for `testrepo` module.
"""

import unittest

from testrepo import testrepo


class TestTestrepo(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert testrepo.test_func() == "hello"

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
