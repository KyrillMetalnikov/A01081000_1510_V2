from unittest import TestCase
import country


class TestCountry(TestCase):
    def test_init_proper_use(self):
        canada = country.Country("Canada", 36290000, 9985000)
        actual = [canada.name, canada.population, canada.area]
        expected = ["Canada", 36290000, 9985000]
        self.assertEqual(actual, expected)
