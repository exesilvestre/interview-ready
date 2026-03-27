import unittest
from ...recursion.towersOfHanoi import towersOfHanoi

class TestTowersOfHanoi(unittest.TestCase):

    def test_towers_configuration(self):
        result1 = towersOfHanoi(3)
        self.assertEqual(result1, ([], [], [3, 2, 1]))

        result2 = towersOfHanoi(4)
        self.assertEqual(result2, ([], [], [4, 3, 2, 1]))

        result3 = towersOfHanoi(5)
        self.assertEqual(result3, ([], [], [5, 4, 3, 2, 1]))



