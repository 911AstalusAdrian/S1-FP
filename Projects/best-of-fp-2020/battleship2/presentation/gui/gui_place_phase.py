
import tkinter as tk

from engines.beginner import BeginnerAI
from engines.easy import EasyAI
from engines.hard import HardAI
from engines.medium import MediumAI
from errors import ServiceError
from persistence.last_board_config import LastBoardConfig
from persistence.rules import Rules
from presentation.gui.GUIBoard import GUIBoard
from presentation.gui.GUIShipPosition import GUIShipPosition
from presentation.gui.gui_shooting_phase import GUIShootingPh


class GUIPlacePh:

    def __init__(self, master, main_frame, player, ai):
        self.__master = master
        self.__main_frame = main_frame
        self.__player = player
        self.__ai = ai

        self.__clear_frame(self.__main_frame)
        self.__board = None

        self.__display_level()

        self.__board_config = LastBoardConfig()

    def assembly(self):
        left_side_frame = tk.Frame(self.__main_frame)
        right_side_frame = tk.Frame(self.__main_frame)

        left_side_frame.grid(row=0, column=0, sticky="nesw")
        right_side_frame.grid(row=0, column=1, sticky="nesw")

        self.__main_frame.grid_rowconfigure(0, weight=1)
        self.__main_frame.grid_columnconfigure(0, weight=1, minsize=500)
        self.__main_frame.grid_columnconfigure(1, weight=1, minsize=500)

        self.__board = GUIBoard(left_side_frame)
        self.__board.pack(expand=1, fill=tk.BOTH)
        self._assembly_right_side(right_side_frame)

        if Rules().test:
            self.__go_to_shooting()

    def __display_level(self):
        if isinstance(self.__ai, BeginnerAI):
            self.__master.title('Battleships (Beginner)')
        if isinstance(self.__ai, MediumAI):
            self.__master.title('Battleships (Medium)')
            return
        if isinstance(self.__ai, EasyAI):
            self.__master.title('Battleships (Easy)')
        if isinstance(self.__ai, HardAI):
            self.__master.title('Battleships (Hard)')

    def _assembly_right_side(self, right_side_frame):
        right_side_frame.grid_columnconfigure(0, weight=1)
        right_side_frame.grid_rowconfigure(0, weight=1)
        right_side_frame.grid_rowconfigure(1, weight=1)
        right_side_frame.grid_rowconfigure(2, weight=1)
        right_side_frame.grid_rowconfigure(3, weight=1)
        right_side_frame.grid_rowconfigure(4, weight=1)
        right_side_frame.grid_rowconfigure(5, weight=1)

        self.__destroyer = GUIShipPosition(right_side_frame, 'Destroyer (length = 2)', self.__preview_destroyer,
                                           self.__board_config.get_position('destroyer'), self.__board_config.get_orientation('destroyer'))
        self.__submarine = GUIShipPosition(right_side_frame, 'Submarine (length = 3)', self.__preview_submarine,
                                           self.__board_config.get_position('submarine'), self.__board_config.get_orientation('submarine'))
        self.__cruiser = GUIShipPosition(right_side_frame, 'Cruiser (length = 3)', self.__preview_cruiser,
                                         self.__board_config.get_position('cruiser'), self.__board_config.get_orientation('cruiser'))
        self.__battleship = GUIShipPosition(right_side_frame, 'Battleship (length = 4)', self.__preview_battleship,
                                            self.__board_config.get_position('battleship'), self.__board_config.get_orientation('battleship'))
        self.__carrier = GUIShipPosition(right_side_frame, 'Aircraft carrier (length = 5)', self.__preview_carrier,
                                         self.__board_config.get_position('carrier'), self.__board_config.get_orientation('carrier'))
        next_but = tk.Button(right_side_frame, text='Next', command=self.__go_to_shooting)

        self.__destroyer.grid(row=0, column=0, sticky="nesw", padx=20, pady=5)
        self.__submarine.grid(row=1, column=0, sticky="nesw", padx=20, pady=5)
        self.__cruiser.grid(row=2, column=0, sticky="nesw", padx=20, pady=5)
        self.__battleship.grid(row=3, column=0, sticky="nesw", padx=20, pady=5)
        self.__carrier.grid(row=4, column=0, sticky="nesw", padx=20, pady=5)
        next_but.grid(row=5, column=0, sticky="nesw", padx=100, pady=5)

    def __go_to_shooting(self):
        ships = {'destroyer': self.__destroyer,
                 'cruiser': self.__cruiser,
                 'submarine': self.__submarine,
                 'battleship': self.__battleship,
                 'carrier': self.__carrier}

        all_placed = True

        for ship_type in ships:
            all_placed &= self.__gui_place(ship_type, ships[ship_type], clear=False)

        if not all_placed:
            return

        self.__ai.place_all_ships()

        GUIShootingPh(self.__master, self.__main_frame, self.__player, self.__ai).assembly()

    def __preview_destroyer(self):
        self.__gui_place('destroyer', self.__destroyer)

    def __preview_cruiser(self):
        self.__gui_place('cruiser', self.__cruiser)

    def __preview_submarine(self):
        self.__gui_place('submarine', self.__submarine)

    def __preview_battleship(self):
        self.__gui_place('battleship', self.__battleship)

    def __preview_carrier(self):
        self.__gui_place('carrier', self.__carrier)

    def __gui_place(self, ship_type, ship, clear=True):
        self.__player.clear_ship(ship_type)

        coords = ship.start_position.strip().upper()

        try:
            line = ord(coords[0]) - ord('A') + 1
            column = int(coords[1:])
        except ValueError:
            ship.error = 'Not a valid position!'
            return False
        except IndexError:
            ship.error = 'Not a valid position!'
            return False
        orientation = ship.orientation.strip().lower()

        try:
            line = int(line)
            column = int(column)

            self.__player.place_ship(ship_type, line, column, orientation)
            self.__board_config.set_config({ship_type: {'position': ship.start_position, 'orientation': ship.orientation}})
        except ServiceError as serv_err:
            ship.error = serv_err
            return False
        except KeyError:
            ship.error = 'The chosen ship is not an option!'
            return False
        except ValueError as val_err:
            ship.error = val_err
            return False

        self._refresh_board()
        ship.error = ''
        return True

    def _refresh_board(self):
        values = self.__player.get_own_board()
        self.__board.display(values)

    @staticmethod
    def __clear_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()
