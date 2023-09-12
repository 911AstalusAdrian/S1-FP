from unittest import TestCase

from board.board import Board
from strategy.randomstrategy import RandomStrategy


class TestRandomStrategy(TestCase):
    def setUp(self):
        self.board = Board(6, 7)
        self.strategy = RandomStrategy()

    def test_move(self):
        self.strategy.move(self.board, 1, 2)
        self.assertIn(1, [self.board._board[5][column].value for column in range(7)])
        for column in range(7):
            self.board.set_value(5, column, "O")
        self.board.set_value(5, 0, 1)
        self.board.set_value(5, 1, 1)
        self.board.set_value(5, 2, 1)
        self.strategy.move(self.board, 1, 2)
        self.assertEqual(self.board._board[5][3].value, 1)
        self.board.set_value(5, 0, 2)
        self.board.set_value(5, 1, 2)
        self.board.set_value(5, 2, 2)
        self.board.set_value(5, 3, "O")
        self.strategy.move(self.board, 1, 2)
        self.assertEqual(self.board._board[5][3].value, 1)
        for row in range(6):
            for column in range(6):
                self.board.set_value(row, column, "a")
        self.strategy.move(self.board, 1, 2)
        self.assertEqual(self.board._board[5][6].value, 1)



