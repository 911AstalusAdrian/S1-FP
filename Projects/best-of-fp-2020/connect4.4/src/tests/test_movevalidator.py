from unittest import TestCase

from board.board import Board
from utility.movevalidator import MoveException, MoveValidator


class TestMoveValidator(TestCase):
    def setUp(self):
        self.board = Board(6, 7)
        for line in range(6):
            self.board.set_value(line, 0, 1)

    def test_validate(self):
        self.assertRaises(MoveException, MoveValidator.validate, "a", self.board)
        self.assertRaises(MoveException, MoveValidator.validate, -1, self.board)
        self.assertRaises(MoveException, MoveValidator.validate, 0, self.board)
