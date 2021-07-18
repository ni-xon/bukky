import pygame
from .constants import *
from .objects import Unit, Building, Piece


class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.player_gold = [500 for i in range(NO_PLAYERS)]

    def __str__(self):
        output = ""
        for row in range(ROWS):
            output += f"{self.board[row]}\n"
        return output


    def draw(self, win):
        """Draws and paints the entire game onto the window."""
        # Draw white background
        win.fill(WHITE)

        # Draw green background
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, DARK_GREEN, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        # Draw grid
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, BLACK, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

        # Draw end turn button
        pygame.draw.rect(win, BLACK, ((COLS*SQUARE_SIZE)-1,0,SQUARE_SIZE+1,SQUARE_SIZE+1))

        # Draw pieces and health
        pygame.init()
        number_font = pygame.font.Font( None, 16)
        for i in range(ROWS):
            for j in range(COLS):
                object = self.board[i][j]
                if object != None:
                    object.draw(win)
                    number_text = str(object.power)
                    number_image = number_font.render(number_text, False, WHITE)
                    win.blit(number_image, (object.x, object.y))

    def create_initial_objects(self):
        """Creates all initial piece objects."""
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

    def move(self, piece, row, col):
        """Moves a piece on board array."""
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        """Returns piece object located at (row, col) on board array."""
        return self.board[row][col]

    def get_valid_moves(self, piece):
        """Returns a piece's valid moves if they have enough resources."""
        valid_moves = []
        valid_moves.append((piece.row + 1, piece.col))
        valid_moves.append((piece.row, piece.col + 1))
        valid_moves.append((piece.row - 1, piece.col))
        valid_moves.append((piece.row, piece.col - 1))

        if type(piece) == Unit:
            if self.enough_action_points(piece) is False:
                valid_moves = []

        if type(piece) == Building:
            if self.player_gold[piece.id - 1] <= 0:
                valid_moves = []

        return valid_moves

    def delete_piece(self, row, col):
        """Deletes a piece from the board."""
        self.board[row][col] = None
    
    def attack(self, agg, vict):
        """Attacks 2 piece objects of different player ids."""
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
        """Merges 2 piece objects of the same player id."""
        # Target's power gets incremented
        target.power = target.power + merger.power
    
        # Merger gets deleted
        self.delete_piece(merger.row, merger.col)

    def spawn(self, id, row, col):
        """Creates a new Unit object at a desired (row, col)."""
        self.board[row][col] = Unit(id=id, row=row, col=col, power=100)

    def reset_action_points(self):
        """Resets action points for all Unit objects on board."""
        for row in range(ROWS):
            for col in range(COLS):
                object = self.board[row][col]
                if type(object) == Unit:
                    object.action_points = object.initial_action_points

    def enough_action_points(self, unit):
        """Returns True if a Unit object has action points, otherwise returns False."""
        if unit.action_points > 0:
            return True

        return False