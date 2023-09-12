from unittest import TestCase
from domain.board import Board, BoardException


class TestBoard(TestCase):
    def setUp(self):
        self._board = Board(15, 15)

    def test_move(self):
        self._board.make_move(0, 2, 'O')
        self.assertEqual(self._board.is_symbol(0, 2, 'O'), True)

        self.assertRaises(BoardException, self._board.make_move, -1, -1, 'X')
        self.assertRaises(BoardException, self._board.make_move, 2, 5, 'Z')

        self.assertRaises(BoardException, self._board.delete_move, 5, -2)
        self.assertRaises(BoardException, self._board.delete_move, 0, 1)

        self._board.delete_move(0, 2)
        self.assertEqual(self._board.is_square_empty(0, 2), True)

    def test_has_neighbours(self):
        self.assertEqual(self._board.has_neighbours(0, 2), False)

        self._board.make_move(5, 2, 'O')
        self.assertEqual(self._board.has_neighbours(4, 2), True)
        self.assertEqual(self._board.has_neighbours(5, 3), True)

    def test_is_empty(self):
        self.assertEqual(self._board.free, 225)

        self._board.make_move(3, 2, 'X')
        self.assertEqual(self._board.free, 224)

    def test_get_available_squares(self):
        available = self._board.get_available_squares()
        self.assertEqual(len(available), self._board.free)
