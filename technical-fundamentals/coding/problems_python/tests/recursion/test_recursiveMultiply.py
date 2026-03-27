import unittest
from ...recursion.recursive_multiply import recursiveMultiply 

class TestRecursiveMultiply(unittest.TestCase):
    
    def test_positive_integers(self):
        # Test cases con dos enteros positivos
        self.assertEqual(recursiveMultiply(3, 4), 12)  # 3 * 4 = 12
        self.assertEqual(recursiveMultiply(5, 7), 35)  # 5 * 7 = 35
        self.assertEqual(recursiveMultiply(9, 2), 18)  # 9 * 2 = 18

        # Test cases donde uno de los números es 0
        self.assertEqual(recursiveMultiply(0, 10), 0)  # 0 * 10 = 0
        self.assertEqual(recursiveMultiply(8, 0), 0)   # 8 * 0 = 0

