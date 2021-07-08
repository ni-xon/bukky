import pygame
from risk.constants import SQUARE_SIZE, WIDTH, HEIGHT
from risk.board import Board

def get_row_col_from_mouse(pos):
    x_mouse, y_mouse = pos
    row = y_mouse // SQUARE_SIZE
    col = x_mouse // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 6, 6)

        # Draw the board and update pygame window screen
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('RISK')

board = Board()
board.create_initial_objects()
main()
