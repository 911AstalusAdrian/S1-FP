from abc import abstractmethod


class Player:
    def __init__(self, name, board, value):
        """
        Creates an object of type Player
        :param name: The name of the Player, a string
        :param board: The board on which the Player will play, an object of type Board
        :param value: The value used to represent the Player's pieces on the board
        """
        self._name = name
        self._board = board
        self._value = value

    @property
    def name(self):
        """
        Returns the Player's name
        :return: The Player's name, a string
        """
        return self._name

    @property
    def value(self):
        """
        Returns the value used to represent the Player's pieces on the board
        :return: The value used to represent the Player's pieces on the board
        """
        return self._value

    @abstractmethod
    def move(self, *args):
        """
        Does a move for the player. This function must be implemented in all subclasses
        :param args: The arguments of the function, depending on the subclass from which it is called
        :return: The new form of the Cell affected by the move, an object of type Cell
        """
        pass
