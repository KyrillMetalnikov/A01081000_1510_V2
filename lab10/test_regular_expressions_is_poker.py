from unittest import TestCase
import regular_expressions


class Test(TestCase):
    def test_is_poker_four_of_a_kind_numbers(self):
        expected = True
        actual = regular_expressions.is_poker("22223")
        self.assertEqual(expected, actual)
