class MoveException(Exception):
    def __init__(self, message):
        """
        Generates an object of type MoveException
        :param message: The message of the MoveException, a string
        """
        super().__init__(message)


class MoveValidator:

    @staticmethod
    def validate(column, board):
        """
        Checks if a move is valid on a given board
        :param column: The column on which the piece is placed
        :param board: The board on which the game is played, an object of type Board
        :return: nothing
        Raise MoveException if the move is not a valid one (i.e, the column is not an integer, it does not represent a
        column on the given board, or the column that it represents is full)
        """
        if not isinstance(column, int):
            raise MoveException("Invalid move! It is not an integer")
        if 0 > column or column > board.columns - 1:
            raise MoveException("Invalid move! It doesn't represent any column!")
        line = board.get_line_first_empty_cell_in_column(column)
        if line is None:
            raise MoveException("Invalid move! The selected column is full!")
