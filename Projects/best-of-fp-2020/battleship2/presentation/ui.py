from business.human import HumanPlayer
from domain.board import Board
from engines.ai import AI
from engines.easy import EasyAI
from engines.hard import HardAI
from engines.medium import MediumAI
from engines.beginner import BeginnerAI
from errors import ServiceError
from colorama import Fore, Back, Style

from persistence.last_board_config import LastBoardConfig


class UI:

    def __init__(self):
        self.__player_board = Board()
        self.__ai_board = Board()

        self.__player = HumanPlayer(self.__player_board, self.__ai_board)
        self.__ai = AI(self.__ai_board, self.__player_board)

    def run(self):
        while True:
            self._rules_select()
            self._level_select()
            self._placement_phase()
            self._shooting_phase()
            again = input("Go again? (y/n)")
            if again.lower().strip() == 'n':
                return

    @staticmethod
    def _make_colored_cell(value, style='normal'):
        """ Prints a cell in a given style """
        styles = {
            'normal':   {'foreground': Style.RESET_ALL, 'background': ''},
            'occupied': {'foreground': Fore.BLACK, 'background': Back.BLUE},
            'hit':      {'foreground': Fore.BLACK, 'background': Back.YELLOW},
            'missed':   {'foreground': Fore.BLACK, 'background': Back.RED},
            'sunk':     {'foreground': Fore.BLACK, 'background': Back.MAGENTA}
        }
        style = 'normal' if value == '0' else \
                'occupied' if value[0] in ['a', 'b', 'c', 'd', 's'] else \
                'hit' if value == '+' else \
                'missed' if value == '-' else \
                'sunk' if value == '*' else 'normal'
        return styles[style]['foreground'] + styles[style]['background'] + '   ' + Style.RESET_ALL

    def _print_board(self, player='player'):
        # TODO better this
        values = self.__player.get_own_board() if player == 'player' else \
            self.__player.get_opponent_board() if player == 'ai' else \
            self.__player.unveil_opponent_board()

        if values is None:
            print('Some error!')
            return

        print(end='\t|| ')
        for i in range(10):
            print(i + 1, end=' | ' if i < 9 else ' |\n')
        print(end='====||=')
        for i in range(10):
            print(end='====' if i < 9 else '===|')

        print()
        for i in range(10):
            print(chr(ord('A') + i), end='\t||')
            for j in range(10):
                cell = i*10 + j
                print(self._make_colored_cell(values[cell]), end='|' if j < 9 else ' |\n')
            print(end='----||-')
            for j in range(9):
                print('-', end='-+-' if i < 9 else '---')
            print('--', end='-|\n')

    def _print_both_boards(self, end=False):
        human_values = self.__player.get_own_board()
        ai_values = self.__player.get_opponent_board() if end is False else self.__player.unveil_opponent_board()

        if human_values is None or ai_values is None:
            print('Some error!')
            return

        print("Opponent board:\t\t\t\t\t\t\t\t\t\tOwn board:")
        print(end='\t|| ')
        for i in range(10):  # Opponent board column headers
            print(i + 1, end=' | ' if i < 9 else ' |\t\t')
        print(end='\t|| ')
        for i in range(10):  # Own board column headers
            print(i + 1, end=' | ' if i < 9 else ' |\n')
        print(end='====||=')  # Opponent board header separator
        for i in range(10):
            print(end='====' if i < 9 else '===|\t\t')
        print(end='====||=')  # Own board header separator
        for i in range(10):
            print(end='====' if i < 9 else '===|\n')

        for i in range(10):
            print(chr(ord('A') + i), end='\t||')   # Opponent board line headers
            for j in range(10):                     # Opponent board values
                cell = i * 10 + j
                print(self._make_colored_cell(ai_values[cell]), end='|' if j < 9 else ' |\t\t')
            print(chr(ord('A') + i), end='\t||')   # Own board line headers
            for j in range(10):                     # Own board values
                cell = i * 10 + j
                print(self._make_colored_cell(human_values[cell]), end='|' if j < 9 else ' |\n')
            print(end='----||-')                    # Opponent board line separator
            for j in range(9):
                print('-', end='-+-' if i < 9 else '---')
            print('--', end='-|\t\t')
            print(end='----||-')                    # Own board line separator
            for j in range(9):
                print('-', end='-+-' if i < 9 else '---')
            print('--', end='-|\n')

    def _level_select(self):
        print('Select level:')
        print('1. Beginner')
        print('2. Easy')
        print('3. Medium')
        print('4. Hard')

        while True:
            level = input('Choose level (1/2/3/4): ').strip()
            if level == '1':
                self.__ai = BeginnerAI(self.__ai_board, self.__player_board)
                return
            if level == '2':
                self.__ai = EasyAI(self.__ai_board, self.__player_board)
                return
            if level == '3':
                self.__ai = MediumAI(self.__ai_board, self.__player_board)
                return
            if level == '4':
                self.__ai = HardAI(self.__ai_board, self.__player_board)
                return
            else:
                print("Unavailable level!")

    def __preset_placement(self):
        config = LastBoardConfig()
        ships = ['destroyer', 'submarine', 'cruiser', 'battleship', 'carrier']
        for ship in ships:
            position = config.get_position(ship)
            orientation = config.get_orientation(ship)
            self.__player.place_ship(ship, ord(position[0].upper())-ord('A'), int(position[1]), orientation)

    def _placement_phase(self):
        """
        The human player chooses the positioning of the ships and the AI randomises them
        """
        self.__ai.place_all_ships()

        yes = input("Use preset placement? (y/n): ")
        if yes.lower() in 'yes':
            self.__preset_placement()

        while not self.__player.are_all_placed():

            not_placed_ships = self.__player.unplaced_ships()

            print()
            self._print_board()
            for ship in not_placed_ships:
                print(ship)

            ship_type = input('Ship: ').strip().lower()
            coords = input("Coordinates: ").strip().upper()

            try:
                line = ord(coords[0]) - ord('A') + 1
                column = int(coords[1:])
            except ValueError:
                print('Not a valid position!')
                continue
            orientation = input('Orientation ((1/h/horizontal) / (2/v/vertical)): ').strip().lower()

            if ship_type == 'd':
                ship_type = 'destroyer'
            if ship_type == 's':
                ship_type = 'submarine'
            if ship_type == 'c':
                ship_type = 'cruiser'
            if ship_type == 'b':
                ship_type = 'battleship'
            if ship_type == 'a':
                ship_type = 'carrier'

            if orientation == '1' or orientation == '' or orientation == 'h':
                orientation = 'horizontal'
            elif orientation == '2' or orientation == 'v':
                orientation = 'vertical'

            try:
                line = int(line)
                column = int(column)

                self.__player.place_ship(ship_type, line, column, orientation)
            except ServiceError as serv_err:
                print(serv_err)
            except KeyError:
                print('The chosen ship is not an option!')
            except ValueError as val_err:
                print(val_err)

    def _shooting_phase(self):

        while True:
            self._print_both_boards()

            coords = input("Shoot: ").strip().upper()

            try:
                line = ord(coords[0]) - ord('A') + 1
                column = int(coords[1:])
            except ValueError:
                print('Not a valid position!')
                continue

            try:
                message = self.__player.shoot(line, column)
                print('You: ' + message)
            except ServiceError as err:
                print(err)
                continue

            if self.__player.won():
                self._print_both_boards(end=True)
                print('YOU WON!')
                return

            message = self.__ai.shoot()[0]
            print('Ai:  ' + message)

            if self.__ai.won():
                self._print_both_boards(end=True)
                print('YOU LOST!')
                return

    def _rules_select(self):
        pass
