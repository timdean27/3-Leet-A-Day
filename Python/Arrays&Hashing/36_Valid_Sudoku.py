def is_valid_sudoku(board):
    # Function to check rows, columns, and 3 by 3 boxes for repeated numbers
    def check_for_repeats(lst):
        nums_set = set()
        for num in lst:
            if num != '.':
                nums_set.add(num)
        print("Numbers in array:", list(nums_set))
        return len(nums_set) == len(lst) - lst.count('.')

    # Check rows, columns, and 3 by 3 boxes for duplicates
    for i in range(len(board)):
        # Check rows
        print("Checking row:", board[i])
        if not check_for_repeats(board[i]):
            return False

        # Check columns
        column = [board[j][i] for j in range(len(board))]
        print("Checking column:", column)
        if not check_for_repeats(column):
            return False

        # Check 3 by 3 boxes
        if i % 3 == 0:
            for j in range(0, len(board), 3):
                box = [board[i + k][j + l] for k in range(3) for l in range(3)]
                print("Checking box:", box)
                if not check_for_repeats(box):
                    return False

    return True

# Example usage
sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(is_valid_sudoku(sudoku_board))

