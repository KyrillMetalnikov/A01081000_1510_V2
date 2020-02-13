from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch("random.choice", side_effect =["b", "o"])
    def test_generate_name_one_syllable(self, mock_rand_choice):
        expected = "bo"
        actual = dnd.generate_name(1)
        self.assertEqual(expected, actual)

    @patch("random.choice", side_effect=["b", "o", "j", "y"])
    def test_generate_name_two_syllables(self, mock_rand_choice):
        expected = "bojy"
        actual = dnd.generate_name(2)
        self.assertEqual(expected, actual)
