from unittest import TestCase
from unittest.mock import patch
import unittest
import io
import dnd


class Test(TestCase):
    @patch("dnd.roll_die", side_effect=[20, 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("dnd.roll_hitpoints", side_effect=[6])
    def test_single_attack_hit_and_live(self, _, mock_stdout, __):
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
        dnd.single_attack(character, sad_jim)
        expected = """Sad Jim took the hit like a real champ but still took 2 damage!

"""
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch("dnd.roll_die", side_effect=[20, 6])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("dnd.roll_hitpoints", side_effect=[6])
    def test_single_attack_hit_and_death(self, _, mock_stdout, __):
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
        dnd.single_attack(character, sad_jim)
        expected = """Xyxy hits Sad Jim for 6 damage. Sad Jim never stood a chance and now lies dead.

"""
        self.assertEqual(expected, mock_stdout.getvalue())
