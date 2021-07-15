import pygame
from .constants import *
from .objects import Unit, Building, Piece

class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.selected_unit = None

    def __str__(self):
        output = ""
        for row in range(ROWS):
            output += f"{self.board[row]}\n"

        return output

    def intial_draw(self, win):
        win.fill(WHITE)

        # Draw green background
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, DARK_GREEN, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        # Draw grid
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, BLACK, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

        pygame.draw.rect(win,BLACK,((COLS*SQUARE_SIZE)-1,0,SQUARE_SIZE+1,SQUARE_SIZE+1))



    def update_draw(self,win):
        pygame.init()
        number_font = pygame.font.Font( None, 16)
        # DRAW PIECES AND HEALTH
        for i in range(ROWS):
            for j in range(COLS):
                object = self.board[i][j]
                if object != None:
                    object.draw(win)
                    number_text = str(object.power)
                    number_image = number_font.render(number_text, False, WHITE)
                    win.blit(number_image, (object.x, object.y))


    def create_initial_objects(self):
        p1_base = Building(id=1, row=0, col=0, power=0)
        self.board[0][0] = p1_base

        p1_unit = Unit(id=1, row=1, col=1, power=100)
        self.board[1][1] = p1_unit
        
        p2_unit = Unit(id=1, row=1, col=2, power=100)
        self.board[1][2] = p2_unit

        p3_unit = Unit(id=2, row=1, col=3, power=150)
        self.board[1][3] = p3_unit

        p2_base = Building(id=2, row=4, col=4, power=0)
        self.board[4][4] = p2_base

    def move(self, unit, row, col):
        self.board[unit.row][unit.col], self.board[row][col] = self.board[row][col], self.board[unit.row][unit.col]
        unit.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def valid_move(self, piece, row_move, col_move):
        valid_moves = []
        valid_moves.append((piece.row + 1, piece.col))
        valid_moves.append((piece.row, piece.col + 1))
        valid_moves.append((piece.row - 1, piece.col))
        valid_moves.append((piece.row, piece.col - 1))
        
        if (row_move, col_move) in valid_moves:
            return True
        return False

    def draw_valid_move(self, win, piece):
        if type(piece) == Unit:
            # UP
            pygame.draw.rect(win, YELLOW, (piece.col*SQUARE_SIZE, (piece.row-1)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
            # DOWN
            pygame.draw.rect(win, YELLOW, (piece.col*SQUARE_SIZE, (piece.row+1)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
            # LEFT
            pygame.draw.rect(win, YELLOW, ((piece.col-1)*SQUARE_SIZE, (piece.row)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
            # RIGHT
            pygame.draw.rect(win, YELLOW, ((piece.col+1)*SQUARE_SIZE, (piece.row)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

        elif type(piece) == Building:
            radius = (SQUARE_SIZE // 2) - 40
            pygame.draw.circle(win, YELLOW, (SQUARE_SIZE * (piece.row+1) + SQUARE_SIZE // 2,SQUARE_SIZE * (piece.col) + SQUARE_SIZE // 2 ), radius, width = 1)
            pygame.draw.circle(win, YELLOW, (SQUARE_SIZE * (piece.row) + SQUARE_SIZE // 2,SQUARE_SIZE * (piece.col+1) + SQUARE_SIZE // 2 ), radius, width = 1)
            pygame.draw.circle(win, YELLOW, (SQUARE_SIZE * (piece.row-1) + SQUARE_SIZE // 2,SQUARE_SIZE * (piece.col) + SQUARE_SIZE // 2 ), radius, width = 1)
            pygame.draw.circle(win, YELLOW, (SQUARE_SIZE * (piece.row) + SQUARE_SIZE // 2,SQUARE_SIZE * (piece.col-1) + SQUARE_SIZE // 2 ), radius, width = 1)
    
        else:
            raise AttributeError

    def delete_piece(self, row, col):
        self.board[row][col] = None
    
    def attack(self, agg, vict):
        # CASE 1: If aggressor kills victim:
        if agg.power > vict.power:
            # Aggressor loses health (but stays alive)
            agg.power = agg.power - vict.power

            # Victim is killed
            self.delete_piece(vict.row, vict.col)

        # CASE 2: If victim kills aggressor:
        elif agg.power < vict.power:
            # Victim loses health (but stays alive)
            vict.power = vict.power - agg.power

            # Aggressor is killed
            self.delete_piece(agg.row, agg.col)

        # CASE 3: Double Suicide -> if agg.power == vict.power
        else:
            # Both aggressor/victim are killed
            self.delete_piece(vict.row, vict.col)
            self.delete_piece(agg.row, agg.col)

    def merge(self, merger, target):
        # Target's power gets incremented
        target.power = target.power + merger.power
    
        # Merger get's deleted
        self.delete_piece(merger.row, merger.col)

    def spawn(self, building, row, col):
        self.board[row][col] = Unit(id=building.id, row=row, col=col, power=100)

    def reset_action_points(self):
        for row in range(ROWS):
            for col in range(COLS):
                object = self.board[row][col]
                if type(object) == Unit:
                    object.action_points = object.initial_action_points

