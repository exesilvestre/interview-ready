import unittest
from ...recursion.coinChange import change  

class TestCoinChange(unittest.TestCase):

    def test_invalid_or_no_match(self):
        self.assertEqual(change(10, [15]), 0)
        self.assertEqual(change(10, []), 0)
        self.assertEqual(change(10, [7]), 0)

    def test_valid_examples(self):
        self.assertEqual(change(5, [1, 2, 5]), 4)
        self.assertEqual(change(10, [10]), 1)


