from .constants import SQUARE_SIZE, RED, BLUE, GRAY
import pygame

class Piece:
    PADDING = 10
    OUTLINE = 2
    def __init__(self, id, type, row, col):
        self.id = id
        self.row = row
        self.col = col
        self.type = type.lower()
        
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
        if self.type == "unit":
            self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
            self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

        elif self.type == "building":
            self.x = SQUARE_SIZE * self.col
            self.y = SQUARE_SIZE * self.row

    def draw(self, win):
        if self.type == "unit":
            radius = SQUARE_SIZE // 2 - self.PADDING
            pygame.draw.circle(win, self.color, (self.x, self.y), radius)

        elif self.type == "building":
            pygame.draw.rect(win, self.color, (self.x+3, self.y+3, SQUARE_SIZE-6, SQUARE_SIZE-6))

    def __repr__(self):
        if self.type == "unit":
            return "Unit " + str(self.id)

        elif self.type == "building":
            return "Building " + str(self.id)




