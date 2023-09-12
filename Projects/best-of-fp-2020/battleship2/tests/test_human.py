from unittest import TestCase

from business.human import HumanPlayer
from domain.board import Board
from errors import ServiceError
from persistence.rules import Rules


class TestHuman(TestCase):

    def setUp(self) -> None:
        self.__original_edge = Rules().edge
        self.__original_can_touch = Rules().can_touch
        self.__original_number_of_a = Rules().number_of['carrier']
        self.__original_number_of_b = Rules().number_of['battleship']
        self.__original_number_of_c = Rules().number_of['cruiser']
        self.__original_number_of_d = Rules().number_of['destroyer']
        self.__original_number_of_s = Rules().number_of['submarine']
        self.__original_difficulty = Rules().difficulty

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

    def test_human(self):
        own_board = Board()
        opponent_board = Board()

        player = HumanPlayer(own_board, opponent_board)
        opponent = HumanPlayer(opponent_board, own_board)

        self.assertFalse(player.are_all_placed())
        self.assertEqual(player.unplaced_ships(), [
            'd / destroyer',
            'c / cruiser',
            's / submarine',
            'b / battleship',
            'a / (aircraft) carrier'
        ])

        player.place_ship('destroyer', 3, 6)
        player.place_ship('battleship', 1, 1, 'vertical')
        opponent.place_ship('carrier', 7, 2)

        self.assertEqual(player.get_own_board(), [
            'b0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            'b0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            'b0', '0', '0', '0', '0', 'd0', 'd0', '0', '0', '0',
            'b0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'
        ])

        with self.assertRaisesRegex(ServiceError, "Invalid ship type!"):
            player.clear_ship('battleships')

        player.clear_ship('battleship')
        self.assertEqual(player.get_own_board(), [
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', 'd0', 'd0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'
        ])

        self.assertEqual(player.unveil_opponent_board(), [
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', 'a0', 'a0', 'a0', 'a0', 'a0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'
        ])
        self.assertEqual(player.get_opponent_board(), ['0']*100)

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
