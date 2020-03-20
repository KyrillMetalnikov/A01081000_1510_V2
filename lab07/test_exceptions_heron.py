from unittest import TestCase
import exceptions
import math


class Test(TestCase):
    def test_heron_perfect_root(self):
        actual = 10.0
        expected = exceptions.heron(100)
        self.assertEqual(actual, expected)