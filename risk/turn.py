import pygame
from .board import Board
from .constants import *

class Turn:
    def __init__(self):
        self.current_player = 1
        self.turn_counter = 0
        self.number_of_players = 2

    def change_turn(self):
        self.turn_counter += 1
        self.current_player = (self.turn_counter % self.number_of_players) + 1
        
        