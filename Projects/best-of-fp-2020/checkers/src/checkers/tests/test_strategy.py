import unittest

from checkers.board.board import Board
from checkers.tools.constants import YELLOW
from strategy.strategy import Strategy


class TestStrategy(unittest.TestCase):
    def setUp(self):
        self._board = Board()

    def test_strategy(self):
        self._board.move(self._board.get_piece(5, 0), 4, 1)
        score, new_board = Strategy.minimax(self._board, 3, YELLOW)
        self.assertEqual(new_board.get_piece(2, 7), 0)


def suite():
    testsuite = unittest.TestSuite()
    tests = unittest.TestLoader().loadTestsFromTestCase(TestStrategy)
    testsuite.addTests(tests)
    return  testsuite


