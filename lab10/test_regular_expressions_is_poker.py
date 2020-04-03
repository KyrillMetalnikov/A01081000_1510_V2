from unittest import TestCase
import regular_expressions


class Test(TestCase):
    def test_is_poker_four_of_a_kind_numbers(self):
        expected = True
        actual = regular_expressions.is_poker("22223")
        self.assertEqual(expected, actual)

    def test_is_poker_four_of_a_kind_letters(self):
        expected = True
        actual = regular_expressions.is_poker("ttttk")
        self.assertEqual(expected, actual)

    def test_is_poker_full_house_mix(self):
        expected = True
        actual = regular_expressions.is_poker("222jj")
        self.assertEqual(expected, actual)

    def test_is_poker_three_of_a_kind(self):
        expected = True
        actual = regular_expressions.is_poker("222jk")
        self.assertEqual(expected, actual)

    def test_is_poker_two_pair(self):
        expected = True
        actual = regular_expressions.is_poker("qqaa3")
        self.assertEqual(expected, actual)

    def test_is_poker_pair(self):
        expected = True
        actual = regular_expressions.is_poker("66jqk")
        self.assertEqual(expected, actual)

    def test_is_poker_high_card(self):
        expected = True
        actual = regular_expressions.is_poker("aqj45")
        self.assertEqual(expected, actual)

    def test_is_poker_four_cards(self):
        expected = False
        actual = regular_expressions.is_poker("ajqk")
        self.assertEqual(expected, actual)

    def test_is_poker_six_cards(self):
        expected = False
        actual = regular_expressions.is_poker("ajqk34")
        self.assertEqual(expected, actual)

    def test_is_poker_five_of_a_kind(self):
        expected = False
        actual = regular_expressions.is_poker("jjjjj")
        self.assertEqual(expected, actual)