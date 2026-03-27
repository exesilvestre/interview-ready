import unittest
from typing import Optional, List

from ...recursion.magicIndex import find_magic_index_distinct, find_magic_index_non_distinct

class TestMagicIndex(unittest.TestCase):

    def test_distinct(self):
        # Magic index existe
        self.assertEqual(find_magic_index_distinct([-2, -1, 0, 2, 4, 6, 8]), 4)
        # No hay magic index
        self.assertIsNone(find_magic_index_distinct([-3, -2, -1, 4, 5, 7, 9]))

    def test_non_distinct(self):
        # Magic index existe
        self.assertEqual(
            find_magic_index_non_distinct([-10, -5, 2, 2, 2, 2, 4, 7, 9, 12, 13]),
            2
        )
        # No hay magic index
        self.assertIsNone(
            find_magic_index_non_distinct([-10, -5, 0, 2, 5, 7, 9, 12, 13])
        )