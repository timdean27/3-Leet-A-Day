class Solution:
    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return
        
        #  we wll first loop through and find all zeros and store those positions in an array
        # once we have zeros we will loop back thorugh and set the rows and clumons of these zeros to zero

        arrayOfZeros = []

        for row in range(len(matrix)):
            # print(row)
            for cloumn in range(len(matrix[row])):
                print(matrix[row][cloumn])
                if matrix[row][cloumn] == 0:
                    arrayOfZeros.append([row, cloumn])


        for zero in arrayOfZeros:
            # Set the entire row to zero
            for cloumn in range(len(matrix[0])):
                matrix[zero[0]][cloumn] = 0
            # Set the entire column to zero
            for row in range(len(matrix)):
                matrix[row][zero[1]] = 0
        return matrix



# Example usage:
sol = Solution()
matrix = [[1,1,0],[1,1,1],[1,1,1]]
  # This modifies the matrix in place
print(sol.setZeroes(matrix))