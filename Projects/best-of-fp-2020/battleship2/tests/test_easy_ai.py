from random import randint

from business.human import HumanPlayer
from domain.board import Board
from engines.easy import EasyAI
from persistence.rules import Rules
from tests.test_beginner_ai import TestBeginnerAI


class TestEasyAI(TestBeginnerAI):

    def _setup_players(self):
        player_board = Board()
        ai_board = Board()

        self._ai = EasyAI(ai_board, player_board)
        self._player = HumanPlayer(player_board, ai_board)

