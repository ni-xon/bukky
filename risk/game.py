import pygame
from .board import Board
from .constants import *
from .objects import *

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        """Initialises all variables and board object for a new game."""
        self.selected = None
        self.board = Board()
        self.board.create_initial_objects()
        self.current_player = 1
        self.turn_counter = 0
        self.number_of_players = 2
        self.valid_moves = []

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

    def menu(self, row, col):
        # Handler for clicking change turns button
        if row == 0:
            self.change_turn()
            self.board.reset_action_points()

        return

    def select(self, row, col):
        # Handler for clicking menu
        menu = COLS
        if col == menu:
            self.menu(row, col) 
            return

        # Obtain target click
        target = self.board.get_piece(row, col)

        # If something is already selected in the previous iteration
        if self.selected != None:
            if type(self.selected) == Unit:
                if (row, col) in self.valid_moves and self.board.enough_action_points(self.selected):
                    if target == None:
                        self.board.move(self.selected, row, col)

                    elif target != None:
                        # Merge
                        if self.selected.id == target.id:
                            self.board.merge(self.selected, target)

                        # Attack
                        elif self.selected.id != target.id:
                            self.board.attack(self.selected, target)

                    self.selected.action_points -= 1

            elif type(self.selected) == Building and (row, col) in self.valid_moves:
                self.board.spawn(self.current_player, row, col)

            # This code chunk deselects
            self.selected = None
            self.valid_moves = []
            return

        # If valid select
        if target != None and target.id == self.current_player:
            self.selected = target
            self.valid_moves = self.board.get_valid_moves(target)
            return True # returns back to main

        return False # returns back to main
        