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