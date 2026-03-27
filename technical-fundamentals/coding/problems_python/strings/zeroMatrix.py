# 8. *Zero Matrix*#
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.


def zeroMatrix (matrix: list[list[int]]) ->list[list[int]]:
    if not matrix or not matrix[0]:
        return matrix
    rows = set()
    cols = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)
    
    for row in rows:
        for col in range(len(matrix[0])):
            matrix[row][col] = 0
    
    for col in cols:
        for row in range(len(matrix)):
            matrix[row][col] = 0

    return matrix
    