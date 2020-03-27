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