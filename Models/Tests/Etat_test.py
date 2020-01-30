import unittest
from Models.Etat import Etat

class EtatTestCase(unittest.TestCase):
    def setUp(self):
        self.a = Etat('a')
        self.b = Etat('b')

    def test_equality(self):
        self.assertNotEqual(self.a, self.b)
        self.assertEqual(self.a, Etat('a'))

    def test_modification(self):
        self.a.modifier_valeur('b')
        self.assertEqual(self.a, Etat('b'))

    def test_mauvaise_valeur(self):
        self.assertRaises(TypeError, lambda:Etat(1))