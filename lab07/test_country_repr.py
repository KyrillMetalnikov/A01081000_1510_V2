from unittest import TestCase
import country


class TestCountry(TestCase):
    def test_country_repr(self):
        canada = country.Country("Canada", 36290000, 9985000)
        actual = canada.__repr__()
        expected = 'Country("Canada", 36290000, 9985000)'
        self.assertEqual(actual, expected)

