from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch("dnd.generate_consonant", side_effect=["c"])
    @patch("dnd.generate_vowel", side_effect=["a"])
    def test_generate_syllable_once(self, _, __):
        expected = "ca"
        actual = dnd.generate_syllable()
        self.assertEqual(expected, actual)
