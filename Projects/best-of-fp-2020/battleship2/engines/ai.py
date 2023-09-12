from random import randint, choice

from business.player import Player
from errors import ServiceError
from persistence.rules import Rules


class AI(Player):
    """
    The base class for all AI classes
    Contains the basic methods:
    """

    def __init__(self, own_board, opponent_board):
        super().__init__(own_board, opponent_board)
        self._edge_length = Rules().edge
        self._available_positions = self._compute_available_positions()

    def _compute_available_positions(self):
        """
        Computes a set of the available positions for the ai to shoot (initially are all the cells in the board)
        """
        return {(x + 1, y + 1) for x in range(self._edge_length) for y in range(self._edge_length)}

    def place_all_ships(self):
        """
        Places all the ships
        """
        available_ships = {'destroyer': Rules().number_of['destroyer'],
                           'cruiser': Rules().number_of['cruiser'],
                           'submarine': Rules().number_of['submarine'],
                           'battleship': Rules().number_of['battleship'],
                           'carrier': Rules().number_of['carrier']}
        all_placed = False
        while not all_placed:                       # While not all the ships are placed try to place each one that has not been already
            for ship in available_ships:
                if available_ships[ship] == 0:      # If all the ships of that type are already placed, continue with the next one
                    continue

                while True:                         # Keeps trying to place a ship on a random position with a random orientation
                    line = randint(1, self._edge_length)
                    column = randint(1, self._edge_length)
                    orientation = choice(['horizontal', 'vertical'])

                    try:                            # If there are no errors while placing do so, else retry with other random parameters
                        self.place_ship(ship, line, column, orientation)
                        available_ships[ship] -= 1
                        break
                    except ServiceError:
                        pass

                all_placed = available_ships['destroyer'] == 0 and available_ships['cruiser'] == 0 and available_ships['submarine'] == 0 \
                    and available_ships['battleship'] == 0 and available_ships['carrier'] == 0

    def _compute_target_coords(self):
        """
        Computes the target's (cell that will get shot) coordinates (line, column)
        """
        return None, None

    def shoot(self, line=None, column=None):
        while True:
            line, column = self._compute_target_coords()
            try:                                    # If there appears no error while taking the shot, do so, else retry
                message = super().shoot(line, column)
                return message, (line, column)
            except ServiceError:
                pass
