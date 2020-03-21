from unittest import TestCase
from unittest.mock import patch
import file_io


class Test(TestCase):
    @patch("builtins.input", side_effect=["moby_dick.txt"])
    def test_get_user_input_proper_use(self, _):
        expected = "moby_dick.txt"
        actual = file_io.get_user_input()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["    moby_dick.txt  "])
    def test_get_user_input_with_white_space(self, _):
        expected = "moby_dick.txt"
        actual = file_io.get_user_input()
        self.assertEqual(expected, actual)