from unittest import TestCase
import exceptions
import math


class Test(TestCase):
    def test_heron_perfect_root(self):
        expected = 10.0
        actual = exceptions.heron(100)
        self.assertEqual(actual, expected)

    def test_heron_float(self):
        expected = math.sqrt(5.5)
        actual = exceptions.heron(5.5)
        self.assertAlmostEqual(actual, expected)

    def test_heron_non_perfect_int(self):
        expected = math.sqrt(42)
        actual = exceptions.heron(42)
        self.assertAlmostEqual(actual, expected)

    def test_heron_error(self):
        actual = exceptions.heron(-1)
        self.assertRaises(ZeroDivisionError)