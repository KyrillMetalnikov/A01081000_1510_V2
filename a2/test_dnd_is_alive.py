from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    def test_is_alive_one_hp(self):
        character = {"HP": [5, 1]}
        expected = True
        actual = dnd.is_alive(character)
        self.assertEqual(expected, actual)

    def test_is_alive_multiple_hp(self):
        character = {"HP": [5, 5]}
        expected = True
        actual = dnd.is_alive(character)
        self.assertEqual(expected, actual)
