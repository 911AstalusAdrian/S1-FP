from unittest import TestCase

from board.board import Board
from player.computer import Computer
from strategy.randomstrategy import RandomStrategy


class TestComputer(TestCase):
    def setUp(self):
        self.board = Board(6, 7)
        self.computer_player = Computer("computer", self.board, 1, RandomStrategy())

    def test_move(self):
        self.computer_player.move(2)
        self.assertIn(1, [self.board._board[5][column].value for column in range(7)])
