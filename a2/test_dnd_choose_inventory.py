from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch("builtins.input", side_effect=['1', '2', '2', '-1'])
    def test_choose_inventory(self, _):
        character = {"Name": "Xyxy",
                     "Strength": 10,
                     "Dexterity": 8,
                     "Intelligence": 5,
                     "Charisma": 9,
                     "Wisdom": 7,
                     "Constitution": 3,
                     "Inventory": [],
                     "XP": 0,
                     "Class": "monk",
                     "Race": "elf",
                     "HP": [7, 7]}
        dnd.choose_inventory(character)
        self.assertEqual(['Thumbtacks of blindness', 'Double edged dagger', 'Double edged dagger'],
                         character["Inventory"])
