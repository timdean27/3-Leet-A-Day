# Initialize an empty 3x3 board
def initialize_board():
    board = []
    for i in range(3):
        row = []  # Create an empty row
        for j in range(3):
            row.append(" ")  # Add an empty space to the row
        board.append(row)    # Add the row to the board
    return board

def print_board(board):
    for row in board:
        print(" | ".join(row))   # Print each row with vertical dividers
        print("-" * 9)           # Print a horizontal divider line between rows

# Display the initial empty board
# print_board(board)



def get_player_input(player , board):
    while True:
        # Prompt for the row and column from the player
        row = int(input(f"Player {player}, enter the row (0-2): "))
        col = int(input(f"Player {player}, enter the column (0-2): "))

        # Check if the row and column are within the valid range
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Invalid input. Please enter a row and column between 0 and 2.")
            continue  # Prompt the user again

        # Check if the chosen cell is already occupied
        if board[row][col] != " ":
            print("Cell already taken! Choose another cell.")
            continue  # Prompt the user again

        # If valid and cell is empty, return the row and column
        # player = switch_player(player)
        # print(f"Switched to player: {player}")
        return row, col

def check_for_winner(board):
    # check if rows or columns are full
    print(board , "board inside win fucntion")
    for i in range(3):
        # check rows
        if board[i][0] == board[i][1] == board[i][2] != " ":
            print (f"row {i} is full {board[i]}")
            return True  # A winner is found
        # check columns
        if board[0][i] == board[1][i] == board[2][i] != " ":
            print (f"column {i} is full {[board[0][i], board[1][i], board[2][i]]} ")
            return True

    # check for diagonals
    # there can only be across to left and across to right 
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print("diagonals match")
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        print("diagonals match")
        return True
    
    return False

def switch_player(current_player):
    return "O" if current_player == "X" else "X"

def Game():
    board = initialize_board()
    current_player = "X"
    print_board(board)


    for turn in range(9):
        print(f"Turn {turn +1} Player: {current_player}'s move")

        row , col = get_player_input(current_player , board)

        # Place the player's symbol on the board
        board[row][col] = current_player
        print_board(board)  # Print the updated board

        # Check for a winner
        if check_for_winner(board):
            print(f"Player {current_player} wins!")
            break  # Exit the loop if there's a winner

        # Switch players for the next turn
        current_player = switch_player(current_player)

Game()