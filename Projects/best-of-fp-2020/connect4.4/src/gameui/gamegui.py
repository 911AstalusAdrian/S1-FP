import tkinter
from tkinter import messagebox

from player.computer import Computer
from utility.gameutility import GameCalculations


class GameGUI:
    def __init__(self, board, player1, player2):
        self.__board = board
        self.__players = [player1, player2]
        self.__turn = 0
        self.__available_columns = [column for column in range(board.columns)]
        self._set_board()

    PLAYER_COLOURS = ("yellow", "red")

    def play_human_turn(self, event):
        column = self.__entry_buttons.index(event.widget)
        line = self.__board.get_line_first_empty_cell_in_column(column)
        affected_cell = self.__players[self.__turn % 2].move(line, column)
        self.drop_piece(affected_cell)

    def play_computer_turn(self):
        affected_cell = self.__players[self.__turn % 2].move(self.__players[(self.__turn + 1) % 2].value)
        self.drop_piece(affected_cell)

    def prepare_next_turn(self, moved_cell):
        if moved_cell.line == 0:
            self.__available_columns.remove(moved_cell.column)
            self.disable_button(self.__entry_buttons[moved_cell.column])
        if GameCalculations.is_winner(self.__board, moved_cell):
            self.show_winner()
        elif GameCalculations.is_board_full(self.__board):
            self.show_draw()
        else:
            self.__turn += 1
            if type(self.__players[self.__turn % 2]) == Computer:
                self.play_computer_turn()
            else:
                for column in self.__available_columns:
                    self.enable_button(self.__entry_buttons[column])

    def drop_piece(self, cell, current_line=0):
        self.change_color(current_line, cell.column)
        if current_line != 0:
            self.__cells[current_line - 1][cell.column]["bg"] = "white"
        else:
            for button in self.__entry_buttons:
                self.disable_button(button)
        if current_line != cell.line:
            self.__window.after(100, self.drop_piece, cell, current_line + 1)
        else:
            self.__window.after(50, self.prepare_next_turn, cell)

    def change_color(self, line, column):
        self.__cells[line][column]["bg"] = self.PLAYER_COLOURS[self.__turn % 2]

    def show_winner(self):
        messagebox.showinfo(title="Winner!", message=self.__players[self.__turn % 2].name + " won the game!")
        for column in range(self.__board.columns):
            self.disable_button(self.__entry_buttons[column])

    @staticmethod
    def disable_button(button):
        button["state"] = "disabled"
        button["bg"] = "gray"
        button["text"] = ""
        button.unbind("<1>")

    def enable_button(self, button):
        button["state"] = "active"
        button["bg"] = "SystemButtonFace"
        button["text"] = "|\nV"
        button.bind("<1>", self.play_human_turn)

    def show_draw(self):
        messagebox.showinfo(title="Draw!", message="The game ended in a draw!")
        for column in range(self.__board.columns):
            self.disable_button(self.__entry_buttons[column])

    def _set_board(self):
        self.__window = tkinter.Tk()
        self.__window.title("Connect 4!")
        title_label = tkinter.Label(master=self.__window, text="Connect 4!", font=10, fg="grey")
        title_label.grid(row=0, columnspan=self.__board.lines)
        first_player_label = tkinter.Label(master=self.__window, text="First player: " + self.__players[0].name + ", " +
                                                                      type(self.__players[0]).__name__)
        first_player_label.grid(row=1, columnspan=self.__board.lines // 2)
        second_player_label = tkinter.Label(master=self.__window, text="Second player: " + self.__players[1].name + ", "
                                                                       + type(self.__players[1]).__name__)
        second_player_label.grid(row=1, column=self.__board.lines // 2, columnspan=self.__board.lines // 2)
        rules_label = tkinter.Label(master=self.__window, text="Press the button corresponding to the column you want "
                                                               "to put the piece in!")
        rules_label.grid(row=2, columnspan=self.__board.lines)
        self.__entry_buttons = []
        for i in range(self.__board.columns):
            self.__entry_buttons.append(tkinter.Button(master=self.__window, text="|\nV", width=10, height=2))
            self.__entry_buttons[i].bind("<1>", self.play_human_turn)
            self.__entry_buttons[i].grid(row=3, column=i)
        self.__cells = []
        for line in range(self.__board.lines):
            cell_line = []
            for column in range(self.__board.columns):
                cell_line.append(tkinter.Label(master=self.__window, bg="white", width=10, borderwidth=2, height=4,
                                               relief="solid"))
                cell_line[column].grid(row=line + 4, column=column)
            self.__cells.append(cell_line)
        if type(self.__players[0]) == Computer:
            self.play_computer_turn()
        self.__window.mainloop()
