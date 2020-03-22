from unittest import TestCase
import country


class TestCountry(TestCase):
    def test_is_larger_true(self):
        canada = country.Country("Canada", 36290000, 9985000)
        denmark = country.Country("Denmark", 5603000, 42933)
        actual = canada.is_larger(denmark)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_larger_false(self):
        canada = country.Country("Canada", 36290000, 9985000)
        denmark = country.Country("Denmark", 5603000, 42933)
        actual = denmark.is_larger(canada)
        expected = False
        self.assertEqual(actual, expected)
