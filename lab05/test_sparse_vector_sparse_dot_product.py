from unittest import TestCase
import sparse_vector


class Test(TestCase):
    def test_sparse_dot_product_length_zero(self):
        actual = sparse_vector.sparse_dot_product({'length': 0}, {'length': 0})
        expected = 0
        self.assertEqual(actual, expected)
