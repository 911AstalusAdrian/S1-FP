import unittest

from checkers.tests import test_piece, test_board, test_game, test_strategy

suite = unittest.TestSuite([test_piece.suite(), test_board.suite(), test_game.suite(), test_strategy.suite()])

def roll():
    unittest.TextTestRunner(verbosity=2).run(suite)
