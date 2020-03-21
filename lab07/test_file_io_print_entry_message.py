from unittest import TestCase
from unittest.mock import patch
import io
import file_io


class Test(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_entry_message(self, mock_stdout):
        file_io.print_entry_message()
        expected = "Welcome to Kyrill's word ranker!  You bank 'em we rank 'em!\n"
        self.assertEqual(expected, mock_stdout.getvalue())
