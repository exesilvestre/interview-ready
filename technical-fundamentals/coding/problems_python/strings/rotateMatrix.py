# 7. *Rotate Matrix*:

# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place
"""
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

[1, 4., 7]
[2, 5, 8]
[3, 6, 9]

[7, 4, 1]
[8, 5, 2]
[9, 6, 3]
"""


def rotateMatrix (matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
        
    for i in range(n):
        matrix[i].reverse()
    
    return matrix