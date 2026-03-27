import unittest
from ...recursion.permutationWithDups import permutationsWithDups, permutationsWithoutDups

class TestPermutationsWithoutDups(unittest.TestCase):

    def test_permutations_without_dups(self):
        # Test case with a string of length 3
        result1 = permutationsWithoutDups("abc")
        expected = ["abc", "acb", "bac", "bca", "cab", "cba"]
        
        for p in expected:
            self.assertIn(p, result1)


class TestPermutationsWithDups(unittest.TestCase):

    def test_permutations_with_dups(self):
        # Test case with duplicate characters "aab"
        result1 = permutationsWithDups("aab")
        expected1 = ["aab", "aba", "baa"]

        for p in expected1:
            self.assertIn(p, result1)

        # Test case with duplicate characters "aabb"
        result2 = permutationsWithDups("aabb")
        expected2 = ["aabb", "abab", "abba", "baab", "baba", "bbaa"]

        for p in expected2:
            self.assertIn(p, result2)

