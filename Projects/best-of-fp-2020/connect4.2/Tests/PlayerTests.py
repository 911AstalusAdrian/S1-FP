import unittest

from Domain.Player import Player


class PlayerTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_player(self):
        """ Testing Player """
        self.assertRaises(TypeError, Player, 'u', 1, 1)

        player = Player('h', 1, 1)

        self.assertEqual(player.id, 1)
        self.assertEqual(player.piece, 1)
        self.assertEqual(player.type, 'h')

        player.type = 'c'

        self.assertEqual(player.type, 'c')

        player.piece = 2

        self.assertEqual(player.piece, 2)
