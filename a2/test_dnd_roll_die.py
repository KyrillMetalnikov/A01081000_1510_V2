from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    def test_roll_die_one_side_one_time(self):
        expected = 1
        actual = dnd.roll_die(1, 1)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[3])
    def test_roll_die_six_sides_once(self, mock_randint):
        actual = dnd.roll_die(1, 6)
        self.assertEqual(actual, 3)

    @patch("random.randint", side_effect=[3, 5])
    def test_roll_die_six_sides_twice(self, mock_randint):
        actual = dnd.roll_die(2, 6)
        self.assertEqual(actual, 8)

    @patch("random.randint", side_effect=[3, 8, 15, 12, 9, 1, 10, 8, 7, 4])
    def test_roll_die_fifteen_sides_ten_times(self, mock_randint):
        actual = dnd.roll_die(10, 15)
        self.assertEqual(actual, 77)
