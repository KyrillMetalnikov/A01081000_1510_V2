from unittest import TestCase
from unittest.mock import patch
import io
import country


class TestCountry(TestCase):
    def test_init_proper_use(self):
        canada = country.Country("Canada", 36290000, 9985000)
        actual = [canada.__name, canada.__population, canada.__area]
        expected = ["Canada", 36290000, 9985000]
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_init_wrong_population(self, mock_stdout):
        canada = country.Country("Canada", -25, 9985000)
        expected = "A population cannot be negative!\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_init_wrong_area(self, mock_stdout):
        canada = country.Country("Canada", 36290000, -30)
        expected = "An area cannot be negative!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
