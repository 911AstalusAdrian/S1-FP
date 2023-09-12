import unittest

from Domain.Board import BoardException, Board
from Tests.TestFileParser import TestFileParser


class BoardTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_place_cell(self):
        """ Testing board.place_cell """
        file = open('Test_files/test_place_cell', 'r')
        parser = TestFileParser(file)

        for args, board in parser.get_boards_from_file():
            args = args.split(' ')
            is_valid = bool(int(args[0]))
            col = int(args[1])

            if is_valid:
                board.place_piece(col, 1)
                self.assertEqual(board.get_cell_from_column(col).value, 1)
            else:
                self.assertRaises(BoardException, board.place_piece, col, 1)

        file.close()

    def test_won(self):
        """ Testing board.won """
        file = open('Test_files/test_won', 'r')
        parser = TestFileParser(file)

        for args, board in parser.get_boards_from_file():
            is_won = bool(int(args))
            self.assertEqual(board.won(), is_won)

        file.close()

    def test_is_full(self):
        """ Testing board.is_full """
        file = open('Test_files/test_is_full', 'r')
        parser = TestFileParser(file)

        for args, board in parser.get_boards_from_file():
            is_full = bool(int(args))
            self.assertEqual(board.is_full(), is_full)

        file.close()

    def test_is_empty(self):
        """ Testing board.is_cell_empty """
        board = Board(6, 7, 4)

        self.assertRaises(BoardException, board.is_cell_empty, 8, 8)

        board.place_piece(4, 1)

        self.assertEqual(False, board.is_cell_empty(5, 4))

    def test_remove_piece(self):
        """ Testing board.remove_piece """
        board = Board(6, 7, 4)

        self.assertRaises(BoardException, board.remove_piece, 8)  # col out of bounds
        self.assertRaises(BoardException, board.remove_piece, 1)  # col is empty

        board.place_piece(4, 1)
        board.remove_piece(4)

        self.assertEqual(True, board.is_cell_empty(5, 4))

    def test_get_cell_from_column(self):
        """ Testing board.get_cell_from_column """
        board = Board(6, 7, 4)

        self.assertRaises(BoardException, board.get_cell_from_column, 8)  # col out of bounds
        self.assertRaises(BoardException, board.get_cell_from_column, 4)  # col is empty

        board.place_piece(4, 1)
        board.place_piece(4, 2)

        cell = board.get_cell_from_column(4)

        self.assertEqual(2, cell.value)
