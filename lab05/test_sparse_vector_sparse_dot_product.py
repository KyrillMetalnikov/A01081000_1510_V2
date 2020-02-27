from unittest import TestCase
import sparse_vector


class Test(TestCase):
    def test_sparse_dot_product_length_zero(self):
        actual = sparse_vector.sparse_dot_product({'length': 0}, {'length': 0})
        expected = 0
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_different_length(self):
        actual = sparse_vector.sparse_dot_product({0: 1, 5: 2, 6: 1, 'length': 7}, {1: 2, 3: 2, 6: 2, 'length': 8})
        expected = None
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_same_length(self):
        actual = sparse_vector.sparse_dot_product({0: 1, 5: 2, 6: 1, 'length': 8}, {1: 2, 3: 2, 6: 2, 'length': 8})
        expected = 2
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_unordered_with_negatives(self):
        actual = sparse_vector.sparse_dot_product({4: -5, 'length': 5, 0: 4.3}, {'length': 5, 2: 7.5, 4: -6})
        expected = 30
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_same_length_all_zeroes(self):
        actual = sparse_vector.sparse_dot_product({'length': 5, 0: 0, 1: 0, 2: 0}, {'length': 5, 0: 0, 1: 0, 2: 0})
        expected = 0
        self.assertEqual(actual, expected)