import pygame
from .constants import *
from .objects import Unit, Building, Piece

class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.selected_unit = None

    def __str__(self):
        output = ""
        for row in range(ROWS):
            output += f"{self.board[row]}\n"

        return output

    def intial_draw(self, win):
        win.fill(WHITE)

        # Draw green background
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, DARK_GREEN, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        # Draw grid
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, BLACK, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

    def update_draw(self,win):
        #### ADD FUNCTIONALITY FOR DRAWING FROM BOARD ARRAY
        for i in range(ROWS):
            for j in range(COLS):
                object = self.board[i][j]
                if object != None:
                    object.draw(win)

    def create_initial_objects(self):
        p1_base = Building(id=1, row=0, col=0, power=0)
        self.board[0][0] = p1_base

        n1_base = Building(id=0, row=3, col=4, power=0)
        self.board[0][1] = n1_base

        p1_unit = Unit(id=1, row=1, col=1, power=100)
        self.board[1][1] = p1_unit
        
        p2_unit = Unit(id=2, row=1, col=2, power=64)
        self.board[1][2] = p2_unit

        p2_base = Building(id=2, row=7, col=7, power=0)
        self.board[7][7] = p2_base

    def move(self, unit, row, col):
        self.board[unit.row][unit.col], self.board[row][col] = self.board[row][col], self.board[unit.row][unit.col]
        unit.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def valid_move(self,piece,row_move,col_move):
        if abs((row_move + col_move) - (piece.row + piece.col)) != 1:
            return False
        return True

    def draw_valid_move(self, win, piece):
        # UP
        pygame.draw.rect(win, YELLOW, (piece.col*SQUARE_SIZE, (piece.row-1)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
        # DOWN
        pygame.draw.rect(win, YELLOW, (piece.col*SQUARE_SIZE, (piece.row+1)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
        # LEFT
        pygame.draw.rect(win, YELLOW, ((piece.col-1)*SQUARE_SIZE, (piece.row)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
        # RIGHT
        pygame.draw.rect(win, YELLOW, ((piece.col+1)*SQUARE_SIZE, (piece.row)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

    def delete_piece(self, row, col):
        self.board[row][col] = None
