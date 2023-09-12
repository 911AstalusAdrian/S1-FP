import unittest

from checkers.board.board import Board
from checkers.piece.piece import Piece
from checkers.tools.constants import YELLOW, PURPLE


class TestBoard(unittest.TestCase):
    def setUp(self):
        self._board = Board()

    def test_board(self):
        #create_board()
        self._board.create_board()
        board = self._board.get_board()
        self.assertEqual(board[0][0], 0)
        self.assertEqual(type(board[0][1]), type(Piece(0, 1, YELLOW)))
        self.assertEqual(type(board[7][0]), type(Piece(7, 0, PURPLE)))
        # winner()
        self.assertEqual(self._board.winner(), None)
        #move()
        piece = self._board.get_piece(5, 6)
        self._board.move(piece, 4, 5)
        self.assertEqual(type(board[4][5]), type(Piece(4, 5, PURPLE)))
        #get_valid_moves() - cross_left - cross_right
        moves = self._board.get_valid_moves(self._board.get_piece(5, 2))
        self.assertEqual(moves, {(4, 1): [], (4, 3): []})
        #remove()
        pieces = [self._board.get_piece(4, 5), self._board.get_piece(0, 1), self._board.get_piece(5, 2)]
        self._board.remove(pieces)
        self.assertEqual([self._board.get_piece(4, 5), self._board.get_piece(0, 1), self._board.get_piece(5, 2)], [0, 0, 0])
        #evaluate()
        self.assertEqual(self._board.evaluate(), 1.0)

def suite():
    testsuite = unittest.TestSuite()
    tests = unittest.TestLoader().loadTestsFromTestCase(TestBoard)
    testsuite.addTests(tests)
    return  testsuite

