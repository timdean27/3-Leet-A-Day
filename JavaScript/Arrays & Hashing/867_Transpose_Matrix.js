// Given a 2D integer array matrix, return the transpose of matrix.

// The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

// Example 1:

// Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
// Output: [[1,4,7],[2,5,8],[3,6,9]]

var transpose = (matrix)=> {
    let result = []
    for(let i = 0 ; i < matrix[0].length ; i++){
        result.push([])
        for (let j = 0 ; j < matrix.length ; j++){
            result[i].push(matrix[j][i])

        }
    }
return result
};

console.log(transpose([[1,2,3],[4,5,6],[7,8,9]]))