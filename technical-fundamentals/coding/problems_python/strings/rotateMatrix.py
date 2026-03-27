# 7. *Rotate Matrix*:

# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place
"""
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

[1, 4, 7]
[2, 5, 8]
[3, 6, 9]

[7, 4, 1]
[8, 5, 2]
[9, 6, 3]
"""


def rotateMatrix (matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    for row in range(n):
        for col in range(row + 1, n):
            value = matrix[row][col]
            matrix[row][col] =  matrix[col][row]
            matrix[col][row] = value
    
    for row in range(n):
        matrix[row].reverse()
    
    return matrix