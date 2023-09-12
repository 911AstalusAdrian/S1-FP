from unittest import TestCase

from domain.board import Board
from persistence.rules import Rules


class TestBoard(TestCase):

    def setUp(self) -> None:
        self.__original_edge = Rules().edge
        self.__original_can_touch = Rules().can_touch
        self.__original_number_of_a = Rules().number_of['carrier']
        self.__original_number_of_b = Rules().number_of['battleship']
        self.__original_number_of_c = Rules().number_of['cruiser']
        self.__original_number_of_d = Rules().number_of['destroyer']
        self.__original_number_of_s = Rules().number_of['submarine']
        self.__original_difficulty = Rules().difficulty

    def tearDown(self) -> None:
        Rules().set_rules(
            edge=self.__original_edge,
            can_touch=self.__original_can_touch,
            carriers=self.__original_number_of_a,
            battleships=self.__original_number_of_b,
            cruisers=self.__original_number_of_c,
            destroyers=self.__original_number_of_d,
            submarines=self.__original_number_of_s,
            difficulty=self.__original_difficulty
        )

    def test_classic_game_board(self):
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

        empty_board = [
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'
        ]
        target_board = [
            '0', 's0', 's0', 's0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', 'a0', 'a0', 'a0', 'a0', 'a0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', 'c0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', 'c0', '0',
            '0', '0', '0', '0', 'b0', '0', '0', '0', 'c0', '0',
            '0', '0', '0', '0', 'b0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', 'b0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', 'b0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', 'd0', 'd0', '0', '0'
        ]
        final_board = [
            '0', 's0', '+', 's0', '0', '0', '0', '0', '0', '-',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', 'a0', 'a0', 'a0', 'a0', 'a0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '-', '0', '0', 'c0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '+', '0',
            '0', '0', '0', '0', '+', '0', '0', '0', 'c0', '0',
            '0', '0', '-', '0', '+', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '+', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '+', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', 'd0', '+', '0', '-'
        ]
        final_board_with_sunken = [
            '0', 's0', '+', 's0', '0', '0', '0', '0', '0', '-',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', 'a0', 'a0', 'a0', 'a0', 'a0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '-', '0', '0', 'c0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '+', '0',
            '0', '0', '0', '0', '*', '0', '0', '0', 'c0', '0',
            '0', '0', '-', '0', '*', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '*', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '*', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', 'd0', '*', '0', '-'
        ]

        board = Board()

        self.assertEqual(board, empty_board)
        self.assertEqual(board.last_shot_success, '')

        board.place_ship('destroyer', 10, 7, 'E')
        board.place_ship('cruiser', 6, 9, 'N')
        board.place_ship('carrier', 3, 2, 'e')
        board.place_ship('submarine', 1, 4, 'w')
        board.place_ship('battleship', 6, 5, 'S')

        board.clear_ship('battleship')
        board.place_ship('battleship', 6, 5, 'S')

        self.assertEqual(board, target_board)

        self.assertTrue(board.is_ship(1, 2))
        self.assertFalse(board.is_ship(1, 1))

        self.assertEqual(board.hp['destroyer'][0], 2)
        self.assertEqual(board.hp['cruiser'][0], 3)
        self.assertEqual(board.hp['submarine'][0], 3)
        self.assertEqual(board.hp['battleship'][0], 4)
        self.assertEqual(board.hp['carrier'][0], 5)

        self.assertEqual(board.ships_left['destroyer'], 1)
        self.assertEqual(board.ships_left['cruiser'], 1)
        self.assertEqual(board.ships_left['submarine'], 1)
        self.assertEqual(board.ships_left['battleship'], 1)
        self.assertEqual(board.ships_left['carrier'], 1)

        self.assertFalse(board.already_shot(4, 6))
        self.assertFalse(board.already_shot(7, 5))

        self.assertTrue(board.empty(4, 6))
        self.assertFalse(board.empty(7, 5))

        board.shoot(4, 6)
        board.shoot(7, 5)

        self.assertTrue(board.already_shot(4, 6))
        self.assertTrue(board.already_shot(7, 5))

        board.shoot(1, 3)
        board.shoot(1, 10)
        board.shoot(10, 10)
        board.shoot(9, 5)
        board.shoot(5, 9)
        self.assertEqual(board.last_shot_success, 'hit')

        board.shoot(7, 3)
        self.assertEqual(board.last_shot_success, 'miss')
        board.shoot(6, 5)
        board.shoot(8, 5)
        self.assertEqual(board.last_shot_success, "sunk 'battleship'")
        board.shoot(10, 8)

        self.assertEqual(board.ships_left['destroyer'], 1)
        self.assertEqual(board.ships_left['cruiser'], 1)
        self.assertEqual(board.ships_left['submarine'], 1)
        self.assertEqual(board.ships_left['battleship'], 0)
        self.assertEqual(board.ships_left['carrier'], 1)

        self.assertEqual(board.values, final_board)
        self.assertEqual(board.hp['destroyer'][0], 1)
        self.assertEqual(board.hp['cruiser'][0], 2)
        self.assertEqual(board.hp['submarine'][0], 2)
        self.assertEqual(board.hp['battleship'][0], 0)
        self.assertEqual(board.hp['carrier'][0], 5)

        with self.assertRaisesRegex(ValueError, "Not ok!"):
            board.sink_ship(1, 1)

        board.sink_ship(9, 5)
        board.sink_ship(10, 8)
        self.assertEqual(board.values, final_board_with_sunken)
