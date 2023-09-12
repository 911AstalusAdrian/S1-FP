# coding=UTF8
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from copy import deepcopy
from time import time
from Board.board import Board
from Game.game import *


class GUI:
    def __init__(self):
        self.board = Board()
        self._data = self.board.get_data()

        self.app = Tk()
        self.app.title('Connect4')
        self.app.resizable(width=False, height=False)
        self.app.geometry('667x250')
        self.difficulty = Entry(self.app, text="Choose a number representing difficulty between 1 and 5").get()
        self.canvas1 = Canvas(self.app, width=400, height=300, relief='raised')
        self.canvas1.pack()
        label1 = Label(self.app, text="Choose difficulty between 1 and 5")
        label1.config(font=('helvetica', 14))
        self.canvas1.create_window(200, 25, window=label1)
        button1 = Button(text='Set difficulty', command=self.getdifficulty, bg='brown', fg='white',
                            font=('helvetica', 9, 'bold'))
        self.canvas1.create_window(200, 180, window=button1)
        self.entry1 = Entry(self.app)
        self.canvas1.create_window(200, 140, window=self.entry1)
    def getdifficulty(self):
        self.difficulty = self.entry1.get()
        self.difficulty=int(self.difficulty)
        self.canvas1.destroy()
        self.start()
        return self.difficulty

    def start(self):
        self.button1 = Button(self.app, text="1", fg='red', bg='lightyellow', font=('Arial', 10, 'bold'),
                              command=self.move1, width=10)
        self.button2 = Button(self.app, text="2", fg='blue', bg='lightgreen', font=('Arial', 10, 'bold'),
                              command=self.move2, width=10)
        self.button3 = Button(self.app, text="3", fg='red', bg='lightyellow', font=('Arial', 10, 'bold'),
                              command=self.move3, width=10)
        self.button4 = Button(self.app, text="4", fg='blue', bg='lightgreen', font=('Arial', 10, 'bold'),
                              command=self.move4, width=10)
        self.button5 = Button(self.app, text="5", fg='red', bg='lightyellow', font=('Arial', 10, 'bold'),
                              command=self.move5, width=10)
        self.button6 = Button(self.app, text="6", fg='blue', bg='lightgreen', font=('Arial', 10, 'bold'),
                              command=self.move6, width=10)
        self.button7 = Button(self.app, text="7", fg='red', bg='lightyellow', font=('Arial', 10, 'bold'),
                              command=self.move7, width=10)
        self.button1.grid(row=1, column=0)
        self.button2.grid(row=1, column=1)
        self.button3.grid(row=1, column=2)
        self.button4.grid(row=1, column=3)
        self.button5.grid(row=1, column=4)
        self.button6.grid(row=1, column=5)
        self.button7.grid(row=1, column=6)

        self.button8 = Button(self.app, text='RESET', command=self.reset)
        self.button8.grid(row=11, column=3)
        for x in range(0, 6):
            for y in range(0, 7):
                self.e = Entry(self.app, textvariable=self._data[x][y], width=7, fg='blue',
                               font=('Arial', 16, 'bold'), justify='center')
                self.e.grid(row=2 + x, column=y, sticky="W")
                self.e.insert(END, self._data[x][y])
        self.update()


    def reset(self):
        if messagebox.askyesno('RESET', 'ARE YOU SURE?'):
            self._data = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            self.app.destroy()
            self.__init__()

    def aimove(self):
        b = self.board.get_data()
        s = Strategy()
        aiMove = s.MiniMaxAlphaBeta(b, self.difficulty, 'O')
        self.board.move(aiMove, 'O')
        if self.board.is_free(0) == False:
            self.button1['state'] = 'disabled'
        elif self.board.is_free(1) == False:
            self.button2['state'] = 'disabled'
        elif self.board.is_free(2) == False:
            self.button3['state'] = 'disabled'
        elif self.board.is_free(3) == False:
            self.button4['state'] = 'disabled'
        elif self.board.is_free(4) == False:
            self.button5['state'] = 'disabled'
        elif self.board.is_free(5) == False:
            self.button6['state'] = 'disabled'
        elif self.board.is_free(6) == False:
            self.button7['state'] = 'disabled'
        self.update()
        self.win('O')
        self.tie()

    def move1(self):

        self.board.move(0, 'X')
        self.update()
        if self.board.is_free(0) == False:
            self.button1['state'] = 'disabled'

        if self.win('X') is False:
            self.aimove()
        self.tie()

    def move2(self):
        self.board.move(1, 'X')
        self.update()
        if self.board.is_free(1) == False:
            self.button2['state'] = 'disabled'
        if self.win('X') is False:
            self.aimove()
        self.tie()

    def move3(self):
        self.board.move(2, 'X')
        self.update()
        if self.board.is_free(2) == False:
            self.button3['state'] = 'disabled'
        if self.win('X') is False:
            self.aimove()
        self.tie()

    def move4(self):
        self.board.move(3, 'X')
        self.update()
        if self.board.is_free(3) == False:
            self.button4['state'] = 'disabled'
        if self.win('X') is False:
            self.aimove()
        self.tie()

    def move5(self):
        self.board.move(4, 'X')
        self.update()
        if self.board.is_free(4) == False:
            self.button5['state'] = 'disabled'
        if self.win('X') is False:
            self.aimove()
        self.tie()

    def move6(self):
        self.board.move(5, 'X')
        self.update()
        if self.board.is_free(5) == False:
            self.button6['state'] = 'disabled'
        if self.win('X') is False:
            self.aimove()
        self.tie()

    def move7(self):
        self.board.move(6, 'X')
        self.update()
        if self.board.is_free(6) == False:
            self.button7['state'] = 'disabled'
        if self.win('X') is False:
            self.aimove()
        self.tie()

    def win(self, symbol):
        if self.board.checkWin(symbol) is True:
            self.button1['state'] = 'disabled'
            self.button2['state'] = 'disabled'
            self.button3['state'] = 'disabled'
            self.button4['state'] = 'disabled'
            self.button5['state'] = 'disabled'
            self.button6['state'] = 'disabled'
            self.button7['state'] = 'disabled'
            if symbol == 'O':
                messagebox.showinfo(str('WINNER'), str('THE COMPUTER WON!!!!!'))
            else:
                messagebox.showinfo(str('WINNER'), str('YOU WON!!!!!'))
            return True
        else:
            return False

    def tie(self):
        if self.board.is_full() == True:
            self.button1['state'] = 'disabled'
            self.button2['state'] = 'disabled'
            self.button3['state'] = 'disabled'
            self.button4['state'] = 'disabled'
            self.button5['state'] = 'disabled'
            self.button6['state'] = 'disabled'
            self.button7['state'] = 'disabled'
            messagebox.showinfo(str('NO WINNER'), str('TIE!!!!!'))

    def update(self):

        for x in range(0, 6):
            for y in range(0, 7):
                if self._data[x][y] == 'X':
                    color = 'blue'
                else:
                    color = 'red'
                self.e = Entry(self.app, textvariable=self._data[x][y], width=7, fg=color,
                               font=('Arial', 18, 'bold'), justify='center')

                self.e.grid(row=2 + x, column=y, sticky="W")
                self.e.delete(0, END)
                self.e.insert(0, self._data[x][y])

    def mainloop(self):
        self.app.mainloop()


# g = GUI()
# if __name__ == '__main__':
#     g.mainloop()
