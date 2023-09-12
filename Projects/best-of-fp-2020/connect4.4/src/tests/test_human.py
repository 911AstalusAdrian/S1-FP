from unittest import TestCase

from board.board import Board
from player.human import Human


class TestHuman(TestCase):
    def setUp(self):
        self.board = Board(3, 3)
        self.human_player = Human("name", self.board, 1)

    def test_move(self):
        self.human_player.move(0, 0)
        self.assertEqual(self.board._board[0][0].value, 1)
