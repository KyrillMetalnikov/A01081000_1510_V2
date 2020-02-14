from unittest import TestCase
from unittest.mock import patch
import unittest
import io
import dnd


class Test(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character(self, mock_stdout):
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
        expected = """Name Xyxy
Strength 10
Dexterity 8
Intelligence 5
Charisma 9
Wisdom 7
Constitution 3
Inventory []
XP 0
Class monk
Race elf
HP [7, 7]

"""
        dnd.print_character(character)
        self.assertEqual(expected, mock_stdout.getvalue())
