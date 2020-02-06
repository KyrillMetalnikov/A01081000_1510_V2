from unittest import TestCase
import lab04

"""Test the eratosthenes function from lab04 module."""


class Test(TestCase):
    def test_eratosthenes_zero(self):
        """Test eratosthenes for a value of 0"""
        argument = lab04.eratosthenes(0)
        expected = []
        self.assertEqual(expected, argument, "The list is empty")

    def test_eratosthenes_one(self):
        """Test eratosthenes for a value of 1"""
        argument = lab04.eratosthenes(1)
        expected = []
        self.assertEqual(expected, argument, "The list is empty")

    def test_eratosthenes_two(self):
        """Test eratosthenes for a value of 2"""
        argument = lab04.eratosthenes(2)
        expected = [2]
        self.assertEqual(expected, argument, "The list has one element with value of 2")

    def test_eratosthenes_mid_value(self):
        """Test eratosthenes for medium sized value"""
        argument = lab04.eratosthenes(29)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(expected, argument, "The list contains multiple elements with prime numbered values")

    def test_eratosthenes_large_value(self):
        """Test eratosthenes for a large value"""
        argument = lab04.eratosthenes(100)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(expected, argument, "The list contains multiple elements with prime numbered values")

