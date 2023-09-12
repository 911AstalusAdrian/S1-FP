import unittest
from Game.game import *


class TestGame(unittest.TestCase):
    def test_game(self):
        g = Game()
        self.assertEqual(g.board.get_data(), [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                              [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                              [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        g.human_move(1)
        #print(g.board)
        self.assertEqual(g.board.get_data(), [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                              [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                              [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'X', ' ', ' ', ' ', ' ', ' ']])
        g.human_move(1)
        g.human_move(1)
        g.computer_move(5)  # this should put a O over the 3 X's
        self.assertEqual(g.board.get_data(), [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                              [' ', 'O', ' ', ' ', ' ', ' ', ' '], [' ', 'X', ' ', ' ', ' ', ' ', ' '],
                                              [' ', 'X', ' ', ' ', ' ', ' ', ' '], [' ', 'X', ' ', ' ', ' ', ' ', ' ']])