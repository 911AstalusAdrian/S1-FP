from unittest import TestCase

from board.board import Board
from strategy.minimaxstrategy import MinimaxStrategy


class TestMinimaxStrategy(TestCase):
    def setUp(self):
        self.board = Board(6, 7)
        self.strategy = MinimaxStrategy()

    def test_score_position(self):
        self.board.set_value(5, 0, 1)
        self.board.set_value(5, 1, 1)
        self.board.set_value(5, 6, 2)
        self.board.set_value(5, 5, 2)
        self.assertEqual(self.strategy.score_position(self.board, 1, 2), 0)

    def test_evaluate_space(self):
        self.assertEqual(self.strategy.evaluate_space([1, 1, 1, 1], 1, 2, "O"), self.strategy.FOUR_IN_A_ROW_SCORE)
        self.assertEqual(self.strategy.evaluate_space([1, 1, 1, 1], 2, 1, "O"), -self.strategy.FOUR_IN_A_ROW_SCORE)
        self.assertEqual(self.strategy.evaluate_space([1, 1, 1, "O"], 1, 2, "O"), self.strategy.THREE_IN_A_ROW_SCORE)
        self.assertEqual(self.strategy.evaluate_space([1, 1, 1, "O"], 2, 1, "O"), -self.strategy.THREE_IN_A_ROW_SCORE)
        self.assertEqual(self.strategy.evaluate_space([1, 1, "O", "O"], 1, 2, "O"), self.strategy.TWO_IN_A_ROW_SCORE)
        self.assertEqual(self.strategy.evaluate_space([1, 1, "O", "O"], 2, 1, "O"), -self.strategy.TWO_IN_A_ROW_SCORE)
        self.assertEqual(self.strategy.evaluate_space([1, "O", "O", "O"], 1, 2, "O"), self.strategy.ONE_IN_A_ROW_SCORE)
        self.assertEqual(self.strategy.evaluate_space([1, "O", "O", "O"], 2, 1, "O"), -self.strategy.ONE_IN_A_ROW_SCORE)
        self.assertEqual(self.strategy.evaluate_space(["O", "O", "O", "O"], 1, 2, "O"), 0)

    def test_move(self):
        self.strategy.MINIMAX_DEPTH = 3
        self.strategy.move(self.board, 1, 2)
        self.assertEqual(self.board._board[5][3].value, 1)
        for column in range(7):
            self.board.set_value(5, column, "O")
        for column in range(2, 5):
            self.board.set_value(5, column, 2)
        self.strategy.move(self.board, 1, 2)
        self.assertEqual(self.board._board[5][1].value, 1)

    def test_minimax(self):
        minimax_return = self.strategy.minimax(self.board, 3, 1, 2)
        self.assertEqual(minimax_return[0], 3)
        self.assertEqual(minimax_return[1], 9)
        self.board.set_value(5, 2, 1)
        self.board.set_value(5, 3, 1)
        self.board.set_value(5, 4, 1)
        minimax_return = self.strategy.minimax(self.board, 3, 1, 2)
        self.assertEqual(minimax_return[0], 1)
