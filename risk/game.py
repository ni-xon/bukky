import pygame
from .board import Board
from .constants import *
from .objects import *
from .player import *

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        """Initialises all required variables and board object for a new game."""
        self.selected = None
        self.players = [Player() for i in range(NO_PLAYERS + 1)]
        self.board = Board()
        self.board.create_initial_objects()
        self.current_player_id = 1
        self.current_player = self.players[self.current_player_id]   # Initially points to first player object
        self.turn_counter = 0
        self.valid_moves = []
        self.players2 = [[0 for _ in range(TER_NUM+1)] for i in range(NO_PLAYERS + 1)]

    def update(self):
        """Updates board visuals to pygame window."""
        self.board.initial_draw(self.win)
        self.draw_player_territories(self.win)
        self.board.object_draw(self.win, self.current_player_id)
        self.draw_menu(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def reset(self):
        """Resets the game."""
        self._init()

    def draw_valid_moves(self, moves):
        """Draws all valid moves (tuples) for a particular piece object."""
        for move in moves:
            row, col = move
            pygame.draw.rect(self.win, PLAYER_COLOURS[self.current_player_id], (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
    
    def change_turn(self):
        """Switches to the next player's turn."""
        self.turn_counter += 1
        self.current_player_id = (self.turn_counter % NO_PLAYERS) + 1
        self.current_player = self.players[self.current_player_id]

    def menu(self, row, col):
        """Handles all menu click logic given row, col."""
        # Handler for clicking "next turn" button
        if row == 0:
            self.change_turn()
            self.board.reset_action_points()

        return

    def draw_menu(self, win):
        # Draw reset turn button with current player turn
        pygame.draw.rect(win, PLAYER_COLOURS[self.current_player_id], ((COLS*SQUARE_SIZE)-1,0,SQUARE_SIZE+1,SQUARE_SIZE+1))
        self.board.write_on_board(win, "RESET", WHITE, COLS*SQUARE_SIZE + (SQUARE_SIZE//4), (SQUARE_SIZE//2.5), (SQUARE_SIZE//4))

        left_x = COLS*SQUARE_SIZE + (SQUARE_SIZE//6)
        # Draw gold
        self.board.write_on_board(win, "GOLD:", WHITE, left_x, SQUARE_SIZE + (SQUARE_SIZE//15), (SQUARE_SIZE//4))
        self.board.write_on_board(win, self.current_player.gold, WHITE, left_x, SQUARE_SIZE + (SQUARE_SIZE//2.5), (SQUARE_SIZE//4))
        
        # Draw health and action points
        if type(self.selected) == Unit:
            self.board.write_on_board(win, "POWER:", WHITE, left_x, (SQUARE_SIZE*2) + (SQUARE_SIZE//15), (SQUARE_SIZE//4))
            self.board.write_on_board(win, self.selected.power, WHITE, left_x, (SQUARE_SIZE*2) + (SQUARE_SIZE//2.5), (SQUARE_SIZE//4))

            self.board.write_on_board(win, "ACTION:", WHITE, left_x, (SQUARE_SIZE*3) + (SQUARE_SIZE//15), (SQUARE_SIZE//4))
            self.board.write_on_board(win, self.selected.action_points, WHITE, left_x, (SQUARE_SIZE*3) + (SQUARE_SIZE//2.5), (SQUARE_SIZE//4))

        # Draw currently selected
        self.board.write_on_board(win, "SELECT:", WHITE, left_x, (SQUARE_SIZE*4) + (SQUARE_SIZE//15), (SQUARE_SIZE//4))
        self.board.write_on_board(win, repr(self.selected), WHITE, left_x, (SQUARE_SIZE*4) + (SQUARE_SIZE//2.5), (SQUARE_SIZE//4))

    def select(self, row, col):
        """Handles all logic upon any selections on the board given row, col."""
        # Handler for clicking menu
        menu = COLS
        if col == menu:
            self.menu(row, col) 
            return # returns back to main

        # Obtain target from click (can either be None or Piece)
        target = self.board.get_piece(row, col)

        # If something is already selected in the previous iteration
        if self.selected is not None:
            # If selected piece is a Unit object
            if type(self.selected) == Unit:
                if (row, col) in self.valid_moves and self.board.enough_action_points(self.selected):
                    if target is None:
                        self.board.move(self.selected, row, col)
                    elif target is not None:
                        # Merge
                        if self.selected.id == target.id:
                            self.board.merge(self.selected, target)
                        # Attack
                        elif self.selected.id != target.id:
                            self.board.attack(self.selected, target)
                    # Subtract an action point for action performed
                    self.selected.action_points -= 1

            # If selected piece is a Building object
            elif type(self.selected) == Building:
                if (row, col) in self.valid_moves and self.current_player.gold >= UNIT_COST:
                    self.board.spawn(self.current_player_id, row, col)
                    self.current_player.reduce_gold(UNIT_COST)

            # This code chunk deselects
            self.selected = None
            self.valid_moves = []
            return # returns back to main

        # If selection is valid (it is a piece that belongs to the current player)
        if target is not None and target.id == self.current_player_id:
            self.selected = target
            self.valid_moves = self.board.get_valid_moves(target)
            return True # returns back to main

        return False # returns back to main
        
    def winner(self):
        """Function that returns the winner when all bases are occupied by a single player"""
        player_ids = []
        for row in range(ROWS):
            for col in range(COLS):
                object = self.board.get_piece(row, col)
                if type(object) == Building:
                    player_ids.append(object.id)
                    
        # Get all unique player id that currently inhabit a building
        temp = list(set(player_ids))

        # If there only remains a single id, that player is the winner
        if len(temp) == 1:
            return f"The winner is player {temp[0]}!"
        else:
            return None
    
    def check_territory_ownership(self):
        territories_no_pieces = [[0 for _ in range(NO_PLAYERS+1)] for _ in range(TER_NUM+1)]
        for row in range(ROWS):
            for col in range(COLS):
                territory_no = self.board.territories[row][col]
                piece = self.board.get_piece(row, col)

                if type(piece) == Unit:
                    territories_no_pieces[territory_no][piece.id] += piece.power

        ##territories_no_pieces = [ [None, 300, 300, 300, 400], [None, 300, 600, 300, 100], ...]


        # skip first array
        for territory_numbers in range(1, len(territories_no_pieces)):
            territory = territories_no_pieces[territory_numbers]

            max_power = max(territory)
            max_counter = 0

            for power in territory:
                if power == max_power:
                    max_counter += 1

            if max_counter == 1:
                owner = territory.index(max_power)
                for each_player in range(1,len(self.players2)):
                    self.players2[each_player][territory_numbers] = 0
                
                self.players2[owner][territory_numbers] = 1

    def draw_player_territories(self, win):
        self.check_territory_ownership()
        for each_player in range(1,len(self.players2)):
            for row in range(ROWS):
                for col in range(COLS):
                    territory_no = self.board.territories[row][col]
                    if self.players2[each_player][territory_no] == 1:
                        pygame.draw.rect(win, PLAYER_LIGHTER_COLOURS[each_player], (col*SQUARE_SIZE+10, row*SQUARE_SIZE+10, SQUARE_SIZE-20, SQUARE_SIZE-20))
                    

