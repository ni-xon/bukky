from .constants import SQUARE_SIZE, RED, BLUE, GRAY
import pygame


class Piece:
    PADDING = 10
    OUTLINE = 2
    def __init__(self, id, row, col, power):
        self.id = id
        self.row = row
        self.col = col
        self.power = power
        
        if self.id == 0:
            self.color = GRAY
        elif self.id == 1:
            self.color = RED
        elif self.id == 2:
            self.color = BLUE
        else:
            raise ValueError("Enter valid id (0, 1 or 2)")


class Building(Piece):
    def __init__(self, id, row, col, power):
        super(Building, self).__init__(id, row, col, power)
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col
        self.y = SQUARE_SIZE * self.row

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.y+3, self.x+3, SQUARE_SIZE-6, SQUARE_SIZE-6))

    def __repr__(self):
        return "Building " + str(self.id)


class Unit(Piece):
    def __init__(self, id, row, col, power):
        super(Unit, self).__init__(id, row, col, power)
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
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def __repr__(self):
        return "Unit " + str(self.id)

 

