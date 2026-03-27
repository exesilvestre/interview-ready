from typing import List, Tuple, Union

# 2. Robot in a Grid
# Imagine a robot sitting on the upper left corner of a grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are
# "off limits" such that the robot cannot step on them.
# Design an algorithm to find a path for the robot from the top left to the bottom right.

Grid = List[List[bool]]
Path = List[Tuple[int, int]]

def robot_in_a_grid(grid: Grid) -> Union[Path, bool]:
    path = []
    if moveRobot([0, 0], grid, path):
        return path
    return False


def moveRobot(position: List[int], grid, path):
    row, col = position
    rows, cols  = len(grid), len(grid[0])

    if row >= rows or col >= cols or not grid[row][col]:
        return False
    
    path.append([col, row])

    if row == rows - 1 and col == cols - 1:
        return True
    
    if moveRobot([row, col + 1], grid, path):
        return True
    if moveRobot([row + 1, col], grid, path):
        return True

    path.pop()
    return False

