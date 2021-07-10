import pygame
from risk.constants import WIDTH, HEIGHT
from risk.board import Board

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('RISK')

board = Board()
board.create_initial_objects()
piece = board.get_piece(1, 1) # For testing feel free to remove

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

    print(board)
    board.delete_piece(0, 0)
    print(board)
    pygame.quit()
main()