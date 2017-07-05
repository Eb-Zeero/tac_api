import unittest
from tac_api.app.points.user import  *

class TestStringMethods(unittest.TestCase):

    def test_is_user_valid(self):
        self.assertEqual(True, True)
        self.assertEqual('foo'.upper(), True)
        self.assertEqual('foo'.upper(), True)
        self.assertEqual('foo'.upper(), True)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()