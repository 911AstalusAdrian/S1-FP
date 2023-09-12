from unittest import TestCase

from business.human import HumanPlayer
from domain.board import Board
from engines.ai import AI
from persistence.rules import Rules


class TestAI(TestCase):

    def setUp(self) -> None:
        self._original_edge = Rules().edge
        self._original_can_touch = Rules().can_touch
        self._original_number_of_a = Rules().number_of['carrier']
        self._original_number_of_b = Rules().number_of['battleship']
        self._original_number_of_c = Rules().number_of['cruiser']
        self._original_number_of_d = Rules().number_of['destroyer']
        self._original_number_of_s = Rules().number_of['submarine']
        self._original_difficulty = Rules().difficulty

    def _setup_players(self):
        player_board = Board()
        ai_board = Board()

        self._ai = AI(ai_board, player_board)
        self._player = HumanPlayer(player_board, ai_board)

    def _player_places_ships(self):
        self._player.place_ship('destroyer', 5, 3, 'vertical')
        self._player.place_ship('submarine', 1, 2)
        self._player.place_ship('carrier', 3, 2)
        self._player.place_ship('cruiser', 4, 9, 'vertical')
        self._player.place_ship('battleship', 6, 5, 'vertical')

    def _cell_formula(self, line, column, edge_size=10):
        return line * edge_size + column

    def _check_surroundings(self, board, line, column, value, edge_size=10):
        """ Returns false if in the neighbour cells of the given one contain a ship part from another ship, true o.. """
        result = board[self._cell_formula(line - 1, column, edge_size)] in ['0', '-', '+', value] if line > 1 else True
        result = result and (board[self._cell_formula(line - 1, column + 1, edge_size)] in ['0', '-', '+', value]
                             if (line > 1 and column < edge_size - 1) else True)
        result = result and (board[self._cell_formula(line, column + 1, edge_size)] in ['0', '-', '+', value]
                             if column < edge_size - 1 else True)
        result = result and (board[self._cell_formula(line + 1, column + 1, edge_size)] in ['0', '-', '+', value]
                             if (line < edge_size - 1 and column < edge_size - 1) else True)
        result = result and (board[self._cell_formula(line + 1, column, edge_size)] in ['0', '-', '+', value]
                             if line < edge_size - 1 else True)
        result = result and (board[self._cell_formula(line + 1, column - 1, edge_size)] in ['0', '-', '+', value]
                             if (column > 1 and line < edge_size - 1) else True)
        result = result and (board[self._cell_formula(line, column - 1, edge_size)] in ['0', '-', '+', value]
                             if column > 1 else True)
        result = result and (board[self._cell_formula(line - 1, column - 1, edge_size)] in ['0', '-', '+', value]
                             if (line > 1 and column > 1) else True)
        return result

    def test_usual_game_no_touch(self):
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
        self._ai.place_all_ships()

        check_dict = {'a0': 0, 'b0': 0, 'c0': 0, 'd0': 0, 's0': 0}

        opp_board = self._player.unveil_opponent_board()

        for i in range(10):
            for j in range(10):
                value = opp_board[i * 10 + j]
                if value in check_dict:
                    check_dict[value] += 1
                    self.assertTrue(self._check_surroundings(opp_board, i, j, value))

        self.assertEqual(check_dict['a0'], 5)
        self.assertEqual(check_dict['b0'], 4)
        self.assertEqual(check_dict['c0'], 3)
        self.assertEqual(check_dict['d0'], 2)
        self.assertEqual(check_dict['s0'], 3)

    def test_usual_game_with_touch(self):
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
        self._ai.place_all_ships()

        check_dict = {'a0': 0, 'b0': 0, 'c0': 0, 'd0': 0, 's0': 0}

        opp_board = self._player.unveil_opponent_board()

        for i in range(10):
            for j in range(10):
                value = opp_board[i * 10 + j]
                if value in check_dict:
                    check_dict[value] += 1

        self.assertEqual(check_dict['a0'], 5)
        self.assertEqual(check_dict['b0'], 4)
        self.assertEqual(check_dict['c0'], 3)
        self.assertEqual(check_dict['d0'], 2)
        self.assertEqual(check_dict['s0'], 3)

    # def test_game_with_more_ships_no_touch(self):
    #     Rules().set_rules(
    #         edge=15,
    #         can_touch=False,
    #         carriers=3,
    #         battleships=2,
    #         cruisers=5,
    #         destroyers=2,
    #         submarines=3,
    #         difficulty=2
    #     )
    #     self._setup_players()
    #     self._ai.place_all_ships()
    #
    #     check_dict = {'a0': 0, 'a1': 0, 'a2': 0, 'b0': 0, 'b1': 0,
    #                   'c0': 0, 'c1': 0, 'c2': 0, 'c3': 0, 'c4': 0,
    #                   'd0': 0, 'd1': 0, 's0': 0, 's1': 0, 's2': 0,
    #                   }
    #
    #     opp_board = self._player.unveil_opponent_board()
    #
    #     for i in range(15):
    #         for j in range(15):
    #             value = opp_board[i * 15 + j]
    #             if value in check_dict:
    #                 check_dict[value] += 1
    #                 self.assertTrue(self._check_surroundings(opp_board, i, j, value, edge_size=15))
    #
    #     self.assertEqual(check_dict['a0'], 5)
    #     self.assertEqual(check_dict['a1'], 5)
    #     self.assertEqual(check_dict['a2'], 5)
    #     self.assertEqual(check_dict['b0'], 4)
    #     self.assertEqual(check_dict['b1'], 4)
    #     self.assertEqual(check_dict['c0'], 3)
    #     self.assertEqual(check_dict['c1'], 3)
    #     self.assertEqual(check_dict['c2'], 3)
    #     self.assertEqual(check_dict['c3'], 3)
    #     self.assertEqual(check_dict['c4'], 3)
    #     self.assertEqual(check_dict['d0'], 2)
    #     self.assertEqual(check_dict['d1'], 2)
    #     self.assertEqual(check_dict['s0'], 3)
    #     self.assertEqual(check_dict['s1'], 3)
    #     self.assertEqual(check_dict['s2'], 3)

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
        with self.assertRaises(Exception):
            self._ai.shoot()

    def tearDown(self) -> None:
        Rules().set_rules(
            edge=self._original_edge,
            can_touch=self._original_can_touch,
            carriers=self._original_number_of_a,
            battleships=self._original_number_of_b,
            cruisers=self._original_number_of_c,
            destroyers=self._original_number_of_d,
            submarines=self._original_number_of_s,
            difficulty=self._original_difficulty
        )