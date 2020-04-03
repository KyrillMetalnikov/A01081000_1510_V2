from unittest import TestCase
import regular_expressions


class Test(TestCase):
    def test_is_email_valid_letters_only(self):
        actual = regular_expressions.is_email("Kyrill@hotmail.com")
        expected = True
        self.assertEqual(actual, expected)
