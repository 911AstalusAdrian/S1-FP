import pygame

from checkers.tools.constants import SQUARE_SIZE


class Piece:
    def __init__(self, row, col, color):
        self._row = row
        self._col = col
        self._color = color
        self._king = False

        self._x = 0
        self._y = 0
        #self.calculate_position()
        from checkers.view.gui import GUI
        GUI.piece_calculate_position(self)

    # def calculate_position(self):
    #     """
    #     calculates x and y coordinates, and places the piece in the middle of the square
    #     :return:
    #     """
    #     self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
    #     self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    @property
    def row(self):
        return self._row
    @property
    def col(self):
        return self._col

    @property
    def color(self):
        return self._color

    @property
    def king(self):
        return self._king

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def make_king(self):
        self._king = True

    def move(self, row, col):
        self._row = row
        self._col = col
        #self.calculate_position()
        from checkers.view.gui import GUI
        GUI.piece_calculate_position(self)