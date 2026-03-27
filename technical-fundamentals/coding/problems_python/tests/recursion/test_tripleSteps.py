import unittest
from ...recursion.tripleSteps import tripleSteps  # Asumiendo que tu función está en tripleStep.py

class TestTripleStep(unittest.TestCase):
    def test_valid_input(self):
        # Test cases with expected counts
        self.assertEqual(tripleSteps(0), 0)  # No steps
        self.assertEqual(tripleSteps(1), 1)  # 1 step: (1)
        self.assertEqual(tripleSteps(2), 2)  # 2 steps: (1,1), (2)
        self.assertEqual(tripleSteps(3), 4)  # 3 steps: (1,1,1), (1,2), (2,1), (3)
        self.assertEqual(tripleSteps(4), 7)  # 4 steps
        self.assertEqual(tripleSteps(5), 13) # 5 steps
        # Agregar más casos si se necesitan

    def test_negative_input(self):
        # Negative input should return 0
        self.assertEqual(tripleSteps(-1), 0)
        self.assertEqual(tripleSteps(-10), 0)

