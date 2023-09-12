import unittest
from Board.board import *


class TestBoard(unittest.TestCase):
    def test_board(self):
        b = Board()
        self.assertEqual(b.col_count, 7)
        self.assertEqual(b.row_count, 6)
        self.assertEqual(b.get_data(), [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                        [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                        [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        b.move(1,'X')
        self.assertEqual(b.is_free(1),True)
        self.assertEqual(b.checkWin('X'),False)
        for i in range(4):
            b.move(1, 'X')
        self.assertEqual(b.is_free(1),True)
        self.assertEqual(b.checkWin('X'), True)
        b.move(1, 'X')
        self.assertEqual(b.is_free(1), False)
        self.assertEqual(b.is_full(), False)