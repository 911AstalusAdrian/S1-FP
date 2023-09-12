from engines.beginner import BeginnerAI
from engines.easy import EasyAI
from engines.hard import HardAI
from engines.medium import MediumAI
from errors import ServiceError
from persistence.rules import Rules
from presentation.gui.GUIBoard import GUIBoard
import tkinter as tk
from tkinter import messagebox

from statistics.place_statistics import PlaceStatistics


class GUIShootingPh:

    def __init__(self, master, main_frame, player, ai):
        self.__master = master
        self.__main_frame = main_frame
        self.__player = player
        self.__ai = ai

        self.__clear_frame(self.__main_frame)
        self.__board = None

        self._shots_taken = 0

        self.__display_level()

        if self._should_display_probability():
            self._top_win = tk.Toplevel(self.__master)

    def __display_level(self):
        self.__master.title(f'Battleships ({self.__get_level().capitalize()})')

    def __get_level(self):
        if isinstance(self.__ai, BeginnerAI):
            return 'beginner'
        if isinstance(self.__ai, MediumAI):
            return 'medium'
        if isinstance(self.__ai, EasyAI):
            return 'easy'
        if isinstance(self.__ai, HardAI):
            return 'hard'

    def assembly(self):
        left_side_frame = tk.Frame(self.__main_frame)
        right_side_frame = tk.Frame(self.__main_frame)

        left_side_frame.grid(row=0, column=0, sticky="nesw")
        right_side_frame.grid(row=0, column=1, sticky="nesw")

        self.__main_frame.grid_rowconfigure(0, weight=1)
        self.__main_frame.grid_columnconfigure(0, weight=1, minsize=500)
        self.__main_frame.grid_columnconfigure(1, weight=1, minsize=500)

        self.__own_board = GUIBoard(left_side_frame)
        self.__own_board.pack(expand=1, fill=tk.BOTH)
        self.__own_board.display(self.__player.get_own_board())

        self.__opponent_board = GUIBoard(right_side_frame, button_command=self._shoot_button_command)
        self.__opponent_board.pack(expand=1, fill=tk.BOTH)
        self.__opponent_board.display(self.__player.get_opponent_board())

        if Rules().test:
            self._test()

    def _test(self):
        while True:
            self.__ai.shoot()
            self._shots_taken += 1
            if self.__ai.won():
                self.__opponent_board.display(self.__player.unveil_opponent_board())
                self.__own_board.display(self.__player.get_own_board())
                # messagebox.showerror("", f"You lost! (in {self._shots_taken} shots)")
                file = self.__get_level()
                PlaceStatistics().write_to_file(file, str(self._shots_taken))
                self.__master.destroy()
                return
            self.__own_board.display(self.__player.get_own_board())
            self.__opponent_board.display(self.__player.get_opponent_board())

    def _shoot_button_command(self, row, col, event):

        try:
            self.__player.shoot(row, col)
        except ServiceError:
            return

        if self.__player.won():
            self.__opponent_board.display(self.__player.unveil_opponent_board())
            self.__own_board.display(self.__player.get_own_board())
            messagebox.showinfo("", f"You won! (in {self._shots_taken} shots)")
            if self._should_display_probability():
                self._top_win.destroy()
            self.__master.quit()
            return

        self.__ai.shoot()
        self._shots_taken += 1

        if self.__ai.won():
            self.__opponent_board.display(self.__player.unveil_opponent_board())
            self.__own_board.display(self.__player.get_own_board())
            messagebox.showerror("", f"You lost! (in {self._shots_taken} shots)")
            if self._should_display_probability():
                self._top_win.destroy()
            self.__master.quit()

        self.__own_board.display(self.__player.get_own_board())
        self.__opponent_board.display(self.__player.get_opponent_board())

        if self._should_display_probability():
            self._top_win.destroy()
            self._display_the_probabilities()

    def _should_display_probability(self):
        return isinstance(self.__ai, HardAI) and Rules().display_probability

    def _display_the_probabilities(self):
        self._top_win = tk.Toplevel(self.__master)
        self._top_win.geometry('500x500')
        self._top_win.minsize(500, 500)
        values = self.__ai.score_board
        prob_board = GUIBoard(self._top_win)
        prob_board.pack(expand=1, fill=tk.BOTH)
        prob_board.display_probability(values)
        self._top_win.mainloop()

    @staticmethod
    def __clear_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()
