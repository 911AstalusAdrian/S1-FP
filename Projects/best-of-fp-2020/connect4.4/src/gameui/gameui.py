from gameui.colors import F_YELLOW, RESET, F_RED
from utility.movevalidator import MoveValidator, MoveException
from player.human import Human
from utility.gameutility import GameCalculations


class GameUI:
    def __init__(self, board, player1, player2):
        """
        Creates an object of type GameUI
        :param board: The board on which the game will be played, an object of type Board
        :param player1: The first player, an object whose class inherits the class Player
        :param player2: The second player, an object whose class inherits the class Player
        """
        self.__board = board
        self.__player1 = player1
        self.__player2 = player2

    def play(self):
        """
        Plays the game. Call this function in order to start the game
        :return: nothing
        """
        game_done = False
        while not game_done:
            if self.__move(self.__player1, self.__player2.value):
                game_done = True
            elif self.__move(self.__player2, self.__player1.value):
                game_done = True

    def __move(self, player, enemy_value):
        """
        Does a move for a given player
        :param player: The player that has to do the move, an object whose class inherits the class Player
        :param enemy_value: The value used to represent the opposing player's pieces on the board
        :return: True if the move ended the game (i.e, the player won or a draw was reached), otherwise False
        """
        latest_move = 0
        if type(player) == Human:
            self.__draw_board()
            column_valid = False
            while not column_valid:
                try:
                    column = self.__read_data(player)
                    MoveValidator.validate(column, self.__board)
                except MoveException as me:
                    print(me)
                else:
                    column_valid = True
                    line = self.__board.get_line_first_empty_cell_in_column(column)
                    latest_move = player.move(line, column)
        else:
            latest_move = player.move(enemy_value)
        if GameCalculations.is_winner(self.__board, latest_move):
            self.__show_winner(player)
            return True
        if GameCalculations.is_board_full(self.__board):
            self.__show_draw()
            return True
        return False

    def __draw_board(self):
        """
        Prints the board on the screen
        :return: nothing
        """
        board = str(self.__board)
        board = board.replace(str(self.__player1.value), F_YELLOW + "O" + RESET)
        board = board.replace(str(self.__player2.value), F_RED + "O" + RESET)
        print(board)

    @staticmethod
    def __read_data(player):
        """
        Reads player input for the human player's move
        :param player: The player that does the move, an object of type Human
        :return: The column on which the player will place his next piece, a positive integer
        Raise MoveException if the user has not inputted an integer
        """
        column = input(player.name + ", give the column where you want to insert the next piece. "
                       "The columns are numbered starting from 1:")
        try:
            column = int(column) - 1
        except ValueError:
            raise MoveException("Invalid input! It is not an integer!")
        return column

    def __show_winner(self, player):
        """
        Shows the winning statement on the screen
        :param player: The player that won the game, an object whose class inherits the class Player
        :return: nothing
        """
        self.__draw_board()
        print(str(player.name), "won the game!")

    def __show_draw(self):
        """
        Shows the draw statement on the screen
        :return: nothing
        """
        self.__draw_board()
        print("The game ended in a draw!")
