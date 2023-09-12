from persistence.rules import Rules
import queue


class Board:
    """
    The game board
        10x10 grid
        Each cell has one of the following states:
             0 = empty
             - = shot and missed
             + = shot and hit
             * = shot and sunk
             d = destroyer
             c = cruiser
             s = submarine
             b = battleship
             a = aircraft carrier

    ! lines and columns are numbered from 1 to 10
    """

    def __init__(self):
        self._board = ['0']*(Rules().edge * Rules().edge)
        self._hp = {
            'destroyer': [2] * Rules().number_of['destroyer'],
            'cruiser': [3] * Rules().number_of['cruiser'],
            'submarine': [3] * Rules().number_of['submarine'],
            'battleship': [4] * Rules().number_of['battleship'],
            'carrier': [5] * Rules().number_of['carrier']
        }
        self._ships_left = {
            'destroyer': 0,
            'cruiser': 0,
            'submarine': 0,
            'battleship': 0,
            'carrier': 0
        }
        self.__next_in_orientation = {
            'n': {'line': -1, 'column':  0},
            'e': {'line':  0, 'column':  1},
            's': {'line':  1, 'column':  0},
            'w': {'line':  0, 'column': -1},
        }

        self._last_shot_success = ''

    @property
    def last_shot_success(self):
        """
            '' - if there was no last shot
            'hit' - if the last shot was a hit
            'sunk' - if the last shot sunk a ship
            'miss' - if the last shot missed
        """
        return self._last_shot_success

    @property
    def hp(self):
        """
        Returns the remaining health of the ships
        :returns dictionary
            available keys: destroyer, cruiser, submarine, battleship, carrier
        """
        return self._hp

    @property
    def ships_left(self):
        """
        The number of ships left of each type
        :return: dictionary
            available keys: destroyer, cruiser, submarine, battleship, carrier
        """
        return self._ships_left

    @property
    def values(self):
        """
        Gets all the values from the board if form of a list
        """
        return self._board[:]

    def is_ship(self, line, column):
        """
        Checks if the cell on the given line and column contains a ship part
        :return: True if so, False otherwise
        """
        return self._board[self._compute_cell(line, column)][0] in ['a', 'b', 'c', 'd', 's']

    def _compute_cell(self, line, column):
        """
        * Internal method
        Composes the cell in the array from the given line and column, both indexed from 1
        """
        return (line - 1) * Rules().edge + (column - 1)

    def place_ship(self, ship_type, start_line, start_column, orientation):
        """
        Places a ship of type 'ship_type' on the board starting with the coordinates ('start_line', 'start_column')
        and heading in the direction 'orientation'
        :param ship_type: [destroyer, cruiser, submarine, battleship, carrier]
        :param start_line:
        :param start_column:
        :param orientation: [n, e, s, w] - str
        :return:
        """
        # Use the dictionary to get the corresponding character for the specified ship type
        # Fill the cells for the ship with a string formed of the character and the number of the ship
        # (how many ships of the same type were already placed)

        type_dictionary = {
            'destroyer':    {'length': 2, 'character': 'd'},
            'cruiser':      {'length': 3, 'character': 'c'},
            'submarine':    {'length': 3, 'character': 's'},
            'battleship':   {'length': 4, 'character': 'b'},
            'carrier':      {'length': 5, 'character': 'a'}
        }

        ship_type = ship_type.lower()
        orientation = orientation.lower()

        current_line = start_line
        current_column = start_column
        for i in range(type_dictionary[ship_type]['length']):
            cell = self._compute_cell(current_line, current_column)
            self._board[cell] = type_dictionary[ship_type]['character'] + str(self._ships_left[ship_type])
            current_line += self.__next_in_orientation[orientation]['line']
            current_column += self.__next_in_orientation[orientation]['column']
        self._ships_left[ship_type] += 1

    def already_shot(self, line, column):
        """
        Returns True if the cell was already shot or False otherwise
        """
        cell = self._compute_cell(line, column)
        return self._board[cell] in ['-', '+', '*']

    def empty(self, line, column):
        """
        Returns True if the cell is empty or False otherwise
        """
        cell = self._compute_cell(line, column)
        return self._board[cell] == '0'

    def _hit_ship(self, cell):
        """
        Hits the ship on the given cell:
            the hp decreases with one
            the state becomes '+'
        :returns 'sunk' if the left hp is 0 and 'hit' otherwise
        """
        symbol_to_name = {
            'd': 'destroyer',
            'c': 'cruiser',
            's': 'submarine',
            'b': 'battleship',
            'a': 'carrier'
        }

        ship = symbol_to_name[self._board[cell][0]]
        ship_number = int(self._board[cell][1])
        self._hp[ship][ship_number] -= 1
        self._board[cell] = '+'

        if self._hp[ship][ship_number] == 0:
            self._ships_left[ship] -= 1
            self._last_shot_success = f"sunk '{ship}'"
        else:
            self._last_shot_success = 'hit'

    def shoot(self, line, column):
        """
        Take a shot on a cell
        """

        cell = self._compute_cell(line, column)
        state = self._board[cell]
        if state == '0':            # there is nothing to hit
            self._board[cell] = '-'
            self._last_shot_success = 'miss'
        else:
            self._hit_ship(cell)

    def sink_ship(self, line, column):
        """
        Sinks the ship that has a part on the given cell
        """
        # Transforms the + on the cell into a *-for sunken ships
        # search the next part of the ship (neighbour +'s)

        if self._board[self._compute_cell(line, column)] != '+':
            raise ValueError("Not ok!")

        to_check = queue.SimpleQueue()
        to_check.put({'line': line, 'column': column})

        while not to_check.empty():
            coords = to_check.get()
            line = coords['line']
            column = coords['column']

            self._board[self._compute_cell(line, column)] = '*'

            for direction in self.__next_in_orientation:
                next_line = line + self.__next_in_orientation[direction]['line']
                next_column = column + self.__next_in_orientation[direction]['column']
                next_cell = self._compute_cell(next_line, next_column)

                try:
                    if self._board[next_cell] == '+':
                        to_check.put({'line': next_line, 'column': next_column})
                except IndexError:
                    pass

    def clear_ship(self, ship_type):
        """
        Clears a ship off the board
        """
        # in gui placement previews
        key = 'a' if ship_type == 'carrier' else ship_type[0]

        ship_found = False
        for i in range(100):
            if self._board[i][0] == key:
                ship_found = True
                self._board[i] = '0'

        # self._board = [val if val[0] != key else '0' for val in self._board]

        if ship_found:
            self._ships_left[ship_type] -= 1

    def __eq__(self, other):
        """ Compares the board with a list resembling the arrangement of the pieces in the board """
        return self._board == other
