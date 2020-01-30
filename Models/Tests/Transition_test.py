import unittest
from Models.Transition import Transition, Etat

class AlphabetTestCase(unittest.TestCase):
    def setUp(self):
        self.a = Etat('a')
        self.b = Etat('b')
        self.t = Transition(self.a,'',self.b);


    def test_verification(self):
        self.assertEqual(self.t, Transition(self.a,'€',self.b))
        self.assertEqual(self.t, Transition(self.a,'',self.b))
        self.assertNotEqual(self.t, Transition(self.a,'e',self.b))
        self.assertNotEqual(Transition(self.b,'e',self.a), Transition(self.a,'e',self.b))
        self.assertEqual(Transition(self.b,'e',self.a), Transition(self.b,'e',self.a))
    def test_epsilon(self):
        self.assertTrue(self.t.est_epsilon())
        self.assertTrue(Transition(self.a,'€',self.b))
        self.t.changer_symbole('e')
        self.assertFalse(self.t.est_epsilon())
