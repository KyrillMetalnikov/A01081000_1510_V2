from unittest import TestCase
import dnd


class Test(TestCase):
    def test_generate_consonant(self):
        for _ in range(1000):
            result = dnd.generate_consonant()
            if result not in "bcdfghjklmnpqrstvwxyz":
                self.fail()
        self.defaultTestResult()
