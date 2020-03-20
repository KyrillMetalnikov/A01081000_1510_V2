from unittest import TestCase
import exceptions


class Test(TestCase):
    def test_find_an_even_empty_list(self):
        with self.assertRaises(ValueError):
            exceptions.findAnEven([])

    def test_find_an_even_one_even(self):
        actual = exceptions.findAnEven([1, 4, 5, 9, 11])
        expected = 4
        self.assertEqual(actual, expected)
