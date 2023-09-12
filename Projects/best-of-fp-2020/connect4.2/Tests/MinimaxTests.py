import unittest

from Domain.Player import Player
from Strategies.MinimaxStrategy import MinimaxStrategy
from Tests.TestFileParser import TestFileParser


class MinimaxTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_minimax(self):
        file = open('Test_files/test_minimax')
        parser = TestFileParser(file)

        for args, board in parser.get_boards_from_file():
            col = int(args)

            strategy = MinimaxStrategy(board, 2)
            player1 = Player('c', 1, 'x')
            player2 = Player('c', 2, 'o')

            self.assertEqual(strategy.next_move(player1, player2), col)
