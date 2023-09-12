import pygame

from checkers.board.board import Board
from checkers.tools.constants import PURPLE, YELLOW, GREEN, SQUARE_SIZE, WIDTH, HEIGHT, WHITE, BLACK, ROWS, COLS, CROWN, \
    LAVA, ROCK, PURPLE_PIC, YELLOW_PIC


class Game:
    def __init__(self):
        self.__init()

    def __init(self):
        self._selected_piece = None
        self._board = Board()
        self._turn = PURPLE
        self._valid_moves = {}

    @property
    def board(self):
        return self._board

    @property
    def valid_moves(self):
        return self._valid_moves
    
    @property
    def turn(self):
        return self._turn

    @property
    def selected_piece(self):
        return self._selected_piece

    def reset(self):
        self.__init()

    def select(self, row, col):
        """
        If we already selected a piece, we try to move it.
        If we fail to move it at a valid position, we retry the process

        If we do not have a selected piece, we get the one at the current position
        and find its valid possible moves

        :param row:
        :param col:
        :return: True if we selected a valid board cell, False otherwise
        """
        if self._selected_piece:
            result = self.__move(row, col)
            if not result:
                self._selected_piece = None
                self.select(row, col)

        piece = self._board.get_piece(row, col)
        if piece != 0 and piece.color == self._turn:
            self._selected_piece = piece
            self._valid_moves = self._board.get_valid_moves(piece)
            return True

        return False

    def __move(self, row, col):
        """
        checks if the position we want to move a piece in is valid or not, then moves it
        :param row:
        :param col:
        :return: True if we are able to move a piece at row, col, False otherwise
        """
        piece = self._board.get_piece(row, col)
        if self._selected_piece and piece == 0 and (row, col) in self._valid_moves:
            self._board.move(self._selected_piece, row, col)
            skipped = self._valid_moves[(row, col)]
            if skipped:
                self._board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def change_turn(self):
        """
        Resets the valid moves dictionary and switches turn between Purple and Yellow
        :return:
        """
        self._valid_moves = {}
        if self._turn == PURPLE:
            self._turn = YELLOW
        else:
            self._turn = PURPLE

    def winner(self):
        return self._board.winner()

    def ai_move(self, board):
        self._board = board
        self.change_turn()


class GameException(Exception):
    pass