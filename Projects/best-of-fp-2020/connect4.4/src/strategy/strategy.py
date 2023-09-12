from abc import abstractmethod

from board.cell import Cell
from utility.gameutility import GameCalculations


class Strategy:
    @abstractmethod
    def move(self, board, value, enemy_value):
        pass

    @staticmethod
    def generate_winning_move(board, value):
        """
        Generates a move that wins the game for the player with the value given in the "value" parameter
        :param board: The board on which the game is played, an object of type Board
        :param value: The value used to represent the pieces of the player for which the winning move is generated
        :return: An object of type Cell representing the cell that must be changed so that the player wins the game, if
        such a move is possible, otherwise None
        """
        for column in range(board.columns):
            line = board.get_line_first_empty_cell_in_column(column)
            if line is not None:
                moved_cell = Cell(line, column, value)
                if GameCalculations.is_winner(board, moved_cell):
                    return moved_cell
        return None