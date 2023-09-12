from business.player import Player
from errors import ServiceError
from persistence.rules import Rules


class HumanPlayer(Player):

    def are_all_placed(self):
        """ Checks if all the ships are already placed """
        return self._own_board.ships_left['destroyer'] == Rules().number_of['destroyer'] and \
            self._own_board.ships_left['cruiser'] == Rules().number_of['cruiser'] and \
            self._own_board.ships_left['submarine'] == Rules().number_of['submarine'] and \
            self._own_board.ships_left['battleship'] == Rules().number_of['battleship'] and \
            self._own_board.ships_left['carrier'] == Rules().number_of['carrier']

    def unplaced_ships(self):
        """ Returns a list with the names of the ships that are not placed (and their abbreviation) """
        unplaced_ships = []

        if self._own_board.ships_left['destroyer'] < Rules().number_of['destroyer']:
            unplaced_ships.append('d / destroyer')
        if self._own_board.ships_left['cruiser'] < Rules().number_of['cruiser']:
            unplaced_ships.append('c / cruiser')
        if self._own_board.ships_left['submarine'] < Rules().number_of['submarine']:
            unplaced_ships.append('s / submarine')
        if self._own_board.ships_left['battleship'] < Rules().number_of['battleship']:
            unplaced_ships.append('b / battleship')
        if self._own_board.ships_left['carrier'] < Rules().number_of['carrier']:
            unplaced_ships.append('a / (aircraft) carrier')

        return unplaced_ships

    def get_own_board(self):
        """
        Returns the values of the own board
        """
        values = self._own_board.values
        return values

    def get_opponent_board(self):
        """
        Returns the values of the own board, the positions of the ships are being hidden
        """
        values = self._opponent_board.values
        hidden_values = ['0' if val[0] in ['a', 'b', 'c', 'd', 's'] else val for val in values]
        return hidden_values

    def unveil_opponent_board(self):
        """
        Returns the values of the own board, the positions of the ships are no longer hidden
        """
        values = self._opponent_board.values
        return values

    def clear_ship(self, ship_type):
        """
        Clears a ship off the board
        """
        available_ships_types = ['destroyer', 'cruiser', 'submarine', 'battleship', 'carrier']
        # in gui placement previews
        if ship_type not in available_ships_types:
            raise ServiceError("Invalid ship type!")
        self._own_board.clear_ship(ship_type)
