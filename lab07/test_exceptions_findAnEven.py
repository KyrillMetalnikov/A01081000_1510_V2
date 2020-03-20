from unittest import TestCase
import exceptions


class Test(TestCase):
    def test_find_an_even_empty_list(self):
        with self.assertRaises(ValueError):
            exceptions.findAnEven([])
