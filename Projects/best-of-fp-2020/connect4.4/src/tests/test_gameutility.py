from unittest import TestCase

from board.board import Board
from board.cell import Cell
from utility.gameutility import GameCalculations


class TestGameCalculations(TestCase):
    def setUp(self):
        self.board = Board(6, 7)
        
    def test_is_winner(self):
        self.board.set_value(5, 0, 1)
        self.board.set_value(5, 1, 1)
        self.board.set_value(5, 2, 1)
        self.assertTrue(GameCalculations.is_winner(self.board, Cell(5, 3, 1)))
        self.assertFalse(GameCalculations.is_winner(self.board, Cell(5, 3, 2)))

    def test_is_board_full(self):
        self.assertFalse(GameCalculations.is_board_full(self.board))
        for line in range(6):
            for column in range(7):
                self.board.set_value(line, column, 1)
        self.assertTrue(GameCalculations.is_board_full(self.board))

