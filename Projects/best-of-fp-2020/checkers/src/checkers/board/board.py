import pygame

from checkers.piece.piece import Piece
from checkers.tools.constants import BLACK, ROWS, SQUARE_SIZE, COLS, YELLOW, PURPLE
from strategy.strategy import Strategy


class Board:
    def __init__(self):
        self._board = []
        self._purple_left = self._yellow_left = 12
        self._purple_kings = self._yellow_kings = 0
        self.create_board()

    def get_board(self):
        return self._board

    def create_board(self):
        """
        The board is created in the memory
        :return:
        """
        for row in range(ROWS):
            self._board.append([])
            for col in range(COLS):
                #on row 0, we draw the odd columns, row 1 - even cols, row 2 - odd cols, and so on
                if col % 2 == ((row + 1) % 2):
                    if row <= 2:
                        self._board[row].append(Piece(row, col, YELLOW))
                    elif row >= 5:
                        self._board[row].append(Piece(row, col, PURPLE))
                    else:
                        self._board[row].append(0)
                else:
                    self._board[row].append(0)

    def move(self, piece, row, col):
        """
        swaps the values of 2 cells
        a piece becomes king if it ARRIVES at the top or bottom of the board (not if they are already there)

        """
        self._board[piece.row][piece.col], self._board[row][col] = self._board[row][col], self._board[piece.row][piece.col]
        piece.move(row, col)

        if piece.row == ROWS - 1 or piece.row == 0 and piece.king == False:
            piece.make_king()
            if piece.color == YELLOW:
                self._yellow_kings += 1
            else:
                self._purple_kings += 1

    def get_piece(self, row, col):
        return self._board[row][col]

    def get_valid_moves(self, piece):
        """
        moves - dictonary: key = destination position of our piece
                           value = any pieces that we jump (capture) to that move
        :param piece:
        :return:
        """

        moves = {}
        left_col = piece.col - 1
        right_col = piece.col + 1

        if piece.color == PURPLE or piece._king:
            moves.update(self.__cross_left(piece.row - 1, max(piece.row - 3, -1), -1, piece.color, left_col))
            moves.update(self.__cross_right(piece.row - 1, max(piece.row - 3, -1), -1, piece.color, right_col))
        if piece.color == YELLOW or piece._king:
            moves.update(self.__cross_left(piece.row + 1, min(piece.row + 3, ROWS), 1, piece.color, left_col))
            moves.update(self.__cross_right(piece.row + 1, min(piece.row + 3, ROWS), 1, piece.color, right_col))
        return moves

    def __cross_left(self, start, stop, direction, color, left_position, skipped=list()):
        """

        :param start - what row we start from
        :param stop: what row we stop at
        :param direction: the direction we go through the rows, -1 / +1
        :param color:
        :param left: where we start, in terms of columns, when we traverse to the left
        :param skipped: Tells us if we have skipped(captured) any pieces.
        If we have, we can only move to squares where we continue capturing other pieces
        :return:
        """
        moves = {}
        last = []
        for row in range(start, stop, direction):
            if left_position < 0:
                break

            current = self.get_piece(row, left_position)
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(row, left_position)] = last + skipped
                else:
                    moves[(row, left_position)] = last
                if last:
                    if direction == -1:
                        row_stop = max(row - 3, -1)
                    else:
                        row_stop = min(row + 3, ROWS)
                    moves.update(self.__cross_left(row + direction, row_stop, direction, color, left_position - 1, skipped=skipped + last))
                    moves.update(self.__cross_right(row + direction, row_stop, direction, color, left_position + 1, skipped=skipped + last))
                break

            elif current.color == color:
                break
            else:
                last = [current]
            left_position -= 1

        return moves
    def __cross_right(self, start, stop, direction, color, right_position, skipped=list()):
        """
        :param start:
        :param stop:
        :param direction: the direction we go through the rows, -1 / +1
        :param color:
        :param right: where we start, in terms of columns, when we traverse to the right
        :param skipped: Tells us if we have skipped(captured) any pieces.
        If we have, we can only move to squares where we continue capturing other pieces
        :return:
        """
        moves = {}
        last = []
        for row in range(start, stop, direction):
            if right_position >= COLS:
                break

            current = self.get_piece(row, right_position)
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(row, right_position)] = skipped + last
                else:
                    moves[(row, right_position)] = last
                if last:
                    if direction == -1:
                        row_stop = max(row - 3, -1)
                    else:
                        row_stop = min(row + 3, ROWS)

                    moves.update(self.__cross_left(row + direction, row_stop, direction, color, right_position - 1, skipped=skipped + last))
                    moves.update(self.__cross_right(row + direction, row_stop, direction, color, right_position + 1, skipped=skipped + last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right_position += 1

        return moves

    def remove(self, pieces):
        for piece in pieces:
            if piece.color == YELLOW:
                self._yellow_left -= 1
            else:
                self._purple_left -= 1
            self._board[piece.row][piece.col] = 0


    def winner(self):
        if self._yellow_left <= 0 or not Strategy.get_all_moves(self, YELLOW):
            return PURPLE
        elif self._purple_left <= 0 or not Strategy.get_all_moves(self, PURPLE):
            return YELLOW

        return None

#=========================================AI=======================================================

    def evaluate(self):
        return self._yellow_left - self._purple_left + (self._yellow_kings * 0.5 - self._purple_kings * 0.5)

    def get_all_pieces(self, color):
        pieces = []
        for row in self._board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)

        return pieces