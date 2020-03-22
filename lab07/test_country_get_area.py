from unittest import TestCase
import country


class TestCountry(TestCase):
    def test_get_area(self):
        canada = country.Country("Canada", 36290000, 9985000)
        actual = canada.get_area()
        expected = 9985000
        self.assertEqual(actual, expected)
