
import tkinter as tk

from engines.ai import AI
from engines.easy import EasyAI
from engines.hard import HardAI
from engines.medium import MediumAI
from engines.beginner import BeginnerAI
from persistence.rules import Rules
from presentation.gui.gui_place_phase import GUIPlacePh


class GUISelectPh:

    def __init__(self, master, main_frame, ai_board, player_board, player):
        self.__master = master
        self.__main_frame = main_frame
        self.__player_board = player_board
        self.__ai_board = ai_board
        self.__player = player

        self.__ai = AI(self.__ai_board, self.__player_board)
        
        self.__clear_frame(self.__main_frame)

    def assembly(self):
        secondary_frame = tk.Frame(self.__main_frame)
        secondary_frame.pack(padx=250, pady=20, expand=1, fill=tk.BOTH)

        tk.Label(secondary_frame, text="Select AI level", font='Default 50').pack()

        beginner_but = tk.Button(secondary_frame, text='Beginner', command=self.__select_beginner)
        easy_but = tk.Button(secondary_frame, text='Easy', command=self.__select_easy)
        medium_but = tk.Button(secondary_frame, text='Medium', command=self.__select_medium)
        hard_but = tk.Button(secondary_frame, text='Hard', command=self.__select_hard)

        beginner_but.pack(expand=1, fill=tk.BOTH, pady=(30, 10), padx=100)
        easy_but.pack(expand=1, fill=tk.BOTH, pady=(10, 10), padx=100)
        medium_but.pack(expand=1, fill=tk.BOTH, pady=(10, 10), padx=100)
        hard_but.pack(expand=1, fill=tk.BOTH, pady=(10, 30), padx=100)

        if Rules().test:
            levels = {
                1: self.__select_beginner,
                2: self.__select_easy,
                3: self.__select_medium,
                4: self.__select_hard
            }
            levels[Rules().difficulty]()

    def __select_beginner(self):
        self.__ai = BeginnerAI(self.__ai_board, self.__player_board)
        GUIPlacePh(self.__master, self.__main_frame, self.__player, self.__ai).assembly()

    def __select_easy(self):
        self.__ai = EasyAI(self.__ai_board, self.__player_board)
        GUIPlacePh(self.__master, self.__main_frame, self.__player, self.__ai).assembly()

    def __select_medium(self):
        self.__ai = MediumAI(self.__ai_board, self.__player_board)
        GUIPlacePh(self.__master, self.__main_frame, self.__player, self.__ai).assembly()

    def __select_hard(self):
        self.__ai = HardAI(self.__ai_board, self.__player_board)
        GUIPlacePh(self.__master, self.__main_frame, self.__player, self.__ai).assembly()

    @staticmethod
    def __clear_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()
