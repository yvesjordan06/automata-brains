import unittest
from Models.Alphabet import Alphabet

class AlphabetTestCase(unittest.TestCase):
    def setUp(self):
        self.a = Alphabet(['a','b'])


    def test_verification(self):
        self.assertTrue('b' in self.a)
        self.assertFalse('c' in self.a)

    def test_insertion(self):
        self.a.ajouter_symbole('c')
        self.assertTrue('c' in self.a)

    def test_supression(self):
        self.a.supprime_symbole('a')
        self.assertFalse('a' in self.a)