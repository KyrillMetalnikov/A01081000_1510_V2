from unittest import TestCase
import dnd


class Test(TestCase):
    def test_generate_vowel(self):
        for _ in range(100):
            result = dnd.generate_vowel()
            if result not in "aeiouy":
                self.fail()
        self.defaultTestResult()