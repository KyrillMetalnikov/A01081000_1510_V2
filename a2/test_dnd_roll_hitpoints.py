from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch("dnd.roll_die", side_effect=[12])
    def test_roll_hitpoints(self, _):
        character = {"Class": "barbarian"}
        expected = 12
        actual = dnd.roll_hitpoints(character)
        self.assertEqual(expected, actual)
