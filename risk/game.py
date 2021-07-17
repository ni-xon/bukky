import pygame
from .board import Board
from .constants import *

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        """Initialises all variables and board object for a new game."""
        self.selected = False
        self.board = Board()
        self.board.create_initial_objects()
        self.current_player = 1
        self.turn_counter = 0
        self.number_of_players = 2
        self.valid_moves = {}

    def update(self):
        self.board.initial_draw(self.win)
        self.board.update_draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def reset(self):
        self._init()

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.rect(self.win, YELLOW, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
    
    def change_turn(self):
        self.turn_counter += 1
        self.current_player = (self.turn_counter % self.number_of_players) + 1

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = False
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != None and piece.id == self.current_player:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
e
        return False
        
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == None and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()

        else:
            return False

        return True

    def _attack(self, row, col):
        pass
