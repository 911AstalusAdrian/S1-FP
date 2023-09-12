from random import choice

from engines.ai import AI
from collections import deque

from persistence.rules import Rules


class EasyAI(AI):
    """
    Easy level AI

    Randomised ship placement

    Randomised shooting + hunting when hitting a ship:

    Strategy:
        When hitting a ship it enters the 'hunt mode':
            Uses a priority queue with the neighboring cells that are most likely to contain the rest of the ship
        If the priority queue (deque) is empty it shoots randomly
    """

    def __init__(self, own_board, opponent_board):
        super().__init__(own_board, opponent_board)

        self._root = None
        self._priority = deque()
        self._ship_positions = []

    def _compute_target_coords(self):
        # Take the first value of the priority queue
        # or randomly choose from the available position if the priority queue is empty
        if len(self._priority) == 0:
            coords = choice(tuple(self._available_positions))
        else:
            coords = self._priority.popleft()

        try:
            self._available_positions.remove(coords)
        except KeyError:
            pass
        line = coords[0]
        column = coords[1]

        return line, column

    def _start_the_hunt(self, line, column, directions):
        """
        Enters 'hunt mode'
        The root is the current cell
        Puts in the priority queue all the neighboring cells to the north, east, south and west (in a random order)
        """

        self._root = (line, column)
        dirs = ['n', 'e', 's', 'w']
        for i in range(4):
            direction = choice(dirs)
            dirs.remove(direction)

            future_line = line + directions[direction]['line']
            future_column = column + directions[direction]['column']

            if 0 < future_line <= self._edge_length and 0 < future_column <= self._edge_length and not self._opponent_board.already_shot(
                    future_line, future_column):
                if not Rules().can_touch:
                    if self._opponent_board.is_ship(future_line, future_column):
                        self._priority.append((future_line, future_column))
                else:
                    self._priority.append((future_line, future_column))

    def _continue_the_hunt(self, line, column, directions):
        """
        Puts in the priority queue (on the first position) the next cell in the given direction (if it is in bounds)
        """
        direction = 'n' if (column == self._root[1] and line < self._root[0]) else \
            's' if (column == self._root[1] and line > self._root[0]) else \
            'w' if (column < self._root[1] and line == self._root[0]) else 'e'

        future_line = line + directions[direction]['line']
        future_column = column + directions[direction]['column']

        if 0 < future_line <= self._edge_length and 0 < future_column <= self._edge_length and not self._opponent_board.already_shot(
                future_line, future_column):
            self._priority.appendleft((future_line, future_column))

    def _hunt(self, line, column):
        directions = {
            'n': {'line': -1, 'column':  0},
            'e': {'line':  0, 'column':  1},
            's': {'line':  1, 'column':  0},
            'w': {'line':  0, 'column': -1}
        }

        if self._root is None:      # If there is no root it enters the 'hunt mode'
            self._start_the_hunt(line, column, directions)
        else:                       # continues to hunt
            self._continue_the_hunt(line, column, directions)

    def shoot(self, line=None, column=None):

        message, coords = super().shoot()
        line = coords[0]
        column = coords[1]
        if 'sunk' in message.lower():
            self._priority.clear()              # clear the priority queue  <=> exit the hunt mode
            self._root = None                   # clear the root            <=> exit the hunt mode
            if not Rules().can_touch:
                self._ship_positions.append({'line': line, 'column': column})
                self._create_border_of_sunken_ship()        # if the ships cannot touch, in the case of a sunken ship, all the cells around it are cleared from the available positions
                self._ship_positions.clear()
        elif 'hit' in message.lower():
            self._hunt(line, column)
            if not Rules().can_touch:
                self._ship_positions.append({'line': line, 'column': column})

        return message, (line, column)

    def _create_border_of_sunken_ship(self):
        """
        Clears all the cells near a sunken ships from the available positions set
        :return:
        """
        directions = {
            'n':    {'line': -1, 'column': 0},
            'ne':   {'line': -1, 'column': 1},
            'e':    {'line': 0, 'column': 1},
            'se':   {'line': 1, 'column': 1},
            's':    {'line': 1, 'column': 0},
            'sw':   {'line': 1, 'column': -1},
            'w':    {'line': 0, 'column': -1},
            'nw':   {'line': -1, 'column': -1}
        }
        for position in self._ship_positions:
            line = position['line']
            column = position['column']

            for direction in directions:
                next_line = line + directions[direction]['line']
                next_column = column + directions[direction]['column']
                try:
                    self._available_positions.remove((next_line, next_column))
                except KeyError:
                    pass

        self._ship_positions.clear()
