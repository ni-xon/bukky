import pygame
from .constants import ROWS, COLS, BLACK, WHITE, DARK_GREEN, SQUARE_SIZE
from .objects import Piece
from random import randint

class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.selected_unit = None

    def __str__(self):
        output = ""
        for row in range(ROWS):
            output += f"{self.board[row]}\n"

        return output

    def draw(self, win):
        win.fill(WHITE)

        # Draw green background
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, DARK_GREEN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        # Draw grid
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)


        #### ADD FUNCTIONALITY FOR DRAWING FROM BOARD ARRAY
        for i in range(ROWS):
            for j in range(COLS):
                object = self.board[i][j]
                if object != None:
                    object.draw(win)


    def create_initial_objects(self):
        p1_base = Piece(id=1, type="building", row=0, col=0)
        self.board[0][0] = p1_base

        n1_base = Piece(id=0, type="building", row=3, col=4)
        self.board[0][1] = n1_base

        p1_unit = Piece(id=1, type="unit", row=1, col=1)
        self.board[1][1] = p1_unit

        p2_base = Piece(id=2, type="building", row=7, col=7)
        self.board[7][7] = p2_base

    def generate_board(self, win):
        self.create_initial_objects()
        self.draw(win)


        


