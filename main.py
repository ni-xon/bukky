import pygame
from risk.constants import WIDTH, HEIGHT
from risk.board import Board

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('RISK')

board = Board()

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
        
        # Visualise
        board.generate_board(WIN)
        pygame.display.update()
        print(board)
    pygame.quit()
main()