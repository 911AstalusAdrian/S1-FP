from unittest import TestCase

from board.board import Board
from strategy.strategy import Strategy


class TestStrategy(TestCase):
    def setUp(self):
        self.board = Board(6, 7)

    def test_generate_winning_move(self):
        self.assertIsNone(Strategy.generate_winning_move(self.board, 1))
        self.board.set_value(5, 0, 1)
        self.board.set_value(5, 1, 1)
        self.board.set_value(5, 2, 1)
        self.assertEqual(Strategy.generate_winning_move(self.board, 1).column, 3)

    def test_move(self):
        test_strategy = Strategy()
        self.assertIsNone(test_strategy.move(self.board, 1, 0))
