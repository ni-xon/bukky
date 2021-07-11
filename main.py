import pygame
from risk.constants import *
from risk.board import Board
from risk.objects import *

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('RISK')

board = Board()
board.create_initial_objects()
board.intial_draw(WIN)

def get_position_mouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    selected = False
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_position_mouse(pos)
                
                if selected == False:
                    try:
                        piece = board.get_piece(row, col)
                        board.draw_valid_move(WIN, piece)
                        selected = True
                    except AttributeError:
                        pass
                
                elif selected == True:
                    if board.valid_move(piece, row, col) == True:
                        board.move(piece, row, col)
                        piece.move(row, col)
                        board.intial_draw(WIN)
                        selected = False

        # Draw the board and update pygame window screen
        board.update_draw(WIN)
        pygame.display.update()

    pygame.quit()
main()