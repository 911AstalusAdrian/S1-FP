import tkinter as tk
from tkinter.messagebox import askyesno, showinfo


class GUI:
    def __init__(self, game):
        self._window = tk.Tk()
        self._game = game
        self._human_first = True
        self._buttons = []
        self._game_finished = False
        self._window.title("Gomoku")
        self.create_widgets()

    def check_game_state(self, human_move, winning_move):
        human_win = None

        if winning_move is True:
            human_win = 1 if human_move is True else -1
        elif self._game.is_draw() is True:
            human_win = 0

        if human_win == 1:
            showinfo(title="Game over!", message="You won!")
        elif human_win == -1:
            showinfo(title="Game over!", message="I won!")
        elif human_win == 0:
            showinfo(title="Game over!", message="It's a tie!")

        if human_win is not None:
            self._game_finished = True

    def on_button_press(self, row_ind, col_ind):
        if self._game_finished is True:
            return

        if self._game.board.is_square_empty(row_ind, col_ind):
            human_color = "yellow" if self._human_first is True else "purple"
            computer_color = "purple" if self._human_first is True else "yellow"

            self._buttons[row_ind][col_ind]["bg"] = human_color
            self.check_game_state(True, self._game.human_move(row_ind, col_ind, self._human_first))

            if self._game_finished is True:
                return

            finished, comp_row, comp_col = self._game.computer_move(not self._human_first)
            self._buttons[comp_row][comp_col]["bg"] = computer_color
            self.check_game_state(False, finished)

    def create_widgets(self):
        for i in range(self._game.board.row_size):
            row = []
            for j in range(self._game.board.col_size):
                button = tk.Button(self._window, bg="grey", width=4, height=2, activebackground="grey", text=" ",
                                   command=lambda row_ind=i, col_ind=j: self.on_button_press(row_ind, col_ind))
                button.grid(row=i, column=j)
                row.append(button)
            self._buttons.append(row)

    def run(self):
        message_box = askyesno(title="Start", message="Do you want to play first?")

        if message_box is True:
            self._human_first = True
        else:
            self._human_first = False

            computer_color = "purple" if self._human_first is True else "yellow"
            finished, comp_row, comp_col = self._game.computer_move(not self._human_first)
            self._buttons[comp_row][comp_col]["bg"] = computer_color
            self.check_game_state(False, finished)
        self._window.mainloop()
