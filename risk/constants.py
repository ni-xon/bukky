import pygame
import random

WIDTH, HEIGHT = 600, 500
ROWS, COLS = 10, 10
SQUARE_SIZE = HEIGHT // COLS

# RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
DARK_GREEN = (3, 125, 80)

#
NO_PLAYERS = 2


# Territory Constants
TER_NUM = ROWS      # "How to calc #Territories" can be changed later with team

COLOUR_LIST = []
for _ in range(TER_NUM):
    COLOUR_LIST.append(tuple(random.choices(range(256), k=3)))

