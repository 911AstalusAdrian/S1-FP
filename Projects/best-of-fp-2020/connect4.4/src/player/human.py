from board.cell import Cell
from player.player import Player


class Human(Player):
    def move(self, line, column):
        """
        Does a move for the Human using given coordinates
        :param line: The line on which the Human will do the move
        :param column: The column on which the Human will do the move
        :return: The new form of the Cell affected by the Human's move, an object of type Cell
        """
        self._board.set_value(line, column, self._value)
        return Cell(line, column, self._value)
