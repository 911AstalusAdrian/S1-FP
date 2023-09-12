from checkers.game.game import GameException
from checkers.tools.constants import ROWS, COLS, PURPLE, YELLOW


class UI:
    def __init__(self, game):
        self._game = game
        self.print_board()


    def update(self):
        self.print_board()

    def print_board(self):
        print('  ', end=' ')
        for index in range(0, 8):
            print( '\033[04m' +'\033[96m' + str(index), end=' ')
        print('\033[0m' + '')
        for row in range(ROWS):
            print('\033[96m' + str(row) + "|", end=' ')
            for col in range(COLS):
                piece = self._game.board.get_piece(row, col)
                if piece != 0:
                    if piece.color == PURPLE:
                        print('\033[95m' + "P", end=' ')
                    else:
                        print('\033[93m' + "Y", end=' ')
                else:
                    print('\033[0m' + "O", end=' ')
                if col % 8 == 7:
                    print('')


    def end_game(self, color):
        if color == YELLOW:
            print('\033[91m' + "YELLOW WINS", end=' ')
        else:
            print('\033[91m' + "PURPLE WINS", end=' ')

    def print_valid_moves(self, moves):
        for move in moves:
            print(move, end=' ')

    def get_input_source(self):
        print('')
        print("Select the piece you want to move")
        source_row = int(input("Row: "))
        source_col = int(input("Col: "))
        if self.validate_input(source_row, source_col) == False:
            raise GameException("Board index out of range!")
        return source_row, source_col

    def get_input_dest(self):
        print("Choose where you want to move")
        #self.print_valid_moves(self._game.valid_moves)
        dest_row = int(input("Row: "))
        dest_col = int(input("Col: "))
        if self.validate_input(dest_row, dest_col) == False:
            raise GameException("Board index out of range!")
        return dest_row, dest_col

    def check_valid_move(self, row, col):
        if (row, col) in self._game.valid_moves:
            return True
        return False


    def validate_input(self, row, col):
        return row > -1 and row < 8 and col > -1 and col < 8