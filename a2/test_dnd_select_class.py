from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch("builtins.input", side_effect=["1"])
    def test_select_class_barbarian(self, _):
        expected = "barbarian"
        actual = dnd.select_class()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["7"])
    def test_select_class_paladin(self, _):
        expected = "paladin"
        actual = dnd.select_class()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["12"])
    def test_select_class_wizard(self, _):
        expected = "wizard"
        actual = dnd.select_class()
        self.assertEqual(expected, actual)
