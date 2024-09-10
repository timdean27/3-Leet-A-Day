// Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

// You must do it in place.

 

// Example 1:


// Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
// Output: [[1,0,1],[0,0,0],[1,0,1]]
// Example 2:


// Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
// Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


//first lets find the zeros [i][j]
var setZeroes = function(matrix) {
    let array_of_zeros = [];
    for(let i = 0; i < matrix.length; i++){
        
        for(let j = 0; j < matrix[i].length; j++){
            // console.log(matrix[i][j])
            if(matrix[i][j] === 0){
                array_of_zeros.push([i,j])
            }
        }
    }
    for(let i = 0; i < array_of_zeros.length; i++){
        console.log("array_of_zeros[i]",array_of_zeros[i])
        // we are setting the i part of the zero array to the row and the j part of the zero array to the column
        let [row,col] = array_of_zeros[i]
        console.log("set row and column",row,col)
        for(let i =0 ;i < matrix.length; i++){
            matrix[i][col] = 0;
        }
        // matrix[0].length is the length of the inner array(like matrix[j].length above)
        for(let i =0 ;i < matrix[0].length; i++){
            matrix[row][i] = 0;
        }
    }

    return matrix
};

console.log(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))