from unittest import TestCase
from unittest.mock import patch
import io
import country


class TestCountry(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_str(self, mock_stdout):
        canada = country.Country("Canada", 36290000, 9985000)
        print(canada)
        expected = "Canada has a population of 36290000 and is 9985000 square kilometres.\n"
        self.assertEqual(expected, mock_stdout.getvalue())