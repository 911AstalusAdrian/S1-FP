from random import randint

from business.human import HumanPlayer
from domain.board import Board
from engines.beginner import BeginnerAI
from persistence.rules import Rules
from tests.test_ai import TestAI


class TestBeginnerAI(TestAI):

    def _setup_players(self):
        player_board = Board()
        ai_board = Board()

        self._ai = BeginnerAI(ai_board, player_board)
        self._player = HumanPlayer(player_board, ai_board)

    def test_shoot(self):
        Rules().set_rules(
            edge=10,
            can_touch=False,
            carriers=1,
            battleships=1,
            cruisers=1,
            destroyers=1,
            submarines=1,
            difficulty=2
        )
        self._setup_players()
        self._player_places_ships()

        self._test_body()

    def test_shoot_with_touch(self):
        Rules().set_rules(
            edge=10,
            can_touch=True,
            carriers=1,
            battleships=1,
            cruisers=1,
            destroyers=1,
            submarines=1,
            difficulty=2
        )
        self._setup_players()
        self._player_places_ships()
        self._test_body()

    def _test_body(self):
        times_hit = 0
        times_miss = 0
        sunken_ships = []
        times = randint(20, 30)
        i = 0
        while i < times or len(sunken_ships) == 0:
            message = self._ai.shoot()[0]
            if 'hit' in message.lower():
                times_hit += 1
            elif 'miss' in message.lower():
                times_miss += 1
            else:
                times_hit += 1
                message = message.split('\'')[1]
                sunken_ships.append(message)
            i += 1

        own_board = self._player.get_own_board()
        for elem in own_board:
            if elem == '-':
                times_miss -= 1
            elif elem == '+':
                times_hit -= 1
            elif elem == '*':
                times_hit -= 1

        self.assertEqual(times_hit, 0)
        self.assertEqual(times_miss, 0)
