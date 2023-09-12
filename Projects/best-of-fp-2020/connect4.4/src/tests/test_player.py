from unittest import TestCase

from board.board import Board
from player.player import Player


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("name", Board(3, 3), 1)

    def test_name(self):
        self.assertEqual(self.player.name, "name")

    def test_value(self):
        self.assertEqual(self.player.value, 1)

    def test_move(self):
        self.assertIsNone(self.player.move())
