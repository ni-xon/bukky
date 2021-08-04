from .constants import *

class Player:
    def __init__(self):
        self.gold = 100
        self.territories = [0 for _ in range(TER_NUM+1)]
    
    def reduce_gold(self, value):
        self.gold -= value