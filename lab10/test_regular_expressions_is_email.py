from unittest import TestCase
import regular_expressions


class Test(TestCase):
    def test_is_email_valid_letters_only(self):
        actual = regular_expressions.is_email("Kyrill@hotmail.com")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_email_valid_numbers_only(self):
        actual = regular_expressions.is_email("5432@3553.com")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_email_valid_letters_numbers_underscores(self):
        actual = regular_expressions.is_email("xX_420N008Sn1p3R_Xx@9gag.ca")
        expected = True
        self.assertEqual(actual, expected)

    def test_is_email_invalid_no_dot(self):
        actual = regular_expressions.is_email("xX_420N008Sn1p3R_Xx@9gagca")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_invalid_no_at_symbol(self):
        actual = regular_expressions.is_email("xX_420N008Sn1p3R_Xx9gag.ca")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_invalid_two_dots(self):
        actual = regular_expressions.is_email("xX_420N008Sn1p3R_Xx@9.gag..ca")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_invalid_two_at_symbols(self):
        actual = regular_expressions.is_email("xX_420N008Sn1p3R_Xx@bcit@bcit.ca")
        expected = False
        self.assertEqual(actual, expected)

    def test_is_email_invalid_dashes_in_domain(self):
        actual = regular_expressions.is_email("xX_420N008Sn1p3R_Xx@9_gag.ca")
        expected = False
        self.assertEqual(actual, expected)
