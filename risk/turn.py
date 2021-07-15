import pygame
from .board import Board
from .constants import RED, WHITE, NO_PLAYERS

class Turn:
    def __init__(self):
        self.current_player = 1
        self.turn_counter = 1
        self.number_of_players = NO_PLAYERS

    def change_turn(self):
        self.turn_counter += 1
        self.current_player = self.turn_counter % self.number_of_players
        
        