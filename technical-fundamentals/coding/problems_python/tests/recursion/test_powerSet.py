import unittest
from typing import List

from ...recursion.powerSet import powerSet

def sorted_power_set(ps: List[List[int]]) -> List[List[int]]:
    # Ordena los elementos dentro de cada subconjunto y luego ordena la lista de subconjuntos
    return sorted([sorted(subset) for subset in ps])

class TestPowerSet(unittest.TestCase):
    
    def test_power_set_123(self):
        set1 = [1, 2, 3]
        expected_power_set1 = [
            [], [1], [1, 2], [1, 2, 3], [1, 3],
            [2], [2, 3], [3]
        ]
        self.assertEqual(sorted_power_set(powerSet(set1)), sorted_power_set(expected_power_set1))
        
        set2 = []
        expected_power_set2 = [[]]
        self.assertEqual(sorted_power_set(powerSet(set2)), sorted_power_set(expected_power_set2))
    
    def test_power_set_1234(self):
        set1 = [1, 2, 3, 4]
        expected_power_set1 = [
            [1], [1, 4], [1, 3, 4], [1, 3], [1, 2, 3], [1, 2, 3, 4],
            [1, 2, 4], [1, 2], [2], [2, 4], [2, 3, 4], [2, 3],
            [3], [3, 4], [4], []
        ]
        self.assertEqual(sorted_power_set(powerSet(set1)), sorted_power_set(expected_power_set1))