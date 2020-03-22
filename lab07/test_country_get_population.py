from unittest import TestCase
import country


class TestCountry(TestCase):
    def test_get_population(self):
        canada = country.Country("Canada", 36290000, 9985000)
        actual = canada.get_population()
        expected = 36290000
        self.assertEqual(expected, actual)
