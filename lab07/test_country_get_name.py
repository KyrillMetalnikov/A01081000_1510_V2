from unittest import TestCase
import country


class TestCountry(TestCase):
    def test_get_name(self):
        canada = country.Country("Canada", 36290000, 9985000)
        actual = canada.get_name()
        expected = "Canada"
        self.assertEqual(actual, expected)
