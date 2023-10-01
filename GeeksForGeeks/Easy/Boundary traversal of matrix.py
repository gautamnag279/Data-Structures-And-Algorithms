class Solution:
    def BoundaryTraversal(self,matrix, rows, cols):
        result = []
    
        for j in range(cols):
            result.append(matrix[0][j])
    
        for i in range(1, rows):
            result.append(matrix[i][-1])
    
        if rows > 1:
            for j in range(cols - 2, -1, -1):
                result.append(matrix[-1][j])
    
        if cols > 1:
            for i in range(rows - 2, 0, -1):
                result.append(matrix[i][0])
    
        return result