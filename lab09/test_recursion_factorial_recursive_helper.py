from unittest import TestCase
import recursion


class Test(TestCase):
    def test_factorial_recursive_helper_zero(self):
        actual = recursion.factorial_recursive_helper(0)
        expected = 1
        self.assertEqual(actual, expected)

    def test_factorial_recursive_helper_one(self):
        actual = recursion.factorial_recursive_helper(1)
        expected = 1
        self.assertEqual(actual, expected)

