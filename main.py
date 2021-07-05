import pygame
from risk.constants import SQUARE_SIZE, WIDTH, HEIGHT
from risk.board import Board

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('RISK')

def get_row_col_from_mouse(pos):
    x_mouse, y_mouse = pos
    row = y_mouse // SQUARE_SIZE
    col = x_mouse // SQUARE_SIZE
    return row, col


board = Board()
board.create_initial_objects()
piece = board.get_piece(1, 1) # For testing feel free to remove
board.move(piece, 6, 6) # For testing feel free to remove

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        # Draw the board and update pygame window screen
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()
main()