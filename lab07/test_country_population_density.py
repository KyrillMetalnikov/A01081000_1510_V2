from unittest import TestCase
import country


class TestCountry(TestCase):
    def test_population_density(self):
        canada = country.Country("Canada", 36290000, 9985000)
        actual = canada.population_density()
        expected = 3.6344516775162745
        self.assertEqual(actual, expected)