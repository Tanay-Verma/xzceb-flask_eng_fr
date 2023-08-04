import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def testEnglishToFrench(self):
        self.assertEqual(english_to_french("Hello"), 'Bonjour')
        


class TestFrenchToEnglish(unittest.TestCase):
    def testFrenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"), 'Hello')

unittest.main()

