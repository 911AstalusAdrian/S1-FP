import tkinter as tk

from business.human import HumanPlayer
from domain.board import Board
from presentation.gui.gui_select_phase import GUISelectPh


class GUI:

    def __init__(self):
        self.__player_board = Board()
        self.__ai_board = Board()
        self.__player = HumanPlayer(self.__player_board, self.__ai_board)

        self.__master = tk.Tk()
        self.__master.geometry('1000x500')
        self.__master.minsize(1000, 500)
        self.__master.title('Battleships')

        self.__main_frame = tk.Frame(master=self.__master)
        self.__main_frame.pack(padx=5, pady=5, expand=1, fill=tk.BOTH)

        select_phase = GUISelectPh(self.__master, self.__main_frame, self.__ai_board, self.__player_board, self.__player)
        select_phase.assembly()

    def run(self):
        self.__master.mainloop()
