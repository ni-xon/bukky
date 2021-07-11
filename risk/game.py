import pygame
from .board import Board
from .constants import RED, WHITE

class Game:
    def __init__(self, win):
        self.selected_piece = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.win = win

    def update(self):
        self.board.draw()
        pygame.display.update()
        