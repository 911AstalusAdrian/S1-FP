class Connect4:
    def __init__(self, board, strategy, player1, player2):
        self._board = board  # the game board
        self._strategy = strategy  # the strategy used by the game
        self._player1 = player1  # the players
        self._player2 = player2
        self._current_player = 0  # int representing the current player (0 - p1, 1 - p2)

    def get_board(self):
        """ Return the board instance """
        return self._board

    def stalemate(self):
        """ Check if a stalemate occurred """
        return self._board.is_full()

    def won(self):
        """ Check if a win occurred """
        return self._board.won()

    def get_current_player(self):
        """ Return the current player instance """
        if self._current_player == 0:
            return self._player1
        else:
            return self._player2

    def get_current_opponent(self):
        """ Return the current opponent player instance """
        if self._current_player == 0:
            return self._player2
        else:
            return self._player1

    def next_human_move(self, move):
        """
        Performs the next human move
        :param move: the column on which the human chose to drop the piece
        :return: void
        """
        self._board.place_piece(move, self.get_current_player().id)
        self._current_player = (self._current_player + 1) % 2  # switch the current player

    def next_computer_move(self):
        """ Performs the next computer move """
        move = self._strategy.next_move(self.get_current_player(), self.get_current_opponent())
        self._board.place_piece(move, self.get_current_player().id)
        self._current_player = (self._current_player + 1) % 2  # switch the current player
