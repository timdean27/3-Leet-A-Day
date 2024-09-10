var isValidSudoku = function(board) {
    // Use to check rows, columns, and 3 by 3 boxes for repeated numbers
    let checkforRepeats = function(array) {
        let numsAry = [];
        for (let i = 0; i < array.length; i++) {
            if (array[i] !== ".") {
                numsAry.push(array[i]);
            }
        }
        // console.log("Numbers in array:", numsAry);
        // console.log("Set of numbers:", new Set(numsAry));
        return numsAry.length === new Set(numsAry).size;
    };

    // Check rows, columns, and 3 by 3 boxes for duplicates
    for (let i = 0; i < board.length; i++) {
        // Check rows
        // console.log("Checking row:", board[i]);
        if (!checkforRepeats(board[i])) {
            return false;
        }

        // Check columns
        let column = [];
        for (let j = 0; j < board.length; j++) {
            column.push(board[j][i]);
        }
        // console.log("Checking column:", column);
        if (!checkforRepeats(column)) {
            return false;
        }

        // Check 3 by 3 boxes
        if (i % 3 === 0) { console.log(i, "I")
            for (let j = 0; j < board.length; j += 3) {
        console.log(j,"J")
                let box = [];
                for (let k = 0; k < 3; k++) {
                    for (let l = 0; l < 3; l++) {
                        console.log(board[i + k][j + l])
                        box.push(board[i + k][j + l]);
                    }
                }
                console.log("Checking box:", box);
                if (!checkforRepeats(box)) {
                    return false;
                }
            }
        }
    }

    return true;
};

console.log(
    isValidSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ])
);
