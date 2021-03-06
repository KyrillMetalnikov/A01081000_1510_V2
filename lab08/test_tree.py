from unittest import TestCase
from unittest.mock import patch
import io
import tree


class TestTree(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_tree_for_init_species(self, mock_stdout):
        tree1 = tree.Tree("Oak", 2, 2.0)
        print(tree1)
        expected = "Tree('species = Oak', age = 2, circumference = 2.0)\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_tree_for_init_empty_species(self):
        with self.assertRaises(ValueError):
            tree1 = tree.Tree("", 2, 2.0)

    def test_tree_for_init_species_only_white_space(self):
        with self.assertRaises(ValueError):
            tree1 = tree.Tree("      ", 2, 2.0)

    def test_tree_for_init_negative_age(self):
        with self.assertRaises(ValueError):
            tree1 = tree.Tree("Oak", -2, 2.0)

    def test_tree_for_init_negative_circumference(self):
        with self.assertRaises(ValueError):
            tree1 = tree.Tree("Oak", 2, -2.0)

    def test_tree_get_species(self):
        tree1 = tree.Tree("Oak", 2, 2.0)
        actual = tree1.get_species()
        expected = "Oak"
        self.assertEqual(actual, expected)

    def test_tree_get_age(self):
        tree1 = tree.Tree("Oak", 2, 2.0)
        actual = tree1.get_age()
        expected = 2
        self.assertEqual(actual, expected)

    def test_tree_get_circumference(self):
        tree1 = tree.Tree("Oak", 2, 2.0)
        actual = tree1.get_circumference()
        expected = 2.0
        self.assertEqual(actual, expected)

    def test_tree_set_age_correct_use(self):
        tree1 = tree.Tree("Oak", 2, 2.0)
        tree1.set_age(5)
        actual = tree1.get_age()
        expected = 5
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_tree_set_age_negative_age(self, mock_stdout):
        tree1 = tree.Tree("Oak", 2, 2.0)
        tree1.set_age(-5)
        expected = "Error: age cannot be a negative number.\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_tree_set_circumference_correct_use(self):
        tree1 = tree.Tree("Oak", 2, 2.0)
        tree1.set_circumference(5.0)
        actual = tree1.get_circumference()
        expected = 5.0
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_tree_set_circumference_negative_circumference(self, mock_stdout):
        tree1 = tree.Tree("Oak", 2, 2.0)
        tree1.set_circumference(-5.0)
        expected = "Error: circumference cannot be a negative number.\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_tree_print_tree(self, mock_stdout):
        tree1 = tree.Tree("Oak", 2, 2.0)
        print(tree1)
        expected = "Tree('species = Oak', age = 2, circumference = 2.0)\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_tree_repr(self):
        tree1 = tree.Tree("Oak", 2, 2.0)
        actual = tree1.__repr__()
        expected = "Tree('species = Oak', age = 2, circumference = 2.0)"
        self.assertEqual(expected, actual)