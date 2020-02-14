from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch("dnd.roll_die", side_effect=[12, 8])
    def test_roll_for_initiative_char_one_wins(self, _):
        expected = True
        actual = dnd.roll_for_initiative()
        self.assertEqual(expected, actual)

    @patch("dnd.roll_die", side_effect=[8, 12])
    def test_roll_for_initiative_char_two_wins(self, _):
        expected = False
        actual = dnd.roll_for_initiative()
        self.assertEqual(expected, actual)

    @patch("dnd.roll_die", side_effect=[8, 8, 10, 7])
    def test_roll_for_initiative_loop_then_char_one_true(self, _):
        expected = True
        actual = dnd.roll_for_initiative()
        self.assertEqual(expected, actual)
