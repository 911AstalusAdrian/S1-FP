import unittest

#from checkers.tools.constants import YELLOW, SQUARE_SIZE
from checkers.piece import piece
from checkers.piece.piece import Piece
from checkers.tools.constants import SQUARE_SIZE, YELLOW


class TestPiece(unittest.TestCase):
    def setUp(self):
        self._piece = Piece(0, 1, YELLOW)

    def test_piece(self):
        self._piece.x = SQUARE_SIZE * self._piece.col + SQUARE_SIZE // 2
        self._piece.y = SQUARE_SIZE * self._piece.row + SQUARE_SIZE // 2
        self.assertEqual(self._piece.row, 0)
        self.assertEqual(self._piece.col, 1)
        self.assertEqual(self._piece.color, YELLOW)
        self.assertEqual(self._piece.x, SQUARE_SIZE * 1 + SQUARE_SIZE // 2)
        self.assertEqual(self._piece.y, SQUARE_SIZE * 0 + SQUARE_SIZE // 2)
        self.assertEqual(self._piece.king, False)
        self._piece.make_king()
        self.assertEqual(self._piece.king, True)
        self._piece.move(1, 2)
        self.assertEqual((1, 2), (self._piece.row, self._piece.col))

def suite():
    testsuite = unittest.TestSuite()
    tests = unittest.TestLoader().loadTestsFromTestCase(TestPiece)
    testsuite.addTests(tests)
    return  testsuite

