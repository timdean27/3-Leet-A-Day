class Solution:
    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return
        
        # Get matrix dimensions
        rows, cols = len(matrix), len(matrix[0])
        
        # Flags to determine if first row or first column should be zero
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Use first row and column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out cells based on markers in the first row and column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle the first row
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Handle the first column
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0

# Example usage:
sol = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(matrix)  # This modifies the matrix in place
print(matrix)  # Print the modified matrix
