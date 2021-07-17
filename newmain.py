import pygame
from risk.constants import *
from risk.board import Board
from risk.objects import *
from risk.game import *

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FRISK')

def get_position_mouse(pos):
    """Takes in a pos tuple (x, y) and returns appropriate (row, col) tuple according to board."""
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# MAIN GAME LOOP
def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        # if game.winner() != None:
        #   print(game.winner())
        #   run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Handler for mouse button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get row, col according to dimensions of board array
                pos = pygame.mouse.get_pos()
                row, col = get_position_mouse(pos)
                game.select(row, col)

        game.update()
    pygame.quit()
main()
