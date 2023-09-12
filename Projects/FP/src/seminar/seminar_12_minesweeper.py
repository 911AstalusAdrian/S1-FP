"""
Minesweeper - https://www.google.com/search?q=play+minesweeper
"""
from texttable import Texttable
import random


class Minefield:
    def __init__(self, rows, cols, mines):
        self._rows = rows
        self._cols = cols
        self._mines = mines
        # Initialize matrix -> each cell represents the number of adjacent mines, or 9 if it is a mine
        # [0..8] number of adjacent mines
        # 9 - square hold a mine itself
        # 10 + (value) -> 10 means square is visible to player
        self._data = [[0 for col in range(self._cols + 2)] for row in range(self._rows + 2)]
        # Lay the mines
        self._lay_mines()

    def reveal(self, row, col):
        """
        Upper left corner is (1,1)
        """
        if row < 0 or row > self._rows or col < 0 or col > self._cols:
            return
        if self._data[row][col] > 9:
            return
            # raise Exception('Square already revealed')
        if self._data[row][col] == 9:
            # Stepped on a mine
            # TODO Create GameException class
            raise Exception('Game over!')

        # At least one adjacent mine, we reveal the square and are done
        if self._data[row][col] > 0 and self._data[row][col] < 9:
            self._data[row][col] += 10
            return

        # No adjacent mines, we reveal recursively
        self._data[row][col] = 10

        # Uncover locations recursively
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Don't recurse for itself
                if i != 0 or j != 0:
                    self.reveal(row + i, col + j)

    def _lay_mines(self):
        map = []
        for row in range(1, self._rows + 1):
            for col in range(1, self._cols + 1):
                map.append((row, col))

        mines = self._mines
        while mines > 0:
            # Choose the location of the next mine
            location = random.choice(map)
            row = location[0]
            col = location[1]
            # Remove location from list of eligible locations
            map.remove(location)
            # Actually place the mine (mines are marked with 9)
            self._data[row][col] = 9
            # Decrease the number of mines left to place
            mines -= 1

            # TODO Stop recursion at first and last row/column
            # Mark locations adjacent to this mine
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if self._data[row + i][col + j] != 9:
                        # Not a mine, so update the count of adjacent mines
                        self._data[row + i][col + j] += 1

    def __str__(self):
        t = Texttable()
        # Build table header
        header = [' ']
        for h in range(self._cols):
            header.append(chr(65 + h))
        t.header(header)

        # Add each table row
        for row in range(1, self._rows + 1):
            data = []

            for val in self._data[row][1:-1]:
                if val == 10:
                    data.append(' ')
                elif val > 10:
                    data.append(str(val - 10))
                else:
                    data.append('*')
            t.add_row([row] + data)
        return t.draw()


# TODO Add ui, handle excetions, figure out when the player cleared all mines
m = Minefield(8, 10, 5)
m.reveal(1, 1)
print(str(m))
