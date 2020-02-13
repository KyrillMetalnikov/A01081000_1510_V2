from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch("random.choice", side_effect=["c", "a"])
    def test_generate_syllable_once(self, mock_rand_choice):
        expected = "ca"
        actual = dnd.generate_syllable()
        self.assertEqual(expected, actual)
