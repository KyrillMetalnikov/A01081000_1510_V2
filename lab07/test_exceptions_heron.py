from unittest import TestCase
import math
import io
from unittest.mock import patch
import exceptions


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

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_heron_error_print_value(self, mock_stdout):
        exceptions.heron(-1)
        expected = "Error: The number provided must be positive!\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_heron_error_return_value(self):
        actual = exceptions.heron(-1)
        expected = -1
        self.assertEqual(actual, expected)
