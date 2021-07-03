from .constants import SQUARE_SIZE, RED, BLUE, GRAY
import pygame

class Unit:
    PADDING = 20
    OUTLINE = 2
    def __init__(self, id, row, col):
        self.id = id
        self.row = row
        self.col = col
        
        if self.id == 0:
            self.color = GRAY
        elif self.id == 1:
            self.color = RED
        elif self.id == 2:
            self.color = BLUE
        else:
            raise ValueError("Enter valid id (0, 1 or 2)")

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def __repr__(self):
        return f"Unit {self.id}"

class Building:
    def __init__(self, id, row, col):
        self.id = id
        self.row = row
        self.col = col
        
        if self.id == 0:
            self.color = GRAY
        elif self.id == 1:
            self.color = RED
        elif self.id == 2:
            self.color = BLUE
        else:
            raise ValueError("Enter valid id (0, 1 or 2)")

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col
        self.y = SQUARE_SIZE * self.row

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))

    def __repr__(self):
        return f"Building {self.id}"