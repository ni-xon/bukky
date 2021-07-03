import pygame
from .constants import ROWS, COLS, BLACK, WHITE, SQUARE_SIZE
from .objects import Building, Unit

class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.selected_unit = None

    def draw(self, win):
        win.fill(WHITE)

        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

    def create_objects(self, win):
        p1_base = Building(1, 0, 0)
        self.board[0][0] = p1_base
        p1_base.draw(win)

        p1_unit = Unit(1, 1, 1)
        self.board[1][1] = p1_unit
        p1_unit.draw(win)

        p2_base = Building(2, 7, 7)
        self.board[7][7] = p2_base
        p2_base.draw(win)

    def generate_board(self, win):
        self.draw(win)
        self.create_objects(win)


