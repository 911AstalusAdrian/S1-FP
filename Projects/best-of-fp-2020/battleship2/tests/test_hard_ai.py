from business.human import HumanPlayer
from domain.board import Board
from engines.hard import HardAI
from engines.medium import MediumAI
from tests.test_beginner_ai import TestBeginnerAI


class TestHardAI(TestBeginnerAI):

    def _setup_players(self):
        player_board = Board()
        ai_board = Board()

        self._ai = HardAI(ai_board, player_board)
        self._player = HumanPlayer(player_board, ai_board)

    def test_score_board(self):
        self._setup_players()
        self._player_places_ships()

        self._ai.shoot()
        for i in range(100):
            self.assertGreaterEqual(self._ai.score_board[i], 0)
            self.assertLessEqual(self._ai.score_board[i], 1)
