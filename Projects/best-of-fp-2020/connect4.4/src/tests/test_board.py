from copy import copy
from unittest import TestCase

from board.board import Board
from board.cell import Cell


class TestBoard(TestCase):
    def setUp(self):
        self.test_board = Board(6, 7)

    def test_columns(self):
        self.assertEqual(self.test_board.columns, 7)

    def test_lines(self):
        self.assertEqual(self.test_board.lines, 6)

    def test_set_value(self):
        self.test_board.set_value(1, 1, 1)
        self.assertEqual(self.test_board._board[1][1].value, 1)

    def test_get_line_first_empty_cell_in_column(self):
        self.test_board.set_value(5, 0, 1)
        self.assertEqual(self.test_board.get_line_first_empty_cell_in_column(0), 4)
        for line in range(6):
            self.test_board.set_value(line, 1, 1)
        self.assertIsNone(self.test_board.get_line_first_empty_cell_in_column(1))

    def test_count_connected_pieces_to_cell_on_column(self):
        for line in [2, 3, 4]:
            self.test_board.set_value(line, 1, 1)
        self.assertEqual(self.test_board.count_connected_pieces_to_cell_on_column(Cell(3, 1, 1)), 3)

    def test_count_connected_pieces_to_cell_on_line(self):
        for column in [2, 3, 4]:
            self.test_board.set_value(1, column, 1)
        self.assertEqual(self.test_board.count_connected_pieces_to_cell_on_line(Cell(1, 3, 1)), 3)

    def test_count_connected_pieces_to_cell_on_principal_diagonal(self):
        for i in [0, 1, 2]:
            self.test_board.set_value(i, i, 1)
        self.assertEqual(self.test_board.count_connected_pieces_to_cell_on_principal_diagonal(Cell(1, 1, 1)), 3)

    def test_count_connected_pieces_to_cell_on_secondary_diagonal(self):
        for i in [0, 1, 2]:
            self.test_board.set_value(i, 6 - i, 1)
        self.assertEqual(self.test_board.count_connected_pieces_to_cell_on_secondary_diagonal(Cell(1, 5, 1)), 3)

    def test_str(self):
        test_board_2 = Board(2, 2)
        string = "-----\n|O|O|\n-----\n|O|O|\n-----\n"
        self.assertEqual(str(test_board_2), string)

    def test_copy(self):
        board_copy = copy(self.test_board)
        self.assertEqual(board_copy.lines, 6)
        self.assertEqual(board_copy.columns, 7)
