import pygame


WHITE = (255, 255, 255)
RED = (255, 0, 0)
PEG_SIZE = 8
BALL_SIZE = 10
space_between_pegs = 40

class Peg: 
    def __init__(self, x,y,num_rows):
        self.x = x
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.peg_positions = []  # store x and y alues of pegs
        # Generate positions for pegs
        self.generate_peg_positions()


    def generate_peg_positions(self):
         
         for row in range(2,self.num_rows + 2):
              print("row" , row)
              for pegs in range(row+1):
                print("pegs" , pegs)
                number_of_pegs = row
                x_pos = (self.x-((number_of_pegs * space_between_pegs)//2)) +(pegs*space_between_pegs)
                y_pos = self.y + (50 * number_of_pegs)
                self.peg_positions.append((x_pos, y_pos))  # Append the position to the list

    def draw_peg(self, screen):
        for position in self.peg_positions:
            pygame.draw.circle(screen, WHITE, position, PEG_SIZE)  # Draw peg at the stored position


class Ball:
    def __init__(self, x_ball, y_ball):
        self.x_ball = x_ball
        self.y_ball = y_ball
    def draw_ball(self, screen):
        pygame.draw.circle(screen, RED, (self.x_ball, self.y_ball), BALL_SIZE)


    def move_down(self):
        self.y_ball += 5 # Move down by 5 units