class GUI:

    def __init__(self):
        self.app = Tk()
        self.app.title('Connect4')
        self.app.resizable(width=False, height=False)
        self.board = Board()
        self.buttons = {}
        self.frame = Frame(self.app, borderwidth=1, relief="raised")
        self.tiles = {}

        self.frame.grid(row=1, column=0, columnspan=self.board.width)
        for x, y in self.board.fields:
            tile = Canvas(self.frame, width=60, height=50, bg="navy", highlightthickness=0)
            tile.grid(row=self.board.height - 1 - y, column=x)
            self.tiles[x, y] = tile
        handler = lambda: self.reset()
        self.restart = Button(self.app, command=handler, text='reset')
        self.restart.grid(row=2, column=0, columnspan=self.board.width, sticky="WE")
        self.update()

    def reset(self):
        self.board = Board()
        self.update()



