from domain.board import Board


class GameException(Exception):
    pass


class Game:
    def __init__(self, strategy, row_size, col_size):
        """
        Creates a new instance of the Game class
        :param strategy: the strategy to be used
        :param row_size: the number of rows of the board
        :param col_size: the number of columns of the board
        """
        self._board = Board(row_size, col_size)
        self._strategy = strategy

    @property
    def board(self):
        return self._board

    def human_move(self, row_ind, col_ind, first):
        """
        Makes a move at the given indices
        :param row_ind: the given row
        :param col_ind: the given column
        :param first: whether the human moved first or not
        :return: True if the move was a winning one, False otherwise
        """
        symbol = 'O' if first is True else 'X'

        self._board.make_move(row_ind, col_ind, symbol)

        return self.is_win(symbol)

    def computer_move(self, first):
        """
        Makes a move determined by the strategy attribute
        :param first: whether the human moved first or not
        :return: True if the move was a winning one, False otherwise, and the pair of coordinates
        """
        symbol = 'O' if first is True else 'X'

        move = self._strategy.get_next_move(self._board, first)
        self._board.make_move(*move, symbol)

        return self.is_win(symbol), move[0], move[1]

    def find_five_line(self, symbol):
        """
        Checks for a horizontal or vertical line of five with the given digit
        :param symbol: the given symbol
        :return: True if there exists, False otherwise
        """
        n = self.board.row_size

        for i in range(n):
            consecutive = [0, 0]
            for j in range(n):
                # Check horizontally
                if self.board.is_symbol(i, j, symbol) is True:
                    consecutive[0] += 1
                    if consecutive[0] == 5:
                        return True
                else:
                    consecutive[0] = 0

                # Check vertically
                if self.board.is_symbol(j, i, symbol) is True:
                    consecutive[1] += 1
                    if consecutive[1] == 5:
                        return True
                else:
                    consecutive[1] = 0

        return False

    def find_five_sec_diagonal(self, symbol):
        """
        Checks for a diagonal line parallel to the secondary diagonal of five with the given digit
        :param symbol: the given symbol
        :return: True if there exists, False otherwise
        """
        n = self._board.row_size

        for d in range(2 * n - 1):
            consecutive = 0
            size = n - abs(n - 1 - d)
            start = max(0, d - n + 1)
            for i in range(start, start + size):
                j = d - i
                if self.board.is_symbol(i, j, symbol) is True:
                    consecutive += 1
                    if consecutive == 5:
                        return True
                else:
                    consecutive = 0

        return False

    def find_five_main_diagonal(self, symbol):
        """
        Checks for a diagonal line parallel to the main diagonal of five with the given digit
        :param symbol: the given symbol
        :return: True if there exists, False otherwise
        """
        n = self._board.row_size

        for d in range(2 * n - 1):
            consecutive = 0
            size = n - abs(n - 1 - d)
            start = max(0, d - n + 1)
            diff = d - n + 1
            for i in range(start, start + size):
                j = i - diff
                if self.board.is_symbol(i, j, symbol) is True:
                    consecutive += 1
                    if consecutive == 5:
                        return True
                else:
                    consecutive = 0

        return False

    def is_win(self, symbol):
        """
        Checks whether the player with the given symbol has won
        :param: symbol
        """
        if self.find_five_line(symbol) is True or self.find_five_main_diagonal(symbol) is True \
                or self.find_five_sec_diagonal(symbol) is True:
            return True

        return False

    def is_draw(self):
        return self._board.is_full()
