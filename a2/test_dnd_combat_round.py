from unittest import TestCase
from unittest.mock import patch
import dnd
import unittest
import io


class Test(TestCase):
    @patch("roll_for_initiative", side_effect=[True])
    @patch()
    def test_combat_round(self, _):
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