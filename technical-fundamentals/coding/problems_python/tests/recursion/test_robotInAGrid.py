import unittest
from ...recursion.robotInAGrid import robot_in_a_grid 

class TestRobotInAGrid(unittest.TestCase):

    def test_3x3_grid(self):
        grid1 = [
            [True, True, False],
            [True, False, True],
            [True, True, True],
        ]
        expected_path = [
            [0, 0],
            [0, 1],
            [0, 2],
            [1, 2],
            [2, 2],
        ]
        self.assertEqual(robot_in_a_grid(grid1), expected_path)

    def test_4x4_grid(self):
        grid2 = [
            [True, True, True, False],
            [True, False, True, True],
            [True, True, False, False],
            [False, True, True, True],
        ]
        expected_path = [
            [0, 0],
            [0, 1],
            [0, 2],
            [1, 2],
            [1, 3],
            [2, 3],
            [3, 3],
        ]
        self.assertEqual(robot_in_a_grid(grid2), expected_path)

    def test_no_path(self):
        grid3 = [
            [True, False, True, False],
            [False, False, True, True],
            [True, True, True, False],
            [True, True, True, True],
        ]
        self.assertFalse(robot_in_a_grid(grid3))  # Debería devolver False


