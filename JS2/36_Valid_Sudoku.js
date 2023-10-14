// Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

// Each row must contain the digits 1-9 without repetition.
// Each column must contain the digits 1-9 without repetition.
// Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
// Note:

// A Sudoku board (partially filled) could be valid but is not necessarily solvable.
// Only the filled cells need to be validated according to the mentioned rules.

function isValidSudoku(board) {
    // Function to check if an array contains duplicate values
    const hasDuplicates = (arr) => {
        const set = new Set();
        for (const value of arr) {
            if (value !== '.') {
                if (set.has(value)) {
                    return true;
                }
                set.add(value);
            }
        }
        return false;
    };

    // Check rows
    for (const row of board) {
        if (hasDuplicates(row)) {
            return false;
        }
    }

    // Check columns
    for (let col = 0; col < 9; col++) {
        const column = [];
        for (let row = 0; row < 9; row++) {
            column.push(board[row][col]);
        }
        if (hasDuplicates(column)) {
            return false;
        }
    }

    // Check sub-grids
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const subGrid = [];
            for (let row = i * 3; row < i * 3 + 3; row++) {
                for (let col = j * 3; col < j * 3 + 3; col++) {
                    subGrid.push(board[row][col]);
                }
            }
            if (hasDuplicates(subGrid)) {
                return false;
            }
        }
    }

    return true;
}

// Example usage:
const sudokuBoard = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
];

console.log(isValidSudoku(sudokuBoard)); 


