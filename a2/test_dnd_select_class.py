from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch("builtins.input", side_effect="1")
    def test_select_class_barbarian(self, _):
        expected = "barbarian"
        actual = dnd.select_class()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect="2")
    def test_select_class_bard(self, _):
        expected = "bard"
        actual = dnd.select_class()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect="3")
    def test_select_class_cleric(self, _):
        expected = "cleric"
        actual = dnd.select_class()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect="4")
    def test_select_class_druid(self, _):
        expected = "druid"
        actual = dnd.select_class()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect="5")
    def test_select_class_fighter(self, _):
        expected = "fighter"
        actual = dnd.select_class()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect="6")
    def test_select_class_monk(self, _):
        expected = "monk"
        actual = dnd.select_class()
        self.assertEqual(expected, actual)
