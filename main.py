import pygame
from risk.constants import *
from risk.board import Board
from risk.objects import *
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('RISK')

board = Board()
board.create_initial_objects()
board.intial_draw(WIN)

def get_position_mouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# MAIN GAME LOOP
def main():
    run = True
    clock = pygame.time.Clock()
    selected = False

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False

            # If click is detected
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_position_mouse(pos)

                # HANDLE MENU ROW, COL SELECTION
                if col == 5:
                    pass
                
                elif selected == False:
                    try:
                        piece = board.get_piece(row, col)
                        board.draw_valid_move(WIN, piece)
                        selected = True
                    except AttributeError:
                        pass

                elif selected == True:
                    if board.valid_move(piece, row, col) == True:
                        # If there is a Unit/Building here
                        if board.get_piece(row,col) != None:
                            if type(piece) == Unit:
                                # Checking friendly unit (merge)
                                if board.get_piece(row,col).id == piece.id:
                                    target = board.get_piece(row, col)
                                    board.merge(piece,target)

                                else:
                                    victim = board.get_piece(row, col)
                                    board.attack(piece,victim)
                        else:
                            if type(piece) == Unit:
                                board.move(piece, row, col)
                                piece.move(row, col)

                            elif type(piece) == Building:
                                board.spawn(piece, row, col)

                    board.intial_draw(WIN)
                    selected = False
                                
        # Draw the board and update pygame window screen
        board.update_draw(WIN)
        pygame.display.update()

    pygame.quit()

main()
