"""
Chomp - http://www.papg.com/chomp.html

Plan:
    1. Draw an empty board (with poison pill :) )
    2. Alternate moves (computer moves)
    3. UI, win/lose condition

Classes:
    Board
        - internal state of the board
        - move
            -> make a move on the board with X or O
            -> moves at A1 are forbidden
            -> return True iif at least 1 valid move remaining

    Strategy
        - computer "AI"
        - next_move(board) => return computer's next move

    Game
        - has a Board instance
        - human player move
        - computer move
            -> call a strategy for the computer player

    UI
        - has a Game instance
        - has a Strategy instance
        - alternate play between human and computer
"""
from texttable import Texttable
import random


class Board:
    def __init__(self):
        # TODO Have a variable number of rows and columns
        self._rows = 4
        self._columns = 5

        # Empty squares marked with None
        self._data = [[None for j in range(self._columns)] for i in range(self._rows)]
        # Mark the bad piece of chocolate
        self._data[0][0] = -1

        # Count the number of unoccupied squares remaining
        self._free_chocolate = self._rows * self._columns - 1

    @property
    def row_count(self):
        return self._rows

    @property
    def col_count(self):
        return self._columns

    def get(self, x, y):
        """
        Return symbol at position [x,y] on board
            -1       -> expired piece of chocolate
            None     -> empty square
            'X', 'O' -> symbols
            1        -> piece already eaten
        """
        return self._data[x][y]

    def is_free(self, x, y):
        return self.get(x, y) is None

    def move(self, x, y, symbol):
        if symbol not in ['X', 'O']:
            raise Exception('Bad symbol!')
        if x == 0 and y == 0:
            raise Exception('Cannot move to (0,0)')
        if self._data[y][x] == 1:
            raise Exception('Square already taken')

        # Mark the rest of the choco square to the right and below
        for row in range(y, self._rows):
            for col in range(x, self._columns):
                if self._data[row][col] not in ['X', 'O', 1]:
                    self._data[row][col] = 1
                    self._free_chocolate -= 1
        # Mark the new move on the board
        self._data[y][x] = symbol
        return self._free_chocolate > 0

    def __str__(self):
        t = Texttable()
        t.header(['A', 'B', 'C', 'D', 'E', ' '])
        for row in range(4):
            row_data = []

            for index in self._data[row]:
                if index is None:
                    row_data.append(' ')
                elif index == -1:
                    row_data.append('*')
                elif index == 'X' or index == 'O':
                    row_data.append(index)
                elif index == 1:
                    row_data.append('-')
            t.add_row(row_data + [row])

        return t.draw()


class Strategy:
    """
    Class decides computer's next move
    Basic implementation of the strategy design pattern - https://refactoring.guru/design-patterns/strategy
    """

    def next_move(self, board):
        """
        Return the computer's next move
        """
        # TODO Acts like an abstract base class
        raise Exception('Subclass strategy in order to implement computer play!')


class RandomMoveStrategy(Strategy):
    def next_move(self, board):
        """
        Make a random, but valid move
        """
        # Store possible moves here
        available_moves = []

        for col in range(board.col_count):  # 0 - 4
            for row in range(board.row_count):  # 0 - 3
                if board.is_free(row, col):
                    available_moves.append((row, col))
        # Pick one of the available moves
        move = random.choice(available_moves)
        # print(move)
        return board.move(move[1], move[0], 'O')


class Game:
    def __init__(self, strategy):
        self._board = Board()
        self._strategy = strategy

    @property
    def board(self):
        return self._board

    def human_move(self, x, y):
        # TODO Change so that human can also play with 'O'
        return self._board.move(x, y, 'X')

    def computer_move(self):
        return self._strategy.next_move(self._board)


class UI:
    def __init__(self):
        self._strategy = RandomMoveStrategy()
        self._game = Game(self._strategy)

    def read_human_move(self):
        # TODO Add error handling
        coord = input('where to play>')
        row = int(coord[1])
        # Calculate column index from character's ASCII code
        col = ord(coord[0].lower()) - 97
        return row, col

    def start(self):
        finished = False
        human_turn = True

        while not finished:
            # Print the board state
            print(self._game.board)

            if human_turn:
                coord = self.read_human_move()
                # print(coord)
                if self._game.human_move(coord[1], coord[0]) is False:
                    print('You wins!')
                    print(self._game.board)
                    return
            else:
                if self._game.computer_move() is False:
                    print('All you base are belong to us!')
                    print(self._game.board)
                    return
            human_turn = not human_turn


ui = UI()
ui.start()
