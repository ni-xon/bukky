from risk.constants import SQUARE_SIZE
import pygame

class Unit:
    PADDING = 10
    OUTLINE = 2
    def __init__(self, id, color, row, col):
        self.id = id
        self.row = row
        self.col = col
        
        if self.id == 0:
            self.color = "grey"

        elif self.id == 1:
            self.color = "red"

        elif self.id == 2:
            self.color = "blue"

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

class Building:
    def __init__(self, id, color, row, col):
        self.id = id
        self.row = row
        self.col = col
        
        if self.id == 0:
            self.color = "grey"

        elif self.id == 1:
            self.color = "red"

        elif self.id == 2:
            self.color = "blue"

        else:
            raise ValueError("Enter valid id (0, 1 or 2)")

    def draw(self, win):
        length = SQUARE_SIZE
        pygame.draw.rect(win, self.color)

