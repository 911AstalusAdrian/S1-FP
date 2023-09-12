from random import randint

from board.cell import Cell
from strategy.strategy import Strategy


class RandomStrategy(Strategy):
    def move(self, board, value, enemy_value):
        """
        Does a move using the Random Strategy for the player with the value given in the "value" parameter
        First, the method verifies if the player can win in one move, in which case it does that move. If they cannot,
        the method verifies if the opposing player can win in one move, in which case it does a move that stops them
        from doing so. Lastly, if neither player can win in one move, the method does a random move.
        :param board: The board on which the game is played, an object of type Board
        :param value: The value used to represent the pieces of the player for which the method does the move
        :param enemy_value: The value used to represent the pieces of the opposing player
        :return: The new form of the Cell affected by the move, an object of type Cell
        """
        move = self.generate_winning_move(board, value)
        if move is not None:
            board.set_value(move.line, move.column, value)
            return move
        move = self.generate_winning_move(board, enemy_value)
        if move is not None:
            board.set_value(move.line, move.column, value)
            return Cell(move.line, move.column, value)
        column = randint(0, board.columns-1)
        line = board.get_line_first_empty_cell_in_column(column)
        while line is None:
            column = randint(0, board.columns-1)
            line = board.get_line_first_empty_cell_in_column(column)
        board.set_value(line, column, value)
        return Cell(line, column, value)
