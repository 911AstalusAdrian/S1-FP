from unittest import TestCase
from service.strategy import AIStrategy
from service.game import Game


class GameTest(TestCase):
    def setUp(self):
        self._strategy = AIStrategy()
        self._game = Game(self._strategy, 15, 15)

    def test_human_move(self):
        self.assertEqual(self._game.human_move(1, 1, True), False)
        self.assertEqual(self._game.human_move(2, 1, True), False)
        self.assertEqual(self._game.human_move(3, 1, True), False)
        self.assertEqual(self._game.human_move(4, 1, True), False)
        self.assertEqual(self._game.human_move(5, 1, True), True)

    def test_computer_move(self):
        self.assertEqual(self._game.computer_move(True)[0], False)
        self.assertEqual(self._game.computer_move(True)[0], False)
        self.assertEqual(self._game.computer_move(True)[0], False)
        self.assertEqual(self._game.computer_move(True)[0], False)
        self.assertEqual(self._game.computer_move(True)[0], True)

    def test_five_line(self):
        self.assertEqual(self._game.find_five_line('O'), False)

        self._game.human_move(0, 1, True)
        self._game.human_move(1, 1, True)
        self._game.human_move(2, 1, True)
        self._game.human_move(3, 1, True)
        self._game.human_move(4, 1, True)

        self.assertEqual(self._game.find_five_line('O'), True)

    def test_five_main_diagonal(self):
        self.assertEqual(self._game.find_five_main_diagonal('X'), False)

        self._game.human_move(0, 0, False)
        self._game.human_move(1, 1, False)
        self._game.human_move(2, 2, False)
        self._game.human_move(3, 3, False)
        self._game.human_move(4, 4, False)

        self.assertEqual(self._game.find_five_main_diagonal('X'), True)

    def test_five_sec_diagonal(self):
        self.assertEqual(self._game.find_five_sec_diagonal('O'), False)

        self._game.human_move(0, 4, True)
        self._game.human_move(1, 3, True)
        self._game.human_move(2, 2, True)
        self._game.human_move(3, 1, True)
        self._game.human_move(4, 0, True)

        self.assertEqual(self._game.find_five_sec_diagonal('O'), True)