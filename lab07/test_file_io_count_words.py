from unittest import TestCase
import file_io


class Test(TestCase):
    def test_count_words_text_file(self):
        actual = file_io.count_words("exceptions.py")
        expected = {'demonstrate': 1, 'proper': 1, 'exception': 1, 'protocol': 1, 'def': 3, 'heron': 6, 'number': 19,
                    'float': 3, 'find': 2, 'the': 8, 'square': 9, 'root': 9, 'of': 7, 'a': 9, 'function': 1, 'that': 2,
                    'uses': 1, 's': 1, 'theorem': 1, 'to': 1, 'param': 2, 'positive': 3, 'or': 1, 'integer': 1,
                    'precondition': 2, 'must': 4, 'be': 4, 'postcondition': 2, 'close': 3, 'estimate': 2, 'will': 1,
                    'found': 1, 'return': 7, 'as': 1, '9': 2, '3': 2, '0': 7, '5': 3, '2': 5, '345207879911715': 1,
                    'try': 1, 'if': 5, 'except': 1, 'zerodivisionerror': 1, 'print': 1, 'error': 1, 'provided': 1,
                    '1': 4, 'guess': 5, 'arbitrary': 2, 'value': 4, 'for': 3, 'formula': 1, 'in': 5, 'range': 1,
                    '1000': 1, 'amount': 1, 'runs': 1, 'get': 1, 'it': 1, 'enough': 1, 'findaneven': 3, 'input': 9,
                    'list': 11, 'first': 3, 'even': 9, 'integers': 2, 'raise': 2, 'valueerror': 2, 'does': 1, 'not': 1,
                    'contain': 2, 'an': 2, '6': 2, '8': 1, 'append': 1, 'break': 1, 'len': 1, 'main': 3, 'doctest': 1,
                    'testmod': 1, 'name': 1}
        self.assertEqual(actual, expected)
