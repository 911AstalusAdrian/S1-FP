import unittest

from checkers.board.board import Board
from checkers.game.game import Game
from checkers.tools.constants import YELLOW, PURPLE


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self._game = Game()

    def test_game(self):
        #winner()
        self.assertEqual(self._game.winner(), None)
        #select()
        self._game.select(5, 6)
        self.assertEqual(self._game.selected_piece, self._game.board.get_piece(5, 6))
        self._game.select(5, 5)
        self.assertEqual(self._game.selected_piece, None)
        #move()
        self._game.select(5, 6)
        self._game.select(4, 5)
        self.assertEqual(self._game.board.get_piece(5, 6), 0)
        #change_turn
        self._game.change_turn()
        self.assertEqual(self._game.turn, PURPLE)
        self._game.change_turn()
        self.assertEqual(self._game.turn, YELLOW)
        #ai_move()
        board = self._game.board
        board.move(board.get_piece(2, 1), 3, 0)
        self._game.ai_move(board)
        self.assertEqual(self._game.board.get_piece(2, 1), 0)
        self._game.reset()
        self.assertEqual((self._game.selected_piece, self._game.valid_moves),(None, {}))


def suite():
    testsuite = unittest.TestSuite()
    tests = unittest.TestLoader().loadTestsFromTestCase(TestGame)
    testsuite.addTests(tests)
    return  testsuite

