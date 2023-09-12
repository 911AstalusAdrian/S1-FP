from copy import deepcopy

from board.cell import Cell


class Board:
    def __init__(self, lines, columns, empty_value="O", board_state=None):
        """
        Creates an object of type Board
        :param lines: The number of lines of the board, a positive integer
        :param columns: The number of columns of the board, a positive integer
        :param empty_value: The value that will represent an empty cell of the board
        """
        self.__lines = lines
        self.__columns = columns
        self.__empty_value = empty_value

        if board_state is None:
            self._board = self.__create_board()
        else:
            self._board = board_state

    @property
    def columns(self):
        """
        Returns the number of columns for a given board
        :return: The number of columns of the board
        """
        return self.__columns

    @property
    def lines(self):
        """
        Returns the number of lines for a given board
        :return: The number of lines of the board
        """
        return self.__lines

    @property
    def empty_value(self):
        """
        Returns the value that represents an empty cell on the board
        :return: The value that represents an empty cell on the board
        """
        return self.__empty_value

    def get_board(self):
        """
        Returns a copy of the current board
        :return: A copy of the current board, a list of lists of objects of type Cell
        """
        return deepcopy(self._board)

    def set_value(self, line, column, value):
        """
        Changes the value of a given cell on the board
        :param line: The line on which the cell is located, a positive integer
        :param column: The column on which the cell is located, a positive integer
        :param value: The new value of the cell
        :return: nothing
        """
        self._board[line][column].value = value

    def get_line_first_empty_cell_in_column(self, column):
        """
        Returns the first line which has an empty cell on a given column, or None if no such line exists. The search is
        done from the bottom of the matrix to the top, due to the nature of the game.
        :param column: The column for which the first empty cell needs to be found, a positive integer
        :return: An integer representing the line on which the first empty cell was found, if one exists, otherwise None
        """
        for line in range(self.__lines - 1, -1, -1):
            if self._board[line][column].value == self.__empty_value:
                return line
        return None

    def count_connected_pieces_to_cell_on_column(self, cell):
        """
        Counts the number of cells that are connected with the given cell on the column and have the same value
        :param cell: The cell for which the number of connected cells is counted, an object of type Cell
        :return: An integer representing the number of cells connected to the given cell on its column with the same
        value as the given cell, including it.
        """
        count = 1
        position_line = cell.line - 1
        while position_line > -1 and self._board[position_line][cell.column].value == cell.value:
            position_line -= 1
            count += 1
        position_line = cell.line + 1
        while position_line < self.__lines and self._board[position_line][cell.column].value == cell.value:
            position_line += 1
            count += 1
        return count

    def count_connected_pieces_to_cell_on_line(self, cell):
        """
        Counts the number of cells that are connected with the given cell on the line and have the same value
        :param cell: The cell for which the number of connected cells is counted, an object of type Cell
        :return: An integer representing the number of cells connected to the given cell on its line with the same value
        as the given cell, including it.
        """
        count = 1
        position_column = cell.column - 1
        while position_column > -1 and self._board[cell.line][position_column].value == cell.value:
            position_column -= 1
            count += 1
        position_column = cell.column + 1
        while position_column < self.__columns and self._board[cell.line][position_column].value == cell.value:
            position_column += 1
            count += 1
        return count

    def count_connected_pieces_to_cell_on_principal_diagonal(self, cell):
        """
        Counts the number of cells that are connected with the given cell on the principal diagonal (NW -> SE) and have
        the same value
        :param cell: The cell for which the number of connected cells is counted, an object of type Cell
        :return: An integer representing the number of cells connected to the given cell on its principal diagonal with
        the same value as the given cell, including it.
        """
        count = 1
        position_line = cell.line - 1
        position_column = cell.column - 1
        while position_line > -1 and position_column > -1 and \
                self._board[position_line][position_column].value == cell.value:
            position_column -= 1
            position_line -= 1
            count += 1
        position_line = cell.line + 1
        position_column = cell.column + 1
        while position_line < self.__lines and position_column < self.__columns and \
                self._board[position_line][position_column].value == cell.value:
            position_column += 1
            position_line += 1
            count += 1
        return count

    def count_connected_pieces_to_cell_on_secondary_diagonal(self, cell):
        """
        Counts the number of cells that are connected with the given cell on the secondary diagonal (NE -> SW) and have
        the same value
        :param cell: The cell for which the number of connected cells is counted, an object of type Cell
        :return: An integer representing the number of cells connected to the given cell on its secondary diagonal with
        the same value as the given cell, including it.
        """
        count = 1
        position_line = cell.line - 1
        position_column = cell.column + 1
        while position_line > -1 and position_column < self.__columns and \
                self._board[position_line][position_column].value == cell.value:
            position_column += 1
            position_line -= 1
            count += 1
        position_line = cell.line + 1
        position_column = cell.column - 1
        while position_line < self.__lines and position_column > -1 and \
                self._board[position_line][position_column].value == cell.value:
            position_column -= 1
            position_line += 1
            count += 1
        return count

    def __copy__(self):
        return Board(self.__lines, self.__columns, self.__empty_value, deepcopy(self._board))

    def __create_board(self):
        """
        Creates a matrix with self.__lines lines and self.__columns columns filled with objects of type Cell with the
        values equal to self.__empty_value, representing the initial game board
        :return: The created matrix, a list of lists of objects of type Cell
        """
        return [[Cell(line, column, self.__empty_value) for column in range(self.__columns)]
                for line in range(self.__lines)]

    def __str__(self):
        """
        Represents the board as a string
        :return: The string form of the board
        """
        res = "-" * (self.__columns * 2 + 1) + "\n"
        for line in range(self.__lines):
            s = "|" + "|".join([str(self._board[line][column].value) for column in range(self.__columns)]) + "|\n"
            res += s + "-" * (self.__columns * 2 + 1) + "\n"
        return res
