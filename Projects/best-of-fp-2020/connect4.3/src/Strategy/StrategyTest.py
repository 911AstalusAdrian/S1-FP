import unittest
from Strategy.strategy import *
from Board.board import *

class TestStrategy(unittest.TestCase):
    def test_strategy(self):
        s = Strategy()
        board=Board()
        board.move(0,'X')
        board.move(0,'X')
        b=board.get_data()
        difficulty=5
        aimove=s.MiniMaxAlphaBeta(b,difficulty,'O')
        self.assertEqual(aimove,0)
        board.move(aimove,'O')
        board.move(1, 'X')
        board.move(1, 'X')

        board.move(2, 'O')
        board.move(2, 'O')
        board.move(2, 'X')

        board.move(3, 'O')
        board.move(3, 'O')
        board.move(3, 'X')

        b1 = board.get_data()
        difficulty = 5
        aimove = s.MiniMaxAlphaBeta(b1, difficulty, 'O')
        self.assertEqual(aimove, 3)
        board.move(aimove, 'O')
        b=board.get_data()
        self.assertEqual(s.findFours(b),False)
        self.assertEqual(s.isBoardFilled(b), False)
        self.assertEqual(s.getEmptyLocations(b),30) # empty spaces
