from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch("builtins.input", side_effect="1")
    def test_select_race_min(self, _):
        expected = "dragonborn"
        actual = dnd.select_race()
        self.assertEqual(expected, actual)