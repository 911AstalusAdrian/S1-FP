from unittest import TestCase

from business.player import Player
from domain.board import Board
from errors import ServiceError, RuleError
from persistence.rules import Rules


class TestPlayer(TestCase):

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

        self.__own_board = Board()
        self.__opponent_board = Board()

        self.__player = Player(self.__own_board, self.__opponent_board)

        self.__empty_board = [
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
        self.__target_board = [
            '0', 's0', 's0', 's0', '0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
            '0', 'a0', 'a0', 'a0', 'a0', 'a0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', 'c0', '0',
            '0', '0', 'd0', '0', '0', '0', '0', '0', 'c0', '0',
            '0', '0', 'd0', '0', 'b0', '0', '0', '0', 'c0', '0',
            '0', '0', '0', '0', 'b0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', 'b0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', 'b0', '0', '0', '0', '0', '0',
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'
        ]

    def test_set_own_ships(self):
        with self.assertRaisesRegex(ServiceError, '^Ship not in bounds!$'):
            self.__player.place_ship('carrier', 11, 4, 'horizontal')
        with self.assertRaisesRegex(ServiceError, '^Ship not in bounds!$'):
            self.__player.place_ship('cruiser', 2, 0, 'vertical')
        with self.assertRaisesRegex(ServiceError, '^Ship not in bounds!$'):
            self.__player.place_ship('destroyer', 6, 10, 'horizontal')
        with self.assertRaisesRegex(ServiceError, '^Ship not in bounds!$'):
            self.__player.place_ship('battleship', 8, 9, 'vertical')

        self.__player.place_ship('battleship', 6, 5, 'vertical')

        with self.assertRaisesRegex(ServiceError, '^Ships cannot overlap!$'):
            self.__player.place_ship('submarine', 7, 4, 'horizontal')

        self.__player.place_ship('submarine', 1, 2, 'horizontal')
        self.__player.place_ship('carrier', 3, 2, 'horizontal')

        with self.assertRaisesRegex(ServiceError, '^Ship.*is already placed!$'):
            self.__player.place_ship('battleship', 10, 5, 'horizontal')

        with self.assertRaisesRegex(ServiceError, '^Ship \'carrier\' is already placed!$'):
            self.__player.place_ship('carrier', 3, 10, 'vertical')

        self.__player.place_ship('destroyer', 5, 3, 'vertical')

        with self.assertRaisesRegex(ServiceError, '^Ships cannot overlap!$'):
            self.__player.place_ship('cruiser', 4, 5, 'vertical')

        self.__player.place_ship('cruiser', 4, 9, 'vertical')

        self.assertEqual(self.__own_board.values, self.__target_board)

    def test_shoot(self):


        opponent = Player(self.__opponent_board, self.__own_board)

        opponent.place_ship('battleship', 6, 5, 'vertical')
        opponent.place_ship('submarine', 1, 2, 'horizontal')
        opponent.place_ship('carrier', 3, 2, 'horizontal')
        opponent.place_ship('destroyer', 5, 3, 'vertical')
        opponent.place_ship('cruiser', 4, 9, 'vertical')

        self.assertEqual(self.__own_board, self.__empty_board)

        self.assertEqual(self.__opponent_board, self.__target_board)

        with self.assertRaisesRegex(ServiceError, '^Position out of bounds!$'):
            self.__player.shoot(0, 2)
        with self.assertRaisesRegex(ServiceError, '^Position out of bounds!$'):
            self.__player.shoot(3, -3)
        with self.assertRaisesRegex(ServiceError, '^Position out of bounds!$'):
            self.__player.shoot(11, 5)
        with self.assertRaisesRegex(ServiceError, '^Position out of bounds!$'):
            self.__player.shoot(3, 13)

        message = self.__player.shoot(4, 6)
        self.assertEqual(message, 'Miss!')

        message = self.__player.shoot(7, 5)
        self.assertEqual(message, 'Hit!')

        message = self.__player.shoot(1, 3)
        self.assertEqual(message, 'Hit!')

        message = self.__player.shoot(1, 10)
        self.assertEqual(message, 'Miss!')

        message = self.__player.shoot(10, 10)
        self.assertEqual(message, 'Miss!')

        with self.assertRaisesRegex(ServiceError, '^Cannot shoot in the same place two times!$'):
            self.__player.shoot(7, 5)

        message = self.__player.shoot(9, 5)
        self.assertEqual(message, 'Hit!')

        message = self.__player.shoot(5, 9)
        self.assertEqual(message, 'Hit!')

        message = self.__player.shoot(7, 3)
        self.assertEqual(message, 'Miss!')

        message = self.__player.shoot(8, 5)
        self.assertEqual(message, 'Hit!')

        message = self.__player.shoot(6, 5)
        self.assertEqual(message, 'Sunk \'battleship\'!')

        opponent = Player(self.__opponent_board, self.__own_board)
        self.assertTrue(opponent.won())
        self.assertFalse(self.__player.won())

    def test_touch_rule_true(self):
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

        self.__player.place_ship('submarine', 5, 5)

        self.__player.place_ship('destroyer', 4, 6)
        self.__player.place_ship('battleship', 4, 1)
        self.__player.place_ship('cruiser', 6, 5, 'vertical')
        self.__player.place_ship('carrier', 6, 8, 'vertical')

    def test_touch_rule_false(self):
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

        self.assertFalse(Rules().can_touch)

        self.__player.place_ship('submarine', 5, 5)

        with self.assertRaisesRegex(ServiceError, '^.*touch.*$'):
            self.__player.place_ship('destroyer', 4, 6)
        with self.assertRaisesRegex(ServiceError, '^.*touch.*$'):
            self.__player.place_ship('battleship', 4, 1)
        with self.assertRaisesRegex(ServiceError, '^.*touch.*$'):
            self.__player.place_ship('cruiser', 6, 5, 'vertical')
        with self.assertRaisesRegex(ServiceError, '^.*touch.*$'):
            self.__player.place_ship('carrier', 6, 8, 'vertical')

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
