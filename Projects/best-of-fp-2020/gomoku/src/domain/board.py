from texttable import Texttable


class BoardException(Exception):
    pass


class Board:
    def __init__(self, row_size, col_size):
        """
        Initializes a new instance of the Board class
        :param row_size: the number of rows of the board
        :param col_size: the number of columns of the board
        """
        self._data = [[None for j in range(col_size)] for i in range(row_size)]
        self._row_size = row_size
        self._col_size = col_size
        self._free = row_size * col_size

    @property
    def data(self):
        return self._data

    @property
    def row_size(self):
        return self._row_size

    @property
    def col_size(self):
        return self._col_size

    @property
    def free(self):
        return self._free

    def get_square(self, row_ind, col_ind):
        """
        Returns the square from the given indices
        :param row_ind: the given row index
        :param col_ind: the given column index
        :return: the square at the given indices
        Raises a BoardException if one of the indices is out of bounds
        """
        if self.in_bounds(row_ind, col_ind) is False:
            raise BoardException("Indices out of bounds!")

        return self._data[row_ind][col_ind]

    def is_square_empty(self, row_ind, col_ind):
        """
        Checks if the square at the given indices is empty or not
        :param row_ind: the given row index
        :param col_ind: the given column index
        :return: True if the square is empty, False otherwise
        Raises a BoardException if one of the indices is out of bounds
        """
        if self.in_bounds(row_ind, col_ind) is False:
            raise BoardException("Indices out of bounds!")

        return self.get_square(row_ind, col_ind) is None

    def is_symbol(self, row_ind, col_ind, symbol):
        """
        Checks if the square at the given indices is occupied by the given symbol
        :param row_ind: the given row index
        :param col_ind: the given column index
        :param symbol: the given symbol
        :return: True if the square is occupied by the symbol, False otherwise
        Raises a BoardException if one of the indices is out of bounds or the symbol is not valid
        """
        if self.in_bounds(row_ind, col_ind) is False:
            raise BoardException("Indices out of bounds!")

        if symbol not in ['O', 'X']:
            raise BoardException("Invalid symbol!")

        return self._data[row_ind][col_ind] == 0 if symbol == 'O' else self._data[row_ind][col_ind] == 1

    def make_move(self, row_ind, col_ind, symbol):
        """
        Makes a new move at the given coordinates with the given symbol
        :type col_ind: int
        :param row_ind: the row where the move is made
        :param col_ind: the column where the move is made
        :param symbol: the symbol of the move, either X or O
        Raises a BoardException if one of the indices is out of bounds, the given square is occupied or the symbol
        is invalid
        """
        if self.in_bounds(row_ind, col_ind) is False:
            raise BoardException("Indices out of bounds!")

        if self.is_square_empty(row_ind, col_ind) is False:
            raise BoardException("Square is occupied!")

        if symbol not in ['O', 'X']:
            raise BoardException("Invalid symbol!")

        if symbol == 'O':
            self._data[row_ind][col_ind] = 0
        else:
            self._data[row_ind][col_ind] = 1

        self._free -= 1

    def delete_move(self, row_ind, col_ind):
        """
        Deletes a move made to the given square
        :param row_ind: the row index of the square
        :param col_ind: the column index of the square
        Raises a BoardException if one of the indices is out of bounds or if the square is already empty
        """
        if self.in_bounds(row_ind, col_ind) is False:
            raise BoardException("Indices out of bounds!")

        if self.is_square_empty(row_ind, col_ind) is True:
            raise BoardException("Square is not occupied!")

        self._data[row_ind][col_ind] = None
        self._free += 1

    def is_full(self):
        return self._free == 0

    def in_bounds(self, row_ind, col_ind):
        if row_ind < 0 or col_ind < 0 or row_ind >= self._row_size or col_ind >= self._col_size:
            return False
        return True

    def has_neighbours(self, row_ind, col_ind):
        """
        Checks if the given square has any occupied neighbours
        :param row_ind: the row index of the given square
        :param col_ind: the column index of the given square
        :return: True if it has neighbours, False otherwise
        """
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        for d in directions:
            i, j = row_ind + d[0], col_ind + d[1]

            if self.in_bounds(i, j) is False:
                continue

            if self.is_square_empty(i, j) is False:
                return True

        return False

    def get_available_squares(self):
        """
        Returns a list of tuples which hold the values of the indices of the squares which are empty
        :return: a list of tuples
        """
        available = []

        for i in range(self._row_size):
            for j in range(self._col_size):
                if self.is_square_empty(i, j) is True:
                    available.append((i, j))

        return available

    def __str__(self):
        """
        Returns the string representation of the board, using the custom Texttable class
        :return: string representation
        """
        table = Texttable()
        header = []

        for i in range(self._col_size):
            header.append(chr(ord('A') + i))
        header.append(' ')

        table.header(header)
        for index in range(self._row_size):
            row = []

            for el in self._data[index]:
                if el is None:
                    row.append(' ')
                elif el == -1:
                    row.append('*')
                elif el == 1:
                    row.append('X')
                elif el == 0:
                    row.append('0')
                elif el == 2:
                    row.append('-')

            row.append(str(index + 1))

            table.add_row(row)

        return table.draw()
