from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    def test_create_character_invalid_input(self):
        expected = None
        actual = dnd.create_character(-1)
        self.assertEqual(actual, expected)

    @patch("dnd.roll_die", side_effect=[10, 8, 5, 9, 7, 3])
    @patch("dnd.generate_name", side_effect=["xyxy"])
    @patch("dnd.select_class", side_effect=["monk"])
    @patch("dnd.select_race", side_effect=["elf"])
    @patch("dnd.roll_hitpoints", side_effect=[7])
    def test_create_character_two_syllables(self, _, __, ___, ____, _____):
        expected = {"Name": "Xyxy",
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
        actual = dnd.create_character(2)
        self.assertEqual(expected, actual)

    @patch("dnd.roll_die", side_effect=[10, 8, 5, 9, 7, 3])
    @patch("dnd.generate_name", side_effect=["Po"])
    @patch("dnd.select_class", side_effect=["monk"])
    @patch("dnd.select_race", side_effect=["elf"])
    @patch("dnd.roll_hitpoints", side_effect=[7])
    def test_create_character_one_syllable(self, _, __, ___, ____, _____):
        expected = {"Name": "Po",
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
        actual = dnd.create_character(1)
        self.assertEqual(expected, actual)
