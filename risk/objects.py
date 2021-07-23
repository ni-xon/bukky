from .constants import *
import pygame


class Piece:
    PADDING = 10
    OUTLINE = 2
    def __init__(self, id, row, col, power):
        self.id = id
        self.row = row
        self.col = col
        self.power = power
        self.colour = PLAYER_COLOURS[id]


class Building(Piece):
    def __init__(self, id, row, col, power):
        super(Building, self).__init__(id, row, col, power)
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col
        self.y = SQUARE_SIZE * self.row

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x+9, self.y+9, SQUARE_SIZE-18, SQUARE_SIZE-18))

    def __repr__(self):
        return f"P{self.id} Base"


class Unit(Piece):
    def __init__(self, id, row, col, power):
        super(Unit, self).__init__(id, row, col, power)
        self.initial_action_points = 2
        self.action_points = 2
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, self.colour, (self.x, self.y), radius)

    def __repr__(self):
        return f"P{self.id} Unit"

 

