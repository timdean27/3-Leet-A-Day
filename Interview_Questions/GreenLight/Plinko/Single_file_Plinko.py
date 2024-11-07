import time  # Import the time module
import random
# Define board size
rows, columns = 10, 16


def make_points_row(columns):
    points_row = [0] * columns  # Initialize with zeros
    mid1 = (columns - 1) // 2  # Left of the center
    mid2 = columns // 2        # Right of the center

    # Populate points symmetrically around the two central indices
    for i in range(mid1 + 1):
        if mid1 - i >= 0:
            points_row[mid1 - i] += i + 1  # Increment left side
        if mid2 + i < columns:
            points_row[mid2 + i] += i + 1  # Increment right side

    return points_row  # Return the constructed points row
points_row = make_points_row(columns)

def create_board(rows , columns):
    board = []
    for row in range(rows):
        # skip every other row we can do that by skipping even number rows
        if row % 2 == 0:
            # append an empty space for length of the columns
            board.append([' ']* columns)
            # print(" " * columns)
        else:
          # Create a row with pegs in every other column
            # peg_row = []  # Initialize an empty list for the peg row
            # for column in range(columns):
            #     if column % 2 == 0:
            #         peg_row.append('*')  # Add a peg
            #     else:
            #         peg_row.append(' ')  # Add a space
            peg_row = ['*'] * columns 
            board.append(peg_row)  # Append the constructed peg row

    # print(board)
    return board

def create_points_row(columns):
    mid = columns // 2  # Define the center column
    # Populate points symmetrically around the center
    for i in range(mid + 1):
        if (mid) - i >= 0:
            points_row[mid - i] += i+1  # Increment left side
        if (mid+1)+ i < columns:
            points_row[mid + i] += i+1  # Increment right side
    return points_row  # Return the constructed points row



# create function for ball position
def place_ball(board, initial_col):
    col = initial_col
    current_row = 0
    board[current_row][col] = 'O'
    # print_board(board)
    # Randomly choose the initial direction: -1 for left, 1 for right
    direction = random.choice([-1, 1])

    while current_row < rows:
        print_board(board)
        print(points_row)
        time.sleep(1)
        # blank out the spot the ball was
        board[current_row][col] = ' '
        # move ball down a rows
        current_row += 1

            # Check if the ball has reached the last row
        if current_row == rows:
            print(f"You landed on: {points_row[col]} points")  # Output points for final landing position
            break


        # Check if the ball is hitting a peg
        hit_left_peg = col > 0 and board[current_row][col - 1] == '*'
        hit_right_peg = col < columns - 1 and board[current_row][col + 1] == '*'

        # If the ball hits a peg, change direction
        if hit_left_peg and direction == -1:
            print("Hit a peg to the left!")  # Print message when hitting a peg
            direction = random.choice([-1, 1])  # Change direction to right
        elif hit_right_peg and direction == 1:
            print("Hit a peg to the right!")  # Print message when hitting a peg
            direction = random.choice([-1, 1])  # Change direction to left


        # Move in the current direction
        col += direction  # Adjust column based on direction
        col = max(0, min(col, columns - 1))  # Keep col within bounds
        board[current_row][col] = 'O'

  

def print_board(board):
    """Print the Plinko board."""
    for row in board:
        print("".join(row))
        

board = create_board(rows, columns)
initial_col = columns // 2
place_ball(board, initial_col)




