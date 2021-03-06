from unittest import TestCase
import sparse_vector


class Test(TestCase):
    def test_sparse_add_dict_length_0(self):
        actual = sparse_vector.sparse_add({'length': 0}, {'length': 0})
        expected = {'length': 0}
        self.assertEqual(actual, expected)

    def test_sparse_add_different_length(self):
        actual = sparse_vector.sparse_add({0: 1, 5: 2, 6: 1, 'length': 7}, {1: 2, 3: 2, 6: 2, 'length': 8})
        expected = None
        self.assertEqual(actual, expected)

    def test_sparse_add_ordered_dictionary(self):
        actual = sparse_vector.sparse_add({0: 1, 5: 2, 6: 1, 'length': 8}, {1: 2, 3: 2, 6: 2, 'length': 8})
        expected = {'length': 8, 0: 1, 1: 2, 3: 2, 5: 2, 6: 3}
        self.assertEqual(actual, expected)

    def test_sparse_add_unordered_with_negatives(self):
        actual = sparse_vector.sparse_add({4: -5, 'length': 5, 0: 4.3}, {'length': 5, 2: 7.5, 4: -6})
        expected = {'length': 5, 0: 4.3, 2: 7.5, 4: -11}
        self.assertEqual(actual, expected)

    def test_sparse_add_complementary_values(self):
        actual = sparse_vector.sparse_add({0: 1, 1: 2, 2: 3, 'length': 8}, {0: -1, 1: -2, 2: -3, 'length': 8})
        expected = {'length': 8}
        self.assertEqual(expected, actual)

    def test_sparse_add_all_zeroes(self):
        actual = sparse_vector.sparse_add({'length': 5, 0: 0, 1: 0, 2: 0, 3: 0}, {'length': 5, 0: 0, 1: 0, 2: 0, 3: 0})
        expected = {'length': 5}
        self.assertEqual(expected, actual)

    def test_sparse_add_one_dict_all_zeroes(self):
        actual = sparse_vector.sparse_add({'length': 5, 0: 0, 1: 0, 2: 0, 3: 0}, {'length': 5, 0: 1, 1: 2, 2: 3, 3: 4})
        expected = {'length': 5, 0: 1, 1: 2, 2: 3, 3: 4}
        self.assertEqual(expected, actual)
