from unittest import TestCase
import exceptions
import math


class Test(TestCase):
    def test_heron_perfect_root(self):
        actual = 10.0
        expected = exceptions.heron(100)
        self.assertEqual(actual, expected)

    def test_heron_float(self):
        actual = math.sqrt(5.5)
        expected = exceptions.heron(5.5)
        self.assertAlmostEqual(actual, expected)

    def test_heron_non_perfect_int(self):
        actual = math.sqrt(42)
        expected = exceptions.heron(42)
        self.assertAlmostEqual(actual, expected)