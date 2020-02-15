from unittest import TestCase
from unittest.mock import patch
import dnd
import unittest
import io


class Test(TestCase):
    @patch("dnd.roll_for_initiative", side_effect=[True])
    @patch('dnd.roll_die', side_effect=[20, 6])
    @patch('dnd.roll_hitpoints', side_effect=[6])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round(self, mock_sysout, _, __, ___):
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
        sad_jim = {
            "Name": "Sad Jim",
            "Strength": 7,
            "Dexterity": 8,
            "Intelligence": 5,
            "Charisma": 0,  # I'm aware this is impossible by normal means, but sad jim is just awful.
            "Wisdom": 11,
            "Constitution": 3,
            "Inventory": [],
            "XP": 0,
            "Class": "loser",
            "Race": "human",
            "HP": [3, 3]
        }
        expected = """Xyxy hits Sad Jim for 6 damage. Sad Jim never stood a chance and now lies dead.

"""
        dnd.combat_round(character, sad_jim)
        self.assertEqual(expected, mock_sysout.getvalue())
