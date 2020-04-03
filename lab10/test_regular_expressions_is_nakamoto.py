from unittest import TestCase
import regular_expressions


class Test(TestCase):
    def test_is_nakamoto_correct_usage(self):
        expected = True
        actual = regular_expressions.is_nakamoto("Charles Nakamoto")
        self.assertEqual(expected, actual)

    def test_is_nakamoto_invalid_first_name_non_capitalized(self):
        expected = False
        actual = regular_expressions.is_nakamoto("charles Nakamoto")
        self.assertEqual(expected, actual)

    def test_is_nakamoto_invalid_last_name_not_capitalized(self):
        expected = False
        actual = regular_expressions.is_nakamoto("Charles nakamoto")
        self.assertEqual(expected, actual)

    def test_is_nakamoto_invalid_first_name_dot(self):
        expected = False
        actual = regular_expressions.is_nakamoto("Mr. Nakamoto")
        self.assertEqual(expected, actual)

    def test_is_nakamoto_invalid_usage_gibberish_before(self):
        expected = False
        actual = regular_expressions.is_nakamoto("ffas;fjalsdkfj Charles Nakamoto")
        self.assertEqual(expected, actual)

    def test_is_nakamoto_correct_usage_gibberish_after(self):
        expected = False
        actual = regular_expressions.is_nakamoto("Charles Nakamoto asfasnosi")
        self.assertEqual(expected, actual)