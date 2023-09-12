import tkinter as tk
from tkinter import ttk


class GUIShipPosition(tk.Frame):

    def __init__(self, parent, text, button_command=None, position='', orientation=''):

        super(GUIShipPosition, self).__init__(parent)
        self._label = tk.Label(self, text=text)
        self._button = tk.Button(self, text="Preview", command=button_command)

        entry_frame = tk.Frame(self)
        tk.Label(entry_frame, text='Starting position: ').pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
        self._entry = tk.Entry(entry_frame)
        self._entry.insert(0, position)
        self._entry.pack(side=tk.RIGHT, expand=1, fill=tk.BOTH)

        comb_box_frame = tk.Frame(self)
        tk.Label(comb_box_frame, text='Orientation: ').pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
        self._comb_box = ttk.Combobox(comb_box_frame, values=['Horizontal', 'Vertical'])
        self._comb_box.pack(side=tk.RIGHT, expand=1, fill=tk.BOTH)
        self._comb_box.current(1 if orientation.lower() == 'vertical' else 0)

        self._error_label = tk.Label(self, text='', font='Default 7', foreground='red')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self._label.grid(row=0, column=0, columnspan=2, sticky='nesw')
        entry_frame.grid(row=1, column=0, sticky='nesw', padx=(0, 10))
        comb_box_frame.grid(row=1, column=1, sticky='nesw')
        self._button.grid(row=2, column=0, columnspan=2, sticky='nesw', padx=200, pady=(5, 0))
        self._error_label.grid(row=2, column=0, sticky='nw', padx=(5, 0), pady=(5, 0))

    @property
    def start_position(self):
        return self._entry.get()

    @property
    def orientation(self):
        return self._comb_box.get()

    @property
    def error(self):
        return self._error_label.cget('text')

    @error.setter
    def error(self, error_message):
        self._error_label.config(text=error_message)
