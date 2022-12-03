import unittest
from translator import frenchToEnglish, englishToFrench



class TestFrenchToEnglish(unittest.TestCase):

    def test_null(self):
        self.assertEqual(frenchToEnglish(""), "")
    def test_bonjour(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

class TestEnglishToFrench(unittest.TestCase):

    def test_null(self):
        self.assertEqual(englishToFrench(""), "")
    def test_bonjour(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

unittest.main()