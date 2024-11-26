def scitani(a, b):
    if isinstance(a,str) or isinstance(b,str):
        raise ValueError("Tohle je ValueError")
    if type(a) not in (complex,float,int) or type(b) not in (complex,float,int):
        raise TypeError("Tohle je TypeError")
    else:
        return a + b
import unittest

class TestScitani(unittest.TestCase):

    def test_integer(self):
        self.assertEqual(scitani(1, 1), 2)
        self.assertEqual(scitani(-1, 1), 0)
        self.assertEqual(scitani(1, -1), 0)
        self.assertEqual(scitani(2, 3), 5)


    def test_float(self):
        self.assertEqual(scitani(0.5, -0.5),0)
        self.assertEqual(scitani(-0.5, 0.5), 0)
        self.assertEqual(scitani(1.5, 1.5), 3)


    def test_complex(self):
        self.assertEqual(scitani(3, 3j),3+3j)

    def test_bad_input(self):
        with self.assertRaises(ValueError):
            scitani("AHOJ", 100)
        with self.assertRaises(ValueError):
            scitani(100, "AHOJ")
        with self.assertRaises(TypeError):
            scitani(None, None)
        with self.assertRaises(TypeError):
            scitani([4, 5, 6], [1, 2, 3])


        if __name__ == '__main__':
            unittest.main()