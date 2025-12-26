# 8. *Zero Matrix*#
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.


def zeroMatrix (matrix: list[list[int]]) ->list[list[int]]:
    rows = set()
    cols = set()

    rows_len = len(matrix)
    cols_len = len(matrix[0])

    for i in range(rows_len):
        for j in range(cols_len):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
        
    
    for r in rows:
        matrix[r] = [0] * cols_len
    
    for c in cols:
        for i in range(rows_len):
            matrix[i][c] = 0

    
    return matrix