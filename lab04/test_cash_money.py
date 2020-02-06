from unittest import TestCase

import lab04


class Test(TestCase):
    def test_cash_money_zero(self):
        """Test cash_money for value 0."""
        argument = lab04.cash_money(0)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, argument, "The list is all zeroes")

    def test_cash_money_one_hundred(self):
        """Test cash_money for value 100."""
        argument = lab04.cash_money(100)
        expected = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, argument, "Only the hundred dollar value is increased")

    def test_cash_money_all_numbers(self):
        """Test cash_money where every list is non-zero."""
        argument = lab04.cash_money(188.93)
        expected = [1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3]
        self.assertEqual(expected, argument, "The list is all non-zeroes")

    def test_cash_money_big_number(self):
        """Test cash_money with a large parameter input."""
        argument = lab04.cash_money(1000000)
        expected = [10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, argument, "The list has a large first element")
