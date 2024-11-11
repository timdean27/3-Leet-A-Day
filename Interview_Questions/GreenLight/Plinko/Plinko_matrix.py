rows , columns = 3 ,3
board = []
def createboard(rows , columns):
    right_left = "L"
    gap_peg = True
    for row in range(rows):
        inner_board = []
        for column in range(columns):
            if gap_peg:
                if right_left == "R":
                    inner_board.append("L")
                    right_left = "L"
                    gap_peg = False
                elif right_left == "L":
                    inner_board.append("R")
                    right_left = "R"
                    gap_peg = False
            else:
                inner_board.append("_")
                gap_peg = True

        board.append(inner_board)
    return board

board = createboard(rows , columns)

def print_board(board):
    """Print the Plinko board."""
    for row in board:
        print("".join(row))
        

print_board(board)

