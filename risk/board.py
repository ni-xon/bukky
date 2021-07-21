import pygame
from .constants import *
from .objects import Unit, Building, Piece
import random


class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]

        # TERRITORY THINGS
        self.territories = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self._create_territories_good()


    def __str__(self):
        output = ""
        for row in range(ROWS):
            output += f"{self.board[row]}\n"
        return output

    def _territories_do_not_fill_the_board(self, ter_list):
        filled_in_squares = 0
        for territory in ter_list:
            filled_in_squares += len(territory)

        return filled_in_squares < (ROWS*COLS)

    def _not_beyond_the_realms(self, pos):
        # MAKE MORE EFFICENT LATER
        if (pos[0]>(ROWS-1) or pos[0]<0 or pos[1]>(ROWS-1) or pos[1]<0):
            return False

        return True
        # return not (pos[0]>(ROWS-1) or pos[0]<0 or pos[1]>(ROWS-1) or pos[1]<0)

    def _does_not_overlap(self, pos):
        return self.territories[pos[0]][pos[1]] is None

    def _create_territories(self):
        ter_list = []

        # Randomly initalise territory 'seeds'
        i = 1
        while len(ter_list) < TER_NUM:

            # Generate a random territory position
            ter_x = random.randint(1, ROWS-2)
            ter_y = random.randint(1, ROWS-2)

            # While ter_pos already exists in the -territory list-, keep generating random territory positions
            while (ter_x, ter_y) in ter_list:
                ter_x = random.randint(1, ROWS-2)
                ter_y = random.randint(1, ROWS-2)
            # INV: at the end of this while loop, ter_pos contains a territory position that is NOT in the -territory list-

            if self._does_not_overlap((ter_x, ter_y)):
                ter_list.append([(ter_x, ter_y, i)])
                self.territories[ter_x][ter_y] = i
                i += 1

        # Grow the 'seeds' until the board is full
        while self._territories_do_not_fill_the_board(ter_list):    ################### change it to return False if a None exists - for _ in row: for _ in column
            # Give each 'seed' a chance to grow
            for territory in ter_list:
                added = False
                timeout_counter = 0
                while added is False and timeout_counter < 20:
                    head = territory[random.randint(0, len(territory)-1)]
                    # Create a random movement
                    random_move = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
                    pos = (head[0]+random_move[0], head[1]+random_move[1], head[2])

                    if self._not_beyond_the_realms(pos) and self._does_not_overlap(pos):
                        territory.append(pos)
                        self.territories[pos[0]][pos[1]] = head[2]
                        added = True

                    timeout_counter += 1
        
        return ter_list
                        
    def _create_territories_good(self):
        good_counter = 0
        while good_counter != TER_NUM:     
            self.territories = [[None for _ in range(COLS)] for _ in range(ROWS)]
            ter_list = self._create_territories()   
            good_counter = 0
            for territory in ter_list:
                if not ((len(territory) > (((ROWS*COLS)//TER_NUM)+X)) or (len(territory) < (((ROWS*COLS)//TER_NUM)-X))):
                    good_counter += 1

    def _draw_territories(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, COLOUR_LIST[self.territories[row][col]-1], (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw(self, win):
        """Draws and paints the entire game onto the window."""
        win.fill(BLACK)

        # Draw territories
        self._draw_territories(win)

        # Draw grid
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, BLACK, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

        # Draw pieces and health
        for i in range(ROWS):
            for j in range(COLS):
                object = self.board[i][j]
                if object is not None:
                    object.draw(win)

        for i in range(ROWS):
            for j in range(COLS):
                object = self.board[i][j]
                if object is not None:
                    if type(object) == Building:
                        self.write_on_board(win, object.power, WHITE, object.x + (SQUARE_SIZE//4), object.y + (SQUARE_SIZE//4), (SQUARE_SIZE//3))
                    if type(object) == Unit:
                        self.write_on_board(win, object.action_points, WHITE, object.x - (SQUARE_SIZE//4), object.y - (SQUARE_SIZE//32), (SQUARE_SIZE//3))
                        self.write_on_board(win, object.power, WHITE, object.x - (SQUARE_SIZE//4), object.y - (SQUARE_SIZE//4), (SQUARE_SIZE//3))

    def write_on_board(self, win, string, colour, x, y, size):
        pygame.init()
        number_font = pygame.font.Font(None, size)
        number_text = str(string)
        number_image = number_font.render(number_text, False, colour)
        win.blit(number_image, (x, y))

    def create_initial_objects(self):
        """Creates all initial piece objects."""
        # PLAYER 1
        self.board[0][0] = Building(id=1, row=0, col=0, power=BUILDING_POWER)
        self.board[1][1] = Unit(id=1, row=1, col=1, power=UNIT_POWER)
        # PLAYER 2
        self.board[0][COLS-1] = Building(id=2, row=0, col=COLS-1, power=BUILDING_POWER)
        self.board[1][COLS-2] = Unit(id=2, row=1, col=COLS-2, power=UNIT_POWER)

        if NO_PLAYERS == 3:
            # PLAYER 3
            self.board[ROWS-1][0] = Building(id=3, row=ROWS-1, col=0, power=BUILDING_POWER)
            self.board[ROWS-2][1] = Unit(id=3, row=ROWS-2, col=1, power=UNIT_POWER)
        elif NO_PLAYERS == 4:
            # PLAYER 3
            self.board[ROWS-1][0] = Building(id=3, row=ROWS-1, col=0, power=BUILDING_POWER)
            self.board[ROWS-2][1] = Unit(id=3, row=ROWS-2, col=1, power=UNIT_POWER)
            # PLAYER 4
            self.board[ROWS-1][COLS-1] = Building(id=4, row=ROWS-1, col=COLS-1, power=BUILDING_POWER)
            self.board[ROWS-2][COLS-2] = Unit(id=4, row=ROWS-2, col=COLS-2, power=UNIT_POWER)



    def move(self, piece, row, col):
        """Moves a piece on board array."""
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        """Returns piece object located at (row, col) on board array."""
        return self.board[row][col]

    def get_valid_moves(self, piece):
        """Returns a piece's valid moves if they have enough resources."""
        # Initialise a list with all possible moves
        valid_moves = []

        pos = (piece.row+1, piece.col)
        if self._not_beyond_the_realms(pos) is True:
            valid_moves.append(pos)

        pos = (piece.row, piece.col+1)
        if self._not_beyond_the_realms(pos) is True:
            valid_moves.append(pos)

        pos = (piece.row-1, piece.col)
        if self._not_beyond_the_realms(pos) is True:
            valid_moves.append(pos)

        pos = (piece.row, piece.col-1)
        if self._not_beyond_the_realms(pos) is True:
            valid_moves.append(pos)

        # Checks if Unit has enough action points
        if type(piece) == Unit:
            if self.enough_action_points(piece) is False:
                valid_moves = []
        # Checks if theres anything in the way blocking spawn
        if type(piece) == Building:
            delete_list = []
            for (row, col) in valid_moves:
                if self.board[row][col] is not None:
                    delete_list.append((row, col))    
            valid_moves = list(set(valid_moves) - set(delete_list))
        return valid_moves

    def delete_piece(self, row, col):
        """Deletes a piece from the board."""
        self.board[row][col] = None
    
    def attack(self, agg, vict):
        """Attacks 2 piece objects of different player ids."""
        if type(vict) == Unit:
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

        elif type(vict) == Building:
            # CASE 1: If aggressor takes over building:
            if agg.power > vict.power:
                # Aggressor loses health (but stays alive)
                agg.power = agg.power - vict.power

                # Building is converted to player colour
                self.board[vict.row][vict.col] = Building(agg.id, vict.row, vict.col, 0)
                self.merge(agg, self.board[vict.row][vict.col])

            # CASE 2: If victim kills aggressor:
            elif agg.power < vict.power:
                # Victim loses health (but stays alive)
                vict.power = vict.power - agg.power

                # Aggressor is killed
                self.delete_piece(agg.row, agg.col)

            # CASE 3: Double Suicide -> if agg.power == vict.power
            else:
                # Agressor is killed and building still belongs to player
                self.delete_piece(agg.row, agg.col)
                vict.power = vict.power - agg.power

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