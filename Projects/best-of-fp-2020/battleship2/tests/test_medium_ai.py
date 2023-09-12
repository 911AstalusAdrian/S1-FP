from business.human import HumanPlayer
from domain.board import Board
from engines.medium import MediumAI
from tests.test_beginner_ai import TestBeginnerAI


class TestMediumAI(TestBeginnerAI):

    def _setup_players(self):
        player_board = Board()
        ai_board = Board()

        self._ai = MediumAI(ai_board, player_board)
        self._player = HumanPlayer(player_board, ai_board)
