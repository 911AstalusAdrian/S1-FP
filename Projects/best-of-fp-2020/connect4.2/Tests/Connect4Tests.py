import unittest

from Domain.Board import Board
from Domain.Player import Player
from Game.Connect4 import Connect4
from Strategies.MinimaxStrategy import MinimaxStrategy


class Connect4Tests(unittest.TestCase):
    def setUp(self):
        self.board = Board(6, 7, 4)
        strategy = MinimaxStrategy(self.board, 1)
        self.player1 = Player('h', 1, 'x')
        self.player2 = Player('c', 2, 'o')
        self.connect4 = Connect4(self.board, strategy, self.player1, self.player2)

    def test_get_board(self):
        """ Testing get_board """
        self.connect4.next_human_move(4)

        board2 = self.connect4.get_board()

        self.assertEqual(self.board[5][4].value, board2[5][4].value)

    def test_stalemate(self):
        """ Testing stalemate """
        for col in range(0, 7):
            for row in range(0, 6):
                self.board.place_piece(col, 1)

        self.assertEqual(True, self.connect4.stalemate())

    def test_won(self):
        """ Testing won """
        for col in range(0, 7):
            for row in range(0, 6):
                self.board.place_piece(col, 1)

        self.assertEqual(True, self.connect4.won())

    def test_get_current_player(self):
        """ Testing get_current_player """
        self.assertEqual(self.player1.id, self.connect4.get_current_player().id)

        self.connect4.next_human_move(3)

        self.assertEqual(self.player2.id, self.connect4.get_current_player().id)

    def test_get_current_opponent(self):
        """ Testing get_current_opponent """
        self.assertEqual(self.player2.id, self.connect4.get_current_opponent().id)

        self.connect4.next_human_move(3)

        self.assertEqual(self.player1.id, self.connect4.get_current_opponent().id)

    def test_next_computer_move(self):
        """ Testing next_computer_move """
        self.assertEqual(self.player1.id, self.connect4.get_current_player().id)

        self.connect4.next_computer_move()

        self.assertEqual(self.player2.id, self.connect4.get_current_player().id)

    def test_next_human_move(self):
        """ Testing next_human_move """
        self.assertEqual(self.player1.id, self.connect4.get_current_player().id)

        self.connect4.next_human_move(3)

        self.assertEqual(self.player2.id, self.connect4.get_current_player().id)
