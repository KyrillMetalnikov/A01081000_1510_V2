from unittest import TestCase
import recursion


class Test(TestCase):
    def test_factorial_iterative_zero(self):
        actual = recursion.factorial_iterative(0)
        expected = 1
        self.assertEqual(actual, expected)
