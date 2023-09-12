from domain.board import Board
from errors import ServiceError
from persistence.rules import Rules


class Player:

    def __init__(self, own_board: Board, opponent_board: Board):
        self._own_board = own_board
        self._opponent_board = opponent_board
        self._edge_size = Rules().edge

    def _check_position(self, start_line, start_column, end_line, end_column):
        """
        Checks if the ship is in the bounds of the 10x10 board
        """
        if not 1 <= start_line <= self._edge_size:
            raise ServiceError('Ship not in bounds!')
        if not 1 <= start_column <= self._edge_size:
            raise ServiceError('Ship not in bounds!')
        if not 1 <= end_line <= self._edge_size:
            raise ServiceError('Ship not in bounds!')
        if not 1 <= end_column <= self._edge_size:
            raise ServiceError('Ship not in bounds!')

    def _check_overlapping(self, length, current_line, current_column, orientation='horizontal'):
        """
        Checks if the ship doesn't overlap an already placed one
        """
        next_in_orientation = {
            'horizontal': {'line': 0, 'column': 1},
            'vertical': {'line': 1, 'column': 0},
        }
        for i in range(length):
            if not self._own_board.empty(current_line, current_column):
                raise ServiceError("Ships cannot overlap!")

            current_line += next_in_orientation[orientation]['line']
            current_column += next_in_orientation[orientation]['column']

    def _would_touch(self, line, column):
        """
        Checks if, in case there was a ship part placed on the given cell, it would touch another ship
        """
        result = self._own_board.empty(line-1, column) if line > 1 else True
        result = result and (self._own_board.empty(line-1, column+1) if (line > 1 and column < self._edge_size) else True)
        result = result and (self._own_board.empty(line, column+1) if column < self._edge_size else True)
        result = result and (self._own_board.empty(line+1, column+1) if (line < self._edge_size and column < self._edge_size) else True)
        result = result and (self._own_board.empty(line+1, column) if line < self._edge_size else True)
        result = result and (self._own_board.empty(line+1, column-1) if (column > 1 and line < self._edge_size) else True)
        result = result and (self._own_board.empty(line, column-1) if column > 1 else True)
        result = result and (self._own_board.empty(line-1, column-1) if (line > 1 and column > 1) else True)
        return not result

    def _check_touching(self, length, current_line, current_column, orientation='horizontal'):
        """
        Checks if the ship doesn't touch an already placed one
        """
        next_in_orientation = {
            'horizontal': {'line': 0, 'column': 1},
            'vertical': {'line': 1, 'column': 0},
        }
        for i in range(length):
            if self._would_touch(current_line, current_column):
                raise ServiceError("Ships cannot touch!")

            current_line += next_in_orientation[orientation]['line']
            current_column += next_in_orientation[orientation]['column']

    def won(self):
        """
        Checks if the player won:
            all the opponent's ships are destroyed <=> all the values in the dict are false
        """
        return self._opponent_board.ships_left['destroyer'] == 0 and self._opponent_board.ships_left['cruiser'] == 0 and \
            self._opponent_board.ships_left['submarine'] == 0 and self._opponent_board.ships_left['battleship'] == 0 and \
            self._opponent_board.ships_left['carrier'] == 0

    def place_ship(self, ship_type, line, column, orientation='horizontal'):
        """
        Places a ship
        :param ship_type: [destroyer, cruiser, submarine, battleship, carrier]
        :param line: starting line
        :param column: starting column
        :param orientation: horizontal(default) / vertical
        """
        length_dictionary = {
            'destroyer': 2,
            'cruiser': 3,
            'submarine': 3,
            'battleship': 4,
            'carrier': 5
        }
        ship_type = ship_type.lower().strip()

        if self._own_board.ships_left[ship_type] == Rules().number_of[ship_type]:
            raise ServiceError(f"Ship '{ship_type}' is already placed!")

        orientation = orientation.lower().strip()

        start_line = line
        start_column = column
        end_line = line if orientation == 'horizontal' else line + length_dictionary[ship_type] - 1
        end_column = column if orientation == 'vertical' else column + length_dictionary[ship_type] - 1

        self._check_position(start_line, start_column, end_line, end_column)
        self._check_overlapping(length_dictionary[ship_type], start_line, start_column, orientation)
        if not Rules().can_touch:
            self._check_touching(length_dictionary[ship_type], start_line, start_column, orientation)

        directional_orientation = 's' if orientation == 'vertical' else 'e'

        self._own_board.place_ship(ship_type, start_line, start_column, directional_orientation)

    def shoot(self, line, column):
        """
        Takes a shot
        :return: a message confirming whether the shot was missed or hit
        """
        if not (1 <= line <= 10 and 1 <= column <= 10):
            raise ServiceError("Position out of bounds!")

        if self._opponent_board.already_shot(line, column):
            raise ServiceError("Cannot shoot in the same place two times!")

        self._opponent_board.shoot(line, column)

        message = self._opponent_board.last_shot_success.capitalize() + '!'
        if 'sunk' in message.lower():
            self._opponent_board.sink_ship(line, column)

        return message
