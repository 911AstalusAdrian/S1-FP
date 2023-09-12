from Board.board import Board
from Strategy.strategy import *


class Game:
    def __init__(self):
        self._board = Board()

    @property
    def board(self):
        return self._board

    def human_move(self, row):
        """
        Makes a move with the symbol X
        :param row:
        :return:
        """

        return self._board.move(row, 'X')

    def computer_move(self, difficulty):
        """
        Makes a move that depends on the difficulty of the game
        :param difficulty:
        :return:
        """
        b = self._board.get_data()
        s=Strategy()
        aiMove = s.MiniMaxAlphaBeta(b, difficulty, 'O')

        return self._board.move(aiMove, 'O')
