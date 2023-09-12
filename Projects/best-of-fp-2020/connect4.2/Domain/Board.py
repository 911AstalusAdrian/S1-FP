from Domain.Cell import Cell
from Domain.Connect4Exception import Connect4Exception


class BoardException(Connect4Exception):
    """
    Exception thrown at the board level
    """

    def __init__(self, msg):
        super().__init__(msg)


class Board:
    def __init__(self, height, width, pieces_to_win):
        self._board = []
        self._height = height  # the height and width of the game board
        self._width = width
        self._pieces_to_win = pieces_to_win  # the number of pieces placed in a sequence required to win

        # Initialize the board matrix with empty cells
        for row in range(self._height):
            board_row = []
            for col in range(self._width):
                board_row.append(Cell())
            self._board.append(board_row)

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def __getitem__(self, item):
        return self._board[item]

    @property
    def pieces_to_win(self):
        return self._pieces_to_win

    def is_cell_empty(self, row, col):
        """
        Returns whether a cell is empty or not
        :param row: int representing the cell's row position
        :param col: int representing the cell's column position
        :return: bool
        """

        if row < 0 or row >= self._height or col < 0 or col >= self._width:  # check if the coordinates are in bounds
            raise BoardException("Column and row out of bounds.")

        return self._board[row][col].is_empty()

    def place_piece(self, col, player_id):
        """
        Attempts to place a cell on a column
        :param col: the column on which the piece will be dropped
        :param player_id: the player id belonging to the piece
        :return: void
        """

        if col < 0 or col >= self._width:  # except invalid column coordinates
            raise BoardException("Column" + str(col) + "out of bounds.")

        if self._board[0][col].is_empty():  # check if the column isn't filled
            row = 0
            while row < self._height and self._board[row][col].is_empty():  # find the row of the first piece on the
                # column
                row += 1

            self._board[row - 1][col].value = player_id

        else:  # raise error if column is filled
            raise BoardException("Column " + str(col) + " is full, can't place piece there.")

    def remove_piece(self, col):
        """
        Attempts to remove the last cell from a column
        :param col: int representing the column from which to remove the piece
        :return: void
        """

        if col < 0 or col >= self._width:  # except invalid column coordinates
            raise BoardException("Column" + str(col) + "out of bounds.")

        if self._board[self._height - 1][col].is_filled():  # check if the column isn't empty
            for row in range(self._height):  # remove the piece from the top of the column
                if self._board[row][col].is_filled():
                    self._board[row][col].free_cell()  # free the cell
                    break
        else:
            raise BoardException("Column " + str(col) + " is empty, there's nothing to remove.")

    def get_cell_from_column(self, col):
        """
        Returns the cell at the top of a column
        :param col: int representing the column from which to return the piece
        :return: Piece instance
        """

        if col < 0 or col >= self._width:  # except invalid column coordinates
            raise BoardException("Column" + str(col) + "out of bounds.")

        if not self._board[self._height - 1][col].is_empty():  # check if the column isn't empty
            for row in range(self._height):  # remove the piece from the top of the column
                if self._board[row][col].is_filled():
                    return self._board[row][col]
        else:
            raise BoardException("Column " + str(col) + " is empty, there's nothing to return.")

    def is_full(self):
        """
        Checks if the board is full
        :return: bool
        """

        for col in range(self._width):
            if self._board[0][col].is_empty():  # if we find a column that isn't full, return False
                return False

        return True

    def won(self):
        """
        Checks if the current board state indicates a win
        :return: bool
        """

        # check for a win on the rows of the table
        for row in range(self._height):
            # look for longest sequence of identical pieces on the row
            seq = 1
            longest_seq = 1

            for col in range(1, self._width):
                if self._board[row][col].is_filled() and self._board[row][col] == self._board[row][col - 1]:
                    seq += 1  # if the piece is identical to the previous piece, increase the sequence
                    longest_seq = max(longest_seq, seq)
                else:
                    seq = 1

            if longest_seq >= self._pieces_to_win:  # if we found a winning sequence of pieces, return True
                return True

        # check for a win on the columns of the table
        for col in range(self._width):
            # look for longest sequence of identical pieces on the column
            seq = 1
            longest_seq = 1

            for row in range(1, self._height):
                if self._board[row][col].is_filled() and self._board[row][col] == self._board[row - 1][col]:
                    seq += 1  # if the piece is identical to the previous piece, increase the sequence
                    longest_seq = max(longest_seq, seq)
                else:
                    seq = 1

            if longest_seq >= self._pieces_to_win:  # if we found a winning sequence of pieces, return True
                return True

        # check for a win on the main diagonals
        for row in range(self._height - self._pieces_to_win + 1):  # starting row of the diagonal
            for col in range(self._width - self._pieces_to_win + 1):  # starting column of the diagonal
                i = 0
                seq = 1
                longest_seq = 1
                while row + i < self._height - 1 and col + i < self._width - 1:  # go down the diagonal from (row, move)
                    if self._board[row + i][col + i].is_filled() and \
                            self._board[row + i][col + i] == self._board[row + i + 1][col + i + 1]:
                        seq += 1
                        longest_seq = max(seq, longest_seq)
                    else:
                        seq = 1
                    i += 1

                if longest_seq >= self._pieces_to_win:
                    return True

        # check for a win on the secondary diagonals
        for row in range(self._pieces_to_win - 1, self._height):
            for col in range(self._width - self._pieces_to_win + 1):
                i = 0
                seq = 1
                longest_seq = 1
                while row - i > 0 and col + i < self._width - 1:
                    if self._board[row - i][col + i].is_filled() and \
                            self._board[row - i][col + i] == self._board[row - i - 1][col + i + 1]:
                        seq += 1
                        longest_seq = max(seq, longest_seq)
                    else:
                        seq = 1
                    i += 1

                if longest_seq >= self._pieces_to_win:
                    return True

        return False
