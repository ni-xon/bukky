import pygame
from risk.constants import ROWS, COLS, BLACK, WHITE, SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.selected_unit = None

    def draw_squares(self, win):
        win.fill(WHITE)

        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

    def create_board(self):
        pass
