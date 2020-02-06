from unittest import TestCase

import lab04

"""Test the cash_money function from the lab04 module."""


class Test(TestCase):
    def test_cash_money_zero(self):
        """Test cash_money for value 0."""
        argument = lab04.cash_money(0.00)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, argument, "The list is all zeroes")

    def test_cash_money_one_cent(self):
        """Test cash_money for one penny."""
        argument = lab04.cash_money(0.01)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        self.assertEqual(expected, argument, "The pennies element is the only non-zero element")

    def test_cash_money_two_cents(self):
        """Test cash_money for two pennies."""
        argument = lab04.cash_money(0.02)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
        self.assertEqual(expected, argument, "The pennies element is 2 and the rest are all zeroes")

    def test_cash_money_nickel(self):
        """Test cash_money for one nickel."""
        argument = lab04.cash_money(0.05)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        self.assertEqual(expected, argument, "The nickel element is the only non-zero element")

    def test_cash_money_dime(self):
        """Test cash_money for one dime."""
        argument = lab04.cash_money(0.10)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        self.assertEqual(expected, argument, "The dimes element is the only non-zero element")

    def test_cash_money_quarter(self):
        """Test cash_money for one quarter."""
        argument = lab04.cash_money(0.25)
        expected = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        self.assertEqual(expected, argument, "The quarter element is the only non-zero element")

    def test_cash_money_one_dollar(self):
        """Test cash_money for one dollar."""
        argument = lab04.cash_money(1.00)
        expected = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        self.assertEqual(expected, argument, "The loonie element is the only non-zero element")

    def test_cash_money_one_dollar_five_cents(self):
        """Test cash_money for one dollar and five cents."""
        argument = lab04.cash_money(1.05)
        expected = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
        self.assertEqual(expected, argument, "The loonie element and the nickel element are the non-zero elements")

    def test_cash_money_two_dollars(self):
        """Test cash_money for two dollars."""
        argument = lab04.cash_money(2.00)
        expected = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        self.assertEqual(expected, argument, "The toonie element is the only non-zero element")

    def test_cash_money_five_dollars(self):
        """Test cash_money for five dollars."""
        argument = lab04.cash_money(5.00)
        expected = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, argument, "The fives element is the only non-zero element")

    def test_cash_money_ten_dollars(self):
        """Test cash_money for ten dollars."""
        argument = lab04.cash_money(10.00)
        expected = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, argument, "The tens element is the only non-zero element")

    def test_cash_money_twenty_dollars(self):
        """Test cash_money for twenty dollars."""
        argument = lab04.cash_money(20.00)
        expected = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, argument, "The twenties element is the only non-zero element")

    def test_cash_money_fifty_dollars(self):
        """Test cash_money for fifty dollars."""
        argument = lab04.cash_money(50.00)
        expected = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, argument, "The fifties element is the only non-zero element")

    def test_cash_money_one_hundred(self):
        """Test cash_money for one hundred dollars."""
        argument = lab04.cash_money(100.00)
        expected = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, argument, "The hundreds element is the only non-zero element")

    def test_cash_money_all_numbers(self):
        """Test cash_money where every list is non-zero."""
        argument = lab04.cash_money(188.93)
        expected = [1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3]
        self.assertEqual(expected, argument, "The list is all non-zeroes")

    def test_cash_money_hundred_dollars_fifty_seven_cents(self):
        """Test cash_money with a hundred dollars and fifty seven cents."""
        argument = lab04.cash_money(100.57)
        expected = [1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 2]
        self.assertEqual(expected, argument, "A variety of elements are non-zeroes")

    def test_cash_money_big_number(self):
        """Test cash_money with a large parameter input."""
        argument = lab04.cash_money(1000000)
        expected = [10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, argument, "The list has a large first element")
