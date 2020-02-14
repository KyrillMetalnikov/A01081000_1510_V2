from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch("dnd.roll_die", side_effect=[12])
    def test_roll_hitpoints_max_12(self, _):
        character = {"Class": "barbarian"}
        expected = 12
        actual = dnd.roll_hitpoints(character)
        self.assertEqual(expected, actual)

    @patch("dnd.roll_die", side_effect=[9])
    def test_roll_hitpoints_max_10(self, _):
        character = {"Class": "fighter"}
        expected = 9
        actual = dnd.roll_hitpoints(character)
        self.assertEqual(expected, actual)

    @patch("dnd.roll_die", side_effect=[6])
    def test_roll_hitpoints_max_8(self, _):
        character = {"Class": "rogue"}
        expected = 6
        actual = dnd.roll_hitpoints(character)
        self.assertEqual(expected, actual)
