def booleanMatrix(matrix):
    rows, columns = len(matrix), len(matrix[0])
    
    row_to_change = set()
    col_to_change = set()

    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 1:
                row_to_change.add(i)
                col_to_change.add(j)
    
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0 and (i in row_to_change or j in col_to_change):
                matrix[i][j] = 1
    
    return matrix

# using an array to store the row_to_change/col_to_change will give an "time exceeded" error