import pygame
from Peg_Ball import Peg , Ball

pygame.init()

WIDTH , HEIGHT = 400 , 600
BLACK = (0,0,0)
WHITE = (255,255,255)
num_rows = 6

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plinko Game")


#Create Pegs
peg = Peg(WIDTH // 2, 100, num_rows)  # Position it at center
ball = Ball(WIDTH //2 , HEIGHT -500)
# Main game loop
running = True


while running:
    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the pegs
    peg.draw_peg(screen)
    # Draw ball
    ball.draw_ball(screen)
    # Move the ball down
    ball.move_down()
    # Update the display
    pygame.display.flip()
    # Control the frame rate
    pygame.time.delay(100)  # Delay for 1 second
# Quit Pygame
pygame.quit()