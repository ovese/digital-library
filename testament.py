import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
            
    def test_capitalize(self):
        my_str = "rododendron"
        # print(my_str.capitalize())
        self.assertEqual(my_str.capitalize(), "Rododendron")

    def test_add_two_numbers(self):
        a=3
        b=4
        self.assertEqual(str(a+b), str(7))
        
    def test_equivalence(self):
        a=3
        b=4
        self.assertTrue(a+b, 7)

if __name__ == '__main__':
    unittest.main()