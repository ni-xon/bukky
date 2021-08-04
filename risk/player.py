from .constants import *

class Player:
    def __init__(self):
        self.gold = 4
    
    def reduce_gold(self, value):
        self.gold -= value