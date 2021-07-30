import pygame
from risk.constants import *
from risk.board import Board
from risk.objects import *
from risk.game import *

# Initial settings
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FRISK')

def get_position_mouse(pos):
    """Takes in a pos tuple (x, y) and returns appropriate (row, col) tuple according to board."""
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Main game loop
def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN) # Initialise game object

    while run:
        clock.tick(FPS)

        if game.winner() != None:
          print(game.winner())
          run = False

        for event in pygame.event.get():
            # Close game window when windows X button is pressed 
            if event.type == pygame.QUIT:
                run = False

            # Get row, col of click and pass onto method for handling target selected
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_position_mouse(pos)  
                game.select(row, col)
                print(game.selected)

        # Update board visuals
        game.update()
    # Quit window if run == False
    pygame.quit()
main()
