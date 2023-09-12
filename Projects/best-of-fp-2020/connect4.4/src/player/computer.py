from player.player import Player


class Computer(Player):
    def __init__(self, name, board, value, strategy):
        """
        Creates an object of type Computer
        :param name: The name of the Computer, a string
        :param board: The board on which the Computer will play, an object of type Board
        :param value: The value used to represent the Computer's pieces on the board
        :param strategy: The strategy that the Computer will use, an object whose class inherits the class Strategy
        """
        super().__init__(name, board, value)
        self.__strategy = strategy

    def move(self, enemy_value):
        """
        Does a move for the Computer using the given strategy
        :param enemy_value: The value used to represent the enemy player on the board
        :return: The new form of the Cell affected by the move, an object of type Cell
        """
        return self.__strategy.move(self._board, self._value, enemy_value)
