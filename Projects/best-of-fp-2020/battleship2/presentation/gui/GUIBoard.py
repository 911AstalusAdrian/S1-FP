import tkinter as tk


class GUIBoard(tk.Frame):
    def __init__(self, parent, button_command=None):
        """
        Board types:
            inactive - no communication with the user
            shooting - the user is able to shoot the opponent board
            placement -  the user is able to place his own ships on the board
        :param parent:
        """
        super().__init__(parent)

        for i in range(11):
            self.grid_rowconfigure(i, weight=1)
        for i in range(11):
            self.grid_columnconfigure(i, weight=1)

        self.__buttons = []

        for i in range(10):
            tk.Label(self, text=i+1, height=20, width=20).grid(row=0, column=i+1, sticky="nesw")
            tk.Label(self, text=chr(ord('A') + i), height=20, width=20).grid(row=i+1, column=0, sticky="nesw")

        for i in range(10):
            for j in range(10):
                but = tk.Button(self, text='', relief=tk.RIDGE, background='gray')
                but.grid(row=i+1, column=j+1, sticky="nesw")

                if button_command is None:
                    button_command = self._on_click

                but.bind('<Button-1>', lambda e, row=i+1, col=j+1: button_command(row, col, e))
                self.__buttons.append(but)

    def _on_click(self, row, col, event):
        pass

    def display(self, values):
        for i in range(10):
            # print()
            for j in range(10):
                # print(values[i*10 + j], end=' ')
                self._make_colored_cell(i, j, values[i*10 + j])
        # print()

    def _make_colored_cell(self, row, col, value):
        """ Prints a cell in a given style """
        styles = {
            'normal': 'grey',
            'occupied': 'blue',
            'hit': 'yellow',
            'missed': 'red',
            'sunk': 'orange'
        }
        style = 'normal' if value == '0' else \
                'occupied' if value[0] in ['a', 'b', 'c', 'd', 's'] else \
                'hit' if value == '+' else \
                'missed' if value == '-' else \
                'sunk' if value == '*' else \
                'normal'

        button = self.__buttons[row * 10 + col]
        button.config(background=styles[style])

    def display_probability(self, values):
        for i in range(10):
            for j in range(10):
                cell = i * 10 + j
                color = '#%02x%02x%02x' % (255 - int(255*values[cell]), 255 - int(255*values[cell]), 255 - int(255*values[cell]))
                _color = '#%02x%02x%02x' % (int(255*values[cell]), int(255*values[cell]), int(255*values[cell]))
                button = self.__buttons[cell]
                button.config(background=color, foreground=_color, text=round(values[cell], 3))
