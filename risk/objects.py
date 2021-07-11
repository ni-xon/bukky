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

    # We need a 'board' argument, because we need to know which Board to delete from
    def delete_unit(self, board, row, col):
        board[row][col] = None

    # # EXAMPLE FUNCTION of Tim's move()
    # def move(self, piece, new_position):
        
    #     #...

    #     enemy_position = "An enemy unit's position"

    #     if new_position == enemy_position:
    #         self.attack(piece, self.get_piece(new_position))

    #     #...

    # ASSUMPTION: attack() method will ONLY be called when a unit moves onto an enemy unit
    def attack(self, board, agg, vict):
        # CASE 1: If aggressor kills victim:
        if agg.power > vict.power:
            # Aggressor loses health (but stays alive)
            agg.power = agg.power - vict.power

            # Victim is killed
            vict.delete_unit(board, vict.row, vict. col)

            # Aggressor moves to victim's position
            ## self.move(agg, victim's position)   <-- change according to Tim's move()       


        # CASE 2: If victim kills aggressor:
        elif agg.power < vict.power:
            # Victim loses health (but stays alive)
            vict.power = vict.power - agg.power

            # Aggressor is killed
            agg.delete_unit(board, agg.row, agg.col)

            # Note: victim does not have to move

        # CASE 3: Double Suicide -> if agg.power == vict.power
        else:
            # Both aggressor/victim are killed
            agg.delete_unit(board, agg.row, agg.col)
            vict.delete_unit(board, vict.row, vict. col)


